FROM ruby:alpine
MAINTAINER Ivo von Putzer Reibegg <ivo.putzer@gmail.com>
RUN apk --no-cache add build-base \
 && gem install bundler
WORKDIR /wd
VOLUME /wd
EXPOSE 80
ENTRYPOINT ["bin/entrypoint"]
