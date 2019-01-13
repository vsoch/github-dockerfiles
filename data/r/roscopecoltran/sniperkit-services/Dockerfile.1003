FROM alpine:3.4

RUN set -x \
    && apk update \
    && apk --no-cache add \
        ca-certificates \
        ruby \
        zlib \
    && apk --no-cache add --virtual .builddeps \
        build-base \
        ruby-dev \
        zlib-dev \
    && echo 'gem: --no-document' >> /etc/gemrc \
    && gem install wp2txt \
    && apk del .builddeps