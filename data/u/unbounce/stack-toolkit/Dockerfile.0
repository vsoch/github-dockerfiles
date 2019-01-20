FROM alpine:3.4

ENV APP_NAME stack-toolkit
ENV APP_VERSION 1.0.0
ENV APP_ARCHIVE_URL https://github.com/unbounce/${APP_NAME}/releases/download/v${APP_VERSION}/${APP_NAME}.${APP_VERSION}.linux-amd64.tar.gz
ENV APP_ARCHIVE_SHA256SUM 2f614327798030676f131a3c14ba829b899db3c0611b561a6fbae9cec55143e8

RUN apk add --no-cache \
    ca-certificates \
    curl \
    tar

RUN curl \
    --silent \
    --show-error \
    --location "${APP_ARCHIVE_URL}" \
    --output /tmp/${APP_NAME}.tar.gz \
  && echo "${APP_ARCHIVE_SHA256SUM} /tmp/${APP_NAME}.tar.gz" | sha256sum -c . \
  && tar \
    -C /usr/local/bin \
    -xzf /tmp/${APP_NAME}.tar.gz \
    --strip-components 1 \
  && rm /tmp/${APP_NAME}.tar.gz

ENTRYPOINT ["stack-instances"]
CMD ["--help"]
