# build certbot container

```
docker build -t boundlessgeo/spatialconnect-server:certbot .
```

# run certbot container

```
docker run -e DOMAIN_NAME=spatialconnect.boundlessgeo.com -e EMAIL=mcenac@boundlessgeo.com  boundlessgeo/spatialconnect-server:certbot
```
