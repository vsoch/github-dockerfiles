# Koki Short

<img src="https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiaFdaQUJleFNQRkI3NXdKcllWSVJ0THREYkl2WEJBTkZCRkhrWERoeUYxbjFsUTZNSEZ4WGxWZnNmcWxvenlMallELytyNTI0VSsxZ0JEV3FrOS9JYzVzPSIsIml2UGFyYW1ldGVyU3BlYyI6InFKYXBITkJ0Z3NsTkhWN0UiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master"/>

Manageable Kubernetes manifests through composable, reusable syntax

## Motivation
The description format for Kubernetes manifests, as it stands today, is verbose and unintuitive. Anecdotally, it has been:

 - Time consuming to write
 - Error-prone, hard to get right without referring to documentation
 - Difficult to maintain, read, and reuse

e.g. In order to create a simple nginx pod that runs on any host in region `us-east1` or `us-east2`, here is the Kubernetes native syntax:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  containers:
  - name: nginx_container
    image: nginx:latest
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      	nodeSelectorTerms:
        - matchExpressions:
          - key: k8s.io/failure-domain
            operator: In
            values: 
            - us-east1
        - matchExpressions:
          - key: k8s.io/failure-domain
            operator: In
            value:
            - us-east2
```

The Short format is designed to be user friendly, intuitive, reusable, and maintainable. The same pod in Short syntax looks like

```yaml
pod:
  name: nginx
  labels:
    app: nginx
  containers:
  - name: nginx
    image: nginx:latest
  affinity:
  - node: k8s.io/failure-domain=us-east1,us-east2
```

Our approach is to reframe Kubernetes manifests in an operator-friendly syntax without sacrificing expressiveness.

Koki Short can transform Kubernetes syntax into Short and Short syntax back into Kubernetes. No information is lost in either direction.

For more information on Koki Short transformations, please refer to [Resources.](https://docs.koki.io/short/resources)

## Modular and Reusable

Koki Short introduces the concept of modules, which are reusable collections of Short resources. Any resource can be reused multiple times in other resources and linked resources can be managed as a single unit on the Koki platform. 

Any valid koki resource object can be reused. This includes subtypes of top-level resource types. For example, here's module called `pod-affinity-us-east-1.yaml`:

```yaml
exports:
- default: node affinity for us-east-1
  value:
  - node: k8s.io/failure-domain=us-east-1
```

This affinity value can be reused in any pod spec:

```yaml
imports:
- affinity: pod-affinity-us-east-1.yaml
exports:
- default: an nginx pod
  value:
    pod:
      name: nginx
      labels:
        app: nginx
      containers:
      - name: nginx
        image: nginx-latest
      affinity: ${affinity}  # re-use the affinity resource here
```

For more information on Koki Modules, please refer to [Modules.](https://docs.koki.io/short/modules)

## Getting started

In order to start using Short, simply download the binary from the [releases page](https://github.com/koki/short/releases).

```sh

#start with any existing Kubernetes manifest file
$$ cat kube_manifest.yaml
apiVersion: v1
kind: Pod
metadata:
  name: podName
  namespace: podNamespace
spec:
  hostAliases:
   - ip: 127.0.0.1
     hostnames:
      - localhost
      - myMachine
  affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
     - matchExpressions:
        - key: k8s.io/failure-domain
          operator: In
          value: us-east1
  containers:
   - name: container
     image: busybox:latest
     ports:
      - containerPort: 6379
        hostPort: 8080
        name: service
        protocol: TCP
     resources:
        limits:
          cpu: "2"
          memory: 1024m
        requests:
          cpu: "1"
          memory: 512m

     
#convert Kubernetes manifest into a Short syntax representation
$$ short -f kube_manifest.yaml
pod:
  name: podName
  namespace: podNamespace
  affinity:
   - node: k8s.io/failure-domain=us-east1
  host_aliases:
   - 127.0.0.1 localhost myMachine
  containers:
   - image: busybox
     cpu:
       min: "1"
       max: "2"
     mem:
       min: "512m"
       max: "1024m"
     expose:
      - port_map: "8080:6379"
        name: service


#input can be json or yaml
$$ short -f kube_manifest.json -f kube_manifest2.yaml -f kube_multi_manifest.yaml

#stream input
$$ cat kube_manifest.yaml | short -

#revert to kubernetes type
$$ short -k -f koki_spec.yaml

#-k flag denotes that it should output Kubernetes manifest

```

For more information, refer to our [getting started guide.](https://docs.koki.io/user-guide#getting-started)

## Contribute
Koki is completely open source community driven, including the roadmaps, planning, and implementation. We encourage everyone to help us make Kubernetes manifests more manageable. We welcome Issues, Pull Requests and participation in our [weekly meetings]().

If you'd like to get started with contributing to Koki Short, read our [Roadmap](https://github.com/koki/short/projects) and start with any issue labelled `help-wanted` or `good-first-issue`

## Important Links

- [Releases](https://github.com/koki/short/releases)
- [Docs](https://docs.koki.io/short)
- [Roadmap](https://github.com/koki/short/tree/master/releases/ROADMAP.md)
- [Issues](https://github.com/koki/short/issues)

## LICENSE
[Apache v2.0](https://github.com/koki/short/blob/master/LICENSE)
# YAML marshaling and unmarshaling support for Go

[![Build Status](https://travis-ci.org/ghodss/yaml.svg)](https://travis-ci.org/ghodss/yaml)

## Introduction

A wrapper around [go-yaml](https://github.com/go-yaml/yaml) designed to enable a better way of handling YAML when marshaling to and from structs.

In short, this library first converts YAML to JSON using go-yaml and then uses `json.Marshal` and `json.Unmarshal` to convert to or from the struct. This means that it effectively reuses the JSON struct tags as well as the custom JSON methods `MarshalJSON` and `UnmarshalJSON` unlike go-yaml. For a detailed overview of the rationale behind this method, [see this blog post](http://ghodss.com/2014/the-right-way-to-handle-yaml-in-golang/).

## Compatibility

This package uses [go-yaml](https://github.com/go-yaml/yaml) and therefore supports [everything go-yaml supports](https://github.com/go-yaml/yaml#compatibility).

## Caveats

**Caveat #1:** When using `yaml.Marshal` and `yaml.Unmarshal`, binary data should NOT be preceded with the `!!binary` YAML tag. If you do, go-yaml will convert the binary data from base64 to native binary data, which is not compatible with JSON. You can still use binary in your YAML files though - just store them without the `!!binary` tag and decode the base64 in your code (e.g. in the custom JSON methods `MarshalJSON` and `UnmarshalJSON`). This also has the benefit that your YAML and your JSON binary data will be decoded exactly the same way. As an example:

```
BAD:
	exampleKey: !!binary gIGC

GOOD:
	exampleKey: gIGC
... and decode the base64 data in your code.
```

**Caveat #2:** When using `YAMLToJSON` directly, maps with keys that are maps will result in an error since this is not supported by JSON. This error will occur in `Unmarshal` as well since you can't unmarshal map keys anyways since struct fields can't be keys.

## Installation and usage

To install, run:

```
$ go get github.com/ghodss/yaml
```

And import using:

```
import "github.com/ghodss/yaml"
```

Usage is very similar to the JSON library:

```go
package main

import (
	"fmt"

	"github.com/ghodss/yaml"
)

type Person struct {
	Name string `json:"name"` // Affects YAML field names too.
	Age  int    `json:"age"`
}

func main() {
	// Marshal a Person struct to YAML.
	p := Person{"John", 30}
	y, err := yaml.Marshal(p)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(string(y))
	/* Output:
	age: 30
	name: John
	*/

	// Unmarshal the YAML back into a Person struct.
	var p2 Person
	err = yaml.Unmarshal(y, &p2)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(p2)
	/* Output:
	{John 30}
	*/
}
```

`yaml.YAMLToJSON` and `yaml.JSONToYAML` methods are also available:

```go
package main

import (
	"fmt"

	"github.com/ghodss/yaml"
)

func main() {
	j := []byte(`{"name": "John", "age": 30}`)
	y, err := yaml.JSONToYAML(j)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(string(y))
	/* Output:
	name: John
	age: 30
	*/
	j2, err := yaml.YAMLToJSON(y)
	if err != nil {
		fmt.Printf("err: %v\n", err)
		return
	}
	fmt.Println(string(j2))
	/* Output:
	{"age":30,"name":"John"}
	*/
}
```
