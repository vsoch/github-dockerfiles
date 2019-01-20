# "API-Operator" Project main repository

This is not a supported/official redhat product.

## Deployment

* To learn how to deploy openshift locally:

<https://github.com/openshift/origin/blob/master/docs/cluster_up_down.md>

* Clone the repo:

```
git clone https://github.com/3scale/api-operator.git
cd api-operator
```

* At the cluster scope, create the Custom Resource Definition (requires `cluster-admin` role):

```
oc login -u system:admin
oc create -f api-operator/deploy/crd.yaml
```

* Create the RBAC (requires `cluster-admin` role). Deploy the operator into the namespace where you wish to manage your API:

```
oc new-project my-hello-api
oc create -f api-operator/deploy/rbac.yaml
oc create -f api-operator/deploy/operator.yaml
```

* Within the same namespace as the operator, deploy the example Custom Resource:

```
oc create -f api-operator/deploy/cr.yaml -n my-hello-api
```

## Build

* Prerequisites:
  * Go >= 1.10
  * Go Dep (<https://github.com/golang/dep>)
  * Operator-SDK v0.0.5 (<https://github.com/operator-framework/operator-sdk>)
  * Docker

* Installing Go:

Please refer to the official docs: <https://golang.org/doc/install>

* Installing Go Dep:

Mac:

```
brew install dep
```

Other Platforms:

```
curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
```

* Get the API Operator code

```
go get github.com/3scale/api-operator
```

* Run dep ensure

```
cd ${GOPATH}/src/github.com/3scale/api-operator
dep ensure -v
```

* Install operator-framework from vendored sources

```
go install ./vendor/github.com/operator-framework/operator-sdk/commands/operator-sdk
```

Make sure ${GOPATH}/bin is added to your PATH

* Build

```
operator-sdk build yourregistry/imagename:version
```

* Push

```
docker push yourregistry/imagename:version
```