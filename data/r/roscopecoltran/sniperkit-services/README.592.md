# alpine-ngx_mruby/Dockerfile
This dockerfile is the ngx_mruby in a container.

## Usage example
build:

```
docker build -t ngx_mruby .
```

run:

```
echo 'hello, world' > index.html
docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html ngx_mruby
curl http://$(docker-machine ip default):8080
```
