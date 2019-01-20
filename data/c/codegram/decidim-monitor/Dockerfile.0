FROM elixir:1.6.1

ARG MIX_ENV=prod

ENV PORT 4000
ENV MIX_ENV $MIX_ENV
ENV MIX_ARCHIVES=/.mix
ENV MIX_HOME=/.mix

WORKDIR /code

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y bash inotify-tools
RUN apt-get install -y nodejs

RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && \
    apt-get install nodejs

RUN mix local.hex --force \
    && mix local.rebar --force

COPY mix.exs .
COPY mix.lock .

RUN mix deps.get
RUN mix deps.compile

COPY frontend/package.json frontend/package.json
COPY frontend/package-lock.json frontend/package-lock.json

RUN cd frontend && \
    npm install

COPY frontend frontend

RUN if [ "${MIX_ENV}" = "prod" ]; then cd frontend && npm run build:prod; fi

COPY . .

RUN mix compile
RUN if [ "${MIX_ENV}" = "prod" ]; then mix phx.digest; fi