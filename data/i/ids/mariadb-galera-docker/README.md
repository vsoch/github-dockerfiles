MariaDB Galera Docker
=====================

This is a containerized version of a MariaDB Galera cluster.  It makes use of shim scripts to manage and control the cluster startup and syncronization through declarative container infrastructure and orchestration.

> The underlying mariadb-galera-docker container is based on a fork of [mariadb-galera-swarm](https://github.com/colinmollenhour/mariadb-galera-swarm).  If you see anything particularly clever in this implementation, chances are good it came from __colinmollenhour__.  I was quite impressed with the implementation, and although it was origiinally limited by the underlying Swarm persistent storage model, it was easily ported to a more explicit 3 and 5 node configuration that works quite nicely in all of the major orchestrators and the more advanced persistent storage capabilities of k8s.

It currently works in both Docker Swarm and DC/OS using the same Docker images.  The more advanced implementation, and the one likely to be the most maintained, is the k8s variant that includes an automated backup and restore workflow.

See the [kubernetes](./k8s) README for instructions on deploying to Kubernetes.

See the [dcos](./dcos) README for instructions on deploying to DC/OS.

See the [docker](./swarm) README for instructions on deploying to Docker Swarm.

