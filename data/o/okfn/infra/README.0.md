# Sendy

This role helps install Sendy on a given server at the domain sendy.okfn.org.
Countermeasures against vinabot
===============================

Zombies in Vietnam are attacking our listserv. The botnet seems to work
in two stages. First some hosts on the Internet, usually web servers with
the Wordpress software installed, are compromised and they host some PHP
code that does nasty things. Then people's computers are compromised and
caused to visit the compromised server which instructs their web browsers
to do things like ask for some poor sod to be subscribed to many mailing 
lists again and again. This generates a lot of email traffic causing the
listserv to be banned by some sites such as hotmail and aol and fills up
the poor sod's mailbox. 

The scripts here are designed to be run in a pipeline like so::

     tail -f /var/log/nginx/access.log | xvinabot.sh | tee -a xvinabot.log | sh

The shell script uses an awk script to parse out the offending IP addresses
and does a whois on them to find out the netblock they belong to. If the
netblock is in Vietnam it outputs a command to null route the entire 
netblock. If it isn't it outputs a command to null route the host.

The output looks like this::

    route add -host 185.17.26.247 reject # BM-PRIVAX-LIMITED-IP-9 (GB)
    route add -net 42.116.208.0/20 reject # FPT-STATICIP-NET (VN)

The log file can be run with::

    sh xvinabot.log

after a reboot to re-create the null routes.
Generate a report of the memory usage on ansible-managed hosts. This
can be thought of as a network-wide ps(1). The report can be generated
by running the make(1) command.

That they are ansible-managed is accidental -- but the Makefile uses
the inventory to get the list of hosts. It does not use ansible
directly (though it could) because parsing ansible's output is
unreliable. This is because it expects that it might be run in a
multi-threaded way and doesn't appear to take measures to properly
serialise its output so that it can be processed by another
program. That's not the UNIX Way. But I digress.

The scripts run ps and look in /proc/meminfo. They sum the resident
size of the programs running, and compare that the the total
memory. Similar comparisons are done for kernel I/O buffers and cache,
as well as swap space usage. A report is generated to standard output.

Sometimes a server appears to have overcommitted memory, sometimes by
a significant margin 3-4x. This is almost always postgresql which
makes heavy use of CoW with its child processes sharing much of the
parent's address space. Inspecting the column with buffers shows that
actually the apparent memory usage is unrealistically high, and there
is still (or should be) plenty of RAM for I/O buffering which is
critical to database performance.
Try to figure out the canonical list of hosts.

Start with the list in the ansible inventory, and the list in the
trello ticket. Clean them up, sort them and run diff.

       make clean all

will produce hosts.ansible.diff and hosts.trello.diff which represent
the difference between those individual host lists and the combined
one.
# Ansible configuration management

This repository contains scripts and data used in managing the configuration of
the Open Knowledge Foundation's servers.

The files in this repository are used by
[Ansible](http://www.ansibleworks.com/).

## Using this repository

1. [Install Ansible](http://docs.ansible.com/intro_installation.html).

2. Clone this repository and
   [`okfn/credentials`](https://github.com/okfn/credentials) alongside one
   another.

3. Run `ansible-playbook` 

## Example invocations

Run plays that apply to nodes tagged with `monitoring`:

    ansible-playbook main.yml -t monitoring

Run play to add a new group and its users

    ansible-playbook main.yml -t add_group,add_users,add_ssh_keys,sudoers -e host=all

Run a play to just run one role

    ansible-playbook main.yml -vvvv -i inventory/hosts -s -t project_users -l s107.okserver.org

You can also use the `ansible` command directly to run tasks on remote hosts:

    ansible all -i inventory/hosts -e uptime

Adding -vvvv (or --verbose) will get you lots of useful debug info.

## Repository structure

### `main.yml`, `bootstrap.yml`, etc.

Top-level ansible playbooks.

### `roles/`

Application-specific configuration.

### `inventory/`

Host or host-group specific configuration. The main inventory lives at
`inventory/hosts` and host and group variables files live in
`inventory/{host,group}_vars`.

### `vars/`

Global variables, applicable to all hosts.

### `files/`

More application-specific configuration (?).
# scripts Role

Sets up and configures a number of scripts.  Mainly to do with check_mk.  

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# apt Role

Installed a list (pkg_list) of software using apt-get

## Tags

apt

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# Simple sudo role

This role sets up a simple sudoers file. Each user has full sudo access, and a
global setting determines whether NOPASSWD is set or not.

## Variables

 * sudo_users - A list of users who have sudo access. Use '%foo' to specify
   that users in a given group have sudo access.
   * default: root, users in group wheel
 * sudo_nopasswd - if set, NOPASSWD is added to all sudoers entries. Use this
   when users don't have passwords set.
   * default: true
[![Build Status](https://travis-ci.org/WillsherSystems/ansible-sshd.svg?branch=master)](https://travis-ci.org/WillsherSystems/ansible-sshd) [![Ansible Galaxy](http://img.shields.io/badge/galaxy-willshersystems.sshd-660198.svg?style=flat)](https://galaxy.ansible.com/list#/roles/2488)

OpenSSH Server
==============

This role configures the OpenSSH daemon. It:

* By default configures the SSH daemon with the normal OS defaults.
* Works across a variety of UN*X like distributions
* Can be configured by dict or simple variables
* Supports Match sets
* Supports all sshd_config options. Templates are programmatically generated.
  (see [meta/make_option_list](meta/make_option_list))
* Tests the sshd_config before reloading sshd.

**WARNING** Misconfiguration of this role can lock you out of your server!
Please test your configuration and its interaction with your users configuration
before using in production!

**WARNING** Digital Ocean allows root with passwords via SSH on Debian and
Ubuntu. This is not the default assigned by this module - it will set
`PermitRootLogin without-password` which will allow access via SSH key but not
via simple password. If you need this functionality, be sure to set
`ssh_PermitRootLogin yes` for those hosts.

Requirements
------------

Tested on:

* Ubuntu precise, trusty
* Debian wheezy, jessie
* FreeBSD 10.1
* EL 6,7 derived distributions

It will likely work on other flavours and more direct support via suitable
[vars/](vars/) files is welcome.

Role variables
---------------

Unconfigured, this role will provide a sshd_config that matches the OS default,
minus the comments and in a different order.

* sshd_skip_defaults

If set to True, don't apply default values. This means that you must have a
complete set of configuration defaults via either the sshd dict, or sshd_Key
variables. Defaults to *False*.

* sshd_allow_reload

If set to False, a reload of sshd wont happen on change. This can help with 
troubleshooting. You'll need to manually reload sshd if you want to apply the
changed configuration. Defaults to *True*.

* sshd

A dict containing configuration.  e.g.

```yaml
sshd:
  Compression: delayed
  ListenAddress:
    - 0.0.0.0
```

* ssh_...

Simple variables can be used rather than a dict. Simple values override dict
values. e.g.:

```yaml
sshd_Compression: off
```

In all cases, booleans correctly rendered as yes and no in sshd configuration.
Lists can be used for multiline configuration items. e.g.

```yaml
sshd_ListenAddress:
  - 0.0.0.0
  - '::'
```

Renders as:

```
ListenAddress 0.0.0.0
ListenAddress ::
```

* sshd_match

A list of dicts for a match section. See the example playbook.

* sshd_match_1 through sshd_match_9

A list of dicts or just a dict for a Match section.

Example Playbook
----------------
 
```yaml
---
- hosts: all
  vars:
    sshd_skip_defaults: true
    sshd:
      Compression: true
      ListenAddress:
        - "0.0.0.0"
        - "::"
      GSSAPIAuthentication: no
      Match:
        - Condition: "Group user"
          GSSAPIAuthentication: yes
    sshd_UsePrivilegeSeparation: sandbox
    sshd_match:
        - Condition: "Group xusers"
          X11Forwarding: yes
  roles:
    - role: willshersystems.sshd
```

Results in:

``` 
# Ansible managed: ...
Compression yes
GSSAPIAuthentication no
UsePrivilegeSeparation sandbox
Match Group user
  GSSAPIAuthentication yes
Match Group xusers
  X11Forwarding yes
```

License
-------

LGPLv3


Author
------

Matt Willsher <matt@willsher.systems>

Copyright 2014,2015 Willsher Systems
# tmpreaper Role

A role to install the tmpreaper software on a server.  tmpreaper can be used to clean down files over a certain age.  It's mainly intended to be used on the tmp directory.

## Tags

install_tmpreaper
configure_tmpreaper

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# spamassassin Role

Installs spamassassin and configures it to work with postfix.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# supervisor Role

Installs the supervisor software on a server.  More details here - http://supervisord.org/  It's similar to software such as launchd, daemontools and runit.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
========

Set timezone on Debian-like systems.

Role Variables
--------------

 * *timezone* - timezone (like _UTC_, _Europe/Moscow_)

License
-------

MIT

Author Information
------------------

Sergey Korolev (<korolev.srg@gmail.com>)

# unattended-upgrades Role

Installed the unattended-upgrades software.  This means that the server will automatically run security updates on a daily basis.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# rsyncd Role

Installs rsyncd on a server.  Also configures it.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# okfn-org-manager Role

A custom role to install a few different things on okfn servers.  Including awscli, okfn-heroku-copyapp and a cronjob to move prod data to staging.

## Tags

None

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# nginx Role

Installs nginx and configures sites as per the variables passed. 

## Tags

nginx_ssl

## Dependencies



## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

sites_enabled
project
inventory_hostname
item
# nagios-server Role

Installs the nagios server.  

## Tags



## Dependencies

role: php-fpm

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

item
private_dir
# fail2ban Role

Installs and configures fail2ban.

## Tags

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# iptables-persistent Role

Installs and configures iptables-persistent.

## Tags

install_iptables_persistent
iptables_config

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables



None

## Notes

This command will throw a dpkg error on linode hosts because linode does not
allow modprobe, the fix is to run the following:

sudo sed \
    -i 's/\(modprobe -q ip6\?table_filter\)/\1 || true/g' \
    /var/lib/dpkg/info/iptables-persistent.postinst; \
sudo apt-get install iptables-persistent

See https://forum.linode.com/viewtopic.php?t=9070&p=58732

# rsnapshot Role

Installs and configures rsnapshot.  rsnapshot is a collection of perl scripts which is used to backup servers, through a series of snapshots.  It uses symlinks on unchanged files to keep the backup set size manageable.  We currently use it to backup our mailman install.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# awscli Role

Installs pip, then awscli and then configures awscli using keys supplied through extra vars.

We have an extra store for the variables so you need to specify that with setting a private_dir extra var.  For example:

    - "{{ private_dir }}/p.yml"

And in p.yml you'll need the following:

aws_keys:
  - 
    id: user0
    key: somekey
    secret_key: somesecretkey
    region: eu-west-1
  - 
    id: user1
    key: key
    secret_key: secretkey
    region: eu-west-2


So if you want user0 you'd call it like this in main.yml:

- hosts: s138.okserver.org
  sudo: true
  vars_files:
    - "{{ private_dir }}/p.yml"
  roles:
    - role: awscli
      tags: ['awscli']
      key: "{{ aws_keys[0].key }}"
      secret_key: "{{ aws_keys[0].secret_key }}"
      region: "{{ aws_keys[0].region }}"
      


Just change the number to reference the key you want.



## Tags

awscli
awscli_install
awscli_create_config_dir
awscli_configure

## Dependencies

## Usage

Ideally specify the variables in the two yml files as above, but you can pass them on the command line like this:

ansible-playbook main.yml --verbose -i inventory/hosts --extra-vars="private_dir=/path/to/dir awscli_user_home=/root awscli_user=root awscli_group=root" -t awscli -l s138.okserver.org -s

So assuming that you've defined everything correctly just:

ansible-playbook main.yml --verbose -i inventory/hosts --extra-vars="private_dir=/path/to/dir" -t awscli -l s138.okserver.org -s

## Variables

awscli_aws_access_key - the access key
awscli_aws_secret_access_key
awscli_region - the region, we're normally ireland
aws_user_home - has to start with a slash but have no trailing slash.  eg /home/bob or /root
awscli_user - a specific user for the config to go in
awscli_group - a specific group for the config to go in

# motd Role

Adds a motd stating that the system is under control of ansible.  Updates it as needed.

## Tags

motd

## Dependencies



## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# varnish Role

A role to install and configure the varnish cache server.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# heroku-toolbelt Role

Installs and configures heroku toolbelt software.

## Tags

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# postfix Role

Installs and configures the postfix MTA suite of software.

## Tags

postfix
mastercf

## Dependancies

Has a dependancy on the scripts role.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# db-backup Role

Copies a number of backup scripts over to the server and makes sure they're running in cron.

## Tags

ensure_backup_scripts_dir
ensure_backup_cron
copy_backup_scripts
psql_backup_config
mysql_backup_config

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# rt Role

Installs and configures RT on a server.  It assumes that the RT database has already been setup and is stored on an existing database server.  In our case that's RDS, but this could be any other database server.  So this role is really for installing RT as a front-end.

This also installs a number of plugins, the current list is below:

https://github.com/bestpractical/rt-extension-activityreports
https://github.com/bestpractical/rt-extension-commandbymail
https://github.com/bestpractical/rt-extension-mergeusers
https://github.com/bestpractical/rt-extension-repeatticket
https://github.com/gitpan/RT-Extension-ResetPassword
https://github.com/bestpractical/rt-extension-spawnlinkedticketinqueue

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts -s -t rt -l server.to.install.rt.on.tld

## Variables

None
# php-fpm Role

Installs the php-fpm package and configures it.  PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI implementation with some additional features useful for sites of any size, especially busier sites.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# check-mk-agent Role

Installs the check_mk agent on either debian or ubuntu servers.  Also installed xinetd, changes the firewall and sets up some plugins.

## Tags

## Dependencies

role: scripts 

role: iptables-persistent 

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

iptables_config_file
check_mk_port
monitoring_server
enabled_plugin_check

local_checks_paths
ntp
===

This role enables users to install and configure ntp on their hosts.

Requirements
------------

This role requires Ansible 1.4 or higher, and platform requirements are listed
in the metadata file.

Role Variables
--------------

The variables that can be passed to this role and a brief description about
them are as follows. See the NTP configuration documentation for details:

	# The driftfile
	ntp_driftfile: /var/lib/ntp/drifta

	# The server to sync time with
	ntp_server: [0.ubuntu.pool.ntp.org, 1.ubuntu.pool.ntp.org]

	ntp_restrict:                                                           
	  - "restrict -4 default kod notrap nomodify nopeer noquery"
	  - "restrict -6 default kod notrap nomodify nopeer noquery"
	  - "restrict 127.0.0.1"

	ntp_crypto: no
	ntp_includefile: no
	ntp_keys: no
	ntp_trustedkey: no
	ntp_requestkey: no
	ntp_controlkey: no
	ntp_statistics: no
	ntp_broadcast: no
	ntp_broadcastclient: no
	ntp_multicastclient: no

Examples
--------

1) Install ntp and set the default settings.

	- hosts: all
	  roles:
	    - role: ntp

2) Install ntp and set some custom servers.

	- hosts: all
	  roles:
	    - role: ntp
	      ntp_server: [2.ubuntu.pool.ntp.org, 1.ubuntu.pool.ntp.org]

Dependencies
------------

None

License
-------

BSD

Author Information
------------------

Benno Joy


# check-mk-server Role

Installs check_mk on a server and configures it.

## Tags

setup-main.mk

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# nagios-api Role

Installs a nagios api, from github and using pip.

## Tags

nagios-api
nagios-api_clone_repo
nagios-api_install
nagios-api_install_deps

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

item
src_dir
# update-notifier Role

This installs the update-notifier software on a server.  This software will provide a report as to what updates are pending on a server.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# postgrey Role

Installs postgrey.  Postgrey is software which provides greylisting functionality to postgres.  Greylisting is whereby email not on the whitelist gets rejected initially, but allowed through after 10 minutes (configurable) once it's been allowed once it's whitelisted.  Spammers don't normally try more than once, so this cuts down on spam.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# nagios-client Role

Installs the nagios plugins and adds users and groups for the plugins.

## Tags

install_nagios_plugins

add_nagios_group

add_nagios_users

## Dependencies

role: scripts
 
## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

users.monitoring
item
item.name
item.group
# cron Role

Sets up some backup cronjobs and sets up backups to s3.

## Tags

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# apt-mirror-config Role

Sets up some extra apt config files.

## Tags

copy_apt_config

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# mailman Role

Installs and configures mailman.
 
## Tags

mailman_config

## Dependencies

role: spamassassin

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
# docker Role

Installs docker and them makes sure all the okfn docker containers are running.  This is currently mariadb, etherpad, booktype, opensendy and RT.

## Tags

start-mariadb55
start-okfnpad
start-booktype
start-sendy
start-rt

## Dependencies

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

None
## Omeka role

An ansible role to install Omeka and configure it on a standard server.

## Tags

omeka

## Dependencies

None

## Usage


## Variables


# users Role

A role to install users across the various servers.

## Usage

ansible-playbook --verbose main.yml -i inventory/hosts --sudo --tags=

## Variables

devs_group
# OKF custom host vars

The following custom host variables are used in this inventory:

## `disable_nagios_checks`

Define this var, and run the `check_mk` role to disable ALL nagios checks for
the host, the host will essentially be removed from nagios.

Accepted args are True/False

    disable_nagios_checks=True

## `local_checks`

`local_checks` expects an array of check scripts which are `check_mk` specific and
need to be enabled on the host. Setting this var adds the script into the `check_mk` agent local checks folder, from which `check_mk` will periodically run scripts.

    local_checks: ['exim_mailqueue']

## `check_parameters`

`check_parameters` is an array of parameters which should be setup per check, these apply to both inventorized and manually defined checks,
each array element should be in the format:

    <check name>:<warning level>:<critical level>

 e.g:

     check_parameters: ['Postfix Queue:80:120']

For more details on [`checkmk_check parameters`](http://mathias-kettner.de/checkmk_check_parameters.html)


## `disabled_checks`

`disabled_checks` accepts an array of elements with the names of local passive
checks that should be disabled for a host. Once added to the host var file, the `check_mk-server` role should be invoked to apply changes to the nagios server.

    disabled_checks: ['apt-security-check']

For further reference see [`check_mk` local checks](http://mathias-kettner.de/checkmk_localchecks.html)

## `backup_postgres`

This was added to identify hosts that need postgres to be backed up, and a
cronjob was added to each host that defines it.

Accepted args are True/False

    backup_postgres=True

## `sites_to_monitor`

This var expects an array with elements `<domainname>:<port>:<http_status>`.
It is used by the `check_mk` play to add http nagios checks.

    sites_to_monitor: ['subdomain.okfn.org:80:301','foo.bar:8000:200']

`http_status` is the expected normal http status return code.

## `sites_enabled`

This var expects an array of domain names, which have been added into the
nginx/apache (sites-available folder) and need to be enabled.

    sites_enabled: ['new-site.okfn.org']

## `rsnapshot_backup`

This var is used by the rsnapshot role to build the rsnaphot config
running on the backup host. It expects one or more array elements which contain key, value pairs (required: `src`, `dest`; optional: `exclude`)

    rsnapshot_backup:
      - { src: 'root@somehost:/home/okfn/', dest: 'somehost/' }
      - { src: 'root@somehost:/var/lib/munin/', dest: 'somehost/' }

## `rsnapshot_backup_scripts`

This var is similar to rsnapshot_backup, except it defines the scripts rsnapshot
needs to run for the backup process of a host. All keys must be defined (`src`, `script`, `dest`)

    rsnapshot_backup_script:
      - { src: '/usr/bin/ssh       somehost.org', script: '"/usr/bin/sudo -u postgres /usr/bin/pg_dumpall | gzip > /var/backups/pgdump.sql.gz"', dest: 'empty/1' }

## `ban_abusive_ips`

This var expects an array of IPs that should be blocked on the server. It is used
by the iptables-persistent role.

    ban_abusive_ips: ['192.168.1.1', '192.168.1.2']

## `custom_iptables_rules`

This var expects an array of rules that should be directly applied to the
server, was added to allow adding custom rules without having to create rule
files for each host.

## `timezone`

This variable allows us to define the timezone for each host/group, which is
then setup by the ntpd role. The defined timezone should be a tz file defined under `/usr/share/zoneinfo`

    timezone: UTC

## `postfix_map_files`

Defines the set of postfix map hash files that postmap should be run on for each host.
