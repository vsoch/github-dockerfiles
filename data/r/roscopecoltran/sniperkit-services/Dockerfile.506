FROM anapsix/alpine-java:8_jdk
MAINTAINER luongbangvh@gmail.com

ENV WEB_FILE vaadin-example-web.jar
ENV SCRIPT_FILE start-server.sh
ENV LIB_DIR /opt/vaadin-example/lib
ENV BIN_DIR /opt/vaadin-example/bin
ENV SPRING_OUTPUT_ANSI_ENABLED ALWAYS

RUN mkdir -p ${LIB_DIR}
RUN mkdir -p ${BIN_DIR}

RUN apk --no-cache add netcat-openbsd

COPY ${WEB_FILE} ${LIB_DIR}/${WEB_FILE}
COPY ${SCRIPT_FILE} ${BIN_DIR}/${SCRIPT_FILE}
RUN dos2unix ${BIN_DIR}/${SCRIPT_FILE}

WORKDIR ${BIN_DIR}
ENTRYPOINT ["./start-server.sh"]

EXPOSE 8080