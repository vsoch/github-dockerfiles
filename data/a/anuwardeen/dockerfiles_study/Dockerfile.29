#
# Ruby runtime Dockerfile
#
# https://github.com/dockerfile/ruby-runtime
#

# Pull base image.
FROM dockerfile/ruby

# Set instructions on build.
ONBUILD ADD Gemfile /app/
ONBUILD ADD Gemfile.lock /app/
ONBUILD RUN bundle install
ONBUILD ADD . /app

# Define working directory.
WORKDIR /app

# Set environment variables.
ENV APPSERVER webrick

# Define default command.
CMD bundle exec rackup -p 8080 /app/config.ru -s $APPSERVER

# Expose ports.
EXPOSE 8080
