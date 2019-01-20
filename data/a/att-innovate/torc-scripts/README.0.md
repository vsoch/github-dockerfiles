# To run it replace $TORC-IP with the public IP of your wedge.

Running it with Snaproute as network agent
$ docker run -d --etcd http://$TORC-IP:2379/v2/keys/ --basedir torc --agenttype snaproute --agenturl $TORC-IP:8080 --service http://$TORC-IP:3000/services/running --machine http://$TORC-IP:3000/nodes

Running it with FBOSS as network agent
$ docker run -d --etcd http://$TORC-IP:2379/v2/keys/ --basedir torc --agenttype fboss --agenturl $TORC-IP::5909 --service http://$TORC-IP:3000/services/running --machine http://$TORC-IP:3000/nodes
Please copy the statesync binary into this folder before building statesync container
