# Leonidas SMS gateway

[![Build Status](https://drone.plat2.leonidasoy.fi/api/badges/leonidas/leonidas-smsgw/status.svg)](https://drone.plat2.leonidasoy.fi/leonidas/leonidas-smsgw)

## Features

* Provides a single integration point for whatever SMS service we will be using in the future
* Counts messages by customer (hierarchically, customers-of-customers supported to an arbitrary depth)

## Supported backends

Please submit further backends via pull requests.

* **Labyrintti/LINK Mobility**: Production-ready, in production use at Leonidas.
* **Mock**: Useful for testing.

## Getting Started

### Docker Compose

    docker-compose up

    alias dc-test="docker-compose -f docker-compose.test.yml up --exit-code-from=test"
    dc-test

### Manually

Have a Redis running on port 6379. All your base are belong to us.

    yarn install
    yarn start
    yarn test

## Configuration

Via environment variables. See [Config.ts](https://github.com/leonidas/leonidas-smsgw/blob/master/src/Config.ts).

## API

### POST `/api/v1/messages`

Body:

```json
{
    "customer": "leonidas.platform",
    "message": "Hello, World!",
    "recipients": ["+3585551235"],
    "sender": "+3585551234"
}
```

Successful response (`201 Created`):

```json
{
    "success": true,
    "recipients": [{
        "recipient": "+3585551235",
        "success": "true",
        "statusMessage": "1 message succesfully queued for sending"
    }]
}
```

### `/api/v1/users`

CRUD user management. See [users.test.ts](https://github.com/leonidas/leonidas-smsgw/blob/master/src/controllers/users.test.ts) until properly documented.

### GET `/metrics`

Response:

```
# HELP smsgw_messages Sent SMS messages by customer
# TYPE smsgw_messages counter
smsgw_messages{customer0="leonidas"} 0
```

## Deployment

This project is using the [Leonidas Platform Drone CI](https://drone.plat2.leonidasoy.fi/leonidas/leonidas-360gateway). All pushes to `master` will trigger a production deployment.

If you need to deploy manually, the command to deploy from your working copy is

    ./deploy.sh

## TODO

### Future features

* [ ] JSON endpoint for accounting information (currently only Prometheus metrics provided)
* [ ] Inbound messages
* [ ] Mask passwords from logs (perhaps fork/hack `winston-console-formatter` for this)
* [ ] Restrict sender numbers by user/customer
* [ ] Restrict customers by user
* [ ] Configurable per-user rate limiting

### Untyped packages

Write type wrappers or get rid of.

* [ ] `winston-console-formatter`
* [ ] `koa-request-logger`
* [ ] `fluent-logger`
