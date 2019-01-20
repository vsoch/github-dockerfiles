FROM phusion/baseimage:0.9.17

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq
RUN apt-get -y install git wget

# No need for ssh server
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh


# Install Java
ENV JAVA_HOME /usr/jdk1.8.0_25

RUN cd /tmp \
    && wget \
    --no-check-certificate \
    --no-cookies \
    --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    --progress=bar:force \
    download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.tar.gz \
    && tar -xvf jdk-8u25-linux-x64.tar.gz -C /usr/ \
    && ln -s $JAVA_HOME /usr/java \
    && rm -rf $JAVA_HOME/src.zip $JAVA_HOME/javafx-src.zip $JAVA_HOME/man

ENV PATH $PATH:$JAVA_HOME/bin


# Install sbt/scala
RUN cd /tmp \
    && wget \
    --no-check-certificate \
    --no-cookies \
    --progress=bar:force \
    https://dl.bintray.com/sbt/native-packages/sbt/0.13.7/sbt-0.13.7.tgz \
    && tar -xvf sbt-0.13.7.tgz -C /usr/ \
    && /usr/sbt/bin/sbt -batch

ENV PATH $PATH:/usr/sbt/bin


# Install Spark
ENV SPARK_BINARY_RELEASE 1.2.0-bin-cdh4
ENV SPARK_HOME /usr/spark-$SPARK_BINARY_RELEASE

RUN curl \
  --silent \
  --location \
  --retry 3 \
  --insecure \
  https://d3kbcqa49mib13.cloudfront.net/spark-$SPARK_BINARY_RELEASE.tgz \
    | gunzip \
    | tar x -C /usr/ \
  && ln -s /usr/spark-$SPARK_BINARY_RELEASE /usr/spark


RUN sed 's/^\(log4j.rootCategory=\)INFO\(, console\)$/\1ERROR\2/' \
  $SPARK_HOME/conf/log4j.properties.template \
  > $SPARK_HOME/conf/log4j.properties

ENV PATH $PATH:$SPARK_HOME/bin:/usr/python/bin/


# Install maxusage
ENV MAXUSAGE_DIR /maxusage

RUN mkdir -p $MAXUSAGE_DIR/src

ADD src/ $MAXUSAGE_DIR/src
ADD lib/ $MAXUSAGE_DIR/lib
ADD build.sbt $MAXUSAGE_DIR/

RUN cd $MAXUSAGE_DIR && sbt package


# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT cd $MAXUSAGE_DIR && spark-submit --class MaxUsage --master local[*] --jars lib/charmander-utils_2.10-1.0.jar target/scala-2.10/max-usage_2.10-1.0.jar



