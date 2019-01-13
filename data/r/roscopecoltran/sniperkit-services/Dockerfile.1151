FROM deepcortex/zeromq-scala:latest

RUN apt-get -y update && \
    apt-get install -y \
    python-pip \
    software-properties-common \
    python-dev && \
    pip install pyzmq && \
    apt-get purge -y \
    software-properties-common \
    locales \
    manpages \
    manpages-dev \
    perl \
    gcc \
    python-dev && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get -y autoremove

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
      org.label-schema.docker.cmd="docker run --rm -it deepcortex/zeromq-scala-python /bin/bash"
      