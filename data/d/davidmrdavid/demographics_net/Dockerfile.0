# =============================================================================
# Name: Dockerfile
# Maintainers: David Justo and Kareem Moussa
# Description: Dockerfile for the demographics_net project by Kareem Moussa
#              and David Justo. The goal is that this file will enable us
#              enable reproducible results on an easy to transport development
#              environment. This Dockerfile is for the models that will run on
#              a CPU. 
# Last revised: 2/22/17
# Sources:
#   1. Caffe:cpu Dockerfile
#   => https://github.com/BVLC/caffe/blob/master/docker/cpu/Dockerfile
# =============================================================================


# ======================== Installing basic Caffe =============================
FROM ubuntu:16.04
LABEL maintainer caffe-maint@googlegroups.com

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python-dev \
        python-numpy \
        python-pip \
        python-setuptools \
        python-scipy && \
    rm -rf /var/lib/apt/lists/*

ENV CAFFE_ROOT=/opt/caffe
WORKDIR $CAFFE_ROOT

ENV CLONE_TAG=rc4

RUN git clone -b ${CLONE_TAG} --depth 1 https://github.com/BVLC/caffe.git . && \
    pip install --upgrade pip && \
    cd python && for req in $(cat requirements.txt) pydot; do pip install $req; done && cd .. && \
    mkdir build && cd build && \
    cmake -DCPU_ONLY=1 .. && \
    make -j"$(nproc)"

ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

WORKDIR /workspace

# ======================== Installing Tensorflow  =============================
# TODO: update this to tensorflow-gpu when running for GPU
RUN pip install tensorflow 

# ======================== Installing Keras ===================================
RUN pip install keras

# ======================== Installing Jupyter =================================
RUN pip install jupyter

# ======================== Installing VIM =====================================
RUN apt-get update
RUN apt-get install vim -y


