# k8ecr

Utility for managing ecr repositories with kubernetes

## Building

If you don't already have `dep` installed go get it from the releases page:

    https://github.com/golang/dep/releases

And put it in your path.

Then:

    dep ensure

To install the dependencies into the vendor/ folder.

## Concepts

k8ecr provides tooling to make it easier to use docker images from ECR repositories in your Kubernetes clusters created by kops. In particular it understands the link between an AWS account and role (i.e. an AWS profile) and a Kubernetes context.

It can:

- create ECR repositories and grant appropriate permissions to your cluster roles.
- push images to ECR repositories directly.
- issue appropriate kubectl set image commands to update deployments.

## Usage

    k8ecr config PROFILE
    k8ecr create REPOSITORY
    k8ecr push REPOSITORY VERSION...
    k8ecr deploy

## Configuration

    k8ecr config PROFILE

This will link the current kubectl context to the specified AWS profile.

This writes to the YAML config file ~/.k8ecr

From now on the current kubectl context will be used to determine which AWS profile to use for AWS API calls.

## Creating repositories

    k8ecr create REPOSITORY

This will create an ECR repository in the current profile, and grant:

    ecr:GetDownloadUrlForLayer
    ecr:BatchGetImage
    ecr:BatchCheckLayerAvailability

To the IAM master and nodes role for the current cluster.

## Pushing images

    k8ecr push REPOSITORY VERSION...

This will log in to ECR, then push images to the remote repository with the specified versions.  For example:

    k8ecr push myimage 1.0.0 latest

Will push 1.0.0 and latest tags.

## Deploying

    k8ecr deploy [NAMESPACE]

This will compare all deployments and the must recent version numbers available and present options for deploying images.

All possible upgrade options for the specified namespace are shown.
