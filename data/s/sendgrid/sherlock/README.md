SHERLOCK
========

Example of envlock API using sinatra and swagger.


# Building

```
$ docker-compose build
```

# Running

```
$ docker-compose up -d
```

Access http://sherlock_swag.docker using the dns container, or the ip directy using


```
$ docker inspect -f '{{.NetworkSettings.IPAddress}}' sherlock_swag_1
172.17.0.101
```
