# Prometheus Operator
[![Build Status](https://travis-ci.org/coreos/prometheus-operator.svg?branch=master)](https://travis-ci.org/coreos/prometheus-operator)
[![Go Report Card](https://goreportcard.com/badge/coreos/prometheus-operator "Go Report Card")](https://goreportcard.com/report/coreos/prometheus-operator)

**Project status: *beta*** Not all planned features are completed. The API, spec, status and other user facing objects may change, but in a backward compatible way.

The Prometheus Operator for Kubernetes provides easy monitoring definitions for Kubernetes
services and deployment and management of Prometheus instances.

Once installed, the Prometheus Operator provides the following features:

* **Create/Destroy**: Easily launch a Prometheus instance for your Kubernetes namespace,
  a specific application or team easily using the Operator.

* **Simple Configuration**: Configure the fundamentals of Prometheus like versions, persistence, 
  retention policies, and replicas from a native Kubernetes resource.

* **Target Services via Labels**: Automatically generate monitoring target configurations based
  on familiar Kubernetes label queries; no need to learn a Prometheus specific configuration language.

For an introduction to the Prometheus Operator, see the initial [blog
post](https://coreos.com/blog/the-prometheus-operator.html).

## Prometheus Operator vs. kube-prometheus

The Prometheus Operator makes the Prometheus configuration Kubernetes native
and manages and operates Prometheus and Alertmanager clusters. It is a piece of
the puzzle regarding full end-to-end monitoring.

[kube-prometheus](contrib/kube-prometheus) combines the Prometheus Operator
with a collection of manifests to help getting started with monitoring
Kubernetes itself and applications running on top of it.

## Prerequisites

Version `>=0.18.0` of the Prometheus Operator requires a Kubernetes
cluster of version `>=1.8.0`. If you are just starting out with the
Prometheus Operator, it is highly recommended to use the latest version.

If you have an older version of Kubernetes and the Prometheus Operator running,
we recommend upgrading Kubernetes first and then the Prometheus Operator.

## CustomResourceDefinitions

The Operator acts on the following [custom resource definitions (CRDs)](https://kubernetes.io/docs/tasks/access-kubernetes-api/extend-api-custom-resource-definitions/):

* **`Prometheus`**, which defines a desired Prometheus deployment.
  The Operator ensures at all times that a deployment matching the resource definition is running.

* **`ServiceMonitor`**, which declaratively specifies how groups
  of services should be monitored. The Operator automatically generates Prometheus scrape configuration
  based on the definition.

* **`PrometheusRule`**, which defines a desired Prometheus rule file, which can
  be loaded by a Prometheus instance containing Prometheus alerting and
  recording rules.

* **`Alertmanager`**, which defines a desired Alertmanager deployment.
  The Operator ensures at all times that a deployment matching the resource definition is running.

To learn more about the CRDs introduced by the Prometheus Operator have a look
at the [design doc](Documentation/design.md).

## Installation

Install the Operator inside a cluster by running the following command:

```sh
kubectl apply -f bundle.yaml
```

> Note: make sure to adapt the namespace in the ClusterRoleBinding if deploying in another namespace than the default namespace.

To run the Operator outside of a cluster:

```sh
make
hack/run-external.sh <kubectl cluster name>
```

## Removal

To remove the operator and Prometheus, first delete any custom resources you created in each namespace. The
operator will automatically shut down and remove Prometheus and Alertmanager pods, and associated configmaps.

```sh
for n in $(kubectl get namespaces -o jsonpath={..metadata.name}); do
  kubectl delete --all --namespace=$n prometheus,servicemonitor,alertmanager
done
```

After a couple of minutes you can go ahead and remove the operator itself.

```sh
kubectl delete -f bundle.yaml
```

The operator automatically creates services in each namespace where you created a Prometheus or Alertmanager resources,
and defines three custom resource definitions. You can clean these up now.

```sh
for n in $(kubectl get namespaces -o jsonpath={..metadata.name}); do
  kubectl delete --ignore-not-found --namespace=$n service prometheus-operated alertmanager-operated
done

kubectl delete --ignore-not-found customresourcedefinitions \
  prometheuses.monitoring.coreos.com \
  servicemonitors.monitoring.coreos.com \
  alertmanagers.monitoring.coreos.com
```

## Development

### Prerequisites

- golang environment
- docker (used for creating container images, etc.)
- minikube (optional)

### Testing

> Ensure that you're running tests in the following path:
> `$GOPATH/src/github.com/coreos/prometheus-operator` as tests expect paths to
> match. If you're working from a fork, just add the forked repo as a remote and
> pull against your local coreos checkout before running tests.

#### Running *unit tests*:

`make test-unit`

#### Running *end-to-end* tests on local minikube cluster:

1. `minikube start --kubernetes-version=v1.10.0 --memory=4096
    --extra-config=apiserver.Authorization.Mode=RBAC`
2. `eval $(minikube docker-env) && make image` - build Prometheus Operator
    docker image on minikube's docker
3. `make test-e2e`

## Contributing

Many files (documentation, manifests, ...) in this repository are
auto-generated. E.g. `bundle.yaml` originates from the _Jsonnet_ files in
`/jsonnet/prometheus-operator`. Before proposing a pull request:

1. Commit your changes.
2. Run `make generate-in-docker`.
3. Commit the generated changes.


## Security

If you find a security vulnerability related to the Prometheus Operator, please
do not report it by opening a GitHub issue, but instead please send an e-mail to
the maintainers of the project found in the [OWNERS](OWNERS) file.
# E2E Testing

End-to-end (e2e) testing is automated testing for real user scenarios.

## Build and run test

Prerequisites:
- a running k8s cluster and kube config. We will need to pass kube config as arguments.
- Have kubeconfig file ready.
- Have prometheus operator image ready.

e2e tests are written as Go test. All go test techniques apply, e.g. picking
what to run, timeout length. Let's say I want to run all tests in "test/e2e/":

```
$ go test -v ./test/e2e/ --kubeconfig "$HOME/.kube/config" --operator-image=quay.io/coreos/prometheus-operator
```
# kube-prometheus

> Note that everything in the `contrib/kube-prometheus/` directory is experimental and may change significantly at any time.

This repository collects Kubernetes manifests, [Grafana](http://grafana.com/) dashboards, and [Prometheus rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with [Prometheus](https://prometheus.io/) using the Prometheus Operator.

The content of this project is written in [jsonnet](http://jsonnet.org/). This project could both be described as a package as well as a library.

Components included in this package:

* The [Prometheus Operator](https://github.com/coreos/prometheus-operator)
* Highly available [Prometheus](https://prometheus.io/)
* Highly available [Alertmanager](https://github.com/prometheus/alertmanager)
* [Prometheus node-exporter](https://github.com/prometheus/node_exporter)
* [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)
* [Grafana](https://grafana.com/)

This stack is meant for cluster monitoring, so it is pre-configured to collect metrics from all Kubernetes components. In addition to that it delivers a default set of dashboards and alerting rules. Many of the useful dashboards and alerts come from the [kubernetes-mixin project](https://github.com/kubernetes-monitoring/kubernetes-mixin), similar to this project it provides composable jsonnet as a library for users to customize to their needs.

## Table of contents

* [Prerequisites](#prerequisites)
    * [minikube](#minikube)
* [Quickstart](#quickstart)
* [Customizing Kube-Prometheus](#customizing-kube-prometheus)
    * [Installing](#installing)
    * [Compiling](#compiling)
    * [Containerized Installing and Compiling](#containerized-installing-and-compiling)
* [Configuration](#configuration)
* [Customization Examples](#customization-examples)
    * [Cluster Creation Tools](#cluster-creation-tools)
    * [NodePorts](#nodeports)
    * [Prometheus Object Name](#prometheus-object-name)
    * [node-exporter DaemonSet namespace](#node-exporter-daemonset-namespace)
    * [Alertmanager configuration](#alertmanager-configuration)
    * [Static etcd configuration](#static-etcd-configuration)
    * [Customizing Prometheus alerting/recording rules and Grafana dashboards](#customizing-prometheus-alertingrecording-rules-and-grafana-dashboards)
    * [Exposing Prometheus/Alermanager/Grafana via Ingress](#exposing-prometheusalermanagergrafana-via-ingress)
* [Minikube Example](#minikube-example)
* [Troubleshooting](#troubleshooting)
    * [Error retrieving kubelet metrics](#error-retrieving-kubelet-metrics)
    * [kube-state-metrics resource usage](#kube-state-metrics-resource-usage)
* [Contributing](#contributing)

## Prerequisites

You will need a Kubernetes cluster, that's it! By default it is assumed, that the kubelet uses token authN and authZ, as otherwise Prometheus needs a client certificate, which gives it full access to the kubelet, rather than just the metrics. Token authN and authZ allows more fine grained and easier access control.

This means the kubelet configuration must contain these flags:

* `--authentication-token-webhook=true` This flag enables, that a `ServiceAccount` token can be used to authenticate against the kubelet(s).
* `--authorization-mode=Webhook` This flag enables, that the kubelet will perform an RBAC request with the API to determine, whether the requesting entity (Prometheus in this case) is allow to access a resource, in specific for this project the `/metrics` endpoint.

### minikube

In order to just try out this stack, start minikube with the following command:

```
$ minikube delete && minikube start --kubernetes-version=v1.10.1 --memory=4096 --bootstrapper=kubeadm --extra-config=kubelet.authentication-token-webhook=true --extra-config=kubelet.authorization-mode=Webhook --extra-config=scheduler.address=0.0.0.0 --extra-config=controller-manager.address=0.0.0.0
```

## Quickstart

This project is intended to be used as a library (i.e. the intent is not for you to create your own modified copy of this repository).

Though for a quickstart a compiled version of the Kubernetes [manifests](manifests) generated with this library (specifically with `example.jsonnet`) is checked into this repository in order to try the content out quickly. To try out the stack un-customized run:
 * Simply create the stack:
```
$ kubectl create -f manifests/ || true
$ kubectl create -f manifests/ 2>/dev/null || true  # This command sometimes may need to be done twice
```
 * And to teardown the stack:
```
$ kubectl delete -f manifests/ || true
```

### Access the dashboards

Prometheus, Grafana, and Alertmanager dashboards can be accessed quickly using `kubectl port-forward` after running the quickstart via the commands below. Kubernetes 1.10 or later is required.

> Note: There are instructions on how to route to these pods behdind an ingress controller in the [Exposing Prometheus/Alermanager/Grafana via Ingress](#exposing-prometheusalermanagergrafana-via-ingress) section.

Prometheus

```shell
kubectl --namespace monitoring port-forward svc/prometheus-k8s 9090
```

Then access via [http://localhost:9090](http://localhost:9090)

Grafana

```shell
kubectl --namespace monitoring port-forward svc/grafana 3000
```

Then access via [http://localhost:3000](http://localhost:3000) and use the default grafana user:password of `admin:admin`.

Alert Manager

```shell
kubectl --namespace monitoring port-forward svc/alertmanager-main 9093
```

Then access via [http://localhost:9093](http://localhost:9093)

## Customizing Kube-Prometheus

This section:
 * describes how to customize the kube-prometheus library via compiling the kube-prometheus manifests yourself (as an alternative to the [Quickstart section](#Quickstart)).
 * still doesn't require you to make a copy of this entire repository, but rather only a copy of a few select files.

### Installing

The content of this project consists of a set of [jsonnet](http://jsonnet.org/) files making up a library to be consumed.

Install this library in your own project with [jsonnet-bundler](https://github.com/jsonnet-bundler/jsonnet-bundler#install) (the jsonnet package manager):
```
$ mkdir my-kube-prometheus; cd my-kube-prometheus
$ jb init  # Creates the initial/empty `jsonnetfile.json`
# Install the kube-prometheus dependency
$ jb install github.com/coreos/prometheus-operator/contrib/kube-prometheus/jsonnet/kube-prometheus  # Creates `vendor/` & `jsonnetfile.lock.json`, and fills in `jsonnetfile.json`
```

> `jb` can be installed with `go get github.com/jsonnet-bundler/jsonnet-bundler/cmd/jb`

> An e.g. of how to install a given version of this library: `jb install github.com/coreos/prometheus-operator/contrib/kube-prometheus/jsonnet/kube-prometheus/@v0.22.0`

In order to update the kube-prometheus dependency, simply use the jsonnet-bundler update functionality:
`$ jb update`

### Compiling

e.g. of how to compile the manifests: `./build.sh example.jsonnet`

Here's [example.jsonnet](example.jsonnet):

[embedmd]:# (example.jsonnet)
```jsonnet
local kp = (import 'kube-prometheus/kube-prometheus.libsonnet') + {
  _config+:: {
    namespace: 'monitoring',
  },
};

{ ['00namespace-' + name]: kp.kubePrometheus[name] for name in std.objectFields(kp.kubePrometheus) } +
{ ['0prometheus-operator-' + name]: kp.prometheusOperator[name] for name in std.objectFields(kp.prometheusOperator) } +
{ ['node-exporter-' + name]: kp.nodeExporter[name] for name in std.objectFields(kp.nodeExporter) } +
{ ['kube-state-metrics-' + name]: kp.kubeStateMetrics[name] for name in std.objectFields(kp.kubeStateMetrics) } +
{ ['alertmanager-' + name]: kp.alertmanager[name] for name in std.objectFields(kp.alertmanager) } +
{ ['prometheus-' + name]: kp.prometheus[name] for name in std.objectFields(kp.prometheus) } +
{ ['grafana-' + name]: kp.grafana[name] for name in std.objectFields(kp.grafana) }
```

And here's the [build.sh](build.sh) script (which uses `vendor/` to render all manifests in a json structure of `{filename: manifest-content}`):

[embedmd]:# (build.sh)
```sh
#!/usr/bin/env bash

# This script uses arg $1 (name of *.jsonnet file to use) to generate the manifests/*.yaml files.

set -e
set -x
# only exit with zero if all commands of the pipeline exit successfully
set -o pipefail

# Make sure to start with a clean 'manifests' dir
rm -rf manifests
mkdir manifests

                                               # optional, but we would like to generate yaml, not json
jsonnet -J vendor -m manifests "${1-example.jsonnet}" | xargs -I{} sh -c 'cat {} | gojsontoyaml > {}.yaml; rm -f {}' -- {}

```

> Note you need `jsonnet` (`go get github.com/google/go-jsonnet/jsonnet`) and `gojsontoyaml` (`go get github.com/brancz/gojsontoyaml`) installed to run `build.sh`. If you just want json output, not yaml, then you can skip the pipe and everything afterwards.

This script runs the jsonnet code, then reads each key of the generated json and uses that as the file name, and writes the value of that key to that file, and converts each json manifest to yaml.

### Containerized Installing and Compiling

If you don't care to have `jb` nor `jsonnet` nor `gojsontoyaml` installed, then build the `po-jsonnet` Docker image (this is something you'll need a copy of this repository for). Do the following from this `kube-prometheus` directory:
```
$ make ../../hack/jsonnet-docker-image
```

Then you can do commands such as the following:
```
docker run \
	--rm \
	-v `pwd`:`pwd` \
	--workdir `pwd` \
	po-jsonnet jb init

docker run \
	--rm \
	-v `pwd`:`pwd` \
	--workdir `pwd` \
	po-jsonnet jb install github.com/coreos/prometheus-operator/contrib/kube-prometheus/jsonnet/kube-prometheus

docker run \
	--rm \
	-v `pwd`:`pwd` \
	--workdir `pwd` \
	po-jsonnet ./build.sh example.jsonnet
```

## Configuration

Jsonnet has the concept of hidden fields. These are fields, that are not going to be rendered in a result. This is used to configure the kube-prometheus components in jsonnet. In the example jsonnet code of the above [Usage section](#Usage), you can see an example of this, where the `namespace` is being configured to be `monitoring`. In order to not override the whole object, use the `+::` construct of jsonnet, to merge objects, this way you can override individual settings, but retain all other settings and defaults.

These are the available fields with their respective default values:
```
{
	_config+:: {
    namespace: "default",

    versions+:: {
        alertmanager: "v0.15.2",
        nodeExporter: "v0.16.0",
        kubeStateMetrics: "v1.3.1",
        kubeRbacProxy: "v0.3.1",
        addonResizer: "1.0",
        prometheusOperator: "v0.24.0",
        prometheus: "v2.4.3",
    },

    imageRepos+:: {
        prometheus: "quay.io/prometheus/prometheus",
        alertmanager: "quay.io/prometheus/alertmanager",
        kubeStateMetrics: "quay.io/coreos/kube-state-metrics",
        kubeRbacProxy: "quay.io/coreos/kube-rbac-proxy",
        addonResizer: "quay.io/coreos/addon-resizer",
        nodeExporter: "quay.io/prometheus/node-exporter",
        prometheusOperator: "quay.io/coreos/prometheus-operator",
    },

    prometheus+:: {
        names: 'k8s',
        replicas: 2,
        rules: {},
    },

    alertmanager+:: {
      name: 'main',
      config: |||
        global:
          resolve_timeout: 5m
        route:
          group_by: ['job']
          group_wait: 30s
          group_interval: 5m
          repeat_interval: 12h
          receiver: 'null'
          routes:
          - match:
              alertname: DeadMansSwitch
            receiver: 'null'
        receivers:
        - name: 'null'
      |||,
      replicas: 3,
    },

    kubeStateMetrics+:: {
      collectors: '',  // empty string gets a default set
      scrapeInterval: '30s',
      scrapeTimeout: '30s',

      baseCPU: '100m',
      baseMemory: '150Mi',
      cpuPerNode: '2m',
      memoryPerNode: '30Mi',
    },
	},
}
```

The grafana definition is located in a different project (https://github.com/brancz/kubernetes-grafana), but needed configuration can be customized from the same top level `_config` field. For example to allow anonymous access to grafana, add the following `_config` section:
```
      grafana+:: {
        config: { // http://docs.grafana.org/installation/configuration/
          sections: {
            "auth.anonymous": {enabled: true},
          },
        },
      },
```

## Customization Examples

Jsonnet is a turing complete language, any logic can be reflected in it. It also has powerful merge functionalities, allowing sophisticated customizations of any kind simply by merging it into the object the library provides.

### Cluster Creation Tools

A common example is that not all Kubernetes clusters are created exactly the same way, meaning the configuration to monitor them may be slightly different. For [kubeadm](examples/jsonnet-snippets/kubeadm.jsonnet) and [bootkube](examples/jsonnet-snippets/bootkube.jsonnet) and [kops](examples/jsonnet-snippets/kops.jsonnet) clusters there are mixins available to easily configure these:

kubeadm:

[embedmd]:# (examples/jsonnet-snippets/kubeadm.jsonnet)
```jsonnet
(import 'kube-prometheus/kube-prometheus.libsonnet') +
(import 'kube-prometheus/kube-prometheus-kubeadm.libsonnet')
```

bootkube:

[embedmd]:# (examples/jsonnet-snippets/bootkube.jsonnet)
```jsonnet
(import 'kube-prometheus/kube-prometheus.libsonnet') +
(import 'kube-prometheus/kube-prometheus-bootkube.libsonnet')
```

kops:

[embedmd]:# (examples/jsonnet-snippets/kops.jsonnet)
```jsonnet
(import 'kube-prometheus/kube-prometheus.libsonnet') +
(import 'kube-prometheus/kube-prometheus-kops.libsonnet')
```

### NodePorts

Another mixin that may be useful for exploring the stack is to expose the UIs of Prometheus, Alertmanager and Grafana on NodePorts:

[embedmd]:# (examples/jsonnet-snippets/node-ports.jsonnet)
```jsonnet
(import 'kube-prometheus/kube-prometheus.libsonnet') +
(import 'kube-prometheus/kube-prometheus-node-ports.libsonnet')
```

### Prometheus Object Name

To give another customization example, the name of the `Prometheus` object provided by this library can be overridden:

[embedmd]:# (examples/prometheus-name-override.jsonnet)
```jsonnet
((import 'kube-prometheus/kube-prometheus.libsonnet') + {
   prometheus+: {
     prometheus+: {
       metadata+: {
         name: 'my-name',
       },
     },
   },
 }).prometheus.prometheus
```

### node-exporter DaemonSet namespace

Standard Kubernetes manifests are all written using [ksonnet-lib](https://github.com/ksonnet/ksonnet-lib/), so they can be modified with the mixins supplied by ksonnet-lib. For example to override the namespace of the node-exporter DaemonSet:

[embedmd]:# (examples/ksonnet-example.jsonnet)
```jsonnet
local k = import 'ksonnet/ksonnet.beta.3/k.libsonnet';
local daemonset = k.apps.v1beta2.daemonSet;

((import 'kube-prometheus/kube-prometheus.libsonnet') + {
   nodeExporter+: {
     daemonset+:
       daemonset.mixin.metadata.withNamespace('my-custom-namespace'),
   },
 }).nodeExporter.daemonset
```

### Alertmanager configuration

The Alertmanager configuration is located in the `_config.alertmanager.config` configuration field. In order to set a custom Alertmanager configuration simply set this field.

[embedmd]:# (examples/alertmanager-config.jsonnet)
```jsonnet
((import 'kube-prometheus/kube-prometheus.libsonnet') + {
   _config+:: {
     alertmanager+: {
       config: |||
         global:
           resolve_timeout: 10m
         route:
           group_by: ['job']
           group_wait: 30s
           group_interval: 5m
           repeat_interval: 12h
           receiver: 'null'
           routes:
           - match:
               alertname: DeadMansSwitch
             receiver: 'null'
         receivers:
         - name: 'null'
       |||,
     },
   },
 }).alertmanager.secret
```

In the above example the configuration has been inlined, but can just as well be an external file imported in jsonnet via the `importstr` function.

[embedmd]:# (examples/alertmanager-config-external.jsonnet)
```jsonnet
((import 'kube-prometheus/kube-prometheus.libsonnet') + {
   _config+:: {
     alertmanager+: {
       config: importstr 'alertmanager-config.yaml',
     },
   },
 }).alertmanager.secret
```

### Adding additional namespaces to monitor

In order to monitor additional namespaces, the Prometheus server requires the appropriate `Role` and `RoleBinding` to be able to discover targets from that namespace. By default the Prometheus server is limited to the three namespaces it requires: default, kube-system and the namespace you configure the stack to run in via `$._config.namespace`. This is specified in `$._config.prometheus.namespaces`, to add new namespaces to monitor, simply append the additional namespaces:

[embedmd]:# (examples/additional-namespaces.jsonnet)
```jsonnet
local kp = (import 'kube-prometheus/kube-prometheus.libsonnet') + {
  _config+:: {
    namespace: 'monitoring',

    prometheus+:: {
      namespaces+: ['my-namespace', 'my-second-namespace'],
    },
  },
};

{ ['00namespace-' + name]: kp.kubePrometheus[name] for name in std.objectFields(kp.kubePrometheus) } +
{ ['0prometheus-operator-' + name]: kp.prometheusOperator[name] for name in std.objectFields(kp.prometheusOperator) } +
{ ['node-exporter-' + name]: kp.nodeExporter[name] for name in std.objectFields(kp.nodeExporter) } +
{ ['kube-state-metrics-' + name]: kp.kubeStateMetrics[name] for name in std.objectFields(kp.kubeStateMetrics) } +
{ ['alertmanager-' + name]: kp.alertmanager[name] for name in std.objectFields(kp.alertmanager) } +
{ ['prometheus-' + name]: kp.prometheus[name] for name in std.objectFields(kp.prometheus) } +
{ ['grafana-' + name]: kp.grafana[name] for name in std.objectFields(kp.grafana) }
```

### Static etcd configuration

In order to configure a static etcd cluster to scrape there is a simple [kube-prometheus-static-etcd.libsonnet](jsonnet/kube-prometheus/kube-prometheus-static-etcd.libsonnet) mixin prepared - see [etcd.jsonnet](examples/etcd.jsonnet) for an example of how to use that mixin, and [Monitoring external etcd](docs/monitoring-external-etcd.md) for more information.

> Note that monitoring etcd in minikube is currently not possible because of how etcd is setup. (minikube's etcd binds to 127.0.0.1:2379 only, and within host networking namespace.)

### Customizing Prometheus alerting/recording rules and Grafana dashboards

See [developing Prometheus rules and Grafana dashboards](docs/developing-prometheus-rules-and-grafana-dashboards.md) guide.

### Exposing Prometheus/Alermanager/Grafana via Ingress

See [exposing Prometheus/Alertmanager/Grafana](docs/exposing-prometheus-alertmanager-grafana-ingress.md) guide.

## Minikube Example

To use an easy to reproduce example, see [minikube.jsonnet](examples/minikube.jsonnet), which uses the minikube setup as demonstrated in [Prerequisites](#prerequisites). Because we would like easy access to our Prometheus, Alertmanager and Grafana UIs, `minikube.jsonnet` exposes the services as NodePort type services.

## Troubleshooting

### Error retrieving kubelet metrics

Should the Prometheus `/targets` page show kubelet targets, but not able to successfully scrape the metrics, then most likely it is a problem with the authentication and authorization setup of the kubelets.

As described in the [Prerequisites](#prerequisites) section, in order to retrieve metrics from the kubelet token authentication and authorization must be enabled. Some Kubernetes setup tools do not enable this by default.

If you are using Google's GKE product, see [docs/GKE-cadvisor-support.md].

#### Authentication problem

The Prometheus `/targets` page will show the kubelet job with the error `403 Unauthorized`, when token authentication is not enabled. Ensure, that the `--authentication-token-webhook=true` flag is enabled on all kubelet configurations.

#### Authorization problem

The Prometheus `/targets` page will show the kubelet job with the error `401 Unauthorized`, when token authorization is not enabled. Ensure that the `--authorization-mode=Webhook` flag is enabled on all kubelet configurations.

### kube-state-metrics resource usage

In some environments, kube-state-metrics may need additional
resources. One driver for more resource needs, is a high number of
namespaces. There may be others.

kube-state-metrics resource allocation is managed by
[addon-resizer](https://github.com/kubernetes/autoscaler/tree/master/addon-resizer/nanny)
You can control it's parameters by setting variables in the
config. They default to:

``` jsonnet
    kubeStateMetrics+:: {
      baseCPU: '100m',
      cpuPerNode: '2m',
      baseMemory: '150Mi',
      memoryPerNode: '30Mi',
    }
```

## Contributing

All `.yaml` files in the `/manifests` folder are generated via
[Jsonnet](https://jsonnet.org/). Contributing changes will most likely include
the following process:

1. Make your changes in the respective `*.jsonnet` file.
2. Commit your changes (This is currently necessary due to our vendoring
   process. This is likely to change in the future).
3. Update the pinned kube-prometheus dependency in `jsonnetfile.lock.json`: `jb
   update`.
3. Generate dependent `*.yaml` files: `make generate-in-docker`.
4. Commit the generated changes.
# Custom Metrics API

The custom metrics API allows the HPA v2 to scale on arbirary metrics.

This directory contains an example deployment of the custom metrics API adapter using Prometheus as the backing monitoring system.

In order to deploy the custom metrics adapter for Prometheus you need to generate TLS certficates used to serve the API. An example of how these could be generated can be found in `./gencerts.sh`, note that this is _not_ recommended to be used in production. You need to employ a secure PKI strategy, this is merely an example to get started and try it out quickly.

Once the generated `Secret` with the certificates is in place, you can deploy everything in the `monitoring` namespace using `./deploy.sh`.

When you're done, you can teardown using the `./teardown.sh` script.
# WARNING: 
This helm charts are been migrated to kubernetes charts upstream. Therefore we are currently not accepting any pull requests. Thank you for your understanding. 

You can track the progess of the work [here](https://github.com/coreos/prometheus-operator/issues/592) and [here](https://github.com/helm/charts/pull/6765)

# TL;DR

```
# Install helm https://docs.helm.sh/using_helm/ then run:
helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable/
helm install coreos/prometheus-operator --name prometheus-operator --namespace monitoring
helm install coreos/kube-prometheus --name kube-prometheus --namespace monitoring
````

# How to contribute?

1. Fork the project
2. Make	 the changes in the helm charts
3. Bump the version in Chart.yaml for each modified chart
4. Update [kube-prometheus/requirements.yaml](kube-prometheus/requirements.yaml) file with the dependencies
5. Bump the [kube-prometheus/Chart.yaml](kube-prometheus/Chart.yaml)
6. [Test locally](#how-to-test)
7. Push the changes

# How to test?


```
# From top directory i.e. prometheus-operator
helm install helm/prometheus-operator --name prometheus-operator --namespace monitoring
mkdir -p helm/kube-prometheus/charts
helm package -d helm/kube-prometheus/charts helm/alertmanager helm/grafana helm/prometheus  helm/exporter-kube-dns \
helm/exporter-kube-scheduler helm/exporter-kubelets helm/exporter-node helm/exporter-kube-controller-manager \
helm/exporter-kube-etcd helm/exporter-kube-state helm/exporter-coredns helm/exporter-kubernetes
helm install helm/kube-prometheus --name kube-prometheus --namespace monitoring

```
# prometheus-operator

Installs [prometheus-operator](https://github.com/coreos/prometheus-operator) to create/configure/manage Prometheus clusters atop Kubernetes.

## TL;DR;

```console
$ helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable/
$ helm install coreos/prometheus-operator
```

## Introduction

This chart bootstraps a [prometheus-operator](https://github.com/coreos/prometheus-operator) deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites
  - Kubernetes 1.8+ with Beta APIs

### RBAC
If role-based access control (RBAC) is enabled in your cluster, you may need to give Tiller (the server-side component of Helm) additional permissions. **If RBAC is not enabled, be sure to set `rbacEnable` to `false` when installing the chart.**

1. Create a ServiceAccount for Tiller in the `kube-system` namespace
```console
$ kubectl -n kube-system create sa tiller
```

2. Create a ClusterRoleBinding for Tiller
```console
$ kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
```

3. Install Tiller, specifying the new ServiceAccount
```console
$ helm init --service-account tiller
```

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm install --name my-release coreos/prometheus-operator
```

The command deploys prometheus-operator on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section lists the parameters that can be configured during installation.

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following tables lists the configurable parameters of the prometheus-operator chart and their default values.

Parameter | Description | Default
--- | --- | ---
`configmapReload.repository` | configmap-reload image | `quay.io/coreos/configmap-reload`
`configmapReload.tag` | configmap-reload tag | `v0.0.1`
`global.hyperkube.repository` | Hyperkube image | `quay.io/coreos/hyperkube`
`global.hyperkube.tag` | Hyperkube image tag | `v1.7.6_coreos.0`
`global.hyperkube.pullPolicy` | Hyperkube image pull policy | `IfNotPresent`
`image.repository` | Image | `quay.io/coreos/prometheus-operator`
`image.tag` | Image tag | `v0.19.0`
`image.pullPolicy` | Image pull policy | `IfNotPresent`
`kubeletService.enable` | If true, the operator will create a service for scraping kubelets | `true`
`kubeletService.namespace` | The namespace in which the kubelet service should be created | `kube-system`
`kubeletService.name` | The name of the kubelet service to be created | `kubelet`
`nodeSelector` | Node labels for pod assignment | `{}`
`prometheusConfigReloader.repository` | prometheus-config-reloader image | `quay.io/coreos/prometheus-config-reloader`
`prometheusConfigReloader.tag` | prometheus-config-reloader tag | `v0.0.4`
`rbacEnable` | If true, create & use RBAC resources | `true`
`resources` | Pod resource requests & limits | `{}`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,

```console
$ helm install --name my-release coreos/prometheus-operator --set sendAnalytics=true
```

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example,

```console
$ helm install --name my-release coreos/prometheus-operator -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)
# Grafana Helm Chart

* Installs the web dashboarding system [Grafana](http://grafana.org/)

## TL;DR;

```console
$ helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable/
$ helm install coreos/grafana
```
## Introduction

This chart bootstraps an [Grafana](http://grafana.org) deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager, and preinstalled some defaut dashboard for dashboarding Kubernetes metrics.

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm install --name my-release coreos/grafana
```

## Uninstalling the Chart

To uninstall/delete the my-release deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.


## Configuration

Parameter | Description | Default
--- | --- | ---
`routePrefix` | Prefix used to register routes | `"/"`
`auth.anonymous.enabled` | If true, enable anonymous authentication | `true`
`adminUser` | Grafana admin user name | `admin`
`adminPassword` | Grafana admin user password | `admin`
`image.repository` | Image | `grafana/grafana`
`image.tag` | Image tag | `4.4.1`
`extraVars` | Pass extra environment variables to the Grafana container. | `{}`
`grafanaWatcher.repository` | Image | `quay.io/coreos/grafana-watcher`
`grafanaWatcher.tag` | Image tag | `v0.0.8`
`ingress.enabled` | If true, Grafana Ingress will be created | `false`
`ingress.annotations` | Annotations for Grafana Ingress | `{}`
`ingress.labels` | Labels for Grafana Ingress | `{}`
`ingress.hosts` | Grafana Ingress fully-qualified domain names | `[]`
`ingress.tls` | TLS configuration for Grafana Ingress | `[]`
`nodeSelector` | Node labels for pod assignment | `{}`
`resources` | Pod resource requests & limits | `{}`
`service.annotations` | Annotations to be added to the Grafana Service | `{}`
`service.clusterIP` | Cluster-internal IP address for Grafana Service | `""`
`service.externalIPs` | List of external IP addresses at which the Grafana Service will be available | `[]`
`service.labels` | Labels for Grafana Service | `{}`
`service.loadBalancerIP` | External IP address to assign to Grafana Service | `""`
`service.loadBalancerSourceRanges` | List of client IPs allowed to access Grafana Service | `[]`
`service.nodePort` | Port to expose Grafana Service on each node | `30902`
`service.type` | Grafana Service type | `ClusterIP`
`storageSpec` | Grafana StorageSpec for persistent data | `{}`
`resources` | Pod resource requests & limits | `{}`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,
$ helm install coreos/grafana --name my-release --set adminUser=bob
```

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example,

```console
$ helm install coreos/grafana --name my-release -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)

> **Tip**: On GCE If you want to  use  `Ingress.enabled=true`, you must put `service.type=NodePort`

## Adding Grafana Dashboards

You can either add new dashboards via `serverDashboardConfigmaps` in `values.yaml`. These can then be
picked up by Grafana Watcher.

```yaml
serverDashboardConfigmaps:
  - example-dashboards
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: example-dashboards
data:
{{ (.Files.Glob "custom-dashboards/*.json").AsConfig | indent 2 }}

# Or
#
# data:
#   custom-dashboard.json: |-
# {{ (.Files.Get "custom.json") | indent 4 }}
#
# The filename (and consequently the key under data) must be in the format `xxx-dashboard.json` or `xxx-datasource.json`
# for them to be picked up.
```

Another way is to add them through `serverDashboardFiles` directly in `values.yaml`. These are then combined
into the same ConfigMap for the rest of the default dashboards.

```yaml
serverDashboardFiles:
  example-dashboard.json: |-
    {
      "dashboard": {
        "annotations:[]
        ...
      }
    }
```

In both cases, if you're exporting the jsons directly from Grafana, you'll want to wrap it in `{"dashboard": {}}`
as stated in [Grafana Watcher's README](https://github.com/coreos/prometheus-operator/tree/master/contrib/grafana-watcher).
# kube-prometheus

This is the helm chart equivalent of `contrib/kube-prometheus`.

# Prerequisites

Requires helm >= 2.5.0

# Installing on GKE/EKS/AKS

Since the controlplane is managed in these solutions, make sure you tell prometheus to not monitor the scheduler or controller-manager:

```
deployKubeScheduler: False
deployKubeControllerManager: False
```

Then install your custom values (for example):

```
helm upgrade --install kube-prometheus coreos/kube-prometheus --namespace monitoring -f /root/.helm/kube-prometheus-values.yml"
```
# alertmanager

Installs a [Prometheus](https://prometheus.io) Alertmanager instance using the CoreOS [prometheus-operator](https://github.com/coreos/prometheus-operator).

## TL;DR;

```console
$ helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable/
$ helm install coreos/alertmanager
```

## Introduction

This chart bootstraps an [Alertmanager](https://github.com/prometheus/alertmanager) deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites
  - Kubernetes 1.4+ with Beta APIs & ThirdPartyResources enabled
  - [prometheus-operator](https://github.com/coreos/prometheus-operator/blob/master/helm/prometheus-operator/README.md).

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm install coreos/alertmanager --name my-release
```

The command deploys Alertmanager  on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section lists the parameters that can be configured during installation.

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following tables lists the configurable parameters of the alertmanager chart and their default values.

Parameter | Description | Default
--- | --- | ---
`config` | Alertmanager configuration directives | `{}`
`configFromSecret` | Alertmanager configuration directives read from external Secret reference by name | `""`
`externalUrl` | External URL at which Alertmanager will be reachable | `""`
`routePrefix` | Prefix used to register routes | `"/"`
`image.repository` | Image | `quay.io/prometheus/alertmanager`
`image.tag` | Image tag | `v0.12.0`
`ingress.enabled` | If true, Alertmanager Ingress will be created | `false`
`ingress.annotations` | Annotations for Alertmanager Ingress` | `{}`
`ingress.labels` | Labels for Alertmanager Ingress` | `{}`
`ingress.hosts` | Alertmanager Ingress hosts | `[]`
`ingress.tls` | TLS configuration for Alertmanager Ingress | `[]`
`nodeSelector` | Node labels for pod assignment | `{}`
`paused` | If true, the Operator won't process any Alertmanager configuration changes | `false`
`podAntiAffinity` | If "soft", the scheduler attempts to place Alertmanager replicas on different nodes. If "hard" the scheduler is required to place them on different nodes. If "" (empty) then no anti-affinity rules will be configured. | `soft`
`prometheusRules` | Prometheus rules | `[templates/alertmanager.rules.yaml](templates/alertmanager.rules.yaml)`
`replicaCount` | Number of Alertmanager replicas desired | `1`
`resources` | Pod resource requests & limits | `{}`
`service.annotations` | Annotations to be added to the Alertmanager Service | `{}`
`service.clusterIP` | Cluster-internal IP address for Alertmanager Service | `""`
`service.externalIPs` | List of external IP addresses at which the Alertmanager Service will be available | `[]`
`service.loadBalancerIP` | External IP address to assign to Alertmanager Service | `""`
`service.loadBalancerSourceRanges` | List of client IPs allowed to access Alertmanager Service | `[]`
`service.nodePort` | Port to expose Alertmanager Service on each node | `39093`
`service.type` | Alertmanager Service type | `ClusterIP`
`storageSpec` | Alertmanager StorageSpec for persistent data | `{}`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,
$ helm install coreos/alertmanager --name my-release --set externalUrl=http://alertmanager.example.com
```

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example,

```console
$ helm install coreos/alertmanager --name my-release -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)

### CRD Resource Documentation
- [Alertmanager](/Documentation/design.md#alertmanager)
- [Prometheus](/Documentation/design.md#prometheus)
- [ServiceMonitor](/Documentation/design.md#servicemonitor)
# prometheus

Installs a [Prometheus](https://prometheus.io) instance using the CoreOS [prometheus-operator](https://github.com/coreos/prometheus-operator).

## TL;DR;

```console
$ helm repo add coreos https://s3-eu-west-1.amazonaws.com/coreos-charts/stable/
$ helm install coreos/prometheus
```

## Introduction

This chart bootstraps a [Prometheus](https://github.com/prometheus/prometheus) deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites
  - Kubernetes 1.4+ with Beta APIs & ThirdPartyResources enabled
  - [prometheus-operator](https://github.com/coreos/prometheus-operator/blob/master/helm/prometheus-operator/README.md).

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm install coreos/prometheus --name my-release
```

The command deploys Prometheus on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section lists the parameters that can be configured during installation.

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following tables lists the configurable parameters of the prometheus chart and their default values.

Parameter | Description | Default
--- | --- | ---
`alertingEndpoints` | Alertmanagers to which alerts will be sent | `[]`
`config` | Prometheus configuration directives | `{}`
`externalLabels` | The labels to add to any time series or alerts when communicating with external systems  | `{}`
`externalUrl` | External URL at which Prometheus will be reachable | `""`
`routePrefix` | Prefix used to register routes | `"/"`
`image.repository` | Image | `quay.io/prometheus/prometheus`
`image.tag` | Image tag | `v2.2.1`
`ingress.enabled` | If true, Prometheus Ingress will be created | `false`
`ingress.annotations` | Annotations for Prometheus Ingress` | `{}`
`ingress.labels` | Labels for Prometheus Ingress | `{}`
`ingress.hosts` | Prometheus Ingress fully-qualified domain names | `[]`
`ingress.tls` | TLS configuration for Prometheus Ingress | `[]`
`nodeSelector` | Node labels for pod assignment | `{}`
`paused` | If true, the Operator won't process any Prometheus configuration changes | `false`
`podAntiAffinity` | If "soft", the scheduler attempts to place Prometheus replicas on different nodes. If "hard" the scheduler is required to place them on different nodes. If "" (empty) then no anti-affinity rules will be configured. | `soft`
`prometheusRules` | Prometheus rules | `[templates/prometheus.rules.yaml](templates/prometheus.rules.yaml)`
`replicaCount` | Number of Prometheus replicas desired | `1`
`remoteRead` | The remote_read spec configuration for Prometheus | `{}`
`remoteWrite` | The remote_read spec configuration for Prometheus | `{}`
`resources` | Pod resource requests & limits | `{}`
`retention` | How long to retain metrics | `24h`
`routePrefix` | Prefix used to register routes, overriding externalUrl route | `/`
`rules` | Prometheus alerting & recording rules | `{}`
`ruleNamespaceSelector` | Namespaces to be selected for PrometheusRules discovery | `{}`
`rulesSelector` | Rules CRD selector | `{}`
`secrets` | List of Secrets in the same namespace as the Prometheus object, which shall be mounted into the Prometheus Pods. | `{}`
`service.annotations` | Annotations to be added to the Prometheus Service | `{}`
`service.clusterIP` | Cluster-internal IP address for Prometheus Service | `""`
`service.externalIPs` | List of external IP addresses at which the Prometheus Service will be available | `[]`
`service.loadBalancerIP` | External IP address to assign to Prometheus Service | `""`
`service.loadBalancerSourceRanges` | List of client IPs allowed to access Prometheus Service | `[]`
`service.nodePort` | Port to expose Prometheus Service on each node | `39090`
`service.type` | Prometheus Service type | `ClusterIP`
`serviceMonitors` | ServiceMonitor crd resources to create & be scraped by this Prometheus instance | `[]`
`serviceMonitorsSelector` | ServiceMonitor ConfigMap selector | `{}`
`storageSpec` | Prometheus StorageSpec for persistent data | `{}`

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`. For example,
$ helm install coreos/prometheus --name my-release --set externalUrl=http://prometheus.example.com


Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example:

```console
$ helm install coreos/prometheus --name my-release -f values.yaml
```

> **Tip**: You can use the default [values.yaml](values.yaml)


### Service Monitors

Custom service monitors can be added in values.yaml in the `serviceMonitors` section. Please refere to `values.yaml` for all available parameters.


#### Example service monitor


This example Service Monitor will monitor applications matching `app: nginx-ingress`. The port `metrics` will be scraped with the path `/metrics`. The endpoint will be scraped every 30 seconds.

```
serviceMonitors:
  - name: kube-prometheus-nginx-ingress
    labels:
      prometheus: kube-prometheus
    selector:
      matchLabels:
        app: nginx-ingress
    endpoints:
      - port: metrics
        interval: 30s
        path: /metrics
    namespaceSelector:
      any: true
```

### CRD Resource Documentation
- [Alertmanager](/Documentation/design.md#alertmanager)
- [Prometheus](/Documentation/design.md#prometheus)
- [ServiceMonitor](/Documentation/design.md#servicemonitor)
