# Helloservice

A RESTful API example for simple helloservice application with Go.

![Helloservice!](img/GO-GKE.png)

## API Endpoint
- http://helloservice.example.com/hello:name
    - `GET`: responds with Hello,< name >!
- http://helloservice.example.com/health
    - `GET`: responds with system stats
- http://helloservice.example.com/counts
    - `GET`: returns a JSON response with the counts of how many times each name has been called
    - `DELETE`: remove counts 

## Assumptions
- Application:
    - Assuming there is no DB involved and only will be keeping count of names during single runtime.
- Deployment(GKE):
    - Using n1-standard-1 machine type in GKE.
    - Application will be deployed in us-east1-c zone.

## Structure
```
├── pkg
│   ├── hello          
│   │   ├── hello.go          // APIs for hello
│   │   └── hello_test.go     
│   ├── health
│   │   ├── health.go        // APIs for health
│   │   └── health_test.go 
│   └── counts
│       ├── counts.go        // APIs for getting counts
│       └── counts_test.go 
├── helm-chart              // Helm chart(Kubernetes Package Manager for deploying helloservice in cluster)
│   └── helloservice
│       ├── templates
│       │     ├── deployment.yaml
│       │     ├── ingress.yaml
│       │     └── service.yaml 
│       ├── Chart.yaml
│       └── values.yaml       
└── main.go
```

The following repository will create you a Kubernetes cluster using:

1. [GKE](https://console.cloud.google.com) for the underlying infrastructure.

## What is setup? 
 
 This repository setup the following:
 
 - 2 Worker nodes

## Prerequisites

A list of prerequisities for Mac can be found [here](docs/1.mac-prerequisites.md)

A list of prerequisities for Windows can be found [here](docs/2.windows-prerequisites.md)

## Cluster creation

A list of steps to build and provision the Kubernetes cluster can be found [here](docs/3.create-cluster.md)

## Helloservice Helm chart deployment

A list of steps to deploy the necessary Helm charts can be found [here](docs/4.deploy-helloservice.md)

## Cleanup (from your local machine)

To remove the worker node from Google Kubernetes Engine execute the following:

```
$ make destroy-cluster
```