# Docker Image for running siege

Note: this image is public so no sensitive information be included.

## Running a container from the image

```
docker run lonelyplanet/siege siege -r 10 http://www.lonelyplanet.com/status
```

## Building an image

```
docker build -t lonelyplanet/siege .
```

## Publishing an image

We have a lonelyplanet organization on Docker Hub. To push the image, run the following:

```
docker push lonelyplanet/siege
```
