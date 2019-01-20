# mySociety Public Builds

This repository contains shared recipes for building our software and
dependencies in various formats and environments. With some adjustment,
re-users should be able to use these to create custom builds of their
own.

## Usage

Each subdirectory is named for the tool used for the build process, so
in order to use these you'll need to be at least broadly familiar with
these and have them installed locally.

Running `script/bootstrap` will check for current dependencies and download any
required assets (such as a Debian ISO for the Vagrant build, see below).

### Docker

Where a project supports Docker, we'll include the relevant `Dockerfile`
in the project repository rather than here. The Docker builds in this
repository will generally be dependencies and shared containers used in
our example Docker Compose environments.

### Packer

We're using [Packer](https://www.packer.io/) to build AMIs and Vagrant boxes.
The `packer/` directory contains a `Makefile` that documents how we produce our
supported images.

The builds use Debian Stretch; the Amazon build will use the most recent official
Debian AMI as a basis and the Vagrant build expects a copy of the Debian Stretch
network installation ISO to be present in `packer/iso` - as noted above, the
required file can be downloaded by running `script/bootstrap`.

### Standard Builds

Our standard builder definitions can be found in `packer/builders`. These are
intended to be able to build various different mySociety applications using
overrides set in files under `packer/vars` names for the application in question,
for example `vars/fixmystreet.json`.

We currently provide the following example build recipes:

* FixMyStreet full AMI - this contains everything needed to run an instance
  of FixMyStreet, including a local Postgres database, nginx reverse proxy and memcached.

* FixMyStreet Vagrant box - this is a simple box with our current dependencies (including
  Perl modules) pre-installed. This is intended for use with the `Vagrantfile` supplied
  in [the FixMyStreet repository](https://github.com/mysociety/fixmystreet).

### Custom Builds

Should you wish to build your own images based on the recipes here, this should be
possible without having to make significant changes. You'll need to provide your
own AWS credentials, the builder expects `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
environment variables.

#### Controlling the availability of images

The AMI builder sets `ami_groups` to `all`, this means that any AMIs built as-is
**will be public** - if you want to build a private image, remove this line from
`packer/builders/amazon.json`.

#### Setting the AWS region

Currently the builds default to using the `eu-west-1` region, to override this
pass a `-var` option when you run the build, for example `-var 'region=us-east-1'`.

#### Configuring a particular build or instance

First, note the comments above about AMIs being **publicly available** by default, so
take care about adding secrets to any images.

See the following documents for more information on customising builds for
specific services:

* [FixMyStreet](/docs/fixmystreet.md)
