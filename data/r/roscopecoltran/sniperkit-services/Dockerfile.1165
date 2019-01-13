FROM alpine:3.6
MAINTAINER Binghong Liang <liangbinghong@gmail.com>

ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV BAZEL_VERSION 0.5.3
ENV TENSORFLOW_VERSION 1.3.0

COPY others/FALCONN-2.0.0.tar.gz /tmp/FALCONN-2.0.0.tar.gz
RUN apk upgrade --update \
    && apk add bash python2 py2-pip python3 freetype libpng libjpeg-turbo libstdc++ openblas \
    && apk add --no-cache --virtual=build-dependencies wget curl ca-certificates unzip sed \
        python3-dev freetype-dev libpng-dev libjpeg-turbo-dev musl-dev openblas-dev \
        gcc g++ make cmake swig linux-headers openjdk8 patch perl rsync zip tar gzip \
    && rm -rf /usr/bin/python \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && pip3 install --no-cache-dir numpy \
    && cd /tmp \
    && tar xzvf FALCONN-2.0.0.tar.gz \
    && cd FALCONN-2.0.0 \
    && /usr/bin/python3 setup.py install \
    && cd .. \
    && pip3 install --no-cache-dir wheel \
    && curl -SLO https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-dist.zip \
    && mkdir bazel-${BAZEL_VERSION} \
    && unzip -qd bazel-${BAZEL_VERSION} bazel-${BAZEL_VERSION}-dist.zip \
    && cd bazel-${BAZEL_VERSION} \
    && sed -i -e '/"-std=c++0x"/{h;s//"-fpermissive"/;x;G}' tools/cpp/cc_configure.bzl \
    && sed -i -e '/#endif  \/\/ COMPILER_MSVC/{h;s//#else/;G;s//#include <sys\/stat.h>/;G;}' third_party/ijar/common.h \
    && bash compile.sh \
    && cp -p output/bazel /usr/bin/ \
    && cd /tmp \
    && curl -SL https://github.com/tensorflow/tensorflow/archive/v${TENSORFLOW_VERSION}.tar.gz \
        | tar xzf - \
    && cd tensorflow-${TENSORFLOW_VERSION} \
    && sed -i -e '/JEMALLOC_HAVE_SECURE_GETENV/d' third_party/jemalloc.BUILD \
    && PYTHON_BIN_PATH=/usr/bin/python \
        PYTHON_LIB_PATH=/usr/lib/python3.6/site-packages \
        CC_OPT_FLAGS="-march=native" \
        TF_NEED_MKL=0 \
        TF_NEED_JEMALLOC=1 \
        TF_NEED_GCP=0 \
        TF_NEED_HDFS=0 \
        TF_ENABLE_XLA=0 \
        TF_NEED_VERBS=0 \
        TF_NEED_OPENCL=0 \
        TF_NEED_CUDA=0 \
        TF_NEED_MPI=0 \
        bash configure \
    && bazel build --config opt --local_resources 4096,.5,1.0 //tensorflow/tools/pip_package:build_pip_package \
    && ./bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg \
    && cd \
    && pip3 install --no-cache-dir /tmp/tensorflow_pkg/tensorflow-${TENSORFLOW_VERSION}-cp36-cp36m-linux_x86_64.whl \
    && pip3 install --no-cache-dir pandas scipy scikit-learn keras tensorlayer pillow requests cython \
    && pip2 install --no-cache-dir supervisor \
    && apk del build-dependencies \
    && rm -f /usr/bin/bazel \
    && rm -rf /tmp/* /root/.cache
