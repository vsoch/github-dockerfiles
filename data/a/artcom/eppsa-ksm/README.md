# EPPSA KSM

Game and CMS setup behind an nginx server as reverse proxy.

`git clone --recursive https://github.com/artcom/eppsa-ksm.git`

## Requirements

### Certificate
Use the production certificate or create a self-signed development certificate as follows.

Copy `certificate/development/openssl.cnf.template` to `certificate/development/openssl.cnf` and set your environment name:

```
[alt_names]
...
DNS.2 = *.<environment>.eppsa.de
```

Create certificate:

```
cd certificate/development
mkdir -p live/eppsa.de
openssl req -new -newkey rsa:2048 -sha1 -days 3650 -nodes -x509 -keyout ./live/eppsa.de/privkey.pem -out ./live/eppsa.de/fullchain.pem -config openssl.cnf
```

The development certificate points to `*.eppsa.de`. Set the correct path in CERTIFICATE_PATH below.

### Local Service Lookup
  * For local development:
    * /etc/hosts:
    ```
    127.0.0.1 cms.local.eppsa.de
    127.0.0.1 game.local.eppsa.de
    127.0.0.1 asset-server.local.eppsa.de
    127.0.0.1 content-server.local.eppsa.de
    127.0.0.1 content.local.eppsa.de
    127.0.0.1 game-server.local.eppsa.de
    127.0.0.1 dashboard.local.eppsa.de
    127.0.0.1 <challenge>.local.eppsa.de
    ```
  * Certificate for `*.eppsa.de` or for each subdomain `*.<environment>.eppsa.de`

### Docker & Docker Compose
  * [Docker](https://docs.docker.com/install/)

## Run
Set environment variable for the path to the ssl certificate:
  * `CERTIFICATE_PATH=/path/to/certificate`

Set the HOST variable of your target environment:
  * `HOST=<environment>.eppsa.de`

### Build Images
`docker-compose -f docker-compose.yml -f docker-compose.development.yml build`

### Start Containers
`docker-compose -f docker-compose.yml -f docker-compose.development.yml up`

### Open (local)
* Game: https://game.local.eppsa.de/
* CMS: https://cms.local.staging.eppsa.de/
* Dashboard: https://dashboard.local.eppsa.de/

## Production
```
HOST=<environment>.eppsa.de
./build.sh
docker-compose -f docker-compose.yml -f docker-compose.production.yml build
docker-compose -f docker-compose.yml -f docker-compose.production.yml up
```

#### Troubleshooting (Development)

##### Missing npm packages
When you need to recreate a volume (but not "named volumes"), first use the following commands before using 'up':
```
docker-compose -f docker-compose.yml -f docker-compose.development.yml stop
docker-compose -f docker-compose.yml -f docker-compose.development.yml rm
```
This will be necessary if you want to install new node dependencies using `npm install` during the build.

##### Browser does not allow access to subdomains
You have to trust the self-signed certificate for each subdomain in your browser.

## Content

### Transfer content into the docker environment:

```
git clone https://github.com/artcom/eppsa-ksm-content
cd eppsa-ksm-content
git remote add docker https://content.<environment>.eppsa.de
git push -f docker master
```

#### Troubleshooting

When using a self-signed certificate you have to allow an insecure connection:

`git config http.sslVerify "false"`

Be aware to reset this after your operation

`git config http.sslVerify "true"`
