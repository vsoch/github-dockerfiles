# build certbot container

```
docker build -t boundlessgeo/signal-server:certbot .
```

# run certbot container

```
docker run -e DOMAIN_NAME=signal.boundlessgeo.com -e EMAIL=mcenac@boundlessgeo.com  boundlessgeo/signal-server:certbot
```
