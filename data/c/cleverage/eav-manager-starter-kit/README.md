CleverAge/EAVManager Starter Kit
================================

The main documentation is located here: [CleverAge/EAVManager](https://github.com/cleverage/eav-manager)

## Installation

You will need make, docker and docker-compose installed on your machine.

````bash
$ make install && make shell
````

If this setup conflicts with open ports on your system, simply edit your ````docker/.env```` file.

From there you will be in a shell inside you main container

### Setting up the database

````bash
$ sf doctrine:schema:create
````

### Creating your admin user

````bash
$ sf eavmanager:create-user -a your-email@my-domain.com -pMyPassw0rd
````

### Accessing the application

The Nginx server will answer to any domain so you can either go to [http://127.0.0.1](http://127.0.0.1) or to any
domain matching this IP.

All the emails sent by the application are caught by mailcatcher: [http://127.0.0.1:1080](http://127.0.0.1:1080)

### Managing docker containers

Starting your containers

````bash
$ make start
````

Stoping your containers

````bash
$ make stop
````


## Editing your model

All the configuration is in ````app/config````.

