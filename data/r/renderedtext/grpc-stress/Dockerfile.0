FROM renderedtext/elixir:1.4


ENV TERM=xterm
ENV MIX_ENV=prod

COPY mix* ./
COPY config/ config/

RUN mix do local.hex --force, local.rebar --force, deps.get, compile; \
    chown developer.developer -R ../

COPY lib lib/
COPY test test/

RUN chown developer.developer -R lib test

USER developer
RUN mix compile

CMD elixir --sname ex_client -S mix run --no-halt

