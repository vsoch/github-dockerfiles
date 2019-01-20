# community docker deployment

build the image:
docker build -t quran/quran.com-community .

run it:

`docker run --name community -d --link [name or id]:postgres quran/quran.com-community`

where `[name or id]` is the name or id of the database docker image.

note that this container needs to connect to the correct postgres server
(which requires updating config/database.yml to read from the environment
variables:

```
    host: <%= ENV['POSTGRES_PORT_5432_TCP_ADDR'] %>
    port: <%= ENV['POSTGRES_PORT_5432_TCP_PORT'] %>
```

one caveat is that nginx clears all environment variables that it passes
to its children, and hence the addition of `postgres-env.conf` to maintain
these.
