FROM ubuntu:14.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y apt-transport-https ca-certificates

# update repos
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
	echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF; DISTRO=$(lsb_release -is | tr "[:upper:]" "[:lower:]"); CODENAME=$(lsb_release -cs) && \
	echo "deb http://repos.mesosphere.io/${DISTRO} ${CODENAME} main" | tee /etc/apt/sources.list.d/mesosphere.list
RUN apt-get update -y

# Docker, Mesos
ENV DOCKER_PACKAGE_VERSION=1.7.1-0~trusty
RUN apt-get -y install -y docker-engine=$DOCKER_PACKAGE_VERSION

ENV MESOS_PACKAGE_VERSION=0.28.0-2.0.16.ubuntu1404
RUN apt-get -y install mesos=$MESOS_PACKAGE_VERSION

# Overwrite mesos-init-wrapper
ADD ./provision/mesos-init-wrapper.sh /usr/bin/mesos-init-wrapper.sh
# Add the bootstrap script
ADD ./provision/mesos_bootstrap.sh /usr/local/bin/mesos_bootstrap.sh

# Use the mesos_bootstrap.sh script to start
ENTRYPOINT ["/usr/local/bin/mesos_bootstrap.sh"]
