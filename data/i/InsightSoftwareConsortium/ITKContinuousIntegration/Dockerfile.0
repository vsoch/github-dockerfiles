FROM docker:18.05.0-ce-rc1-git
MAINTAINER Matt McCormick <matt.mccormick@kitware.com>

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories \
  && apk update \
  && apk add \
    bash \
    curl \
    curl-dev \
    expat-dev \
    g++ \
    make \
    jpeg-dev \
    libpng-dev \
    ninja \
    openssl-dev \
    python3-dev \
    tiff-dev \
    zlib-dev \
  && ln -s /usr/bin/python3 /usr/bin/python

ENV CMAKE_VERSION 3.11.1
RUN mkdir -p /usr/src && \
  curl -O https://raw.githubusercontent.com/dockcross/dockcross/f5c87215fc52e7f72c88842c8486d0be6ba8161b/imagefiles/build-and-install-cmake.sh && \
  chmod +x ./build-and-install-cmake.sh && \
  ./build-and-install-cmake.sh

# ITK master 2019-01-12
ENV ITK_VERSION 99475715b85a3258834556a41ee3f09f59eadf7b
RUN git clone https://github.com/InsightSoftwareConsortium/ITK.git \
  && cd ITK \
  && git checkout ${ITK_VERSION} \
  && rm -rf .git
RUN mkdir ITK-build \
  && cd ITK-build \
  && cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE:STRING=MinSizeRel \
    -DBUILD_TESTING:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DITK_USE_SYSTEM_EXPAT:BOOL=ON \
    -DITK_USE_SYSTEM_JPEG:BOOL=ON \
    -DITK_USE_SYSTEM_PNG:BOOL=ON \
    -DITK_USE_SYSTEM_TIFF:BOOL=ON \
    -DITK_USE_SYSTEM_ZLIB:BOOL=ON \
    -DModule_RLEImage:BOOL=ON \
    ../ITK \
  && ninja \
  && find . -name '*.o' -delete
