# Devkit

Devkit is a framework to build Vagrant boxes for our projects' development environments. This framework uses many tools including Packer, Ansible, Vagrant, Vagrant Cloud, and ServerSpec.

Build the current box with:

```
$> make drupalbox
```

Test the current box with:

```
$> cd dev
$> vagrant up
```

## Development Requirements

- Packer 1.2.1
- Ansible 2.2
- VMWare
- VirtualBox
- Vagrant
- Vagrant plugins:
  - `vagrant-vmware-fusion`
  - `vagrant-auto_network`
  - `vagrant-hostmanager`
  - `vagrant-serverspec`

## Current Boxes

Boxes are released on Vagrant Cloud as [palantir/drupalbox](https://app.vagrantup.com/palantir/boxes/drupalbox).

There is a [drupalbox changelog](drupalbox/CHANGELOG-0.0.md), which is the source of the release notes both here and on Vagrant Cloud.

## Docs

- [How Devkit Works](docs/How-Devkit-Works.md)
- [Updating an existing box](docs/Updating-Existing-Box.md)
- [Writing tests](docs/Writing-Tests.md)
- [Development tips](docs/Development-Workflow.md)

## Support

This project uses the [GitHub issue queue](https://github.com/palantirnet/devkit/issues).

----
Copyright 2016, 2017, 2018 Palantir.net, Inc.
