## Transmission Docker image

> This Docker image is based on Alpine image (size: 5mb).

> ROOT account password: passw0rd12

You can run:
```
docker run \
  -d \
  -p 9091:9091 \
  giabar/gb-transmission
```

With volumes:
```
docker run \
  -d \
  -p 9091:9091 \
  -v /your-incomplete-folder:/downloads_incomplete \
  -v /your-complete-folder:/downloads_complete \
  giabar/gb-transmission
```

Now you can open your browser at `http://your-ip:9091`.
