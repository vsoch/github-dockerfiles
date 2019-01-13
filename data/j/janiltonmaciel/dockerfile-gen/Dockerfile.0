FROM alpine:3.7

LABEL maintainer="Janilton Maciel <janilton@gmail.com>"

ENV DOCKERFILE_GEN_VERSION 1.10.0

RUN apk update && apk upgrade \
    && apk add --no-cache wget tar \
    && wget https://github.com/janiltonmaciel/dockerfile-gen/releases/download/${DOCKERFILE_GEN_VERSION}/dockerfile-gen_${DOCKERFILE_GEN_VERSION}_linux_amd64.tar.gz \
    && tar -C /usr/local/bin -xvf dockerfile-gen*

WORKDIR /app

CMD ["dockerfile-gen"]
