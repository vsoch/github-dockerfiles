FROM deepcortex/java-ubuntu:latest

ENV SCALA_HOME=/usr/local/share/scala
ENV PATH=$PATH:$SCALA_HOME/bin \
    SCALA_VERSION=2.11.8

RUN wget --quiet http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz && \
    tar -xf /scala-$SCALA_VERSION.tgz -C /usr/local/ && \
    ln -s /usr/local/scala-$SCALA_VERSION $SCALA_HOME && \
    rm scala-$SCALA_VERSION.tgz

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
      org.label-schema.docker.cmd="docker run --rm -it deepcortex/scala-ubuntu scala"
      