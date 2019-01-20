#
# Small memcached docker image based on alpine linux
#
# http://github.com/tenstartups/memcached-docker
#

FROM tenstartups/alpine:latest

MAINTAINER Marc Lennox <marc.lennox@gmail.com>

# Install packages
RUN \
  apk --update add memcached && \
  wget --no-check-certificate -O /usr/local/bin/gosu https://github.com/tianon/gosu/releases/download/1.4/gosu-amd64 && \
  chmod +x /usr/local/bin/gosu && \
  rm -rf /var/cache/apk/*

RUN mkdir /data && chown memcached:memcached /data

VOLUME /data

WORKDIR /data

COPY entrypoint.sh /docker-entrypoint

ENTRYPOINT ["/docker-entrypoint"]

EXPOSE 11211

CMD ["memcached"]
