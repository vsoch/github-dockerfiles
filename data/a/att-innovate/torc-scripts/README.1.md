Examples for running Mesos master and slave in containers on the switch.
Btw, we run Mesos slave bare-metal on the compute nodes.

$ docker run -d --name mesos-master --net=host --memory=1g -e MY_IP=$MY_IP mesos master

$ docker run -d  --name mesos-slave --net=host  -e MY_IP=$MY_IP \
        -e MACHINE_NAME="wedge" -e MACHINE_TYPE="master" -e MACHINE_FUNCTION="controller" \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v /sys/fs/cgroup/:/sys/fs/cgroup/ \
        mesos slave --master=zk://$MY_IP:2181/mesos
