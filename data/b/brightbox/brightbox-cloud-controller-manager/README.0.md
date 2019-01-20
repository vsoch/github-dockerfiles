# Running the Cloud Controller on a Cluster

## Intro
As well as directly in the master node, the cloud controller can be run
as a Daemonset within the `kube-system` namespace.

The [YAML file](cloud-controller.yml) within this directory is the latest recommended
configuration to use on Kubernetes.

By far the easiest way to get the Brightbox cloud controller running on
a k8s cluster is to [create a new one](https://www.brightbox.com/docs/guides/kubernetes/deploy-kubernetes-on-brightbox-cloud/).

## Create Secrets
To use the configuration, first create a secret config map containing
the Brightbox credentials. You can get a
[suitable api client from the Brightbox Manager](https://www.brightbox.com/docs/guides/manager/api-clients/)

```
$ kubectl -n kube-system create secret generic brightbox-cloud-controller \
    '--from-literal=controller-client=cli-xxxxx' \
    '--from-literal=controller-client-secret=my_secret' \
    '--from-literal=apiurl=https://api.gb1.brightbox.com'
```

## Running the config
- Ensure your cluster is running with the [cloud provider switches set to external](https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/#administration)
- Put the YAML file somewhere where kubectl can see it.
- Edit the file and make sure that the server path in `cloud-controller.conf` points to your k8s apiserver, and the version number of the cloud-controller docker image is what you want to run
- Run `kubectl apply -f <your_file_path>.yml`

This will run the cloud-controller on all your master nodes, with one
of them electing itself as the leader.
