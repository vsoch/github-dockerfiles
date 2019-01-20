This container runs nginx with a custom mimetypes file, and empty conf.d
directory, which is exposed as a volume.

```bash
$ docker run --name=nginx -p 80:80 -p 443:443 howgood/nginx
$ docker run --volumes-from=nginx my-webapp ...
$ docker kill -s HUP nginx
```
