FROM ruby:2.1.5

ENV RAILS_ROOT /var/www/monocle
ENV GEM_PATH $RAILS_ROOT/.localgems
WORKDIR $RAILS_ROOT

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev postgresql-client wget ruby-dev zlib1g-dev liblzma-dev libgmp3-dev software-properties-common vim imagemagick advancecomp gifsicle jhead jpegoptim libjpeg-progs optipng pngcrush pngquant \
  && mkdir -p $RAILS_ROOT/tmp/pids \
  && cd $RAILS_ROOT \
  && gem install bundler \
  && apt-get purge -y build-essential libpq-dev 

COPY .localgems .localgems/
COPY . .

RUN gem update && gem update --system
RUN bundle install --path .localgems

ENTRYPOINT [ "bash","config/containers/start_server.sh" ]
