FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu24.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility \
    CUDA_HOME="/usr/local/cuda" \
    PATH="/usr/local/cuda/bin:${PATH}" \
    LD_LIBRARY_PATH="/.singularity.d/libs" \
    PYTHONUNBUFFERED=1

# First install basic dependencies and add deadsnakes PPA
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    git \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update

RUN apt-get update -y \
    && apt-get install -qy build-essential wget libfontconfig1

# Now install Python 3.13 and related packages
RUN apt-get install -y \
    python3.13 \
    python3.13-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install pip and set Python alternatives
RUN wget https://bootstrap.pypa.io/get-pip.py \
    && python3.13 get-pip.py \
    && rm get-pip.py \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.13 1

# Verify Python installation
RUN python --version && python -m pip --version

# Install JAX with CUDA 12 support
RUN python -m pip install --no-cache-dir \
    jax[cuda12]==0.7.0 \
    grain==0.2.12 \
    chex==0.1.90 \
    flax==0.11.1 \
    ml_dtypes==0.5.3 \
    optax==0.2.5 \
    orbax-checkpoint==0.11.23 \
    orbax-export==0.0.6 

# Install data processing and visualization libraries
RUN python -m pip install --no-cache-dir \
    numpy \
    scipy \
    pandas \
    matplotlib \
    seaborn \
    scikit-learn \
    ml_collections \
    ipython \
    ipykernel \
    jupyter_client \
    jupyter_core \
    tqdm \
    rich \
    humanize \
    simplejson \
    ipdb \
    pdbpp 

# Install additional JAX-related tools
RUN python -m pip install --no-cache-dir \
    treescope==0.1.10 \
    tensorstore==0.1.77

# Install development and monitoring tools
RUN python -m pip install --no-cache-dir \
    wandb \
    tensorboard

# Set environment variable for wandb API key
ENV WANDB_API_KEY=6128eac130254e0a9810543ff04f3c0696510b50
RUN wandb login $WANDB_API_KEY || echo "Warning: wandb login failed, you can login manually later"

# Create entrypoint script for Apptainer compatibility
RUN echo '#!/bin/bash\n\
# For Apptainer/Singularity compatibility\n\
if [ -d "/.singularity.d/libs" ]; then\n\
    export LD_LIBRARY_PATH="/.singularity.d/libs:${LD_LIBRARY_PATH}"\n\
fi\n\
exec "$@"' > /usr/local/bin/entrypoint.sh && \
    chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["bash"]

# Build and run commands:
# docker build -t nguyenvanhaibk92/x86_64_jaxaistack_cuda1281:v3.13 .
# docker push nguyenvanhaibk92/x86_64_jaxaistack_cuda1281:v3.13
# apptainer pull docker://nguyenvanhaibk92/x86_64_jaxaistack_cuda1281:v3.13
# apptainer shell --nv x86_64_jaxaistack_cuda1281_v3.13.sif
# 
# Inside container, test JAX GPU detection:
# python -c "import jax; print('JAX devices:', jax.devices())"