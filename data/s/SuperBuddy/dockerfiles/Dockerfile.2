FROM appropriate/curl
MAINTAINER svlentink <sander@superbuddy.nl>
LABEL version="0.4"
# 0.1 basics, based on debian
# 0.2 basics based on curl
# 0.3 file structure change
# 0.4 inverse operation allowed

#RUN ln -s /bin/sh /bin/bash
RUN apk add --update bash && rm -rf /var/cache/apk/*

COPY entrypoint.sh /usr/local/bin/entrypoint
ENV testdir=/usr/bin/curltests
COPY tests $testdir
ENV testlib=/usr/lib/testlib.sh
COPY testlib.sh $testlib

RUN mkdir /var/log/tests
ENV passedLogFile=/var/log/tests/pass.log
ENV failedLogFile=/var/log/tests/fail.log

VOLUME /totest

ENTRYPOINT /usr/local/bin/entrypoint
#ENTRYPOINT /bin/bash