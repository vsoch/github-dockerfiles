= THIS RECIPE
* is for testing CookbookLoader/CookbookVersion
* has at least one of every kind of file that cookbooks can have# name-mismatch

TODO: Enter the cookbook description here.

# invalid-metadata

TODO: Enter the cookbook description here.

# incomplete-metadata

TODO: Enter the cookbook description here.

This directory contains bootstrap templates which can be used with the -d flag
to 'knife bootstrap' to install Chef in different ways. To simplify installation,
and reduce the matrix of common installation patterns to support, we have
standardized on the [Omnibus](https://github.com/chef/omnibus) built installation
packages.

The 'chef-full' template downloads a script which is used to determine the correct
Omnibus package for this system from the [Omnitruck](https://docs.chef.io/api_omnitruck.html) API.

You can still utilize custom bootstrap templates on your system if your installation
needs are unique. Additional information can be found on the [docs site](https://docs.chef.io/knife_bootstrap.html#custom-templates).
# End-To-End Testing for Chef Client

Here we seek to provide end-to-end testing of Chef Client through cookbooks which exercise many of the available resources, providers, and common patterns. The cookbooks here are designed to ensure certain capabilities remain functional with updates to the client code base.

## Getting started

All the gems needed to run these tests can be installed with Bundler.

```shell
chef/kitchen-tests$ bundle install
```

To ensure everything is working properly, and to see which platforms can have tests executed on them, run

```shell
chef/kitchen-tests$ bundle exec kitchen list
```

You should see output similar to

```shell
Instance                     Driver   Provisioner  Verifier  Transport  Last Action    Last Error
end-to-end-amazonlinux       Vagrant  ChefGithub   Inspec    Ssh        <Not Created>  <None>
```

## Testing

We use Test Kitchen to build instances, test client code, and destroy instances. If you are unfamiliar with Test Kitchen we recommend checking out the [tutorial](http://kitchen.ci/) along with the `kitchen-vagrant` [driver documentation](https://github.com/test-kitchen/kitchen-vagrant). Test Kitchen is configured to manipulate instances using [Vagrant](https://www.vagrantup.com/) when testing locally, and Docker via [kitchen-dokken](https://github.com/someara/kitchen-dokken/) when testing pull requests on [Travis CI](https://travis-ci.com/).

### Commands

Kitchen instances are led through a series of states. The instance states, and the actions taken to transition into each state, are in order:

- `destroy`: Delete all information for and terminate one or more instances. 
	- This is equivalent to running `vagrant destroy` to stop and delete a Vagrant machine.
- `create`: Start one or more instances. 
	- This is equivalent to running `vagrant up --no-provision` to start a Vagrant instance.
- `converge`: Use a provisioner to configure one or more instances.
  - By default, Test Kitchen is configured to use the `ChefSolo` provisioner which:
    - Prepares local files for transfer,
    - Installs the latest release of Chef Omnibus,
    - Downloads Chef Client source code from the prescribed GitHub repository and reference,
    - Builds and installs a `chef` gem from the downloaded source,
    - Runs `chef-client`.
- `setup`: Prepare the instance to run automated tests.
- `verify`: Run automated tests on one or more instances.

When transitioning between states, actions for any and all intermediate states will performed. Executing the `create` then the `verify` commands is equivalent to executing `create`, `converge`, `setup`, and `verify` one-by-one and in order. The only exception is `destroy`, which will immediately transfer that machine's state to destroyed.

The `test` command takes one or more instances through all the states, in order: `destroy`, `create`, `converge`, `setup`, `verify`, `destroy`.

To see a list of available commands, type `bundle exec kitchen help`. To see more information about a particular command, type `bundle exec kitchen help <command>`.

### Configuring your tests

Test Kitchen is configured for local testing in the `kitchen.yml` file which resides in this directory. You will need to configure the provisioner before running the tests.

The provisioner can be configured to pull client source code from a GitHub repository using any valid Git reference. You are encouraged to modify any of these settings, but please return them to their original values before submitting a pull request for review (unless, of course, your changes are enhancements to the default provisioner settings).

By default, the provisioner is configured to pull your most recent commit to `chef/chef`. You can change this by modifying the `github` and `branch` provisioner options:

- `github`: Set this to `"<your_username>/<your_chef_repo>"`. The default is `"chef/chef"`.
- `branch`: This can be any valid git reference (e.g., branch name, tag, or commit SHA). If omitted, it defaults to `master`.

The branch you choose must be accessible on GitHub. You cannot use a local commit at this time.

### Testing pull requests

These end-to-end tests are also configured to run on Travis-CI with docker containers when you submit a pull request to `chef/chef`. Kitchen is configured to pull chef client source code from the branch it is testing. There is no need to modify `kitchen.travis.yml` unless you are contributing tests.

## Contributing

We would love to fill out our end-to-end testing coverage! If you have cookbooks and tests that you would like to see become a part of client testing, we encourage you to submit a pull request with your additions. We request that you do not add platforms to `kitchen.travis.yml`. Please file a request to add a platform under [Issues](https://github.com/chef/chef/issues).
# end_to_end

A standard chef "base" cookbook that performs various base system configuration tasks using common community cookbooks.
# Client Tools Omnibus project

This project creates full-stack platform-specific packages for the following projects:

- AngryChef
- Chef
- Chef with FIPS enabled

## Installation

You must have a sane Ruby environment with Bundler installed. Ensure all the required gems are installed:

```shell
$ bundle install --without development
```

## Usage

### Build

You create a platform-specific package using the `build project` command:

```shell
$ bundle exec omnibus build <PROJECT>
```

The platform/architecture type of the package created will match the platform where the `build project` command is invoked. For example, running this command on a MacBook Pro will generate a Mac OS X package. After the build completes packages will be available in the `pkg/` folder.

### Clean

You can clean up all temporary files generated during the build process with the `clean` command:

```shell
$ bundle exec omnibus clean <PROJECT>
```

Adding the `--purge` purge option removes **ALL** files generated during the build including the project install directory (`/opt/chef`) and the package cache directory (`/var/cache/omnibus/pkg`):

```shell
$ bundle exec omnibus clean <PROJECT> --purge
```

### Publish

Omnibus has a built-in mechanism for releasing to a variety of "backends", such as Amazon S3 and Artifactory. You must set the proper credentials in your `omnibus.rb` config file or specify them via the command line.

```shell
$ bundle exec omnibus publish path/to/*.deb --backend s3
```

### Help

Full help for the Omnibus command line interface can be accessed with the `help` command:

```shell
$ bundle exec omnibus help
```

## Kitchen-based Build Environment

Every Omnibus project ships will a project-specific [Berksfile](https://docs.chef.io/berkshelf.html) that will allow you to build your omnibus projects on all of the projects listed in the `kitchen.yml`. You can add/remove additional platforms as needed by changing the list found in the `kitchen.yml` `platforms` YAML stanza.

This build environment is designed to get you up-and-running quickly. However, there is nothing that restricts you to building on other platforms. Simply use the [omnibus cookbook](https://github.com/chef-cookbooks/omnibus) to setup your desired platform and execute the build steps listed above.

The default build environment requires Test Kitchen and VirtualBox for local development. Test Kitchen also exposes the ability to provision instances using various cloud providers like AWS, DigitalOcean, or OpenStack. For more information, please see the [Test Kitchen documentation](http://kitchen.ci).

Once you have tweaked your `kitchen.yml` (or `kitchen.local.yml`) to your liking, you can bring up an individual build environment using the `kitchen` command.

```shell
$ bundle exec kitchen converge chef-ubuntu-1404
```

Additional settings are required if using the kitchen-vagrant driver with the Hyper-V provider:

```
PS> $env:KITCHEN_LOCAL_YAML="kitchen.hyperv.yml"; kitchen converge chef-windows-server-2012r2-standard
```

Then login to the instance and build the project as described in the Usage section:

```shell
$ bundle exec kitchen login <PROJECT>-ubuntu-1204
[vagrant@ubuntu...] $ cd chef/omnibus
[vagrant@ubuntu...] $ bundle install --without development # Don't install dev tools!
[vagrant@ubuntu...] $ ...
[vagrant@ubuntu...] $ bundle exec omnibus build <PROJECT> -l internal
```

```shell
$ kitchen login chef-ubuntu-1404
[vagrant@ubuntu...] $ source load-omnibus-toolchain.sh
[vagrant@ubuntu...] $ cd chef/omnibus
[vagrant@ubuntu...] $ bundle install --without development # Don't install dev tools!
[vagrant@ubuntu...] $ ...
[vagrant@ubuntu...] $ bundle exec omnibus build chef -l internal
```

You can also login to Windows instances but will have to manually call the `load-omnibus-toolchain.ps1` script from an administrative PowerShell session which initializes the build environment. You will also need to `git clone https://github.com/chef/chef` into the `c:\vagrant` folder to workaround the lack of a shared folder.

```shell
$ bundle exec kitchen login <PROJECT>-windows-81-professional
Last login: Sat Sep 13 10:19:04 2014 from 172.16.27.1
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\>C:\vagrant\load-omnibus-toolchain.ps1

C:\>cd C:\vagrant\chef\omnibus

C:\vagrant\chef\omnibus>bundle install --without development

C:\vagrant\chef\omnibus>bundle exec omnibus build chef -l internal
```

For a complete list of all commands and platforms, run `kitchen list` or `kitchen help`.

## License

```text
Copyright 2012-2018, Chef Software, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
