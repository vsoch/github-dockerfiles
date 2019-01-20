FROM ruby:2.1.4

RUN mkdir -p /apps/lti2_tc

# Copy gems and libs to tmp and then run bundle install, by doing it this way it will be
# cached until the gemfile changes and will not need to be run on every build
COPY Gemfile* /tmp/
WORKDIR /tmp
RUN bundle install -j 4

ADD ./ /apps/lti2_tc
COPY ./docker/database.yml /apps/lti2_tc/config/

WORKDIR /apps/lti2_tc

EXPOSE 3000
