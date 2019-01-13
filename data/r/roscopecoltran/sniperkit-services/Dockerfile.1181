FROM ssemichev/sbt:latest

USER root

USER alpine

VOLUME /projects
WORKDIR /projects

ARG BUILD_DATE
ARG VCS_REF
ARG IMAGE_VERSION

LABEL maintainer="ssemichev@gmail.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref=$VCS_REF \
	  org.label-schema.version=$IMAGE_VERSION \
      org.label-schema.vcs-url="https://github.com/deepcortex/docker-scala-zeromq" \
      org.label-schema.schema-version="1.0" \
	  org.label-schema.docker.cmd="docker run --rm -it -v HOST_PATH:/projects deepcortex/scala-zeromq /bin/sh"