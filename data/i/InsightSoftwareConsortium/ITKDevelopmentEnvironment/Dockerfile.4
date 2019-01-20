FROM ubuntu:14.04 as simpleitk-doxygen
MAINTAINER Francois Budin <francois.budin@kitware.com>

RUN apt-get update && apt-get install -y \
  apt-utils \
  bison \
  build-essential \
  curl \
  flex \
  git \
  graphviz \
  ninja-build \
  doxygen \
  python \
  vim \
  && apt-get clean

# Install the latest CMake release
WORKDIR /tmp/
RUN curl  -L https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    pip install cmake

RUN git clone https://github.com/doxygen/doxygen.git && \
    cd doxygen && \
    git checkout Release_1_8_9_1 && \
    ./configure && \
    make -j$(nproc) && make install

WORKDIR /

ARG TAG=master

RUN git clone http://itk.org/SimpleITK.git && \
    cd SimpleITK && \
    git checkout $TAG && \
    cd .. && \
    mkdir SimpleITK-build && \
    cd SimpleITK-build && \
    cmake -G Ninja -DBUILD_DOXYGEN=ON -DSimpleITK_BUILD_DISTRIBUTE:BOOL=ON ../SimpleITK/SuperBuild/ && \
    ninja SimpleITK-doc

ENTRYPOINT ["/bin/bash"]
