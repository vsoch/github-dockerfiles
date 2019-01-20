FROM azul/zulu-openjdk:8u172-8.30.0.1

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends wget
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD
RUN wget http://public-repo-1.hortonworks.com/HDP/ubuntu16/2.x/updates/2.6.1.0/hdp.list -O /etc/apt/sources.list.d/hdp.list
RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -y --allow-unauthenticated spark2-2-6-1-0-129

ENV HADOOP_PREFIX /usr/hdp/2.6.1.0-129/hadoop
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop

RUN \
  echo 'HADOOP_PREFIX="/usr/hdp/2.6.1.0-129/hadoop"' >> /etc/environment && \
  echo 'HADOOP_COMMON_HOME="/usr/hdp/2.6.1.0-129/hadoop"' >> /etc/environment && \
  echo 'HADOOP_HDFS_HOME="/usr/hdp/2.6.1.0-129/hadoop"' >> /etc/environment && \
  echo 'HADOOP_MAPRED_HOME="/usr/hdp/2.6.1.0-129/hadoop"' >> /etc/environment && \
  echo 'HADOOP_YARN_HOME="/usr/hdp/2.6.1.0-129/hadoop-yarn"' >> /etc/environment && \
  echo 'HADOOP_CONF_DIR="/usr/hdp/2.6.1.0-129/hadoop/etc/hadoop"' >> /etc/environment && \
  echo 'YARN_CONF_DIR="/usr/hdp/2.6.1.0-129/hadoop/etc/hadoop"' >> /etc/environment
ENV PATH $PATH:$HADOOP_PREFIX/bin:$HADOOP_PREFIX/sbin:$HADOOP_PREFIX-yarn/bin:$HADOOP_PREFIX-yarn/sbin:$HADOOP_PREFIX-hdfs/bin:$HADOOP_PREFIX-hdfs/sbin

COPY core-site.xml $HADOOP_PREFIX/etc/hadoop/
COPY hdfs-site.xml $HADOOP_PREFIX/etc/hadoop/
COPY mapred-site.xml $HADOOP_PREFIX/etc/hadoop/
COPY yarn-site.xml $HADOOP_PREFIX/etc/hadoop/
ENV JAVA_HOME /usr/lib/jvm/zulu-8-amd64
