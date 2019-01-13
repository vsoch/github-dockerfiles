# laravel-nginx

[![](https://images.microbadger.com/badges/image/superbuddy/laravel-nginx.svg)](https://microbadger.com/images/superbuddy/laravel-nginx "Get your own image badge on microbadger.com")

Just Laravel, Nginx, PHP fpm, Composer and Mcrypt.
We put this online, since we could not find a decent base image for our use.

## Our usage
The previous version of the Superbuddy backoffice uses some libraries on top of composer (PHP).
This Docker image contains the base on which the backoffice is build.
The next Docker image uses `FROM superbuddy/laravel-nginx` and specifies the ENVironment variables,
PORTS and ENTRYPOINT.

## Example Dockerfile
The following is an example of how this file can be used.

```
# $tree
laravel-dockerfiles
  |
  - Project01
  |  |
  |  - docker-compose.yml
  |  - .env
  |  - laravel.env
  - Project99
  |  |
  |  - docker-compose.yml
  |  - .env
  |  - laravel.env
  |  - my.cnf
  - common.env
  - laravel.Dockerfile
  - common.yml
  - db.yml
  
```



```dockerfile
# laravel.Dockerfile
FROM superbuddy/laravel-nginx
COPY . /var/www
WORKDIR /var/www
RUN run_after_copying_repo
CMD service php5-fpm start && nginx
```


```yaml
# docker-compose.yml
version: '2'
services:
  web:
    extends:
      file: $PWD/../common.yml
      service: laravelcommon
    container_name: project99
    links:
      - cache:redis
      - db
      - search
  db:
    extends:
      file: $PWD/../db.yml
      service: db
  cache:
    image: redis
    expose:
      - "6379"
  search:
    image: elasticsearch
    expose:
      - "1622"
```


```bash
# .env
path_to_project_repo=~/laravel-example-project
exposed_to_host_port=8080
db_location=/var/lib/mysql
db_pwd=password
```


```yaml
# common.yml
version: '2'
services:
  laravelcommon:
    build:
      context: "${path_to_project_repo}/"
      dockerfile: "$PWD/../laravel.Dockerfile"
    env_file:
      - $PWD/laravel.env
      - common.env
    ports:
      - "${exposed_to_host_port}:80"
    volumes:
      - /var/log/docker/frontend/laravel:/var/www/storage/logs
      - /var/log/docker/frontend/nginx:/var/log/nginx
```


```yaml
# db.yml
version: '2'
services:
  db:
    image: mariadb
    environment:
      - MYSQL_ROOT_PASSWORD=${db_pwd}
    expose:
      - "3306"
    volumes:
      - "$PWD/my.cnf:/etc/mysql/my.cnf"
      - "${db_location}:/var/lib/mysql"
```
