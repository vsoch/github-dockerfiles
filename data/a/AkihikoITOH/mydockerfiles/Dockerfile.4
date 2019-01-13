FROM ubuntu:trusty
MAINTAINER ITOH Akihiko

RUN apt-get update && \
    apt-get install -yq --no-install-recommends python python-pip groff-base && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN pip install awscli

RUN mkdir -p /root/.aws && \
    mkdir -p /tmp

COPY ["./credentials", "/root/.aws/credentials"]

ENTRYPOINT ["aws"]
CMD ["help"]

