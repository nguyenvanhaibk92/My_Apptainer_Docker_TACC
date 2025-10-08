FROM nvidia/cuda:12.6.0-cudnn-devel-ubuntu20.04
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install graphics and rendering libraries (enhanced for PyVista/VTK)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    libxrender1 \
    libxext6 \
    libglu1-mesa \
    libsm6 \
    libice6 \
    libosmesa6 \
    libosmesa6-dev \
    mesa-utils \
    xvfb \
    x11-utils \
    libxrandr2 \
    libxss1 \
    libxcursor1 \
    libxcomposite1 \
    libasound2 \
    libxi6 \
    libxtst6 \
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

# Set PyVista/VTK environment variables for headless operation
ENV PYVISTA_OFF_SCREEN=true
ENV PYVISTA_USE_PANEL=false
ENV VTK_SILENCE_GET_VOID_POINTER_WARNINGS=1
ENV VTK_DISABLE_OPENGL_WARNING=1
ENV DISPLAY=""
ENV MESA_GL_VERSION_OVERRIDE=3.3
ENV GALLIUM_DRIVER=llvmpipe
ENV LIBGL_ALWAYS_INDIRECT=1
ENV LIBGL_ALWAYS_SOFTWARE=1

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

# Install VTK first with specific version that works well with headless rendering
RUN python3.10 -m pip install vtk==9.3.0

# Install other common Python packages
RUN python3.10 -m pip install numpy==1.25.2 pandas matplotlib wandb rich seaborn tqdm tensorboard scikit-learn

# Install PyVista with all optional dependencies for better compatibility
RUN python3.10 -m pip install "pyvista[all,trame]>=0.42.0"

# Install additional visualization tools
RUN python3.10 -m pip install plotly imageio pillow

# Create PyVista configuration directory and config file
RUN mkdir -p /root/.config/pyvista && \
    echo 'off_screen: true' > /root/.config/pyvista/config.yml && \
    echo 'use_panel: false' >> /root/.config/pyvista/config.yml && \
    echo 'theme: document' >> /root/.config/pyvista/config.yml && \
    echo 'window_size: [1024, 768]' >> /root/.config/pyvista/config.yml && \
    echo 'auto_close: true' >> /root/.config/pyvista/config.yml

# Create a startup script for PyVista configuration
RUN echo '#!/bin/bash\n\
# PyVista environment setup\n\
export PYVISTA_OFF_SCREEN=true\n\
export PYVISTA_USE_PANEL=false\n\
export VTK_SILENCE_GET_VOID_POINTER_WARNINGS=1\n\
export VTK_DISABLE_OPENGL_WARNING=1\n\
export DISPLAY=""\n\
export MESA_GL_VERSION_OVERRIDE=3.3\n\
export GALLIUM_DRIVER=llvmpipe\n\
export LIBGL_ALWAYS_INDIRECT=1\n\
export LIBGL_ALWAYS_SOFTWARE=1\n\
echo "PyVista environment configured for headless operation"\n\
' > /usr/local/bin/setup_pyvista.sh && \
    chmod +x /usr/local/bin/setup_pyvista.sh

# Set environment variable for wandb API key # Login to wandb
ENV WANDB_API_KEY=6128eac130254e0a9810543ff04f3c0696510b50
RUN wandb login $WANDB_API_KEY

# PyVista is now installed and configured for headless operation

# Install Jupyter and related packages for better notebook support
RUN python3.10 -m pip install jupyter jupyterlab ipykernel notebook

# # Install TexLive with scheme-basic
# RUN wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz; \
# 	mkdir /install-tl-unx; \
# 	tar -xvf install-tl-unx.tar.gz -C /install-tl-unx --strip-components=1; \
#     echo "selected_scheme scheme-full" >> /install-tl-unx/texlive.profile; \
# 	/install-tl-unx/install-tl -profile /install-tl-unx/texlive.profile; \
#     rm -r /install-tl-unx; \
# 	rm install-tl-unx.tar.gz

# ENV PATH="/usr/local/texlive/2025/bin/x86_64-linux/:${PATH}"

# Create a entrypoint script that sets up the environment
RUN echo '#!/bin/bash\n\
# Setup PyVista environment on container start\n\
export PYVISTA_OFF_SCREEN=true\n\
export PYVISTA_USE_PANEL=false\n\
export VTK_SILENCE_GET_VOID_POINTER_WARNINGS=1\n\
export VTK_DISABLE_OPENGL_WARNING=1\n\
export DISPLAY=""\n\
export MESA_GL_VERSION_OVERRIDE=3.3\n\
export GALLIUM_DRIVER=llvmpipe\n\
export LIBGL_ALWAYS_INDIRECT=1\n\
export LIBGL_ALWAYS_SOFTWARE=1\n\
\n\
# Execute the command passed to the container\n\
exec "$@"\n\
' > /entrypoint.sh && chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Set default command
CMD ["/bin/bash"]

# docker build -t nguyenvanhaibk92/jaxtorch_ls6_pyvista:v0.4.26 .
# apptainer pull docker://nguyenvanhaibk92/jaxtorch_ls6_pyvista:v0.4.26
# apptainer shell --nv jaxtorch_ls6_pyvista_v0.4.26.sif