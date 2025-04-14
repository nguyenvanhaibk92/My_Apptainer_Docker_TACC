FROM nvidia/cuda:11.4.3-cudnn8-devel-ubuntu20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility \
    CUDA_HOME="/usr/local/cuda" \
    PATH="/usr/local/cuda/bin:${PATH}" \
    LD_LIBRARY_PATH="/usr/local/cuda/compat:/usr/local/cuda/lib64:${LD_LIBRARY_PATH}" \
    PYTHONUNBUFFERED=1

# Install basic dependencies and add deadsnakes PPA
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    git \
    build-essential \
    libfontconfig1 \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update

# Install Python 3.9 and its distutils package
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3.9-distutils \
    python3.9-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install pip
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9

# Set Python alternatives
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1

# Verify Python installation
RUN python --version && python -m pip --version

# Upgrade pip and setuptools
RUN python -m pip install --upgrade pip setuptools wheel

# Install NumPy first with specific version
RUN python -m pip install --no-cache-dir numpy==1.23.5

# Install core dependencies with specific versions
RUN python -m pip install --no-cache-dir \
    jax[cuda11_cudnn82]==0.3.4 \
    jaxlib==0.3.2+cuda11.cudnn82 -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html \
    flax==0.4.0 \
    optax==0.1.1 \
    clu==0.0.6

# Install TFDS dependencies with specific versions
RUN python -m pip install --no-cache-dir \
    tensorflow==2.8.0 \
    tensorflow-datasets==4.5.2

# Install additional tools and libraries with specific versions
RUN python -m pip install --no-cache-dir \
    pandas==1.4.1 \
    wandb==0.12.11 \
    ml-collections==0.1.1 \
    scikit-learn==1.0.2

# Set a working directory
WORKDIR /app

# Change ENTRYPOINT to CMD for more flexibility
CMD ["python"]

# Build command:
# docker build -t nguyenvanhaibk92/jaxaistackmaskae:2024.12.10 .
# Apptainer commands:
# apptainer pull docker://nguyenvanhaibk92/jaxaistackmaskae:2024.12.10
# apptainer shell --nv /work/08171/nvhai/ls6/apptainer/jaxaistackmaskae_2024.12.10.sif

# docker build -t nguyenvanhaibk92/jaxaistackmaskae:2024.12.10 .
# apptainer pull docker://nguyenvanhaibk92/jaxaistackmaskae:2024.12.10
# apptainer shell --nv /work/08171/nvhai/ls6/apptainer/jaxaistackmaskae_2024.12.10.sif
