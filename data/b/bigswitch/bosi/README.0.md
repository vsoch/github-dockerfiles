This directory contains artifacts required for building tarballs
for RHOSP. Contents of this directory are not used by BOSI in any
way.

Placeholder for RHOSP resources.

Resources are grouped based on Openstack release branches.
Typically all branch directories are symlinks to 'master' directory.
Unless there is change for a particular branch, in which case it will
be an actual directory containing the script/yaml files.

When making a fix in master that should be propogated to all the other
releases, please check branch specific directory to make sure it is
updated.
This directory contains the rpm packages of Big Switch
openstack plugins, switch light virtual rpm and a few
helper scripts. RHOSP and BCF have different release
schedules. As a result, the Big Switch openstack plugins
in RHOSP overcloud image may not always be compatable
with a particular BCF release. The rpm packages in this
directory is verified to work with BCF 3.6 and RHOSP8.0.
Please refer to BCF deployment guide for the steps to
patch RHOSP overcloud images.

neutron-bsn-lldp-${lldp_version}-1.el7.centos.noarch.rpm
contains the Big Switch LLDP service

ivs-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual

ivs-debuginfo-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual debugging tools

customize.sh
is the script to customize overcloud ISO image, adding BSN packages

startup.sh
is the script needs to be run on undercloud node first boot
This directory contains the rpm packages of Big Switch
openstack plugins, switch light virtual rpm and a few
helper scripts. RHOSP and BCF have different release
schedules. As a result, the Big Switch openstack plugins
in RHOSP overcloud image may not always be compatable
with a particular BCF release. The rpm packages in this
directory is verified to work with BCF 3.6 and RHOSP8.0.
Please refer to BCF deployment guide for the steps to
patch RHOSP overcloud images.

python-networking-bigswitch-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch ml2 plugin and l3 service plugin

openstack-neutron-bigswitch-lldp-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch lldp service

openstack-neutron-bigswitch-agent-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch virtual switch agent

python-horizon-bsn-${horizon_bsn_version}-1.el7.centos.noarch.rpm
contains the Big Switch horizon plugin

ivs-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual

ivs-debuginfo-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual debugging tools

customize.sh
is the script to customize overcloud ISO image, adding BSN packages

RUNME.sh
is the script to finalize customize.sh and startup.sh with version numbers

startup.sh
is the script needs to be run on undercloud node first boot
This directory contains the rpm packages of Big Switch
openstack plugins, switch light virtual rpm and a few
helper scripts. RHOSP and BCF have different release
schedules. As a result, the Big Switch openstack plugins
in RHOSP overcloud image may not always be compatable
with a particular BCF release. The rpm packages in this
directory is verified to work with BCF 4.0 and RHOSP9.0.
Please refer to BCF deployment guide for the steps to
patch RHOSP overcloud images.

python-networking-bigswitch-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch ml2 plugin and l3 service plugin

openstack-neutron-bigswitch-lldp-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch lldp service

openstack-neutron-bigswitch-agent-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch virtual switch agent

python-horizon-bsn-${horizon_bsn_version}-1.el7.centos.noarch.rpm
contains the Big Switch horizon plugin

nfvswitch-${nfvswitch_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual

qemu-system-x86-2.5.0-4bsn1.el7.centos.x86_64.rpm
qemu-common-2.5.0-4bsn1.el7.centos.x86_64.rpm
qemu-img-2.5.0-4bsn1.el7.centos.x86_64.rpm
contains the qemu version needed by nfvswitch

startup.sh
is the script needs to be run on undercloud node first boot
This directory contains the rpm packages of Big Switch
openstack plugins, switch light virtual rpm and a few
helper scripts. RHOSP and BCF have different release
schedules. As a result, the Big Switch openstack plugins
in RHOSP overcloud image may not always be compatable
with a particular BCF release. The rpm packages in this
directory is verified to work with BCF 3.6 and RHOSP8.0.
Please refer to BCF deployment guide for the steps to
patch RHOSP overcloud images.

python-networking-bigswitch-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch ml2 plugin and l3 service plugin

openstack-neutron-bigswitch-lldp-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch lldp service

openstack-neutron-bigswitch-agent-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch virtual switch agent

python-horizon-bsn-${horizon_bsn_version}-1.el7.centos.noarch.rpm
contains the Big Switch horizon plugin

ivs-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual

ivs-debuginfo-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual debugging tools

customize.sh
is the script to customize overcloud ISO image, adding BSN packages

RUNME.sh
is the script to finalize customize.sh and startup.sh with version numbers

startup.sh
is the script needs to be run on undercloud node first boot
This directory contains the rpm packages of Big Switch
openstack plugins, switch light virtual rpm and a few
helper scripts. RHOSP and BCF have different release
schedules. As a result, the Big Switch openstack plugins
in RHOSP overcloud image may not always be compatable
with a particular BCF release. The rpm packages in this
directory is verified to work with BCF 3.6 and RHOSP8.0.
Please refer to BCF deployment guide for the steps to
patch RHOSP overcloud images.

python-networking-bigswitch-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch ml2 plugin and l3 service plugin

openstack-neutron-bigswitch-lldp-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch lldp service

openstack-neutron-bigswitch-agent-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch virtual switch agent

python-horizon-bsn-${horizon_bsn_version}-1.el7.centos.noarch.rpm
contains the Big Switch horizon plugin

ivs-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual

ivs-debuginfo-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual debugging tools

customize.sh
is the script to customize overcloud ISO image, adding BSN packages

startup.sh
is the script needs to be run on undercloud node first boot
This directory contains the rpm packages of Big Switch
openstack plugins, switch light virtual rpm and a few
helper scripts. RHOSP and BCF have different release
schedules. As a result, the Big Switch openstack plugins
in RHOSP overcloud image may not always be compatable
with a particular BCF release. The rpm packages in this
directory is verified to work with BCF 3.6 and RHOSP8.0.
Please refer to BCF deployment guide for the steps to
patch RHOSP overcloud images.

python-networking-bigswitch-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch ml2 plugin and l3 service plugin

openstack-neutron-bigswitch-lldp-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch lldp service

openstack-neutron-bigswitch-agent-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch virtual switch agent

python-horizon-bsn-${horizon_bsn_version}-1.el7.centos.noarch.rpm
contains the Big Switch horizon plugin

ivs-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual

ivs-debuginfo-${ivs_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual debugging tools

ifup-ivs
is the script to bring up interfaces on switch light virtual

ifdown-ivs
is the script to bring down interfaces on switch light virtual

assign-ivs-ip
is the script to assign ip address to interfaces on switch light virtual

startup.sh
is the script needs to be run on undercloud node first boot
This directory contains the rpm packages of Big Switch
openstack plugins, switch light virtual rpm and a few
helper scripts. RHOSP and BCF have different release
schedules. As a result, the Big Switch openstack plugins
in RHOSP overcloud image may not always be compatable
with a particular BCF release. The rpm packages in this
directory is verified to work with BCF 4.0 and RHOSP9.0.
Please refer to BCF deployment guide for the steps to
patch RHOSP overcloud images.

python-networking-bigswitch-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch ml2 plugin and l3 service plugin

openstack-neutron-bigswitch-lldp-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch lldp service

openstack-neutron-bigswitch-agent-${networking_bigswitch_version}-1.el7.centos.noarch.rpm
contains the Big Switch virtual switch agent

python-horizon-bsn-${horizon_bsn_version}-1.el7.centos.noarch.rpm
contains the Big Switch horizon plugin

nfvswitch-${nfvswitch_version}.el7.centos.x86_64.rpm
contains the Big Switch switch light virtual

qemu-system-x86-2.5.0-4bsn1.el7.centos.x86_64.rpm
qemu-common-2.5.0-4bsn1.el7.centos.x86_64.rpm
qemu-img-2.5.0-4bsn1.el7.centos.x86_64.rpm
contains the qemu version needed by nfvswitch

startup.sh
is the script needs to be run on undercloud node first boot
