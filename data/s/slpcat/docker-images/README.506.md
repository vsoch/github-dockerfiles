# ChartMuseum
<img align="right" src="https://github.com/kubernetes-helm/chartmuseum/raw/master/logo.png">

[![CircleCI](https://circleci.com/gh/kubernetes-helm/chartmuseum.svg?style=svg)](https://circleci.com/gh/kubernetes-helm/chartmuseum)
[![Go Report Card](https://goreportcard.com/badge/github.com/kubernetes-helm/chartmuseum)](https://goreportcard.com/report/github.com/kubernetes-helm/chartmuseum)
[![GoDoc](https://godoc.org/github.com/kubernetes-helm/chartmuseum?status.svg)](https://godoc.org/github.com/kubernetes-helm/chartmuseum)
<sub>**_"Preserve your precious artifacts... in the cloud!"_**<sub>

*ChartMuseum* is an open-source **[Helm Chart Repository](https://github.com/kubernetes/helm/blob/master/docs/chart_repository.md)** written in Go (Golang), with support for cloud storage backends, including [Google Cloud Storage](https://cloud.google.com/storage/), [Amazon S3](https://aws.amazon.com/s3/), [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/), [Alibaba Cloud OSS Storage](https://www.alibabacloud.com/product/oss) and [Openstack Object Storage](https://developer.openstack.org/api-ref/object-store/).

Works as a valid Helm Chart Repository, and also provides an API for uploading new chart packages to storage etc.

<img width="60" align="right" src="https://github.com/golang-samples/gopher-vector/raw/master/gopher-side_color.png">
<img width="20" align="right" src="https://github.com/golang-samples/gopher-vector/raw/master/gopher-side_color.png">

Powered by some great Go technology:
- [Kubernetes Helm](https://github.com/kubernetes/helm) - for working with charts, generating repository index
- [Gin Web Framework](https://github.com/gin-gonic/gin) - for HTTP routing
- [cli](https://github.com/urfave/cli) - for command line option parsing
- [zap](https://github.com/uber-go/zap) - for logging

## Things that have been said in Helm land
>"Finally!!"

>"ChartMuseum is awesome"

>"This is awesome!"

>"Oh yes!!!! I’ve been waiting for this for so long. Makes life much easier, especially for the index.yaml creation!"

>"I was thinking about writing one of these up myself. This is perfect! thanks!"

>"I am jumping for joy over ChartMuseum, a full-fledged Helm repository server with upload!"

>"This is really cool ... We currently have a process that generates the index file and then uploads, so this is nice"

>"Really a good idea ... really really great, thanks again. I can use nginx to hold the repos and the museum to add/delete the chart. That's a whole life cycle management of chart with the current helm"

>"thanks for building the museum!"

## API
### Helm Chart Repository
- `GET /index.yaml` - retrieved when you run `helm repo add chartmuseum http://localhost:8080/`
- `GET /charts/mychart-0.1.0.tgz` - retrieved when you run `helm install chartmuseum/mychart`
- `GET /charts/mychart-0.1.0.tgz.prov` - retrieved when you run `helm install` with the `--verify` flag

### Chart Manipulation
- `POST /api/charts` - upload a new chart version
- `POST /api/prov` - upload a new provenance file
- `DELETE /api/charts/<name>/<version>` - delete a chart version (and corresponding provenance file)
- `GET /api/charts` - list all charts
- `GET /api/charts/<name>` - list all versions of a chart
- `GET /api/charts/<name>/<version>` - describe a chart version

### Server Info
- `GET /` - HTML welcome page
- `GET /health` - returns 200 OK

## Uploading a Chart Package
<sub>*Follow **"How to Run"** section below to get ChartMuseum up and running at ht<span>tp:/</span>/localhost:8080*<sub>

First create `mychart-0.1.0.tgz` using the [Helm CLI](https://docs.helm.sh/using_helm/#installing-helm):
```
cd mychart/
helm package .
```

Upload `mychart-0.1.0.tgz`:
```bash
curl --data-binary "@mychart-0.1.0.tgz" http://localhost:8080/api/charts
```

If you've signed your package and generated a [provenance file](https://github.com/kubernetes/helm/blob/master/docs/provenance.md), upload it with:
```bash
curl --data-binary "@mychart-0.1.0.tgz.prov" http://localhost:8080/api/prov
```

Both files can also be uploaded at once (or one at a time) on the `/api/charts` route using the `multipart/form-data` format:

```bash
curl -F "chart=@mychart-0.1.0.tgz" -F "prov=@mychart-0.1.0.tgz.prov" http://localhost:8080/api/charts
```

You can also use the [helm-push plugin](https://github.com/chartmuseum/helm-push):
```
helm push mychart/ chartmuseum
```

## Installing Charts into Kubernetes
Add the URL to your *ChartMuseum* installation to the local repository list:
```bash
helm repo add chartmuseum http://localhost:8080
```

Search for charts:
```bash
helm search chartmuseum/
```

Install chart:
```bash
helm install chartmuseum/mychart
```

## How to Run
### CLI
#### Installation
Install the binary:
```bash
# on Linux
curl -LO https://s3.amazonaws.com/chartmuseum/release/latest/bin/linux/amd64/chartmuseum

# on macOS
curl -LO https://s3.amazonaws.com/chartmuseum/release/latest/bin/darwin/amd64/chartmuseum

# on Windows
curl -LO https://s3.amazonaws.com/chartmuseum/release/latest/bin/windows/amd64/chartmuseum

chmod +x ./chartmuseum
mv ./chartmuseum /usr/local/bin
```
Using `latest` in URLs above will get the latest binary (built from master branch).

Replace `latest` with `$(curl -s https://s3.amazonaws.com/chartmuseum/release/stable.txt)` to automatically determine the latest stable release (e.g. `v0.7.0`).

Determine your version with `chartmuseum --version`.

#### Configuration
Show all CLI options with `chartmuseum --help`. Common configurations can be seen below.

All command-line options can be specified as environment variables, which are defined by the command-line option, capitalized, with all `-`'s replaced with `_`'s.

For example, the env var `STORAGE_AMAZON_BUCKET` can be used in place of `--storage-amazon-bucket`.

#### Using with Amazon S3
Make sure your environment is properly setup to access `my-s3-bucket`
```bash
chartmuseum --debug --port=8080 \
  --storage="amazon" \
  --storage-amazon-bucket="my-s3-bucket" \
  --storage-amazon-prefix="" \
  --storage-amazon-region="us-east-1"
```
You need at least the following permissions inside your IAM Policy
```yaml
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowListObjects",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::my-s3-bucket"
    },
    {
      "Sid": "AllowObjectsCRUD",
      "Effect": "Allow",
      "Action": [
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-s3-bucket/*"
    }
  ]
}
```

#### Using with Google Cloud Storage
Make sure your environment is properly setup to access `my-gcs-bucket`
```bash
chartmuseum --debug --port=8080 \
  --storage="google" \
  --storage-google-bucket="my-gcs-bucket" \
  --storage-google-prefix=""
```

#### Using with Microsoft Azure Blob Storage

Make sure your environment is properly setup to access `mycontainer`.

To do so, you must set the following env vars:
- `AZURE_STORAGE_ACCOUNT`
- `AZURE_STORAGE_ACCESS_KEY`

```bash
chartmuseum --debug --port=8080 \
  --storage="microsoft" \
  --storage-microsoft-container="mycontainer" \
  --storage-microsoft-prefix=""
```

#### Using with Alibaba Cloud OSS Storage

Make sure your environment is properly setup to access `my-oss-bucket`.

To do so, you must set the following env vars:
- `ALIBABA_CLOUD_ACCESS_KEY_ID`
- `ALIBABA_CLOUD_ACCESS_KEY_SECRET`

```bash
chartmuseum --debug --port=8080 \
  --storage="alibaba" \
  --storage-alibaba-bucket="my-oss-bucket" \
  --storage-alibaba-prefix="" \
  --storage-alibaba-endpoint="oss-cn-beijing.aliyuncs.com"
```

#### Using with Openstack Object Storage

Make sure your environment is properly setup to access `mycontainer`.

To do so, you must set the following env vars (depending on your openstack version):
- `OS_AUTH_URL`
- either `OS_PROJECT_NAME` or `OS_TENANT_NAME` or `OS_PROJECT_ID` or `OS_TENANT_ID`
- either `OS_DOMAIN_NAME` or `OS_DOMAIN_ID`
- either `OS_USERNAME` or `OS_USERID`
- `OS_PASSWORD`

```bash
chartmuseum --debug --port=8080 \
  --storage="openstack" \
  --storage-openstack-container="mycontainer" \
  --storage-openstack-prefix="" \
  --storage-openstack-region="myregion"
```

#### Using with local filesystem storage
Make sure you have read-write access to `./chartstorage` (will create if doesn't exist on first upload)
```bash
chartmuseum --debug --port=8080 \
  --storage="local" \
  --storage-local-rootdir="./chartstorage"
```

#### Basic Auth
If both of the following options are provided, basic http authentication will protect all routes:
- `--basic-auth-user=<user>` - username for basic http authentication
- `--basic-auth-pass=<pass>` - password for basic http authentication

You may want basic auth to only be applied to operations that can change Charts, i.e. PUT, POST and DELETE.  So to avoid basic auth on GET operations use

- `--auth-anonymous-get` - allow anonymous GET operations

#### HTTPS
If both of the following options are provided, the server will listen and serve HTTPS:
- `--tls-cert=<crt>` - path to tls certificate chain file
- `--tls-key=<key>` - path to tls key file

#### Just generating index.yaml
You can specify the `--gen-index` option if you only wish to use _ChartMuseum_ to generate your index.yaml file. Note that this will only work with `--depth=0`.

The contents of index.yaml will be printed to stdout and the program will exit. This is useful if you are satisfied with your current Helm CI/CD process and/or don't want to monitor another webservice.

#### Other CLI options
- `--log-json` - output structured logs as json
- `--disable-api` - disable all routes prefixed with /api
- `--disable-statefiles` - disable use of index-cache.yaml
- `--allow-overwrite` - allow chart versions to be re-uploaded
- `--chart-url=<url>` - absolute url for .tgzs in index.yaml
- `--storage-amazon-endpoint=<endpoint>` - alternative s3 endpoint
- `--storage-amazon-sse=<algorithm>` - s3 server side encryption algorithm
- `--storage-openstack-cacert=<path>` - path to a custom ca certificates bundle for openstack
- `--chart-post-form-field-name=<field>` - form field which will be queried for the chart file content
- `--prov-post-form-field-name=<field>` - form field which will be queried for the provenance file content
- `--index-limit=<number>` - limit the number of parallel indexers
- `--context-path=<path>` - base context path (new root for application routes)
- `--depth=<number>` - levels of nested repos for multitenancy

### Docker Image
Available via [Docker Hub](https://hub.docker.com/r/chartmuseum/chartmuseum/).

Example usage (S3):
```bash
docker run --rm -it \
  -p 8080:8080 \
  -e PORT=8080 \
  -e DEBUG=1 \
  -e STORAGE="amazon" \
  -e STORAGE_AMAZON_BUCKET="my-s3-bucket" \
  -e STORAGE_AMAZON_PREFIX="" \
  -e STORAGE_AMAZON_REGION="us-east-1" \
  -v ~/.aws:/root/.aws:ro \
  chartmuseum/chartmuseum:latest
```

### Helm Chart
There is a [Helm chart for *ChartMuseum*](https://github.com/kubernetes/charts/tree/master/stable/chartmuseum) itself which can be found in the official Kubernetes Charts repository.

You can also view it on [Kubeapps Hub](https://hub.kubeapps.com/charts/stable/chartmuseum).

To install:
```bash
helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm install stable/chartmuseum
```

If interested in making changes, please submit a PR to kubernetes/charts. Before doing any work, please check for any [currently open pull requests](https://github.com/kubernetes/charts/pulls?q=is%3Apr+is%3Aopen+chartmuseum). Thanks!

## Multitenancy
Multitenancy is supported with the `--depth` flag.

To begin, start with a directory structure such as
```
charts
├── org1
│   ├── repoa
│   │   └── nginx-ingress-0.9.3.tgz
├── org2
│   ├── repob
│   │   └── chartmuseum-0.4.0.tgz
```

This represents a storage layout appropriate for `--depth=2`. The organization level can be eliminated by using `--depth=1`. The default depth is 0 (singletenant server).

Start the server with `--depth=2`, pointing to the `charts/` directory:
```
chartmuseum --debug --depth=2 --storage="local" --storage-local-rootdir=./charts
```

This example will provide two separate Helm Chart Repositories at the following locations:
- `http://localhost:8080/org1/repoa`
- `http://localhost:8080/org2/repob`

This should work with all supported storage backends.

To use the chart manipulation routes, simply place the name of the repo directly after "/api" in the route:

```bash
curl -F "chart=@mychart-0.1.0.tgz" http://localhost:8080/api/org1/repoa/charts
```

## Cache

By default, the contents of `index.yaml` (per-tenant) will be stored in memory. This means that memory usage will continue to grow indefinitely as more charts are added to storage.

You may wish to offload this to an external cache store, especially for large, multitenant installations.

### Using Redis

Example of using Redis as an external cache store:
```bash
chartmuseum --debug --port=8080 \
  --storage="local" \
  --storage-local-rootdir="./chartstorage" \
  --cache="redis" \
  --cache-redis-addr="localhost:6379" \
  --cache-redis-password="" \
  --cache-redis-db=0
```


## Prometheus Metrics

ChartMuseum exposes its [Prometheus metrics](https://prometheus.io/docs/concepts/metric_types/) at the `/metrics` route on the main port. This can be disabled with the `--disable-metrics` command-line flag or the `DISABLE_METRICS` environment variable.

> Note that the Kubernetes chart currently disables metrics by default (`DISABLE_METRICS=true` is set in the chart).

Below are the current application metrics exposed. Note that there is a per tenant (repo) label. The repo label corresponds to the depth parameter, so a depth=2 as the example above would
have repo labels named `org1/repoa` and `org2/repob`.

| Metric                                   | Type           | Labels     | Description                              |
| ---------------------------------------- | -------------- | ---------- | ---------------------------------------- |
| chartmuseum_charts_served_total          | Gauge          | {repo="*"} | Total number of charts                   |
| chartmuseum_charts_versions_served_total | Gauge          | {repo="*"} | Total number of chart versions available |

*: see above for repo label

There are other general global metrics harvested (per process, hence for all tenants). You can get the complete list by using the `/metrics` route.

| Metric                                       | Type    | Labels                                                | Description                               |
| -------------------------------------------- | ------- | ----------------------------------------------------- | ----------------------------------------- |
| chartmuseum_request_duration_seconds         | Summary | {quantile="0.5"}, {quantile="0.9"}, {quantile="0.99"} | The HTTP request latencies in seconds     |
| chartmuseum_request_duration_seconds_sum     |         |                                                       |                                           |
| chartmuseum_request_duration_seconds_count   |         |                                                       |                                           |
| chartmuseum_request_size_bytes               | Summary | {quantile="0.5"}, {quantile="0.9"}, {quantile="0.99"} | The HTTP request sizes in bytes           |
| chartmuseum_request_size_bytes_sum           |         |                                                       |                                           |
| chartmuseum_request_size_bytes_count         |         |                                                       |                                           |
| chartmuseum_response_size_bytes              | Summary | {quantile="0.5"}, {quantile="0.9"}, {quantile="0.99"} | The HTTP response sizes in bytes          |
| chartmuseum_response_size_bytes_sum          |         |                                                       |                                           |
| chartmuseum_response_size_bytes_count        |         |                                                       |                                           |
| go_goroutines                                | Gauge   |                                                       | Number of goroutines that currently exist |


## Notes on index.yaml
The repository index (index.yaml) is dynamically generated based on packages found in storage. If you store your own version of index.yaml, it will be completely ignored.

`GET /index.yaml` occurs when you run `helm repo add chartmuseum http://localhost:8080` or `helm repo update`.

If you manually add/remove a .tgz package from storage, it will be immediately reflected in `GET /index.yaml`.

You are no longer required to maintain your own version of index.yaml using `helm repo index --merge`.

The `--gen-index` CLI option (described above) can be used to generate and print index.yaml to stdout.

Upon index regeneration, *ChartMuseum* will, however, save a statefile in storage called `index-cache.yaml` used for cache optimization. This file is only meant for internal use, but may be able to be used for migration to simple storage.

## Mirroring the official Kubernetes repositories
Please see `scripts/mirror_k8s_repos.sh` for an example of how to download all .tgz packages from the official Kubernetes repositories (both stable and incubator).

You can then use *ChartMuseum* to serve up an internal mirror:
```
scripts/mirror_k8s_repos.sh
chartmuseum --debug --port=8080 --storage="local" --storage-local-rootdir="./mirror"
 ```

## Community
You can reach the *ChartMuseum* community and developers in the [Kubernetes Slack](https://slack.k8s.io) **#chartmuseum** channel.

# ChartMuseum Helm Chart

Deploy your own private ChartMuseum.   

Please also see https://github.com/kubernetes-helm/chartmuseum

## Table of Content

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Prerequisites](#prerequisites)
- [Configuration](#configuration)
- [Installation](#installation)
  - [Using with Amazon S3](#using-with-amazon-s3)
    - [permissions grant with access keys](#permissions-grant-with-access-keys)
    - [permissions grant with IAM instance profile](#permissions-grant-with-iam-instance-profile)
    - [permissions grant with IAM assumed role](#permissions-grant-with-iam-assumed-role)
  - [Using with Google Cloud Storage](#using-with-google-cloud-storage)
  - [Using with Microsoft Azure Blob Storage](#using-with-microsoft-azure-blob-storage)
  - [Using with Alibaba Cloud OSS Storage](#using-with-alibaba-cloud-oss-storage)
  - [Using with local filesystem storage](#using-with-local-filesystem-storage)
    - [Example storage class](#example-storage-class)
- [Uninstall](#uninstall)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
 

## Prerequisites

* Kubernetes with extensions/v1beta1 available
* [If enabled] A persistent storage resource and RW access to it
* [If enabled] Kubernetes StorageClass for dynamic provisioning

## Configuration

By default this chart will not have persistent storage, and the API service
will be *DISABLED*.  This protects against unauthorized access to the API
with default configuration values.

For a more robust solution supply helm install with a custom values.yaml   
You are also required to create the StorageClass resource ahead of time:   
```
kubectl create -f /path/to/storage_class.yaml
```

The following table lists common configurable parameters of the chart and
their default values. See values.yaml for all available options. 

|       Parameter                        |           Description                       |                         Default                     |
|----------------------------------------|---------------------------------------------|-----------------------------------------------------|
| `image.pullPolicy`                     | Container pull policy                       | `IfNotPresent`                                      |
| `image.repository`                     | Container image to use                      | `chartmuseum/chartmuseum`                           |
| `image.tag`                            | Container image tag to deploy               | `v0.7.1`                                            |
| `persistence.accessMode`               | Access mode to use for PVC                  | `ReadWriteOnce`                                     |
| `persistence.enabled`                  | Whether to use a PVC for persistent storage | `false`                                             |
| `persistence.size`                     | Amount of space to claim for PVC            | `8Gi`                                               |
| `persistence.storageClass`             | Storage Class to use for PVC                | `-`                                                 |
| `replicaCount`                         | k8s replicas                                | `1`                                                 |
| `resources.limits.cpu`                 | Container maximum CPU                       | `100m`                                              |
| `resources.limits.memory`              | Container maximum memory                    | `128Mi`                                             |
| `resources.requests.cpu`               | Container requested CPU                     | `80m`                                               |
| `resources.requests.memory`            | Container requested memory                  | `64Mi`                                              |
| `serviceAccount.create`                | If true, create the service account         | `false`                                             |
| `serviceAccount.name`                  | Name of the serviceAccount to create or use | `{{ chartmuseum.fullname }}`                        |
| `securityContext`                      | Map of securityContext for the pod          | `{}`                                                |
| `nodeSelector`                         | Map of node labels for pod assignment       | `{}`                                                |
| `tolerations`                          | List of node taints to tolerate             | `[]`                                                |
| `affinity`                             | Map of node/pod affinities                  | `{}`                                                |
| `env.open.STORAGE`                     | Storage Backend to use                      | `local`                                             |
| `env.open.ALIBABA_BUCKET`              | Bucket to store charts in for Alibaba       | ``                                                  |
| `env.open.ALIBABA_PREFIX`              | Prefix to store charts under for Alibaba    | ``                                                  |
| `env.open.ALIBABA_ENDPOINT`            | Alternative Alibaba endpoint                | ``                                                  |
| `env.open.ALIBABA_SSE`                 | Server side encryption algorithm to use     | ``                                                  |
| `env.open.AMAZON_BUCKET`               | Bucket to store charts in for AWS           | ``                                                  |
| `env.open.AMAZON_ENDPOINT`             | Alternative AWS endpoint                    | ``                                                  |
| `env.open.AMAZON_PREFIX`               | Prefix to store charts under for AWS        | ``                                                  |
| `env.open.AMAZON_REGION`               | Region to use for bucket access for AWS     | ``                                                  |
| `env.open.AMAZON_SSE`                  | Server side encryption algorithm to use     | ``                                                  |
| `env.open.GOOGLE_BUCKET`               | Bucket to store charts in for GCP           | ``                                                  |
| `env.open.GOOGLE_PREFIX`               | Prefix to store charts under for GCP        | ``                                                  |
| `env.open.STORAGE_MICROSOFT_CONTAINER` | Container to store charts under for MS      | ``                                                  |
| `env.open.STORAGE_MICROSOFT_PREFIX`    | Prefix to store charts under for MS         | ``                                                  |
| `env.open.STORAGE_OPENSTACK_CONTAINER` | Container to store charts for openstack     | ``                                                  |
| `env.open.STORAGE_OPENSTACK_PREFIX`    | Prefix to store charts for openstack        | ``                                                  |
| `env.open.STORAGE_OPENSTACK_REGION`    | Region of openstack container               | ``                                                  |
| `env.open.STORAGE_OPENSTACK_CACERT`    | Path to a CA cert bundle for openstack      | ``                                                  |
| `env.open.CHART_POST_FORM_FIELD_NAME`  | Form field to query for chart file content  | ``                                                  |
| `env.open.PROV_POST_FORM_FIELD_NAME`   | Form field to query for chart provenance    | ``                                                  |
| `env.open.DEPTH`                       | levels of nested repos for multitenancy.    | `0`                                                 |
| `env.open.DEBUG`                       | Show debug messages                         | `false`                                             |
| `env.open.LOG_JSON`                    | Output structured logs in JSON              | `true`                                              |
| `env.open.DISABLE_STATEFILES`          | Disable use of index-cache.yaml             | `false`                                             |
| `env.open.DISABLE_METRICS`             | Disable Prometheus metrics                  | `true`                                              |
| `env.open.DISABLE_API`                 | Disable all routes prefixed with /api       | `true`                                              |
| `env.open.ALLOW_OVERWRITE`             | Allow chart versions to be re-uploaded      | `false`                                             |
| `env.open.CHART_URL`                   | Absolute url for .tgzs in index.yaml        | ``                                                  |
| `env.open.AUTH_ANONYMOUS_GET`          | Allow anon GET operations when auth is used | `false`                                             |
| `env.open.CONTEXT_PATH`                | Set the base context path                   | ``                                                  |
| `env.open.INDEX_LIMIT`                 | Parallel scan limit for the repo indexer    | ``                                                  |
| `env.open.CACHE`                       | Cache store, can be one of: redis           | ``                                                  |
| `env.open.CACHE_REDIS_ADDR`            | Address of Redis service (host:port)        | ``                                                  |
| `env.open.CACHE_REDIS_DB`              | Redis database to be selected after connect | `0`                                                 |
| `env.secret.BASIC_AUTH_USER`           | Username for basic HTTP authentication      | ``                                                  |
| `env.secret.BASIC_AUTH_PASS`           | Password for basic HTTP authentication      | ``                                                  |
| `env.secret.CACHE_REDIS_PASSWORD`      | Redis requirepass server configuration      | ``                                                  |
| `gcp.secret.enabled`                   | Flag for the GCP service account            | `false`                                             |
| `gcp.secret.name`                      | Secret name for the GCP json file           | ``                                                  |
| `gcp.secret.key`                       | Secret key for te GCP json file             | `credentials.json`                                  |

Specify each parameter using the `--set key=value[,key=value]` argument to
`helm install`.

## Installation

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

### Using with Amazon S3
Make sure your environment is properly setup to access `my-s3-bucket`

You need at least the following permissions inside your IAM Policy
```yaml
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowListObjects",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::my-s3-bucket"
    },
    {
      "Sid": "AllowObjectsCRUD",
      "Effect": "Allow",
      "Action": [
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::my-s3-bucket/*"
    }
  ]
}
```

You can grant it to `chartmuseum` by several ways:

#### permissions grant with access keys

Grant permissions to `special user` and us it's access keys for auth on aws

Specify `custom.yaml` with such values

```yaml
env:
  open:
    STORAGE: amazon
    STORAGE_AMAZON_BUCKET: my-s3-bucket
    STORAGE_AMAZON_PREFIX:
    STORAGE_AMAZON_REGION: us-east-1
  secret:
    AWS_ACCESS_KEY_ID: "********" ## aws access key id value
    AWS_SECRET_ACCESS_KEY: "********" ## aws access key secret value 
```

Run command to install

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

#### permissions grant with IAM instance profile

You can grant permissions to k8s node IAM instance profile.
For more information read this [article](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

Specify `custom.yaml` with such values

```yaml
env:
  open:
    STORAGE: amazon
    STORAGE_AMAZON_BUCKET: my-s3-bucket
    STORAGE_AMAZON_PREFIX:
    STORAGE_AMAZON_REGION: us-east-1
```

Run command to install

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

#### permissions grant with IAM assumed role

To provide access with assumed role you need to install [kube2iam](https://github.com/kubernetes/charts/tree/master/stable/kube2iam)
and create role with granded permissions.

Specify `custom.yaml` with such values

```yaml
env:
  open:
    STORAGE: amazon
    STORAGE_AMAZON_BUCKET: my-s3-bucket
    STORAGE_AMAZON_PREFIX:
    STORAGE_AMAZON_REGION: us-east-1
replica:
  annotations:
    iam.amazonaws.com/role: "{assumed role name}"
```

Run command to install

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

### Using with Google Cloud Storage
Make sure your environment is properly setup to access `my-gcs-bucket`

Specify `custom.yaml` with such values

```yaml
env:
  open:
    STORAGE: google
    STORAGE_GOOGLE_BUCKET: my-gcs-bucket
    STORAGE_GOOGLE_PREFIX:    
```

### Using with Google Cloud Storage and a Google Service Account

A Google service account credentials are stored in a json file. There are two approaches here. Ideally you don't want to send your secrets to tiller. In that case, before installing this chart, you should create a secret with those credentials:

```shell
kubectl create secret generic chartmuseum-secret --from-file=credentials.json="my-project-45e35d85a593.json"
```

Then you can either use a `VALUES` yaml with your values or set those values in the command line:

```shell
helm install stable/chartmuseum --debug  --set gcp.secret.enabled=true,env.open.STORAGE=google,env.open.DISABLE_API=false,env.open.STORAGE_GOOGLE_BUCKET=my-gcp-chartmuseum,gcp.secret.name=chartmuseum-secret
```

If you prefer to use a yaml file:

```yaml
env:
  open:
    STORAGE: google
    STORAGE_GOOGLE_BUCKET: my-gcs-bucket
    STORAGE_GOOGLE_PREFIX:

gcp:
  secret:
    enabled: true
    name: chartmuseum-secret
    key: credentials.json
```

Run command to install

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

In case that you don't mind adding your secret to tiller (you shouldn't do it), this are the commands

```yaml
env:
  open:
    STORAGE: google
    STORAGE_GOOGLE_BUCKET: my-gcs-bucket
    STORAGE_GOOGLE_PREFIX:
  secret:
    GOOGLE_CREDENTIALS_JSON: my-json-file-base64-encoded
gcp:
  secret:
    enabled: true

```

Run command to install

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

To set the values directly in the command line, use the follosing command. Note that we have to base64 encode the json file because we cannot pass a multi-line text as a value.

```shell
export JSONKEY=$(cat my-project-77e35d85a593.json | base64)
helm install stable/chartmuseum --debug  --set gcp.secret.enabled=true,env.secret.GOOGLE_CREDENTIALS_JSON=${JSONKEY},env.open.STORAGE=google,env.open.DISABLE_API=false,env.open.STORAGE_GOOGLE_BUCKET=my-gcp-chartmuseum
```

### Using with Microsoft Azure Blob Storage

Make sure your environment is properly setup to access `mycontainer`.

To do so, you must set the following env vars:
- `AZURE_STORAGE_ACCOUNT`
- `AZURE_STORAGE_ACCESS_KEY`

Specify `custom.yaml` with such values

```yaml
env:
  open:
    STORAGE: microsoft
    STORAGE_MICROSOFT_CONTAINER: mycontainer
    # prefix to store charts for microsoft storage backend
    STORAGE_MICROSOFT_PREFIX:    
  secret:
    AZURE_STORAGE_ACCOUNT: "********" ## azure storage account
    AZURE_STORAGE_ACCESS_KEY: "********" ## azure storage account access key 
```

Run command to install

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

### Using with Alibaba Cloud OSS Storage

Make sure your environment is properly setup to access `my-oss-bucket`.

To do so, you must set the following env vars:
- `ALIBABA_CLOUD_ACCESS_KEY_ID`
- `ALIBABA_CLOUD_ACCESS_KEY_SECRET`

Specify `custom.yaml` with such values

```yaml
env:
  open:
    STORAGE: alibaba
    STORAGE_ALIBABA_BUCKET: my-oss-bucket
    STORAGE_ALIBABA_PREFIX:
    STORAGE_ALIBABA_ENDPOINT: oss-cn-beijing.aliyuncs.com
  secret:
    ALIBABA_CLOUD_ACCESS_KEY_ID: "********" ## alibaba OSS access key id
    ALIBABA_CLOUD_ACCESS_KEY_SECRET: "********" ## alibaba OSS access key secret 
```

Run command to install

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

### Using with Openstack Object Storage

Make sure your environment is properly setup to access `mycontainer`.

To do so, you must set the following env vars (depending on your openstack version):
- `OS_AUTH_URL`
- either `OS_PROJECT_NAME` or `OS_TENANT_NAME` or `OS_PROJECT_ID` or `OS_TENANT_ID`
- either `OS_DOMAIN_NAME` or `OS_DOMAIN_ID`
- either `OS_USERNAME` or `OS_USERID`
- `OS_PASSWORD`

Specify `custom.yaml` with such values

```yaml
env:
  open:
    STORAGE: openstack
    STORAGE_OPENSTACK_CONTAINER: mycontainer
    STORAGE_OPENSTACK_PREFIX:
    STORAGE_OPENSTACK_REGION: YOURREGION
  secret:
    OS_AUTH_URL: https://myauth.url.com/v2.0/
    OS_TENANT_ID: yourtenantid
    OS_USERNAME: yourusername
    OS_PASSWORD: yourpassword
```

Run command to install

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

### Using with local filesystem storage
By default chartmuseum uses local filesystem storage. 
But on pod recreation it will lose all charts, to prevent that enable persistent storage. 

```yaml
env:
  open:
    STORAGE: local
persistence:
  enabled: true
  accessMode: ReadWriteOnce
  size: 8Gi
  ## A manually managed Persistent Volume and Claim
  ## Requires persistence.enabled: true
  ## If defined, PVC must be created manually before volume will be bound
  # existingClaim:

  ## Chartmuseum data Persistent Volume Storage Class
  ## If defined, storageClassName: <storageClass>
  ## If set to "-", storageClassName: "", which disables dynamic provisioning
  ## If undefined (the default) or set to null, no storageClassName spec is
  ##   set, choosing the default provisioner.  (gp2 on AWS, standard on
  ##   GKE, AWS & OpenStack)
  ##
  # storageClass: "-"
```

Run command to install

```shell
helm install --name my-chartmuseum -f custom.yaml stable/chartmuseum
```

#### Example storage class

Example storage-class.yaml provided here for use with a Ceph cluster.   

```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: storage-volume
provisioner: kubernetes.io/rbd
parameters:
  monitors: "10.11.12.13:4567,10.11.12.14:4567"
  adminId: admin
  adminSecretName: thesecret
  adminSecretNamespace: default
  pool: chartstore
  userId: user
  userSecretName: thesecret 
```

## Uninstall 

By default, a deliberate uninstall will result in the persistent volume 
claim being deleted.   

```shell
helm delete my-chartmuseum
```

To delete the deployment and its history:
```shell
helm delete --purge my-chartmuseum
```
Loadtesting is made with the excellent Python [locust](https://locust.io/) library.

To facilitate installation, this loadtesting subproject uses pipenv.

Install pipenv

```
pip install pipenv
```

Install chartmuseum locust loadtesting

```
cd loadtesting
pipenv install
```

Start chartmuseum.

Start locust:

```
# run locust on a running chartmuseum instance
pipenv run locust --host http://localhost:8080
```

Open your locust console in your browser at http://localhost:8089, and start a new loadtest.
