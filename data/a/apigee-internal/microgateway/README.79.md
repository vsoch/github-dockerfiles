# Docker for Microgateway
The following steps will allow you to run Microgateway as a Docker container.

## Pre-requisites
* Microgateway is configured against an org/environment
* User has the configuration file for microgateway
* User has the credentials to start microgateway

### Step 1: Download Microgateway container for docker
```
docker pull gcr.io/apigee-microgateway/edgemicro:latest
```
Use a tag to download a specific version

### Step 2: Base64 encode the microgateway configuration file
```
export EDGEMICRO_CONFIG=`base64 $HOME/.edgemicro/org-test-config.yaml`
```

NOTE: This version of docker accepts a microgateway configuration as a base64 encoded string. This allows you to pass the configuration file as an environment variable. When using Kubernetes, the configuration file can be stored in a Kubernetes Secret entity.

### Step 3: Start Microgateway with params
```
docker run -P -p 8000:8000 -d --name edgemicro -v /var/tmp:/opt/apigee/logs -e EDGEMICRO_PROCESS=1 -e EDGEMICRO_ORG=org -e EDGEMICRO_ENV=test -e EDGEMICRO_KEY=xxx -e EDGEMICRO_SECRET=xxx -e EDGEMICRO_CONFIG=$EDGEMICRO_CONFIG -e SERVICE_NAME=edgemicro --security-opt=no-new-privileges --cap-drop=ALL gcr.io/apigee-microgateway/edgemicro:latest
```

P = publish all exposed ports to the host
d = run in detached mode
v = volume mount for logs
expose port 8443 if you are expose node.js over TLS

List of environment variables
* `EDGEMICRO_ORG` = Apigee Edge org name
* `EDGEMICRO_ENV` = Apigee Edge environment name
* `EDGEMICRO_PROCESSES` = Number of worker processes to start
* `EDGEMICRO_KEY` = Microgateway key 
* `EDGEMICRO_SECRET` = Microgateway secret
* `EDGEMICRO_CONFIG` = A base64 encoded string of the microgateway config file
* `SERVICE_NAME` = set to "default" (used in Kubernetes)
* `DEBUG` = `*` to enable debugging
* `HTTP_PROXY` = set http proxy ex: http_proxy=http://10.203.0.1:5187/
* `HTTPS_PROXY` = set https proxy ex: https_proxy=https://10.203.0.1:5187/
* `NO_PROXY` = skip/bypass proxy ex: "localhost,127.0.0.1,localaddress,.localdomain.com"

### Step 4: Stop Microgateway
```
docker stop edgemicro
```

NOTE: You can now restart Microgateway using this command
```
docker start edgemicro
```

## TLS certificates
The container has a mount point on `/opt/apigee/.edgemicro`. You can load the certificates on the mount point and refer to it from the `org-env-config.yaml`

### Self signed certificates
If you are using CA not trusted by default by node.js, consider using
`NODE_EXTRA_CA_CERTS` = A file path to the file that should consist of one or more trusted certificates in PEM format

Whlie we recommend this flag never be used, you could also set
`NODE_TLS_REJECT_UNAUTHORIZED` = 1
to turn off validation. This option is NOT provided in the default docker image. Please build a new image to support this option.


### Example to setup Northbound TLS

Here is an example of how to use this feature (along with self-signed certificates) for setting:

#### Preparation
In the opensssl.cnf file, add the following stanza to generate the right SNI attributes
```
[ alt_names ]
DNS.1 = www.srinandans.com
DNS.2 = srinandans.com
DNS.3 = localhost
DNS.4 = localhost.localdomain
DNS.5 = 127.0.0.1
DNS.6 = ::1
DNS.7 = fe80::1
```
#### Generate self signed certificates

```
#!/bin/bash

# generate ca
openssl genrsa -out rootca.key 2048
openssl req -x509 -new -nodes -key rootca.key -sha256 -days 1024 -out rootca.pem
# generate key
openssl genrsa -out tls.key 2048
openssl req -new -key tls.key -out tls.csr
# sign cert
openssl x509 -req -in tls.csr -CA rootca.pem -CAkey rootca.key -CAcreateserial -out tls.crt -days 1024 -sha256 -extensions 'v3_req' -extfile openssl.cnf
```

This should generate the following files:
* rootca.key
* rootca.pem
* tls.key
* tls.csr
* rootca.srl
* tls.crt

#### Change the config.yaml

```
edge_config:
...
edgemicro:
  port: 8443
  max_connections: 1000
  config_change_poll_interval: 600
  ssl:
    key: /opt/apigee/.edgemicro/tls.key
    cert: /opt/apigee/.edgemicro/tls.crt
    passphrase: admin123
    rejectUnauthorized: true
    requestCert: false
  logging:
  ...
```
Observe the changes to `port`, and the `ssl` stanza.

#### Start docker

```
docker run -P -p 8443:8443 -d --name edgemicro -v ~/workspace/tmp/tls:/opt/apigee/.edgemicro -v ~/workspace/tmp/tls:/opt/apigee/logs -e NODE_EXTRA_CA_CERTS=/opt/apigee/.edgemicro/rootca.pem -e EDGEMICRO_PORT=8443 -e EDGEMICRO_ORG=$EDGEMICRO_ORG -e EDGEMICRO_ENV=$EDGEMICRO_ENV -e EDGEMICRO_KEY=$EDGEMICRO_KEY -e EDGEMICRO_SECRET=$EDGEMICRO_SECRET -e EDGEMICRO_CONFIG=$EDGEMICRO_CONFIG gcr.io/apigee-microgateway/edgemicro
```

Observe a few changes:
* `port` is set to `8443`
* A volume mount was use to mount the key and cert
* use `NODE_EXTRA_CA_CERTS` to add any custom CA (like in the case of self-signed certs)

#### Test it

Here is a cURL command to test the setup

```
curl https://localhost:8443/httpbin/get --cacert rootca.pem -v -H "x-api-key: xxx"
```

OUTPUT:
```
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 8443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* Cipher selection: ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH
* successfully set certificate verify locations:
*   CAfile: rootca.pem
  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Client hello (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: C=CA; ST=Ontario; L=Toronto; O=Google Canada; OU=Google Cloud Platform; CN=edgemicro; emailAddress=sxxxxxxxxs@google.com
*  start date: Dec 10 02:12:22 2018 GMT
*  expire date: Sep 29 02:12:22 2021 GMT
*  subjectAltName: host "localhost" matched cert's "localhost"
*  issuer: C=CA; ST=Ontario; L=Toronto; O=Google Canada; OU=Google Cloud Platform; CN=edgemicro; emailAddress=sxxxxxxxxs@google.com
*  SSL certificate verify ok.
> GET /httpbin/get HTTP/1.1
> Host: localhost:8443
> User-Agent: curl/7.54.0
> Accept: */*
> x-api-key: Tg0aiH9kZS2N4AP6AxlqYWwFwDdLmm6u
>
< HTTP/1.1 200 OK
< server: gunicorn/19.9.0
....
....
....
```

### Example to setup southbound TLS

In this setup you'll setup TLS to a target/southbound application

#### Preparation

In the opensssl.cnf file, add the following stanza to generate the right SNI attributes
```
[ alt_names ]
DNS.1 = helloworld
DNS.2 = localhost
DNS.3 = localhost.localdomain
DNS.4 = 127.0.0.1
DNS.5 = ::1
DNS.6 = fe80::1
```

#### Sample application

Here is a sample node.js application that will serve as a target app

server.js
```
'use strict';

const express = require('express');
const https = require('https');
const fs = require('fs');


const options = {
  key: fs.readFileSync("tls.key"),
  cert: fs.readFileSync("tls.crt")
};

// Constants
const PORT = 9443;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello world\n');
});

https.createServer(options, app).listen(PORT);
```

Dockerfile
```
FROM node:8-alpine
WORKDIR /usr/src/app
COPY package*.json ./

RUN npm install
COPY . .
EXPOSE 9443
CMD [ "npm", "start" ]
```

build the Docker image

```
docker build -t helloworld . 
```

#### Start the sample app

```
docker run -P -p 9443:9443 --name helloworld helloworld
```

#### Create a edgemicro proxy in Edge

Proxy name: `edgemicro_local`
Revision: `1`
Basepath: `/local`
Target: `https://helloworld:9443`

Create a Product and Developer App (please see Microgateway docs on how these are setup).

#### Start Microgateway

```
docker run -P -p 8443:8443 -d --name edgemicro -v ~/workspace/tmp/tls:/opt/apigee/.edgemicro -v ~/workspace/tmp/tls:/opt/apigee/logs -e EDGEMICRO_PORT=8443 -e EDGEMICRO_ORG=$EDGEMICRO_ORG -e EDGEMICRO_ENV=$EDGEMICRO_ENV -e EDGEMICRO_KEY=$EDGEMICRO_KEY -e EDGEMICRO_SECRET=$EDGEMICRO_SECRET -e EDGEMICRO_CONFIG=$EDGEMICRO_CONFIG --link helloworld:helloworld gcr.io/apigee-microgateway/edgemicro
```

NOTE: We have used `--link` to link the two containers.

Test the proxy:
```
curl https://localhost:8443/local -k -H "x-api-key: xxxx" -v
```

You should see an error:
```
...
*  subject: C=CA; ST=Ontario; L=Toronto; O=Google Canada; OU=Google Cloud Platform; CN=edgemicro; emailAddress=srinandans@google.com
*  start date: Dec 10 02:12:22 2018 GMT
*  expire date: Sep 29 02:12:22 2021 GMT
*  issuer: C=CA; ST=Ontario; L=Toronto; O=Google Canada; OU=Google Cloud Platform; CN=edgemicro; emailAddress=srinandans@google.com
*  SSL certificate verify result: unable to get local issuer certificate (20), continuing anyway.
> GET /local HTTP/1.1
> Host: localhost:8443
> User-Agent: curl/7.54.0
> Accept: */*
> x-api-key: 9fVC65pFj8LrmlPmVyxFjx4KgAHTxqSd
>
< HTTP/1.1 502 Bad Gateway
< Date: Wed, 12 Dec 2018 05:25:01 GMT
< Connection: keep-alive
< Content-Length: 93
<
* Connection #0 to host localhost left intact
{"message":"unable to verify the first certificate","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

Re-run MG, but this time with the NODE_EXTRA_CA_CERTS variable set. 
NOTE: The pem file in the NODE_EXTRA_CA_CERTS variable must have the target's CA (in this case `helloworld`)

```
docker run -P -p 8443:8443 -d --name edgemicro -v ~/workspace/tmp/tls:/opt/apigee/.edgemicro -v ~/workspace/tmp/tls:/opt/apigee/logs -e NODE_EXTRA_CA_CERTS=/opt/apigee/.edgemicro/rootca.pem -e EDGEMICRO_PORT=8443 -e EDGEMICRO_ORG=$EDGEMICRO_ORG -e EDGEMICRO_ENV=$EDGEMICRO_ENV -e EDGEMICRO_KEY=$EDGEMICRO_KEY -e EDGEMICRO_SECRET=$EDGEMICRO_SECRET -e EDGEMICRO_CONFIG=$EDGEMICRO_CONFIG --link helloworld:helloworld gcr.io/apigee-microgateway/edgemicro
```

Expected output:
```
...
> GET /local HTTP/1.1
> Host: localhost:8443
> User-Agent: curl/7.54.0
> Accept: */*
> x-api-key: 9fVC65pFj8LrmlPmVyxFjx4KgAHTxqSd
>
< HTTP/1.1 200 OK
< x-powered-by: Express
< content-type: text/html; charset=utf-8
< etag: W/"c-M6tWOb/Y57lesdjQuHeB1P/qTV0"
< date: Wed, 12 Dec 2018 05:49:28 GMT
< x-response-time: 421
< Connection: keep-alive
< Transfer-Encoding: chunked
<
Hello world
```

## Using custom plugins
There are two options to deal with custom plugins:

### Option 1: Mount the plugins

Plugins can be mounted on the volume `/opt/apigee/plugins`
```
docker run -v /volume/mount:/opt/apigee/plugins .....
```

### Option 2: Build plugins into the container

Build a new container with the plugins

Here is an example:
```
FROM gcr.io/apigee-microgateway/edgemicro:latest
USER root
RUN apk update && \
    apk upgrade && \
    apk add zip && \
    mkdir /opt/apigee/customplugins && \
    chown apigee:apigee /opt/apigee/customplugins
COPY plugins.zip /opt/apigee/customplugins
RUN su - apigee -c "unzip /opt/apigee/customplugins/plugins.zip -d /opt/apigee/customplugins"
EXPOSE 8000
EXPOSE 8443
USER apigee
ENTRYPOINT ["entrypoint"]
```

Build the new docker image
```
docker build -t edgemicrocustomplugin .
```

Start the new image
```
docker run -P -p 8000:8000 -d --name edgemicrocustomplugin -e EDGEMICRO_PLUGIN_DIR=/opt/apigee/customplugins/plugins -e EDGEMICRO_ORG=$EDGEMICRO_ORG -e EDGEMICRO_ENV=$EDGEMICRO_ENV -e EDGEMICRO_KEY=$EDGEMICRO_KEY -e EDGEMICRO_SECRET=$EDGEMICRO_SECRET -e EDGEMICRO_CONFIG=$EDGEMICRO_CONFIG -e SERVICE_NAME=edgemicrocustomplugin edgemicrocustomplugin
```