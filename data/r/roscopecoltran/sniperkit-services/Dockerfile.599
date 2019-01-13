FROM asakaguchi/ngx-mruby
MAINTAINER asakaguchi

ENV TDIARY_ROOT=/opt/tdiary \
    CONFIG=/root/config


COPY config ${CONFIG}/

RUN set -x \
  && apk --update add git \
                      apache2-utils \
                      ruby \
                      build-base \
                      ruby-bigdecimal \
                      ruby-bundler \
                      ruby-dev \
                      ruby-io-console \
                      ruby-json \                      
  && gem update --no-document \
  && gem install tdiary --no-document \
  && tdiary new ${TDIARY_ROOT} --skip-bundle \
  && cd ${TDIARY_ROOT} \
  && cp ${CONFIG}/nginx* ${CONFIG}/Procfile . \
  && if [ -e ${CONFIG}/Gemfile.local ]; then cp ${CONFIG}/Gemfile.local .; fi \
  && bundle install --without test development --jobs=4 --retry=3 \
  && if [ -e ${CONFIG}/tdiary.conf ]; then cp ${CONFIG}/tdiary.conf .; fi \
  && if [ -e ${CONFIG}/.htpasswd ]; then cp ${CONFIG}/.htpasswd .; else htpasswd -bcd .htpasswd tdiary tdiary; fi \
  && git clone https://github.com/tdiary/tdiary-theme.git theme \
  && apk del git apache2-utils build-base ruby-dev \
  && rm -rf /var/cache/apk/*

WORKDIR /opt/tdiary

CMD ["bundle", "exec", "foreman", "start"]