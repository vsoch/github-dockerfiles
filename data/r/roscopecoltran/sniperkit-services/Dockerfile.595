FROM alpine:3.4

MAINTAINER Akiyoshi Sakaguchi <autumngoodluck@gmail.com>

ENV MAGELLAN_PROXY_VERSION=0.1.4 \
    APP_ROOT=/opt/nginx_omniauth_adapter

WORKDIR ${APP_ROOT}

COPY Gemfile   ${APP_ROOT}/
COPY config.ru ${APP_ROOT}/

RUN set -x \
  && apk --update add git \
                      ruby \
                      build-base \
                      ruby-bigdecimal \
                      ruby-bundler \
                      ruby-dev \
                      ruby-io-console \
                      ruby-json \
                      ca-certificates \
                      openssl \
  && cd ${APP_ROOT} \
  && bundle install \
  && apk del git build-base ruby-dev \
  && rm -rf /var/cache/apk/*


ADD https://github.com/groovenauts/magellan-proxy/releases/download/v${MAGELLAN_PROXY_VERSION}/magellan-proxy-${MAGELLAN_PROXY_VERSION}_linux-amd64 /usr/local/bin/magellan-proxy
RUN chmod +x /usr/local/bin/magellan-proxy

CMD ["/usr/local/bin/magellan-proxy", "--port", "18081", "bundle", "exec", "rackup", "-p", "18081", "config.ru"]
