FROM phusion/baseimage:0.9.17

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq

RUN apt-get install wget -y

# Install etcd
RUN wget  https://github.com/coreos/etcd/releases/download/v2.2.3/etcd-v2.2.3-linux-amd64.tar.gz; \
    tar xzvf etcd-v2.2.3-linux-amd64.tar.gz; \
    mv etcd-v2.2.3-linux-amd64 etcd

# Install etcd-browser
RUN apt-get install -y nodejs

RUN mkdir /app
COPY ./provision/etcd-browser /app/
COPY ./provision/startup.sh /app/

ENTRYPOINT ["/app/startup.sh"]
