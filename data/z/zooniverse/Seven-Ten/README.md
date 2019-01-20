# Seven-Ten

Split testing service

[![Build Status](https://travis-ci.org/zooniverse/Seven-Ten.svg?branch=master)](https://travis-ci.org/zooniverse/Seven-Ten)

## Getting started

``` bash
# clone the repository
git clone https://github.com/zooniverse/Seven-Ten.git
cd Seven-Ten

# copy some config files
for f in config/*.yml.docker; do cp "$f" "${f%.docker}"; done
```

On Linux

``` bash
docker-compose up
```

On OS X

``` bash
# setup docker
brew install docker-machine
docker-machine create --driver virtualbox seven-ten
eval $(docker-machine env seven-ten)

# Create and start the containers
docker-compose up

# Show the host
docker-machine ls
# URL
# tcp://192.168.99.100:2376
# Rails is running on http://192.168.99.100:3000
```

## [Documentation](https://github.com/zooniverse/Seven-Ten/blob/master/docs/)

Documentation can be found in [/docs](https://github.com/zooniverse/Seven-Ten/blob/master/docs/).

### Client

The JavaScript client is located at [zooniverse/Seven-Ten-Client](https://github.com/zooniverse/Seven-Ten-Client).
