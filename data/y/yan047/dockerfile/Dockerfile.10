# Version: 1
# Name: jdk6
FROM phusion/baseimage:0.9.15

MAINTAINER "boyan.au@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

# In case someone loses the Dockerfile
RUN rm -rf /etc/Dockerfile
ADD Dockerfile /etc/Dockerfile

RUN apt-get -qq update && \
    apt-get -qq -y install wget curl unzip htop && \
    apt-get -qq -y autoremove && \
    apt-get -qq -y autoclean

# Create needed directories
ENV DOWNLOAD_DIR /srv/downloads
RUN mkdir -p "${DOWNLOAD_DIR}"


# Install Oracle Java 6 SDK
ENV JAVA_VERSION=jdk1.6.0_45
ENV JAVA_HOME=/opt/java/${JAVA_VERSION}
ENV JDK_FILE=jdk-6u45-linux-x64.bin

# Install Java SDK
	RUN wget -q --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" -O "${DOWNLOAD_DIR}/${JDK_FILE}" "http://download.oracle.com/otn-pub/java/jdk/6u45-b06/${JDK_FILE}" && \
  		mkdir -p /opt/java && \
    	chmod +x ${DOWNLOAD_DIR}/${JDK_FILE} && \
		${DOWNLOAD_DIR}/${JDK_FILE} && \
		mv ${JAVA_VERSION} /opt/java && \
		update-alternatives --install /usr/bin/java java /opt/java/${JAVA_VERSION}/bin/java 100 && \
		update-alternatives --config java && \
		rm -rf ${DOWNLOAD_DIR}* && rm -rf /var/log/*
	
