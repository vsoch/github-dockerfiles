FROM alpine:3.7

RUN mkdir -p /test/foo && \
   touch /test/foo/1 /test/foo/2 && \
   mkdir -p /test/foo/bar && \
   touch /test/foo/bar/3
RUN rm -rf /test/foo/*
