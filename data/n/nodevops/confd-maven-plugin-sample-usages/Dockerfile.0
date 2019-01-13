FROM fabric8/java-alpine-openjdk8-jdk
MAINTAINER Christophe Furmaniak <christophe.furmaniak@gmail.com>

ENV AB_OF= \
    JAVA_APP_DIR=/usr/local/appli \
    JAVA_APP_NAME=sb-greeting-and-resolve


LABEL DOCKERFILE_PATH=/usr/local/appli/Dockerfile \
      LOOZ_VERSION=v0.0.1

RUN mkdir -p /usr/local/appli

COPY target/springboot-sample-*.jar  /usr/local/appli/

COPY Dockerfile /usr/local/appli/

EXPOSE 8080
