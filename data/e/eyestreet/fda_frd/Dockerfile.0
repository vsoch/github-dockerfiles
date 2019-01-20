FROM ruby:2.2.2

RUN apt-get update -qq && apt-get install -y \
    build-essential \
    nodejs

WORKDIR /tmp
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock
RUN bundle install

ADD . /fda-frd

WORKDIR /fda-frd

# RUN RAILS_ENV=production bundle exec rake assets:precompile --trace
# CMD ["rails","server","-b","0.0.0.0"]
