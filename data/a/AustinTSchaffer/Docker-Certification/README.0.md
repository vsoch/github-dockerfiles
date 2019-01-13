# Assignments

This directory is for any demos or assignments that were completed either just
for fun, or were assigned by the Docker course on UDemy.
# Assignment 5 - Performing Database Upgrades using Volumes

- Database upgrades with containers
- Create a `postgres` container with named volume `psql-data` using image tag
  `9.6.1`.
- User Docker Hub documentation to learn VOLUME path and versions needed to run
  it.
- Check logs until container is done starting up. Stop the container.
- Create a new postgres container with the same named volume, but using
  `postgres` version `9.6.2`
- Check new logs


## Notes

This is a SQL database. The first container must be stopped before mounting the
volume in the second. DBs cannot have multiple DB Daemons, typically.

You cannot jump versions too quickly (i.e. v1 to v99). This is a limitation of
Postgres and other DB systems, not Docker.


## Environment Variables

**PGDATA.** This optional environment variable can be used to define another
location - like a subdirectory - for the database files. The **default is
/var/lib/postgresql/data**, but if the data volume you're using is a fs
mountpoint (like with GCE persistent disks), Postgres initdb recommends a
subdirectory (for example /var/lib/postgresql/data/pgdata ) be created to
contain the data.

**POSTGRES_PASSWORD.** This environment variable is recommended for you to use
the PostgreSQL image. This environment variable sets the superuser password for
PostgreSQL. The default superuser is defined by the POSTGRES_USER environment
variable.
# Assignment 9 - Create a MultiService App

- Docker's Distributed Voting App
- Use `swarm-app-1` from bretfischer repo
- 1 volume, 2 networks, 5 services
- Create the commands needed, spin up services, and test app
- Everything is using Docker Hub images, so no data needed on Swarm
- You don't want to be building images on your Swarm. THAT IS BAD.
- This assignment is 1/2 science, 1/2 art.
# Assignment: Create A Multi-Service Multi-Node Web App

## Goal: create networks, volumes, and services for a web-based "cats vs. dogs" voting app.

- See architecture.png in this directory for a basic diagram of how the 5 services will work
- All images are on Docker Hub, so you should use editor to craft your commands locally, then paste them into swarm shell (at least that's how I'd do it)
- a `backend` and `frontend` overlay network are needed. Nothing different about them other then that backend will help protect database from the voting web app. (similar to how a VLAN setup might be in traditional architecture)
- The database server should use a named volume for preserving data. Use the new `--mount` format to do this: `--mount type=volume,source=db-data,target=/var/lib/postgresql/data`

### Services (names below should be service names)
- vote
    - dockersamples/examplevotingapp_vote:before
    - web front end for users to vote dog/cat
    - ideally published on TCP 80. Container listens on 80
    - on frontend network
    - 2+ replicas of this container

- redis
    - redis:3.2
    - key/value storage for incoming votes
    - no public ports
    - on frontend network
    - 1 replica NOTE VIDEO SAYS TWO BUT ONLY ONE NEEDED

- worker
    - dockersamples/examplevotingapp_worker
    - backend processor of redis and storing results in postgres
    - no public ports
    - on frontend and backend networks
    - 1 replica

- db
    - postgres:9.4
    - one named volume needed, pointing to /var/lib/postgresql/data
    - on backend network
    - 1 replica

- result
    - dockersamples/examplevotingapp_result:before
    - web app that shows results
    - runs on high port since just for admins (lets imagine)
    - so run on a high port of your choosing (I choose 5001), container listens on 80
    - on backend network
    - 1 replica
# Assignment 1 - 3 Container Application

- Run `nginx`, `mysql`, `httpd` (apache) servers
- Detach all of them and give them all a name.
- Port mappings
    - nginx: 80:80
    - httpd: 8080:80
    - mysql: 3306:3306
- Use `--env` to generate a random root password for the mysql instance in the
  mysql container. Use `docker container logs` to get that password.
- Use docker container stop and docker container rm to clean up afterward.
- Use docker container ls to show that everything is cleaned up.
# Assignment 4 - Create Your Own Image

Dockerize an existing node.js app.

## Objectives

- Take an existing node.js app and Dockerize it
- Make a Dockerfile for the node.js application.
- Details are in the Dockerfile of the application
- Use the alpine version of Node 6.X as a base image
- Expected resulting website is http://localhost (need to expose port 80, so
  port-forwarding can be enabled)
- Push the completed image to a repository in the Docker
  Hub.
- Remove the local images and run the image, which should pull the image down
  from the Hub.

## Node App

The node app was provided by

- Repo: https://github.com/BretFisher/udemy-docker-mastery
- Directory: `dockerfile-assignment-1/`

**Note:** If you're cloning this repo, there should be a symbolic link from the
"node-app" of this directory, to the `dockerfile-assignment-1/` directory of the
git submodule, that points to the repo specified above. If it did not work, copy
the directory from the submodule as a subdirectory of this directory, with the
dir name of "node-app/". Destroy the symlink if you have to.

## Difficulties

1. Having a hard time running the `apk add tini` when building the image, when
   connected to public wifi. This is causing the `docker image build` to fail.
   Getting errors when it is trying to fetch the APKINDEX. It is possible to
   download the .tar.gz files onto my host machine with no issue.

    Step 2/9 : RUN apk add --update tini
    ---> Running in 5eae06851684
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/APKINDEX.tar.gz
    ERROR: http://dl-cdn.alpinelinux.org/alpine/v3.4/main: temporary error (try again later)
    WARNING: Ignoring APKINDEX.167438ca.tar.gz: No such file or directory
    fetch http://dl-cdn.alpinelinux.org/alpine/v3.4/community/x86_64/APKINDEX.tar.gz
    ERROR: http://dl-cdn.alpinelinux.org/alpine/v3.4/community: temporary error (try again later)
    WARNING: Ignoring APKINDEX.a2e6dac0.tar.gz: No such file or directory
    ERROR: unsatisfiable constraints:
    tini (missing):
        required by: world[tini]


# Assignment 10 - Create Stack with Secrets

- Fork Assignment 8 (compose-assignment-2)
- Use drupal:8.2 image
- Remove `build:`
- Add secret via `external:`
- Use environment variable `POSTGRES_PASSWORD_FILE`
- Add secret via `echo "<pw>" | docker secret create psql-pw`
- Copy compose to a swarm node and deploy.

## Notes

Bash history is written on logout. Also, if you start a command with a space, it
won't be written to the history, as long as `HISTCONTROL=ignoreboth`. If you
forget this, you can commit the history to file, truncate bash history, then log
out and back in.

```bash
# Scorch the Earth method
export HISTCONTROL=ignoreboth
 echo "mypsqlpassword123!!!" | docker secret create mypsqlpassword -
history -a
truncate --size 0 ~/.bash_history
truncate --size 0 ~/.history
exit
```

When specifying external secrets in the stack compose file, you can either use
the boolean syntax, or the mapping syntax. The boolean syntax specifies that the
external secret has the same name as the stack secret.

```yml
secrets:
  external_secret:
    external: true
  mapped_external_sectret:
    name: some_external_secret
```
# Assignment 2 - CLI App Testing

## Objectives

Check the `curl` version bundled on various Linux distros.

## Script

```bash
sudo docker container run -it --rm centos:7 curl --version

sudo docker container run -it --rm ubuntu:14.04 curl --version
# sudo apt update
# sudo apt install curl
# curl --version
# exit

sudo docker container run -it --rm alpine:3.8 /bin/sh
# apk add curl
# curl --version
```

## Results

| Linux OS	| Image Tag 	| CURL Version 	|
|-		|-		|-		|
| Centos 	| 7		| 7.29.0	|
| Ubuntu	| 14.04		| 7.35.0	|
| Alpine	| 3.8		| 7.61.1	|

# Assignment 8 - Building a Docker-Compose File

- build a basic compose file for a Drupal CMS website.
- Use the `drupal` image along with a `postgres` image
- Use `ports` to expose the Drupal server on 8080 on the host machine.
- Be sure to set `POSTGRES_PASSWORD` for postgres
- Drupal assumes that DB is on `localhost`. Make sure it is using the POSTGRES
  container
- Extra Credit: Use volumes to store Drupal's unique data.

## Solution

I also added `adminer` to the solution. This allowed me to debug connections to
the db image, because I'm unfamiliar with Postgres, along with any command line
utilities for connecting to Postgres. I also wanted to see how `adminer` worked,
since I've seen it on so many sample `docker-compose.yml` files.

## Expansion

Use compose for local building/testing using compose's 
image building capabilities.# Assignment: Compose For On-The-Fly Image Building and Multi-Container Testing

Goal: This time imagine you're just wanting to learn Drupal's admin and GUI, or
maybe you're a software tester and you need to test a new theme for Drupal. When
configured properly, this will let you build a custom image and start everything
with `docker compose up` including storing important db and config data in
volumes so the site will remember your changes across Compose restarts.

- Use the compose file you created in the last assignment (drupal and postgres)
  as a starting point.
- Let's pin image version from Docker Hub this time. It's always a good idea to
  do that so a new major version doesn't surprise you.

## Dockerfile
- First you need to build a custom Dockerfile in this directory,
  `FROM drupal:8.2`
- Then RUN apt package manager command to install git:
  `apt-get update && apt-get install -y git`
- Remember to cleanup after your apt install with `rm -rf /var/lib/apt/lists/*`
  and use `\` and `&&` properly. You can find examples of them in drupal
  official image. More on this below under Compose file.
- Then change `WORKDIR /var/www/html/themes`
- Then use git to clone the theme with:
  `RUN git clone --branch 8.x-3.x --single-branch --depth 1 https://git.drupal.org/project/bootstrap.git`
- Combine that line with this line, as we need to change permissions on files
  and don't want to use another image layer to do that (it creates size bloat).
  This drupal container runs as www-data user but the build actually runs as
  root, so often we have to do things like `chown` to change file owners to the
  proper user: `chown -R www-data:www-data bootstrap`. Remember the fist line
  needs a `\` at end to signify the next line is included in the command, and at
  start of next line you should have `&&` to signify "if first command succeeds
  then also run this command"
- Then, just to be safe, change the working directory back to its default (from
  drupal image) at `/var/www/html`

## Compose File
- We're going to build a custom image in this compose file for drupal service.
  Use Compose file from previous assignment for Drupal to start with, and we'll
  add to it, as well as change image name.
- Rename image to `custom-drupal` as we want to make a new image based on the
  official `drupal:8.2`.
- We want to build the default Dockerfile in this directory by adding `build: .`
  to the `drupal` service. When we add a build + image value to a compose
  service, it knows to use the image name to write to in our image cache, rather
  then pull from Docker Hub.
- For the `postgres:9.6` service, you need the same password as in previous
  assignment, but also add a volume for `drupal-data:/var/lib/postgresql/data`
  so the database will persist across Compose restarts.

## Start Containers, Configure Drupal
- Start containers like before, configure Drupal web install like before.
- After website comes up, click on `Appearance` in top bar, and notice a new
  theme called `Bootstrap` is there. That's the one we added with our custom
  Dockerfile.
- Click `Install and set as default`. Then click `Back to site` (in top left)
  and the website interface should look different. You've successfully installed
  and activated a new theme in your own custom image without installing anything
  on your host other then Docker!
- If you exit (ctrl-c) and then `docker-compose down` it will delete containers,
  but not the volumes, so on next `docker-compose up` everything will be as it
  was.
- To totally clean up volumes, add `-v` to `down` command.
# Assignment 3 - Containers and DNS

This assignment is to test linking between containers within a Docker virtual
network.

## Prerequisites

- Know how to use -it to get shell in a container
- Understand the basics of a Linux Distro
- Docker Container management (run, rm, inspect, port)
- Basics of DNS records

## Objectives

DNS Round Robin. 2 different hosts with 2 different aliases, that respond to the
same name. Multiple IP address and DNS records behind the name that you're
using. For example, the google.com DNS name 100% has more than 1 server that you
can connect to.

Since Docker Engine 1.11, you can assign aliases so that multiple containers
respond to the same DNS address. You can add as many containers that you want
under the same net alias.

## Task

- Create a new virtual network
- Create 2 `elasticsearch:2` containers.
- Research and use `--net-alias search` when creating them to give them an
  additional DNS name to respond to.
- Run `alpine nslookup search` with `--net` to see the 2 containers for the same
  DNS name.
- Run `centos curl -s search:9200` with `--net` multiple times to see the round
  robin in action.

## Solution

```bash
docker container run -d --name es1 elasticsearch:2
docker container run -d --name es2 elasticsearch:2
docker container run -d --name es3 elasticsearch:2

docker network create elasticsearch_net

docker network connect --alias search elasticsearch_net es1
docker network connect --alias search elasticsearch_net es2
docker network connect --alias search elasticsearch_net es3

docker container run --name alpine alpine:3.8 nslookup search 
# nslookup: can't resolve '(null)': Name does not resolve
# Name:      search
# Address 1: 137.155.254.55

docker network connect elasticsearch_net alpine

docker container start -ia alpine 
# nslookup: can't resolve '(null)': Name does not resolve
# Name:      search
# Address 1: 172.19.0.4 es3.elasticsearch_net
# Address 2: 172.19.0.2 es1.elasticsearch_net
# Address 3: 172.19.0.3 es2.elasticsearch_net

docker container run -it --name centos --rm --network elasticsearch_net centos:7 /bin/bash
yum install -y bind-utils
nslookup search
# Server: 127.0.0.11
# Address: 127.0.0.11#53
# 
# Non-authoritative answer:
# Name: search
# Address: 172.19.0.2
# Name: search
# Address: 172.19.0.3
# Name: search
# Address: 172.19.0.4

curl search:9200 # { name: "Mop Man", ... }
curl search:9200 # { name: "Mop Man", ... }
curl search:9200 # { name: "Mister One", ... }
curl search:9200 # { name: "Bishop", ... }
curl search:9200 # { name: "Mop Man", ... }
# etc
exit

docker container rm -f es1 es2 es3 alpine
```

## Notes

Please note that DNS-round-robin is not an acceptable stand-in for a genuine
load balancer.

If you keep retrying the connection to the search service, you'll notice that
the machine that is chosen is a bit random every time.
# Assignment 7 - Building a Docker-Compose File

- build a basic compose file for a Drupal CMS website.
- Use the `drupal` image along with a `postgres` image
- Use `ports` to expose the Drupal server on 8080 on the host machine.
- Be sure to set `POSTGRES_PASSWORD` for postgres
- Drupal assumes that DB is on `localhost`. Make sure it is using the POSTGRES
  container
- Extra Credit: Use volumes to store Drupal's unique data.

## Solution

I also added `adminer` to the solution. This allowed me to debug connections to
the db image, because I'm unfamiliar with Postgres, along with any command line
utilities for connecting to Postgres. I also wanted to see how `adminer` worked,
since I've seen it on so many sample `docker-compose.yml` files.
# Assignment 6 - Jekyll Static Site Generator

- Use Jekyll "Static Site Generator" to start a local web server
- Bridge gap between local file access and apps running in containers
- Use `bindmount-sample-1` for source code
- Edit files with editor on our host using native tools
- Container detects changes with host files
- Use Bret Fisher's Jekyll Server
- Change the file in `_posts/` and refresh browser

```bash
docker run -p 80:4000 -v "$(pwd):/site" bretfisher/jekyll-serve
```

# [Start Bootstrap](http://startbootstrap.com/) - [Agency](http://startbootstrap.com/template-overviews/agency/)

[Agency](http://startbootstrap.com/template-overviews/agency/) is a one page agency portfolio theme for [Bootstrap](http://getbootstrap.com/) created by [Start Bootstrap](http://startbootstrap.com/). This theme features several content sections, a responsive portfolio grid with hover effects, full page portfolio item modals, a responsive timeline, and a working PHP contact form.

## Getting Started

Several options are available to get started quickly:
* [Download the latest release on Start Bootstrap](http://startbootstrap.com/template-overviews/agency/)
* Clone the repo: `git clone https://github.com/BlackrockDigital/startbootstrap-agency.git`
* Fork the repo

## Developing Using Source Files

To use the source files, you will need to have npm installed globally along with Gulp.js. To start:
* Run `npm install` in the root directory
* Run `gulp dev` and edit the files as needed

If you need to update the plugins included with this template, simply run the following tasks:
* First run `npm update` to update the dependencies
* Then run `gulp copy` to copy the new versions to their proper destinations

## Bugs and Issues

Have a bug or an issue with this template? [Open a new issue](https://github.com/BlackrockDigital/startbootstrap-agency/issues) here on GitHub or leave a comment on the [template overview page at Start Bootstrap](http://startbootstrap.com/template-overviews/agency/).

## Creator

Start Bootstrap was created by and is maintained by **[David Miller](http://davidmiller.io/)**, Owner of [Blackrock Digital](http://blackrockdigital.io/).

* https://twitter.com/davidmillerskt
* https://github.com/davidtmiller

Start Bootstrap is based on the [Bootstrap](http://getbootstrap.com/) framework created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thorton](https://twitter.com/fat).

## Copyright and License

Copyright 2013-2017 Blackrock Digital LLC. Code released under the [MIT](https://github.com/BlackrockDigital/startbootstrap-agency/blob/gh-pages/LICENSE) license.# Images

This directory contains notes on Docker Images and how they relate to the rest of Docker.

# Containers

This directory contains information about Linux Containers and how they relate
to the rest of Docker.
# Docker Virtual Networks

This directory contains notes on Docker's networking capabilities.

