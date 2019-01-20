FROM anapsix/alpine-java

ARG APP_NAME
ARG APP_VERSION

ADD target/${APP_NAME}-${APP_VERSION}.jar app.jar

ENV APP_NAME=${APP_NAME}
ENV APP_VERSION=${APP_VERSION}

EXPOSE 9000
ENTRYPOINT ["sh", "-c", "java -Djava.security.egd=file:/dev/./urandom -Dconfig.resource=application.${ENVIRONMENT}.conf -jar /app.jar"]
