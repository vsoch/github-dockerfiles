# etcd-version-monitor

This is a tool for exporting metrics related to etcd version, like etcd
server's binary version, cluster version, and counts of different kinds of
gRPC calls (which is a characteristic of v3), etc. These metrics are in
prometheus format and can be scraped by a prometheus server.
The metrics are exposed at the http://localhost:9101/metrics endpoint.

**RUNNING THE TOOL**

To run this tool as a docker container:
- make build
- docker run --net=host -i -t gcr.io/google_containers/etcd-version-monitor:test /etcd-version-monitor --logtostderr

To run this as a pod on the kubernetes cluster:
- Place the 'etcd-version-monitor.yaml' in the manifests directory of
  kubelet on the master machine.

*Note*: This tool has to run on the same machine as etcd, as communication
with etcd is over localhost.

**VERIFYING THE TOOL**

- Goto [http://localhost:9101/metrics](http://localhost:9101/metrics) in order to view the exported metrics.
- The metrics prefixed with "etcd_" are the ones of interest to us.
### etcd

This is a small etcd image used in Kubernetes setups where `etcd` is deployed as a docker image.

For `amd64`, official `etcd` and `etcdctl` binaries are downloaded from Github to maintain official support.
For other architectures, `etcd` is cross-compiled from source. Arch-specific `busybox` images serve as base images.

#### How to release

First, run the migration and rollback tests.

```console
$ make build test
```

Next, build and push the docker images for all supported architectures.

```console
# Build for linux/amd64 (default)
$ make push ARCH=amd64
# ---> gcr.io/google_containers/etcd-amd64:TAG
# ---> gcr.io/google_containers/etcd:TAG

$ make push ARCH=arm
# ---> gcr.io/google_containers/etcd-arm:TAG

$ make push ARCH=arm64
# ---> gcr.io/google_containers/etcd-arm64:TAG

$ make push ARCH=ppc64le
# ---> gcr.io/google_containers/etcd-ppc64le:TAG

$ make push ARCH=s390x
# ---> gcr.io/google_containers/etcd-s390x:TAG
```

If you don't want to push the images, run `make` or `make build` instead


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/images/etcd/README.md?pixel)]()
# Rollback workflow

Build it in this directory.
Make sure you have etcd dependency ready. Last time we use etcd v3.0.7.
```
$ go build .
```


Run it:
```
$ ./rollback2 --data-dir $ETCD_DATA_DIR --ttl 1h
```

This will rollback KV pairs from v3 into v2.
If a key was attached to a lease before, it will be created with given TTL (default to 1h).

On success, it will print at the end:
```
Finished successfully
```

Repeat this on all etcd members.

You can do simple check on keys (if any exists):
```
etcdctl ls /
```

Important Note
------

This tool isn't recommended to use if any problem comes up in etcd3 backend.
Please report bugs and we will fix it soon.

If it's still preferred to run this tool, please backup all your data beforehand.
This tool will also back up datadir to same path with ".rollback.backup" suffix.

Caveats:
- The tool doesn't preserve versions of keys.
- If any v2 data exists before rollback, they will be wiped out.
- v3 data only exists in the backup after successful rollback.


[![Analytics](https://kubernetes-site.appspot.com/UA-36037335-10/GitHub/cluster/images/etcd/rollback/README.md?pixel)]()