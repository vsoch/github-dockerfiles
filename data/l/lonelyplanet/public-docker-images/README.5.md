# Docker Image for Postgres 9.4 (with postgis)

Note: this image is public so no sensitive information be included.

## Building the image

```
docker build -t lonelyplanet/postgres:9.4 .
```

## Running a container from the image

```
docker run -p 55432:5432 lonelyplanet/postgres:9.4
```

Starts a container that binds 5432 on in the container to 55432 on the host system.

## Connecting to running postgres container

* username: `postgres`
* password: <none>

```
psql -p 55432 -U postgres
```

If you are using the docker toolbox to run docker (ex. boot2docker):

```
psql -h $(docker-machine ip default) -p 55432 -U postgres
```

## Publishing an image

We have a lonelyplanet organization on Docker Hub. To push the image, run the following:

```
# tag the image with the date in YYYYMMDD format
docker tag lonelyplanet/postgres:9.4 lonelyplanet/postgres:9.4-YYYYMMDD

# push to Docker Hub
docker push lonelyplanet/postgres:9.4
```
