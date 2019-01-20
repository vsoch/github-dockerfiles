FROM docker-internal.stackato.com/stackato/base-redis:master

ADD . /source
ADD stackon.json /

CMD ["redis-server", "/source/redis-server.conf"]

EXPOSE 7474
VOLUME ["/var/stackato/data/config_redis"]
