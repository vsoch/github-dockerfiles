# docker-lemp

## Images
based on official:
- nginx:mainline-alpine
- php:fpm-alpine
- mariadb:10.1

nginx offical repository is often slow with update  
to have the last version, build your own image with a dockerfile  
simply copy the original dockerfile and change the version :D  

in the dokcer-compose.yml, under nginx sections, add:
```
build: .
dockerfile: nginx-1.11.3-alpine.dockerfile
```

## Config
```
cp mariadb.config.env.sample mariadb.config.env
```
```
cp php.config.env.sample php.config.env
```
then, change default value ...
