# Ruby Ubuntu images

Built for CI

```
docker build -f Dockerfile.ubuntu-base -t avvo/ubuntu-base:latest .
docker push avvo/ubuntu-base:latest
docker build -f Dockerfile.2.2.6 -t avvo/ruby-ubuntu:2.2.6 .
docker push avvo/ruby-ubuntu:2.2.6
docker build -f Dockerfile.2.2.7 -t avvo/ruby-ubuntu:2.2.7 -t avvo/ruby-ubuntu:2.2 .
docker push avvo/ruby-ubuntu:2.2.7
docker push avvo/ruby-ubuntu:2.2
docker build -f Dockerfile.2.3.4 -t avvo/ruby-ubuntu:2.3.4 -t avvo/ruby-ubuntu:2.3 .
docker push avvo/ruby-ubuntu:2.3.4
docker push avvo/ruby-ubuntu:2.3
docker build -f Dockerfile.2.4.1 -t avvo/ruby-ubuntu:2.4.1 -t avvo/ruby-ubuntu:2.4 -t avvo/ruby-ubuntu:2 -t avvo/ruby-ubuntu:latest .
docker push avvo/ruby-ubuntu:2.4.1
docker push avvo/ruby-ubuntu:2.4
docker push avvo/ruby-ubuntu:2
docker push avvo/ruby-ubuntu:latest
```

Tags:

* `avvo/ubuntu-base:1.1` adds unzip package
