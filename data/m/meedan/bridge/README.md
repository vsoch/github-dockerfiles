# Bridge

Translate the Global Web

This is a [Docker Compose](https://docs.docker.com/compose/) configuration that spins up the whole Bridge app locally. Tested on Linux and Mac OS X (with [Docker for Mac](https://www.docker.com/products/docker#/mac)). The repo contains two Docker Compose files, one for development (`docker-compose.yml`) and the other for testing (`docker-test.yml`).

## DO NOT USE IN PRODUCTION! THIS IS ONLY MEANT AS A DEVELOPMENT ENVIRONMENT.

- Install `docker-compose`
- `git clone --recursive git@github.com:meedan/bridge.git && cd bridge`
- Configuration - copy and edit the following files:
  - `bridge-web/config.js.example` to `bridge-web/config.js`
  - `bridge-web/test/config.js.example` to `bridge-web/test/config.js`
  - `bridge-web/test/config.yml.example` to `bridge-web/test/config.yml`
  - `bridge-reader/config/bridgembed.yml.example` to `bridge-reader/config/bridgembed.yml`
  - `bridge-reader/config/database.yml.example` to `bridge-reader/config/database.yml`
  - `check-api/config/config.yml.example` to `check-api/config/config.yml`
  - `check-api/config/database.yml.example` to `check-api/config/database.yml`
  - `check-api/config/sidekiq.yml.example` to `check-api/config/sidekiq.yml`
  - `pender/config/config.yml.example` to `pender/config/config.yml`
  - `pender/config/database.yml.example` to `pender/config/database.yml`
- Update your [virtual memory settings](https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html), e.g. by setting `vm.max_map_count=262144` in `/etc/sysctl.conf`
- `docker-compose pull && docker-compose build --pull && docker-compose up`

## Available services and container names

### `development` mode using `docker-compose.yml`

- Bridge web client (container `web`) at [http://localhost:3333](http://localhost:3333)
- Bridge Reader web client (container `reader`) at [http://localhost:3400](http://localhost:3400)
- Check service API (container `api`) at [http://localhost:3000/api](http://localhost:3000/api) - use `dev` as API key
- Check service GraphQL at [http://localhost:3000/graphiql](http://localhost:3000/graphiql)
- Pender service API (container `pender`) at [http://localhost:3200/api](http://localhost:3200/api) - use `dev` as API key
- Alegre service API (container `alegre`) at [http://localhost:3100](http://localhost:3100) - no need for an API key
- Elasticsearch API (container `elasticsearch`) at [http://localhost:9200](http://localhost:9200)
- PostgreSQL (container `postgres`) at `localhost:5432` (use a standard Pg admin tool to connect)

### `test` mode using `docker-test.yml`

- Bridge web client (container `web.test`) at [http://localhost:13333](http://localhost:13333)
- Bridge Reader web client (container `reader.test`) at [http://localhost:13400](http://localhost:13400)
- Check service API (container `api.test`) at [http://localhost:13000/api](http://localhost:13000/api) - use `test` as API key
- Check service GraphQL at [http://localhost:13000/graphiql](http://localhost:13000/graphiql)
- Pender service API (container `pender.test`) at [http://localhost:13200/api](http://localhost:13200/api) - use `test` as API key
- Alegre service API (container `alegre`) at [http://localhost:3100](http://localhost:3100) - no need for an API key
- Elasticsearch API (container `elasticsearch`) at [http://localhost:9200](http://localhost:9200)
- PostgreSQL (container `postgres`) at `localhost:5432` (use a standard Pg admin tool to connect)
- Chromedriver (container `chromedriver`) at [http://localhost:4444/wd/hub](http://localhost:4444/wd/hub)
- Chromedriver VNC at `localhost:5900` (use a standard VNC client to connect with password `secret`)

## Testing

- Build the app in test mode: `docker-compose -f docker-test.yml pull && docker-compose -f docker-test.yml build --pull`
- Start the app in test mode: `docker-compose -f docker-test.yml up`
- Bridge web client: `docker-compose -f docker-test.yml run web.test npm run test`
- Check service: `docker-compose -f docker-test.yml run api.test bundle exec rake test`
- Pender service: `docker-compose -f docker-test.yml run pender.test bundle exec rake test`
- Running a specific Bridge web client test: `docker-compose -f docker-test.yml run web.test bash -c "cd test && rspec --example KEYWORD spec/integration_spec.rb"`
- Running a specific Check API or Pender test (from within the container): `ruby -I"lib:test" test/path/to/specific_test.rb -n /.*KEYWORD.*/`

## Helpful one-liners and scripts

- Build the web client bundle: `docker-compose run web npm run build`
- Restart a service, e.g. Check API: `docker-compose run api bash -c "touch tmp/restart.txt"`
- Invoke the Rails console on a service, e.g. Check API: `docker-compose run api bundle exec rails c d`
- Reset the `api.test` database: `docker-compose -f docker-test.yml run api.test bundle exec rake db:drop db:create db:migrate`
- Update submodules to their latest commit: `./bin/git-update.sh`
- Cleanup docker images and volumes: `./bin/docker-clean.sh`
- Packing your local config files: `./bin/tar-config.sh`
- Run a standalone image, e.g. Pender: `docker run -e SERVER_PORT=3200 -e RAILS_ENV=test -p 3200:3200 -v /absolute/path/to/check-app/pender:/app bridge_pender`

## More documentation

- [Check service API](https://github.com/meedan/check-api)
- [Bridge web client](https://github.com/meedan/bridge-web)
- [Bridge Reader web client](https://github.com/meedan/bridge-reader)
- [Pender service API](https://github.com/meedan/pender)
- [Alegre service API](https://github.com/meedan/alegre)
- [Bridge bot](https://github.com/meedan/bridge-bot)

## Troubleshooting and known issues

- Upon initial installation, the submodules may be checked out at a specific commit instead of the `develop` branch. You will need to go into each submodule and issue an explicit `git checkout develop`.
- Upon initial installation, to make sure the frontend is up to date, issue an explicit `docker-compose exec web npm run build`.
