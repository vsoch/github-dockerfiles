===============================
os-vif-bigswitch
===============================

Neutron OS-VIF plugin for Big Switch Networks SwitchLight VX

OS-VIF is required on Openstack compute nodes to plug/unplug an interface
to the appropriate virtual switch. This package handles it for IVS, now known
as SwitchLight VX.
Installation is typically done by BOSI (BigSwitch Openstack Installer).
Versioning follows upstream Openstack major release numbers. Minor version can
vary based on BCF (Big Cloud Fabric) release in use.
For more information about support matrix with BCF (Big Cloud Fabric) release
versions, please contact https://www.bigswitch.com/support

* Free software: Apache license
* Source: https://github.com/bigswitch/os-vif-bigswitch

Features
--------

* Supports VIFBridge vnic type for port binding.
