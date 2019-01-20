FROM mhart/alpine-node:7.2
MAINTAINER Raul <raul.requero@vizzuality.com>

ARG NAME=node-script
ENV NAME ${NAME}

RUN apk update && apk upgrade && \
    apk add --no-cache --update bash git openssh python alpine-sdk

RUN addgroup $NAME && adduser -s /bin/bash -D -G $NAME $NAME

RUN mkdir -p /opt/$NAME
COPY package.json /opt/$NAME/package.json
RUN cd /opt/$NAME && npm install

WORKDIR /opt/$NAME

COPY ./index.js /opt/$NAME/index.js
COPY ./src /opt/$NAME/src
COPY ./data /opt/$NAME/data
RUN chown $NAME:$NAME /opt/$NAME

# Tell Docker we are going to use this ports
USER $NAME

VOLUME /opt/$NAME/data

ENTRYPOINT ["npm", "start"]