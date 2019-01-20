# Fcrepo 3


## Build

You can build the image without messaging for use in a standalone (no Karaf messaging) way:
```
docker build -f Dockerfile.no-messaging -t suldlss/fcrepo:no-messaging-latest .
```

## Run

```
docker run -p 8080:8080 suldlss/fcrepo:no-messaging-latest
```
