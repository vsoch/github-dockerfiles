FROM node:6
MAINTAINER Onion Tech <webtech@theonion.com>

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /bulbs
WORKDIR /bulbs

# Only build NPM on config change
ADD package.json /bulbs/
RUN npm --loglevel=warn install

ENV PATH /bulbs/node_modules/.bin:$PATH

# Only build Bower on config change
ADD bower.json /bulbs/
RUN bower install --config.interactive=false install --allow-root

ADD . /bulbs

# NOTE: Tests would be faster if we build webpack here (instead of inside karma for each browser flavor).
