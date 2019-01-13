# Docker Mastery: The Complete Toolset From a Docker Captain

> Build, compose, deploy, and manage Docker containers from development to DevOps based Swarm clusters

This repo was used in my Udemy Course https://www.bretfisher.com/dockermastery, so it is just for testing and learning Docker.

# Gloassary:

### Image

- Is the application I want to run. I.e. image of `nginx` web server.
- Is the application `binaries` and` dependencies` for your app and `metadata` on "how to" run it.
- We can store our images as `registry` on Docker Hub (hub.docker.com)
- Official: It is an **ordered collection of root fliesystem changes** and the 
  corresponding **execution parameters** to run within a `container` runtime.
- There is **NO kernel**, **NO kernel modules**, the host (your OS or a Docker-Machine)
  provider the kernel.

### Container

- Is an instance of the image running as a `process`.
- We can have many containers of `same` image running.
- We can publish (allow) ports to be accessed in a container.

### Swarm

- It is a native Docker tool for containers and services Orchestration.

# How to?

### Running container

```
docker container run --publish 80:80 nginx
```

- It will download Nginx image and run it in a container. 
- Now access `http://localhost`.

What happened?

- Docker tried to locate locally an image `nginx` in the image cache.
- Docked did not find, so it will download from `hub.docker.com`.
- The latest image will be download, which means `nginx:latest` and it will be 
stored in the image cache.
- Docker Engine will give to the container an IP in a private network.
- Docker Engine exposed container port `80`.
- Docker Engine redirected the traffic for your localhost port `80` to 
container port `80`.
- Docker Engine started a new process for a container of `nginx` image.
- This container will execute `CMD` command inside the Docker file of 
`nginx` image.


If we want to run it in a `detached` process, we can run:

```
docker container run --publish 80:80 --detach nginx
```

It will give you an unique container ID, i.e. `6db7f4379093a7ea67acc83ca28fd9840e30c92546df4e83998462f57a72656b`.

### Listing containers

You can see the running container by typing:

```
docker container ls
```

or to see all containers history.

```
docker container ls -a
```

### Stopping containers

And to stop the container (where `6db7f4379093` is my container ID):

```
docker container stop 6db7f4379093
```

### Running with name

Specifying a container name is good practice.


```
docker container run --publish 80:80 --detach --name webhost nginx
```

### Restart a previous stoped container: 

By providing the container's `name` or `ID` you can start previously stoped container. 

I.e for `webhost` container's name.

```
docker container start webhost
```

### See container logs.

Where my container is `webhost`.

```
docker container logs webhost
```

### Monitoring a container 

Where `webhost` is my container.

See container process inside container

```
docker container top webhost
```

To obtain ipaddress, gateway, port etc.

```
docker container inspect webhost
```

See memory usage, processor usage, network, process, etc.

```
docker container stats webhost
```

### Removing container

Here I can also remove more than one container by providing theirs IDs as follows.

```
docker container rm 69aeec00bc47 6db7f4379093 16c2c0cf9a66
```

### Starting multiple containers and passing environment variables

Note the `--env` was used to set mysql root password.

```
docker container run --publish 80:80 --detach --name nginx_server nginx
docker container run --publish 8080:80 --detach --name apache_server httpd
docker container run --publish 3307:3306 --detach --env MYSQL_ROOT_PASSWORD=root --name mysql_db mysql
```


### Run interactive commands inside container

For this we use `-i` (interactive: Keep STDIN open even if not attached) and `-t` (tty: Allocate a pseudo-TTY / text terminal).

To go inside the container:

```
docker container exec -it nginx_server bash
```

To execute commands from outside the container:

```
docker container exec -it nginx_server whoami
```

#### For Alpine

For `alpine` there is no `bash` installed by default, so it is needed to use `sh`


```
docker pull alpine
docker container run --detach --name alpine alpine tail -f /dev/null
docker container exec -it alpine sh
```

Obs: Note that we use `tail -f /dev/null` to keep alpine container `alive` after exit.

... and inside Apline, install the bash

```
apk update
apk add bash
```
... now you can run bash:

```
docker container exec -it alpine bash
```

### Run a container overriding initial COMMAND

It will override default image initialization command to `bash` and will bring you to inside the container.

```
docker container run -it --name nginx_server nginx bash
```

### Download image to local image cache

It will download linux `alpine` image to local cache.

```
docker pull alpine
```

### Clean up file system after exit

If you are running short-term foreground processes, these container file 
systems can really pile up. If instead you’d like Docker to automatically clean 
up the container and remove the file system when the container exits, you can 
add the `--rm` flag:

```
docker container run --rm -it --name my_centos centos:7 bash
```

So when you exit the container it will remove all generated container 
filesystem. Type ``` docker container ls -a ``` and you will notice that 
container is not there anymore. 

It also works if you run container with `--detach` and stop the container.

## Docker Networking

- The docker container is created inside a virtual network called `bridge` or `docker0`.
- When we "expose a port" we are telling to our system (in my case, my MAC) 
 open up in the "network interface" (which is a kind of firewall) the port `8080` 
 and NAT (translate the network) traffic through this private network to port `80` of `bridge`.
- We can have more then one "docker virtual network" and restrict access among certain containers.

...Start a container specifing that internal port `80` will be exposed as `8080`.

```
docker container run --publish 8080:80 --detach --name nginx_server nginx
```

...To check the port

```
docker container port nginx_server
```

...To check the ip address using `format` option (very helpful option).

```
docker container inspect --format '{{ .NetworkSettings.IPAddress }}' nginx_server
```

...Useful network commands

- Show networks: ``` docker network ls ```
- Inspect a network (i.e. bridge): ``` docker network inspect bridge ```
- Inspect networks for specific container ``` docker container inspect --format '{{ .NetworkSettings.Networks }}' nginx_server ```
- Create a network: ``` docker network create my_app_net --driver bridge ``` (you can specify different drivers in order to get more networking features).
- Attach a network to a container ``` docker network connect my_app_net nginx_server ```
- Detach a network from a container ``` docker network disconnect my_app_net nginx_server ```

### DNS for containers


Docker container IPs will be generated dynamically inside networks, 
so we need to set DNS to avoid possible inconsistency.

Docker Daemon has an internal DNS server that containers use by default.

Let's suppose I have two containers `apache_server` and `nginx_server` 
and I have a network called `my_app_net`. If I add both containers to this network, 
they will be able to "ping" each other automatically by their "names" instead rellying on IPs.

Example:

First enter in your containers `apache_server` and `nginx_server` and install ping package:

```
apt-get update
apt-get install iputils-ping
```

Exit the containers and create a network:

``` 
docker network create my_app_net --driver bridge 
```

Now connect them to the same network:

```
docker network connect my_app_net apache_server
docker network connect my_app_net nginx_server
```

And it will allow you to reach each other by the container name as you can test:

```
docker container exec -it nginx_server ping apache_server
docker container exec -it apache_server ping nginx_server
```


#### DNS Round Robin

We can have 2 or more containers responding to the same DNS. It is a technique used 
by many companies to balance their farm of servers.

- Since Docker Engine 1.11 it is possible to have containers under a network 
responding to the same DNS.

For this example lets create 2 containers for `elasticsearch:2` image using 
the following container options:

- `--network`: Specify the user network created.
- `--network-alias`: Add network-scoped alias for the container. It will 
basically give to the container an additional DNS name to respond to.

```
docker network create dude
docker container run --detach --network dude --net-alias search --name my_elasticsearch_1 elasticsearch:2
docker container run --detach --network dude --net-alias search --name my_elasticsearch_2 elasticsearch:2
```

To see wich container is called using "Round Robin", we can do a test by:

```
docker container run --rm --network dude alpine nslookup search
```

And to get specific elasticsearch response, inside your centos container 
execute multiple times this (you should get different responses from each 
container):

```
docker container run --rm --network dude centos curl -s search:9200
```

### Maintaining / Monitoring Docker filesystem 

Docker can use mauch space of your hard-drive with non used images, containers, cache, etc.

You can check docker space consuming by:

```
docker system df
```
So if we want to clean this space we can:

- Delete all non runing containers, not in use volumes and images:

**DANGER!!! You will lost your volume data** :
```
docker system prune --all 
```

- To remove only not running containers, but kee volumes and images:

```
docker system prune 
```

- To remove unused images:

```
docker image prune
```

- To remove unused containers:

```
docker container prune
```

## Images

To see image history commands

```
docker image history nginx:latest
```
 And the output will be like this:

```
 IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
cd5239a0906a        11 days ago         /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B
<missing>           11 days ago         /bin/sh -c #(nop)  STOPSIGNAL [SIGTERM]         0B
<missing>           11 days ago         /bin/sh -c #(nop)  EXPOSE 80/tcp                0B
<missing>           11 days ago         /bin/sh -c ln -sf /dev/stdout /var/log/nginx…   22B
<missing>           11 days ago         /bin/sh -c set -x  && apt-get update  && apt…   53.7MB
<missing>           11 days ago         /bin/sh -c #(nop)  ENV NJS_VERSION=1.15.0.0.…   0B
<missing>           11 days ago         /bin/sh -c #(nop)  ENV NGINX_VERSION=1.15.0-…   0B
<missing>           6 weeks ago         /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B
<missing>           7 weeks ago         /bin/sh -c #(nop)  CMD ["bash"]                 0B
<missing>           7 weeks ago         /bin/sh -c #(nop) ADD file:ec5be7eec56a74975…   55.3MB
```

All the lines are **layers** poiting to `cd5239a0906a` image. And they were 
modified in different times. Docker "caches" this layers with a unique SHA.

And to see details about image:

```
docker image inspect nginx:latest
```

It will show you:

- Exposed ports
- Env variables 
- Cmd commands
- Architecture (i.e: amd64)
- OS
- etc...

### Tagging images

Download any image:

Obs: In this example I will use **gabrielfs7/nginx:latest**

```
docker pull nginx:latest
```
Create a tag for the image

```
docker image tag nginx:latest gabrielfs7/nginx:latest
```

Push the image:

```
docker image push gabrielfs7/nginx:latest
```

Obs: Probably you will have to login on DockerHub before push the image, so:

```
docker login
```

#### Automated Build on Docler Hub

It is possible to login to https://hub.docker.com and relate you github or bitbucket accounts
to it, so you can automanted images to be build and available to https://hub.docker.com
when you commit to master for example.

It is possible to customize the build options. It is awsome!!! 

## Dockerfile

Create a file called **Dockerfile** and put it inside:

```
#
# Specify the image and version you will use as base
#
FROM debian:stretch-slim

#
# Create environment variable for your image.
#
ENV HTTP_PROXY 127.0.0.1
ENV APP_PATH /usr/local/myapp

#
# For every "RUN" statement docker will create a layer (or a cache with unique SHA).
#
RUN apt-get update \
   && apt-get install curl \ 
   && apt-get install nginx

#
# By default docker does not expose any port, so you can do it here.
#
EXPOSE 80 443

#
# Command to execute everytime container is lauched
#
CMD ["/etc/init.d/nginx", "restart"]
```

and now build it:

```
docker image build -t customenginx .
```

#### Caching Dockerfile

If in the Dockerfile above you change the by by for example **expose a new port 8080**. i.e:

```
EXPOSE 80 443 8080
```

You will note that is using cache for almost everything, but for port exposing. 
See in the result output **Using cache**. This means that Docker is using the 
**layer's cache**, so it will be very fast:

```
docker image build -t customnginx .
Sending build context to Docker daemon  4.096kB
Step 1/7 : FROM debian:stretch-slim
 ---> 26f0bb790e25
Step 2/7 : ENV NGINX_VERSION 1.13.6-1~stretch
 ---> Using cache
 ---> fa17a6384459
Step 3/7 : ENV NJS_VERSION   1.13.6.0.1.14-1~stretch
 ---> Using cache
 ---> b68fc7e35910
Step 4/7 : RUN apt-get update   && apt-get install --no-install-recommends --no-install-suggests -y gnupg1  &&  NGINX_GPGKEY=573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62;  found='';   for server in       ha.pool.sks-keyservers.net      hkp://keyserver.ubuntu.com:80       hkp://p80.pool.sks-keyservers.net:80        pgp.mit.edu     ; do        echo "Fetching GPG key $NGINX_GPGKEY from $server";         apt-key adv --keyserver "$server" --keyserver-options timeout=10 --recv-keys "$NGINX_GPGKEY" && found=yes && break;     done;   test -z "$found" && echo >&2 "error: failed to fetch GPG key $NGINX_GPGKEY" && exit 1;  apt-get remove --purge -y gnupg1 && apt-get -y --purge autoremove && rm -rf /var/lib/apt/lists/*    && echo "deb http://nginx.org/packages/mainline/debian/ stretch nginx" >> /etc/apt/sources.list     && apt-get update   && apt-get install --no-install-recommends --no-install-suggests -y                         nginx=${NGINX_VERSION}                      nginx-module-xslt=${NGINX_VERSION}                      nginx-module-geoip=${NGINX_VERSION}                         nginx-module-image-filter=${NGINX_VERSION}      nginx-module-njs=${NJS_VERSION}                         gettext-base    && rm -rf /var/lib/apt/lists/*
 ---> Using cache
 ---> 546775568a8b
Step 5/7 : RUN ln -sf /dev/stdout /var/log/nginx/access.log     && ln -sf /dev/stderr /var/log/nginx/error.log
 ---> Using cache
 ---> 9e69506ff3a6
Step 6/7 : EXPOSE 80 443 8080
 ---> Running in 5dbe738571c1
Removing intermediate container 5dbe738571c1
 ---> 47509399aa67
Step 7/7 : CMD ["nginx", "-g", "daemon off;"]
 ---> Running in 8c5408106f99
Removing intermediate container 8c5408106f99
 ---> 537999468b44
Successfully built 537999468b44
Successfully tagged customnginx:latest
```

**Tip:** Put the things that change least at the begining of your docker file, 
and the things that change the most at the bottom.


### Extending original image

This sample uses the **COPY** command to change defaul nginx html file.

```
cd dockerfile-sample-2
gsoares$ docker image build -t nginx-with-html .
docker container run -p 80:80 --rm nginx-with-html
```

and you can tag and push it:

```
docker image tag nginx-with-html gabrielfs7/nginx:1.0.0
docker image push gabrielfs7/nginx:1.0.0
```

## Container Lifetime & Persistent Data

- Ideally our application code should not remain inside the container.
- The same for our database.
- Every time your code need to change, we should recreate the container.
- There is no data lost, cause your container layers are in cache.

To solve these problems we have **Volumes** and **Bind Mounts**

- **Volumes**: make special location outside of container 
  UFS (Union FIle System).
  - Preserves data accross container removal.
  - We can attach the volume for any container we want. 
  - The container sees it as a local file path.
  - Volums need manual deletion.
- **Bind Mounts**: Mount the host file or directory inside the container.

#### Mapping Volumes

Use the `VOLUME` command inside the Dockerfile. I.e:

```
VOLUME /var/lib/mysql
```

Example of mysql image: [https://github.com/docker-library/mysql/blob/fc3e856313423dc2d6a8d74cfd6b678582090fc7/8.0/Dockerfile]

Run the container:
```
docker container run --detach --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=true mysql
```

Check the volume:
```
docker container inspect mysql
```

Inspect volume

```
docker volume ls
docker volume inspect 02d8286f0f4bbb6110a9bdb8e0d44569a26db0d408b5593ac5d7587a69f88601
```

**Name your volume**

It make easier to local your volume instead of using this giant SHA hash.

```
docker container run --detach --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=true -v mysql-volume:/var/lib/mysql mysql
docker volume inspect mysql-volume
```


###### Migrate Database Container - Real world example.

In this example we are going to migrate a DB version of a container by using 
volumes and instantiating new container.


1. Create the `postgres` container version `9.6.1` using a volume 
called `psql-data` and follow the logs.

```
docker container run --detach --publish 5433:5432 --name postgres --env POSTGRES_USER=root --env POSTGRES_USER=root -v psql-data:/var/lib/postgresql/data postgres:9.6.1
docker container logs -f postgres
```

2. Stop the current container

```
docker container stop postgres
```

2. Start the new container named `postgres2` using the **same volume** but 
version `9.6.2` and follow the logs.

```
docker container run --detach --publish 5433:5432 --name postgres2 --env POSTGRES_USER=root --env POSTGRES_USER=root -v psql-data:/var/lib/postgresql/data postgres:9.6.2
ker container logs -f postgres
```

3. Check that there is just one volume, but 2 containers.

```
docker container ls
docker volume ls
```

Now you can just make your applications to call new container.

#### Bind Mounting

- Maps a host file or directory to a container file or directory.
- Hosts files always ovewrite files in container.

Example:

```
docker container rm -f nginx
docker container run --detach --publish 80:80 --name nginx -v $(pwd)/nginx-bind-html:/usr/share/nginx/html nginx
```

Now access `https://localhost` to see the mounted directory.

And if you access the container, you will see the bind mount file:

```
docker container exec -it nginx bash
ls -lha /usr/share/nginx/html
```

And inside the container if you **change content of shared file** it will not 
affect file in the host OS.

Example, inside the container, do this.

```
echo "<br/><br/>Text added"  >> /usr/share/nginx/html/index.html
```

If you check the browser `https://localhost`, the content was changed, and the 
original file in your host OS too.

###### "Bind Mounting" real world example

It used **jekyll** template tool, so you can edit the files and see real time 
changes accessing `localhost`.

```
cd bindmount-sample-1
docker container run --publish 80:4000 --name bindmount-sample-1 -v $(pwd):/site bretfisher/jekyll-serve
```

- You can edit __bindmount-sample-1/_site/about/index.html__ and see the 
modifications by accessing the browser.

- Also you can follow the logs to see how **changes are processed by jekyll**. 
See:

```
docker container logs -f bindmount-sample-1
```

## Docker-compose

Why?

- Way to **create many containers** at once.
- Way to **configure relationship between containers**, networks, volumes and 
  bind mounting, etc.
- Configurable through **YAML files** which contains its all version 
  formats:1, 2, 1.1, etc.

### Is it good for production?

**No**. It is good for testing or development environment. For production the 
ideal is to be based on **Dockerfile** only.


### Commands

Setup volumes, networks and start all containers. This command will be the most
used one. 
```
docker-compose up
```

Stop all containers and remove containers, volumes and networks.
```
docker-compose down
```

#### Testing

Testing **docker-compose** with nginx doing reverse proxy for apache:

- Access test folder.
- Setup and start containers.
- Seee the logs.

```
cd compose-sample-2
docker-compose up -d
docker-compose logs -f
```
Test accessing http://localhost

- To see the **running docker-compose containers**:

```
docker-compose ps
```

- To see process running inside container

```
docker-compose top
```

- To stop and remove all container, networks and volumes created by docker-compose

```
docker-compose down
```

## Install "Drupal" with postgress

docker-compose.yml is located on `compose-assigment-1`.

Do not forget to provide **container's name** as host in drupal (advanced options) instalation.

To test:

```
cd compose-assigment-1
docker-compose up
```

To clean up (removing volumes and images)

```
docker-compose down -v --rmi all
```

## Install "Drupal" with postgress + Download Template + Preserve Volume

```
cd cmpose-assigment-2
docker-compose up
```
Then you can configure your themes, change data, etc. 
After `docker-compose down` you can `docker-compose up` again and you will see all modifications remain.

# Docker Swarm

Swarm is a **Built-in Container Orchestration**. See some questions Swarm can answer for us:

- How we **easily deploy and maitain** our dozens, hundreds or even thousands of containers?
- How can we **scale out/in/up/down** our application containers?
- How can we **start, restart, create and delete** many containers?
- How can we ensure our **containers restart if they fail**?
- How can we **replace containers without downtime** (blue/green deploy)?
  - This means your application is **Always Available**.
- How to create cross-node virtual networks?
- How can we ensure **only trusted servers** run our containers?
- How can we **store secrets, keys, passwords** and get them to the right container?

Good content to read about **Swarm Services** [https://docs.docker.com/engine/swarm/services/]

### Swarm Managers

- Manager is a **Worker with permission to controle the Swarm**.
- They send orders to the **Workers**.
- They contain an internal Database to store configuration called **RAFT**.
- They store in this database the **Certificate of Authority**.
- Store **configuration like replica numbers, rules to scale**, etc.

### Swarm Workers

- They **receive orders from Managers** like start/restart/create/delete containers.


## Activating Swarm

See if Swarm is active:

```
docker info | grep Swarm
```

To initialize swarm:

```
docker swarm init
```

It just did:

- **PKI and security automation**.
 - Root Signing Certificate created for our Swarm.
 - Certificate is issued for first Manager node.
 - Join tokens are created.
- **RAFT database created to store root CA, configs and secrets**.
 - Encrypted by default on disk (1.13+)
 - No need for another key/value system to hold orchestration/secrets.
 - Replicates logs amongst Managers via mutual TLS in "control plane".

 We can see the node details:

```
docker node ls

# output
ID                            HOSTNAME                STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
6pypmtllxqf0o156z3shlzrr9 *   linuxkit-025000000001   Ready               Active              Leader              18.03.1-ce
```

**Creating a Service** for **Alpine image** and ping to Google DNS server:

```
docker service create alpine ping 8.8.8.8
```

It will return the ID of the **created service** with 1 Replica. See:

```
docker service ls
```

and to **see containers inside service**

```
docker service ps <SERVICE_ID>
```

Now we can **update number of replicas** for the service:

```
docker service update <SERVICE_ID> --replicas 3
docker service ps <SERVICE_ID>
```

And if you remove one of the 3 containers replicas, it will recreate the replica again.

```
docker container ls
docker container rm -f <CONTAINER_REPLICA_ID>
docker service ls
docker service ps jpeitdtnedha
```

And finaly to kill the service:

```
docker service rm epic_rosalind
```
__Note__: It will kill all containers for this service replicas.


## Creating a Docker Swarm Cluster

In this case I opted to use **docker-machine** do create the nodes, but you can use
Amazon, GoogleCloud or any other technology to create them.

The `docker-machine` will create **very lightweight linux virtual machine**.

```
docker-machine create node1
docker-machine create node2
docker-machine create node3
```

... and to access the **docker-machines** we can type:

```
docker-machine ssh node1
```

... or to get **docker-machine details** (needed to build the swarm, like IP, etc):

```
docker-machine env node1
```

In this example, we will use **docker-machine ssh** to get inside machines and 
configure the **Swarm Cluster**.

So **ssh** for the first node:

```
docker-machine ssh node1
```

... and inside the `node1`, **init the swarm**.

```
docker swarm init
```

... the command above will ask you to use the `--advertise-addr` to provide an IP, 
so choose one and run again. My local was:

```
docker swarm init --advertise-addr 192.168.99.100
```

... so, the command above will create a **Manager** and show you a 
**join command** to be executed inside the `node2`.

My output, for instance was:

```
Swarm initialized: current node (mi8mnfbdg8ov0pp901sxnllz1) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-44fx0w9arzepmjim9apgw2i1gha9a23mse8fg5qou1ymtpni05-9mexiv7xp2dtb6dsgryufezeh 192.168.99.100:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

Good article to handle with Swarm port [https://www.bretfisher.com/docker-swarm-firewall-ports/].

So now, **ssh** to the `node2` and executed the provided command:

```
docker swarm join --token SWMTKN-1-44fx0w9arzepmjim9apgw2i1gha9a23mse8fg5qou1ymtpni05-9mexiv7xp2dtb6dsgryufezeh 192.168.99.100:2377
```

**Well done!** Now `node2` joined to the Swarm as a **Worker**.

...If you check the nodes after **ssh** inside `node1`:

```
docker@node1:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
mi8mnfbdg8ov0pp901sxnllz1 *   node1               Ready               Active              Leader              18.06.0-ce
fzvvi37tctddflavb2yfw6dfb     node2               Ready               Active                                  18.06.0-ce
```

You will see that `node1` is the **Leader** (The Manager).

So, if we want to transform `node2` into a **Manager**, inside `node1` we type:

```
docker node update --role manager node2
```

And then we see that manager status was updated:

```
docker@node1:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
mi8mnfbdg8ov0pp901sxnllz1 *   node1               Ready               Active              Leader              18.06.0-ce
fzvvi37tctddflavb2yfw6dfb     node2               Ready               Active              Reachable           18.06.0-ce
```

Note that the `*` in the **ID** means that the node we are **talking to**.

... But, what about the `node3`? Let's add `node3` as **Manager by default**.
For this, inside `node1` type:

```
docker swarm join-token manager
```

It will generate a token which can be used to add any node as manager. My 
output was:

```
To add a manager to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-44fx0w9arzepmjim9apgw2i1gha9a23mse8fg5qou1ymtpni05-d43llv24kk9vmht3khfodgct4 192.168.99.100:2377
```

Did you get it? So let's do it! Go **ssh** to the `node3` and execute:

```
docker swarm join --token SWMTKN-1-44fx0w9arzepmjim9apgw2i1gha9a23mse8fg5qou1ymtpni05-d43llv24kk9vmht3khfodgct4 192.168.99.100:2377
```

See the result inside `node1`:

```
docker@node1:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
mi8mnfbdg8ov0pp901sxnllz1 *   node1               Ready               Active              Leader              18.06.0-ce
fzvvi37tctddflavb2yfw6dfb     node2               Ready               Active              Reachable           18.06.0-ce
pae7vqclkh7zo0i8xvad333co     node3               Ready               Active              Reachable           18.06.0-ce
```

So let's start **Creating Containers inside the Swarm Cluster**! Inside `node1`:

```
docker@node1:~$ docker service create --replicas 3 alpine ping 8.8.8.8
docker@node1:~$ docker service ls
ID                  NAME                MODE                REPLICAS            IMAGE               PORTS
xcubybeasggi        nifty_albattani     replicated          3/3                 alpine:latest
```

**So What happened?**. Basically every node joined to the Swarm has now an 
`alpine:latest` container running. You can check by accessing each node, like this:




**node1:**

```
docker@node1:~$ docker service ps nifty_albattani
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
p2t1pc5izauz        nifty_albattani.1   alpine:latest       node1               Running             Running 8 minutes ago
7y44ewmjtsmh        nifty_albattani.2   alpine:latest       node2               Running             Running 8 minutes ago
qjxx02xqj64s        nifty_albattani.3   alpine:latest       node3               Running             Running 8 minutes ago

docker@node1:~$ docker node ps
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
p2t1pc5izauz        nifty_albattani.1   alpine:latest       node1               Running             Running 5 minutes ago

docker@node1:~$ docker container ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
3f31e6d25b0a        alpine:latest       "ping 8.8.8.8"      5 minutes ago       Up 5 minutes                            nifty_albattani.1.p2t1pc5izauzp62c8m5q2d2h6
docker@node1:~$
```

**node2:**

```
docker@node2:~$ docker node ps
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
7y44ewmjtsmh        nifty_albattani.2   alpine:latest       node2               Running             Running 6 minutes ago

docker@node2:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
614bcb71c10d        alpine:latest       "ping 8.8.8.8"      6 minutes ago       Up 6 minutes                            nifty_albattani.2.7y44ewmjtsmh80spe1eappdtq
```

**node3**

```
docker@node3:~$ docker node ps
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
qjxx02xqj64s        nifty_albattani.3   alpine:latest       node3               Running             Running 7 minutes ago

docker@node3:~$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
771dbe099ec2        alpine:latest       "ping 8.8.8.8"      7 minutes ago       Up 7 minutes                            nifty_albattani.3.qjxx02xqj64sqw780wzo82axf
```

Now we can update all the nodes from `node1` and it will propagate through the Swarm Cluster!



## Create a multi-layer netwrok for Swarm hosts.

You need to access **node1** we created above and create a **network** inside of it.

```
docker network create --driver overlay my_drupal_network
```

Let's now create our **Postgres Service** inside **node1** also.

```
docker service create --name my_drupal_postgres --network my_drupal_network -e POSTGRES_PASSWORD=postgres postgres:9.6.2
```

Then we can verify the results by running all these commands:

```
docker service ls
docker service ps my_drupal_postgres
docker container logs my_drupal_postgres
```

Now we can create the **Drupal Service**

```
docker service create --name my_drupal --network my_drupal_network --publish 80:80 drupal:8.5.5-apache
```

So if you can verify now that the **my_drupal** service will be running in **node2**

```
docker service ls
docker service ps my_drupal
```

... Now you can get nodes IP address, by running:

```
docker-machine env node1
docker-machine env node2
docker-machine env node3
```

... and access these IPs on **Port 80** (which we have choosen for my_drupal).
... The drupal installation screen will appear and you can setup postgres host as **my_drupal_postgres**
... then finish the installation and you will see that all 3 IPs (node1, node2 and node3) are responding from Drupal.

But why did the all nodes respond for **port 80 requests** if **my_drupal** contaier was inside **node2**?

   It was because of **Routing Mesh**!

## Routing Mesh

It is a **Routes ingress (or incoming) network to distribute packages** for a service to a **proper Task**.

- It spans **all the nodes** in Swarm.
- It **Load Balances** all the nodes Swarm Services across their tasks.
- It **uses IPVS** (Virtual IP Server) from Linux Kernel.

Let's test it with **3 ElasticSearch replicas** in our swarm. So inside **node1** (the Manager), type:

```
docker service create --name es_search --replicas 3 --publish 9200:9200 elasticsearch:2
```

It will create 3 ElasticSearhc container, one for each node. You can check:

```
docker service ps es_search
```

My output was:

```
docker@node1:~$ docker service ps es_search
ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE            ERROR               PORTS
eblyibinvod2        es_search.1         elasticsearch:2     node3               Running             Running 56 seconds ago
ksydkfspl0gh        es_search.2         elasticsearch:2     node2               Running             Running 14 seconds ago
ppn7cmhq53tj        es_search.3         elasticsearch:2     node1               Running             Running 50 seconds ago
```

Now you can check all ElasticSearch tasks (or containers) are responding. Execute the command above 
and you will see that the "name" of ElasticSerch application will change.

```
curl localhost:9200
```

... and this is the VIP acting as a **load balancer** and distributing the request across the the tasks (or containers).

Attention:

- This is a Load Balancer at OSI (Open Systems Interconnections) Layer 3 (TCP), not Layer 4 (DNS), so it takes decision based on **IP only**, **Not considering port**.
- It does not replace a need for a real DNS loadbalancer like NGinx or HAProxy.

## Deploing multi-tier "Voting App" with Swarm + Volumes + Overlay Network + Routing Mesh:

The application is inside ![Voting App](/swarm-app-1) directory.

![Voting App](/swarm-app-1/architecture.png "Voting App")

We will need:

- 1 volume
- 2 networks
- 5 services
- Everything is using **Docker Hub** images. **No building should be used** inside the Swarm.

To do that, inside **node1** (the Manager):

Create the **Networks**
```
docker network create --driver overlay frontend
docker network create --driver overlay backend
```

Create **vote** service for **frontend** network:
```
docker service create --replicas 2 --publish 80:80 --network frontend --name vote dockersamples/examplevotingapp_vote:before
```

Create **Redis** service for **frontend** network:
```
docker service create --replicas 1 --network frontend --name redis redis:3.2
```

Create **worker** service to process **redis votes** and stores in **postgres** enabled for **frontend** and **backend** networks
```
docker service create --replicas 1 --network frontend --network backend --name worker dockersamples/examplevotingapp_worker
```

Create **db** service to store votes, enabled for **backend** network and volume **db-data**
```
docker service create --replicas 1 --network backend --mount type=volume,source=db-data,target=/var/lib/postgresql/data --name db postgres:9.4
```

Create **result** service running on port **5001** on **backend** network
```
docker service create --replicas 1 --network backend --name result --publish 5001:80 dockersamples/examplevotingapp_result:before
``` 

# Docker Swarm - Stacks of Services

Use docker compose networks and volumes for Swarm deploy. Stack is like the 
**docker-compose for Swarm**. So we have a `.yml` file containing the 
instructions to build our **Stack**.

### Lets try the example:

The example in **(swarm-stack-1)** show the `.yml` file which contains all the 
instructions to create the **stack** (whith networks, containers, replicas, etc).

It is the same architecture used on **/swarm-app-1**. Please copy 
`example-voting-app-stack.yml` inside **node1 /home/docker** and execute:

```
cd swarm-stack-1
docker stack deploy --compose-file example-voting-app-stack.yml voteapp
```

It will not create all the services fast. It will be **assync**, so if you run 
`docker service ls` you will se replicas as **0/N** for most of the services.

To see all **images, nodes and tasks in the Stack** we type:

```
docker stack ps voteapp
```

... or to see also replicas

```
docker stack services voteapp
```

You can access the **visualizer** on your browser to see **really cool view**
of containers, nodes, hardware, etc of your stack 
by (where 192.168.99.102 is my node1 ip) on `http://192.168.99.102:8080/`, 
to vote:`http://192.168.99.102:5000/` and to see 
results `http://192.168.99.102:5001/`.


### SECURITY: Storing "secrets" on Swarm

Swarm supports **store "screts"** like generic strings or binary 
content **up to 500kb**.

**What are the "secrets"?**

- TLS certificates
- username and passwords
- SSH keys and keys
- Any other data we do not want to be exposed

**Features:**

- Swarm RAFT db is **encrypted on disk**.
- Only stores on the disk of **Manager nodes**.
- Communication between **managers and workers** has mutual auth using PKI and TLS.
- They look like files in container, but they are actually **in-memory**. Example:
    `/run/secrets/<secret_name>` or `/run/secrets/<secret_alias>`.


##### Using Secrets in Swarm Services

The example is in `secrets-sample-1`, so **in "node1" go to that folder** and:

```
docker secret create psql_user psql_user.txt
```

And also we can store a password, like:

```
echo "mypass" | docker secret create psql_pass -
```

So now we can list ans inspect the secrets by:

```
docker secret ls
docker secret inspect psql_user
docker secret inspect psql_pass
```

But the **only way to get access to those secrets** values is by assign 
**authorized services or containers** to it. Example:

Create a service providing access to secret as **environment variables**:

```
docker service create --name psql --secret psql_pass --secret psql_user -e POSTGRES_PASSWORD_FILE=/run/secrets/psql_pass -e POSTGRES_USER_FILE=/run/secrets/psql_user postgres
```

Now, get the **node and container** which this service is running, 
so there we will **find the secret files**. We can do it by executing these commands:

```
docker service ps psql
docker container exec -it <<CONTAINER_NAME>> bash
cat /run/secrets/psql_user
cat /run/secrets/psql_pass
```

We can also **remove or add secrets**, but it will **recreate the containers**.

```
docker service update --secret-rm psql_user
docker service update --secret-add psql_user myuser
```

##### Using Secrets in Swarm Stack

The example is in `secrets-sample-2`. So **inside "node1", go to this directory**:

Create 3 replicas of ElasticSearch:

```
docker service create --name search --replicas 3 -p 9200:9200 elasticsearch:2
```

Deploy the Stack using the compose file:

```
docker stack deploy -c docker-compose.yml mydb
```

To see how to use **external secret to stack deploy**, 
check **secrets-assignment-1**.

# Swarm App Lifecycle

## Using Secrets With Local Docker Compose

You can check the sample [here](secrets-sample-2). Execute the commands bellow:

```
docker node ls
```

```
docker-compose up -d
```

For the command bellow mount the volumes in 'secrets.psql_user' inside 'docker-compose.yml' file.

```
docker-compose exec psql cat /run/secrets/psql_user
```

Check the `secrets` mapping:

```
pcat docker-compose.yml
```

## Full App Lifecycle: Dev, Build and Deploy With a Single Compose Design

Access sample [here](swarm-stack-3) and execute commands bellow:

```
docker-compose up -d
```

```
docker inspect TAB COMPLETION
```

```
docker-compose down
```

```
docker-compose -f docker-compose.yml -f docker-compose.test.yml up -d
```

Now the volume was override by the `docker-compose.test.yml` file. 

```
docker inspect TAB COMPLETION
```

We can use the `config` command to merge `docker-compose` files.

```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml config --help
```

This will output merged configuration:

```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml config
```

...and you can put this configuration in a file:

```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml config > output.yml
```

## Service Updates: Changing Things In Flight

Create a service on the stack with Nginx image.

```
docker service create -p 8088:80 --name web nginx:1.13.7
```

```
docker service ls
```

Scaling swarm stack to 5 instances.

```
docker service scale web=5
```

Change in Flight service image to an older version of nginx.
It will not replace all replicas at once, it will change one by one smoothly.

```
docker service update --image nginx:1.13.6 web
```

Change the publish port in Flight. 
It will exchange the previously exposed port 80 from 8088 to 9090.

```
docker service update --publish-rm 8088 --publish-add 9090:80 web
```

Force update of all the `web` containers in the all the nodes. 

```
docker service update --force web
```

## Health checks in Docker files

Create a container `p1` using postgres image.

```
docker container run --name p1 -d postgres
```

```
docker container ls --filter name=p1
```

Create a `cmd command` to report status check of the container.
In this case we keep checking postgres connection status.

```
docker container run --name p2 -d --health-cmd="pg_isready -U postgres || exit 1" postgres
```

```
docker container ls --filter name=p2
```

Here it is possible to check current container status and health check logs:

```
docker container inspect p2 --format '{{ .State.Health.Status }}'
docker container inspect p2 --format '{{json .State.Health.Log }}'
```

```
docker service create --name p1 postgres
```

It is also possible to add health check for all replicas of a swarm.

```
docker service create --name p2 --health-cmd="pg_isready -U postgres || exit 1" postgres
```


# Docker Registry

- Docker Registry is a **HTTPS server** listen to **port 5000** by default.
- It is a **storage** for **Docker images**.

To use local registry with self-signed certificate, access [registry-sample-1](registry-sample-1). 

We can create the registry server like this:

Generate certificates ([here](https://training.play-with-docker.com/linux-registry-part2/) you can find full example): 

```
cd registry-sample-1
mkdir -p certs
openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key -x509 -days 365 -out certs/domain.crt
```

Run registry securely with the certificate:

```
docker run --rm -e COMMON_NAME=127.0.0.1 -e KEY_NAME=registry -v $(pwd)/certs:/certs centurylink/openssl
```

And create the registry

```
docker container run -d -p 5000:5000 --name registry registry
```

Lets create a tag for a image and **store it to our local registry**:

Download the sample image:

```
docker pull hello-world
```

Now tag the image with your host ip (in this case `127.0.0.1`) and port (in this case `5000`):

```
docker tag hello-world 127.0.0.1:5000/hello-world
```

Now push it to your local registry:

```
docker push 127.0.0.1:5000/hello-world 
```

Check your images now: 

```
docker image ls
```

Now that we saved our image to local registry, we can remove the original and new image:

```
docker image rm hello-world
docker image rm 127.0.0.1:5000/hello-world
```

If we want to **remove (and clean)** the local registry:
 
```
docker container kill registry
docker container rm registry
```
 
Cool!!!   :) 

But the smart thing is to create a volume to store your local images, 
this way you can **transport/backup** it.
 
To do this, we should create the registry like this:

```
docker container run -d -p 5000:5000 --name registry -v $(pwd)/registry-data:/var/lib/registry registry
```

Now we can tag/push the image to the the local registry volume:

```
docker tag hello-world 127.0.0.1:5000/hello-world
docker push 127.0.0.1:5000/hello-world
```

Now you can check inside the volume that the image is there inside the folder `docker`:

```
tree registry-data
```

You can create **basic authentication over https** (I used username "moby" and password "gordon" in this example):

```
mkdir auth
docker run --entrypoint htpasswd registry:latest -Bbn moby gordon > auth/htpasswd
```

Check that the username and password were save here: 

```
cat auth/htpasswd
```

Now you can run the registry using `htpasswd` authentication:

```
docker kill registry
docker rm registry
docker run -d -p 5000:5000 --name registry \
  --restart unless-stopped \
  -v $(pwd)/registry-data:/var/lib/registry \
  -v $(pwd)/certs:/certs \
  -v $(pwd)/auth:/auth \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
  -e REGISTRY_AUTH=htpasswd \
  -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
  -e "REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd" \
  registry
```

Now you can login to it:

```
docker login 127.0.0.1:5000
```

and then pull the image:

```
docker pull 127.0.0.1:5000/hello-world
```

## Docker registry with Swarm


This is useful, cause if you have a Swarm you cannot make the nodes download images from a single registry container.
It needs to be a Swarm registry in order to make all Swarm nodes to pull this image.

To do this, we can create a swarm of 5 managers and no workers on [https://labs.play-with-docker.com](https://labs.play-with-docker.com).

- Click on the tool icon and choose `5 Managers and no workers`:

Then we can create the registry for our swarm:

```
docker service create --name registry --publish 5000:5000 registry
```

Now you can check service is running:

```
docker service ps registry
```

If you access the registry catalog you will see it is empty (on play-with-docker.com you can access the 5000 link). Example:

```
http://ip172-19-0-41-bft56dgv0j3g00el2hkg-5000.direct.labs.play-with-docker.com/v2/_catalog
```

It will return empty repositories, like this:

```
{"repositories": []}
```

Now we can start `populating` our repositories by downloading and tagging our first image:

```
docker pull hello-world
```

And tag:

```
docker tag hello-world 127.0.0.1:5000/hello-world
```

and push:

```
docker push 127.0.0.1:5000/hello-world
```

Now if you check the repositories URLs there must be another repository there:

Lets test the propagation of a **Nginx** image on our **Swarm Registry Server**:

```
docker pull nginx
docker tag nginx 127.0.0.1:5000/nginx
docker push 127.0.0.1:5000/nginx
```

Now if we create a service in our Swarm specifying the image from our 
registry, it will be **available on all 5 Swarm nodes** (cause I specify the replicas):
  
```
docker service create --name nginx --publish 80:80 --replicas 5 --detach=false 127.0.0.1:5000/nginx
```

Now you can access the link `80` on each node and check nginx is 
running **using your Swarm Registry image**. In my case:

```
http://ip172-19-0-41-bft56dgv0j3g00el2hkg-80.direct.labs.play-with-docker.com/
```

You can check the services running your `nginx` image:

```
docker service ps nginx
```

...So the five nodes will have this! :)

