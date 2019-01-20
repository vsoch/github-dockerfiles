# signal-server

[![Build Status](https://travis-ci.org/boundlessgeo/signal.svg?branch=master)](https://travis-ci.org/boundlessgeo/signal)

### Version 1.0.8

### To run the migrations

Before running the migration you'll need to create a db and add the
extensions:

```
createuser signal --createdb -h localhost -U postgres
createdb signal -O signal -h localhost -U postgres
psql -U postgres -d signal -c "CREATE EXTENSION IF NOT EXISTS pgcrypto" -h localhost
psql -U postgres -d signal -c "CREATE EXTENSION IF NOT EXISTS postgis" -h localhost
psql -U signal   -d signal -c "CREATE SCHEMA IF NOT EXISTS signal" -h localhost
```

`lein migrate`

### Generate Sample Data

This will generate random data in all the tables of the database using [clojure.spec](https://clojure.org/about/spec) by running:

`lein sampledata`

### To run the tests

`lein test` or `lein test2junit` to generate a JUnit xml and html output

### To run the linter

`lein eastwood`

### To generate a code coverage report

`lein cloverage`

### To run the formatter

`lein cljfmt fix`

### To generate the docs

`lein codox`

### MQTT TLS setup

In order to connect to the MQTT broker, we need to present a valid
client certificate. To do this we must create a keystore to be used
by the service.

```
# create a keystore to hold the client cert and key
openssl pkcs12 -export -out keystore.p12 -in client.crt -inkey client.key
```

We may also need to tell the JVM to trust the CA that signed the client
certificate by setting up a custom trust store. This is required if the default
trust store doesn't contain the CA that signed your client certificate.

```
# create a copy the default trust store
cp $(JAVA_HOME)/jre/lib/security/cacerts custom-cacerts.jks

# import the custom CA into it
keytool -import -file ca.crt -alias "My Custom CA" -keystore custom-cacerts.jks
```

Then we can configure the server to use our keystores and truststores by
setting the following environment variables (which will get set to corresponding JVM system properties):

`TRUST_STORE, TRUST_STORE_TYPE, TRUST_STORE_PASSWORD, KEY_STORE, KEY_STORE_TYPE, KEY_STORE_PASSWORD`

If you need to deploy to a Cloud Foundry environment, you can deploy the container like this:

```
docker build -t quay.io/boundlessgeo/signal:devio .
docker push quay.io/boundlessgeo/signal:devio
cf push signal -o quay.io/boundlessgeo/signal:devio
```

## Using signal

To use signal, you must first sign up for an account, which you can do
using the [webapp](http://localhost:8080/signup) or the REST API

```
curl 'http://localhost:8085/api/users' \
--data-binary '{"name":"Mickey Mouse","email":"mickey@mouse.com","password":"test123"}' \
-H 'Content-Type: application/json'
```

Then you can exchange your account credentials for an access token, by
authenticating using the [webapp](http://localhost:8080/login) or REST
API

### REST Endpoints

All end points return a response of the for `{result:<result>,error:<error>}`

#### Authenticate (POST)

```
curl 'http://localhost:8085/api/authenticate' \
--data-binary '{"email":"mickey@mouse.com","password":"test123"}' \
-H 'Content-Type: application/json'
```

#### Create User `POST`

```
curl -XPOST 'http://localhost:8085/api/authenticate' \
--data-binary '{"email":"mickey@mouse.com","password":"test123"}' \
-H 'Content-Type: application/json'
```

#### List Users `GET`

```
curl -XGET 'http://localhost:8085/api/users'
```
