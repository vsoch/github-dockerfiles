FROM unit9/base:latest
MAINTAINER Kamil Cholewinski <kamil.cholewinski@unit9.com>

RUN apt-key adv \
    --keyserver hkp://ha.pool.sks-keyservers.net:80 \
    --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && echo 'deb https://apt.dockerproject.org/repo debian-jessie main' \
    > /etc/apt/sources.list.d/docker.list \
    apt-get update && \
    apt-get install --no-install-recommends --yes \
            docker-engine \
            && \
    rm -rf /var/cache/apt /var/lib/apt/lists

ADD rc.local /etc/rc.local
