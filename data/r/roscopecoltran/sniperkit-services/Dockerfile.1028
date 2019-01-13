FROM alpine:3.5
MAINTAINER smizy

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.license="Apache License 2.0" \
    org.label-schema.name="smizy/opentsdb" \
    org.label-schema.url="https://github.com/smizy" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-type="Git" \
    org.label-schema.vcs-url="https://github.com/smizy/docker-opentsdb"

ENV OPENTSDB_VERSION     ${VERSION}
ENV OPENTSDB_SRC_DIR     /usr/local/opentsdb-${OPENTSDB_VERSION}
ENV OPENTSDB_HOME        /usr/share/opentsdb
ENV OPENTSDB_CONF_DIR    ${OPENTSDB_HOME}/etc/opentsdb
ENV OPENTSDB_STATIC_DIR  ${OPENTSDB_HOME}/static
ENV OPENTSDB_PLUGINS_DIR ${OPENTSDB_HOME}/plugins  
ENV OPENTSDB_LOG_DIR     /var/log/opentsdb
ENV OPENTSDB_TMP_DIR     /tmp/opentsdb
ENV OPENTSDB_ZK_QUORUM   zookeeper-1.vnet,zookeeper-2.vnet,zookeeper-3.vnet

ENV HBASE_HOME               /usr/local/hbase-1.2.4
ENV HBASE_HMASTER1_HOSTNAME  hmaster-1.vnet

ENV JAVA_HOME   /usr/lib/jvm/default-jvm
ENV PATH        $PATH:${JAVA_HOME}/bin:${HBASE_HOME}/bin:${OPENTSDB_HOME}/bin

RUN set -x \
    && apk update \
    && apk --no-cache add \
        bash \
        ca-certificates \
        su-exec \
        wget \
    && apk --no-cache add \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
        gnuplot \
    && wget -q -O - https://github.com/OpenTSDB/opentsdb/releases/download/v${OPENTSDB_VERSION}/opentsdb-${OPENTSDB_VERSION}.tar.gz  \
        | tar -xzf - -C /usr/local 
        
COPY build.sh.patch ${OPENTSDB_SRC_DIR}/
        
RUN set -x \
    && apk --no-cache add --virtual .builddeps \
        autoconf \
        automake \
        build-base \
        openjdk8 \
        python \
    && cd ${OPENTSDB_SRC_DIR} \
    ## https://github.com/OpenTSDB/opentsdb/issues/707
    && patch < build.sh.patch \
    && ./build.sh \
    && cd ${OPENTSDB_SRC_DIR}/build \
    && make install \
    && apk del .builddeps \
    && rm -rf ${OPENTSDB_SRC_DIR} \
    && apk --no-cache add openjdk8-jre \
    ## user/dir
    && adduser -D  -g '' -s /sbin/nologin -u 1000 docker \
    && for user in hadoop tsdb; do \
         adduser -D -g '' -s /sbin/nologin ${user}; \
       done \
    && for user in root tsdb docker; do \
         adduser ${user} hadoop; \
       done \ 
    && mkdir -p \
        ${OPENTSDB_LOG_DIR} \
        ${OPENTSDB_TMP_DIR} \
        ${OPENTSDB_PLUGINS_DIR} \
    && chmod -R 755 \
        ${OPENTSDB_LOG_DIR} \
        ${OPENTSDB_TMP_DIR} \
    && chown -R tsdb:hadoop \
        ${OPENTSDB_LOG_DIR} \
        ${OPENTSDB_TMP_DIR}  
 
COPY etc/*  ${OPENTSDB_CONF_DIR}/
COPY bin/*  /usr/local/bin/
COPY lib/*  /usr/local/lib/

WORKDIR  ${OPENTSDB_HOME}

VOLUME ["${OPENTSDB_LOG_DIR}", "${OPENTSDB_TMP_DIR}", "${OPENTSDB_HOME}"]

ENTRYPOINT ["entrypoint.sh"]
CMD ["tsdb", "tsd"]