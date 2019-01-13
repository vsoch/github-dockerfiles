FROM ubuntu:15.10
MAINTAINER ITOH Akihiko

RUN apt-get update
RUN apt-get upgrade -y

USER root

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get install -yq --no-install-recommends \
    python \
    openssl \
    libssl-dev \
    automake \
    build-essential \
    curl \
    wget \
    git \
    vim \
    emacs \
    zsh \
    screen \
    tmux \
    silversearcher-ag \
    tcpdump \
    nmap \
    htop \
    mosh \
    sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

RUN useradd -s /bin/zsh -m dev
RUN echo 'dev ALL=(ALL:ALL) NOPASSWD:ALL' | tee /etc/sudoers.d/dev
WORKDIR /home/dev
ENV HOME /home/dev
USER dev
