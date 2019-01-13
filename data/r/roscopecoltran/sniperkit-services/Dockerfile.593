FROM alpine:3.4
MAINTAINER Akiyoshi Sakaguchi <autumngoodluck@gmail.com>

ENV NODE_VERSION=6.2.1 \
    NPM_CONFIG_LOGLEVEL=info

RUN apk add --update --virtual build-dependencies build-base binutils-gold linux-headers curl paxctl python \
  && curl -SLO "https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.gz" \
  && tar -xzf "node-v${NODE_VERSION}.tar.gz" \
  && cd "/node-v${NODE_VERSION}" \
  && ./configure --prefix=/usr/local --fully-static --without-snapshot \
  && make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
  && make install \
  && paxctl -cm /usr/local/bin/node \
  && cd / \
  && apk del build-dependencies \
  && rm -rf /var/cache/apk/* \
    "node-v${NODE_VERSION}.tar.gz" "/node-v${NODE_VERSION}" \
    /usr/local/lib/node_modules/npm/man /usr/local/lib/node_modules/npm/doc /usr/local/lib/node_modules/npm/html \
    /usr/local/share/man \
    /usr/include

CMD ["node"]
