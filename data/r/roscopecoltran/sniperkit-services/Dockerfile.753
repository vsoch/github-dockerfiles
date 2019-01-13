FROM openjdk:8u131-jdk-alpine
MAINTAINER giabar

ENV SPARK_VER="2.1.1" \
    HADOOP_VER="2.7" \
    SPARK_HOME=/opt/spark PATH=$PATH:/opt/spark/bin
COPY download-spark.sh /tmp/download-spark.sh
RUN apk upgrade --update &&\
    apk add --update bash unzip wget curl tar gzip jq coreutils &&\
    /tmp/download-spark.sh &&\
    mkdir /opt &&\
    tar xfz /tmp/spark-$SPARK_VER-bin-hadoop$HADOOP_VER.tgz -C /opt &&\
    rm /tmp/spark-$SPARK_VER-bin-hadoop$HADOOP_VER.tgz &&\
    cd /opt &&\
    ln -s spark-$SPARK_VER-bin-hadoop$HADOOP_VER spark
CMD ["bash"]
