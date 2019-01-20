# yFuzz

[![Build Status](https://travis-ci.org/yahoo/yfuzz.svg?branch=master)](https://travis-ci.org/yahoo/yfuzz) ![godoc](https://godoc.org/github.com/yahoo/yfuzz?status.svg)

yFuzz is a project for running fuzzing jobs at scale with Kubernetes.

**This project is still in alpha. While in alpha, the API may be subject to breaking changes.**

## Table of Contents

- [yFuzz](#yfuzz)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Projects](#projects)
  - [Architecture](#architecture)
  - [Directory Structure](#directory-structure)
  - [Contribute](#contribute)
  - [License](#license)

## Background

Popular fuzzers such as [Libfuzzer](https://llvm.org/docs/LibFuzzer.html) and [AFL](http://lcamtuf.coredump.cx/afl/) have support for running multiple fuzzing processes at once. yFuzz aims to take advantage of this by running each process on a different Kubernetes pod to speed up the fuzzing process.

For open-source projects, this can be done with [OSS-Fuzz](https://github.com/google/oss-fuzz), with some restrictions:
* The targeted project must be open-source
* The targeted project must have a significant user base, or be critical to the global IT infrastructure

yFuzz aims to be an on-premises solution for distributed fuzzing, so that projects that don't meet these constraints can still be fuzzed.

Additional features to make the fuzzing process easier are also planned, such as automatic generation/suggestion of fuzz targets. We welcome all feedback and suggestions as we consider other use-cases.

## Projects
* [yFuzz Server](services/yfuzz-server): The main API server for yFuzz.
* [yFuzz CLI](cmd/yfuzz-cli): A command-line interface for interacting with the yFuzz server.
* [yFuzz Scripts](images/scripts): Docker image with scripts used by yFuzz containers.

## Architecture
![Architecture Diagram](architecture.png)

The yFuzz API resides in a kubernetes cluster along with the pods that run the fuzzing jobs and a shared volume that holds corpus data to be shared between the pods.

## Directory Structure
* `cmd`: Command line utilities.
* `docs`: Documentation relating to yFuzz.
* `images`: Dockerfiles used by yFuzz.
* `pkg`: Shared libraries and packages.
* `scripts`: Scripts for CI tooling.
* `services`: Long-running services, such as the yfuzz-server.

## Contribute

Please refer to [the contributing.md file](CONTRIBUTING.md) for information about how to get involved. We welcome issues, questions, and pull requests. Pull Requests are welcome

## License
This project is licensed under the terms of the [Apache 2.0](LICENSE) open source license.
