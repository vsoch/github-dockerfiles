FROM ubuntu:xenial

LABEL vendor=Rackspace \
      vendor.url=http://www.rackspace.com/ \
      description="NodePool Launcher service"

ENV NODEPOOL_REPO https://github.com/openstack-infra/nodepool
ENV NODEPOOL_SHA 67824d8e64250ede0cb4a3ebe344412f5cba2218

RUN apt-get -y update && \
    apt-get install -y \
    python3.5 \
    python3-pip \
    git \
    build-essential \
    curl \
    sudo \
    libffi-dev \
    libssl-dev && \
    apt-get clean

WORKDIR /root
RUN git clone $NODEPOOL_REPO

WORKDIR /root/nodepool
RUN git checkout $NODEPOOL_SHA
RUN pip3 install -e .

# Make nodepool installation directories
RUN mkdir -p \
    /etc/nodepool \
    /opt/logs \
    /var/log/nodepool \
    /var/run/nodepool

# Copy over the configuration files
ADD nodepool.yaml /etc/nodepool/
ADD logging.conf /etc/nodepool/

WORKDIR /root

ADD launcher.sh /root
RUN chmod 755 /root/launcher.sh

ENTRYPOINT /root/launcher.sh
