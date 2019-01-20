# Cloud Workshop

## Requirements

Virtualbox and Vagrant must be installed before setting up the workshop.

On OS X this can be done easily with `brew`:

```
$ brew install caskroom/cask/brew-cask
$ brew cask install virtualbox
$ brew cask install vagrant
```

Accounts on [Docker Hub](https://registry.hub.docker.com) and [GitHub](https://github.com) is also necessary.


## Setup

To setup your environment for the workshop, fork this project and clone it locally. Then run
`vagrant up` in the root of the project. This downloads quite a lot of stuff so is smart to
do on a fast network.

To make it easier to access the web apps inside the VM, add the following to your `etc/hosts`:

```
192.168.12.34    localdocker
```

With this you can just open `http://localdocker:<port>`.


## Nice to know

To get into the virtual machine, run `vagrant ssh`. The local project is mounted onto `/vagrant` inside the
VM, so just go there before running any commands (`cd /vagrant`).

To stop the virtual machine started with `vagrant up`, you can do `vagrant suspend`. Then to start it again,
you can do `vagrant resume`. When you are finished with the workshop, you can use `vagrant destroy` to remove
all traces of the virtual machine.


## Tasks

* Run only the backend with in-memory db
    * `docker run ...`
        * check the available images with `docker images` to find the backend image
        * the container should be put in the background
        * the container's exposed port (see `Dockerfile`) should be mapped onto port 9000 on the VM
    * access the web app to see that it works (`curl localdocker:9000/person`)
    * list all running docker containers
    * view the docker log for backend
    * get into the running backend container
    * kill the backend docker container
* Run frontend/backend with in-memory db
    * `docker-compose ...`
        * put them in the background
    * view the logs of both containers
    * stop both containers
* Run frontend/backend with PostgreSQL
    * `docker-compose -f docker-compose.postgres.yml ...`
    * try to scale backend
    * look at the logs to see if the second backend is used
    * what happens and why?
* Run frontend/backend with Consul/PostgreSQL
    * start helper containers (`/vagrant/helpers/start_helper_containers.sh`)
    * `docker-compose -f docker-compose.consul.yml ...`
    * try to scale backend
    * look at the logs to see if the second backend is used
    * what happens and why?
* Work with a docker server in the cloud (Digital Ocean)
    * first load the `helpers/env_for_digital_ocean.sh` into current shell
    * `docker-machine ...`
        * use the Digital Ocean API key you got in mail
    * create a new machine
    * list current machines
    * run docker commands against the new machine
    * start up frontend/backend with PostgreSQL on this machine using `docker-compose`
    * ssh to the machine and run docker
    * destroy this machine
