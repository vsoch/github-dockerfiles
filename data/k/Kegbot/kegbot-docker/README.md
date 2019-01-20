# Kegbot on Docker

Docker support for Kegbot.  

[![CircleCI](https://circleci.com/gh/Kegbot/kegbot-docker.svg?style=svg)](https://circleci.com/gh/Kegbot/kegbot-docker)

## Quick start

 Requirements:
* [Docker](https://docs.docker.com/engine/installation/) 1.12+
* [Docker-compose](https://docs.docker.com/compose/install/) 1.9+

To start Kegbot:
```bash
$ docker-compose up
```

To stop Kegbot:

```bash
$ docker-compose down
```

Data is saved in `~/tmp/kegbot` folder on the local disk to prevent data loss during restarts.
You can create a symbolic link should you choose to save the data somewhere else.


## Credit

Thanks to [@blalor/docker-kegbot-server](https://github.com/blalor/docker-kegbot-server)
and [@dencold/kegbot](https://github.com/dencold/kegbot) for inspiring this
project.
