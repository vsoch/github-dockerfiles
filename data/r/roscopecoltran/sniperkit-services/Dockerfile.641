FROM armdocker.rnd.ericsson.se/proj_kds/er/java-jdk8:latest
MAINTAINER Nicolas Seyvet <nicolas.seyvet@ericsson.com>

ENV KAFKA_VERSION 0.10.2.1
ENV SCALA_VERSION 2.12

ENV KAFKA_URL http://www-eu.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz 
ENV ZK_CONNECT 127.0.0.1:2181

# Allow kafka to run chown as sudo
RUN apk add --update curl sudo bash \
    && addgroup -g 1000 kafka       \
    && adduser -u 1000 -G kafka -D -h /home/kafka -s /bin/bash kafka \
    && echo "kafka  ALL = NOPASSWD: /bin/chown" > /etc/sudoers
RUN curl -L ${KAFKA_URL} | tar xz -C /tmp \
    && mv /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION} /opt/kafka 

COPY docker-entrypoint.sh /opt/kafka/    
COPY config/server.properties /opt/kafka/config/server.properties
COPY config/log4j.properties  /opt/kafka/config/log4j.properties

RUN chmod +x /opt/kafka/docker-entrypoint.sh \
    && mkdir -p /opt/kafka/logs              \
    && chown -R kafka:kafka /opt/kafka       \
    && apk del curl

USER kafka
WORKDIR /opt/kafka

EXPOSE 9092

VOLUME /opt/kafka/logs

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["kafka"]
