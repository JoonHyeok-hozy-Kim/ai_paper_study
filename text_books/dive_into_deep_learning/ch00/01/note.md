* [Back to Dive into Deep Learning](../../main.md)

# Installation

#### 1. Installing Miniconda
1. Install Python 3.xx
2. Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/).
   - Open Anaconda Prompt
   - Set Few things for conda
     - Check version
       ```
       conda --version
     - Update
       ```
       conda update conda
       ```
     - Create a new environment
       ```
       conda create --name d2l python=3.12 -y
       ```
     - Activate the environment
       ```
       conda activate d2l
       ```

#### 2. Install the Deep Learning Framework
- Options are...
  - PyTorch (v)
  - MXNet
  - JAX
  - TensorFlow

- How to...
  - Install [CUDA](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local).
  - Install Pytorch.
    ```
    pip install torch==2.0.0 torchvision==0.15.1
    ```



<br>

* [Back to Dive into Deep Learning](../../main.md)