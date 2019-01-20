# Rails image for production

Built for production, uses Alpine

```
docker build -f Dockerfile -t avvo/ruby-rails:latest .
docker push avvo/ruby-rails:latest
```

Versions:
 * v1.1: Set bundler to 1.15
