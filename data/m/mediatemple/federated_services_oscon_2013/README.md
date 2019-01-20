# Description

This repository contains supplemental material for the [Federated Services, POSSE, and You](http://www.oscon.com/oscon2013/public/schedule/detail/31422) talk at [OSCON 2013](http://www.oscon.com/oscon2013) on July 24, 2013.

It contains code to set up these three services:

* [MediaGoblin](http://mediagoblin.org/) (working)
* [pump.io](http://pump.io/) (not working)
* [tent.io](https://tent.io/) (not working)

# Usage

## Vagrant

To start a [Vagrant](http://www.vagrantup.com/) VM, just run `vagrant up` in the root of a clone of this repository.

    $ vagrant up
    Bringing machine 'default' up with 'virtualbox' provider...
    [default] Setting the name of the VM...
    [default] Clearing any previously set forwarded ports...
    [default] Fixed port collision for 22 => 2222. Now on port 2201.
    [default] Creating shared folders metadata...
    [default] Clearing any previously set network interfaces...
    [default] Preparing network interfaces based on configuration...
    [default] Forwarding ports...
    [default] -- 22 => 2201 (adapter 1)
    [default] -- 80 => 9000 (adapter 1)
    [default] Booting VM...
    [default] Waiting for VM to boot. This can take a few minutes.
    [default] VM booted and ready for use!
    [default] Setting hostname...
    [default] Mounting shared folders...
    [default] -- /vagrant
    [default] -- /tmp/vagrant-puppet/manifests
    [default] -- /tmp/vagrant-puppet/modules-0
    [default] Running provisioner: puppet...
    Running Puppet with init.pp...
    stdin: is not a tty
    ... snip ...
    notice: Finished catalog run in 290.85 seconds

After the VM is done provisioning, point your web browser at <http://localhost:9000>.

To see the log for MediaGoblin, run this command.  This is necessary to view the account verification link.

    $ vagrant ssh -- tail -f /var/log/mediagoblin/mediagoblin-paster.log

If the VM spin up stalls before Vagrant can provision it, just run `vagrant halt` and then `vagrant up` again.

    $ vagrant up
    Bringing machine 'default' up with 'virtualbox' provider...
    [default] Setting the name of the VM...
    [default] Clearing any previously set forwarded ports...
    [default] Fixed port collision for 22 => 2222. Now on port 2201.
    [default] Creating shared folders metadata...
    [default] Clearing any previously set network interfaces...
    [default] Preparing network interfaces based on configuration...
    [default] Forwarding ports...
    [default] -- 22 => 2201 (adapter 1)
    [default] -- 80 => 9000 (adapter 1)
    [default] Booting VM...
    [default] Waiting for VM to boot. This can take a few minutes.
    <Ctrl-C>
    $ vagrant halt
    $ vagrant up

## Puppet

This has only been tested on Ubuntu Raring (13.04).

To run the [Puppet](https://puppetlabs.com/) code directly on a machine or VM that has already been created:

    # aptitude install git puppet -y
    # git clone https://github.com/mediatemple/federated_services_oscon_2013.git
    # cd federated_services_oscon_2013
    # git submodule update --init
    # ./puppet/run -r

Look in `/var/log/mediagoblin/mediagoblin-paster.log` for the MediaGoblin log.  This is necessary to view the account verification link.

## Docker

See the [README](docker/README.md) in the docker directory for details.

# Thanks

To [Joar Wandborg](http://wandborg.se/), for [mediagoblin-init-scripts](https://github.com/joar/mediagoblin-init-scripts).

# License

Copyright 2013 Media Temple, Inc.

This work is licensed under the [MIT license](LICENSE.md).
