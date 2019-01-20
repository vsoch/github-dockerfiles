# Signal Web

### Version 1.0.8

The signal Dashboard is a web application that allows users to configure
events, data stores, notifications, users, and other properties of
the signal-server.

## Setup

### to run for local development

```
npm run start:local
```

### testing

To run the tests

```
npm test
```


### Building the nginx container a specific  environment

Update the config file in `./config/production.js` to use your custom domain. This will build the static files to point to your domain.

First you have to build the index and js bundle:

```
npm run build
```

Then you can build the container with the static assets

```
docker build -t boundlessgeo/signal-server:web-dev .
```

### Cloud Foundry deployments
```
npm run build:devio
cd pcf/
cf push efc-web
```

### Running With Docker Compose ##

The following are the environment variables you will need to set in the environment section for `signal-server` in the docker-compose.yml :

```
SMTP_USERNAME=Amazon SES Username
SMTP_PASSWORD=Amazon SES Password
DB_HOST=db
--------Optional--------
DB_USER
DB_PASSWORD
```
