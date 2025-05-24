FROM nvidia/cuda-ppc64le:11.4.0-devel-ubi8

# Build arguments
ARG PYTHON_VERSION=3.10.12
ARG CMAKE_VERSION=3.25.2
ARG CMAKE_BASE_VERSION=3.25
ARG GCC_VERSION=9.5.0

# Set environment variables
ENV PYTHON_VERSION=${PYTHON_VERSION}
ENV CMAKE_VERSION=${CMAKE_VERSION}
ENV GCC_VERSION=${GCC_VERSION}

# Install system dependencies
RUN dnf update -y && \
    dnf install -y \
    git \
    wget \
    curl \
    gcc \
    gcc-c++ \
    make \
    openssl-devel \
    bzip2-devel \
    libffi-devel \
    zlib-devel \
    readline-devel \
    sqlite-devel \
    xz-devel \
    tk-devel \
    gdbm-devel \
    libnsl2-devel \
    libuuid-devel \
    libtirpc-devel \
    expat-devel \
    ncurses-devel \
    bison \
    flex && \
    dnf clean all

# Install Python 3.10 from source
WORKDIR /tmp
RUN curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar -xzf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure \
        --enable-optimizations \
        --enable-shared \
        --with-system-ffi \
        --with-computed-gotos \
        --enable-loadable-sqlite-extensions && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && \
    rm -rf Python-${PYTHON_VERSION}.tgz Python-${PYTHON_VERSION}

# Create python3.10 symlinks
RUN ln -sf /usr/local/bin/python3.10 /usr/local/bin/python3 && \
    ln -sf /usr/local/bin/python3.10 /usr/local/bin/python && \
    ln -sf /usr/local/bin/pip3.10 /usr/local/bin/pip3 && \
    ln -sf /usr/local/bin/pip3.10 /usr/local/bin/pip

# Update PATH
ENV PATH="/usr/local/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/lib:${LD_LIBRARY_PATH}"

# Upgrade pip and install basic Python packages
RUN python3.10 -m pip install --upgrade pip setuptools wheel

# Install CMake from source
WORKDIR /tmp
RUN wget https://cmake.org/files/v${CMAKE_BASE_VERSION}/cmake-${CMAKE_VERSION}.tar.gz && \
    tar zxf cmake-${CMAKE_VERSION}.tar.gz && \
    cd cmake-${CMAKE_VERSION} && \
    ./bootstrap --parallel=$(nproc) && \
    make -j$(nproc) && \
    make install && \
    cd .. && \
    rm -rf cmake-${CMAKE_VERSION}.tar.gz cmake-${CMAKE_VERSION}

# Install newer GCC
WORKDIR /tmp
RUN git clone --depth 1 --branch releases/gcc-${GCC_VERSION} https://gcc.gnu.org/git/gcc.git gcc-${GCC_VERSION} && \
    cd gcc-${GCC_VERSION} && \
    ./contrib/download_prerequisites && \
    cd .. && \
    mkdir gcc-build && \
    cd gcc-build && \
    ../gcc-${GCC_VERSION}/configure \
        --prefix=/usr/local \
        --enable-languages=c,c++,fortran \
        --disable-multilib \
        --enable-shared \
        --enable-threads=posix \
        --enable-__cxa_atexit \
        --enable-clocale=gnu \
        --enable-gnu-unique-object \
        --enable-linker-build-id \
        --with-system-zlib \
        --disable-libunwind-exceptions \
        --enable-gnu-indirect-function \
        --with-tune=power9 \
        --with-cpu=power9 \
        --build=powerpc64le-redhat-linux && \
    make -j$(nproc) && \
    make install && \
    cd .. && \
    rm -rf gcc-${GCC_VERSION} gcc-build

# Update environment for new GCC
ENV CC=/usr/local/bin/gcc
ENV CXX=/usr/local/bin/g++
ENV PATH="/usr/local/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/lib64:/usr/local/lib:${LD_LIBRARY_PATH}"

# Install build dependencies for PyTorch
RUN python3.10 -m pip install \
    ninja \
    pyyaml \
    setuptools \
    cffi \
    typing_extensions \
    future \
    six \
    requests \
    psutil \
    cmake

# Set PyTorch build environment variables
ENV CMAKE_PREFIX_PATH="/usr/local"
ENV TORCH_CUDA_ARCH_LIST="7.0;7.5;8.0;8.6"
ENV CUDA_HOME="/usr/local/cuda"
ENV CUDNN_LIB_DIR="/usr/lib64"
ENV CUDNN_INCLUDE_DIR="/usr/include"
ENV NCCL_ROOT="/usr"
ENV USE_CUDA=1
ENV USE_CUDNN=1
ENV USE_NCCL=1
ENV USE_SYSTEM_NCCL=1
ENV USE_OPENCV=0
ENV BUILD_TEST=0
ENV BUILD_CAFFE2_OPS=1
ENV USE_FBGEMM=0
ENV USE_MKLDNN=0
ENV USE_NNPACK=0
ENV USE_QNNPACK=0
ENV USE_DISTRIBUTED=1
ENV USE_TENSORRT=0
ENV BUILD_BINARY=0
ENV USE_NUMPY=1

# Install PyTorch and TorchVision
RUN python3.10 -m pip install torch==2.2.0 torchvision==0.17.0

# Install wandb and other common Python packages
RUN python3.10 -m pip install \
    numpy==1.25.2 \
    pandas \
    matplotlib \
    wandb \
    rich \
    seaborn \
    tqdm \
    tensorboard \
    scikit-learn \
    e3nn \
    timm \
    torch-geometric

# Set environment variable for wandb
ENV WANDB_API_KEY=""

# Clean up
RUN rm -rf /tmp/* && \
    dnf clean all

# Set working directory
WORKDIR /workspace

# Verify installations
RUN python3.10 -c "import torch; print(f'PyTorch version: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}'); print(f'CUDA version: {torch.version.cuda}'); print(f'cuDNN version: {torch.backends.cudnn.version()}')" && \
    python3.10 -c "import torchvision; print(f'TorchVision version: {torchvision.__version__}')" && \
    python3.10 -c "import numpy; print(f'NumPy version: {numpy.__version__}')" && \
    python3.10 -c "import wandb; print(f'WandB version: {wandb.__version__}')"

# Default command
CMD ["/bin/bash"]