FROM alpine:3.4
MAINTAINER smizy

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.docker.dockerfile="/3.4/Dockerfile" \
    org.label-schema.license="Apache License 2.0" \
    org.label-schema.name="smizy/zookeeper" \
    org.label-schema.url="https://github.com/smizy" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-type="Git" \
    org.label-schema.vcs-url="https://github.com/smizy/docker-zookeeper"

ENV ZOOKEEPER_VERSION     $VERSION
ENV ZOOKEEPER_HOME        /usr/local/zookeeper-${ZOOKEEPER_VERSION}
ENV ZOOKEEPER_DATA_DIR    /zookeeper
ENV ZOOKEEPER_DATALOG_DIR /var/log/zookeeper
ENV ZOOKEEPER_CONF_DIR    ${ZOOKEEPER_HOME}/conf

ENV JAVA_HOME  /usr/lib/jvm/default-jvm
ENV PATH       $PATH:${JAVA_HOME}/bin:${ZOOKEEPER_HOME}/bin

RUN set -x \
    && apk --no-cache add \
        bash \
        openjdk8-jre \
        su-exec \ 
    && mirror_url=$( \
        wget -q -O - "http://www.apache.org/dyn/closer.cgi/?as_json=1" \
        | grep "preferred" \
        | sed -n 's#.*"\(http://*[^"]*\)".*#\1#p' \
        ) \
    && wget -q -O - ${mirror_url}/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz \
        | tar -xzf - -C /usr/local \
    ## user/dir/permmsion
    && adduser -D  -g '' -s /sbin/nologin -u 1000 docker \
    && adduser -D  -g '' -s /sbin/nologin zookeeper \
    && mkdir -p \
        ${ZOOKEEPER_DATA_DIR} \
        ${ZOOKEEPER_DATALOG_DIR} \
    && chown -R zookeeper:zookeeper \
        ${ZOOKEEPER_HOME} \
        ${ZOOKEEPER_DATA_DIR} \
        ${ZOOKEEPER_DATALOG_DIR} \
    ## remove unnecessary files
    && rm -rf ${ZOOKEEPER_HOME}/src ${ZOOKEEPER_HOME}/docs

COPY entrypoint.sh /usr/local/bin/ 
COPY zoo.cfg       ${ZOOKEEPER_CONF_DIR}/
 
VOLUME ["${ZOOKEEPER_DATA_DIR}", "${ZOOKEEPER_DATALOG_DIR}"]

WORKDIR ${ZOOKEEPER_HOME}

EXPOSE 2181 2888 3888

ENTRYPOINT ["entrypoint.sh"]
CMD ["-server", "1", "1" ]