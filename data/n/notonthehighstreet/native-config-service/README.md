# App Config Service
App Config Service is a Docker based microservice written in swift, it enables you to provide application level config for your applications.  It is currently running in production at notonthehigstreet.com providing the configuration elements for our main iOS and AppleTV applications.

## Overview
The application retrieves the configuration from a Consul [https://www.consul.io](https://www.consul.io) server which is a highly distributed key value store. Consul template runs inside the container and listens for changes to the data in Consul, either first run or when a change is detected Consul template retrieves the data and transforms it into a JSON formatted config file which the server reads.  When the client connects to the service using the RESTful API the service returns the requested config from the internal store and returns this as JSON.

## Restful API
### GET /v1/config
This is the main endpoint which is used to retrieve config from the service.

#### url
**/v1/config/:application/:branch/[optional :device]**

#### parameters

| Name |                                                                     |
| ----------------- | -------------------------------------------------------
| application       | The name of the application
| branch            | The branch to use, allows A/B testing
| device [optional] | The device type, defaults to "default" if not specified   
  
#### response
##### 200 OK
If all the parameters are valid then the service will return a 200 OK and the following response body which corresponds to your configuration.

**body**
```json
{
  "products_validation" : "product_validation\/v1\/product_validation",
  "search" : "products\/search",
  "delivery_services" : "delivery_services\/v1\/delivery_services",
  "homepage_favorites" : "iphone\/favourites\/?currencyCode=GBP&data=all",
  "products_availabilities" : "products\/availabilities",
  "products_batched" : "products\/batched\/?currencyCode=GBP&",
  "products" : "products\/%@?currencyCode=GBP",
  "search_suggested" : "https:\/\/suggestedsearch.%@\/",
  "version_check" : "version-check",
  "privacy_policy" : "about\/privacy?no_header_and_footer=true",
  "checkout_customer" : "checkout\/v1\/checkout\/customer",
  "checkout_pay" : "checkout\/v1\/checkout\/%@\/pay",
  "basket_validation" : "carts",
  "checkout_totals" : "checkout\/v1\/totals",
  "checkout" : "checkout\/v1\/checkout",
  "payment_methods" : "payment_methods\/v1\/payment_methods",
  "addresses_postcode_lookup" : "addresses\/postcode-lookup?country=GB&postcode=",
  "base" : "notonthehighstreet.com",
  "checkout_purchase" : "checkout\/v1\/purchase",
  "homepage" : "iphone\/homepage"
}
```

##### 400 BAD REQUEST

**body**
No body is returned with this response type.


### GET /v1/health
The health endpoint is provided so container monitroing software can check that the service is all up and OK.

#### url
**/v1/health**

#### parameters
There are no parameters for this request.

#### response
##### 200 OK

**body**
```json
{
  "status_message" : "OK it's fine"
}
```

## Building the service with Docker
1. Install Docker for Mac or Linux
[https://www.docker.com/products/overview](https://www.docker.com/products/overview)
2. Clone this repo
`git clone git@github.com:notonthehighstreet/native-config-service.git`
3. Change into the build folder
`$ cd _minke`
4. Build the application code and create a container image
`$ ./minke -v build_image`
5. Run the service
`$ ./minke -v run`

The build script will start a Docker container will everything that is needed to compile the application code and run the unit tests, once this passes it will then package the new Swift binary into a new Docker image.
The run step uses docker-compose to start the service and all the dependent applications like Consul on your local machine, once the application stack has started you should see some output resembling the following.

```
DEBUG: registrator_1    | 2016/12/07 16:37:18 Starting registrator v7 ...
DEBUG: registrator_1    | 2016/12/07 16:37:18 Using consul adapter: consul://consul:8500
DEBUG: registrator_1    | 2016/12/07 16:37:18 Connecting to backend (0/0)
DEBUG: registrator_1    | 2016/12/07 16:37:18 consul: current leader  172.20.0.3:8300
DEBUG: registrator_1    | 2016/12/07 16:37:18 Listening for Docker events ...
DEBUG: registrator_1    | 2016/12/07 16:37:18 Syncing services on 3 containers
DEBUG: registrator_1    | 2016/12/07 16:37:18 ignored: 97dce7f1a131 no published ports
DEBUG: registrator_1    | 2016/12/07 16:37:18 added: 2c6d5f2898a4 97dce7f1a131:minkefwzgizjtgeqfqjdy_consul_1:8301
DEBUG: registrator_1    | 2016/12/07 16:37:18 added: 2c6d5f2898a4 97dce7f1a131:minkefwzgizjtgeqfqjdy_consul_1:8301:udp
DEBUG: registrator_1    | 2016/12/07 16:37:18 added: 2c6d5f2898a4 97dce7f1a131:minkefwzgizjtgeqfqjdy_consul_1:8302:udp
DEBUG: registrator_1    | 2016/12/07 16:37:18 added: 2c6d5f2898a4 97dce7f1a131:minkefwzgizjtgeqfqjdy_consul_1:8500
DEBUG: registrator_1    | 2016/12/07 16:37:18 added: 2c6d5f2898a4 97dce7f1a131:minkefwzgizjtgeqfqjdy_consul_1:53:udp
DEBUG: registrator_1    | 2016/12/07 16:37:18 added: 2c6d5f2898a4 97dce7f1a131:minkefwzgizjtgeqfqjdy_consul_1:8302
DEBUG: registrator_1    | 2016/12/07 16:37:18 added: 2c6d5f2898a4 97dce7f1a131:minkefwzgizjtgeqfqjdy_consul_1:8400
DEBUG: registrator_1    | 2016/12/07 16:37:18 added: 2c6d5f2898a4 97dce7f1a131:minkefwzgizjtgeqfqjdy_consul_1:53
DEBUG: registrator_1    | 2016/12/07 16:37:18 added: 2c6d5f2898a4 97dce7f1a131:minkefwzgizjtgeqfqjdy_consul_1:8300
DEBUG: registrator_1    | 2016/12/07 16:37:18 ignored: 55d0605cf9d0 no published ports
DEBUG: statsd_1         | *** Running /etc/my_init.d/00_regen_ssh_host_keys.sh...
DEBUG: statsd_1         | *** Running /etc/my_init.d/01_conf_init.sh...
DEBUG: registrator_1    | 2016/12/07 16:37:19 added: bc6d276ac32f 97dce7f1a131:minkefwzgizjtgeqfqjdy_statsd_1:8125:udp
DEBUG: statsd_1         | *** Running /etc/rc.local...
DEBUG: registrator_1    | 2016/12/07 16:37:19 added: bc6d276ac32f 97dce7f1a131:minkefwzgizjtgeqfqjdy_statsd_1:8126
DEBUG: statsd_1         | *** Booting runit daemon...
DEBUG: statsd_1         | *** Runit started as PID 14
DEBUG: registrator_1    | 2016/12/07 16:37:19 added: bc6d276ac32f 97dce7f1a131:minkefwzgizjtgeqfqjdy_statsd_1:2003
DEBUG: statsd_1         | Dec  7 16:37:19 bc6d276ac32f syslog-ng[33]: syslog-ng starting up; version='3.5.3'
DEBUG: registrator_1    | 2016/12/07 16:37:19 added: bc6d276ac32f 97dce7f1a131:minkefwzgizjtgeqfqjdy_statsd_1:2004
DEBUG: registrator_1    | 2016/12/07 16:37:19 added: bc6d276ac32f 97dce7f1a131:minkefwzgizjtgeqfqjdy_statsd_1:2023
DEBUG: registrator_1    | 2016/12/07 16:37:19 added: bc6d276ac32f 97dce7f1a131:minkefwzgizjtgeqfqjdy_statsd_1:2024
DEBUG: registrator_1    | 2016/12/07 16:37:19 added: bc6d276ac32f 97dce7f1a131:minkefwzgizjtgeqfqjdy_statsd_1:80
DEBUG: registrator_1    | 2016/12/07 16:37:19 added: 786d8000a495 97dce7f1a131:minkefwzgizjtgeqfqjdy_configservice_1:8090
```

The service will now be running to test it first find the port that the service is running on using the following command:
`$ docker ps | grep configservice`

The host port will be shown something like `0.0.0.0:32942->8090/tcp` this is the host the container is running on and the port that it has bound to the host.  The other port in this case `8090/tcp` is the port that the service is running on however this is only available from inside the container or from linked containers.

You can now test your service with the following command:
`curl -i localhost:32942/v1/config/giftfinder/a/default`

## Running locally
1. Install swift
[https://swift.org/download/](https://swift.org/download)
2. Run
`make runserver`

You should now be able to test the service using the following command:
```
curl -i localhost:8090/v1/config/giftfinder/a/default

HTTP/1.1 200 OK
Date: Wed, 07 Dec 2016 16:49:10 GMT
Content-Type: application/json
Content-Length: 1080
Connection: Keep-Alive
Keep-Alive: timeout=60, max=99

{
  "products_validation" : "product_validation\/v1\/product_validation",
  "search" : "products\/search",
  "delivery_services" : "delivery_services\/v1\/delivery_services",
  "homepage_favorites" : "iphone\/favourites\/?currencyCode=GBP&data=all",
  "products_availabilities" : "products\/availabilities",
  "products_batched" : "products\/batched\/?currencyCode=GBP&",
  "products" : "products\/%@?currencyCode=GBP",
  "search_suggested" : "https:\/\/suggestedsearch.%@\/",
  "version_check" : "version-check",
  "privacy_policy" : "about\/privacy?no_header_and_footer=true",
  "checkout_customer" : "checkout\/v1\/checkout\/customer",
  "checkout_pay" : "checkout\/v1\/checkout\/%@\/pay",
  "basket_validation" : "carts",
  "checkout_totals" : "checkout\/v1\/totals",
  "checkout" : "checkout\/v1\/checkout",
  "payment_methods" : "payment_methods\/v1\/payment_methods",
  "addresses_postcode_lookup" : "addresses\/postcode-lookup?country=GB&postcode=",
  "base" : "notonthehighstreet.com",
  "checkout_purchase" : "checkout\/v1\/purchase",
  "homepage" : "iphone\/homepage"
}%
```
