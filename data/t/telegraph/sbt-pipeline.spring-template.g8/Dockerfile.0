FROM anapsix/alpine-java

ARG APP_NAME
ARG APP_VERSION

ADD target/${APP_NAME}-0.1.0-SNAPSHOT.jar app.jar

ENV APP_NAME=${APP_NAME}
ENV APP_VERSION=0.1.0-SNAPSHOT

EXPOSE 9000
ENTRYPOINT ["sh", "-c", "java -Djava.security.egd=file:/dev/./urandom -Dspring.profiles.active=${ENVIRONMENT} -jar /app.jar"]
