# Running Radar with docker

## The explaining

So you want to run quickly a radar server inside docker, and you don't want to think 
about connecting containers, or launching new virtual machines. You just want it to work. 

This example runs radar client and server side. Client on port 80 and server in port 8000. As of now there aren't that many examples to play with, but I promise I'll get some. 

## The preparing

* Install docker, docker-machine and docker-compose.
* https://docs.docker.com/machine/
* https://docs.docker.com/compose/

As of now, you can install the requirements by doing this, if you are on a mac:

    brew install docker docker-composer docker-machine

## The doing

### Create one VM to run radar

Let's keep everything separated

    docker-machine create --driver virtualbox radar-example

### Inspect current VMs

    docker-machine ls

### Let docker know which VM is the current one
    
    eval "$(docker-machine env radar-example)"
    docker ps

It should be empty, since it's brand new. 

### Building Radar

Now, let's build our radar container. This step will take care of building client and server containers. 

    docker-compose build

### Lastly, run radar

Run detached from the console

    docker-compose up -d

You can check the status of the containers (server and redis) by executing:

    docker-compose ps

## The enjoying


### The Server Side of the story

Open a browser window and check if your radar container is running. 

    open http://"$(docker-machine ip radar)":8000/ping

You should see something like:
  
    {"pong":"Radar running at 5a97e3cd4e06"}


### The Client Side of the story

Open a browser window and check if radar client works and can connect to the server.

    open http://"$(docker-machine ip radar)"

Remember to open the JS console on your browser. There's no html UI. 


## Copyright and License

Copyright 2015, Zendesk Inc. Licensed under the Apache License Version 2.0, http://www.apache.org/licenses/LICENSE-2.0
