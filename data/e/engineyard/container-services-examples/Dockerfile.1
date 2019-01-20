FROM ruby:2.3-alpine

RUN apk add --no-cache \
    # Runtime deps
    tzdata nodejs bash \
    # Bundle install deps
    build-base postgresql-dev postgresql-client

ENV APP_HOME=/app
RUN mkdir -p ${APP_HOME} /usr/local/bin
WORKDIR ${APP_HOME}

ADD ./scripts/wait-for-tcp.sh /usr/local/bin/

ADD ./spina_sample_app/Gemfile ./spina_sample_app/Gemfile.lock ${APP_HOME}/
RUN bundle install && true

ADD ./spina_sample_app/ ${APP_HOME}/
ADD ./config/ ${APP_HOME}/config/
RUN bundle exec rake assets:precompile

ENV RAILS_LOG_TO_STDOUT=true \
    RAILS_SERVE_STATIC_FILES=true

ENV RAILS_ENV=development \
    DB_HOST=database \
    DB_PORT=5432 \
    DB_NAME= \
    DB_USER= \
    DB_PASSWORD= \
    SECRET_KEY_BASE=

VOLUME ${APP_HOME}/tmp

CMD wait-for-tcp.sh $DB_HOST $DB_PORT && bundle exec puma
