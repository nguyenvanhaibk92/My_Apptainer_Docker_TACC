FROM nvidia/cuda:12.6.0-cudnn-devel-ubuntu24.04

ENV DEBIAN_FRONTEND=noninteractive

# First install basic dependencies and add deadsnakes PPA
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    git \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update

RUN apt-get update -q \
    && apt-get install -qy build-essential wget libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# Install TexLive with scheme-basic
RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz; \
	mkdir /install-tl-unx; \
	tar -xvf install-tl-unx.tar.gz -C /install-tl-unx --strip-components=1; \
    echo "selected_scheme scheme-full" >> /install-tl-unx/texlive.profile; \
	/install-tl-unx/install-tl -profile /install-tl-unx/texlive.profile; \
    rm -r /install-tl-unx; \
	rm install-tl-unx.tar.gz

ENV PATH="/usr/local/texlive/2024/bin/aarch64-linux:${PATH}"

WORKDIR /work

# docker build --platform linux/amd64 -t nguyenvanhaibk92/jaxaistack_latex:2024.12.10 .
# apptainer pull docker://nguyenvanhaibk92/jaxaistack_latex:2024.12.10
# apptainer shell --nv jaxaistack


