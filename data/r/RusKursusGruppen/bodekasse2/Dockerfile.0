FROM elixir:latest
RUN  mix local.hex --force && \
     mix local.rebar --force && \
     mix archive.install https://github.com/phoenixframework/archives/raw/master/phx_new.ez
COPY bodekasse /code
WORKDIR /code
RUN mix deps.get
