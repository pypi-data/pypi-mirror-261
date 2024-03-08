#include <torch/extension.h>
#include <cuda_runtime.h>
#include <cstdint>
#include <ATen/ATen.h>
#include <ATen/Context.h>
#include <ATen/cuda/CUDAContext.h>

template<typename T>
constexpr T constexpr_max(T a, T b) {
    return (a > b) ? a : b;
}

template <int InputChannels, int InputLength, int Padding, int KernelSize, int ChannelsPerThread>
__global__ void conv1d(float *d_input, float *d_weight, float *d_bias, float *d_output)
{
    //define constants
    constexpr int SharedMemLength = constexpr_max(InputLength, KernelSize);
    const int blockId = blockIdx.x;
    const int tdIdx = threadIdx.x;
    const int laneIdx = threadIdx.x % warpSize;
    const int warpIdx = threadIdx.x / warpSize;

    const int input_accesses_per_thread = (InputChannels * InputLength)/(4 * blockDim.x); 
    const int weight_accesses_per_thread = (InputChannels * KernelSize)/(blockDim.x); 
    const int weight_offset = blockId * InputChannels * KernelSize;
    const int padded_input_length = InputLength + Padding * 2;
    const int shared_mem_offset_denom = (InputLength * ChannelsPerThread) < 32 ? 32 : (InputLength * ChannelsPerThread);


    //static mem allocations
    float regInput[padded_input_length*ChannelsPerThread] = {0};
    float regFilter[KernelSize*ChannelsPerThread];
    __shared__ float shared_mem[InputChannels * SharedMemLength];

    //load input from global memory into shared memory 
    for (int channelIndex = 0; channelIndex < input_accesses_per_thread; ++channelIndex){
        int td_offset = 4 * (channelIndex * blockDim.x + tdIdx); 
        int smem_offset = td_offset/shared_mem_offset_denom; 
        float4 data = *reinterpret_cast<float4*>(&d_input[td_offset]);
        shared_mem[td_offset + smem_offset + 0] = data.x; 
        shared_mem[td_offset + smem_offset + 1] = data.y; 
        shared_mem[td_offset + smem_offset + 2] = data.z; 
        shared_mem[td_offset + smem_offset + 3] = data.w; 
    }

    __syncthreads(); 

    //load input from shared memory into thread registers
    for (int channelIndex = 0; channelIndex < ChannelsPerThread; ++channelIndex){
        for (int colIndex = 0; colIndex < InputLength; ++colIndex){
            int regIndex = Padding + channelIndex * padded_input_length + colIndex;
            int sharedMemIndex = InputLength * (ChannelsPerThread * tdIdx + channelIndex) + colIndex;
            int smem_offset = sharedMemIndex/shared_mem_offset_denom; 
            regInput[regIndex] = shared_mem[sharedMemIndex + smem_offset];
        }
    }

    __syncthreads(); 

    //load weights from global memory into shared memory 
    for (int channelIndex = 0; channelIndex < weight_accesses_per_thread; ++channelIndex){
        int td_offset = (channelIndex * blockDim.x) + tdIdx;
        shared_mem[td_offset] = d_weight[td_offset + weight_offset];
    }

    __syncthreads(); 

    //load weights from shared memory to thread registers
    for (int channelIndex = 0; channelIndex < ChannelsPerThread; ++channelIndex){
        for (int colIdx = 0; colIdx < KernelSize; ++colIdx){
            int regIndex = channelIndex * KernelSize + colIdx;
            int sharedMemIndex = KernelSize * (ChannelsPerThread * tdIdx + channelIndex) + colIdx;
            regFilter[regIndex] = shared_mem[sharedMemIndex];
        }
    }

    //outer loop iterates over each element in output vector
    for (int tileIdx = 0; tileIdx < InputLength; ++tileIdx){
        float res = 0.0;
        
        //inner loop performs dot product over all kernel positions and accumulates results
        for(int dotIdx = 0; dotIdx < KernelSize; ++dotIdx){
            for(int channelIndex = 0; channelIndex < ChannelsPerThread; ++channelIndex){
                res += regInput[tileIdx + dotIdx + (channelIndex * padded_input_length)] * regFilter[dotIdx + (channelIndex * KernelSize)];
            }
        }
        for (int offset = warpSize / 2; offset > 0; offset /= 2) {
            res += __shfl_down_sync(0xffffffff, res, offset);
        }
        
        if (threadIdx.x == 0) {
            atomicAdd(&d_output[blockIdx.x * InputLength + tileIdx], d_bias[blockIdx.x]);
        }

        if (laneIdx == 0) {
            atomicAdd(&d_output[blockIdx.x * InputLength + tileIdx], res);
        }
    }
}

template <int CHUNK_SIZE>
__global__ void parallelGroupNormMishKernel(float* d_input, float* d_output, float* d_weights, float* d_bias, const int input_length) {
    const int tid = threadIdx.x;
    const int bid = blockIdx.x;
    __shared__ float sharedSum[CHUNK_SIZE]; // Shared memory for storing sum and sum of squares

    //1. Load data into shared memory
    float dataValue = d_input[bid * CHUNK_SIZE + tid]; 
    sharedSum[tid] = dataValue;
    __syncthreads();

    //2. Reduction to compute total sum (mean calculation)
    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {
        if (tid < stride) {
            sharedSum[tid] += sharedSum[tid + stride];
        }
        __syncthreads();
    }

    //3. calculates the square of the difference between the value for the current thread and the mean for the group
    float mean = sharedSum[0] / CHUNK_SIZE;
    float diff = dataValue - mean;
    sharedSum[tid] = diff * diff; //save the squared difference in shared memory
    __syncthreads();

    //4. Reduction to compute total sum of squares (variance calculation)
    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {
        if (tid < stride) {
            sharedSum[tid] += sharedSum[tid + stride];
        }
        __syncthreads();
    }

    //5. calculates the normalized value
    float variance = sharedSum[0] / CHUNK_SIZE;
    int global_td = bid * CHUNK_SIZE + tid;
    int weight_bias_idx = global_td / input_length;
    float invStdDev = rsqrtf(variance + 1e-5); // Using epsilon = 1e-5
     float normVal = (dataValue - mean) * invStdDev;
    
    //6. scale normalized value by weight and bias
    float weightedNormVal = normVal * d_weights[weight_bias_idx] + d_bias[weight_bias_idx];

    //7. apply Mish activation using CUDA special functions and store the result in global memory
    float mishVal = weightedNormVal * tanhf(log1pf(expf(weightedNormVal)));
    d_output[bid * CHUNK_SIZE + tid] = mishVal;
}

torch::Tensor conv1d_gnm_cuda(
    torch::Tensor& input,
    torch::Tensor& conv1d_weight_tensor,
    torch::Tensor& conv1d_bias_tensor,
    torch::Tensor& gnm_weight_tensor,
    torch::Tensor& gnm_bias_tensor,
    int output_channels,
    int padding,
    int kernel_size,
    const int channelsPerThread
){
    input = input.contiguous(); 
    conv1d_weight_tensor = conv1d_weight_tensor.contiguous();
    conv1d_bias_tensor = conv1d_bias_tensor.contiguous();
    gnm_weight_tensor = gnm_weight_tensor.contiguous();
    gnm_bias_tensor = gnm_bias_tensor.contiguous();

    float* d_input = input.data_ptr<float>();
    float* d_conv1d_weight = conv1d_weight_tensor.data_ptr<float>();
    float* d_conv1d_bias = conv1d_bias_tensor.data_ptr<float>();
    float* d_gnm_weight = gnm_weight_tensor.data_ptr<float>();
    float* d_gnm_bias = gnm_bias_tensor.data_ptr<float>();

    const int input_channels = input.size(1);
    const int input_length = input.size(2);
    const int output_length = input_length - kernel_size + 1 + 2 * padding;
    const int chunk_size = (output_channels * input_length) / 8; 

    const dim3 conv1d_blocks(output_channels, 1, 1);
    
    const dim3 gnm_blocks(8, 1, 1);
    const dim3 gnm_threads(chunk_size, 1, 1);

    auto options = input.options();
    auto conv1d_out = torch::zeros({1, output_channels, output_length}, options);
    auto gnm_out = torch::empty({1, output_channels, output_length}, options);
    cudaStream_t stream = at::cuda::getCurrentCUDAStream();

    if (input_channels == 2 && input_length == 16) {
        const dim3 conv1d_threads(input_channels / 1, 1, 1);
        conv1d<2, 16, 2, 5, 1><<<conv1d_blocks, conv1d_threads, 0, stream>>>(d_input, d_conv1d_weight, d_conv1d_bias, conv1d_out.data_ptr<float>());
    } else if (input_channels == 512 && input_length == 4) {
        const dim3 conv1d_threads(input_channels / 8, 1, 1);
        conv1d<512, 4, 2, 5, 8><<<conv1d_blocks, conv1d_threads, 0, stream>>>(d_input, d_conv1d_weight, d_conv1d_bias, conv1d_out.data_ptr<float>());
    } else if (input_channels == 256 && input_length == 16) {
        const dim3 conv1d_threads(input_channels / 2, 1, 1);
        conv1d<256, 16, 2, 5, 2><<<conv1d_blocks, conv1d_threads, 0, stream>>>(d_input, d_conv1d_weight, d_conv1d_bias, conv1d_out.data_ptr<float>());
    } else if (input_channels == 512 && input_length == 8) {
        const dim3 conv1d_threads(input_channels / 4, 1, 1);
        conv1d<512, 8, 2, 5, 4><<<conv1d_blocks, conv1d_threads, 0, stream>>>(d_input, d_conv1d_weight, d_conv1d_bias, conv1d_out.data_ptr<float>());
    } else if (input_channels == 1024 && input_length == 4) {
        const dim3 conv1d_threads(input_channels / 4, 1, 1);
        conv1d<1024, 4, 2, 5, 4><<<conv1d_blocks, conv1d_threads, 0, stream>>>(d_input, d_conv1d_weight, d_conv1d_bias, conv1d_out.data_ptr<float>());
    } else if (input_channels == 256 && input_length == 8) {
        const dim3 conv1d_threads(input_channels / 2, 1, 1);
        conv1d<256, 8, 2, 5, 2><<<conv1d_blocks, conv1d_threads, 0, stream>>>(d_input, d_conv1d_weight, d_conv1d_bias, conv1d_out.data_ptr<float>());
    } else if (input_channels == 1024 && input_length == 4) {
        const dim3 conv1d_threads(input_channels / 4, 1, 1);
        conv1d<1024, 8, 2, 5, 4><<<conv1d_blocks, conv1d_threads, 0, stream>>>(d_input, d_conv1d_weight, d_conv1d_bias, conv1d_out.data_ptr<float>());
    } else if (input_channels == 2048 && input_length == 4) {
        const dim3 conv1d_threads(input_channels / 4, 1, 1);
        conv1d<2048, 4, 2, 5, 4><<<conv1d_blocks, conv1d_threads, 0, stream>>>(d_input, d_conv1d_weight, d_conv1d_bias, conv1d_out.data_ptr<float>());
    }

    cudaError_t conv1d_err = cudaGetLastError();
    if (conv1d_err != cudaSuccess) {
        throw std::runtime_error("CUDA error: " + std::string(cudaGetErrorString(conv1d_err)));
    }
    
    if (chunk_size == 512){
        parallelGroupNormMishKernel<512><<<gnm_blocks, gnm_threads, 0, stream>>>(conv1d_out.data_ptr<float>(), gnm_out.data_ptr<float>(), d_gnm_weight, d_gnm_bias, output_length);
    }
    else if (chunk_size == 256){
        parallelGroupNormMishKernel<256><<<gnm_blocks, gnm_threads, 0, stream>>>(conv1d_out.data_ptr<float>(), gnm_out.data_ptr<float>(), d_gnm_weight, d_gnm_bias, output_length);
    }
    else if (chunk_size == 1024){
        parallelGroupNormMishKernel<1024><<<gnm_blocks, gnm_threads, 0, stream>>>(conv1d_out.data_ptr<float>(), gnm_out.data_ptr<float>(), d_gnm_weight, d_gnm_bias, output_length);
    }
    else if (chunk_size == 4){
        parallelGroupNormMishKernel<4><<<gnm_blocks, gnm_threads, 0, stream>>>(conv1d_out.data_ptr<float>(), gnm_out.data_ptr<float>(), d_gnm_weight, d_gnm_bias, output_length);
    }

    cudaError_t gnm_err = cudaGetLastError();
    if (gnm_err != cudaSuccess) {
        throw std::runtime_error("CUDA error: " + std::string(cudaGetErrorString(gnm_err)));
    }
    
    return gnm_out;
}
