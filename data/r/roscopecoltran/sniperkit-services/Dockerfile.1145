FROM deepcortex/zeromq-scala:latest

ENV SBT_VERSION 0.13.15
ENV SBT_HOME /usr/local/sbt-launcher-packaging-${SBT_VERSION}
ENV PATH ${PATH}:${SBT_HOME}/bin

RUN adduser --shell /bin/bash --disabled-password --system ubuntu \
    && echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    apt-get update && apt-get install -y apt-transport-https && \
    echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 && \
    apt-get -y update && \
    apt-get install -y --allow-unauthenticated sbt && \
    apt-get clean && apt-get autoclean && apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

USER ubuntu

VOLUME /projects
WORKDIR /projects

RUN sbt sbtVersion

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
      org.label-schema.docker.cmd="docker run --rm -it -v ~/projects:/projects deepcortex/zeromq-sbt /bin/bash"
      