FROM smizy/scikit-learn:0.18-alpine

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
ARG EXTRA_BAZEL_ARGS

LABEL \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.license="Apache License 2.0" \
    org.label-schema.name="smizy/sonnet" \
    org.label-schema.url="https://gitlab.com/smizy" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-type="Git" \
    org.label-schema.version=$VERSION \
    org.label-schema.vcs-url="https://gitlab.com/smizy/docker-sonnet"

ENV BAZEL_VERSION       0.4.5
ENV TENSORFLOW_VERSION  1.1.0
ENV SONNET_VERSION      1.0

ENV JAVA_HOME  /usr/lib/jvm/default-jvm

ENV EXTRA_BAZEL_ARGS  $EXTRA_BAZEL_ARGS

RUN set -x \
    && apk update \

    ## bazel
    ## - dependencies
    && apk --no-cache add --virtual .builddeps \
        bash \
        build-base \
        linux-headers \
        openjdk8 \
        python3-dev \
        wget \
        zip \
    && mkdir /tmp/bazel \
    && wget -q -O /tmp/bazel-dist.zip https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-dist.zip \
    && unzip -q -d /tmp/bazel /tmp/bazel-dist.zip \
    && cd /tmp/bazel \
    ## - add -fpermissive compiler option to avoid compilation failure 
    && sed -i -e '/"-std=c++0x"/{h;s//"-fpermissive"/;x;G}' tools/cpp/cc_configure.bzl \
    ## - add '#include <sys/stat.h>' to avoid mode_t type error 
    && sed -i -e '/#endif  \/\/ COMPILER_MSVC/{h;s//#else/;G;s//#include <sys\/stat.h>/;G;}' third_party/ijar/common.h \
    && bash compile.sh \
    && cp output/bazel /usr/local/bin/ \

    ## sonnet/tensorflow 
    ## - depedencies
    && apk --no-cache add \
        jemalloc \
        git \
        libc6-compat \
    && apk --no-cache add --virtual .builddeps.1 \
        perl \
        sed \
    && pip3 install wheel \
    && cd /tmp \
    && git clone --recursive https://github.com/deepmind/sonnet \

    ## tensorflow
    && cd sonnet/tensorflow \
    && git checkout r1.1 \
    ## - use alpine-patched protobuf (Undef major/minor if they are defined as macro. #2775)
    && sed -ri 's/2b7430d96aeff2bb624c8d52182ff5e4b9f7f18a/af2d5f5ad3808b38ea58c9880be1b81fd2a89278/g' tensorflow/workspace.bzl \
    && sed -ri 's/e5d3d4e227a0f7afb8745df049bbd4d55474b158ca5aaa2a0e31099af24be1d0/89fb700e6348a07829fac5f10133e44de80f491d1f23bcc65cba072c3b374525/g' tensorflow/workspace.bzl \
    && echo | \
        CC_OPT_FLAGS=-march=native \
        PYTHON_BIN_PATH=/usr/bin/python \
        TF_NEED_CUDA=0 \
        TF_NEED_GCP=0 \
        TF_NEED_JEMALLOC=0 \        
        TF_NEED_HDFS=0 \
        TF_NEED_OPENCL=0 \  
        TF_ENABLE_XLA=0 \
        ./configure \
    && bazel build -c opt ${EXTRA_BAZEL_ARGS} //tensorflow/tools/pip_package:build_pip_package \
    && bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg \
    && pip3 install /tmp/tensorflow_pkg/tensorflow-${TENSORFLOW_VERSION}-cp35-cp35m-linux_x86_64.whl \
    && cd .. \

    ## sonnet 
    ## - python3 compatibility patch
    && wget https://patch-diff.githubusercontent.com/raw/deepmind/sonnet/pull/10.patch \
    && patch -p1 < 10.patch \  
    && bazel build ${EXTRA_BAZEL_ARGS} --config=opt :install \
    && bazel-bin/install /tmp/sonnet_pkg \
    && pip3 install /tmp/sonnet_pkg/sonnet-${SONNET_VERSION}-py3-none-any.whl \
    && cp -r sonnet/examples /code/ \
    ## clean
    && apk del \
        .builddeps \
        .builddeps.1 \
    && find /usr/lib/python3.5 -name __pycache__ | xargs rm -r \
    && rm -rf \
        /root/.[acpw]* \
        /tmp/bazel* \
        /tmp/sonnet* \
        /tmp/tensorflow* \
        /usr/local/bin/bazel