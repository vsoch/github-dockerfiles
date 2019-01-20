# bar-cookbook

TODO: Enter the cookbook description here.

# bar-cookbook

TODO: Enter the cookbook description here.

Dev Cookbook Fixtures

Cookbooks in here that are used to represent local checkouts of a
git-hosted cookbook are stored as git bundles to avoid problems with git
assuming the cookbooks are submodules. For more information, read the
`git-bundle` manpage (`git help bundle`). The short version is that you
can treat the git bundle as a regular git remote if you need to modify
the fixture data:

```
cd staging_dir
git clone $prefix/cookbook.gitbundle
# make edits, commit
git push
```

# another-local-cookbook

TODO: Enter the cookbook description here.

# noignore

TODO: Enter the cookbook description here.

# local-cookbook

TODO: Enter the cookbook description here.

This is an empty directory that represents a cookbook with a missing
metadata.rb file.
# local-cookbook

TODO: Enter the cookbook description here.

# bar-cookbook

TODO: Enter the cookbook description here.

# bar-cookbook

TODO: Enter the cookbook description here.

# bar-cookbook

TODO: Enter the cookbook description here.

# bar-cookbook

TODO: Enter the cookbook description here.

# Overview

Every Chef installation needs a Chef Repository. This is the place where cookbooks, roles, config files and other artifacts for managing systems with Chef will live. We strongly recommend storing this repository in a version control system such as Git and treat it like source code.

While we prefer Git, and make this repository available via GitHub, you are welcome to download a tar or zip archive and use your favorite version control system to manage the code.

# Repository Directories

This repository contains several directories, and each directory contains a README file that describes what it is for in greater detail, and how to use it for managing your systems with Chef.

- `cookbooks/` - Cookbooks you download or create.
- `data_bags/` - Store data bags and items in .json in the repository.
- `roles/` - Store roles in .rb or .json in the repository.
- `environments/` - Store environments in .rb or .json in the repository.

# Configuration

The config file, `.chef/knife.rb` is a repository specific configuration file for knife. If you're using the Chef Platform, you can download one for your organization from the management console. If you're using the Open Source Chef Server, you can generate a new one with `knife configure`. For more information about configuring Knife, see the Knife documentation.

<https://docs.chef.io/knife.html>

# Next Steps

Read the README file in each of the subdirectories for more information about what goes in those directories.
# Data Bags

This directory contains directories of the various data bags you create for your infrastructure. Each subdirectory corresponds to a data bag on the Chef Server, and contains JSON files of the items that go in the bag.

For example, in this directory you'll find an example data bag directory called `example`, which contains an item definition called `example_item.json`

Before uploading this item to the server, we must first create the data bag on the Chef Server.

    knife data bag create example

Then we can upload the items in the data bag's directory to the Chef Server.

    knife data bag from file example example_item.json

For more information on data bags, see the Chef wiki page:

https://docs.chef.io/data_bags.html

# Encrypted Data Bags

Encrypted data bags allow you to encrypt the contents of your data bags. The content of attributes will no longer be searchable. To use encrypted data bags, first you must have or create a secret key.

    openssl rand -base64 512 > secret_key

You may use this secret_key to add items to a data bag during a create.

    knife data bag create --secret-file secret_key passwords mysql

You may also use it when adding ITEMs from files,

    knife data bag create passwords
    knife data bag from file passwords data_bags/passwords/mysql.json --secret-file secret_key

The JSON for the ITEM must contain a key named "id" with a value equal to "ITEM" and the contents will be encrypted when uploaded. For example,

    {
      "id": "mysql",
      "password": "abc123"
    }

Without the secret_key, the contents are encrypted.

    knife data bag show passwords mysql
    id:        mysql
    password:  2I0XUUve1TXEojEyeGsjhw==

Use the secret_key to view the contents.

    knife data bag show passwords mysql --secret-file secret_key
    id:        mysql
    password:  abc123


For more information on encrypted data bags, see the Chef wiki page:

https://docs.chef.io/data_bags.html
Create environments here, in either the Role Ruby DSL (.rb) or JSON (.json) files. To install environments on the server, use knife.

For example, in this directory you'll find an example environment file called `example.json` which can be uploaded to the Chef Server:

    knife environment from file environments/example.json

For more information on environments, see the Chef wiki page:

https://docs.chef.io/environments.html
# Example

An example cookbook

## Requirements

### Platform:

_No platforms defined_

### Cookbooks:

_No dependencies defined_

## Attributes

- `node['example']['name']` - Defaults to `Sam Doe`.

## Recipes

- example::default

## License and Maintainer

Maintainer:: (<>)

License:: All rights reserved
Create policyfiles here. When using a chef-repo, give your policyfiles
the same filename as the name set in the policyfile itself, and use the
`.rb` file extension.

Compile the policy with a command like this:

```
chef install policyfiles/my-app-frontend.rb
```

This will create a lockfile `policyfiles/my-app-frontend.lock.json`.

To update locked dependencies, run `chef update` like this:

```
chef update policyfiles/my-app-frontend.rb
```

You can upload the policy (with associated cookbooks) to the server
using a command like:

```
chef push staging policyfiles/my-app-frontend.rb
```
Create roles here, in either the Role Ruby DSL (.rb) or JSON (.json) files. To install roles on the server, use knife.

For example, in this directory you'll find an example role file called `example.json` which can be uploaded to the Chef Server:

    knife role from file roles/example.json

For more information on roles, see the Chef wiki page:

https://docs.chef.io/roles.html
# build_cookbook

A build cookbook for running the parent project through Chef Delivery

This build cookbook should be customized to suit the needs of the parent project. Using this cookbook can be done outside of Chef Delivery, too. If the parent project is a Chef cookbook, we've detected that and "wrapped" [delivery-truck](https://github.com/chef-cookbooks/delivery-truck). That means it is a dependency, and each of its pipeline phase recipes is included in the appropriate phase recipes in this cookbook. If the parent project is not a cookbook, it's left as an exercise to the reader to customize the recipes as needed for each phase in the pipeline.

## .delivery/config.json

In the parent directory to this build_cookbook, the `config.json` can be modified as necessary. For example, phases can be skipped, publishing information can be added, and so on. Refer to customer support or the Chef Delivery documentation for assistance on what options are available for this configuration.

## Test Kitchen - Local Verify Testing

This cookbook also has a `.kitchen.yml` which can be used to create local build nodes with Test Kitchen to perform the verification phases, `unit`, `syntax`, and `lint`. When running `kitchen converge`, the instances will be set up like Chef Delivery "build nodes" with the [delivery_build cookbook](https://github.com/chef-cookbooks/delivery_build). The reason for this is to make sure that the same exact kind of nodes are used by this build cookbook are run on the local workstation as would run Delivery. It will run `delivery job verify PHASE` for the parent project.

Modify the `.kitchen.yml` if necessary to change the platforms or other configuration to run the verify phases. After making changes in the parent project, `cd` into this directory (`.delivery/build_cookbook`), and run:

```
kitchen test
```

## Recipes

Each of the recipes in this build_cookbook are run in the named phase during the Chef Delivery pipeline. The `unit`, `syntax`, and `lint` recipes are additionally run when using Test Kitchen for local testing as noted in the above section.

## Making Changes - Cookbook Example

When making changes in the parent project (that which lives in `../..` from this directory), or in the recipes in this build cookbook, there is a bespoke workflow for Chef Delivery. As an example, we'll discuss a Chef Cookbook as the parent.

First, create a new branch for the changes.

```
git checkout -b testing-build-cookbook
```

Next, increment the version in the metadata.rb. This should be in the _parent_, not in this, the build_cookbook. If this is not done, the verify phase will fail.

```
% git diff
<SNIP>
-version '0.1.0'
+version '0.1.1'
```

The change we'll use for an example is to install the `zsh` package. Write a failing ChefSpec in the cookbook project's `spec/unit/recipes/default_spec.rb`.

```ruby
require 'spec_helper'

describe 'godzilla::default' do
  context 'When all attributes are default, on Ubuntu 16.04' do
    let(:chef_run) do
      runner = ChefSpec::ServerRunner.new(platform: 'ubuntu', version: '16.04')
      runner.converge(described_recipe)
    end

    it 'installs zsh' do
      expect(chef_run).to install_package('zsh')
    end
  end
end
```

Commit the local changes as work in progress. The `delivery job` expects to use a clean git repository.

```
git add ../..
git commit -m 'WIP: Testing changes'
```

From _this_ directory (`.delivery/build_cookbook`, relative to the parent cookbook project), run

```
cd .delivery/build_cookbook
kitchen converge
```

This will take some time at first, because the VMs need to be created, Chef installed, the Delivery CLI installed, etc. Later runs will be faster until they are destroyed. It will also fail on the first VM, as expected, because we wrote the test first. Now edit the parent cookbook project's default recipe to install `zsh`.

```
cd ../../
$EDITOR/recipes/default.rb
```

It should look like this:

```
package 'zsh'
```

Create another commit.

```
git add .
git commit -m 'WIP: Install zsh in default recipe'
```

Now rerun kitchen from the build_cookbook.

```
cd .delivery/build_cookbook
kitchen converge
```

This will take awhile because it will now pass on the first VM, and then create the second VM. We should have warned you this was a good time for a coffee break.

```
Recipe: test::default

- execute HOME=/home/vagrant delivery job verify unit --server localhost --ent test --org kitchen
  * execute[HOME=/home/vagrant delivery job verify lint --server localhost --ent test --org kitchen] action run
    - execute HOME=/home/vagrant delivery job verify lint --server localhost --ent test --org kitchen

    - execute HOME=/home/vagrant delivery job verify syntax --server localhost --ent test --org kitchen

Running handlers:
Running handlers complete
Chef Client finished, 3/32 resources updated in 54.665445968 seconds
Finished converging <default-centos-71> (1m26.83s).
```

Victory is ours! Our verify phase passed on the build nodes.

We are ready to run this through our Delivery pipeline. Simply run `delivery review` on the local system from the parent project, and it will open a browser window up to the change we just added.

```
cd ../..
delivery review
```

## FAQ

### Why don't I just run rspec and foodcritic/rubocop on my local system?

An objection to the Test Kitchen approach is that it is much faster to run the unit, lint, and syntax commands for the project on the local system. That is totally true, and also totally valid. Do that for the really fast feedback loop. However, the dance we do with Test Kitchen brings a much higher degree of confidence in the changes we're making, that everything will run on the build nodes in Chef Delivery. We strongly encourage this approach before actually pushing the changes to Delivery.

### Why do I have to make a commit every time?

When running `delivery job`, it expects to merge the commit for the changeset against the clean master branch. If we don't save our progress by making a commit, our local changes aren't run through `delivery job` in the Test Kitchen build instances. We can always perform an interactive rebase, and modify the original changeset message in Delivery with `delivery review --edit`. The latter won't modify the git commits, only the changeset in Delivery.

### What do I do next?

Make changes in the cookbook project as required for organizational goals and needs. Modify the `build_cookbook` as necessary for the pipeline phases that the cookbook should go through.

### What if I get stuck?

Contact Chef Support, or your Chef Customer Success team and they will help you get unstuck.
This directory contains the cookbooks used to configure systems in your infrastructure with Chef - an example basic cookbook called `example` has been automatically created for you.

Knife needs to be configured to know where the cookbooks are located with the `cookbook_path` setting. If this is not set, then several cookbook operations will fail to work properly.

```
cookbook_path ["./cookbooks"]
```

This setting tells knife to look for the cookbooks directory in the present working directory. This means the knife cookbook subcommands need to be run in the `chef-repo` directory itself. To make sure that the cookbooks can be found elsewhere inside the repository, use an absolute path. This is a Ruby file, so something like the following can be used:

```
current_dir = File.dirname(__FILE__)
cookbook_path ["#{current_dir}/../cookbooks"]
```

Which will set `current_dir` to the location of the knife.rb file itself (e.g. `~/chef-repo/.chef/knife.rb`).

Configure knife to use your preferred copyright holder, email contact and license. Add the following lines to `.chef/knife.rb`.

```
cookbook_copyright "Example, Com."
cookbook_email     "cookbooks@example.com"
cookbook_license   "apachev2"
```

Supported values for `cookbook_license` are "apachev2", "mit","gplv2","gplv3", or "none". These settings are used to prefill comments in the default recipe, and the corresponding values in the metadata.rb. You are free to change the the comments in those files.

Create new cookbooks in this directory with Chef.

```
chef generate cookbook COOKBOOK
```

This will create all the cookbook directory components. You don't need to use them all, and can delete the ones you don't need. It also creates a README file, metadata.rb and default recipe.

You can also download cookbooks directly from the Chef Supermarket site. There are two subcommands to help with this depending on what your preference is.

The first and recommended method is to use a vendor branch if you're using Git. This is automatically handled with Knife.

```
knife cookbook site install COOKBOOK
```

This will:

- Download the cookbook tarball from the Chef Supermarket.
- Ensure its on the git master branch.
- Checks for an existing vendor branch, and creates if it doesn't.
- Checks out the vendor branch (chef-vendor-COOKBOOK).
- Removes the existing (old) version.
- Untars the cookbook tarball it downloaded in the first step.
- Adds the cookbook files to the git index and commits.
- Creates a tag for the version downloaded.
- Checks out the master branch again.
- Merges the cookbook into master.
- Repeats the above for all the cookbooks dependencies, downloading them from the community site

The last step will ensure that any local changes or modifications you have made to the cookbook are preserved, so you can keep your changes through upstream updates.

If you're not using Git, use the site download subcommand to download the tarball.

```
knife cookbook site download COOKBOOK
```

This creates the COOKBOOK.tar.gz from in the current directory (e.g., `~/chef-repo`). We recommend following a workflow similar to the above for your version control tool.
This directory typically contains Chef cookbooks. This repository was
generated with the '--policy-only' option, which means you have chosen
to use a workflow where each cookbook is treated as an independent
software project. As a result, any cookbooks present in this directory
are independent git projects, and the contents of this directory have
been added to .gitignore.

Love,
Chef
# <%= cookbook_name %>

TODO: Enter the cookbook description here.

# ChefDK Omnibus project

This project creates full-stack platform-specific packages for ChefDK.

Note that the repository name is chef-dk but the omnibus project definition is
chefdk. This is a historical artifact that may eventually get fixed.

## Installation

You must have a sane Ruby environment with Bundler installed. Ensure all the required gems are installed:

```shell
$ bundle install --without development
```

## Usage

### Build

You create a platform-specific package using the `build project` command:

```shell
$ bundle exec omnibus build chefdk
```

The platform/architecture type of the package created will match the platform where the `build project` command is invoked. For example, running this command on a MacBook Pro will generate a macOS package. After the build completes packages will be available in the `pkg/` folder.

### Clean

You can clean up all temporary files generated during the build process with the `clean` command:

```shell
$ bundle exec omnibus clean chefdk
```

Adding the `--purge` purge option removes **ALL** files generated during the build including the project install directory (`/opt/chefdk`) and the package cache directory (`/var/cache/omnibus/pkg`):

```shell
$ bundle exec omnibus clean chefdk --purge
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
$ bundle exec kitchen converge chefdk-ubuntu-1804
```

Then login to the instance and build the project as described in the Usage
section:

```shell
$ kitchen login chefdk-ubuntu-1204
[vagrant@ubuntu...] $ source load-omnibus-toolchain.sh
[vagrant@ubuntu...] $ cd chef-dk/omnibus
[vagrant@ubuntu...] $ bundle install --without development # Don't install dev tools!
[vagrant@ubuntu...] $ ...
[vagrant@ubuntu...] $ bundle exec omnibus build chefdk -l internal
```

You can also login to Windows instances but will have to manually call the
`load-omnibus-toolchain.bat` script which initializes the build environment.
Please note the mounted code directory is also at `C:\home\vagrant\chef-dk\omnibus`
as opposed to `C:\Users\vagrant\chef-dk\omnibus`.

```shell
$ bundle exec kitchen login chefdk-windows-2012r2-standard-i386
Last login: Sat Sep 13 10:19:04 2014 from 172.16.27.1
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\>C:\vagrant\load-omnibus-toolchain.bat

C:\>cd C:\vagrant\code\chef-dk\omnibus

C:\vagrant\code\chef-dk\omnibus>bundle install --without development

C:\vagrant\code\chef-dk\omnibus>bundle exec omnibus build chefdk -l internal
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
