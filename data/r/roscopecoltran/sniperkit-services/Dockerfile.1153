FROM openjdk:8-jre-alpine

ENV SHARE /usr/local/share
ENV SCALA_HOME $SHARE/scala
ENV PATH=$PATH:$SCALA_HOME/bin
ENV SCALA_VERSION 2.11.8

RUN java -version 2>&1 | grep version | sed -e 's/^openjdk version /JAVA_VERSION=/' > $JAVA_HOME/release

RUN apk add --update wget tar bash && \
    wget --quiet http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz && \
    tar -xf scala-$SCALA_VERSION.tgz && \
    rm scala-$SCALA_VERSION.tgz && \
    mv scala-$SCALA_VERSION $SCALA_HOME

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
      org.label-schema.docker.cmd="docker run --rm -it -v HOST_PATH:/projects deepcortex/scala-alpine scala"