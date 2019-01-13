# Node.js 10.14.1 : https://github.com/nodejs/docker-node/blob/e1f2520c7a5f29dc5896edc3816357c0267cb931/10/alpine/Dockerfile
FROM node:10.14.1-alpine

# Ruby 2.5.3 : https://github.com/docker-library/ruby/blob/9af33e632f173e90b4a7aba7644f2080b574e54f/2.5/alpine3.8/Dockerfile
FROM ruby:2.5.3-alpine3.8

RUN apk add --no-cache libstdc++ # node runtime dependency

ENV NODE_VERSION 10.14.1
ENV YARN_VERSION 1.12.3

COPY --from=0 /usr/local/share/doc/node /usr/local/share/doc/node
COPY --from=0 /usr/local/include/node /usr/local/include/node
COPY --from=0 /usr/local/bin/node /usr/local/bin/node

COPY --from=0 /opt/yarn-v$YARN_VERSION /opt/yarn-v$YARN_VERSION
RUN ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
	  && ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg
