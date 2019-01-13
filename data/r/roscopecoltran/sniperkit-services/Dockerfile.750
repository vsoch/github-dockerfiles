FROM openjdk:8u131-jdk-alpine
MAINTAINER giabar

ENV KAFKA_VERSION="0.10.2.0" SCALA_VERSION="2.11"
COPY download-kafka.sh /tmp/download-kafka.sh
RUN apk upgrade --update &&\
    apk add --update \
    bash \
    unzip \
    wget \
    curl \
    jq \
    coreutils &&\
    /tmp/download-kafka.sh &&\
    mkdir /opt &&\
    tar xfz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt &&\
    rm /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
VOLUME ["/kafka"]
ENV KAFKA_HOME /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION}
COPY start-kafka.sh /usr/bin/start-kafka.sh
CMD ["start-kafka.sh"]
EXPOSE 2181 9092
