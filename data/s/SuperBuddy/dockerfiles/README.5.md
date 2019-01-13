# docker ng-cli-nginx

[![](https://images.microbadger.com/badges/image/superbuddy/ng-cli-nginx.svg)](https://microbadger.com/images/superbuddy/ng-cli-nginx "Get your own image badge on microbadger.com")

This docker contains the angular-cli and nginx.

## Environment

`APP_DEBUG=boolean` - Simply a boolean to check if you want to use `nginx` or `ng serve` 
`DEBUG_HOST=ip` - Set the ip for `ng-serve` to host on, defaults to `0.0.0.0`

## Running

To run a docker use the following:

    docker run -it --name name-of-project \
    -v /location/for/project:/project \
    -p 4200:4200 \
    -p 49152:49152 \
    -p 80:80 \
    -e APP_DEBUG=true \
    superbuddy/ng-cli-nginx

If the project folder is empty, `ng init` will be triggered, so don't worry, a project will be made!

## Docker-compose

    version: '2'

    services:
      name-of-project:
        image: superbuddy/ng-cli-nginx
        environment:
          - APP_DEBUG=true
        ports:
          - 4200:4200
          - 49152:49152
          - 80:80
        volumes:
          - /location/for/project:/project


## Environment

`APP_DEBUG=bolean` - Simply a boolean to check if you want to use `nginx` or `ng serve` 
