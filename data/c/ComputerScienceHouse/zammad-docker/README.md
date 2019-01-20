# Zammad Docker

Docker images for the [Zammad](https://zammad.org) open source helpdesk/customer support system. Inspired by the [official images](https://github.com/zammad/zammad-docker-compose).

## Contents

This repository contains the build contexts for 2 images:

* [elasticsearch](https://hub.docker.com/computersciencehouse/zammad-elasticsearch) - Customized Elasticsearch image
* [zammad](https://hub.docker.com/computersciencehouse/zammad) - Main Zammad application and scheduler

The included `docker-compose.yml` will orchestrate these containers into a fully functioning instance of Zammad.

## Usage

#### elasticsearch

See [Elastic's documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html). Changes: removed X-Pack, added mapper-attachments.

Exposes Elasticsearch on port `9200`.

#### zammad

The `zammad` container can be configured with the following environment variables:

| Variable      | Description                                                          | Required |
|---------------|----------------------------------------------------------------------|----------|
| `DB_ADAPTER`  | Database adapter to use (options: `postgresql`, `mysql2`)            | Yes      |
| `DB_HOSTNAME` | Hostname of the database container or server                         | Yes      |
| `DB_PORT`     | Port of the database server (defaults to the adapter's default port) | No       |
| `DB_NAME`     | Name of the database                                                 | Yes      |
| `DB_USERNAME` | Username for the database user                                       | Yes      |
| `DB_PASSWORD` | Password for the database user                                       | No       |
| `ES_HOSTNAME` | Hostname of the `elasticsearch` container or external server         | Yes      |
| `ES_PORT`     | Port number of the Elasticsearch server (default: `9200`)            | Yes      |

Exposes Nginx on port `8080`. Internally, the Rails server (Puma) and the websockets server run on ports `3000` and `6042`, respectively.

## Persistence

Two volumes are required for proper persistence:

| Volume                 | Container       | Mount Point                        | Description        |
|------------------------|-----------------|------------------------------------|--------------------|
| `zammad-data`          | `zammad`        | `/opt/zammad/storage`              | Attachments        |
| `zammad-elasticsearch` | `elasticsearch` | `/usr/share/elasticsearch/data`    | Elasticsearch data |

See `docker-compose.yml` for an example.

## Differences

This repository is different from the [official images](https://github.com/zammad/zammad-docker-compose) in the following ways:

* Hostnames and database/Elasticsearch connections are configured through environment variables (which also makes using external services easy)
* Both MySQL and PostgreSQL are supported
* The application is not tied to a local volume and is only updated when the container is rebuilt
* Containers run as nonroot users off the bat instead of invoking gosu
* Permissions are handled for PaaS environments