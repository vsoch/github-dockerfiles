FROM ruby:2.3

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends build-essential libpq-dev nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
