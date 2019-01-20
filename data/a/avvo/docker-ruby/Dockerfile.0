FROM avvo/alpine
RUN apk update \
  && apk add ruby \
  && gem install --no-document bundler \
  && mkdir /srv
RUN rm -f /var/cache/apk/*
VOLUME ["/srv"]

CMD ["/usr/bin/ruby", "--version"]
