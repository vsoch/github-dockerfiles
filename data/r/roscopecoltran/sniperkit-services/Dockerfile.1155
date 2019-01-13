FROM deepcortex/scala-ubuntu:latest

ENV ZMQ_VERSION 4.2.1

RUN apt-get -y update && \
    apt-get install -y --fix-missing \
    build-essential make pkg-config libtool autoconf automake git && \
    cd /opt && \
    wget https://github.com/zeromq/libzmq/releases/download/v$ZMQ_VERSION/zeromq-$ZMQ_VERSION.tar.gz && \
    tar -zxf zeromq-$ZMQ_VERSION.tar.gz && \
    rm zeromq-$ZMQ_VERSION.tar.gz && \
    cd /opt/zeromq-$ZMQ_VERSION && \
    ./autogen.sh && ./configure && make -j 4 && \
    make check && make install && ldconfig && \
    cd /opt && \
    rm -rf zeromq-$ZMQ_VERSION && rm -rf jzmq && \
    git clone https://github.com/zeromq/jzmq.git && \
    cd /opt/jzmq/jzmq-jni && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig && \
    cd /opt && \
    rm -rf jzmq && \
    apt-get purge -y make pkg-config libtool autoconf automake git && \
    apt-get clean && apt-get autoclean && apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

ENV LD_LIBRARY_PATH /usr/local/lib

ARG BUILD_DATE
ARG VCS_REF
ARG IMAGE_VERSION

LABEL maintainer="ssemichev@gmail.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="DeepCortex" \
      org.label-schema.description="DeepCortex is the world’s first cloud based, automated platform for doing the entire end-to-end Data Science process" \
      org.label-schema.url="http://www.deepcortex.ai" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.version=$IMAGE_VERSION \
      org.label-schema.vcs-url="https://github.com/deepcortex/dockers" \
      org.label-schema.vendor="DeepCortex" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.docker.cmd="docker run --rm -it deepcortex/zeromq-scala /bin/bash"
      