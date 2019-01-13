FROM ubuntu:xenial-20160525
MAINTAINER Akiyoshi Sakaguchi <autumngoodluck@gmail.com>

ENV ATOM_VERSION 1.7.4

RUN DEBIAN_FRONTEND=noninteractive \
  sed -i.bak -e 's;http://archive.ubuntu.com/ubuntu/;http://ftp.jaist.ac.jp/pub/Linux/ubuntu/;' /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
       gconf2 \
       git \
       gvfs-bin \
       libasound2 \
       libgtk2.0-0 \
       libnotify4 \
       libnss3 \
       libxtst6 \
       xdg-utils \
  && rm -rf /var/lib/apt/lists/*

RUN curl -SL https://github.com/atom/atom/releases/download/v${ATOM_VERSION}/atom-amd64.deb -o /tmp/atom-amd64.deb \
  && dpkg --install /tmp/atom-amd64.deb \
  && rm -rf /tmp/atom-amd64.deb
