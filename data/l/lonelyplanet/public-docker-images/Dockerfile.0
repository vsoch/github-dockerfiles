FROM ubuntu:14.04

ENV PHOENIX_VERSION 1.1.4

# Elixir requires UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# update and install base requirements
RUN apt-get update \
    && apt-get install -y curl wget git make

# download and install Erlang package
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
    && dpkg -i erlang-solutions_1.0_all.deb \
    && apt-get update \
    && apt-get install -y elixir erlang \
    && rm erlang-solutions_1.0_all.deb

# install the Phoenix mix archive
RUN mix archive.install --force \
    https://github.com/phoenixframework/archives/raw/master/phoenix_new-$PHOENIX_VERSION.ez

# install hex and rebar, they are needed to compile a phoenix application
RUN mix local.hex --force \
    && mix hex.info \
    && mix local.rebar --force

# install Node.js (>= 5.0.0) and NPM in order to satisfy brunch.io dependencies
# See http://www.phoenixframework.org/docs/installation#section-node-js-5-0-0-
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash - && apt-get install -y nodejs

# install postgres-client for ecto and inotify-tools for live-reloading
RUN apt-get install -y postgresql-client inotify-tools

# setup /code as the workspace
RUN mkdir /code
WORKDIR /code
