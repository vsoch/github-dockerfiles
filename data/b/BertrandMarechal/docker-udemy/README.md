# docker-udemy

[Udemy](https://www.udemy.com/docker-mastery/learn/v4/content)

[Git Repo](https://github.com/bretfisher/udemy-docker-mastery)

## docker commands for lecture 2-18 - first steps

```bat
# 1 run a webserver container
docker container run --publish 80:80 nginx

# 2 list the running containers
docker container ls

# 3 list all the containers
docker container ls -a

# 4 stop a container
docker container stop [CONTAINER ID from 2]

# 5 run a webserver container with a name
docker container run --publish 80:80 --name webhost nginx

# 6 get the docker logs
docker container logs [webhost]

# 7 display the running processes ot a container
docker container top [webhost]

# 8 remove multiple containers
# the command can accept multiple ids
docker container rm [ID 1] [ID 2]

# 9 remove containers forcing stop
# the command can accept multiple ids
docker container rm -f [ID 1]

# BONUS 10 remove all processes
docker rm $(docker ps -a -q)
```

## docker commands for lecture 2-19 - just a process

```bat

# 1 start a mongo db container
docker container run --name mongo -d mongo

# 2 get the running processes
docker container top mongo
```

## Homewrok : lecture 2-21

Tasks :

- [x] Create 3 dockers : nginx, mysql and httpd (apache server)
- [x] Detach them
- [x] Give them a name
- [x] Give them ports (80 for nginx, 8080 for httpd, 3306 for mysql)
- [x] For MySQL, use the option MYSQL_RQNDOM_ROOT_PQSSWORD=yes with the --env option
- [x] Stop them all
- [x] Remove them all

### my code for that

```bat
# 1. create nginx container
docker container run --publish 80:80 --detach --name nginx nginx

# 2. create  mysql container
docker container run --publish 3306:3306 --detach --name mysql --env MYSQL_RANDOM_ROOT_PASSWORD=yes mysql

# 3. create  httpd container
docker container run --publish 8080:80 --detach --name httpd httpd

# 4. list the containers
docker container ls

# 5. stop the containers
docker container stop [CONTAINER IDS]

# 6. remove the containers
docker container rm [CONTAINER IDS]
```

## monitor dockers : lecture 2-23

```bat
# 1. For stats on all containers
docker container stats

# 2. For info on container
docker container info [name]
```

## interract with containers : lecture 2-24

```bat
# 1. Run a container in interractive mode, with a bash CLI
docker container run -it --name proxy nginx bash

# 2. Run a container in interractive mode, with a bash CLI - ubuntu mode
docker container run -it --name ubuntu ubuntu

# 3. Run a container already defined with interracted mode
docker container start -ai ubuntu

# 4. Interract with a running container with interracted mode
docker container exec -it mysql bash

# 5. list docker images
docker image ls

# 6. create an alpine container (sh is the smallest equivalent to bash)
docker container run -it alpine sh
```

## Docker networks : lecture 2-25

```bat
# 1. Run a container on port 80:80
docker container run -p 80:80 -d --name webhost nginx

# 2. Get the docker container port definition
docker container port webhost

# 3. Format the reruned data -- IP address of the container
docker container inspect --format '{{ .NetworkSettings.IPAddress}}' webhost
```

## Docker networks - CLI : lecture 2-27

```bat
# 1. List docker networks
docker network ls

# 2. inspect docker network
docker network inspect [network name]

# 3. create a new docker network
docker network create [network name]

# 4. create a container on the created network
docker container run -d --name new_nginx --network my_app_network nginx

# 5. connect a container to an existing network
docker network connect [my_app_net] [nginx]

# 6. the inspect command on the container will show us the networks
docker container inspect [nginx]

# 7. connect a container to an existing network
docker network disconnect [my_app_net] [nginx]
```

## Docker networks - DNS : lecture 2-28

```bat
# 1. Create a new container with the nginx:alpine implementation
docker container run --name my_nginx -d --network my_app_net nginx:alpine

# 2. Ping between containers that are on the same network
docker container exec -it my_nginx ping new_nginx
```

## Docker networks - DNS : lecture 2-29

Homework : run the curl command inside 2 linux distributions

- [x] create a container on centos:7 -it bash
- [x] create a container on ubuntu:14.04 -it bash
- [x] learn about "docker container --rm" command
- [x] check if curl is installed
- [x] install it if needed ("apt-get update" and "apt-get install curl", or "yum update curl")

### 2-29 my code for that

```bat
# check docker container --rm
docker container run --help
# the rm option removes the existing container if one exists

# create the containers
docker container run -it --name centos centos:7
docker container run -it --name ubuntu ubuntu:14.04

# check if curl is installed on any of those
curl --version

# install curl if needed on any of those
apt-get update" and "apt-get install curl
yum update curl
```

## Docker networks - DNS : lecture 2-31

Homework : create a round Robin

- [x] create a virtual network
- [x] create 2 containers on elasticsearch:2
- [x] learn about "--network-alias search" options for docker run
- [ ] run alpine nslookup search with --net to see the 2 containers for the same DNS name
- [ ] run centos curl -s search:9200 with --net until you see both "name" fields show

### 2-31 my code for that

```bat
# check docker container --network-alias search
docker container run --help
# Add network-scoped alias for the container

# create the network
docker network create es_network

# create the containers
docker container run -d --network-alias search --name elasticsearch1 --net es_network elasticsearch:2
docker container run -d --network-alias search --name elasticsearch2 --net es_network elasticsearch:2

# connect to the ubuntu docker
docker container run -it ubuntu bash

# run a ns lookup
docker container run --rm --net es_network alpine nslookup search

# run the search
docker container run --rm --net es_network centos curl -s search:9200
```

## Images : lecture 2-36

```bat
# 1. list images
docker image ls

# 2. inspect image
docker image inspect [user/image:tag]
```

## Images - tagand push to docker hub: lecture 2-36

```bat
# 1. create new tag
docker image tag nginx bertrandmarechal/nginx

# 2. login from commandline
docker login

# 3. push tag
docker image push bertrandmarechal/nginx

# end. logout
docker logout
```

## Images - building image: lecture 2-38

from \udemy-docker-mastery-master\dockerfile-sample-1 :

```bat
# 1. create new image
docker image build -t customnginx .
```

Important to keep the pieces with most changes at the end of the dockerfile

## Images - custom image: lecture 2-39

from \udemy-docker-mastery-master\dockerfile-sample-2 :

```bat
# 1. create new image
docker image build -t nginx-with-html .

# 2. create a container with this image
docker container run -p 80:80 --rm nginx-with-html
```

## Persistent Data - Volumes: lecture 2-43

Data outlive the containers : the volumes (data storages) are not deleted when we remove a container.

We can create volumes beforehand if we want to use its options (name, label, alias...).

```bat
# 1. list the volumes
docker volume ls

# 2. Create a container set up on a volume
# the volume name should follow the following pattern : [alias]:[volume location from "docker container inspect [container name]"]
docker container run --publish 3306:3306 --detach --name mysql_with_volume -v mysql_data:/var/lib/mysql --env MYSQL_RANDOM_ROOT_PASSWORD=yes mysql
```

## Persistent Data - Bind mount: lecture 2-44

Bind mounts binds a local directory to the container directory
Can't be used in docker file, only in docker run

```bat
# 1. create a container bound to our local file system ## SMALL c and / separated path
docker container run --detach --name mysql_with_volume -v //c/Data/my-data:/var/lib/mysql --env MYSQL_RANDOM_ROOT_PASSWORD=yes mysql
```

## Docker compose : lecture 2-49

Compose all the docker elements in a single yml file
Has to specify a version (to fit with features)
Great for dev, not to use in prod

```bat
# create + start the instances defined in the file
docker-compose up
# to stop with Ctrl+C

# cleans the instances not volumes
docker-compose down

# cleans the instances and volumes
docker-compose down -v
```

## Docker compose - Build : lecture 2-53

```bat
# build images beforehand
docker-compose build

# build an image before run
docker-compose up --build
```

## Swarm Mode - Build orchestration : lecture 2-56

```bat
```