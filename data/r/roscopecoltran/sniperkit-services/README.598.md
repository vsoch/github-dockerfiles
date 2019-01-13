# alpine-nginx/Dockerfile
This dockerfile is the Nginx in a container.

## Usage example
```
docker build -t alpine-nginx .
echo 'hello, world' > index.html
docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html alpine-nginx
curl http://$(docker-machine ip default):8080/
```
