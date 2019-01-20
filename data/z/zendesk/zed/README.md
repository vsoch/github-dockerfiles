# Command line tool for Zendesk

[![Build Status](https://travis-ci.org/zendesk/zed.svg?branch=master)](https://travis-ci.org/zendesk/zed)

Zendesk Draft ( known as zed )  makes it easier for developers to build applications that run on Kubernetes. It provides the skeleton project that can be deployed on Kubernetes.

## Install the draft binary

```
git clone git@github.com:zendesk/zed.git

cd zed/cmd/zed

go build

```
## Take Zed for a Spin 

```
./zed help

./zed create -a test-application -k ruby-worker -t compute

```

## _NOTE: Draft is experimental and does not have a stable release yet._

