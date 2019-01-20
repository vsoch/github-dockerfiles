FROM node:6.10.0-slim
MAINTAINER Plataformatec <opensource@plataformatec.com.br>

WORKDIR /usr/src/app
COPY package.json /usr/src/app/

RUN apk --update add git && \
    npm install && \
    apk del --purge git

COPY . /usr/src/app

RUN adduser -u 9000 -D app
USER app
VOLUME /code
WORKDIR /code

CMD ["/usr/src/app/bin/engine-remark-lint"]
