# etcd-version-monitor

This is a tool for exporting etcd metrics and supplementing them with etcd
server binary version and cluster version. These metrics are in
prometheus format and can be scraped by a prometheus server.
The metrics are exposed at the http://localhost:9101/metrics endpoint.

For etcd 3.1+, the
[go-grpc-prometheus](https://github.com/grpc-ecosystem/go-grpc-prometheus)
metrics format, which backward incompatibly replaces the 3.0 legacy grpc metric
format, is exposed in both the 3.1 format and in the 3.0. This preserves
backward compatibility.

For etcd 3.1+, the `--metrics=extensive` must be set on etcd for grpc request
latency metrics (`etcd_grpc_unary_requests_duration_seconds`) to be exposed.

**RUNNING THE TOOL**

To run this tool as a docker container:
- make build
- docker run --net=host -i -t k8s.gcr.io/etcd-version-monitor:test /etcd-version-monitor --logtostderr

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

### Upgrading and Downgrading

To upgrade to a newer etcd version, or to downgrade to the previous minor
version, always run `/usr/local/bin/migrate-if-needed.sh` before starting the
etcd server.

`migrate-if-needed.sh` writes a `version.txt` file to track the "current" version
of etcd that was used to persist data to disk. A "target" version may also be provided
by the `TARGET_STORAGE` (e.g. "etcd3") and `TARGET_VERSION` (e.g. "3.2.11" )
environment variables. If the persisted version differs from the target version,
`migrate-if-needed.sh` will migrate the data from the current to the target
version.

Upgrades to any target version are supported. The data will be automatically upgraded
in steps to each minor version until the target version is reached.

Downgrades to the previous minor version of the 3.x series and from 3.0 to 2.3.7 are supported.

#### How to release

First, run the migration and rollback tests.

```console
$ make build test
```

Next, build and push the docker images for all supported architectures.

```console
# Build for linux/amd64 (default)
$ make push ARCH=amd64
# ---> staging-k8s.gcr.io/etcd-amd64:TAG
# ---> staging-k8s.gcr.io/etcd:TAG

$ make push ARCH=arm
# ---> staging-k8s.gcr.io/etcd-arm:TAG

$ make push ARCH=arm64
# ---> staging-k8s.gcr.io/etcd-arm64:TAG

$ make push ARCH=ppc64le
# ---> staging-k8s.gcr.io/etcd-ppc64le:TAG

$ make push ARCH=s390x
# ---> staging-k8s.gcr.io/etcd-s390x:TAG
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