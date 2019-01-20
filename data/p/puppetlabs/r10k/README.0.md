Integration Tests
===========================

This folder contains integration tests for the r10k project. These tests were originally written by the QA team
at Puppet Labs and is actively maintained by the QA team. Feel free to contribute tests to this folder as long
as they are written with [Beaker](https://github.com/puppetlabs/beaker) and follow the guidelines
below.

## Integration?

The r10k project already contains RSpec tests and you might be wondering why there is a need to have a set of
tests separate from those tests. At Puppet Labs we define an "integration" test as:

> Validating the system state and/or side effects while completing a complete life cycle of user stories using a
> system. This type of test crosses the boundary of a discrete tool in the process of testing a defined user
> objective that utilizes a system composed of integrated components.

What this means for this project is that we will install and configure all infrastructure needed in a real-world
r10k environment.

## Running Tests

Included in this folder under the "test_run_scripts" sub-folder are simple Bash scripts that will run suites of
Beaker tests. This scripts utilize environment variables for specifying test infrastructure. For security
reasons we do not provide examples from the Puppet Labs testing environment.

## Documentation

Each sub-folder contains a "README.mdk" that describes the content found in the sub-folder.
Scripts
=======

This folder contains helper scripts for setting up manual testing environments
using [Beaker](https://github.com/puppetlabs/beaker) configuration files. The
environments created by these scripts have "r10k" fully configured along with
a Git repository with a valid "production" environment.

These scripts are specific to the Puppet Labs environment and will not work in
other environments without alteration!

## Prerequisites

To utilize this test scripts you will need to have Ruby 1.9.3 or greater
installed on your system along with Bundler. Also, the scripts utilize the
"vmpooler" for virtual machine creation. Access to the "vmpooler" machines
require having valid SSH private keys located on your local computer. Speak
with a QA team member for more information on where to find the necessary
SSH keys.

## Usage

The scripts are written in Bash and should run on any Linux or Mac system as
long as the prerequisites mentioned above are satisfied.

### Cloning

First you will need to clone the "[r10k](https://github.com/puppetlabs/r10k)" repository on your local machine:

```bash
git clone git@github.com:puppetlabs/r10k.git
```

### Executing Script

Navigate to the integration tests "scripts" folder of the "r10k" repository
clone:

```bash
cd r10k/integration/scripts
```

There are separate scripts for each supported platform. Select a desired
platform and execute the script:

```bash
bash setup_r10k_env_centos6.sh
```

## Connecting to Machines

The setup process takes about 10 minutes to complete. Once finished Beaker
will report that all tests have been run successfully. The output log will
list the machines created. The Puppet master will have a name ending with
"-master" which you can scrape from the Beaker console output. Example:

```
a9lrs93vnujsrrg.delivery.puppetlabs.net (centos-6-x86_64-master) executed in 1.26 seconds
```

The FQDN of the Puppet master ("a9lrs93vnujsrrg.delivery.puppetlabs.net" in the
above example) will be printed to the left of the machine tag. The machine tag
is a combination of the platform and role of the virtual machine.

Now that you have the FQDN you can connect to the machine using SSH:

```bash
ssh -i private_key root@a9lrs93vnujsrrg.delivery.puppetlabs.net
```

*Note:* The correct SSH private key needs to be installed on your local machine
first. Speak with a QA representative to get the correct key for "vmpooler"
machines.

## Configuration Details

Now that you have successfully connected to the Puppet master you can begin
manual testing. The script has configured Git on the Puppet master to provide
a working "production" environment for "r10k" testing. The Git repository
serving the Puppet environments is located at "/git_repos/environments.git".
There is a Git clone of the remote repository located at "/root/environments".

When performing manual "r10k" testing you should utilize the Git clone
repository located at "/root/environments". The "r10k" configuration file
"/etc/puppetlabs/r10k/r10k.yaml" is already configured to use the remote Git
repository for deployments.
Lib
===========================

This folder contains Ruby files that extends Beaker.
Tests
===========================

This folder contains the [Beaker](https://github.com/puppetlabs/beaker) test files organized by suite.
Manifests
===========================

This folder contains manifests used for testing the r10k project. The manifests are organized by test suite.
Pre-suite
===========================

This folder contains the [Beaker](https://github.com/puppetlabs/beaker) pre-suite tasks that configures test
test infrastructure for testing.
Files
===========================

This folder contains files used for testing the r10k project. The files are organized by test suite.
