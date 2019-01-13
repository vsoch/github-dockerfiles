FROM alpine:3.4
MAINTAINER smizy

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.license="Apache License 2.0" \
    org.label-schema.name="smizy/fasttext" \
    org.label-schema.url="https://github.com/smizy" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-type="Git" \
    org.label-schema.vcs-url="https://github.com/smizy/fasttext"
    
RUN set -x \
    && apk update \
    && apk --no-cache add \
        bash \
        libstdc++ \
    && apk --no-cache add --virtual .builddeps \
        build-base \
        git \
    ## fastText 
    && git clone https://github.com/facebookresearch/fastText.git \
    && cd fastText \
    && make \
    && mv fasttext /usr/local/bin/ \
    && rm -rf .git \       
    && cd .. \
    && apk del  .builddeps \
    && adduser -D  -g '' -s /sbin/nologin -u 1000 docker



