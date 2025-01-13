FROM nvidia/cuda:12.6.0-cudnn-devel-ubuntu20.04

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
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update

FROM qmcgaw/latexdevcontainer
RUN tlmgr install lastpage

