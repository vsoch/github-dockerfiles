For Spring Boot Learning

Pre: something about Maven

Spring Boot Project

### Add a new service and redeploy
* Add new service `visualizer` to docker-compose.yml
* Make sure the shell is configured to talk to myvm1
1. On MAC or Linux
`eval $(docker-machine env myvm1)`
1. On Windows
`& "C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe" env myvm1 | Invoke-Expression`
* Rerun command on manager
`docker stack deploy -c docker-compose.yml getstartedlab`
* Take a look at the visualizer. Get the IP address of one of your nodes by `running docker-machine ls` and open browser

### Persist the data
* Add a `redis` service to docker-compose.yml
* Create a ./data directory on the manager:
`docker-machine ssh myvm1 "mkdir ./data"`
<br/>
* Make sure the shell is configured to talk to myvm1
* Run docker stack deploy one more time
`docker stack deploy -c docker-compose.yml getstartedlab`
<br/>
* Verify that the three services are running as expected
`docker service ls`
<br/>
* Check the web page at one of your nodes### Set up the swarm
#### Create a cluster
* Create VMs
`docker-machine create --driver virtualbox myvm1`
`docker-machine create --driver virtualbox myvm2`
<br/>
* List the VMs and get their IP addresses
`docker-machine ls`
<br/>
* Initialize the swarm and add nodes
`docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 ip>"`
`docker-machine ssh myvm2 "docker swarm join --token <token> <ip>:2377"`
<br/>
* Run docker node ls on the manager to view the nodes in this swarm:
`docker-machine ssh myvm1 "docker node ls"`

### Deploy the app to the swarm cluster
#### Configure a docker-machine shell to the swarm manager
* Get docker machine shell environment on MAC or Linux
```
$ docker-machine env myvm1
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/Users/sam/.docker/machine/machines/myvm1"
export DOCKER_MACHINE_NAME="myvm1"
# Run this command to configure your shell:
# eval $(docker-machine env myvm1)
```
`eval $(docker-machine env myvm1)`

* Verify that myvm1 is the active machine
`docker-machine ls`

#### Deploy the app to swarm manager
* Run the command on myvm1
`docker stack deploy -c docker-compose.yml getstartedlab`
<br/>
* List the services
`docker stack ps getstartedlab`
#### Accessing the cluster
* Run get VMs’ IP addresses 
`docker-machine ls`
* Visit either of them on a browser. You’ll see five possible container IDs all cycling by randomly, demonstrating the load-balancing.

#### Iterating and scaling your app
1. Scale the app by changing the `docker-compose.yml` file.
1. Change the app behavior by editing code, then rebuild, and push the new image. 
1. Join any machine to the swarm

In either case, simply run `docker stack deploy` again to deploy these changes.

#### Cleanup and reboot
* Tear down the stack
`docker stack rm gtestartedlab`
<br/>
* Unsetting docker-machine shell variable settings
`eval $(docker-machine env -u)`
<br/>
* Restarting Docker machines. To restart a machine that’s stopped, run:
`docker-machine start <machine-name>`### Build the app
    docker build -t friendlyhello .
### Run the app
* Run in frontend
`docker run -p 4000:80 friendlyhello`
* Run in backround
`docker run -d -p 4000:80 friendlyhello`
* End the process
`docker container stop <Container ID>`
### Share the image
* Login in with Docker ID
`docker  login`
* Tag the image
`docker tag image_name username/repository:tag`
* Publish the image
`docker push username/repository:tag`
* Pull and run the image from the remote repository
`docker run -p 4000:80 username/repository:tag`
### Run your new load-balanced app
* Init swarm manager
`docker swarm init`
<br/>
* Run the app
`docker stack deploy -c docker-compose.yml getstartedlab`
<br/>
* Get the service ID
`docker service ls`
<br/>
* List tasks for the service
`docker service ps getstartedlab_web`
<br/>
* List all containers on the system
`docker container ls -q`
### Scale the app
* Change `replicas` value in docker-compose.yml, and run command:
`docker stack deploy -c docker-compose.yml getstartedlab`
### Take down the app and the swarm
* Take down the app
`docker stack rm getstartedlab`
<br/>
* Take down the swarm
`docker swarn leave --force`
EFK Stack Shell

Reference: See the WIKI
