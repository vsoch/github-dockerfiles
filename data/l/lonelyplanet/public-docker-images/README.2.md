# Description
Docker image for the Gor traffic capture and replay utility [gor](https://github.com/buger/gor)

# Build
```
export GOR_VERSION=0.14.1
docker build --build-arg GOR_VERSION=$GOR_VERSION -t tag/gor:latest .
```
