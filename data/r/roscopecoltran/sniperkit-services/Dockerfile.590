FROM ruby:2.3-alpine

MAINTAINER Akiyoshi Sakaguchi <autumngoodluck@gmail.com>

RUN apk add --update build-base \
  && gem install magellan-cli \
  && apk del build-base \
  && rm -rf /var/cache/apk/*