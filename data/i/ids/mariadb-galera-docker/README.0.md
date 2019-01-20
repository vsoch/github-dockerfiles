# MariaDb Galera Cluster

This Docker container is based on the official Docker `mariadb:10.1` image and is designed to be
compatible with auto-scheduling systems, specifically Docker Swarm Mode (1.12+) and Kontena.
However, it could also work with manual scheduling (`docker run`) by specifying the correct
environment variables or possibly other scheduling systems that use similar conventions.

It takes as a command one of the following:

 - "seed" - Used only to initialize a new cluster and after initialization and other nodes are joined
   the "seed" container should be stopped and replaced with a "node" container using the same volume.
 - "node" - Join an existing cluster. Takes as a second argument a comma-separated list of IPs or
   hostnames to resolve which are used to build the `--wsrep_cluster_address` option for joining a cluster.
 - "no-galera" - Start server with Galera disabled. Useful for maintenance tasks like performing mysql_upgrade
   and resetting root credentials.
 - "sleep" - Start the container but not the server. Runs "sleep infinity". Useful just to get volumes
   initialized or if you want to `docker exec` without the server running.

By using DNS resolution to discover other nodes they don't have to be specified explicitly. This should works
with any system with DNS-based service discovery such as Kontena, Docker Swarm Mode, Consul, etc.

### Examples

#### Docker 1.12 Swarm Mode (cli)

```
 $ docker service create --name galera-seed --replicas 1 -e XTRABACKUP_PASSWORD=<pass> \
     colinmollenhour/mariadb-galera-swarm seed
 $ docker service create --name galera --replicas 2 -e XTRABACKUP_PASSWORD=<pass> \
     colinmollenhour/mariadb-galera-swarm node tasks.galera-seed,tasks.galera
 $ docker service rm galera-seed
 $ docker service scale galera=3
```

#### [Docker 1.13 Swarm Mode (stack)](https://github.com/colinmollenhour/mariadb-galera-swarm/blob/master/examples/swarm)

#### [Kontena](https://github.com/colinmollenhour/mariadb-galera-swarm/blob/master/examples/kontena)

Please submit more examples for Kubernetes, Mesos, etc. and also improvements for existing examples!

### Environment Variables

 - `XTRABACKUP_PASSWORD` (required unless `XTRABACKUP_PASSWORD_FILE` is provided)
 - `SYSTEM_PASSWORD` (optional - defaults to hash of `XTRABACKUP_PASSWORD`)
 - `CLUSTER_NAME` (optional)
 - `NODE_ADDRESS` (optional - defaults to ethwe, then eth0)
 - `LISTEN_WHEN_HEALTHY` (optional) - Specify a port number to open a healthcheck socket on once the cluster
   has reached a healthy state. Useful with Kontena's `wait_for_port` feature.
 - `HEALTHY_WHILE_BOOTING` (optional) - If '1' then the HEALTHCHECK script will report healthy
   during the boot phase (waiting for DNS to resolve and recovering wsrep position).

Additional variables for "seed":

 - `MYSQL_ROOT_PASSWORD` (optional)
 - `MYSQL_DATABASE` (optional)
 - `MYSQL_USER` (optional)
 - `MYSQL_PASSWORD` (optional)

Additional variables for "node":

 - `GCOMM_MINIMUM` (optional - defaults to 2)

#### Providing secrets through files

It's also possible to configure the sensitive variables using files, a method used by [Docker Swarm](https://docs.docker.com/engine/swarm/secrets/),
Rancher and perhaps others. The paths to the secret files defaults to `/run/secrets/{lower_case_variable_name}`
but can be specified explicitly as well using the following environment variables:

 - `XTRABACKUP_PASSWORD_FILE`
 - `SYSTEM_PASSWORD_FILE`
 - `MYSQL_ROOT_PASSWORD_FILE`
 - `MYSQL_PASSWORD_FILE`
 - `MYSQL_DATABASE_FILE`

### Flag Files

In order to accomodate controlling the bootstrapping phase without having to change the CMD which is sometimes
hard to do with automated schedulers you can touch the following files to change the bootstrapping behavior
before starting the container. All files are expected to be in the /var/lib/mysql directory which you should be
mounting as a container volume.

 - /var/lib/mysql/new-cluster - Cause a 'node' container to behave as a 'seed' container on it's first run. This
   may also be used for recovery in case a Primary Component cannot be formed or for bootstrapping a fresh cluster
   in place of using the 'seed' container. If the file has any contents they will be used as the `MYSQL_ROOT_PASSWORD`.
 - /var/lib/mysql/hold-start - Cause a 'node' container to wait until this file is deleted before trying to boot.
   This could be used in the absence of a scheduler with an easy fine-grained scheduling control.
 - /var/lib/mysql/force-cluster-bootstrapping - Force the creation of MySQL users again ('seed' or 'node' command).
 - /var/lib/mysql/skip-cluster-bootstrapping - Prevent the creation of MySQL users. This file will be created and
   **should not** be deleted under normal circumstances.

### Health Checks

By default there are two HTTP-based healthcheck servers running in the background.

 - Port 8080 only reports healthy when ready to serve clients. (synced)
 - Port 8081 reports healthy as long as the server is synced or donor/desynced state. This one is used to help
  other nodes determine cluster state before launching the server and also by the Dockerfile HEALTHCHECK command.

The default `HEALTHCHECK` command also returns healthy status if `/var/lib/mysql/sst_in_progress` is present to avoid
a node being killed during an SST. Otherwise it uses the second health check (port 8081) to return healthy only if it
is 'synced' to prevent the node from being killed if it is a donor for a long period of time. How you want the
healthcheck command to behave will vary on your uses for the healthcheck so you may need to override it depending on
the behavior you desire. Regardless, both healthcheck servers will be started and will use negligible resources unless
they are actually being pinged.

Additionally, if a `LISTEN_WHEN_HEALTHY` port number is specified then the container will start a loop checking it's
own port 8080 health check described above until it reports healthy at which point it will open a new socket on this
port which just forwards to port 8080. This can be used with Kontena's `wait_for_port` feature to accomodate the
rolling update mechanism.

### More Info

 - Tries to handle as many recovery scenarios as possible including full cluster ungraceful shutdown by
   using --wsrep-recovery and inter-node communication to discover the optimal node for bootstrapping
   a new cluster when the old one cannot be recovered.
 - If you need to perform manual recovery of a previously healthy cluster you can use "node" mode
   but touch a file at `/var/lib/mysql/wsrep-new-cluster` to force a node to bootstrap a new cluster
   and bypass the automatic recovery steps.
 - XtraBackup is used for state transfer and MariaDb now supports `pc.recovery` so the primary component should
   automatically be recovered in the case of all nodes being gracefully shutdown. It is important tha all nodes are
   started together so that they can communicate status with each-other.
 - A go server runs within the cluster exposing an http service for intelligent health checking.
    - Port 8080 is used by the Docker 1.12 HEALTHCHECK feature and also can be used by any other health checking
      node in the network such as HAProxy or Consul to determine readable/writeable nodes.
    - Port 8081 is used to detemine cluster status
 - If your container network uses something other than `ethwe*` or `eth0` then you need to specify `NODE_ADDRESS`
   as either the name of the interface to listen on or a grep pattern to match one of the container's IP addresses.
   E.g.: `NODE_ADDRESS='^10.0.1.*'`
 - When using DNS for node address discovery the container entrypoint script will wait indefinitely for
   `GCOMM_MINIMUM` IP addresses to resolve before trying to start `mysqld` in case some containers are starting
   slower than others to increase the chance of a healthy recovery. Scenarios where not enough IPs would resolve
   might include:
    - Some nodes may finish pulling container images from remote repositories sooner than others
    - Schedulers may not be launching nodes quickly enough
    - Service discovery systems may be slow to propagate updates via DNS
 - If the file `/usr/local/lib/startup.sh` exists it will be sourced in the start.sh script.
 - If you need to promote a running node to be a new "Primary Component" you can run the following command to do so:
       $ docker exec -i <container> mysql -p /primary-component.sql
 - You can monitor cluster state changes more clearly by setting `wsrep_notify_cmd` to `/usr/local/bin/notify.sh`
   which will output the updates to the Docker logs/console.

### Credit

 - Forked from ["jakolehm/docker-galera-mariadb-10.0"](https://github.com/jakolehm/docker-galera-mariadb-10.0)
   - Forked from ["sttts/docker-galera-mariadb-10.0"](https://github.com/sttts/docker-galera-mariadb-10.0)
 - galera-healthcheck go binary from ["sttts/galera-healthcheck"](https://github.com/sttts/galera-healthcheck)

### Changes

 - Rebase on official Docker mariadb:10.1 image and fix for new 10.1 changes.
 - Add support for Docker Swarm Mode by falling back to eth0 if no ethwe adapter found.
 - Support any adapter/IP by specifying `NODE_ADDRESS=<interface|pattern>`.
 - Fix running mysqld as root using `gosu mysql mysqld.sh`.
 - Add support for HEALTHCHECK for Docker 1.12.
 - Delay starting mysqld until at least GCOMM_MINIMUM total nodes are up when using DNS resolution for node list.
 - Bundle galera-healthcheck binary.
 - Completely rewrite mysqld.sh startup script for proper cluster bootstrapping and recovery.
 - Add sourcing of /usr/local/lib/startup.sh for easier entrypoint extension.
 - Add 'sleep', 'no-galera' and 'bash' modes for easier maintenance/debugging.
 - Various other minor improvements.
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
