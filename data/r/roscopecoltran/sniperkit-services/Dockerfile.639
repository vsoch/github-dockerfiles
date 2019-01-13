FROM armdocker.rnd.ericsson.se/proj_kds/er/java-jdk8:latest
MAINTAINER Nicolas Seyvet <nicolas.seyvet@ericsson.com>

ENV ZK_VERSION 3.4.10

ENV ZK_CLIENT_PORT 2181
ENV ZK_FOLLOWERS_PORT 2888
ENV ZK_ELECTION_PORT 3888

#ENV ZK_SERVER_1 server.1=127.0.0.1:${ZK_FOLLOWERS_PORT}:${ZK_ELECTION_PORT}
ENV ZK_ID 1
ENV ZK_SERVER_1 server.1=127.0.0.1

RUN apk add --update curl sudo bash   \
    && addgroup -g 1000 zookeeper     \
    && adduser -u 1000 -G zookeeper -D -h /home/zookeeper -s /bin/bash zookeeper \
    && echo "zookeeper  ALL = NOPASSWD: /bin/chown" > /etc/sudoers

RUN curl -L http://apache.mirrors.spacedump.net/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz | tar xz -C /tmp \
    && mv /tmp/zookeeper-${ZK_VERSION} /opt/zookeeper 

RUN mkdir -p /opt/zookeeper/conf    \
    && mkdir -p /opt/zookeeper/data \
    && mkdir -p /opt/zookeeper/log  \ 
    && chown -R zookeeper:zookeeper /opt/zookeeper

USER zookeeper
COPY docker-entrypoint.sh /opt/zookeeper
COPY config/zoo-template.cfg /opt/zookeeper/conf

USER root
RUN chmod ug=rx /opt/zookeeper/docker-entrypoint.sh \
    && chown -R zookeeper:zookeeper /opt/zookeeper

WORKDIR /opt/zookeeper
USER zookeeper

ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE ${ZK_CLIENT_PORT} ${ZK_FOLLOWERS_PORT} ${ZK_ELECTION_PORT}

CMD ["zookeeper"]
