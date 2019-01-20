# howgood/cloudwatch
FROM gliderlabs/alpine:3.2

RUN apk add --update \
      openssl \
      ca-certificates \
      groff \
      less \
      python && \
    apk --update add --virtual build-dependencies \
      py-pip \
      python-dev \
      build-base && \
    pip install --upgrade \
      --extra-index-url=http://aws-cloudwatch.s3-website-us-east-1.amazonaws.com/ \
      --trusted-host=aws-cloudwatch.s3-website-us-east-1.amazonaws.com \
      awscli-cwlogs && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/aws", "logs"]
CMD ["help"]
