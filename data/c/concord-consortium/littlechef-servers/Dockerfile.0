FROM ruby:2.1.10

RUN apt-get update -qq && apt-get install -qq python-pip python-dev rsync

RUN pip install --upgrade cffi
RUN pip install littlechef

ENV APP_HOME /usr/src/app/
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY Gemfile .
COPY Gemfile.lock .

RUN bundle install

COPY Cheffile .
COPY Cheffile.lock .

# this is going to make a cookbooks folder in the working directory
RUN bundle exec librarian-chef install

# littlechef likes the file to have this new name now
COPY config.cfg littlechef.cfg
