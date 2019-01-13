## $MONGO_PORT_27017_TCP_ADDR and $MONGO_PORT_27017_TCP_PORT

```
sudo docker.io run -d --name mongodb robinvdvleuten/mongo
sudo docker.io run -t -i --link mongodb:mongo ubuntu:latest env
HOME=/
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=7aea19ddf0ea
TERM=xterm
MONGO_PORT=tcp://172.17.0.2:27017
MONGO_PORT_27017_TCP=tcp://172.17.0.2:27017
MONGO_PORT_27017_TCP_ADDR=172.17.0.2
MONGO_PORT_27017_TCP_PORT=27017
MONGO_PORT_27017_TCP_PROTO=tcp
MONGO_NAME=/condescending_bell/mongo
// stop all container
```

build image

[Remove Untagged Images From Docker — Jim Hoskins](http://jimhoskins.com/2013/07/27/remove-untagged-docker-images.html)

```
$ sudo docker.io rm $(sudo docker.io ps -a -q)
$ git clone https://github.com/y12studio/y12io
$ cd y12io/projects/lbho-mongo2
$ sudo docker.io build -t="test/lbmo2" .
$ sudo docker.io run -d -p 27017:27017 --name mongodb robinvdvleuten/mongo
// add mongo database/user/password
$ mongo devDB mongo_adduser.js
$ sudo docker.io run -d -p 80:3000 --link mongodb:mongo test/lbmo2

```
