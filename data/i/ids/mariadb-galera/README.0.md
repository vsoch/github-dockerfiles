Docker Swarm
============

This is an example only and may not be production-quality. Please submit improvements!

```
$ mkdir -p .secrets
$ openssl rand -base64 32 > .secrets/xtrabackup_password
$ openssl rand -base64 32 > .secrets/mysql_password
$ openssl rand -base64 32 > .secrets/mysql_root_password
$ docker stack deploy -c docker-compose.yml galera
$ docker service ls
(wait for `galera_seed` to be healthy)
$ docker service scale galera_node=2
(wait for both `galera_node` instances to be healthy)
$ docker service scale galera_seed=0
$ docker service scale galera_node=3
```

Note, currently I do not know of a good way to retrieve the DNS name to lookup other IPs so the
`docker-compose.yml` file has `galera_seed,galera_node` hard-coded which would not work unless
`galera` is used as the name of the stack for the `docker stack deploy` command.

For similar reasons, the example `docker-compose.yml` file contains a user network called `galera-network`. The name of this network is not critical, but it needs to be first in the list of user defined overlay networks in `docker-compose.yml`, so that Docker allocates it the subnet 10.0.0.0/24. This is required so that the `NODE_ADDRESS=^10.0.0.*` pattern matching works when the seed and node containers are started.

If you want to use a different subnet address for this user network, then it should be created first and the network type in `docker-compose.yml` should be changed to `external`. The `NODE_ADDRESS` pattern should also be updated to this new address. For example, if the new subnet address is `10.0.9.0` then change it to `NODE_ADDRESS=^10.0.9.*`.

For more information on creating overlay networks with a specific subnet address, see https://docs.docker.com/engine/swarm/networking/#create-an-overlay-network-in-a-swarm
Use flag files to manage the bootstrapping process. Pick one node (e.g. "db1") to be the seed and put the other nodes
(e.g. "db2" and "db3" on "hold" until you are ready to have them join.


    db1 $ docker volume create mysql-data
    db1 $ touch /var/lib/docker/volumes/mysql-data/_data/new-cluster
    db1 $ chmod 666 /var/lib/docker/volumes/mysql-data/_data/new-cluster  #IMPORTANT!
    db2 $ docker volume create mysql-data
    db2 $ touch /var/lib/docker/volumes/mysql-data/_data/hold-start
    db3 $ docker volume create mysql-data
    db3 $ touch /var/lib/docker/volumes/mysql-data/_data/hold-start
    $ kontena stack install kontena.yml
    $ # Check logs for generated root password
    $ # Import database dump on db1
    db2 $ rm /var/lib/docker/volumes/mysql-data/_data/hold-start
    $ # Wait for db2 to become Synced
    db3 $ rm /var/lib/docker/volumes/mysql-data/_data/hold-start
    $ # All done!
