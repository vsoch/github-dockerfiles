FROM ubuntu:16.04

# SET utf-8 locale
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    SCALA_VERSION=2.11.8 \
    SBT_VERSION=0.13.11

# INSTALL common tools
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install curl wget software-properties-common apt-transport-https uuid

# ADD apt repositories
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update

# INSTALL Oracle JDK 8
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

WORKDIR /tmp

# INSTALL Scala and SBT
RUN wget -nv http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.deb && \
    dpkg -i scala-$SCALA_VERSION.deb && \
    wget -nv http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
    dpkg -i sbt-$SBT_VERSION.deb && \
    rm -f scala-* && \
    rm -f sbt-* && \
    sbt exit
