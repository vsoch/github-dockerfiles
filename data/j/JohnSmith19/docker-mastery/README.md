# Docker Mastery

## Creating and Using Containers Like a Boss

```bash
➜  docker version
Client:
Version:           18.06.1-ce
API version:       1.38
Go version:        go1.10.3
Git commit:        e68fc7a
Built:             Tue Aug 21 17:21:31 2018
OS/Arch:           darwin/amd64
Experimental:      false

Server:
Engine:
  Version:          18.06.1-ce
  API version:      1.38 (minimum version 1.12)
  Go version:       go1.10.3
  Git commit:       e68fc7a
  Built:            Tue Aug 21 17:29:02 2018
  OS/Arch:          linux/amd64
  Experimental:     true

docker info
docker <command> <sub-command> (options)
```

### Starting NginX Web Server

```bash
➜  ~ docker container run --publish 80:80 nginx

➜  ~ docker container run --publish 80:80 --detach nginx
72f828592f46e58da3755aa89736db5751386e16461a167cbd0078068c5369d5
```
### List running containers

```bash
➜  ~ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                NAMES
72f828592f46        nginx               "nginx -g 'daemon of…"   About a minute ago   Up About a minute   0.0.0.0:80->80/tcp   heuristic_vaughan
```

### Docker container stop

```bash
➜  ~ docker container stop 72f8
```

### Run vs. Start

```bash
➜  ~ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
72f828592f46        nginx               "nginx -g 'daemon of…"   26 minutes ago      Exited (0) 40 seconds ago                       heuristic_vaughan
5c01ea8f4aee        nginx               "nginx -g 'daemon of…"   28 minutes ago      Exited (0) 26 minutes ago                       mystifying_lalande

'docker container run’ always starts a *new* container
Use ‘docker container start’ to start an existing stopped one 

➜  ~ docker container run --publish 80:80 --detach --name webhost nginx
875fab0a285a0786c0cf8dec867d82f7dd439304f2e2612210923190eac15f6e
➜  ~ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS                NAMES
875fab0a285a        nginx               "nginx -g 'daemon of…"   27 seconds ago      Up 26 seconds               0.0.0.0:80->80/tcp   webhost
72f828592f46        nginx               "nginx -g 'daemon of…"   30 minutes ago      Exited (0) 5 minutes ago                         heuristic_vaughan
5c01ea8f4aee        nginx               "nginx -g 'daemon of…"   32 minutes ago      Exited (0) 31 minutes ago                        mystifying_lalande
```

### Docker container logs

```bash
➜  ~ docker container logs webhost
172.17.0.1 - - [11/Sep/2018:11:20:34 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36" "-"
172.17.0.1 - - [11/Sep/2018:11:20:35 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36" “-"

➜  ~ docker container top webhost
PID                 USER                TIME                COMMAND
2571                root                0:00                nginx: master process nginx -g daemon off;
2604                101                 0:00                nginx: worker process
```

### Docker container rm

```bash
➜  ~ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
875fab0a285a        nginx               "nginx -g 'daemon of…"   6 minutes ago       Up 6 minutes        0.0.0.0:80->80/tcp   webhost
➜  ~ docker container rm -f 875f
875f
```

## Container VS. VM: It’s Just a Process

```bash
➜  ~ docker run --name mongo -d mongo
➜  ~ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
72098970a4ff        mongo               "docker-entrypoint.s…"   59 seconds ago      Up 58 seconds       27017/tcp           mongo
➜  ~ docker top mongo
PID                 USER                TIME                COMMAND
2893                999                 0:01                mongod —bind_ip_all
➜  ~ docker stop mongodocker
mongo
➜  ~ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
➜  ~ docker top mongo
Error response from daemon: Container 72098970a4ff305bb3e4e4941239bff5a5467db39681924386ca18560fa728c1 is not running
```

## Assignment: Manage Multiple Containers

```bash
➜  ~ docker container run -d -p 3306:3306 --name db -e MYSQL_RANDOM_ROOT_PASSWORD=yes mysql
f9b09ad4930a634985f78ab88d4482f2e1e14520f00e56b9238cec3af8c5ee76
➜  ~ docker container logs db
GENERATED ROOT PASSWORD: aiF5bahshieVuu6peex8esahraenie5o

➜  ~ docker container run -d --name webserver -p 8080:80 httpd
487f21cb11a9434e0049e062be11d38ff8c3b4377b6dccfb2e68a6a0004d8cc8

➜  ~ docker container run -d --name proxy -p 80:80 nginx
59e4768b80e3117564aa00b2888fb8114ff8e5f42428d19d1d8d899017e9a13b

➜  ~ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                               NAMES
59e4768b80e3        nginx               "nginx -g 'daemon of…"   29 seconds ago       Up 28 seconds       0.0.0.0:80->80/tcp                  proxy
487f21cb11a9        httpd               "httpd-foreground"       About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp                webserver
f9b09ad4930a        mysql               "docker-entrypoint.s…"   4 minutes ago        Up 3 minutes        0.0.0.0:3306->3306/tcp, 33060/tcp   db

➜  ~ docker container stop 59e4768b80e3 487f21cb11a9 f9b09ad4930a
59e4768b80e3
487f21cb11a9
f9b09ad4930a

➜  ~ docker container rm 59e4 487f f9b0
59e4
487f
f9b0
```

## What’s Going On In Containers: CLI Process Mornitering

```bash
➜  ~ docker container run -d --name nginx nginx
211909cd6753028d15c10662086d8136e4467cbce5df5cb49edfa91001038581
➜  ~ docker container run -d --name mysql -e MYSQL_RANDOM_ROOT_PASSWORD=true mysql
3a742a7a0098ff8fc40845046d6e3afa0e49aa8421534cc576f1f2e0aa465f58

➜  ~ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                 NAMES
3a742a7a0098        mysql               "docker-entrypoint.s…"   41 seconds ago      Up 39 seconds       3306/tcp, 33060/tcp   mysql
211909cd6753        nginx               "nginx -g 'daemon of…"   2 minutes ago       Up 2 minutes        80/tcp                nginx
```

### Process list in one container

```bash
➜  ~ docker container top mysql
PID                 USER                TIME                COMMAND
6499                999                 0:01                mysqld

➜  ~ docker container top nginx
PID                 USER                TIME                COMMAND
6296                root                0:00                nginx: master process nginx -g daemon off;
6329                101                 0:00                nginx: worker process
```

### Details of one container config

```bash
➜  ~ docker container inspect mysql
…
```

### Performance stats for all containers

```bash
➜  ~ docker container stats —help
➜  ~ docker container stats
CONTAINER ID        NAME                CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
3a742a7a0098        mysql               0.83%               373.8MiB / 1.952GiB   18.70%              998B / 0B           2.61MB / 1.29GB     36
211909cd6753        nginx               0.00%               1.895MiB / 1.952GiB   0.09%               1.18kB / 0B         0B / 0B             2
```

## Getting a Shell Inside Containers

### Start new container interactively
docker container run -it  

```bash
➜  ~ docker container run -it --name proxy nginx bash
root@2f7bf298908a:/# exit
➜  ~ docker container run -it --name ubuntu ubuntu
root@e4075bbdc264:/# exit

➜  ~ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                 NAMES
3a742a7a0098        mysql               "docker-entrypoint.s…"   22 minutes ago      Up 22 minutes       3306/tcp, 33060/tcp   mysql
211909cd6753        nginx               "nginx -g 'daemon of…"   24 minutes ago      Up 24 minutes       80/tcp

➜  ~ docker container ls -a
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS                      PORTS                 NAMES
e4075bbdc264        ubuntu              "/bin/bash"              About a minute ago   Exited (0) 25 seconds ago                         ubuntu
2f7bf298908a        nginx               "bash"                   4 minutes ago        Exited (0) 3 minutes ago                          proxy
3a742a7a0098        mysql               "docker-entrypoint.s…"   22 minutes ago       Up 22 minutes               3306/tcp, 33060/tcp   mysql
211909cd6753        nginx               "nginx -g 'daemon of…"   24 minutes ago       Up 24 minutes               80/tcp                nginx


➜  ~ docker container start --help

Usage:    docker container start [OPTIONS] CONTAINER [CONTAINER...]

Start one or more stopped containers

Options:
  -a, --attach                  Attach STDOUT/STDERR and forward signals
      --checkpoint string       Restore from this checkpoint
      --checkpoint-dir string   Use a custom checkpoint storage directory
      --detach-keys string      Override the key sequence for detaching a container
  -i, --interactive             Attach container's STDIN
➜  ~ docker container start -ai ubuntu
```

### Run additional command in existing container
docker container exec -it 

### Run additional process in running container

```bash
➜  ~ docker container exec -it mysql bash
root@3a742a7a0098:/# exit
exit
➜  ~ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                 NAMES
3a742a7a0098        mysql               "docker-entrypoint.s…"   28 minutes ago      Up 28 minutes       3306/tcp, 33060/tcp   mysql
211909cd6753        nginx               "nginx -g 'daemon of…"   30 minutes ago      Up 30 minutes       80/tcp                nginx
```
### Different Linux distros in containers

```bash
➜  ~ docker pull alpine
➜  ~ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
alpine              latest              196d12cf6ab1        3 hours ago         4.41MB
➜  ~ docker container run -it alpine sh
/ #
```

## Docker Networks: Concepts
### -p (—publish) HOST:CONTAINER

```bash
➜  ~ docker container run -p 80:80 --name webhost -d nginx
42b45fcf1fb591d30f40083719af06fe9a2c855d681f302474f9d5b5773ff2da
➜  ~ docker container port webhost
80/tcp -> 0.0.0.0:80
```

### —format

```bash
➜  ~ docker container inspect --format '{{ .NetworkSettings.IPAddress }}' webhost
172.17.0.4
```

## Docker Networks: CLI Management

### —network bridge
Default Docker virtual network, which is NAT’ed behind the Host IP.

### —network host
It gains performance by skipping virtual networks but sacrifices security of container model

### Show networks

```bash
➜  ~ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
99872c644479        bridge              bridge              local
6996509036e0        compose_default     bridge              local
bffb71795310        host                host                local
1e15c3367812        none
```

### Inspect a network

```bash
➜  ~ docker network inspect bridge
…
```

### Create a network

```bash
➜  ~ docker network create my_app_net
1cc36f51375a4654fb95d1d7fad25c5adbe60425b56c6ae601ef4783235abb19

➜  ~ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
1cc36f51375a        my_app_net          bridge              local

➜  ~ docker network create —help

➜  ~ docker container run -d --name new_nginx --network my_app_net nginx:alpine
2e399127b744d8de277288d6de1291754c07f07494c424bc7080abbc08a253ea
➜  ~ docker network inspect my_app_net
…
```

### Attach a network to container 

```bash
➜  ~ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                 NAMES
42b45fcf1fb5        nginx               "nginx -g 'daemon of…"   45 minutes ago      Up 45 minutes       0.0.0.0:80->80/tcp    webhost

➜  ~ docker network connect 1cc36f51375a 42b45fcf1fb5
➜  ~ docker container inspect 42b45fcf1fb5
...
```

### Detach a network from container

```bash
➜  ~ docker network disconnect 1cc36f51375a 42b45fcf1fb5
➜  ~ docker container inspect 42b45fcf1fb5
…
```

## Docker Networks: DNS and How Containers Find Each Other

Docker defaults the hostname to the container’s name, but you can also set aliases

```bash
➜  ~ docker container run -d --name my_nginx --network my_app_net nginx:alpine
b67e64477d5ba5bc571fefed84fd5b0cfa2ffb77c927c8f9280fee1da57a48f7

➜  ~ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
f1f0758d37ac        my_app_net          bridge              local

➜  ~ docker network inspect f1f0758d37ac
…

➜  ~ docker container exec -it my_nginx ping new_nginx
PING new_nginx (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.385 ms
64 bytes from 172.18.0.2: seq=1 ttl=64 time=0.159 ms
64 bytes from 172.18.0.2: seq=2 ttl=64 time=0.300 ms

➜  ~ docker container exec -it new_nginx ping my_nginx
PING my_nginx (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.164 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.229 ms
64 bytes from 172.18.0.3: seq=2 ttl=64 time=0.158 ms
```

### Assignment: Using Containers for CLI Testing

```bash
➜  ~ docker container run --rm -it centos:7 bash
[root@ae3b677af65f /]# exit

➜  ~ docker container run --rm -it ubuntu:16.04 bash
root@aa201fb16aed:/# exit

➜  ~ docker ps -a

Centos and ubuntu disappear —rm
```

### Assignment: DNS Round Robin Test

- Know how to user -it get shell in container
- Understand basics to what a Linux distribution is like Ubuntu and CentOS
- Know how to run a container
- Understand basics of DNS records

```bash
➜  ~ docker network create dude
4e61f1e4140f822717a753a90bfa1f127adc2c42059886a27ecd8d3a067a049b

➜  ~ docker container run -d --net dude --net-alias search elasticsearch:2
db52ebe454dcf6d93224924d609257c645b25643003b160fee93fa1bf490a1f9

➜  ~ docker container run -d --net dude --net-alias search elasticsearch:2
bd0ba831c50ae875c5b1216dbe88ea0e028bdf209703247c5d5b25830fff4dc1

➜  ~ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
bd0ba831c50a        elasticsearch:2     "/docker-entrypoint.…"   20 seconds ago      Up 19 seconds       9200/tcp, 9300/tcp         hardcore_aryabhata
db52ebe454dc        elasticsearch:2     "/docker-entrypoint.…"   36 seconds ago      Up 35 seconds       9200/tcp, 9300/tcp         stoic_shockley

➜  ~ docker container run --rm --net dude alpine nslookup search
nslookup: can't resolve '(null)': Name does not resolve

Name:      search
Address 1: 172.19.0.2 search.dude
Address 2: 172.19.0.3 search.dude


➜  ~ docker container run --rm --net dude centos curl -s search:9200
{
  "name" : "James Howlett",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "VdcaBN8dSMG4bJ1yMhislQ",
  "version" : {
    "number" : "2.4.6",
    "build_hash" : "5376dca9f70f3abef96a77f4bb22720ace8240fd",
    "build_timestamp" : "2017-07-18T12:17:44Z",
    "build_snapshot" : false,
    "lucene_version" : "5.5.4"
  },
  "tagline" : "You Know, for Search"
}

➜  ~ docker container run --rm --net dude centos curl -s search:9200
{
  "name" : "Nicholas Scratch",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "Z8HTm7jBT2CzXOhkuX6tHg",
  "version" : {
    "number" : "2.4.6",
    "build_hash" : "5376dca9f70f3abef96a77f4bb22720ace8240fd",
    "build_timestamp" : "2017-07-18T12:17:44Z",
    "build_snapshot" : false,
    "lucene_version" : "5.5.4"
  },
  "tagline" : "You Know, for Search"
}

➜  ~ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
bd0ba831c50a        elasticsearch:2     "/docker-entrypoint.…"   5 minutes ago       Up 5 minutes        9200/tcp, 9300/tcp         hardcore_aryabhata
db52ebe454dc        elasticsearch:2     "/docker-entrypoint.…"   5 minutes ago       Up 5 minutes        9200/tcp, 9300/tcp         stoic_shockley

➜  ~ docker container rm -f hardcore_aryabhata stoic_shockley
hardcore_aryabhata
stoic_shockley
```

## Container Images

### The Mighty Hub
Basics of Docker Hub
Find Official and other good public images
Download images and basics of image tags

```bash
➜  ~ docker image ls

https://hub.docker.com/_/nginx/

➜  ~ docker pull nginx
Using default tag: latest

➜  ~ docker pull nginx:1.11.9
Status: Downloaded newer image for nginx:1.11.9
```

### Images and Their Layers: Discover the Image Cache
https://docs.docker.com/storage/storagedriver/

```bash
➜  ~ docker history nginx:latest
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
06144b287844        11 days ago         /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
<missing>           11 days ago         /bin/sh -c #(nop)  STOPSIGNAL [SIGTERM]         0B
<missing>           11 days ago         /bin/sh -c #(nop)  EXPOSE 80/tcp                0B
<missing>           11 days ago         /bin/sh -c ln -sf /dev/stdout /var/log/nginx…   22B
<missing>           11 days ago         /bin/sh -c set -x  && apt-get update  && apt…   53.8MB
<missing>           11 days ago         /bin/sh -c #(nop)  ENV NJS_VERSION=1.15.3.0.…   0B
<missing>           11 days ago         /bin/sh -c #(nop)  ENV NGINX_VERSION=1.15.3-…   0B
<missing>           11 days ago         /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B
<missing>           11 days ago         /bin/sh -c #(nop)  CMD ["bash"]                 0B
<missing>           11 days ago         /bin/sh -c #(nop) ADD file:e6ca98733431f75e9…   55.3MB

➜  ~ docker image inspect nginx
```

### Image Tagging and Push to Darker Hub

https://hub.docker.com/r/library/mysql/tags/

https://hub.docker.com/r/library/nginx/

```bash
➜  ~ docker pull nginx:mainline
mainline: Pulling from library/nginx
Digest: sha256:24a0c4b4a4c0eb97a1aabb8e29f18e917d05abfe1b7a7c07857230879ce7d3d3
Status: Downloaded newer image for nginx:mainline

➜  ~ docker image ls
REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
nginx                alpine              994032453556        4 days ago          17.4MB
nginx                latest              06144b287844        11 days ago         109MB
nginx                mainline            06144b287844        11 days ago         109MB
```

### “Lates” Tag
It’s just the default tag, but image owners should assign it to the newest stable version

```bash
➜  ~ docker image tag nginx john/nginx
➜  ~ docker image tag —help

Usage:    docker image tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

➜  ~ docker image ls
REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
john/nginx           latest              06144b287844        11 days ago         109MB
nginx                latest              06144b287844        11 days ago         109MB
nginx                mainline            06144b287844        11 days ago         109MB
```

- docker login <server>
Defaults to logging in hub, but you can override by adding server url

= docker logout
Always logout from shared machines or servers when done, to protect your account

- docker image push
Uploads changed layers to a image registry (default is hub)

```bash
➜  ~ docker image tag nginx johnsmith19/nginx
➜  ~ docker image push johnsmith19/nginx
The push refers to repository [docker.io/johnsmith19/nginx]
579c75bb43c0: Pushed
67d3ae5dfa34: Pushed
8b15606a9e3e: Pushed
latest: digest: sha256:c0b69559d28fb325a64c6c8f47d14c26b95aa047312b29c699da10380e90b4d7 size: 948


➜  ~ docker image tag johnsmith19/nginx johnsmith19/nginx:testing
➜  ~ docker image ls
REPOSITORY           TAG                 IMAGE ID            CREATED             SIZE
johnsmith19/nginx    latest              06144b287844        11 days ago         109MB
johnsmith19/nginx    testing             06144b287844        11 days ago         109MB


➜  ~ docker image push johnsmith19/nginx:testing
The push refers to repository [docker.io/johnsmith19/nginx]
579c75bb43c0: Layer already exists
67d3ae5dfa34: Layer already exists
8b15606a9e3e: Layer already exists
testing: digest: sha256:c0b69559d28fb325a64c6c8f47d14c26b95aa047312b29c699da10380e90b4d7 size: 948
```

### Building Images: The Dockerfile Basics

https://docs.docker.com/engine/reference/builder/#usage
e.g. docker build -f some-dockerfile

### Building Images: Running Docker Builds

[Dockerfile](https://github.com/JohnSmith19/docker-mastery/blob/master/dockerfile-sample-1/Dockerfile)

$ docker image build -t customnginx .

### Building Images: Extending Official Images

[Dockerfile](https://github.com/JohnSmith19/docker-mastery/blob/master/dockerfile-sample-2/Dockerfile)

```bash
$ sudo docker image build -t nginx-with-html .
Sending build context to Docker daemon  3.072kB
Step 1/3 : FROM nginx:latest
---> 8401ca2419eb
Step 2/3 : WORKDIR /usr/share/nginx/html
---> Running in 90c711aaaa97
Removing intermediate container 90c711aaaa97
---> aadd5d0702bd
Step 3/3 : COPY index.html index.html
---> 9b78dc259148
Successfully built 9b78dc259148
Successfully tagged nginx-with-html:latest

$ sudo docker container run -p 80:80 --rm nginx-with-html

$ sudo docker image tag --help

Usage:  docker image tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

$ sudo docker image tag nginx-with-html:latest johnsmith/nginx
-with-html:latest

$ sudo docker image ls
REPOSITORY                          TAG                 IMAGE ID            CREATED             SIZE
johnsmith/nginx-with-html           latest              9b78dc259148        3 minutes ago       88.1MB
nginx-with-html                     latest              9b78dc259148        3 minutes ago       88.1MB
nginx                               latest              8401ca2419eb        9 days ago          88.1MB
```

## Assignment: Build Your Own Dockerfile and Run Containers From It

- Dockerfiles are part process workflow and prt art
- Take existing Node.js app and Dockerize it
- Make Dockerfile. Build it. Test it. Push it. (rm it). Run it.
- Expect this to be iterative. Rarely do I get it right the first time.
- Details in dockerfile-assignment-1/Dockerfile
- User the Alpine version of the official 'node' 6.x image
- Expected result is web site at http://localhost
- Tag and push to your Docker Hub account (free)
- Remove your image from local cache, run again from Hub

[Dockerfile](https://github.com/JohnSmith19/docker-mastery/blob/master/dockerfile-assignment-1/Dockerfile)

```bash

$ docker build -t testnode .

$ docker container run --rm -p 80:3000 testnode

$ docker push --help

Usage:  docker push [OPTIONS] NAME[:TAG]
Push an image or a repository to a registry
Options:
      --disable-content-trust   Skip image signing (default true)

$ docker tag testnode johnsmith19/testing-node

$ docker push johnsmith19/testing-node

$ docker image ls
REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
testnode                 latest              55a6051c3984        42 minutes ago      63MB
johnsmith/testing-node   latest              55a6051c3984        42 minutes ago      63MB
node                     6-alpine            ac75c1f95b80        4 weeks ago         55.2MB

$ docker image rm johnsmith19/testing-node

$ docker container run --rm -p 80:3000 johnsmith19/testing-node
```

## Container Lifetime & Persistent Data

- Defining the problem of persistent data
- Key concepts with containers: immutable, ephemeral
- Learning and using Data Volumes
- Learning and using Bind Mounts
- Assignments




- Containers are usually immutable and ephemeral
- "immutable infrastructure": only re-deploy containers, never chagne
- This is the ideal scenario,  but what about databases, or unique data?
- Docker gives us features to ensure these "separation of concerns"
- This is known as "persistent data"
- Two ways: Volumes and Bind Mounts
- Volumes: make special location outside of container UFS
- Bind Mounts: link container path to host path

## Persistent Data: Data Volumes

[Dockerfile](https://github.com/docker-library/mysql/blob/9d1f62552b5dcf25d3102f14eb82b579ce9f4a26/5.7/Dockerfile)

VOLUME /var/lib/mysql

```bash
$ docker pull mysql

Using default tag: latest
latest: Pulling from library/mysql
802b00ed6f79: Pull complete
30f19a05b898: Pull complete
3e43303be5e9: Pull complete
94b281824ae2: Pull complete
51eb397095b1: Pull complete
54567da6fdf0: Pull complete
bc57ddb85cce: Pull complete
d6cd3c7302aa: Pull complete
d8263dad8dbb: Pull complete
780f2f86056d: Pull complete
8e0761cb58cd: Pull complete
7588cfc269e5: Pull complete
Digest: sha256:038f5f6ea8c8f63cfce1bce9c057ab3691cad867e18da8ad4ba6c90874d0537a
Status: Downloaded newer image for mysql:latest


$ docker image inspect mysql

...
            "ArgsEscaped": true,
            "Image": "sha256:17a4269e383069c990084b4f8bb31c34d28f92d5947c14d48a179b328d5cac61",
            "Volumes": {
                "/var/lib/mysql": {}
            },
...


$ docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysql
d8c9754e4f0e6d120a5ac5b5bd16f8a4c78f21c85dcd7498b59c16ea0bf205ee


$ docker container ls
CONTAINER ID           IMAGE             COMMAND                      CREATED                 STATUS                  PORTS                         NAMES
d8c9754e4f0e            mysql               "docker-entrypoint.s…"    27 seconds ago      Up 25 seconds       3306/tcp, 33060/tcp   mysql


$ docker container inspect mysql

...
        "Mounts": [
            {
                "Type": "volume",
                "Name": "942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e",
                "Source": "/var/lib/docker/volumes/942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e/_data",
                "Destination": "/var/lib/mysql",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
...

$ docker volume ls
DRIVER              VOLUME NAME
local               942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e


$ docker volume inspect 942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e
[
    {
        "CreatedAt": "2018-10-14T10:02:33Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e/_data",
        "Name": "942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e",
        "Options": null,
        "Scope": "local"
    }
]

$ docker container run -d --name mysql2 -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysql
652ff87a8c1b06994f10e974790c99ad815efa614df25c6f2daa96cf3c7cc595

$ docker volume ls
DRIVER              VOLUME NAME
local               942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e
local               c77a8ddaea6b3d9ffc326ee24e2e1ccc7160a2b7596f80d98d0440fe99645c34


$ docker container stop mysql
mysql

$ docker container stop mysql2
mysql2

$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

$ docker container ls -a
CONTAINER ID          IMAGE               COMMAND                        CREATED                       STATUS                         
PORTS               NAMES
652ff87a8c1b            mysql               "docker-entrypoint.s…"       About a minute ago      Exited (0) 10 seconds ago                               mysql2
d8c9754e4f0e           mysql               "docker-entrypoint.s…"       7 minutes ago                Exited (0) 18 seconds ago                               mysql

$ docker volume ls
DRIVER              VOLUME NAME
local               942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e
local               c77a8ddaea6b3d9ffc326ee24e2e1ccc7160a2b7596f80d98d0440fe99645c34

$ docker container rm mysql mysql2
mysql
mysql2

$ docker volume ls
DRIVER              VOLUME NAME
local               942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e
local               c77a8ddaea6b3d9ffc326ee24e2e1ccc7160a2b7596f80d98d0440fe99645c34
```


### Named Volumes
friendly way to assing vols to containers

```bash
$ docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql
0c039c5d5a1864acb3e8fa049e85d6dcfc26c117b645a83efed2053200653036


$ docker volume ls
DRIVER              VOLUME NAME
local               942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e
local               c77a8ddaea6b3d9ffc326ee24e2e1ccc7160a2b7596f80d98d0440fe99645c34
local               mysql-db


$ docker volume inspect mysql-db
[
    {
        "CreatedAt": "2018-10-14T10:16:28Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/mysql-db/_data",
        "Name": "mysql-db",
        "Options": null,
        "Scope": "local"
    }
]

$ docker container rm -f mysql

$ docker container run -d --name mysql3 -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql
039b92ed4d1b506bdd76999d100e4b1dcc821573ca3b123d68c6388370cd2993


$ docker volume ls
DRIVER              VOLUME NAME
local               942836dfed7c5cf6f831dc557c652071fbdcab8932584d326ed3c8a8cb87866e
local               c77a8ddaea6b3d9ffc326ee24e2e1ccc7160a2b7596f80d98d0440fe99645c34
local               mysql-db

$ docker container inspect mysql3
...
        "Mounts": [
            {
                "Type": "volume",
                "Name": "mysql-db",
                "Source": "/var/lib/docker/volumes/mysql-db/_data",
                "Destination": "/var/lib/mysql",
                "Driver": "local",
                "Mode": "z",
                "RW": true,
                "Propagation": ""
            }
        ],
...

```

### Docker volume create
requred to do this before "docker run" to use custom drivers and labels

```bash
$ docker volume create --help

Usage:  docker volume create [OPTIONS] [VOLUME]

Create a volume

Options:
  -d, --driver string   Specify volume driver name (default "local")
      --label list      Set metadata for a volume
  -o, --opt map         Set driver specific options (default map[])
```

## Persistent Data: Bind Mounting

- Maps a host file or directory to a container file or directory
- Basically just two locations pointing to the same file(s)
- Again, skips UFS, and host files overwrite any in container
- Can't use in Dockerfile, must be at container run
- ... run -v /Users/john/stuff:/path/container (mac/linux)
- ... run -v //c/Users/john/stuff:/path/container (windows)

```bash
dockerfile-sample-2$ cat Dockerfile
# this same shows how we can extend/change an existing official image from Docker Hub

FROM nginx:latest
# highly recommend you always pin versions for anything beyond dev/learn

WORKDIR /usr/share/nginx/html
# change working directory to root of nginx webhost
# using WORKDIR is preferred to using 'RUN cd /some/path'

COPY index.html index.html

# I don't have to specify EXPOSE or CMD because they're in my FROM
```

```bash
$ docker container run -d --name nginx -p 80:80 -v $(pwd):/user/share/nginx/html nginx

$ docker container run -d --name nginx2 -p 8080:80 nginx

$ docker container exec -it nginx bash
root@6b5999efcd45:/# cd /usr/share/nginx/html/
root@6b5999efcd45:/usr/share/nginx/html# ls -al
total 12
drwxr-xr-x 4 root root  128 Oct 17 14:32 .
drwxr-xr-x 3 root root 4096 Sep  5 00:56 ..
-rw-r--r-- 1 root root  415 Oct 17 14:32 Dockerfile
-rw-r--r-- 1 root root  249 Oct 17 14:32 index.html

$ touch testme.txt

root@6b5999efcd45:/usr/share/nginx/html# ls -al
total 12
drwxr-xr-x 5 root root  160 Oct 18 11:11 .
drwxr-xr-x 3 root root 4096 Sep  5 00:56 ..
-rw-r--r-- 1 root root  415 Oct 17 14:32 Dockerfile
-rw-r--r-- 1 root root  249 Oct 17 14:32 index.html
-rw-r--r-- 1 root root    0 Oct 18 11:11 testme.txt

$ echo "is it me you're looking for" > testme.txt

http://localhost/testme.txt
is it me you're looking for
```

## Assignment: Database Upgrades with Named Volumes

- Database upgrade with containers
- Create a postgres container with named volume sql-data using version 9.6.1
- Use Docker Hub to learn VOLUME path and versions needed to run it
- Check logs, stop container
- Create a new postgres container with same named volume using 9.6.2
- Check logs to validate

```bash
$ docker container run -d --name psql -v psql:/var/lib/postgresql/data postgres:9.6.1
$ docker container stop 1ad12722b4f8

$ docker container ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
f266a5d08989        postgres:9.6.1      "/docker-entrypoint.…"   6 seconds ago       Up 5 seconds                5432/tcp            psql2
1ad12722b4f8        postgres:9.6.1      "/docker-entrypoint.…"   3 minutes ago       Exited (0) 39 seconds ago                       psql

$ docker volume ls
DRIVER              VOLUME NAME
local                   psql

$ docker container logs f266a5d08989
LOG:  database system was shut down at 2018-10-18 11:57:08 UTC
LOG:  MultiXact member wraparound protections are now enabled
LOG:  database system is ready to accept connections
LOG:  autovacuum launcher started
```

## Assignment: Bind Mounts

- Use a Jekyll ‘Static Site Generator” to start a local web server
- Don’t have to be web developer: this is example of bridging the gap between local file access and apps running in containers
- source code is in the source repo under bindmount-sample-1
- We edit files with editor on our host using native tools
- Container detects changes with host files and updates web server
- start container with docker run -p 80:4000 -v $(pwd):/site bretfisher/jekyll-serve

```bash
$ bindmount-sample-1 git:(master) ✗ docker run -p 80:4000 -v $(pwd):/site bretfisher/jekyll-serve
```
