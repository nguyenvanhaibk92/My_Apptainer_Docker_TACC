# Start with Ubuntu as the base image
FROM ubuntu:latest

# Update packages and install some colorful utilities
RUN apt-get update && apt-get install -y \
    bash-completion \
    colorized-logs \
    zsh \
    zsh-syntax-highlighting \
    git \
    nano \
    curl \
    wget \
    lolcat \
    figlet \
    && rm -rf /var/lib/apt/lists/*

# Set up a colorful bash prompt
RUN echo 'export PS1="\[\033[38;5;135m\]\u\[\033[38;5;128m\]@\[\033[38;5;39m\]\h\[\033[00m\]:\[\033[38;5;34m\]\w\[\033[00m\]\$ "' >> /root/.bashrc

# Add color aliases
RUN echo 'alias ls="ls --color=auto"' >> /root/.bashrc && \
    echo 'alias grep="grep --color=auto"' >> /root/.bashrc && \
    echo 'alias diff="diff --color=auto"' >> /root/.bashrc

# Add a welcome message
RUN echo 'figlet "Colorful Terminal" | lolcat' >> /root/.bashrc

# Set working directory
WORKDIR /app

# Command to run when container starts
CMD ["/bin/bash"]


# docker build -t nguyenvanhaibk92/zsh_test .
# apptainer pull docker://nguyenvanhaibk92/zsh_test

