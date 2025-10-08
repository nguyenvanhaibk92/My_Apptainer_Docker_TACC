FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility \
    CUDA_HOME="/usr/local/cuda" \
    PATH="/usr/local/cuda/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/cuda/compat:/usr/local/cuda/lib64:${LD_LIBRARY_PATH}" \
    PYTHONUNBUFFERED=1
    
# First install basic dependencies and add deadsnakes PPA
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    git \
    tmux \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update

RUN apt-get update -y \
    && apt-get install -qy build-essential wget libfontconfig1

# Now install Python 3.10 and related packages
RUN apt-get install -y \
    python3.10 \
    python3.10-distutils \
    python3.10-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
    # Install pip and set Python alternative
RUN wget https://bootstrap.pypa.io/get-pip.py \
    && python3.10 get-pip.py \
    && rm get-pip.py \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1

# Verify Python installation
RUN python --version && python -m pip --version

# Install core dependencies
RUN python -m pip install --no-cache-dir \
    jax[cuda12]==0.5.3 \
    chex==0.1.89 \
    flax==0.10.5 \
    ml_dtypes==0.5.1 \
    optax==0.2.4 \
    orbax-checkpoint==0.11.12 \
    orbax-export==0.0.6

# Install TFDS dependencies
RUN python -m pip install --no-cache-dir \
    tensorflow==2.19.0 \
    tensorflow_datasets==4.9.8

# Install Grain
RUN python -m pip install --no-cache-dir \
    grain==0.2.7

# Install development dependencies
RUN python -m pip install --no-cache-dir \
    pytest \
    pytest-xdist

# Install additional tools and libraries
RUN python -m pip install --no-cache-dir \
    requests==2.31.0 \
    urllib3==1.26.18 \
    chardet==4.0.0 \
    ipywidgets \
    pandas \
    matplotlib \
    wandb \
    rich \
    seaborn \
    tqdm \
    tensorboard \
    datasets \
    ml_collections \
    plotly

RUN python -m pip install clu

# Set environment variable for wandb API key # Login to wandb
ENV WANDB_API_KEY=6128eac130254e0a9810543ff04f3c0696510b50
RUN wandb login $WANDB_API_KEY 


# docker build --platform linux/arm64 -t nguyenvanhaibk92/jaxaistack_vista_cuda128.1:2024.12.10 .
# apptainer pull docker://nguyenvanhaibk92/jaxaistack_vista_cuda128.1:2024.12.10
# apptainer shell --nv jaxaistack_vista_cuda128.1


