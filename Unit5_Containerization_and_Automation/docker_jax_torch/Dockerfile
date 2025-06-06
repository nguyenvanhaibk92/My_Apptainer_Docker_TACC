FROM nvidia/cuda:12.6.0-cudnn-devel-ubuntu20.04
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

# Set environment variables for CUDA
ENV CUDA_HOME="/usr/local/cuda"
ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/compat:/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"

# Install compatible versions of requests and its dependencies
RUN python3.10 -m pip install requests==2.31.0 urllib3==1.26.18 chardet==4.0.0 ipywidgets

RUN python3.10 -m pip install --upgrade "jax[cuda12]==0.4.26"
RUN python3.10 -m pip install optax==0.2.2 Chex==0.1.86

RUN python3.10 -m pip install --no-deps flax==0.8.2
RUN python3.10 -m pip install typing-extensions PyYAML rich msgpack tensorstore 
RUN python3.10 -m pip install --no-deps orbax-checkpoint==0.6.4
RUN python3.10 -m pip install absl-py etils typing_extensions pyyaml nest_asyncio protobuf humanize fsspec importlib_resources zipp simplejson

RUN python3.10 -m pip install --upgrade git+https://github.com/matthias-wright/flaxmodels.git

# Install PyTorch
RUN python3.10 -m pip install torch==2.2.0 torchvision==0.17.0

# Install wandb and other common Python packages
RUN python3.10 -m pip install numpy==1.25.2 pandas matplotlib wandb rich seaborn tqdm tensorboard scikit-learn 

# Set environment variable for wandb API key # Login to wandb
ENV WANDB_API_KEY=6128eac130254e0a9810543ff04f3c0696510b50
RUN wandb login $WANDB_API_KEY

# Install TexLive with scheme-basic
RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz; \
	mkdir /install-tl-unx; \
	tar -xvf install-tl-unx.tar.gz -C /install-tl-unx --strip-components=1; \
    echo "selected_scheme scheme-full" >> /install-tl-unx/texlive.profile; \
	/install-tl-unx/install-tl -profile /install-tl-unx/texlive.profile; \
    rm -r /install-tl-unx; \
	rm install-tl-unx.tar.gz

ENV PATH="/usr/local/texlive/2024/bin/x86_64-linux/:${PATH}"

# docker build -t nguyenvanhaibk92/jaxtorch:v0.4.26 .
# apptainer pull docker://nguyenvanhaibk92/jaxtorch:v0.4.26
# apptainer shell --nv 
# docker build --platform linux/arm64 -t nguyenvanhaibk92/jaxwesley:1.0.1 .




