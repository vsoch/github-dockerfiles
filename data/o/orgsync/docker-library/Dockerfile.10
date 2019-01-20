FROM debian:jessie
MAINTAINER Joshua Griffith <joshua@orgsync.com>

RUN echo "nameserver 8.8.8.8\nnameserver 8.8.4.4" > /etc/resolv.conf
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y \
        wget \
        sudo \
        curl \
        procps \
        htop \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean
