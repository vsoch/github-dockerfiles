# Phoenix / Elixir Docker

Provides a Dockerfile and public image that you can use to develop and host a
Phoenix web application out of the box. 

## Build a new Phoenix Application

The following commands will mount the current directory and create a Phoenix
application in a new directory "test".  Because docker run's as root normally
you then need to make sure you change ownership back under your user.

``` bash
docker run -v $PWD:/code -it lonelyplanet/phoenix-elixir:latest phoenix.new test
sudo chown -R $USER:$USER ./test
```

## Creating Your Project's Dockerfile

In your project's base directory build a Dockerfile using this an example:

``` Dockerfile
FROM lonelyplanet/phoenix-elixir:latest

ENV MIX_ENV prod
ENV PORT 4000

ADD . /code
RUN mix deps.get
RUN npm install && /code/node_modules/brunch/bin/brunch build /code/
RUN bash -c "mix compile.protocols 2>&1"
RUN mix phoenix.digest
CMD elixir -pa /code/_build/prod/consolidated -S mix phoenix.server
```

This should be able to host your application in a production like environment.


## Developing With Docker-Compose

Use docker-compose to override and develop your project.  Here is an example of
a `docker-compose.yml` file:

``` yaml
database:
  image: postgres
  expose:
    - "5432"
app:
  build: .
  command: bash -c "npm install && mix phoenix.server 2>&1"
  volumes:
    - .:/code
  links:
    - database:database.local
  ports:
    - "4000:4000"
  environment:
    MIX_ENV: "dev"
```

**Note**: In your `config/dev.exs` you'll want to make sure you `hostname` is
set to `database.local`.  The default username and password of `postgres` should
work.
