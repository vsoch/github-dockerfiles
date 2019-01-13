
# flask-alpine-docker

This example creates a non-root user in a docker image based on alpine and runs a flask server with non-root user privileges.

---

## Build using:
```
docker build --no-cache  -t python-build:latest .
```
---

## Run using:
```
docker run -it --name flaskpython -p 8008:8008 python-build:latest
```

---
