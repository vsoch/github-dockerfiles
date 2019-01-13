# Version: 1
# Name: asp2run
FROM microsoft/dotnet:2.1.0-aspnetcore-runtime

MAINTAINER "boyan.au@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && \
    apt-get -qq -y install libgdiplus && \
    apt-get -qq -y install libc6-dev && \
    apt-get -qq -y install procps && \
    apt-get -qq -y install vim
