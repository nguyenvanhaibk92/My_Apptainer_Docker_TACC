FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Add deadsnakes PPA
RUN add-apt-repository ppa:deadsnakes/ppa

# Install Python 3.10
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3.10-distutils \
    python3.10-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install pip for Python 3.10
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3.10 get-pip.py && \
    rm get-pip.py

# Verify Python and pip versions
RUN python3.10 --version && python3.10 -m pip --version

# Set Python 3.10 as the default python3
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# Optional: Set Python 3.10 as the default python
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1

ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility

# Set environment variables for CUDA 12.8
ENV CUDA_HOME="/usr/local/cuda"
ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/compat:/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"

# Install compatible versions of requests and its dependencies
RUN python3.10 -m pip install requests==2.31.0 urllib3==1.26.18 chardet==4.0.0 ipywidgets

# Install PyTorch with CUDA 12.4 support (latest stable for CUDA 12.x)
# Note: PyTorch doesn't have specific CUDA 12.8 builds yet, but 12.4 is forward compatible
RUN python3.10 -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

# Install additional packages to match your environment
RUN python3.10 -m pip install \
    numpy==1.25.2 \
    pandas==2.2.3 \
    matplotlib==3.10.3 \
    wandb==0.19.11 \
    rich==14.0.0 \
    seaborn==0.13.2 \
    tqdm==4.67.1 \
    tensorboard==2.19.0 \
    scikit-learn==1.6.1 \
    scipy==1.15.3 \
    scikit-image==0.25.2 \
    opencv-python==4.11.0.86 \
    pillow==11.2.1 \
    h5py==3.13.0 \
    networkx==3.4.2 \
    timm==1.0.15 \
    huggingface-hub==0.31.2 \
    safetensors==0.5.3

RUN python3.10 -m pip install \
    pytorch-lightning\
    torchmetrics\
    torch-geometric\
    torchinfo
    
# Install Jupyter and development tools
RUN python3.10 -m pip install \
    jupyter==1.1.1 \
    jupyterlab==4.4.2 \
    ipython==8.36.0 \
    ipdb==0.13.13 \
    pdbpp==0.11.6 

RUN python3.10 -m pip install e3nn==0.5.6

# Set environment variable for wandb API key and login to wandb
ENV WANDB_API_KEY=6128eac130254e0a9810543ff04f3c0696510b50
RUN wandb login $WANDB_API_KEY



# Updated build commands:
# docker build --platform linux/arm64 -t nguyenvanhaibk92/pytorch_cuda128_vista:v2.6.0 .
# apptainer pull docker://nguyenvanhaibk92/pytorch_cuda128_vista:v2.6.0
# apptainer shell --nv pytorch_cuda128_vista_v2.6.0.sif

# docker build --platform linux/arm64 -t nguyenvanhaibk92/pytorch_cuda128_vista:v2.7.1 .
# apptainer pull docker://nguyenvanhaibk92/pytorch_cuda128_vista:v2.7.1
# apptainer shell --nv pytorch_cuda128_vista_v2.7.1.sif