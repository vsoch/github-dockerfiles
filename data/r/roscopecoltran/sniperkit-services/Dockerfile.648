FROM alpine:3.5
MAINTAINER Nicolas Seyvet <nicolas.seyvet@ericsson.com>

ENV ETCD_VERSION=v3.1.5     \
    ETCD_DATA_VOLUME_DIR="/opt/etcd/data"                               \
    ETCD_BIN_DIR="/opt/etcd/bin"


RUN apk add --update ca-certificates openssl tar bash             \
    && mkdir -p ${ETCD_BIN_DIR}                                   \
    && addgroup -g 1000 etcd                                      \
    && adduser -u 1000 -G etcd -D -h /opt/etcd -s /bin/bash etcd  \
    && wget https://github.com/coreos/etcd/releases/download/${ETCD_VERSION}/etcd-${ETCD_VERSION}-linux-amd64.tar.gz \
    && tar zxvf etcd-${ETCD_VERSION}-linux-amd64.tar.gz           \
    && mv etcd-${ETCD_VERSION}-linux-amd64/etcd* ${ETCD_BIN_DIR}  \
    && apk del --purge tar openssl                                \
    && rm -Rf etcd-${ETCD_VERSION}-linux-amd64* /var/cache/apk/*

VOLUME ${ETCD_DATA_VOLUME_DIR}
EXPOSE 2379 2380 4001 7001

ADD docker-entrypoint.sh /opt/etcd/docker-entrypoint.sh
RUN chmod -R 755 /opt/etcd/docker-entrypoint.sh \
    && chown -R etcd:etcd /opt/etcd            

WORKDIR /opt/etcd
USER etcd

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["etcd"]