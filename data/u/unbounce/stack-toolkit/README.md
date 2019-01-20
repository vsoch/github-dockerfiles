# stack-toolkit

A collection of CLI tools for use with AWS stack deployed services.

## Download

Download the latest binaries from the [Releases](https://github.com/unbounce/stack-toolkit/releases) page on this repository.  Choose the correct distribution that suits the platform where the commands will be run.

## Installation

### Binary Installation

Unzip the tar.gz file onto your local system, somewhere that the `PATH` environment variable can reach.  If unsure, run `which stacks` and it should return the path to the command.  If nothing is returned, then the files are not installed where `PATH` can see them.

### Source Installation

1. Ensure your system is setup for Go development.
1. Run `go get github.com/aws/aws-sdk-go`.
1. Run `git clone git@github.com:unbounce/stack-toolkit.git $GOPATH/src/github.com/unbounce/stack-toolkit`
1. Run `make` in the stack-toolkit directory to compile the binaries in this project.

## Authentication

Commands will never ask you for your AWS credentials.  Your credentials are assumed to be loaded as environment variables as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

## Commands

`stacks REGION`

This command lists the active CloudFormation stacks in a given `REGION`.

`stack-instances STACK_NAME REGION`

This command lists the EC2 instances that belong to a given `STACK_NAME` within a given `REGION`.

## Fun Stuff

The output from the commands can be combined with other Unix/Linux utilities to form a workflow.

### Example 1: Finding a specific group of stacks

Provide an alphabetically sorted list of stacks labeled "production" from the us-east-1 AWS region.

```
$ stacks us-east-1 | grep production | sort
```

### Example 2: SSHing into an instance

Provide the `ssh` command with one EC2 public DNS name, retrieved from the example-stack in us-east-1.  The `head -1` ensures that only one result is returned (in the case of instances behind an autoscaling group).

```
$ ssh $(stack-instances example-stack us-east-1 | head -1)
```

