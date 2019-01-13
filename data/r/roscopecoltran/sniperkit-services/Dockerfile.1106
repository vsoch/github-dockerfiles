FROM alpine:3.3
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>

RUN set -x && \ 
    apk add --update --no-cache \ 
      curl \
      jq

COPY ./entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
