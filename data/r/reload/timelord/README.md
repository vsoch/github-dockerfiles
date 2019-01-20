![Docker Badge](https://img.shields.io/docker/automated/reload/timelord.svg) ![Docker Badge](https://img.shields.io/docker/build/reload/timelord.svg)

# TimeLord
Timelord is a way to visually present data provided by the [Harvester](https://github.com/reload/harvester "Harvester") project. If you don't know what Harvester is, please go to the project and checkout the README file.

## Setup
There is only a few steps you need to follow for Timelord to be functioning with your Harvester project:

1. Clone the repository `git clone https://github.com/reload/timelord.git`
2. Copy the `config.inc.example` file to `config.inc` and fill out the configuration.

You should now have a fully functioning TimeLord project up and running.

## Local development setup

The local setup requires Docker and docker-compose.

Copy `.env.example` to `.env` and update the variables according to your harvestapp.com credentials, eg.:

```
HARVESTER_HARVEST_USER=harvest@example.com
HARVESTER_HARVEST_PASSWORD=secret
HARVESTER_HARVEST_ACCOUNT=companyname
```

`docker-compose up` will now give you a working timelord _and_ harvester. First time building Harvester will take a long time importing the database.

Alternately, you can edit `config.inc` and insert a remote URL to a Harvester environment, and then just `docker-compose up timelord`. Your local Time Lord container will then fetch data from the remote Harvester environment.

## Customize

We have setup a few steps that you should follow to get a fully customizable version up and running, if you wish to alter the styling or create further functionality.

First build the `node` container and install dependencies:
```
docker-compose build --force-rm node && \
docker-compose run --rm node npm install && \
docker-compose run --rm node bower install
```

To recompile everything, simply run grunt from inside the container:
```
docker-compose run --rm node grunt
```
