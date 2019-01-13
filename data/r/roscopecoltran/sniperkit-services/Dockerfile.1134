FROM  node:alpine
LABEL Vendor="Raja.S"

MAINTAINER Raja. S <rajasoun@icloud.com>

# Stop container initialization if error occurs in cont-init.d fix-attrs.d script's
# ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

ENV BOTDIR /hubot

RUN set -ex \
  && apk add --update --no-cache git \
  && rm -rf /var/cache/apk/* \
  && git clone https://github.com/rajasoun/ops-bot ${BOTDIR} 

WORKDIR ${BOTDIR}

RUN set -ex \
  && npm install \
  && apk del git

# Init
# ENTRYPOINT ["/init"]
# CMD []
