FROM ruby:2.4
MAINTAINER Cloud 66

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get dist-upgrade -y && apt-get autoremove && rm -rf /var/lib/apt

RUN mkdir -p /app
WORKDIR /app

ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock
RUN gem install bundler
RUN bundle config --global frozen 1
RUN bundle install --without development test

COPY . /app

ENV DEBIAN_FRONTEND teletype

CMD bundle exec jekyll serve

