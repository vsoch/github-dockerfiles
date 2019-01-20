# Description

Configures various YUM components on Red Hat-like systems.  Includes
LWRP for managing repositories and their GPG keys.

Based on the work done by Eric Wolfe and Charles Duffy on the
[yumrepo](https://github.com/atomic-penguin/cookbook-yumrepo) cookbook.

# Requirements

Red Hat Enterprise Linux 5, and 6 distributions within this platform
family.

# Attributes

* `yum['exclude']`
    - An array containing a list of packages to exclude from updates or
      installs.  Wildcards and shell globs are supported.
    - Defaults to an empty exclude list.

* `yum['installonlypkgs']`
    - An array containing a list of packages which should only be
      installed, never updated.
    - Defaults to an empty install-only list.

* `yum['ius_release']`
    - Set the IUS release to install.
    - Defaults to the current release of the IUS repo.

* `yum['repoforge_release']`
    - Set the RepoForge release to install.
    - Defaults to the current release of the repoforge repo.

EPEL attributes used in the `yum::epel` recipe, see
`attributes/epel.rb` for default values:

* `yum['epel']['key']`
    - Name of the GPG key used for the repo.

* `yum['epel']['baseurl']`
    - Base URL to an EPEL mirror.

* `yum['epel']['url']`
    - URL to the EPEL mirrorlist.

* `yum['epel']['key_url']`
    - URL to the GPG key for the repo.

* `yum['epel']['includepkgs']`
    - list of packages you want to use for the repo.

* `yum['epel']['exclude']`
    - list of packages you do NOT want to use for the repo.

The `node['yum']['epel_release']` attribute is removed, see the __epel__
recipe information below.

remi attributes used in the `yum::remi` recipe, see
`attributes/remi.rb` for default values:

* `yum['remi']['key']`
    - Name of the GPG key used for the repo.

* `yum['remi']['url']`
    - URL to the remi mirrorlist.

* `yum['remi']['key_url']`
    - URL to the GPG key for the repo.

* `yum['remi']['includepkgs']`
    - list of packages you want to use for the repo.

* `yum['remi']['exclude']`
    - list of packages you do NOT want to use for the repo.

Proxy settings used in yum.conf on RHEL family 5 and 6:

* `yum['proxy']`
    - Set the URL for an HTTP proxy
    - None of the proxy settings are used if this is an empty string
      (default)

* `yum['proxy_username']`
    - Set the username for the proxy
    - not used if `yum['proxy']` above is an empty string

* `yum['proxy_password']`
    - Set the password for the proxy
    - not used if `yum['proxy']` above is an empty string

# Recipes

## default

The default recipe does nothing.

## yum

Manages the configuration of the `/etc/yum.conf` via attributes.  See
the aforementioned Array attributes `yum['exclude']` and
`yum['installonlypkgs']`.

## epel

Uses the `yum_key` and `yum_repository` resources from this cookbook
are used to manage the main EPEL repository. If you need other EPEL
repositories (source, debug-info), use the `yum_repository` LWRP in
your own cookbook where those packages are required. The recipe will
use the `yum['epel']` attributes (see above) to configure the key, url
and download the GPG key for the repo. The defaults are detected by
platform and version and should just work without modification in most
use cases.

On all platforms except Amazon, the action is to add the repository.
On Amazon, the action is add and update.

Amazon Linux has the EPEL repositories already added in the AMI. In
previous versions of this cookbook, they were enabled with
`yum-config-manager`, however in the current version, we manage the
repository using the LWRP. The main difference is that the source and
debuginfo repositories are not available, but if they're needed, add
them using the `yum_repository` LWRP in your own cookbook(s).

## ius

Installs the [IUS Community repositories](http://iuscommunity.org/Repos)
via RPM. Uses the `node['yum']['ius_release']` attribute to select the
right version of the package to install.

The IUS repository requires EPEL, and includes `yum::epel` as a
dependency.

## repoforge

Installs the [RepoForge repositories](http://repoforge.org/)
via RPM. Uses the `node['yum']['repoforge_release']` attribute to select the
right version of the package to install.

The RepoForge repository requires EPEL, and includes `yum::epel` as a
dependency.

## remi

Install the [Les RPM de Remi - Repository](http://rpms.famillecollet.com/)
with the `yum_key` and `yum_repository` resources from this cookbook
are used to manage the remi repository.  Use the `yum['remi']`
attributes (see above) to configure the key, url and download the GPG
key for the repo. The defaults are detected by platform and should
just work without modification in most use cases.

# Resources/Providers

## yum_key

This LWRP handles importing GPG keys for YUM repositories. Keys can be
imported by the `url` parameter or placed in `/etc/pki/rpm-gpg/` by a
recipe and then installed with the LWRP without passing the URL.

### Actions

- :add: installs the GPG key into `/etc/pki/rpm-gpg/`
- :remove: removes the GPG key from `/etc/pki/rpm-gpg/`

#### Attribute Parameters

- key: name attribute. The name of the GPG key to install.
- url: if the key needs to be downloaded, the URL providing the download.

#### Example

``` ruby
# add the Zenoss GPG key
yum_key "RPM-GPG-KEY-zenoss" do
  url "http://dev.zenoss.com/yum/RPM-GPG-KEY-zenoss"
  action :add
end

# remove Zenoss GPG key
yum_key "RPM-GPG-KEY-zenoss" do
  action :remove
end
```

### yum_repository

This LWRP provides an easy way to manage additional YUM repositories.
GPG keys can be managed with the `yum_key` LWRP.  The LWRP automatically
updates the package management cache upon the first run, when a new
repo is added.

#### Actions

- :create: creates a repository file and builds the repository listing
- :add: runs create action if repository file is missing (default)
- :remove: removes the repository file
- :update: updates the repository

#### Attribute Parameters

- repo_name: name attribute. The name of the channel to discover
- description. The description of the repository
- url: The URL providing the packages, used for baseurl in the config
- mirrorlist: Set this as a string containing the URI to the
  mirrorlist, start with "http://", "ftp://", "file://"; use "file://"
  if the mirrorlist is a text file on the system.
- key: Optional, the name of the GPG key file installed by the `key`
  LWRP.
- enabled: Default is `1`, set to `0` if the repository is disabled.
- type: Optional, alternate type of repository
- failovermethod: Optional, failovermethod
- bootstrapurl: Optional, bootstrapurl
- make_cache: Optional, Default is `true`, if `false` then `yum -q
  makecache` will not be ran
- metadata_expire: Optional, Default is nil (or not applied)
- type: Optional, Default is nil (or not applied)

*Note*: When using both url (to set baseurl) and mirrorlist, it is probably a
good idea to also install the fastestmirror plugin, and use
failovermethod "priority".

### Example

``` ruby
# add the Zenoss repository
yum_repository "zenoss" do
  repo_name "zenoss"
  description "Zenoss Stable repo"
  url "http://dev.zenoss.com/yum/stable/"
  key "RPM-GPG-KEY-zenoss"
  action :add
end

# remove Zenoss repo
yum_repository "zenoss" do
  action :remove
end
```

# Usage

Put `recipe[yum::yum]` in the run list to ensure yum is configured
correctly for your environment within your Chef run.

Use the `yum::epel` recipe to enable EPEL, or the `yum::ius` recipe to
enable IUS, or the `yum::repoforge` recipe to enable RepoForge, or the
`yum::remi` recipe to enable remi per __Recipes__ section above.

You can manage GPG keys either with cookbook_file in a recipe if you
want to package it with a cookbook or use the `url` parameter of the
`key` LWRP.

# License and Author

- Author:: Eric G. Wolfe
- Author:: Matt Ray (<matt@opscode.com>)
- Author:: Joshua Timberman (<joshua@opscode.com>)

- Copyright:: 2010 Tippr Inc.
- Copyright:: 2011 Eric G. Wolfe
- Copyright:: 2011-2012 Opscode, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
apache2 Cookbook
================
[![Build Status](https://secure.travis-ci.org/opscode-cookbooks/apache2.png?branch=master)](http://travis-ci.org/opscode-cookbooks/apache2)


This cookbook provides a complete Debian/Ubuntu style Apache HTTPD
configuration. Non-Debian based distributions such as Red Hat/CentOS,
ArchLinux and others supported by this cookbook will have a
configuration that mimics Debian/Ubuntu style as it is easier to
manage with Chef.

Debian-style Apache configuration uses scripts to manage modules and
sites (vhosts). The scripts are:

* a2ensite
* a2dissite
* a2enmod
* a2dismod

This cookbook ships with templates of these scripts for non
Debian/Ubuntu platforms. The scripts are used in the __Definitions__
below.

Requirements
============

## Ohai and Chef:

* Ohai: 0.6.12+
* Chef: 0.10.10+

As of v1.2.0, this cookbook makes use of `node['platform_family']` to
simplify platform selection logic. This attribute was introduced in
Ohai v0.6.12. The recipe methods were introduced in Chef v0.10.10. If
you must run an older version of Chef or Ohai, use [version 1.1.16 of
this cookbook](http://community.opscode.com/cookbooks/apache2/versions/1_1_16/downloads).

## Cookbooks:

This cookbook doesn't have direct dependencies on other cookbooks, as
none are needed for the default recipe or the general use cases.

Depending on your OS configuration and security policy, you may need
additional recipes or cookbooks for this cookbook's recipes to
converge on the node. In particular, the following Operating System
settings may affect the behavior of this cookbook:

* apt cache outdated
* SELinux enabled
* IPtables
* Compile tools
* 3rd party repositories

On Ubuntu/Debian, use Opscode's `apt` cookbook to ensure the package
cache is updated so Chef can install packages, or consider putting
apt-get in your bootstrap process or
[knife bootstrap template](http://wiki.opscode.com/display/chef/Knife+Bootstrap).

On RHEL, SELinux is enabled by default. The `selinux` cookbook
contains a `permissive` recipe that can be used to set SELinux to
"Permissive" state. Otherwise, additional recipes need to be created
by the user to address SELinux permissions.

The easiest but **certainly not ideal way** to deal with IPtables is
to flush all rules. Opscode does provide an `iptables` cookbook but is
migrating from the approach used there to a more robust solution
utilizing a general "firewall" LWRP that would have an "iptables"
provider. Alternately, you can use ufw, with Opscode's `ufw` and
`firewall` cookbooks to set up rules. See those cookbooks' READMEs for
documentation.

Build/compile tools may not be installed on the system by default.
Some recipes (e.g., `apache2::mod_auth_openid`) build the module from
source. Use Opscode's `build-essential` cookbook to get essential
build packages installed.

On ArchLinux, if you are using the `apache2::mod_auth_openid` recipe,
you also need the `pacman` cookbook for the `pacman_aur` LWRP. Put
`recipe[pacman]` on the node's expanded run list (on the node or in a
role). This is not an explicit dependency because it is only required
for this single recipe and platform; the pacman default recipe
performs `pacman -Sy` to keep pacman's package cache updated.

The `apache2::god_monitor` recipe uses a definition from the `god`
cookbook. Include `recipe[god]` in the node's expanded run list to
ensure that the cookbook is available to the node, and to set up `god`.

## Platforms:

The following platforms and versions are tested and supported using
Opscode's [test-kitchen](http://github.com/opscode/test-kitchen).

* Ubuntu 10.04, 12.04
* CentOS 5.8, 6.3

The following platform families are supported in the code, and are
assumed to work based on the successful testing on Ubuntu and CentOS.

* Debian
* Red Hat (rhel)
* Fedora
* Amazon Linux

The following platforms are also supported in the code, have been
tested manually but are not tested under test-kitchen.

* SUSE/OpenSUSE
* ArchLinux
* FreeBSD

### Notes for RHEL Family:

On Red Hat Enterprise Linux and derivatives, the EPEL repository may
be necessary to install packages used in certain recipes. The
`apache2::default` recipe, however, does not require any additional
repositories. Opscode's `yum` cookbook contains a recipe to add the
EPEL repository. See __Examples__ for more information.

### Notes for FreeBSD:

The `apache2::mod_php5` recipe depends on the `freebsd` cookbook,
which it uses to set the correct options for compiling the `php5` port
from sources. You need to ensure the `freebsd` is in the expanded run
list, or this recipe will fail. We don't set an explicit dependency
because we feel the `freebsd` cookbook is something users would want
on their nodes, and due to the generality of this cookbook we don't
want additional specific dependencies.

Tests
=====

This cookbook in the
[source repository](https://github.com/opscode-cookbooks/apache2)
contains minitest and cucumber tests. This is an initial proof of
concept that will be fleshed out with more supporting infrastructure
at a future time.

Please see the CONTRIBUTING file for information on how to add tests
for your contributions.

Attributes
==========

This cookbook uses many attributes, broken up into a few different
kinds.

Platform specific
-----------------

In order to support the broadest number of platforms, several
attributes are determined based on the node's platform. See the
attributes/default.rb file for default values in the case statement at
the top of the file.

* `node['apache']['dir']` - Location for the Apache configuration
* `node['apache']['log_dir']` - Location for Apache logs
* `node['apache']['error_log']` - Location for the default error log
* `node['apache']['access_log']` - Location for the default access log
* `node['apache']['user']` - User Apache runs as
* `node['apache']['group']` - Group Apache runs as
* `node['apache']['binary']` - Apache httpd server daemon
* `node['apache']['icondir']` - Location for icons
* `node['apache']['cache_dir']` - Location for cached files used by Apache itself or recipes
* `node['apache']['pid_file']` - Location of the PID file for Apache httpd
* `node['apache']['lib_dir']` - Location for shared libraries
* `node['apache']['default_site_enabled']` - Default site enabled. Default is false.
* `node['apache']['ext_status']` - if true, enables ExtendedStatus for `mod_status`

General settings
----------------

These are general settings used in recipes and templates. Default
values are noted.

* `node['apache']['listen_addresses']` - Addresses that httpd should listen on. Default is any ("*").
* `node['apache']['listen_ports']` - Ports that httpd should listen on. Default is port 80.
* `node['apache']['contact']` - Value for ServerAdmin directive. Default "ops@example.com".
* `node['apache']['timeout']` - Value for the Timeout directive. Default is 300.
* `node['apache']['keepalive']` - Value for the KeepAlive directive. Default is On.
* `node['apache']['keepaliverequests']` - Value for MaxKeepAliveRequests. Default is 100.
* `node['apache']['keepalivetimeout']` - Value for the KeepAliveTimeout directive. Default is 5.
* `node['apache']['default_modules']` - Array of module names. Can take "mod_FOO" or "FOO" as names, where FOO is the apache module, e.g. "`mod_status`" or "`status`".

The modules listed in `default_modules` will be included as recipes in `recipe[apache::default]`.

Prefork attributes
------------------

Prefork attributes are used for tuning the Apache HTTPD prefork MPM
configuration.

* `node['apache']['prefork']['startservers']` - initial number of server processes to start. Default is 16.
* `node['apache']['prefork']['minspareservers']` - minimum number of spare server processes. Default 16.
* `node['apache']['prefork']['maxspareservers']` - maximum number of spare server processes. Default 32.
* `node['apache']['prefork']['serverlimit']` - upper limit on configurable server processes. Default 400.
* `node['apache']['prefork']['maxclients']` - Maximum number of simultaneous connections.
* `node['apache']['prefork']['maxrequestsperchild']` - Maximum number of request a child process will handle. Default 10000.

Worker attributes
-----------------

Worker attributes are used for tuning the Apache HTTPD worker MPM
configuration.

* `node['apache']['worker']['startservers']` - Initial number of server processes to start. Default 4
* `node['apache']['worker']['serverlimit']` - upper limit on configurable server processes. Default 16.
* `node['apache']['worker']['maxclients']` - Maximum number of simultaneous connections. Default 1024.
* `node['apache']['worker']['minsparethreads']` - Minimum number of spare worker threads. Default 64
* `node['apache']['worker']['maxsparethreads']` - Maximum number of spare worker threads. Default 192.
* `node['apache']['worker']['maxrequestsperchild']` - Maximum number of requests a child process will handle.

mod\_auth\_openid attributes
----------------------------

The following attributes are in the `attributes/mod_auth_openid.rb`
file. Like all Chef attributes files, they are loaded as well, but
they're logistically unrelated to the others, being specific to the
`mod_auth_openid` recipe.

* `node['apache']['mod_auth_openid']['checksum']` - sha256sum of the tarball containing the source.
* `node['apache']['mod_auth_openid']['ref']` - Any sha, tag, or branch found from https://github.com/bmuller/mod_auth_openid
* `node['apache']['mod_auth_openid']['cache_dir']` - the cache directory is where the sqlite3 database is stored. It is separate so it can be managed as a directory resource.
* `node['apache']['mod_auth_openid']['dblocation']` - filename of the sqlite3 database used for directive `AuthOpenIDDBLocation`, stored in the `cache_dir` by default.
* `node['apache']['mod_auth_openid']['configure_flags']` - optional array of configure flags passed to the `./configure` step in the compilation of the module.

mod\_ssl attributes
-------------------

* `node['apache']['mod_ssl']['cipher_suite']` - sets the
  SSLCiphersuite value to the specified string. The default is
  considered "sane" but you may need to change it for your local
  security policy, e.g. if you have PCI-DSS requirements. Additional
  commentary on the
  [original pull request](https://github.com/opscode-cookbooks/apache2/pull/15#commitcomment-1605406).

Recipes
=======

Most of the recipes in the cookbook are for enabling Apache modules.
Where additional configuration or behavior is used, it is documented
below in more detail.

The following recipes merely enable the specified module: `mod_alias`,
`mod_basic`, `mod_digest`, `mod_authn_file`, `mod_authnz_ldap`,
`mod_authz_default`, `mod_authz_groupfile`, `mod_authz_host`,
`mod_authz_user`, `mod_autoindex`, `mod_cgi`, `mod_dav_fs`,
`mod_dav_svn`, `mod_deflate`, `mod_dir`, `mod_env`, `mod_expires`,
`mod_headers`, `mod_ldap`, `mod_log_config`, `mod_mime`,
`mod_negotiation`, `mod_proxy`, `mod_proxy_ajp`, `mod_proxy_balancer`,
`mod_proxy_connect`, `mod_proxy_http`, `mod_python`, `mod_rewrite`,
`mod_setenvif`, `mod_status`, `mod_wsgi`, `mod_xsendfile`.

On RHEL Family distributions, certain modules ship with a config file
with the package. The recipes here may delete those configuration
files to ensure they don't conflict with the settings from the
cookbook, which will use per-module configuration in
`/etc/httpd/mods-enabled`.

default
-------

The default recipe does a number of things to set up Apache HTTPd. It
also includes a number of modules based on the attribute
`node['apache']['default_modules']` as recipes.

logrotate
---------

Logrotate adds a logrotate entry for your apache2 logs. This recipe
requires the `logrotate` cookbook; ensure that `recipe[logrotate]` is
in the node's expanded run list.

mod\_auth\_cas
--------------

This recipe installs the proper package and enables the `auth_cas`
module. It can install from source or package. Package is the default,
set the attribute `node['apache']['mod_auth_cas']['from_source']` to
true to enable source installation. Modify the version to install by
changing the attribute
`node['apache']['mod_auth_cas']['source_revision']`. It is a version
tag by default, but could be master, or another tag, or branch.

The module configuration is written out with the `CASCookiePath` set,
otherwise an error loading the module may cause Apache to not start.

**Note**: This recipe does not work on EL 6 platforms unless
epel-testing repository is enabled (outside the scope of this
cookbook), or the package version 1.0.8.1-3.el6 or higher is otherwise
available to the system due to this bug:

https://bugzilla.redhat.com/show_bug.cgi?format=multiple&id=708550

mod\_auth\_openid
-----------------

**Changed via COOK-915**

This recipe compiles the module from source. In addition to
`build-essential`, some other packages are included for installation
like the GNU C++ compiler and development headers.

To use the module in your own cookbooks to authenticate systems using
OpenIDs, specify an array of OpenIDs that are allowed to authenticate
with the attribute `node['apache']['allowed_openids']`. Use the
following in a vhost to protect with OpenID authentication:

    AuthType OpenID require user <%= node['apache']['allowed_openids'].join(' ') %>
    AuthOpenIDDBLocation <%= node['apache']['mod_auth_openid']['dblocation'] %>

Change the DBLocation with the attribute as required; this file is in
a different location than previous versions, see below. It should be a
sane default for most platforms, though, see
`attributes/mod_auth_openid.rb`.

### Changes from COOK-915:

* `AuthType OpenID` instead of `AuthOpenIDEnabled On`.
* `require user` instead of `AuthOpenIDUserProgram`.
* A bug(?) in `mod_auth_openid` causes it to segfault when attempting
  to update the database file if the containing directory is not
  writable by the HTTPD process owner (e.g., www-data), even if the
  file is writable. In order to not interfere with other settings from
  the default recipe in this cookbook, the db file is moved.

mod\_fastcgi
------------

Install the fastcgi package and enable the module.

Only work on Debian/Ubuntu

mod\_fcgid
----------

Installs the fcgi package and enables the module. Requires EPEL on
RHEL family.

On RHEL family, this recipe will delete the fcgid.conf and on version
6+, create the /var/run/httpd/mod_fcgid` directory, which prevents the
emergency error:

    [emerg] (2)No such file or directory: mod_fcgid: Can't create shared memory for size XX bytes

mod\_php5
--------

Simply installs the appropriate package on Debian, Ubuntu and
ArchLinux.

On Red Hat family distributions including Fedora, the php.conf that
comes with the package is removed. On RHEL platforms less than v6, the
`php53` package is used.

mod\_ssl
--------

Besides installing and enabling `mod_ssl`, this recipe will append
port 443 to the `node['apache']['listen_ports']` attribute array and
update the ports.conf.

god\_monitor
------------

Sets up a `god` monitor for Apache. External requirements are the
`god` and `runit` cookbooks from Opscode. When using this recipe,
include `recipe[god]` in the node's expanded run list to ensure the
client downloads it; `god` depends on runit so that will also be
downloaded.

**Note** This recipe is not tested under test-kitchen yet and is
  pending fix in COOK-744.

Definitions
===========

The cookbook provides a few definitions. At some point in the future
these definitions may be refactored into lightweight resources and
providers as suggested by
[foodcritic rule FC015](http://acrmp.github.com/foodcritic/#FC015).

apache\_conf
------------

Sets up configuration file for an Apache module from a template. The
template should be in the same cookbook where the definition is used.
This is used by the `apache_module` definition and is not often used
directly.

This will use a template resource to write the module's configuration
file in the `mods-available` under the Apache configuration directory
(`node['apache']['dir']`). This is a platform-dependent location. See
__apache\_module__.

### Parameters:

* `name` - Name of the template. When used from the `apache_module`,
  it will use the same name as the module.

### Examples:

Create `#{node['apache']['dir']}/mods-available/alias.conf`.

    apache_conf "alias"

apache\_module
--------------

Enable or disable an Apache module in
`#{node['apache']['dir']}/mods-available` by calling `a2enmod` or
`a2dismod` to manage the symbolic link in
`#{node['apache']['dir']}/mods-enabled`. If the module has a
configuration file, a template should be created in the cookbook where
the definition is used. See __Examples__.

### Parameters:

* `name` - Name of the module enabled or disabled with the `a2enmod` or `a2dismod` scripts.
* `identifier` - String to identify the module for the `LoadModule` directive. Not typically needed, defaults to `#{name}_module`
* `enable` - Default true, which uses `a2enmod` to enable the module. If false, the module will be disabled with `a2dismod`.
* `conf` - Default false. Set to true if the module has a config file, which will use `apache_conf` for the file.
* `filename` - specify the full name of the file, e.g.

### Examples:

Enable the ssl module, which also has a configuration template in `templates/default/mods/ssl.conf.erb`.

    apache_module "ssl" do
      conf true
    end

Enable the php5 module, which has a different filename than the module default:

    apache_module "php5" do
      filename "libphp5.so"
    end

Disable a module:

    apache_module "disabled_module" do
      enable false
    end

See the recipes directory for many more examples of `apache_module`.

apache\_site
------------

Enable or disable a VirtualHost in
`#{node['apache']['dir']}/sites-available` by calling a2ensite or
a2dissite to manage the symbolic link in
`#{node['apache']['dir']}/sites-enabled`.

The template for the site must be managed as a separate resource. To
combine the template with enabling a site, see `web_app`.

### Parameters:

* `name` - Name of the site.
* `enable` - Default true, which uses `a2ensite` to enable the site. If false, the site will be disabled with `a2dissite`.

web\_app
--------

Manage a template resource for a VirtualHost site, and enable it with
`apache_site`. This is commonly done for managing web applications
such as Ruby on Rails, PHP or Django, and the default behavior
reflects that. However it is flexible.

This definition includes some recipes to make sure the system is
configured to have Apache and some sane default modules:

* `apache2`
* `apache2::mod_rewrite`
* `apache2::mod_deflate`
* `apache2::mod_headers`

It will then configure the template (see __Parameters__ and
__Examples__ below), and enable or disable the site per the `enable`
parameter.

### Parameters:

Current parameters used by the definition:

* `name` - The name of the site. The template will be written to
  `#{node['apache']['dir']}/sites-available/#{params['name']}.conf`
* `cookbook` - Optional. Cookbook where the source template is. If
  this is not defined, Chef will use the named template in the
  cookbook where the definition is used.
* `template` - Default `web_app.conf.erb`, source template file.
* `enable` - Default true. Passed to the `apache_site` definition.

Additional parameters can be defined when the definition is called in
a recipe, see __Examples__.

### Examples:

All parameters are passed into the template. You can use whatever you
like. The apache2 cookbook comes with a `web_app.conf.erb` template as
an example. The following parameters are used in the template:

* `server_name` - ServerName directive.
* `server_aliases` - ServerAlias directive. Must be an array of aliases.
* `docroot` - DocumentRoot directive.
* `application_name` - Used in RewriteLog directive. Will be set to the `name` parameter.
* `directory_index` - Allow overriding the default DirectoryIndex setting, optional
* `directory_options` - Override Options on the docroot, for example to add parameters like Includes or Indexes, optional.
* `allow_override` - Modify the AllowOverride directive on the docroot to support apps that need .htaccess to modify configuration or require authentication.

To use the default web_app, for example:

    web_app "my_site" do
      server_name node['hostname']
      server_aliases [node['fqdn'], "my-site.example.com"]
      docroot "/srv/www/my_site"
    end

The parameters specified will be used as:

* `@params[:server_name]`
* `@params[:server_aliases]`
* `@params[:docroot]`

In the template. When you write your own, the `@` is significant.

For more information about Definitions and parameters, see the
[Chef Wiki](http://wiki.opscode.com/display/chef/Definitions)

Usage
=====

Using this cookbook is relatively straightforward. Add the desired
recipes to the run list of a node, or create a role. Depending on your
environment, you may have multiple roles that use different recipes
from this cookbook. Adjust any attributes as desired. For example, to
create a basic role for web servers that provide both HTTP and HTTPS:

    % cat roles/webserver.rb
    name "webserver"
    description "Systems that serve HTTP and HTTPS"
    run_list(
      "recipe[apache2]",
      "recipe[apache2::mod_ssl]"
    )
    default_attributes(
      "apache" => {
        "listen_ports" => ["80", "443"]
      }
    )

For examples of using the definitions in your own recipes, see their
respective sections above.

License and Authors
===================

* Author:: Adam Jacob <adam@opscode.com>
* Author:: Joshua Timberman <joshua@opscode.com>
* Author:: Bryan McLellan <bryanm@widemile.com>
* Author:: Dave Esposito <esposito@espolinux.corpnet.local>
* Author:: David Abdemoulaie <github@hobodave.com>
* Author:: Edmund Haselwanter <edmund@haselwanter.com>
* Author:: Eric Rochester <err8n@virginia.edu>
* Author:: Jim Browne <jbrowne@42lines.net>
* Author:: Matthew Kent <mkent@magoazul.com>
* Author:: Nathen Harvey <nharvey@customink.com>
* Author:: Ringo De Smet <ringo.de.smet@amplidata.com>
* Author:: Sean OMeara <someara@opscode.com>
* Author:: Seth Chisamore <schisamo@opscode.com>
* Author:: Gilles Devaux <gilles@peerpong.com>

* Copyright:: 2009-2012, Opscode, Inc
* Copyright:: 2011, Atriso
* Copyright:: 2011, CustomInk, LLC.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
These configs are taken from a Debian apache2.2-common 2.2.11-3 install. They 
work on CentOS 5.3 with a few conditions using erb. 
Description
===========

Website:: https://github.com/brianbianco/redisio

Installs and configures Redis server instances

Requirements
============

This cookbook builds redis from source, so it should work on any architecture for the supported distributions.  Init scripts are installed into /etc/init.d/
It depends on the ulimit cookbook: https://github.com/bmhatfield/chef-ulimit

Platforms
---------

* Debian, Ubuntu
* CentOS, Red Hat, Fedora, Scientific Linux

Tested on:

* Ubuntu 10.10, 12.04
* Debian 6.0
* Fedora 16
* Scientific Linux 6.2
* Centos 6.2, 6.3

Usage
=====

The redisio cookbook contains an LWRP for installing and uninstalling redis. It also contains 6 recipes for installation and usage of redis.

The install recipe will build, compile, install and configure redis as well as setup service resources for it.  These resources will be named for the port of the redis server, unless a "name" attribute was specified.  Example names would be: service["redis6379"] or service["redismaster"] if the name attribute was "master"

The most common use case for the redisio cookbook is to use the install recipe followed by the enable recipe.  

Another common use case is to use the install recipe, and then call the service resources created by it from another cookbook.  

It is important to note that changing the configuration options of redis does not make them take effect on the next chef run.  Due to how redis works, you cannot reload a configuration without restarting the redis service.  Redis does not offer a reload option, in order to have new options be used redis must be stopped and started. 

You should make sure to set the ulimit for the user you want to run redis as to be higher than the max connections you allow.

The disable recipe just stops redis and removes it from run levels.

The uninstall recipe, and LWRP are used to remove the configuration files and redis binaries.  This is not commonly used and may be removed in future releases.

The cookbook also contains a recipe to allow for the installation of the redis ruby gem. 

Recipes
-------

* default - This is used to install the pre-requisites for building redis, and to make the LWRPs available
* disable - This recipe can be used to disable the redis service and remove it from runlevels
* enable - This recipe can be used to enable the redis services and add it to runlevels
* install - This recipe is used to install AND configure redis.  The name is a little misleading, sorry :)
* redis_gem - This recipe can be used to install the redis ruby gem
* uninstall - This recipe can be used to remove the configuration files and redis binaries

Role File Examples
------------------

#### Install redis and setup an instance with default settings on default port, and start the service through a role file #

```ruby
run_list *%w[
  recipe[redisio::install]
  recipe[redisio::enable]
]

default_attributes({})
```

#### Install redis, give the instance a name, and use a unix socket #

```ruby
run_list *%w[
  recipe[redisio::install]
  recipe[redisio::enable]
]

default_attributes({
  'redisio' => {
    'servers' => [
      {'name' => 'master', 'port' => '6379', 'unixsocket' => '/tmp/redis.sock', 'unixsocketperm' => '755'},
    ]
  }
})
```

#### Install redis and setup two instances on the same server, on different ports, with one slaved to the other through a role file #

```ruby
run_list *%w[
  recipe[redisio::install]
  recipe[redisio::enable]
]

default_attributes({
  'redisio' => {
    'servers' => [
      {'port' => '6379'},
      {'port' => '6380', 'slaveof' => { 'address' => '127.0.0.1', 'port' => '6379' }}
    ]
  }
})
```

#### Install redis and setup two instances, on the same server, on different ports, with the default data directory changed to /mnt/redis, and the second instance named#

```ruby
run_list *%w[
  recipe[redisio::install]
  recipe[redisio::enable]
]

default_attributes({
  'redisio' => {
    'default_settings' => {'datadir' => '/mnt/redis'},
    'servers' => [{'port' => '6379'}, {'port' => '6380', 'name' => "MyInstance"}]
  }
})
```

#### Install redis and setup three instances on the same server, changing the default data directory to /mnt/redis, each instance will use a different backup type, and one instance will use a different data dir #

```ruby
run_list *%w[
  recipe[redisio::install]
  recipe[redisio::enable]
]

default_attributes({
  'redisio' => {
    'default_settings' => { 'datadir' => '/mnt/redis/'},
    'servers' => [
      {'port' => '6379','backuptype' => 'aof'},
      {'port' => '6380','backuptype' => 'both'}
      {'port' => '6381','backuptype' => 'rdb', 'datadir' => '/mnt/redis6381'}
    ]
  }
})
```

#### Install redis 2.4.11 (lower than the default version) and turn safe install off, for the event where redis is already installed.  This will use the default settings.  Keep in mind the redis version will not actually be updated until you restart the service (either through the LWRP or manually). #

```ruby
run_list *%w[
  recipe[redisio::install]
  recipe[redisio::enable]
]

default_attributes({
  'redisio' => {
    'safe_install' => false,
    'version'      => '2.4.11'
  }
})
```

#### Install version 2.2.2 of the redis ruby gem, if you don't list the version, it will simply install the latest available. #

```ruby
run_list *%w[
  recipe[redisio::redis_gem]
]

default_attributes({
  'redisio' => {
    'gem' => {
      'version' => '2.2.2'
    }
  }
})
```

LWRP Examples
-------------

Instead of using my provided recipes, you can simply include the redisio default in your role and use the LWRP's yourself.  I will show a few examples of ways to use the LWRPS, detailed breakdown of options are below
in the resources/providers section

install resource
----------------

It is important to note that this call has certain expectations for example, it expects the redis package to be in the format `redis-VERSION.tar.gz'.  The servers resource expects an array of hashes where each hash is required to contain at a key-value pair of 'port' => '<port numbers>'.

```ruby
redisio_install "redis-servers" do
  version '2.6.9'
  download_url 'http://redis.googlecode.com/files/redis-2.6.9.tar.gz'
  default_settings node['redisio']['default_settings']
  servers node['redisio']['servers']
  safe_install false
  base_piddir node['redisio']['base_piddir']
end
```

uninstall resource
------------------

I generally don't recommend using this LWRP or recipe at all, but in the event you really want to remove files, these are available.


This will only remove the redis binary files if they exist, nothing else.

```ruby
redisio_uninstall "redis-servers" do
  action :run
end
```

This will remove the redis binaries, as well as the init script and configuration files for the specified server. This will not remove any data files

```ruby
redisio_uninstall "redis-servers" do
  servers [{'port' => '6379'}]
  action :run
end
```

service resource
----------------

The install recipe sets up a service resource for each redis instance.  In the past there was a custom service LWRP called "redisio_service".  This is deprecated and should no longer be used.
I have left the resource available so as to not break it for anybody who happens to be calling it themselves from other cookbooks. 

The service resources created will use the 'name' attribute if it is specified, and will default to the port as it's name if no name is given.

Using the service resources:

```ruby
service "redis6379" do
  action :start
end
```

Or if you have named your server "Master"

```ruby
service "redisMaster" do
  action :start
end
```

Attributes
==========

Configuration options, each option corresponds to the same-named configuration option in the redis configuration file;  default values listed

* `redisio['mirror']` - mirror server with path to download redis package, default is https://redis.googlecode.com/files
* `redisio['base_name']` - the base name of the redis package to be downloaded (the part before the version), default is 'redis-'
* `redisio['artifact_type']` - the file extension of the package.  currently only .tar.gz and .tgz are supported, default is 'tar.gz'
* `redisio['version']` - the version number of redis to install (also appended to the `base_name` for downloading), default is '2.6.10'
* `redisio['safe_install'] - prevents redis from installing itself if another version of redis is installed, default is true
* `redisio['base_piddir'] - This is the directory that redis pidfile directories and pidfiles will be placed in.  Since redis can run as non root, it needs to have proper
                           permissions to the directory to create its pid.  Since each instance can run as a different user, these directories will all be nested inside this base one.
* `redisio['install_dir'] - This is the directory that redis will install its binaries.  Defaults to nil which uses the redis default (/usr/local/bin)


Default settings is a hash of default settings to be applied to to ALL instances.  These can be overridden for each individual server in the servers attribute.  If you are going to set logfile to a specific file, make sure to set syslog-enabled to no.

* `redisio['default_settings']` - { 'redis-option' => 'option setting' }

Available options and their defaults

```
'user'                   => 'redis' - the user to own the redis datadir, redis will also run under this user
'group'                  => 'redis' - the group to own the redis datadir
'homedir'                => Home directory of the user. Varies on distribution, check attributes file 
'shell'                  => Users shell. Varies on distribution, check attributes file
'systemuser'             => true - Sets up the instances user as a system user
'ulimit'                 => 0 - 0 is a special value causing the ulimit to be maxconnections +32.  Set to nil or false to disable setting ulimits
'configdir'              => '/etc/redis' - configuration directory
'name'                   => nil, Allows you to name the server with something other than port.  Useful if you want to use unix sockets
'address'                => nil,
'databases'              => '16',
'backuptype'             => 'rdb',
'datadir'                => '/var/lib/redis',
'unixoscket'             => nil - The location of the unix socket to use,
'unixsocketperm'         => nil - The permissions of the unix socket,
'timeout'                => '0',
'loglevel'               => 'verbose',
'logfile'                => nil,
'syslogenabled'         => 'yes',
'syslogfacility         => 'local0',
'save'                   => nil, - This attribute is nil but defaults to ['900 1','300 10','60 10000'], if you want to disable saving use an empty string 
'slaveof'                => nil,
'job_control'            => 'initd', - options are 'initd' and 'upstart'
'masterauth'             => nil,
'slaveservestaledata'    => 'yes',
'replpingslaveperiod'    => '10',
'repltimeout'            => '60',
'requirepass'            => nil,
'maxclients'             => '10000',
'maxmemory'              => nil, - This allows the use of percentages, you must append % to the number.
'maxmemorypolicy'        => 'volatile-lru',
'maxmemorysamples'       => '3',
'appendfsync'            => 'everysec',
'noappendfsynconrewrite' => 'no',
'aofrewritepercentage'   => '100',
'aofrewriteminsize'      => '64mb',
'cluster-enabled'        => 'no',
'cluster-config-file'    => nil, # Defaults to redis instance name inside of template if cluster is enabled.
'cluster-node-timeout'   => 5,
'includes'               => nil
```

* `redisio['servers']` - An array where each item is a set of key value pairs for redis instance specific settings.  The only required option is 'port'.  These settings will override the options in 'default_settings', if it is left empty it will default to [{'port' => '6379'}]

The redis_gem recipe  will also allow you to install the redis ruby gem, these are attributes related to that, and are in the redis_gem attributes file.

* `redisio['gem']['name']` - the name of the gem to install, defaults to 'redis'  
* `redisio['gem']['version']` -  the version of the gem to install.  if it is nil, the latest available version will be installed.

Resources/Providers
===================

This cookbook contains 2 LWRP's, and service resources for each instance of redis.

`service`
---------

Actions:

* `start`
* `stop`
* `restart`
* `enable`
* `disable`

Simply provide redis<server_name> where server name is the port if you haven't given it a name.

```ruby
service "redis<server_name>" do
  action [:start,:stop,:restart,:enable,:disable]
end
```

`install`
--------

Actions:

* `run` - perform the install (default)
* `nothing` - do nothing

Attribute Parameters

* `version` - the version of redis to download / install
* `download_url` - the URL plus filename of the redis package to install
* `download_dir` - the directory to store the downloaded package
* `artifact_type` - the file extension of the package
* `base_name` - the name of the package minus the extension and version number
* `user` - the user to run redis as, and to own the redis files
* `group` - the group to own the redis files
* `default_settings` - a hash of the default redis server settings
* `servers` - an array of hashes containing server configurations overrides (port is the only required)
* `safe_install` - a true or false value which determines if a version of redis will be installed if one already exists, defaults to true

This resource expects the following naming conventions:

package file should be in the format <base_name><version_number>.<artifact_type>

package file after extraction should be inside of the directory <base_name><version_number>

```ruby
install "redis" do
  action [:run,:nothing]
end
```

`uninstall`
----------

Actions:

* `run` - perform the uninstall
* `nothing` - do nothing (default)

Attribute Parameters

* `servers` - an array of hashes containing the port number of instances to remove along with the binarires.  (it is fine to pass in the same hash you used to install, even if there are additional
              only the port is used)

```ruby
uninstall "redis" do
  action [:run,:nothing]
end
```

License and Author
==================

Author:: [Brian Bianco] (<brian.bianco@gmail.com>)
Author\_Website:: http://www.brianbianco.com
Twitter:: @brianwbianco
IRC:: geekbri on freenode

Copyright 2013, Brian Bianco

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Description
===========

This cookbook includes recipes to execute apt-get update to ensure the
local APT package cache is up to date. There are recipes for managing
the apt-cacher-ng caching proxy and proxy clients. It also includes a
LWRP for managing APT repositories in /etc/apt/sources.list.d as well as
an LWRP for pinning packages via /etc/apt/preferences.d.

Requirements
============

Version 1.8.2+ of this cookbook requires **Chef 10.16.4** or later.

If your Chef version is earlier than 10.16.4, use version 1.7.0 of
this cookbook.

See [CHEF-3493](http://tickets.opscode.com/browse/CHEF-3493) and
[this code comment](http://bit.ly/VgvCgf) for more information on this
requirement.

Platform
--------

* Debian
* Ubuntu

May work with or without modification on other Debian derivatives.

Recipes
=======

default
-------

This recipe installs the `update-notifier-common` package to provide
the timestamp file used to only run `apt-get update` if the cache is
more than one day old.

This recipe should appear first in the run list of Debian or Ubuntu
nodes to ensure that the package cache is up to date before managing
any `package` resources with Chef.

This recipe also sets up a local cache directory for preseeding packages.

cacher-ng
---------

Installs the `apt-cacher-ng` package and service so the system can
provide APT caching. You can check the usage report at
http://{hostname}:3142/acng-report.html. The `cacher-ng` recipe
includes the `cacher-client` recipe, so it helps seed itself.

cacher-client
-------------
Configures the node to use the `apt-cacher-ng` server as a client. If you
want to restrict your node to using the `apt-cacher-ng` server in your
Environment, set `['apt']['cacher-client']['restrict_environment']` to `true`.
To use a cacher server (or standard proxy server) not available via search
set the atttribute `['apt']['cacher-ipaddress']` and for a custom port
set `['apt']['cacher_port']`

Resources/Providers
===================

Managing repositories
---------------------

This LWRP provides an easy way to manage additional APT repositories.
Adding a new repository will notify running the `execute[apt-get-update]`
resource immediately.

# Actions

- :add: creates a repository file and builds the repository listing
- :remove: removes the repository file

# Attribute Parameters

- repo_name: name attribute. The name of the channel to discover
- uri: the base of the Debian distribution
- distribution: this is usually your release's codename...ie something
  like `karmic`, `lucid` or `maverick`
- components: package groupings..when it doubt use `main`
- arch: constrain package to a particular arch like `i386`, `amd64` or
  even `armhf` or `powerpc`. Defaults to nil.
- deb_src: whether or not to add the repository as a source repo as
  well - value can be `true` or `false`, default `false`.
- keyserver: the GPG keyserver where the key for the repo should be retrieved
- key: if a `keyserver` is provided, this is assumed to be the
  fingerprint, otherwise it can be either the URI to the GPG key for
  the repo, or a cookbook_file.
- key_proxy: if set, pass the specified proxy via `http-proxy=` to GPG.
- cookbook: if key should be a cookbook_file, specify a cookbook where
  the key is located for files/default. Defaults to nil, so it will
  use the cookbook where the resource is used.

# Examples

    # add the Zenoss repo
    apt_repository "zenoss" do
      uri "http://dev.zenoss.org/deb"
      components ["main","stable"]
    end

    # add the Nginx PPA; grab key from keyserver
    apt_repository "nginx-php" do
      uri "http://ppa.launchpad.net/nginx/php5/ubuntu"
      distribution node['lsb']['codename']
      components ["main"]
      keyserver "keyserver.ubuntu.com"
      key "C300EE8C"
    end

    # add the Nginx PPA; grab key from keyserver, also add source repo
    apt_repository "nginx-php" do
      uri "http://ppa.launchpad.net/nginx/php5/ubuntu"
      distribution node['lsb']['codename']
      components ["main"]
      keyserver "keyserver.ubuntu.com"
      key "C300EE8C"
      deb_src true
    end

    # add the Cloudkick Repo
    apt_repository "cloudkick" do
      uri "http://packages.cloudkick.com/ubuntu"
      distribution node['lsb']['codename']
      components ["main"]
      key "http://packages.cloudkick.com/cloudkick.packages.key"
    end

    # add the Cloudkick Repo with the key downloaded in the cookbook
    apt_repository "cloudkick" do
      uri "http://packages.cloudkick.com/ubuntu"
      distribution node['lsb']['codename']
      components ["main"]
      key "cloudkick.packages.key"
    end

    # add the Cloudera Repo of CDH4 packages for Ubuntu 12.04 on AMD64
    apt_repository "cloudera" do
      uri "http://archive.cloudera.com/cdh4/ubuntu/precise/amd64/cdh"
      arch "amd64"
      distribution "precise-cdh4"
      components ["contrib"]
      key "http://archive.cloudera.com/debian/archive.key"
    end

    # remove Zenoss repo
    apt_repository "zenoss" do
      action :remove
    end

Pinning packages
----------------

This LWRP provides an easy way to pin packages in /etc/apt/preferences.d.
Although apt-pinning is quite helpful from time to time please note that Debian
does not encourage its use without thorough consideration.

Further information regarding apt-pinning is available via
http://wiki.debian.org/AptPreferences.

# Actions

- :add: creates a preferences file under /etc/apt/preferences.d
- :remove: Removes the file, therefore unpin the package

# Attribute Parameters

- package_name: name attribute. The name of the package
- glob: Pin by glob() expression or regexp surrounded by /.
- pin: The package version/repository to pin
- pin_priority: The pinning priority aka "the highest package version wins"

# Examples

    # Pin libmysqlclient16 to version 5.1.49-3
    apt_preference "libmysqlclient16" do
      pin "version 5.1.49-3"
      pin_priority "700"
    end

    # Unpin libmysqlclient16
    apt_preference "libmysqlclient16" do
      action :remove
    end

    # Pin all packages from dotdeb.org
    apt_preference "dotdeb" do
      glob "*"
      pin "origin packages.dotdeb.org "
      pin_priority "700"
    end

Usage
=====

Put `recipe[apt]` first in the run list. If you have other recipes
that you want to use to configure how apt behaves, like new sources,
notify the execute resource to run, e.g.:

    template "/etc/apt/sources.list.d/my_apt_sources.list" do
      notifies :run, resources(:execute => "apt-get update"), :immediately
    end

The above will run during execution phase since it is a normal
template resource, and should appear before other package resources
that need the sources in the template.

Put `recipe[apt::cacher-ng]` in the run_list for a server to provide
APT caching and add `recipe[apt::cacher-client]` on the rest of the
Debian-based nodes to take advantage of the caching server.

If you want to cleanup unused packages, there is also the `apt-get autoclean`
and `apt-get autoremove` resources provided for automated cleanup.

License and Author
==================

Author:: Joshua Timberman (<joshua@opscode.com>)
Author:: Matt Ray (<matt@opscode.com>)
Author:: Seth Chisamore (<schisamo@opscode.com>)

Copyright 2009-2012 Opscode, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
This cookbook is used with test-kitchen to test the parent, apt cookbok
# <a name="title"></a> golang (Chef cookbook for Go)

## <a name="description"></a> Description

Chef cookbook for [Go programming language](http://golang.org/).

## <a name="requirements"></a> Requirements

### <a name="requirements-platform"></a> Platform

* Ubuntu (10.04/11.04/12.04/13.04)
* Debian (6.0)

**Notes**: This cookbook has been tested on the listed platforms. It
may work on other platforms with or without modification. Please
[report issues](/issues) any additional platforms so they can be added.

### <a name="requirements-cookbooks"></a> Cookbooks

This cookbook depends on the following external cookbooks:

* git

## <a name="usage"></a> Usage

#### golang::default

Just include `golang` in your node's `run_list`:

```json
{
  "name":"my_node",
  "run_list": [
    "recipe[golang]"
  ]
}
```

## <a name="attributes"></a> Attributes

#### golang::default
<table>
  <tr>
    <th>Key</th>
    <th>Type</th>
    <th>Description</th>
    <th>Default</th>
  </tr>
  <tr>
    <td><tt>['go']['version']</tt></td>
    <td>String</td>
    <td>Go version</td>
    <td><tt>1.0.3</tt></td>
  </tr>
  <tr>
    <td><tt>['go']['platform']</tt></td>
    <td>String</td>
    <td>`amd64` or `i386`</td>
    <td><tt>amd64</tt></td>
  </tr>
</table>

## <a name="testing"></a> Testing

This project have [foodcritic](https://github.com/acrmp/foodcritic) for syntax checking and
[test-kitchen](https://github.com/opscode/test-kitchen) for integration testing. You can run the test suite by
typing: `rake kitchen:all` (may be slow for the first time).

In order to run these tests, the following
[requirements](https://github.com/opscode/kitchen-vagrant#-requirements) must be
satisfied:

* [Vagrant](http://vagrantup.com/) (>= 1.1.0)
* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant Berkshelf Plugin](http://rubygems.org/gems/vagrant-berkshelf)

## <a name="contributing"></a> Contributing

1. Fork the repository
2. Create a named feature branch (like `add_component_x`)
3. Write you change
4. Test it by running `rake kitchen:all`
5. Submit a Pull Request

## <a name="contributors"></a> Contributors

* **[@akalyaev](https://github.com/akalyaev)**
* **[@xaprb](https://github.com/xaprb)**
* **[@crowdmatt](https://github.com/crowdmatt)**
* **[@buth](https://github.com/buth)**
* **[@computerlyrik](https://github.com/computerlyrik)**

Description
===========

Provides a set of Windows-specific primitives (Chef resources) meant to aid in the creation of cookbooks/recipes targeting the Windows platform.

Requirements
============

Version 1.3.0+ of this cookbook requires Chef 0.10.10+.

Platform
--------

* Windows XP
* Windows Vista
* Windows Server 2003 R2
* Windows 7
* Windows Server 2008 (R1, R2)

The `windows_task` LWRP requires Windows Server 2008 due to its API usage.

Cookbooks
---------

The following cookbooks provided by Opscode are required as noted:

* chef_handler (`windows::reboot_handler` leverages the chef_handler LWRP)
* powershell - The Printer and Printer Port LWRP require Powershell.

**NOTE** We cannot specifically depend on Opscode's powershell,
  because powershell depends on this cookbook. Ensure that
  `recipe[powershell]` exists in the node's expanded run list so it
  gets downloaded where the printer LWRPs are used.

Attributes
==========

* `node['windows']['allow_pending_reboots']` - used to configure the `WindowsRebootHandler` (via the `windows::reboot_handler` recipe) to act on pending reboots. default is true (ie act on pending reboots).  The value of this attribute only has an effect if the `windows::reboot_handler` is in a node's run list.

Resource/Provider
=================

windows\_auto\_run
------------------

### Actions

- :create: Create an item to be run at login
- :remove: Remove an item that was previously setup to run at login

### Attribute Parameters

- :name: Name attribute. The name of the value to be stored in the registry
- :program: The program to be run at login
- :args: The arguments for the program

### Examples

    # Run BGInfo at login
    windows_auto_run 'BGINFO' do
      program "C:/Sysinternals/bginfo.exe"
      args "\"C:/Sysinternals/Config.bgi\" /NOLICPROMPT /TIMER:0"
      not_if { Registry.value_exists?(AUTO_RUN_KEY, 'BGINFO') }
      action :create
    end


windows\_batch
--------------

Execute a batch script using the cmd.exe interpreter (much like the script resources for bash, csh, powershell, perl, python and ruby). A temporary file is created and executed like other script resources, rather than run inline. By their nature, Script resources are not idempotent, as they are completely up to the user's imagination. Use the `not_if` or `only_if` meta parameters to guard the resource for idempotence.

### Actions

- :run: run the batch file

### Attribute Parameters

- command: name attribute. Name of the command to execute.
- code: quoted string of code to execute.
- creates: a file this command creates - if the file exists, the command will not be run.
- cwd: current working directory to run the command from.
- flags: command line flags to pass to the interpreter when invoking.
- user: A user name or user ID that we should change to before running this command.
- group: A group name or group ID that we should change to before running this command.

### Examples

    windows_batch "unzip_and_move_ruby" do
      code <<-EOH
      7z.exe x #{Chef::Config[:file_cache_path]}/ruby-1.8.7-p352-i386-mingw32.7z  -oC:\\source -r -y
      xcopy C:\\source\\ruby-1.8.7-p352-i386-mingw32 C:\\ruby /e /y
      EOH
    end

    windows_batch "echo some env vars" do
      code <<-EOH
      echo %TEMP%
      echo %SYSTEMDRIVE%
      echo %PATH%
      echo %WINDIR%
      EOH
    end

windows\_feature
----------------

Windows Roles and Features can be thought of as built-in operating system packages that ship with the OS.  A server role is a set of software programs that, when they are installed and properly configured, lets a computer perform a specific function for multiple users or other computers within a network.  A Role can have multiple Role Services that provide functionality to the Role.  Role services are software programs that provide the functionality of a role. Features are software programs that, although they are not directly parts of roles, can support or augment the functionality of one or more roles, or improve the functionality of the server, regardless of which roles are installed.  Collectively we refer to all of these attributes as 'features'.

This resource allows you to manage these 'features' in an unattended, idempotent way.

There are two providers for the `windows_features` which map into Microsoft's two major tools for managing roles/features: [Deployment Image Servicing and Management (DISM)](http://msdn.microsoft.com/en-us/library/dd371719(v=vs.85).aspx) and [Servermanagercmd](http://technet.microsoft.com/en-us/library/ee344834(WS.10).aspx) (The CLI for Server Manager).  As Servermanagercmd is deprecated, Chef will set the default provider to `Chef::Provider::WindowsFeature::DISM` if DISM is present on the system being configured.  The default provider will fall back to `Chef::Provider::WindowsFeature::ServerManagerCmd`.

For more information on Roles, Role Services and Features see the [Microsoft TechNet article on the topic](http://technet.microsoft.com/en-us/library/cc754923.aspx).  For a complete list of all features that are available on a node type either of the following commands at a command prompt:

    dism /online /Get-Features
    servermanagercmd -query

### Actions

- :install: install a Windows role/feature
- :remove: remove a Windows role/feature

### Attribute Parameters

- feature_name: name of the feature/role to install.  The same feature may have different names depending on the provider used (ie DHCPServer vs DHCP; DNS-Server-Full-Role vs DNS).

### Providers

- **Chef::Provider::WindowsFeature::DISM**: Uses Deployment Image Servicing and Management (DISM) to manage roles/features.
- **Chef::Provider::WindowsFeature::ServerManagerCmd**: Uses Server Manager to manage roles/features.

### Examples

    # enable the node as a DHCP Server
    windows_feature "DHCPServer" do
      action :install
    end

    # enable TFTP
    windows_feature "TFTP" do
      action :install
    end

    # disable Telnet client/server
    %w{ TelnetServer TelnetClient }.each do |feature|
      windows_feature feature do
        action :remove
      end
    end

windows\_package
----------------

Manage Windows application packages in an unattended, idempotent way.

The following application installers are currently supported:

* MSI packages
* InstallShield
* Wise InstallMaster
* Inno Setup
* Nullsoft Scriptable Install System

If the proper installer type is not passed into the resource's installer_type attribute, the provider will do it's best to identify the type by introspecting the installation package.  If the installation type cannot be properly identified the `:custom` value can be passed into the installer_type attribute along with the proper flags for silent/quiet installation (using the `options` attribute..see example below).

__PLEASE NOTE__ - For proper idempotence the resource's `package_name` should be the same as the 'DisplayName' registry value in the uninstallation data that is created during package installation.  The easiest way to definitively find the proper 'DisplayName' value is to install the package on a machine and search for the uninstall information under the following registry keys:

* `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall`
* `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall`
* `HKEY_LOCAL_MACHINE\Software\Wow6464Node\Microsoft\Windows\CurrentVersion\Uninstall`

For maximum flexibility the `source` attribute supports both remote and local installation packages.

### Actions

- :install: install a package
- :remove: remove a package. The remove action is completely hit or miss as many application uninstallers do not support a full silent/quiet mode.

### Attribute Parameters

- package_name: name attribute. The 'DisplayName' of the application installation package.
- source: The source of the windows installer.  This can either be a URI or a local path.
- installer_type: They type of windows installation package. valid values are: :msi, :inno, :nsis, :wise, :installshield, :custom.  If this value is not provided, the provider will do it's best to identify the installer type through introspection of the file.
- checksum: useful if source is remote, the SHA-256 checksum of the file--if the local file matches the checksum, Chef will not download it
- options: Additional options to pass the underlying installation command
- timeout: set a timeout for the package download (default 600 seconds)
- version: The version number of this package, as indicated by the 'DisplayVersion' value in one of the 'Uninstall' registry keys.  If the given version number does equal the 'DisplayVersion' in the registry, the package will be installed.
- success_codes: set an array of possible successful installation
  return codes. Previously this was hardcoded, but certain MSIs may
  have a different return code, e.g. 3010 for reboot required. Must be
  an array, and defaults to `[0, 42, 127]`.

### Examples

    # install PuTTY (InnoSetup installer)
    windows_package "PuTTY version 0.60" do
      source "http://the.earth.li/~sgtatham/putty/latest/x86/putty-0.60-installer.exe"
      installer_type :inno
      action :install
    end

    # install 7-Zip (MSI installer)
    windows_package "7-Zip 9.20 (x64 edition)" do
      source "http://downloads.sourceforge.net/sevenzip/7z920-x64.msi"
      action :install
    end

    # install Notepad++ (Y U No Emacs?) using a local installer
    windows_package "Notepad++" do
      source "c:/installation_files/npp.5.9.2.Installer.exe"
      action :install
    end

    # install VLC for that Xvid (NSIS installer)
    windows_package "VLC media player 1.1.10" do
      source "http://superb-sea2.dl.sourceforge.net/project/vlc/1.1.10/win32/vlc-1.1.10-win32.exe"
      action :install
    end

    # install Firefox as custom installer and manually set the silent install flags
    windows_package "Mozilla Firefox 5.0 (x86 en-US)" do
      source "http://archive.mozilla.org/pub/mozilla.org/mozilla.org/firefox/releases/5.0/win32/en-US/Firefox%20Setup%205.0.exe"
      options "-ms"
      installer_type :custom
      action :install
    end

    # Google Chrome FTW (MSI installer)
    windows_package "Google Chrome" do
      source "https://dl-ssl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B806F36C0-CB54-4A84-A3F3-0CF8A86575E0%7D%26lang%3Den%26browser%3D3%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dfalse/edgedl/chrome/install/GoogleChromeStandaloneEnterprise.msi"
      action :install
    end

    # remove Google Chrome (but why??)
    windows_package "Google Chrome" do
      action :remove
    end

    # remove 7-Zip
    windows_package "7-Zip 9.20 (x64 edition)" do
      action :remove
    end


windows\_printer\_port
----------------------

**Note** Include `recipe[powershell]` on the node's expanded run list
  to ensure the powershell cookbook is downloaded to avoid circular
  dependency.

Create and delete TCP/IPv4 printer ports.

### Actions

- :create: Create a TCIP/IPv4 printer port. This is the default action.
- :delete: Delete a TCIP/IPv4 printer port

### Attribute Parameters

- :ipv4_address: Name attribute. Required. IPv4 address, e.g. "10.0.24.34"
- :port_name: Port name. Optional. Defaults to "IP_" + :ipv4_address
- :port_number: Port number. Optional. Defaults to 9100.
- :port_description: Port description. Optional.
- :snmp_enabled: Boolean. Optional. Defaults to false.
- :port_protocol: Port protocol, 1 (RAW), or 2 (LPR). Optional. Defaults to 1.

### Examples

    # simplest example. Creates a TCP/IP printer port named "IP_10.4.64.37"
    # with all defaults
    windows_printer_port '10.4.64.37' do
    end

    # delete a printer port
    windows_printer_port '10.4.64.37' do
      action :delete
    end

    # delete a port with a custom port_name
    windows_printer_port '10.4.64.38' do
      port_name "My awesome port"
      action :delete
    end

    # Create a port with more options
    windows_printer_port '10.4.64.39' do
      port_name "My awesome port"
      snmp_enabled true
      port_protocol 2
    end


windows\_printer
----------------

**Note** Include `recipe[powershell]` on the node's expanded run list
  to ensure the powershell cookbook is downloaded to avoid circular
  dependency.

Create Windows printer. Note that this doesn't currently install a printer
driver. You must already have the driver installed on the system.

The Windows Printer LWRP will automatically create a TCP/IP printer port for you using the `ipv4_address` property. If you want more granular control over the printer port, just create it using the `windows_printer_port` LWRP before creating the printer.

### Actions

- :create: Create a new printer
- :delete: Delete a new printer

### Attribute Parameters

- :device_id: Name attribute. Required. Printer queue name, e.g. "HP LJ 5200 in fifth floor copy room"
- :comment: Optional string describing the printer queue.
- :default: Boolean. Optional. Defaults to false. Note that Windows sets the first printer defined to the default printer regardless of this setting.
- :driver_name: String. Required. Exact name of printer driver. Note that the printer driver must already be installed on the node.
- :location: Printer location, e.g. "Fifth floor copy room", or "US/NYC/Floor42/Room4207"
- :shared: Boolean. Defaults to false.
- :share_name: Printer share name.
- :ipv4_address: Printer IPv4 address, e.g. "10.4.64.23". You don't have to be able to ping the IP addresss to set it. Required.


### Examples

    # create a printer
    windows_printer 'HP LaserJet 5th Floor' do
      driver_name 'HP LaserJet 4100 Series PCL6'
      ipv4_address '10.4.64.38'
    end

    # delete a printer
    # Note: this doesn't delete the associated printer port.
    #   See `windows_printer_port` above for how to delete the port.
    windows_printer 'HP LaserJet 5th Floor' do
      action :delete
    end


windows\_reboot
---------------

Sets required data in the node's run_state to notify `WindowsRebootHandler` a reboot is requested.  If Chef run completes successfully a reboot will occur if the `WindowsRebootHandler` is properly registered as a report handler.  As an action of `:request` will cause a node to reboot every Chef run, this resource is usually notified by other resources...ie restart node after a package is installed (see example below).

### Actions

- :request: requests a reboot at completion of successful Cher run.  requires `WindowsRebootHandler` to be registered as a report handler.
- :cancel: remove reboot request from node.run_state.  this will cancel *ALL* previously requested reboots as this is a binary state.

### Attribute Parameters

- :timeout: Name attribute. timeout delay in seconds to wait before proceeding with the requested reboot. default is 60 seconds
- :reason: comment on the reason for the reboot. default is 'Opscode Chef initiated reboot'

### Examples

    # if the package installs, schedule a reboot at end of chef run
    windows_reboot 60 do
      reason 'cause chef said so'
      action :nothing
    end
    windows_package 'some_package' do
      action :install
      notifies :request, 'windows_reboot[60]'
    end

    # cancel the previously requested reboot
    windows_reboot 60 do
      action :cancel
    end

windows\_registry
-----------------

Creates and modifies Windows registry keys.

*Change in v1.3.0: The Win32 classes use `::Win32` to avoid namespace conflict with `Chef::Win32` (introduced in Chef 0.10.10).*

### Actions

- :create: create a new registry key with the provided values.
- :modify: modify an existing registry key with the provided values.
- :force_modify: modify an existing registry key with the provided values.  ensures the value is actually set by checking multiple times. useful for fighting race conditions where two processes are trying to set the same registry key.  This will be updated in the near future to use 'RegNotifyChangeKeyValue' which is exposed by the WinAPI and allows a process to register for notification on a registry key change.
- :remove: removes a value from an existing registry key

### Attribute Parameters

- key_name: name attribute. The registry key to create/modify.
- values: hash of the values to set under the registry key. The individual hash items will become respective 'Value name' => 'Value data' items in the registry key.
- type: Type of key to create, defaults to REG_SZ. Must be a symbol, see the overview below for valid values.

### Registry key types

- :binary: REG_BINARY
- :string: REG_SZ
- :multi_string: REG_MULTI_SZ
- :expand_string: REG_EXPAND_SZ
- :dword: REG_DWORD
- :dword_big_endian: REG_DWORD_BIG_ENDIAN
- :qword: REG_QWORD

### Examples

    # make the local windows proxy match the one set for Chef
    proxy = URI.parse(Chef::Config[:http_proxy])
    windows_registry 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings' do
      values 'ProxyEnable' => 1, 'ProxyServer' => "#{proxy.host}:#{proxy.port}", 'ProxyOverride' => '<local>'
    end

    # enable Remote Desktop and poke the firewall hole
    windows_registry 'HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server' do
      values 'FdenyTSConnections' => 0
    end

    # Delete an item from the registry
    windows_registry 'HKCU\Software\Test' do
      #Key is the name of the value that you want to delete the value is always empty
      values 'ValueToDelete' => ''
      action :remove
    end

    # Add a REG_MULTI_SZ value to the registry
    windows_registry 'HKCU\Software\Test' do
      values 'MultiString' => ['line 1', 'line 2', 'line 3']
      type :multi_string
    end

### Library Methods

    Registry.value_exists?('HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run','BGINFO')
    Registry.key_exists?('HKLM\SOFTWARE\Microsoft')
    BgInfo = Registry.get_value('HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run','BGINFO')

windows\_path
-------------

### Actions

- :add: Add an item to the system path
- :remove: Remove an item from the system path

### Attribute Parameters

- :path: Name attribute. The name of the value to add to the system path

### Examples

    #Add Sysinternals to the system path
    windows_path 'C:\Sysinternals' do
      action :add
    end

    #Remove 7-Zip from the system path
    windows_path 'C:\7-Zip' do
      action :remove
    end

windows\_task
-------------

Creates, deletes or runs a Windows scheduled task. Requires Windows
Server 2008 due to API usage.

### Actions

- :create: creates a task
- :delete: deletes a task
- :run: runs a task
- :change: changes the un/pw or command of a task

### Attribute Parameters

- name: name attribute, The task name.
- command: The command the task will run.
- cwd: The directory the task will be run from.
- user: The user to run the task as. (requires password)
- password: The user's password. (requires user)
- run_level: Run with limited or highest privileges.
- frequency: Frequency with which to run the task. (hourly, daily, ect.)
- frequency_modifier: Multiple for frequency. (15 minutes, 2 days)

### Examples

    # Run Chef every 15 minutes
    windows_task "Chef client" do
      user "Administrator"
      password "$ecR3t"
      cwd "C:\chef\bin"
      command "chef-client -L C:\tmp\"
      run_level :highest
      frequency :minute
      frequency_modifier 15
    end

    # Update Chef Client task with new password and log location
    windows_task "Chef client" do
      user "Administrator"
      password "N3wPassW0Rd"
      cwd "C:\chef\bin"
      command "chef-client -L C:\chef\logs\"
      action :change
    end

    # Delete a taks named "old task"
    windows_task "old task" do
      action :delete
    end

windows\_zipfile
----------------

Most version of Windows do not ship with native cli utility for managing compressed files.  This resource provides a pure-ruby implementation for managing zip files. Be sure to use the `not_if` or `only_if` meta parameters to guard the resource for idempotence or action will be taken on the zip file every Chef run.

### Actions

- :unzip: unzip a compressed file

### Attribute Parameters

- path: name attribute. The path where files will be unzipped to.
- source: The source of the zip file. This can either be a URI or a local path.
- overwrite: force an overwrite of the files if the already exists.
- checksum: useful if source is remote, the SHA-256 checksum of the file--if the local file matches the checksum, Chef will not download it

### Examples

    # unzip a remote zip file locally
    windows_zipfile "c:/bin" do
      source "http://download.sysinternals.com/Files/SysinternalsSuite.zip"
      action :unzip
      not_if {::File.exists?("c:/bin/PsExec.exe")}
    end

    # unzip a local zipfile
    windows_zipfile "c:/the_codez" do
      source "c:/foo/baz/the_codez.zip"
      action :unzip
    end


Exception/Report Handlers
=========================

WindowsRebootHandler
--------------------

Required reboots are a necessary evil of configuring and managing Windows nodes.  This report handler (ie fires at the end of successful Chef runs) acts on requested (Chef initiated) or pending (as determined by the OS per configuration action we performed) reboots.  The `allow_pending_reboots` initialization argument should be set to false if you do not want the handler to automatically reboot a node if it has been determined a reboot is pending.  Reboots can still be requested explicitly via the `windows_reboot` LWRP.

## Initialization Arguments

- `allow_pending_reboots`: indicator on whether the handler should act on a the Window's 'pending reboot' state. default is true
- `timeout`: timeout delay in seconds to wait before proceeding with the reboot. default is 60 seconds
- `reason`:  comment on the reason for the reboot. default is 'Opscode Chef initiated reboot'

Usage
=====

Place an explicit dependency on this cookbook (using depends in the cookbook's metadata.rb) from any cookbook where you would like to use the Windows-specific resources/providers that ship with this cookbook.

    depends "windows"

default
-------

Convenience recipe that installs supporting gems for many of the resources/providers that ship with this cookbook.

*Change in v1.3.0: Uses chef_gem instead of gem_package to ensure gem installation in Chef 0.10.10.*

reboot\_handler
--------------

Leverages the `chef_handler` LWRP to register the `WindowsRebootHandler` report handler that ships as part of this cookbook. By default this handler is set to automatically act on pending reboots.  If you would like to change this behavior override `node['windows']['allow_pending_reboots']` and set the value to false.  For example:

    % cat roles/base.rb
    name "base"
    description "base role"
    override_attributes(
      "windows" => {
        "allow_pending_reboots" => false
      }
    )

This will still allow a reboot to be explicitly requested via the `windows_reboot` LWRP.

License and Author
==================

Author:: Seth Chisamore (<schisamo@opscode.com>)
Author:: Doug MacEachern (<dougm@vmware.com>)
Author:: Paul Morton (<pmorton@biaprotect.com>)
Author:: Doug Ireton (<doug.ireton@nordstrom.com>)

Copyright:: 2011, Opscode, Inc.
Copyright:: 2010, VMware, Inc.
Copyright:: 2011, Business Intelligence Associates, Inc
Copyright:: 2012, Nordstrom, Inc.


Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
Description
===========

Installs and configures PostgreSQL as a client or a server.

Requirements
============

## Platforms

* Debian, Ubuntu
* Red Hat/CentOS/Scientific (6.0+ required) - "EL6-family"
* Fedora
* SUSE

Tested on:

* Ubuntu 10.04, 11.10, 12.04
* Red Hat 6.1, Scientific 6.1, CentOS 6.3

## Cookbooks

Requires Opscode's `openssl` cookbook for secure password generation.

Requires a C compiler and development headers in order to build the
`pg` RubyGem to provide Ruby bindings in the `ruby` recipe.

Opscode's `build-essential` cookbook provides this functionality on
Debian, Ubuntu, and EL6-family.

While not required, Opscode's `database` cookbook contains resources
and providers that can interact with a PostgreSQL database. This
cookbook is a dependency of database.

Attributes
==========

The following attributes are set based on the platform, see the
`attributes/default.rb` file for default values.

* `node['postgresql']['version']` - version of postgresql to manage
* `node['postgresql']['dir']` - home directory of where postgresql
  data and configuration lives.

* `node['postgresql']['client']['packages']` - An array of package names
  that should be installed on "client" systems.
* `node['postgresql']['server']['packages']` - An array of package names
  that should be installed on "server" systems.
* `node['postgresql']['contrib']['packages']` - An array of package names
  that could be installed on "server" systems for useful sysadmin tools.

* `node['postgresql']['enable_pgdg_apt']` - Whether to enable the apt repo
  by the PostgreSQL Global Development Group, which contains newer versions
  of PostgreSQL.

* `node['postgresql']['enable_pgdg_yum']` - Whether to enable the yum repo
  by the PostgreSQL Global Development Group, which contains newer versions
  of PostgreSQL.

The following attributes are generated in
`recipe[postgresql::server]`.

* `node['postgresql']['password']['postgres']` - randomly generated
  password by the `openssl` cookbook's library.
  (TODO: This is broken, as it disables the password.)

Configuration
-------------

The `postgresql.conf` and `pg_hba.conf` files are dynamically
generated from attributes. Each key in `node['postgresql']['config']`
is a postgresql configuration directive, and will be rendered in the
config file. For example, the attribute:

    node['postgresql']['config']['listen_address'] = 'localhost'

Will result in the following line in the `postgresql.conf` file:

    listen_address = 'localhost'

The attributes file contains default values for Debian and RHEL
platform families (per the `node['platform_family']`). These defaults
have disparity between the platforms because they were originally
extracted from the postgresql.conf files in the previous version of
this cookbook, which differed in their default config. The resulting
configuration files will be the same as before, but the content will
be dynamically rendered from the attributes. The helpful commentary
will no longer be present. You should consult the PostgreSQL
documentation for specific configuration details.

See __Recipes__ `config_initdb` and `config_pgtune` below to
auto-generate many postgresql.conf settings.

For values that are "on" or "off", they should be specified as literal
`true` or `false`. String values will be used with single quotes. Any
configuration option set to the literal `nil` will be skipped
entirely. All other values (e.g., numeric literals) will be used as
is. So for example:

    node.default['postgresql']['config']['logging_collector'] = true
    node.default['postgresql']['config']['datestyle'] = 'iso, mdy'
    node.default['postgresql']['config']['ident_file'] = nil
    node.default['postgresql']['config']['port] = 5432

Will result in the following config lines:

    logging_collector = 'on'
    datestyle = 'iso,mdy'
    port = 5432

(no line printed for `ident_file` as it is `nil`)

The `pg_hba.conf` file is dynamically generated from the
`node['postgresql']['pg_hba']` attribute. This attribute must be an
array of hashes, each hash containing the authorization data. As it is
an array, you can append to it in your own recipes. The hash keys in
the array must be symbols. Each hash will be written as a line in
`pg_hba.conf`. For example, this entry from
`node['postgresql']['pg_hba']`:

    {:comment => '# Optional comment',
    :type => 'local', :db => 'all', :user => 'postgres', :addr => nil, :method => 'md5'}

Will result in the following line in `pg_hba.conf`:

    # Optional comment
    local   all             postgres                                md5

Use `nil` if the CIDR-ADDRESS should be empty (as above).
Don't provide a comment if none is desired in the `pg_hba.conf` file.

Note that the following authorization rule is supplied automatically by
the cookbook template. The cookbook needs this to execute SQL in the
PostgreSQL server without supplying the clear-text password (which isn't
known by the cookbook). Therefore, your `node['postgresql']['pg_hba']`
attributes don't need to specify this authorization rule:

    # "local" is for Unix domain socket connections only
    local   all             all                                     ident

(By the way, the template uses `peer` instead of `ident` for PostgreSQL-9.1
and above, which has the same effect.)

Recipes
=======

default
-------

Includes the client recipe.

client
------

Installs the packages defined in the
`node['postgresql']['client']['packages']` attribute.

ruby
----

**NOTE** This recipe may not currently work when installing Chef with
  the
  ["Omnibus" full stack installer](http://opscode.com/chef/install) on
  some platforms due to an incompatibility with OpenSSL. See
  [COOK-1406](http://tickets.opscode.com/browse/COOK-1406). You can
  build from source into the Chef omnibus installation to work around
  this issue.

Install the `pg` gem under Chef's Ruby environment so it can be used
in other recipes. The build-essential packages and postgresql client
packages will be installed during the compile phase, so that the
native extensions of `pg` can be compiled.

server
------

Includes the `server_debian` or `server_redhat` recipe to get the
appropriate server packages installed and service managed. Also
manages the configuration for the server:

* generates a strong default password (via `openssl`) for `postgres`
  (TODO: This is broken, as it disables the password.)
* sets the password for postgres
* manages the `postgresql.conf` file.
* manages the `pg_hba.conf` file.

server\_debian
--------------

Installs the postgresql server packages and sets up the service. You
should include the `postgresql::server` recipe, which will include
this on Debian platforms.

server\_redhat
--------------

Manages the postgres user and group (with UID/GID 26, per RHEL package
conventions), installs the postgresql server packages, initializes the
database, and manages the postgresql service. You should include the
`postgresql::server` recipe, which will include this on RHEL/Fedora
platforms.

config\_initdb
--------------

Takes locale and timezone settings from the system configuration.
This recipe creates `node.default['postgresql']['config']` attributes
that conform to the system's locale and timezone. In addition, this
recipe creates the same error reporting and logging settings that
`initdb` provided: a rotation of 7 days of log files named
postgresql-Mon.log, etc.

The default attributes created by this recipe are easy to override with
normal attributes because of Chef attribute precedence. For example,
suppose a DBA wanted to keep log files indefinitely, rolling over daily
or when growing to 10MB. The Chef installation could include the
`postgresql::config_initdb` recipe for the locale and timezone settings,
but customize the logging settings with these node JSON attributes:

    "postgresql": {
      "config": {
        "log_rotation_age": "1d",
        "log_rotation_size": "10MB",
        "log_filename": "postgresql-%Y-%m-%d_%H%M%S.log"
      }
    }

Credits: This `postgresql::config_initdb` recipe is based on algorithms
in the [source code](http://doxygen.postgresql.org/initdb_8c_source.html)
for the PostgreSQL `initdb` utility.

config\_pgtune
--------------

Performance tuning.
Takes the wimpy default postgresql.conf and expands the database server
to be as powerful as the hardware it's being deployed on. This recipe
creates a baseline configuration of `node.default['postgresql']['config']`
attributes in the right general range for a dedicated Postgresql system.
Most installations won't need additional performance tuning.

The only decision you need to make is to choose a `db_type` from the
following database workloads. (See the recipe code comments for more
detailed descriptions.)

 * "dw" -- Data Warehouse
 * "oltp" -- Online Transaction Processing
 * "web" -- Web Application
 * "mixed" -- Mixed DW and OLTP characteristics
 * "desktop" -- Not a dedicated database

This recipe uses a performance model with three input parameters.
These node attributes are completely optional, but it is obviously
important to choose the `db_type` correctly:

 * `node['postgresql']['config_pgtune']['db_type']` --
   Specifies database type from the list of five choices above.
   If not specified, the default is "mixed".

 * `node['postgresql']['config_pgtune']['max_connections']` --
   Specifies maximum number of connections expected.
   If not specified, it depends on database type:
   "web":200, "oltp":300, "dw":20, "mixed":80, "desktop":5

 * `node['postgresql']['config_pgtune']['total_memory']` --
   Specifies total system memory in kB. (E.g., "49416564kB".)
   If not specified, it will be taken from Ohai automatic attributes.
   This could be used to tune a system that isn't a dedicated database.

The default attributes created by this recipe are easy to override with
normal attributes because of Chef attribute precedence. For example, if
you are running application benchmarks to try different buffer cache
sizes, you would experiment with this node JSON attribute:

    "postgresql": {
      "config": {
        "shared_buffers": "3GB"
      }
    }

Note that the recipe uses `max_connections` in its computations. If
you want to override that setting, you should specify
`node['postgresql']['config_pgtune']['max_connections']` instead of
`node['postgresql']['config']['max_connections']`.

Credits: This `postgresql::config_pgtune` recipe is based on the
[pgtune python script](https://github.com/gregs1104/pgtune)
developed by
[Greg Smith](http://notemagnet.blogspot.com/2008/11/automating-initial-postgresqlconf.html)
and
[other pgsql-hackers](http://www.postgresql.org/message-id/491C6CDC.8090506@agliodbs.com).

contrib
-------

Installs the packages defined in the
`node['postgresql']['contrib']['packages']` attribute. The contrib
directory of the PostgreSQL distribution includes porting tools,
analysis utilities, and plug-in features that database engineers often
require. Some (like `pgbench`) are executable. Others (like
`pg_buffercache`) would need to be installed into the database.

Also installs any contrib module extensions defined in the 
`node['postgresql']['contrib']['extensions']` attribute. These will be
available in any subsequently created databases in the cluster, because
they will be installed into the `template1` database using the
`CREATE EXTENSION` command. For example, it is often necessary/helpful
for problem troubleshooting and maintenance planning to install the
views and functions in these [standard instrumentation extensions]
(http://www.postgresql.org/message-id/flat/4DC32600.6080900@pgexperts.com#4DD3D6C6.5060006@2ndquadrant.com):

    node['postgresql']['contrib']['extensions'] = [
      "pageinspect",
      "pg_buffercache",
      "pg_freespacemap",
      "pgrowlocks",
      "pg_stat_statements",
      "pgstattuple"
    ]

Note that the `pg_stat_statements` view only works if `postgresql.conf`
loads its shared library, which can be done with this node attribute:

    node['postgresql']['config']['shared_preload_libraries'] = 'pg_stat_statements'

apt\_pgdg\_postgresql
----------------------

Enables the PostgreSQL Global Development Group yum repository
maintained by Devrim G&#252;nd&#252;z for updated PostgreSQL packages.
(The PGDG is the groups that develops PostgreSQL.)
Automatically included if the `node['postgresql']['enable_pgdg_apt']`
attribute is true. Also set the
`node['postgresql']['client']['packages']` and
`node['postgresql']['server]['packages']` to the list of packages to
use from this repository, and set the `node['postgresql']['version']`
attribute to the version to use (e.g., "9.2").

yum\_pgdg\_postgresql
---------------------

Enables the PostgreSQL Global Development Group yum repository
maintained by Devrim G&#252;nd&#252;z for updated PostgreSQL packages.
(The PGDG is the groups that develops PostgreSQL.)
Automatically included if the `node['postgresql']['enable_pgdg_yum']`
attribute is true. Also use `override_attributes` to set a number of
values that will need to have embedded version numbers. For example:

    node['postgresql']['enable_pgdg_yum'] = true
    node['postgresql']['version'] = "9.2"
    node['postgresql']['dir'] = "/var/lib/pgsql/9.2/data"
    node['postgresql']['client']['packages'] = ["postgresql92", "postgresql92-devel"]
    node['postgresql']['server']['packages'] = ["postgresql92-server"]
    node['postgresql']['server']['service_name'] = "postgresql-9.2"
    node['postgresql']['contrib']['packages'] = ["postgresql92-contrib"]

You may set `node['postgresql']['pgdg']['repo_rpm_url']` attributes
to pick up recent [PGDG repo packages](http://yum.postgresql.org/repopackages.php).

Resources/Providers
===================

See the [database](http://community.opscode.com/cookbooks/database)
for resources and providers that can be used for managing PostgreSQL
users and databases.

Usage
=====

On systems that need to connect to a PostgreSQL database, add to a run
list `recipe[postgresql]` or `recipe[postgresql::client]`.

On systems that should be PostgreSQL servers, use
`recipe[postgresql::server]` on a run list. This recipe does set a
password for the `postgres` user.
If you're using `chef server`, if the attribute
`node['postgresql']['password']['postgres']` is not found,
the recipe generates a random password and performs a node.save.
(TODO: This is broken, as it disables the password.)
If you're using `chef-solo`, you'll need
to set the attribute `node['postgresql']['password']['postgres']` in
your node's `json_attribs` file or in a role.

On Debian family systems, SSL will be enabled, as the packages on
Debian/Ubuntu also generate the SSL certificates. If you use another
platform and wish to use SSL in postgresql, then generate your SSL
certificates and distribute them in your own cookbook, and set the
`node['postgresql']['config']['ssl']` attribute to true in your
role/cookboook/node.

Chef Solo Note
==============

The following node attribute is stored on the Chef Server when using
`chef-client`. Because `chef-solo` does not connect to a server or
save the node object at all, to have the password persist across
`chef-solo` runs, you must specify them in the `json_attribs` file
used. For Example:

    {
      "postgresql": {
        "password": {
          "postgres": "iloverandompasswordsbutthiswilldo"
        }
      },
      "run_list": ["recipe[postgresql::server]"]
    }

That should actually be the "encrypted password" instead of cleartext,
so you should generate it as an md5 hash using the PostgreSQL algorithm.

* You could copy the md5-hashed password from an existing postgres
database if you have `postgres` access and want to use the same password:<br>
`select * from pg_shadow where usename='postgres';`
* You can run this from any postgres database session to use a new password:<br>
`select 'md5'||md5('iloverandompasswordsbutthiswilldo'||'postgres');`
* You can run this from a linux commandline:<br>
`echo -n 'iloverandompasswordsbutthiswilldo''postgres' | openssl md5 | sed -e 's/.* /md5/'`

License and Author
==================

- Author:: Joshua Timberman (<joshua@opscode.com>)
- Author:: Lamont Granquist (<lamont@opscode.com>)
- Author:: Chris Roberts (<chrisroberts.code@gmail.com>)
- Author:: David Crane (<davidc@donorschoose.org>)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
nginx Cookbook
==============
[![Build Status](https://secure.travis-ci.org/opscode-cookbooks/nginx.png?branch=master)](http://travis-ci.org/opscode-cookbooks/nginx)

Installs nginx from package OR source code and sets up configuration handling similar to Debian's Apache2 scripts.


Requirements
------------
### Cookbooks
The following cookbooks are direct dependencies because they're used for common "default" functionality.

- build-essential (for nginx::source)
- ohai (for nginx::ohai_plugin)

The following cookbook is not a strict dependency because its use can be controlled by an attribute, so it may not be a common "default."

- runit (for nginx::source)
- On RHEL family distros, the "yum" cookbook is required for `recipe[yum::epel]`.
- On Ubuntu, when using Nginx.org's stable package, `recipe[apt::default]` is required.


### Platforms
The following platforms are supported and tested under test kitchen:

- Ubuntu 10.04, Ubuntu 12.04
- CentOS 5.8, 6.3

Other Debian and RHEL family distributions are assumed to work.


Attributes
----------
Node attributes for this cookbook are logically separated into different files. Some attributes are set only via a specific recipe.

### default
Generally used attributes. Some have platform specific values. See `attributes/default.rb`. "The Config" refers to "nginx.conf" the main config file.

- `node['nginx']['dir']` - Location for Nginx configuration.
- `node['nginx']['log_dir']` - Location for Nginx logs.
- `node['nginx']['user']` - User that Nginx will run as.
- `node['nginx']['group]` - Group for Nginx.
- `node['nginx']['binary']` - Path to the Nginx binary.
- `node['nginx']['init_style']` - How to run Nginx as a service when
  using `nginx::source`. Values can be "runit", "upstart", "init" or
  "bluepill".  When using runit or bluepill, those recipes will be
  included as well and are dependencies of this cookbook.  Recipes
  are not included for upstart, it is assumed that upstart is built
  into the platform you are using (ubuntu or el6).  This attribute is
  not used in the `nginx` recipe because the package manager's init
  script style for the platform is assumed.  Upstart is never set as
  a default as this represents a change in behavior, if you are running
  ubuntu or el6 and want to use upstart, please set this attribute in
  a role or similar.
- `node['nginx']['upstart']['foreground']` - Set this to true if you
  want upstart to run nginx in the foreground, set to false if you
  want upstart to detach and track the process via pid.
- `node['nginx']['upstart']['runlevels']` - String of runlevels in the
  format '2345' which determines which runlevels nginx will start at
  when entering and stop at when leaving.
- `node['nginx']['upstart']['respawn_limit']` - Respawn limit in upstart
  stanza format, count followed by space followed by interval in seconds.
- `node['nginx']['pid']` - Location of the PID file.
- `node['nginx']['keepalive']` - Whether to use `keepalive_timeout`,
  any value besides "on" will leave that option out of the config.
- `node['nginx']['keepalive_timeout']` - used for config value of
  `keepalive_timeout`.
- `node['nginx']['worker_processes']` - used for config value of
  `worker_processes`.
- `node['nginx']['worker_connections']` - used for config value of
  `events { worker_connections }`
- `node['nginx']['worker_rlimit_nofile']` - used for config value of
  `worker_rlimit_nofile`. Can replace any "ulimit -n" command. The
  value depend on your usage (cache or not) but must always be
  superior than worker_connections.
- `node['nginx']['multi_accept']` - used for config value of `events {
  multi_accept }`. Try to accept() as many connections as possible.
  Disable by default.
- `node['nginx']['event']` - used for config value of `events { use
  }`. Set the event-model. By default nginx looks for the most
  suitable method for your OS.
- `node['nginx']['server_tokens']` - used for config value of
  `server_tokens`.
- `node['nginx']['server_names_hash_bucket_size']` - used for config
  value of `server_names_hash_bucket_size`.
- `node['nginx']['disable_access_log']` - set to true to disable the
  general access log, may be useful on high traffic sites.
- `node['nginx']['access_log_options']` - Set to a string of additional options
  to be appended to the access log directive
- `node['nginx']['error_log_options']` - Set to a string of additional options
  to be appended to the error log directive
- `node['nginx']['default_site_enabled']` - enable the default site
- `node['nginx']['sendfile']` - Whether to use `sendfile`. Defaults to "on".
- `node['nginx']['install_method']` - Whether nginx is installed from
  packages or from source.
- `node['nginx']['types_hash_max_size']` - Used for the
  `types_hash_max_size` configuration directive.
- `node['nginx']['types_hash_bucket_size']` - Used for the
  `types_hash_bucket_size` configuration directive.
- `node['nginx']['proxy_read_timeout']` - defines a timeout (between two
  successive read operations) for reading a response from the proxied server.
- `node['nginx']['client_body_buffer_size']` - used for config value of
  `client_body_buffer_size`.
- `node['nginx']['client_max_body_size']` - specifies the maximum accepted body
  size of a client request, as indicated by the request header Content-Length.
- `node['nginx']['repo_source']` - when installed from a package this attribute affects
  which yum repositories, if any, will be added before installing the nginx package. The
  default value of 'epel' will use the `yum::epel` recipe, 'nginx' will use the
  `nginx::repo` recipe, and setting no value will not add any additional repositories.

Rate Limiting

- `node['nginx']['enable_rate_limiting']` - set to true to enable rate
  limiting (`limit_req_zone` in nginx.conf)
- `node['nginx']['rate_limiting_zone_name']` - sets the zone in
  `limit_req_zone`.
- `node['nginx']['rate_limiting_backoff']` - sets the backoff time for
  `limit_req_zone`.
- `node['nginx']['rate_limit']` - set the rate limit amount for
  `limit_req_zone`.

### gzip module

- `node['nginx']['gzip']` - Whether to use gzip, can be "on" or "off"
- `node['nginx']['gzip_http_version']` - used for config value of `gzip_http_version`.
- `node['nginx']['gzip_comp_level']` - used for config value of `gzip_comp_level`.
- `node['nginx']['gzip_proxied']` - used for config value of `gzip_proxied`.
- `node['nginx']['gzip_vary']` - used for config value of `gzip_vary`.
- `node['nginx']['gzip_buffers']` - used for config value of `gzip_buffers`.
- `node['nginx']['gzip_types']` - used for config value of `gzip_types` - must be an Array.
- `node['nginx']['gzip_min_length']` - used for config value of `gzip_min_length`.
- `node['nginx']['gzip_disable']` - used for config value of `gzip_disable`.

### Attributes set in recipes

#### nginx::source
- `node['nginx']['daemon_disable']` - Whether the daemon should be
  disabled which can be true or false; disable the daemon (run in the
  foreground) when using a service supervisor such as runit or
  bluepill for "init_style". This is automatically set in the
  `nginx::source` recipe when the init style is not bluepill or runit.

#### nginx::authorized_ips
- `node['nginx']['remote_ip_var']` - The remote ip variable name to
  use.
- `node['nginx']['authorized_ips']` - IPs authorized by the module

#### nginx::http_realip_module
From: http://nginx.org/en/docs/http/ngx_http_realip_module.html

- `node['nginx']['realip']['header']` - Header to use for the RealIp
  Module; only accepts "X-Forwarded-For" or "X-Real-IP"
- `node['nginx']['realip']['addresses']` - Addresses to use for the
  `http_realip` configuration.
- `node['nginx']['realip']['real_ip_recursive']` - If recursive search is enabled, the original client address that matches one of the trusted addresses is replaced by the last non-trusted address sent in the request header field. Can be on "on" or "off" (default).

### source
These attributes are used in the `nginx::source` recipe. Some of them
are dynamically modified during the run. See `attributes/source.rb`
for default values.

- `node['nginx']['source']['url']` - (versioned) URL for the Nginx
  source code. By default this will use the version specified as
  `node['nginx']['version'].
- `node['nginx']['source']['prefix']` - (versioned) prefix for
  installing nginx from source
- `node['nginx']['source']['conf_path']` - location of the main config
  file, in `node['nginx']['dir']` by default.
- `node['nginx']['source']['modules']` - Array of modules that should
  be compiled into Nginx by including their recipes in
  `nginx::source`.
- `node['nginx']['source']['default_configure_flags']` - The default
  flags passed to the configure script when building Nginx.
- `node['nginx']['configure_flags']` - Preserved for compatibility and
  dynamically generated from the
  `node['nginx']['source']['default_configure_flags']` in the
  `nginx::source` recipe.
* `node['nginx']['source']['use_existing_user']` - set to `true` if you
  do not want `nginx::source` recipe to create system user with name
  `node['nginx']['user']`.

### geoip
These attributes are used in the `nginx::http_geoip_module` recipe.
Please note that the `country_dat_checksum` and `city_dat_checksum`
are based on downloads from a datacenter in Fremont, CA, USA. You
really should override these with checksums for the geo tarballs from
your node location.

**Note** The upstream, maxmind.com, may block access for repeated
  downloads of the data files. It is recommended that you download and
  host the data files, and change the URLs in the attributes.

- `node['nginx']['geoip']['path']` - Location where to install the
  geoip libraries.
- `node['nginx']['geoip']['enable_city']` - Whether to enable City
  data
- `node['nginx']['geoip']['country_dat_url']` - Country data tarball
  URL
- `node['nginx']['geoip']['country_dat_checksum']` - Country data
  tarball checksum
- `node['nginx']['geoip']['city_dat_url']` - City data tarball URL
- `node['nginx']['geoip']['city_dat_checksum']` - City data tarball
  checksum
- `node['nginx']['geoip']['lib_version']` - Version of the GeoIP
  library to install
- `node['nginx']['geoip']['lib_url']` - (Versioned) Tarball URL of the
  GeoIP library
- `node['nginx']['geoip']['lib_checksum']` - Checksum of the GeoIP
  library tarball

### upload_progress
These attributes are used in the `nginx::upload_progress_module`
recipe.

- `node['nginx']['upload_progress']['url']` - URL for the tarball.
- `node['nginx']['upload_progress']['checksum']` - Checksum of the
  tarball.
- `node['nginx']['upload_progress']['javascript_output']` - Output in javascript.
  Default is `true` for backwards compatibility.
- `node['nginx']['upload_progress']['zone_name']` - Zone name which will
  be used to store the per-connection tracking information.
  Default is `proxied`.
- `node['nginx']['upload_progress']['zone_size']` - Zone size in bytes.
  Default is `1m` (1 megabyte).

### passenger
These attributes are used in the `nginx::passenger` recipe.

- `node['nginx']['passenger']['version']` - passenger gem version
- `node['nginx']['passenger']['root']` - passenger gem root path
- `node['nginx']['passenger']['max_pool_size']` - maximum passenger
  pool size (default=10)
- `node['nginx']['passenger']['ruby']` - Ruby path for Passenger to
  use (default=`$(which ruby)`)
- `node['nginx']['passenger']['spawn_method']` - passenger spawn
  method to use (default=`smart-lv2`)
- `node['nginx']['passenger']['buffer_response']` - turns on or off
  response buffering (default=`on`)
- `node['nginx']['passenger']['max_pool_size']` - passenger maximum
  pool size (default=`6`)
- `node['nginx']['passenger']['min_instances']` - minimum instances
  (default=`1`)
- `node['nginx']['passenger']['max_instances_per_app']` - maximum
  instances per app (default=`0`)
- `node['nginx']['passenger']['pool_idle_time']` - passenger pool idle
  time (default=`300`)
- `node['nginx']['passenger']['max_requests']` - maximum requests
  (default=`0`)

### echo
These attributes are used in the `nginx::http_echo_module` recipe.

- `node['nginx']['echo']['version']` - The version of `http_echo` you
  want (default: 0.40)
- `node['nginx']['echo']['url']` - URL for the tarball.
- `node['nginx']['echo']['checksum']` - Checksum of the tarball.

### status
These attributes are used in the `nginx::http_stub_status_module` recipe.

- `node['nginx']['status']['port']` - The port on which nginx will
  serve the status info (default: 8090)

### openssl_source
These attributes are used in the `nginx::openssl_source` recipe.

- `node['nginx']['openssl_source']['version']` - The version of OpenSSL
  you want to download and use (default: 1.0.1e)
- `node['nginx']['openssl_source']['url']` - The url for the OpenSSL source


Recipes
-------
This cookbook provides three main recipes for installing Nginx.

- `default.rb` - *Use this recipe* if you have a native package for
  Nginx.
- `repo.rb` - The developer of Nginx also maintain
  [stable packages](http://nginx.org/en/download.html) for several
  platforms.
- `source.rb` - *Use this recipe* if you do not have a native package for
  Nginx, or if you want to install a newer version than is available,
  or if you have custom module compilation needs.

Several recipes are related to the `source` recipe specifically. See
that recipe's section below for a description.

### default
The default recipe will install Nginx as a native package for the
system through the package manager and sets up the configuration
according to the Debian site enable/disable style with `sites-enabled`
using the `nxensite` and `nxdissite` scripts. The nginx service will
be managed with the normal init scripts that are presumably included
in the native package.

Includes the `ohai_plugin` recipe so the plugin is available.

### ohai_plugin
This recipe provides an Ohai plugin as a template. It is included by
both the `default` and `source` recipes.

### authorized_ips
Sets up configuration for the `authorized_ip` nginx module.

### source
This recipe is responsible for building Nginx from source. It ensures
that the required packages to build Nginx are installed (pcre,
openssl, compile tools). The source will be downloaded from the
`node['nginx']['source']['url']`. The `node['nginx']['user']` will be
created as a system user. If you want to use existing user set
`node['nginx']['source']['use_existing_user']` to `true`. The appropriate
configuration and log directories and config files will be created
as well according to the attributes `node['nginx']['dir']` and
`node['nginx']['log_dir']`.

The recipe attempts to detect whether additional modules should be
added to the configure command through recipe inclusion (see below),
and whether the version or configuration flags have changed and should
trigger a recompile.

The nginx service will be set up according to
`node['nginx']['init_style']`. Available options are:

- runit: uses runit cookbook and sets up `runit_service`.
- bluepill: uses bluepill cookbook and sets up `bluepill_service`.
- anything else (e.g., "init") will use the nginx init script
  template.

**RHEL/CentOS** This recipe should work on RHEL/CentOS with "init" as
  the init style.

The following recipes are used to build module support into Nginx. To
use a module in the `nginx::source` recipe, add its recipe name to the
attribute `node['nginx']['source']['modules']`.

- `ipv6.rb` - enables IPv6 support
- `http_echo_module.rb` - downloads the `http_echo_module` module and
  enables it as a module when compiling nginx.
- `http_geoip_module.rb` - installs the GeoIP libraries and data files
  and enables the module for compilation.
- `http_gzip_static_module.rb` - enables the module for compilation.
- `http_perl_module.rb` - enables embedded Perl for compilation.
- `http_realip_module.rb` - enables the module for compilation and
  creates the configuration.
- `http_ssl_module.rb` - enables SSL for compilation.
- `http_stub_status_module.rb` - provides `nginx_status` configuration
  and enables the module for compilation.
- `naxsi_module` - enables the naxsi module for the web application
  firewall for nginx.
- `passenger` - builds the passenger gem and configuration for
  "`mod_passenger`".
- `upload_progress_module.rb` - builds the `upload_progress` module
  and enables it as a module when compiling nginx.
- `openssl_source.rb` - downloads and uses custom OpenSSL source
  when compiling nginx


Adding New Modules
------------------
To add a new module to be compiled into nginx in the source recipe,
the node's run state is manipulated in a recipe, and the module as a
recipe should be added to `node['nginx']['source']['modules']`. For
example:

```ruby
node.run_state['nginx_configure_flags'] =
  node.run_state['nginx_configure_flags'] | ['--with-http_stub_status_module']
```

The recipe will be included by `recipe[nginx::source]` automatically,
adding the configure flags. Add any other configuration templates or
other resources as required. See the recipes described above for
examples.


Ohai Plugin
-----------
The `ohai_plugin` recipe includes an Ohai plugin. It will be
automatically installed and activated, providing the following
attributes via ohai, no matter how nginx is installed (source or
package):

- `node['nginx']['version']` - version of nginx
- `node['nginx']['configure_arguments']` - options passed to
  `./configure` when nginx was built
- `node['nginx']['prefix']` - installation prefix
- `node['nginx']['conf_path']` - configuration file path

In the source recipe, it is used to determine whether control
attributes for building nginx have changed.


Usage
-----
Include the recipe on your node or role that fits how you wish to
install Nginx on your system per the recipes section above. Modify the
attributes as required in your role to change how various
configuration is applied per the attributes section above. In general,
override attributes in the role should be used when changing
attributes.

There's some redundancy in that the config handling hasn't been
separated from the installation method (yet), so use only one of the
recipes, default or source.


License & Authors
-----------------
- Author:: Joshua Timberman (<joshua@opscode.com>)
- Author:: Adam Jacob (<adam@opscode.com>)
- Author:: AJ Christensen (<aj@opscode.com>)
- Author:: Jamie Winsor (<jamie@vialstudios.com>)

```text
Copyright 2008-2013, Opscode, Inc

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
Description
===========

Installs git and optionally sets up a git server as a daemon under runit.

Requirements
============
## Ohai and Chef:

* Ohai: 6.14.0+

This cookbook makes use of `node['platform_family']` to simplify platform
selection logic. This attribute was introduced in Ohai v0.6.12.

## Platform:

The following platform families are supported:

* Debian
* Arch
* RHEL
* Fedora
* Mac OS X (10.6.0+)
* Windows

## Cookbooks:

* runit (for `git::server`)
* build-essential (for `git::source`)
* dmg (for OS X installation)
* yum (for RHEL 5 installation)

### Windows Dependencies
The [`windows_package`](https://github.com/opscode-cookbooks/windows#windows_package) resource from the Windows cookbook is required to
install the git package on Windows.

## Attributes

### default
The following attributes are platform-specific.

#### Windows

* `node['git']['version']` - git version to install
* `node['git']['url']` - URL to git package
* `node['git']['checksum']` - package SHA256 checksum
* `node['git']['display_name']` - `windows_package` resource Display Name (makes the package install idempotent)

#### Mac OS X

* `node['git']['osx_dmg']['url']` - URL to git package
* `node['git']['osx_dmg']['checksum']` - package SHA256 checksum

#### Linux

* `node['git']['prefix']` - git install directory
* `node['git']['version']` - git version to install
* `node['git']['url']` - URL to git tarball
* `node['git']['checksum']` - tarball SHA256 checksum

Recipes
=======

## default

Installs base git packages based on platform.

## server

Sets up a git daemon to provide a server.

## source

Installs git from source.

## windows

Installs git client on Windows

Usage
=====


This cookbook primarily installs git core packages. It can also be
used to serve git repositories.

To install git client (all supported platforms):

    include_recipe 'git'

To install git server:

    include_recipe "git::server"

This creates the directory specified by git/server/base_path (default is /srv/git)
and starts a git daemon, exporting all repositories found. Repositories need to be
added manually, but will be available once they are created.

License and Author
==================

- Author:: Joshua Timberman (<joshua@opscode.com>)
- Copyright:: 2009-2012, Opscode, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
nagios Cookbook
===============
[![Build Status](https://secure.travis-ci.org/tas50/nagios.png?branch=master)](http://travis-ci.org/tas50/nagios)

Installs and configures Nagios server and NRPE client. Chef nodes are automatically discovered using search, and Nagios host groups are created based on Chef roles and optionally environments as well. NRPE client commands can be defined by using a LWRP, and Nagios service checks applied to hostgroups using definitions in data bag items.


Requirements
------------
### Chef
Chef version 0.10.10+ and Ohai 0.6.12+ are required.

Because of the heavy use of search, this recipe will not work with Chef Solo, as it cannot do any searches without a server.

This cookbook relies heavily on multiple data bags. See __Data Bag__ below.

The system running the 'server' recipe should have a role named 'monitoring' so that NRPE clients can authorize monitoring from that system. This role name is configurable via an attribute. See __Attributes__ below.

### Platform
* Debian 6
* Ubuntu 10.04, 12.04
* Red Hat Enterprise Linux (CentOS/Amazon/Scientific/Oracle) 5.X, 6.X

**Notes**: This cookbook has been tested on the listed platforms. It may work on other platforms with or without modification.

### Cookbooks
* apache2
* build-essential
* nginx
* nginx_simplecgi
* php
* yum


Attributes
----------
### default
The following attributes are used by both client and server recipes.

* `node['nagios']['user']` - Nagios user, default 'nagios'.
* `node['nagios']['group']` - Nagios group, default 'nagios'.
* `node['nagios']['plugin_dir']` - location where Nagios plugins go, default '/usr/lib/nagios/plugins'.
* `node['nagios']['multi_environment_monitoring']` - Chef server will monitor hosts in all environments, not just its own, default 'false'

### client
The following attributes are used for the NRPE client

##### installation method
* `node['nagios']['client']['install_method']` - whether to install from package or source. Default chosen by platform based on known packages available for NRPE: debian/ubuntu 'package', Redhat/CentOS/Fedora/Scientific: source
* `node['nagios']['plugins']['url']` - url to retrieve the plugins source
* `node['nagios']['plugins']['version']` - version of the plugins source to download
* `node['nagios']['plugins']['checksum']` - checksum of the plugins source tarball
* `node['nagios']['nrpe']['home']` - home directory of NRPE, default /usr/lib/nagios
* `node['nagios']['nrpe']['log_facility']` - log facility for nrpe configuration, default nil (not set)
* `node['nagios']['nrpe']['debug']` - debug level nrpe configuration, default 0
* `node['nagios']['nrpe']['connection_timeout']` - connection timeout for nrpe configuration, default nil (not set)
* `node['nagios']['nrpe']['conf_dir']` - location of the nrpe configuration, default /etc/nagios
* `node['nagios']['nrpe']['packages']` - nrpe / plugin packages to install. The default attribute for RHEL/Fedora platforms contains a bare minimum set of packages. The full list of available packages is available at: `http://dl.fedoraproject.org/pub/epel/6/x86_64/repoview/letter_n.group.html`
* `node['nagios']['nrpe']['url']` - url to retrieve NRPE source
* `node['nagios']['nrpe']['version']` - version of NRPE source to download
* `node['nagios']['nrpe']['checksum']` - checksum of the NRPE source tarball
* `node['nagios']['plugins']['url']` - url to retrieve the plugins source from
* `node['nagios']['plugins']['version']` - version of the plugins source to download
* `node['nagios']['plugins']['checksum']` - checksum of the plugins source tarball

##### directories and paths
* `node['nagios']['nrpe']['home']` - home directory of NRPE
* `node['nagios']['nrpe']['conf_dir']` - location of the nrpe configuration
* `node['nagios']['nrpe']['ssl_lib_dir']` - ssl directory used by NRPE
* `node['nagios']['nrpe']['pidfile']` - location to store the NRPE pid file

##### authorization and server discovery
* `node['nagios']['server_role']` - the role that the Nagios server will have in its run list that the clients can search for.
* `node['nagios']['allowed_hosts']` - additional hosts that are allowed to connect to this client. Must be an array of strings (i.e. `%w(test.host other.host)`). These hosts are added in addition to 127.0.0.1 and IPs that are found via search.
* `node['nagios']['using_solo_search']` - discover server information in node data_bags even with chef solo through the use of solo-search (https://github.com/edelight/chef-solo-search)

##### misc
* `node['nagios']['nrpe']['dont_blame_nrpe']` - allows the server to send additional values to NRPE via arguments.  this needs to be enabled for most checks to function
* `node['nagios']['nrpe']['command_timeout']` - the amount of time NRPE will wait for a command to execute before timing out

### server
The following attributes are used for the Nagios server

* `node['nagios']['server']['install_method']` - whether to install from package or source. Default chosen by platform based on known packages available for Nagios: debian/ubuntu 'package', redhat/centos/fedora/scientific: source
* `node['nagios']['server']['service_name']` - name of the service used for Nagios, default chosen by platform, debian/ubuntu "nagios3", redhat family "nagios", all others, "nagios"
* `node['nagios']['home']` - Nagios main home directory, default "/usr/lib/nagios3"
* `node['nagios']['conf_dir']` - location where main Nagios config lives, default "/etc/nagios3"
* `node['nagios']['config_dir']` - location where included configuration files live, default "/etc/nagios3/conf.d"
* `node['nagios']['log_dir']` - location of Nagios logs, default "/var/log/nagios3"
* `node['nagios']['cache_dir']` - location of cached data, default "/var/cache/nagios3"
* `node['nagios']['state_dir']` - Nagios runtime state information, default "/var/lib/nagios3"
* `node['nagios']['run_dir']` - where pidfiles are stored, default "/var/run/nagios3"
* `node['nagios']['docroot']` - Nagios webui docroot, default "/usr/share/nagios3/htdocs"
* `node['nagios']['timezone']` - Nagios timezone, defaults to UTC
* `node['nagios']['enable_ssl]` - boolean for whether Nagios web server should be https, default false
* `node['nagios']['ssl_cert_file']` = Location of SSL Certificate File. default "/etc/nagios3/certificates/nagios-server.pem"
* `node['nagios']['ssl_cert_chain_file']` = Optional location of SSL Intermediate Certificate File. No default.
* `node['nagios']['ssl_cert_key']`  = Location of SSL Certificate Key. default "/etc/nagios3/certificates/nagios-server.pem"
* `node['nagios']['http_port']` - port that the Apache/Nginx virtual site should listen on, determined whether ssl is enabled (443 if so, otherwise 80). Note:  You will also need to configure the listening port for either NGINX or Apache within those cookbooks.
* `node['nagios']['server_name']` - common name to use in a server cert, default "nagios"
* `node['nagios']['ssl_req']` - info to use in a cert, default `/C=US/ST=Several/L=Locality/O=Example/OU=Operations/CN=#{node['nagios']['server_name']}/emailAddress=ops@#{node['nagios']['server_name']}`

*  `node['nagios']['server']['url']` - url to download the server source from if installing from source
*  `node['nagios']['server']['version']` - version of the server source to download
*  `node['nagios']['server']['checksum']` - checksum of the source files
*  `node['nagios']['url']` - URL to host Nagios from - defaults to nil and instead uses  FQDN

* `node['nagios']['notifications_enabled']` - set to 1 to enable notification.
* `node['nagios']['check_external_commands']`
* `node['nagios']['default_contact_groups']`
* `node['nagios']['additional_contacts']` - additional contacts to be utilized for notifying of status changes. Example: `node['nagios']['additional_contacts']['pagerduty'] = true`.
* `node['nagios']['sysadmin_email']` - default notification email.
* `node['nagios']['sysadmin_sms_email']` - default notification sms.
* `node['nagios']['server_auth_method']` - authentication with the server can be done with openid (using `apache2::mod_auth_openid`), cas (using `apache2::mod_auth_cas`),ldap (using `apache2::mod_authnz_ldap`), or htauth (basic). The default is htauth. "openid" will utilize openid authentication, "cas" will utilize cas authentication, "ldap" will utilize LDAP authentication, and any other value will use htauth (basic).
* `node['nagios']['cas_login_url']` - login url for cas if using cas authentication.
* `node['nagios']['cas_validate_url']` - validation url for cas if using cas authentication.
* `node['nagios']['cas_validate_server']` - whether to validate the server cert. Defaults to off.
* `node['nagios']['cas_root_proxy_url']` - if set, sets the url that the cas server redirects to after auth.
* `node['nagios']['ldap_bind_dn']` - DN used to bind to the server when searching for ldap entries.
* `node['nagios']['ldap_bind_password']` - bind password used with the DN provided for searcing ldap.
* `node['nagios']['ldap_url']` - ldap url and search parameters.
* `node['nagios']['ldap_authoritative']` - accepts "on" or "off". controls other authentication modules from authenticating the user if this one fails.
* `node['nagios']['users_databag']` - the databag containing users to search for. defaults to users
* `node['nagios']['users_databag_group']` - users databag group considered Nagios admins.  defaults to sysadmin
* `node['nagios']['services_databag']` - the databag containing services to search for. defaults to nagios_services
* `node['nagios']['servicegroups_databag']` - the databag containing servicegroups to search for. defaults to nagios_servicegroups
* `node['nagios']['templates_databag']` - the databag containing templates to search for. defaults to nagios_templates
* `node['nagios']['eventhandlers_databag']` - the databag containing eventhandlers to search for. defaults to nagios_eventhandlers
* `node['nagios']['unmanaged_hosts_databag']` - the databag containing unmanagedhosts to search for. defaults to nagios_unmanagedhosts
* `node['nagios']['serviceescalations_databag']` - the databag containing serviceescalations to search for. defaults to nagios_serviceescalations
* `node['nagios']['contacts_databag']` - the databag containing contacts to search for. defaults to nagios_contacts
* `node['nagios']['contactgroups_databag']` - the databag containing contactgroups to search for. defaults to nagios_contactgroups
* `node['nagios']['servicedependencies_databag']` - the databag containing servicedependencies to search for. defaults to nagios_servicedependencies
* `node['nagios']['host_name_attribute']` - node attribute to use for naming the host. Must be unique across monitored nodes. Defaults to hostname
* `node['nagios']['regexp_matching']` - Attribute to enable [regexp matching](http://nagios.sourceforge.net/docs/3_0/configmain.html#use_regexp_matching). Defaults to 0.
* `node['nagios']['large_installation_tweaks']` - Attribute to enable [large installation tweaks](http://nagios.sourceforge.net/docs/3_0/largeinstalltweaks.html). Defaults to 0.
* `node['nagios']['templates']`
* `node['nagios']['interval_length']` - minimum interval.

These set directives in the default host template. Unless explicitly
overridden, they will be inheirited by the host definitions for each
disovered node and `nagios_unmanagedhosts` data bag. For more
information about these directives, see the Nagios documentation for
[host definitions](http://nagios.sourceforge.net/docs/3_0/objectdefinitions.html#host).

* `node['nagios']['default_host']['flap_detection']` - Defaults to `true`.
* `node['nagios']['default_host']['check_period']` - Defaults to `'24x7'`.
* `node['nagios']['default_host']['check_interval']` - In seconds. Must be divisible by `node['nagios']['interval_length']`. Defaults to `15`.
* `node['nagios']['default_host']['retry_interval']` - In seconds. Must be divisible by `node['nagios']['interval_length']`. Defaults to `15`.
* `node['nagios']['default_host']['max_check_attempts']` - Defaults to `1`.
* `node['nagios']['default_host']['check_command']` - Defaults to the pre-defined command `'check-host-alive'`.
* `node['nagios']['default_host']['notification_interval']` - In seconds. Must be divisible by `node['nagios']['interval_length']`. Defaults to `300`.
* `node['nagios']['default_host']['notification_options']` - Defaults to `'d,u,r'`.

* `node['nagios']['server']['web_server']` - web server to use. supports Apache or Nginx, default "apache"
* `node['nagios']['server']['nginx_dispatch']` - nginx dispatch method. supports cgi or php, default "cgi"
* `node['nagios']['server']['stop_apache']` - stop apache service if using nginx, default false
* `node['nagios']['server']['redirect_root']` - if using Apache, should http://server/ redirect to http://server/nagios3 automatically, default false
* `node['nagios']['server']['normalize_hostname']` - If set to true, normalize all hostnames in hosts.cfg to lowercase. Defaults to false.

These are additional nagios.cfg options.

 * `node['nagios']['conf']['max_service_check_spread']`  - Defaults to 5
 * `node['nagios']['conf']['max_host_check_spread']`     - Defaults to 5
 * `node['nagios']['conf']['service_check_timeout']`     - Defaults to 60
 * `node['nagios']['conf']['host_check_timeout']`        - Defaults to 30
 * `node['nagios']['conf']['process_performance_data']`  - Defaults to 0
 * `node['nagios']['conf']['date_format']`               - Defaults to 'iso8601'
 * `node['nagios']['conf']['p1_file']`                   - Defaults to `#{node['nagios']['home']}/p1.pl`
 * `node['nagios']['conf']['debug_level']`               - Defaults to 0
 * `node['nagios']['conf']['debug_verbosity']`           - Defaults to 1
 * `node['nagios']['conf']['debug_file']`                - Defaults to `#{node['nagios']['state_dir']}/#{node['nagios']['server']['name']}.debug`

 These are nagios cgi.config options.

 * `node['nagios']['cgi']['show_context_help']`                         - Defaults to 1
 * `node['nagios']['cgi']['authorized_for_system_information']`         - Defaults to '*'
 * `node['nagios']['cgi']['authorized_for_configuration_information']`  - Defaults to '*'
 * `node['nagios']['cgi']['authorized_for_system_commands']`            - Defaults to '*'
 * `node['nagios']['cgi']['authorized_for_all_services']`               - Defaults to '*'
 * `node['nagios']['cgi']['authorized_for_all_hosts']`                  - Defaults to '*'
 * `node['nagios']['cgi']['authorized_for_all_service_commands']`       - Defaults to '*'
 * `node['nagios']['cgi']['authorized_for_all_host_commands']`          - Defaults to '*'
 * `node['nagios']['cgi']['default_statusmap_layout']`                  - Defaults to 5
 * `node['nagios']['cgi']['default_statuswrl_layout']`                  - Defaults to 4
 * `node['nagios']['cgi']['escape_html_tags']`                          - Defaults to 0
 * `node['nagios']['cgi']['action_url_target']`                         - Defaults to '_blank'
 * `node['nagios']['cgi']['notes_url_target']`                          - Defaults to '_blank'
 * `node['nagios']['cgi']['lock_author_names']`                         - Defaults to 1


Recipes
-------
### default
Includes the `nagios::client` recipe to install NRPE client.

### client
Includes the correct NRPE client installation recipe based on platform, either `nagios::client_package` or `nagios::client_source`.

The client recipe searches for servers allowed to connect via NRPE that have a role named in the `node['nagios']['server_role']` attribute. The recipe will also install the required packages and start the NRPE service. A custom plugin for checking memory is also added.

Searches are confined to the node's `chef_environment` unless the `multi_environment_monitoring` attribute has been set to true.

Client commands for NRPE can be installed using the nrpecheck lwrp. (See __Resources/Providers__ below.)

RHEL and Fedora default to installation via source, but you can install NRPE via package by changing `node['nagios']['client']['install_method']` to "package". Note that this will enable the EPEL repository on RHEL systems, which may not be desired. You will also need to modify `node['nagios']['nrpe']['packages']` to include the appropriate NRPE plugins for your environment. The complete list is available at `http://dl.fedoraproject.org/pub/epel/6/x86_64/repoview/letter_n.group.html`

### client\_package
Installs the NRPE client and plugins from packages. Default for Debian / Ubuntu systems.

### client\_source
Installs the NRPE client and plugins from source. Default for Redhat and Fedora based systems, as native packages for NRPE are not available in the default repositories.

### server
Includes the correct client installation recipe based on platform, either `nagios::server_package` or `nagios::server_source`.

The server recipe sets up Apache as the web front end by default. The nagios::client recipe is also included. This recipe also does a number of searches to dynamically build the hostgroups to monitor, hosts that belong to them and admins to notify of events/alerts.

Searches are confined to the node's `chef_environment` unless multi-environment monitoring is enabled.

The recipe does the following:

1. Searches for users in 'users' databag belonging to a 'sysadmin' group, and authorizes them to access the Nagios web UI and also to receive notification e-mails.
2. Searches all available roles/environments and builds a list which will become the Nagios hostgroups.
3. Places nodes in Nagios hostgroups by role / environment membership.
4. Installs various packages required for the server.
5. Sets up configuration directories.
6. Moves the package-installed Nagios configuration to a 'dist' directory.
7. Disables the 000-default VirtualHost present on Debian/Ubuntu Apache2 package installations.
8. Templates configuration files for services, contacts, contact groups, templates, hostgroups and hosts.
9. Enables the Nagios web UI.
10. Starts the Nagios server service


### server\_package
Installs the Nagios server from packages. Default for Debian / Ubuntu systems.

### server\_source
Installs the Nagios server from source. Default for Red Hat / Fedora based systems as native packages for Nagios are not available in the default repositories.

### pagerduty
Installs pagerduty plugin for nagios. If you only have a single pagerduty key, you can simply set a `node['nagios']['pagerduty_key']` attribute on your server.  For multiple pagerduty key configuration see Pager Duty under Data Bags.

This recipe was written based on the [Nagios Integration Guide](http://www.pagerduty.com/docs/guides/nagios-integration-guide) from PagerDuty which explains how to get an API key for your Nagios server.


Data Bags
---------
### Users
Create a `users` data bag that will contain the users that will be able to log into the Nagios webui. Each user can use htauth with a specified password, or an openid. Users that should be able to log in should be in the sysadmin group. Example user data bag item:

```javascript
{
  "id": "nagiosadmin",
  "groups": "sysadmin",
  "htpasswd": "hashed_htpassword",
  "openid": "http://nagiosadmin.myopenid.com/",
  "nagios": {
    "pager": "nagiosadmin_pager@example.com",
    "email": "nagiosadmin@example.com"
  }
}
```

When using `server_auth_method` 'openid' (default), use the openid in the data bag item. Any other value for this attribute (e.g., "htauth", "htpasswd", etc) will use the htpasswd value as the password in `/etc/nagios3/htpasswd.users`.

The openid must have the http:// and trailing /. The htpasswd must be the hashed value. Get this value with htpasswd:

    % htpasswd -n -s nagiosadmin
    New password:
    Re-type new password:
    nagiosadmin:{SHA}oCagzV4lMZyS7jl2Z0WlmLxEkt4=

For example use the `{SHA}oCagzV4lMZyS7jl2Z0WlmLxEkt4=` value in the data bag.

### Contacts and Contact Groups
To send alerting notification to contacts that aren't authorized to login to Nagios via the 'users' data bag create `nagios_contacts` and `nagios_contactgroups` data bags.

Example `nagios_contacts` data bag item

```javascript
{
  "id": "devs",
  "alias": "Developers",
  "use": "default-contact",
  "email": "devs@company.com",
  "pager": "page_the_devs@company.com"
}
```

Example `nagios_contactgroup` data bag item

```javascript
{
  "id": "non_admins",
  "alias": "Non-Administrator Contacts",
  "members": "devs helpdesk managers"
}
```

### Services
To add service checks to Nagios create a `nagios_services` data bag containing definitions for services to be monitored. This allows you to add monitoring rules without directly editing the services and commands templates in the cookbook. Each service will be named based on the id of the data bag item and the command will be named using the same id prepended with "check\_". Just make sure the id in your data bag doesn't conflict with a service or command already defined in the templates.

Here's an example of a service check for sshd that you could apply to all hostgroups:

```javascript
{
  "id": "ssh",
  "hostgroup_name": "linux",
  "command_line": "$USER1$/check_ssh $HOSTADDRESS$"
}
```

You may optionally define the service template for your service by including `service_template` and a valid template name. Example:  "service_template": "special_service_template". You may also optionally add a service description that will be displayed in the Nagios UI using "description": "My Service Name". If this is not present the databag item ID will be used as the description. You use defined escalations for the service with 'use_escalation'. See ___Service_Escalations__ for more information.

You may also use an already defined command definition by omitting the command\_line parameter and using use\_existing\_command parameter instead:

```javascript
{
  "id": "pingme",
  "hostgroup_name": "all",
  "use_existing_command": "check-host-alive"
}
```

You may also specify that a check only be run if the nagios server is in a specific environment. This is useful if you have nagios servers in several environments but you would like a service check to only apply in one particular environment:

```javascript
{
  "id": "ssh",
  "hostgroup_name": "linux",
  "activate_check_in_environment": "staging",
  "command_line": "$USER1$/check_ssh $HOSTADDRESS$"
}
```

### Service Groups
Create a nagios\_servicegroups data bag that will contain definitions for service groups. Each server group will be named based on the id of the data bag.

```javascript
{
  "id": "ops",
  "alias": "Ops",
  "notes": "Services for ops"
}
```

You can group your services by using the "servicegroups" keyword in your services data bags. For example, to have your ssh checks show up under the ops service group, you could define it like this:

```javascript
{
  "id": "ssh",
  "hostgroup_name": "all",
  "command_line": "$USER1$/check_ssh $HOSTADDRESS$",
  "servicegroups": "ops"
}
```

### Service Dependencies
Create a nagios\_servicedependencies data bag that will contain definitions for service dependencies. Each service dependency will be named based on the id of the data bag. Each service dependency requires a dependent host name and/or hostgroup name, dependent service description, host name and/or hostgroup name, and service description.

```javascript
{
  "id": "Service_X_depends_on_Service_Y",
  "dependent_host_name": "ServerX",
  "dependent_service_description": "Service X",
  "host_name": "ServerY",
  "service_description": "Service Y",
  "notification_failure_criteria": "u, c"
}
```

Additional directives can be defined as described in the [Nagios documentation](http://nagios.sourceforge.net/docs/3_0/objectdefinitions.html#servicedependency).

### Templates
Templates are optional, but allow you to specify combinations of attributes to apply to a service. Create a nagios_templates\ data bag that will contain definitions for templates to be used. Each template need only specify id and whichever parameters you want to override.

Here's an example of a template that reduces the check frequency to once per day and changes the retry interval to 1 hour.

```javascript
{
  "id": "dailychecks",
  "check_interval": "86400",
  "retry_interval": "3600"
}
```

You then use the template in your service data bag as follows:

```javascript
{
  "id": "expensive_service_check",
  "hostgroup_name": "linux",
  "command_line": "$USER1$/check_example $HOSTADDRESS$",
  "service_template": "dailychecks"
}
```

### Search Defined Hostgroups
Create a nagios\_hostgroups data bag that will contain definitions for Nagios hostgroups populated via search. These data bags include a Chef node search query that will populate the Nagios hostgroup with nodes based on the search.

Here's an example to find all HP hardware systems for an "hp_systems" hostgroup:

```javascript
{
  "search_query": "dmi_system_manufacturer:HP",
  "hostgroup_name": "hp_systems",
  "id": "hp_systems"
}
```

### Monitoring Systems Not In Chef
Create a nagios\_unmanagedhosts data bag that will contain definitions for hosts not in Chef that you would like to manage. "hostgroups" can be an existing Chef role (every Chef role gets a Nagios hostgroup) or a new hostgroup. Note that "hostgroups" must be an array of hostgroups even if it contains just a single hostgroup.

Here's an example host definition:

```javascript
{
  "address": "webserver1.mydmz.dmz",
  "hostgroups": ["web_servers","production_servers"],
  "id": "webserver1",
  "notifications": 1
}
```

Similar to services, you may also filter unmanaged hosts by environment. This is useful if you have nagios servers in several environments but you would like to monitor an unmanaged host that only exists in a particular environment:

```javascript
{
  "address": "webserver1.mydmz.dmz",
  "hostgroups": ["web_servers","production_servers"],
  "id": "webserver1",
  "environment": "production",
  "notifications": 1
}
```

### Service Escalations
You can optionally define service escalations for the data bag defined services. Doing so involves two steps - creating the `nagios_serviceescalations` data bag and invoking it from the service. For example, to create an escalation to page managers on a 15 minute period after the 3rd page:

```javascript
{
  "id": "15-minute-escalation",
  "contact_groups": "managers",
  "first_notification": "3",
  "last_notification": "0",
  "escalation_period": "24x7",
  "notification_interval": "900"
}
```

Then, in the service data bag,

```javascript
{
  "id": "my-service",
  // ...
  "use_escalation": "15-minute-escalation"
}
```

You can also define escalations using wildcards, like so:

```javascript
{
  "id": "first-warning",
  "contact_groups": "sysadmin",
  "hostgroup_name": "*",
  "first_notification": "1",
  "last_notification": "0",
  "notification_interval": "21600",
  "escalation_period": "24x7",
  "escalation_options": "w",
  "hostgroup_name": "*",
  "service_description": "*",
  "register": 1
}
```

This configures notifications for all warnings to repeat on a given interval (under the default config, every 6 hours). (Note that you must register this kind of escalation, as it is not a template.)

### Event Handlers
You can optionally define event handlers to trigger on service alerts by creating a nagios\_eventhandlers data bag that will contain definitions of event handlers for services monitored via Nagios.

This example event handler data bags restarts chef-client. Note: This assumes you have already defined a NRPE job restart\_chef-client on the host where this command will run. You can use the NRPE LWRP to add commands to your local NRPE configs from within your cookbooks.

```javascript
{
  "command_line": "$USER1$/check_nrpe -H $HOSTADDRESS$ -t 45 -c restart_chef-client",
  "id": "restart_chef-client"
}
```

Once you've defined an event handler you will need to add the event handler to a service definition in order to trigger the action. See the example service definition below.

```javascript
{
  "command_line": "$USER1$/check_nrpe -H $HOSTADDRESS$ -t 45 -c check_chef_client",
  "hostgroup_name": "linux",
  "id": "chef-client",
  "event_handler": "restart_chef-client"
}
```

### Pager Duty
You can define pagerduty contacts and keys by creating nagios\_pagerduty data bags that contain the contact and
the relevant key. Setting admin\_contactgroup to "true" will add this pagerduty contact to the admin contact group
created by this cookbook.

       {
         "id": "pagerduty_critical",
         "admin_contactgroup": "true",
         "key": "a33e5ef0ac96772fbd771ddcccd3ccd0"
       }

You can add these contacts to any contactgroups you create.

Monitoring Role
---------------
Create a role to use for the monitoring server. The role name should match the value of the attribute "`node['nagios']['server_role']`". By default, this is '`monitoring`'. For example:

```ruby
# roles/monitoring.rb
name 'monitoring'
description 'Monitoring server'
run_list(
  'recipe[nagios::server]'
)

default_attributes(
  'nagios' => {
    'server_auth_method' => 'htauth'
  }
)
```

```bash
$ knife role from file monitoring.rb
```


Definitions
-----------
### nagios\_conf
This definition is used to drop in a configuration file in the base Nagios configuration directory's conf.d. This can be used for customized configurations for various services.


Libraries
---------
### default
The library included with the cookbook provides some helper methods used in templates.

* `nagios_boolean`
* `nagios_interval` - calculates interval based on interval length and a given number of seconds.
* `nagios_attr` - retrieves a nagios attribute from the node.


Resources/Providers
-------------------
### nrpecheck

The nrpecheck LWRP provides an easy way to add and remove NRPE checks from within cookbooks.

#### Actions

- `:add` creates a NRPE configuration file and restart the NRPE process. Default action.
- `:remove` removes the configuration file and restart the NRPE process

#### Attribute Parameters

- `command_name`  The name of the check. This is the command that you will call from your nagios\_service data bag check
- `warning_condition` String that you will pass to the command with the -w flag
- `critical_condition` String that you will pass to the command with the -c flag
- `command` The actual command to execute (including the path). If this is not specified, this will use `node['nagios']['plugin_dir']/command_name` as the path to the command.
- `parameters` Any additional parameters you wish to pass to the plugin.

#### Examples

```ruby
# Use LWRP to define check_load
nagios_nrpecheck "check_load" do
  command "#{node['nagios']['plugin_dir']}/check_load"
  warning_condition node['nagios']['checks']['load']['warning']
  critical_condition node['nagios']['checks']['load']['critical']
  action :add
end
```

```ruby
# Remove the check_load definition
nagios_nrpecheck "check_load" do
  action :remove
end
```


Usage
-----
### server setup
Create a role named '`monitoring`', and add the nagios server recipe to the `run_list`. See __Monitoring Role__ above for an example.

Apply the Nagios client recipe to nodes in order to install the NRPE client

By default the Nagios server will only monitor systems in its same environment. To change this set the `multi_environment_monitoring` attribute. See __Attributes__

Create data bag items in the `users` data bag for each administer you would like to be able to login to the Nagios server UI. Pay special attention to the method you would like to use to authorization users (openid or htauth). See __Users__ and __Atttributes__

At this point you now have a minimally functional Nagios server, however the server will lack any service checks outside of the single Nagios Server health check.

### defining checks
NRPE commands are defined in recipes using the nrpecheck LWRP provider. For base system monitoring such as load, ssh, memory, etc you may want to create a cookbook in your environment that defines each monitoring command via the LWRP. See the examples folder for an example of base monitoring.

With NRPE commands created using the LWRP you will need to define Nagios services to use those commands. These services are defined using the `nagios_services` data bag and applied to roles and/or environments. See __Services__

### enabling notifications
You need to set `default['nagios']['notifications_enabled'] = 1` attribute on your Nagios server to enable email notifications.

For email notifications to work an appropriate mail program package and local MTA need to be installed so that /usr/bin/mail or /bin/mail is available on the system.

Example:

Include [postfix cookbook](https://github.com/opscode-cookbooks/postfix) to be installed on your Nagios server node.

Add override_attributes to your `monitoring` role:

```ruby
# roles/monitoring.rb
name 'monitoring'
description 'Monitoring Server'
run_list(
  'recipe[nagios::server]',
  'recipe[postfix]'
)

override_attributes(
  'nagios' => { 'notifications_enabled' => '1' },
  'postfix' => { 'myhostname':'your_hostname', 'mydomain':'example.com' }
)

default_attributes(
  'nagios' => { 'server_auth_method' => 'htauth' }
)
```

```bash
$ knife role from file monitoring.rb
```


License & Authors
-----------------
- Author:: Joshua Sierles <joshua@37signals.com>
- Author:: Nathan Haneysmith <nathan@opscode.com>
- Author:: Joshua Timberman <joshua@opscode.com>
- Author:: Seth Chisamore <schisamo@opscode.com>
- Author:: Tim Smith <tsmith84@gmail.com>

```text
Copyright 2009, 37signals
Copyright 2009-2013, Opscode, Inc
Copyright 2012, Webtrends Inc.

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
NginxSimpleCGI
==============

This cookbook provides CGI support for NGINX via SimpleCGI.

Repository
----------

https://github.com/heavywater/chef-nginx_simplecgi

Options
-------

* `node[:nginx_simplecgi][:cgi] -> Enable CGI dispatch`
* `node[:nginx_simplecgi][:php] -> Enable PHP dispatch`
* `node[:nginx_simplecgi][:php_cgi_bin] -> PHP executable path for CGI`
* `node[:nginx_simplecgi][:init_type] -> Init style for dispatchers`
* `node[:nginx_simplecgi][:dispatcher_directory] -> Directory to contain socket and pid files`
* `node[:nginx_simplecgi][:dispatcher_processes] -> Number of dispatcher processes for handling requests`

Template Helper
---------------

A template method helper, `dispatch` is provided to add the require location 
block into your nginx configuration files:

```ruby
<%= nginx_dispatch(:cgi) %>
```

The default call will output:

```
  location ~ ^/cgi-bin/.*\.cgi$ {
    gzip off; 
    fastcgi_pass  unix:/var/run/nginx/cgiwrap-dispatch.sock;
    fastcgi_index index.cgi;
    fastcgi_param SCRIPT_FILENAME /usr/lib$fastcgi_script_name;
    fastcgi_param QUERY_STRING     $query_string;
    fastcgi_param REQUEST_METHOD   $request_method;
    fastcgi_param CONTENT_TYPE     $content_type;
    fastcgi_param CONTENT_LENGTH   $content_length;
    fastcgi_param GATEWAY_INTERFACE  CGI/1.1;
    fastcgi_param SERVER_SOFTWARE    nginx;
    fastcgi_param SCRIPT_NAME        $fastcgi_script_name;
    fastcgi_param REQUEST_URI        $request_uri;
    fastcgi_param DOCUMENT_URI       $document_uri;
    fastcgi_param DOCUMENT_ROOT      $document_root;
    fastcgi_param SERVER_PROTOCOL    $server_protocol;
    fastcgi_param REMOTE_ADDR        $remote_addr;
    fastcgi_param REMOTE_PORT        $remote_port;
    fastcgi_param SERVER_ADDR        $server_addr;
    fastcgi_param SERVER_PORT        $server_port;
    fastcgi_param SERVER_NAME        $server_name;
  }
```

Available options:

* `:pattern -> change the pattern nginx matches`
* `:cgi_bin_dir -> change the prefix directory of the local cgi-bin`
* `:dispatcher -> use a custom dispatcher (socket or tcp based)`
* `:custom -> string to be appended within the location block`

The method will also accept a block that will be eval'd and the result appended
within the location block.
Description
===========

This is a short-and-simple cookbook to provide a user_ulimit resource for overriding various ulimit settings. It places configured templates into /etc/security/limits.d/, named for the user the ulimit applies to.

It also provides a helper recipe (default.rb) for allowing ulimit overrides with the 'su' command on Ubuntu, which is disabled by default for some reason.

Requirements
============

Add to your repo, then depend upon this cookbook from wherever you need to override ulimits.

Attributes
==========

* `node['ulimit']['pam_su_template_cookbook']` - Defaults to nil (current cookbook).  Determines what cookbook the su pam.d template is taken from
* `node['ulimit']['users']` - Defaults to empty Hash.  List of users with their limits

Usage
=====

Consume the user_ulimit resource like so:
```ruby
user_ulimit "tomcat" do
  filehandle_limit 8192 # optional
  process_limit 61504 # optional
  memory_limit 1024 # optional
  core_limit 2048 # optional
end
```

You can also define limits using attributes on roles or nodes:

```
"default_attributes": {
   "ulimit": {
      "users": {
         "tomcat": {
            "filehandle_limit": 8193,
               "process_limit": 61504
             },
            "hbase": {
               "filehandle_limit": 32768
             }
       }
    }
 }
 ```

Domain LWRP
===========

```ruby
ulimit_domain 'my_user' do
  rule do
    item :nofile
    type :hard
    value 10000
  end
  rule do
    item :nofile
    type :soft
    value 5000
  end
end
```
modules-cookbook
================

= DESCRIPTION:
Chef cookbook to manage linux modules with /etc/modules and modprobe (linux 2.6 +)

= REQUIREMENTS:

Linux 2.6+
Ubuntu >9.10 (for the moment. use upstart and not init, any contribution is welcome)

= ATTRIBUTES:
node['modules'] = A namespace for modules settings.

= USAGE:
There are two ways of setting sysctl values:
1. Set chef attributes, E.G.:
   default['modules']['loop']
2. With Ressource/Provider

Resource/Provider
=================

This cookbook includes LWRPs for managing:
* modules
* modules_multi

modules
--------

# Actions

- :save: save and load a module (default)
- :load: load a module
- :remove: remove a (previously saved or load) module.

# Attribute Parameters

- module
- options
- path


# Examples

```
modules "8021q" do
  action :load
end
```

modules_multi
------------

#Actions

- :save: save and load modules (default)
- :remove: remove (previously saved or load) modules.

# Attribute Parameters

- modules
- path

# Examples
# <a name="title"></a> rbenv Chef Cookbook

[![Build Status](https://secure.travis-ci.org/fnichol/chef-rbenv.png?branch=master)](http://travis-ci.org/fnichol/chef-rbenv)

## <a name="description"></a> Description

Manages [rbenv][rbenv_site] and its installed Rubies.
Several lightweight resources and providers ([LWRPs][lwrp]) are also defined.

## <a name="usage"></a> Usage

### <a name="usage-system-rubies"></a> rbenv Installed System-Wide with Rubies

Most likely, this is the typical case. Include `recipe[rbenv::system]` in your
run\_list and override the defaults you want changed. See [below](#attributes)
for more details.

If your platform is the Mac, you may need to modify your
[profile](#mac-system-note).

### <a name="usage-user-rubies"></a> rbenv Installed For A Specific User with Rubies

If you want a per-user install (like on a Mac/Linux workstation for
development, CI, etc.), include `recipe[rbenv::user]` in your run\_list and
add a user hash to the `user_installs` attribute list. For example:

    node.default['rbenv']['user_installs'] = [
      { 'user'    => 'tflowers',
        'rubies'  => ['1.9.3-p0', 'jruby-1.6.5'],
        'global'  => '1.9.3-p0',
        'gems'    => {
          '1.9.3-p0'    => [
            { 'name'    => 'bundler',
              'version' => '1.1.rc.5'
            },
            { 'name'    => 'rake' }
          ],
          'jruby-1.6.5' => [
            { 'name'    => 'rest-client' }
          ]
        }
      }
    ]

See [below](#attributes) for more details.

### <a name="usage-system"></a> rbenv Installed System-Wide and LWRPs Defined

If you want to manage your own rbenv environment with the provided
LWRPs, then include `recipe[rbenv::system_install]` in your run\_list
to prevent a default rbenv Ruby being installed. See the
[Resources and Providers](#lwrps) section for more details.

If your platform is the Mac, you may need to modify your
[profile](#mac-system-note).

### <a name="usage-user"></a> rbenv Installed For A Specific User and LWRPs Defined

If you want to manage your own rbenv environment for users with the provided
LWRPs, then include `recipe[rbenv::user_install]` in your run\_list and add a
user hash to the `user_installs` attribute list. For example:

    node.default['rbenv']['user_installs'] = [
      { 'user' => 'tflowers' }
    ]

See the [Resources and Providers](#lwrps) section for more details.

### <a name="usage-minimal"></a> Ultra-Minimal Access To LWRPs

Simply include `recipe[rbenv]` in your run\_list and the LWRPs will be
available to use in other cookboks. See the [Resources and Providers](#lwrps)
section for more details.

### <a name="usage-other"></a> Other Use Cases

* If node is running in a Vagrant VM, then including `recipe[rbenv::vagrant]`
in your run\_list can help with resolving the *chef-solo* binary on subsequent

## <a name="requirements"></a> Requirements

### <a name="requirements-chef"></a> Chef

Tested on 11.4.4 but newer and older version should work just
fine. File an [issue][issues] if this isn't the case.

### <a name="requirements-platform"></a> Platform

The following platforms have been tested with this cookbook, meaning that
the recipes and LWRPs run on these platforms without error:

* ubuntu (10.04/12.04)
* debian (6.0)
* freebsd
* redhat
* centos
* fedora
* amazon
* scientific
* suse
* mac\_os\_x

Please [report][issues] any additional platforms so they can be added.

### <a name="requirements-cookbooks"></a> Cookbooks

There are **no** external cookbook dependencies. However, if you
want to manage Ruby installations or use the `rbenv_ruby` LWRP then you will
need to include the [ruby\_build cookbook][ruby_build_cb].

## <a name="installation"></a> Installation

Depending on the situation and use case there are several ways to install
this cookbook. All the methods listed below assume a tagged version release
is the target, but omit the tags to get the head of development. A valid
Chef repository structure like the [Opscode repo][chef_repo] is also assumed.

### <a name="installation-berkshelf"></a> Using Berkshelf

[Berkshelf][berkshelf] is a cookbook dependency manager and development
workflow assistant. To install Berkshelf:

    cd chef-repo
    gem install berkshelf
    berks init

To reference the Git version:

    repo="fnichol/chef-rbenv"
    latest_release=$(curl -s https://api.github.com/repos/$repo/git/refs/tags \
    | ruby -rjson -e '
      j = JSON.parse(STDIN.read);
      puts j.map { |t| t["ref"].split("/").last }.sort.last
    ')
    cat >> Berksfile <<END_OF_BERKSFILE
    cookbook 'rbenv',
      :git => 'git://github.com/$repo.git', :branch => '$latest_release'
    END_OF_BERKSFILE
    berks install

### <a name="installation-librarian"></a> Using Librarian-Chef

[Librarian-Chef][librarian] is a bundler for your Chef cookbooks.
To install Librarian-Chef:

    cd chef-repo
    gem install librarian
    librarian-chef init

To reference the Git version:

    repo="fnichol/chef-rbenv"
    latest_release=$(curl -s https://api.github.com/repos/$repo/git/refs/tags \
    | ruby -rjson -e '
      j = JSON.parse(STDIN.read);
      puts j.map { |t| t["ref"].split("/").last }.sort.last
    ')
    cat >> Cheffile <<END_OF_CHEFFILE
    cookbook 'rbenv',
      :git => 'git://github.com/$repo.git', :ref => '$latest_release'
    END_OF_CHEFFILE
    librarian-chef install

### <a name="installation-platform"></a> From the Community Site

This cookbook is not currently available on the site due to the flat
namespace for cookbooks.

## <a name="recipes"></a> Recipes

### <a name="recipes-default"></a> default

Installs the rbenv gem and initializes Chef to use the Lightweight Resources
and Providers ([LWRPs][lwrp]).

Use this recipe explicitly if you only want access to the LWRPs provided.

### <a name="recipes-system-install"></a> system_install

Installs the rbenv codebase system-wide (that is, into `/usr/local/rbenv`). This
recipe includes *default*.

Use this recipe by itself if you want rbenv installed system-wide but want
to handle installing Rubies, invoking LWRPs, etc..

### <a name="recipes-system"></a> system

Installs the rbenv codebase system-wide (that is, into `/usr/local/rbenv`) and
installs rubies driven off attribute metadata. This recipe includes *default*
and *system_install*.

Use this recipe by itself if you want rbenv installed system-wide with rubies
installed.

### <a name="recipes-user-install"></a> user_install

Installs the rbenv codebase for a list of users (selected from the
`node['rbenv']['user_installs']` hash). This recipe includes *default*.

Use this recipe by itself if you want rbenv installed for specific users in
isolation but want each user to handle installing Rubies, invoking LWRPs, etc.

### <a name="recipes-user"></a> user

Installs the rbenv codebase for a list of users (selected from the
`node['rbenv']['user_installs']` hash) and installs rubies driven off attribte
metadata. This recipe includes *default* and *user_install*.

Use this recipe by itself if you want rbenv installed for specific users in
isolation with rubies installed.

### <a name="recipes-vagrant"></a> vagrant

An optional recipe if Chef is installed in a non-rbenv Ruby in a
[Vagrant][vagrant] virtual machine. This recipe installs a `chef-solo`
wrapper script so Chef doesn't need to be re-installed in the global rbenv Ruby.

## <a name="attributes"></a> Attributes

### <a name="attributes-git-url"></a> git_url

The Git URL which is used to install rbenv.

The default is `"git://github.com/sstephenson/rbenv.git"`.

### <a name="attributes-git-ref"></a> git_ref

A specific Git branch/tag/reference to use when installing rbenv. For
example, to pin rbenv to a specific release:

    node.default['ruby_build']['git_ref'] = "v0.2.1"

The default is `"v0.4.0"`.

### <a name="attributes-upgrade"></a> upgrade

Determines how to handle installing updates to the rbenv. There are currently
2 valid values:

* `"none"`, `false`, or `nil`: will not update rbenv and leave it in its
  current state.
* `"sync"` or `true`: updates rbenv to the version specified by the
  `git_ref` attribute or the head of the master branch by default.

The default is `"none"`.

### <a name="attributes-root-path"></a> root_path

The path prefix to rbenv in a system-wide installation.

The default is `"/usr/local/rbenv"`.

### <a name="attributes-rubies"></a> rubies

A list of additional system-wide rubies to be built and installed using the
[ruby\_build cookbook][ruby_build_cb]. You **must** include `recipe[ruby_build]`
in your run\_list for the `rbenv_ruby` LWRP to work properly. For example:

    node.default['rbenv']['rubies'] = [ "1.9.3-p0", "jruby-1.6.5" ]

The default is an empty array: `[]`.

Additional environment variables can be passed to ruby_build via the environment variable.
For example:

    node.default['rbenv']['rubies'] = [ "1.9.3-p0", "jruby-1.6.5",
      {
      :name => '1.9.3-327',
      :environment => { 'CFLAGS' => '-march=native -O2 -pipe' }
      }
    ]

### <a name="attributes-user-rubies"></a> user_rubies

A list of additional system-wide rubies to be built and installed (using the
[ruby\_build cookbook][ruby_build_cb]) per-user when not explicitly set.
For example:

    node.default['rbenv']['user_rubies'] = [ "1.8.7-p352" ]

The default is an empty array: `[]`.

Additional environment variables can be passed to ruby_build via the environment variable.
For example:

    node.default['rbenv']['user_rubies'] = [ "1.8.7-p352",
      {
      :name => '1.9.3-327',
      :environment => { 'CFLAGS' => '-march=native -O2 -pipe' }
      }
    ]
### <a name="attributes-gems"></a> gems

A hash of gems to be installed into arbitrary rbenv-managed rubies system wide.
See the [rbenv_gem](#lwrps-rbgem) resource for more details about the options
for each gem hash and target Ruby environment. For example:

    node.default['rbenv']['gems'] = {
      '1.9.3-p0' => [
        { 'name'    => 'vagrant' },
        { 'name'    => 'bundler'
          'version' => '1.1.rc.5'
        }
      ],
      '1.8.7-p352' => [
        { 'name'    => 'nokogiri' }
      ]
    }

The default is an empty hash: `{}`.

### <a name="attributes-user-gems"></a> user_gems

A hash of gems to installed into arbitrary rbenv-managed rubies for each user
when not explicitly set. See the [rbenv_gem](#lwrps-rbgem) resource for more
details about the options for each gem hash and target Ruby environment. See
the [gems attribute](#attributes-gems) for an example.

The default is an empty hash: `{}`.

### <a name="attributes-vagrant-system-chef-solo"></a> vagrant/system_chef_solo

If using the `vagrant` recipe, this sets the path to the package-installed
*chef-solo* binary.

The default is `"/opt/ruby/bin/chef-solo"`.

### <a name="attributes-create-profiled"></a> create_profiled

The user's shell needs to know about rbenv's location and set up the
PATH environment variable. This is handled in the
[system_install](#recipes-system_install) and
[user_install](#recipes-user_install) recipes by dropping off
`/etc/profile.d/rbenv.sh`. However, this requires root privilege,
which means that a user cannot use a "user install" for only their
user.

Set this attribute to `false` to skip creation of the
`/etc/profile.d/rbenv.sh` template. For example:

    node.default['rbenv']['create_profiled'] = false

The default is `true`.

## <a name="lwrps"></a> Resources and Providers

### <a name="lwrps-rg"></a> rbenv_global

This resource sets the global version of Ruby to be used in all shells, as per
the [rbenv global docs][rbenv_3_1].

#### <a name="lwrps-rg-actions"></a> Actions

<table>
  <thead>
    <tr>
      <th>Action</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>create</td>
      <td>
        Sets the global version of Ruby to be used in all shells. See 3.1
        rbenv global<sup>(1)</sup> for more details.
      </td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>

1. [3.1 rbenv global][rbenv_3_1]

#### <a name="lwrps-rg-attributes"></a> Attributes

<table>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Description</th>
      <th>Default Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rbenv_version</td>
      <td>
        <b>Name attribute:</b> a version of Ruby being managed by rbenv.
        <b>Note:</b> the version of Ruby must already be installed--this LWRP
        will not install it automatically.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>user</td>
      <td>
        A users's isolated rbenv installation on which to apply an action. The
        default value of <code>nil</code> denotes a system-wide rbenv
        installation is being targeted. <b>Note:</b> if specified, the user
        must already exist.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>root_path</td>
      <td>
        The path prefix to rbenv installation, for example:
        <code>/opt/rbenv</code>.
      </td>
      <td><code>nil</code></td>
    </tr>
  </tbody>
</table>

#### <a name="lwrps-rg-examples"></a> Examples

##### Set A Ruby As Global

    rbenv_global "1.8.7-p352"

##### Set System Ruby As Global

    rbenv_global "system"

##### Set A Ruby As Global For A User

    rbenv_global "jruby-1.7.0-dev" do
      user "tflowers"
    end

### <a name="lwrps-rsc"></a> rbenv_script

This resource is a wrapper for the `script` resource which wraps the code block
in an rbenv-aware environment. See the Opscode
[script resource][script_resource] page and the [rbenv shell][rbenv_3_3]
documentation for more details.

#### <a name="lwrps-rsc-actions"></a> Actions

<table>
  <thead>
    <tr>
      <th>Action</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>run</td>
      <td>Run the script</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>nothing</td>
      <td>Do not run this command</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>

Use `action :nothing` to set a command to only run if another resource
notifies it.

#### <a name="lwrps-rsc-attributes"></a> Attributes

<table>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Description</th>
      <th>Default Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>
        <b>Name attribute:</b> Name of the command to execute.
      </td>
      <td>name</td>
    </tr>
    <tr>
      <td>rbenv_version</td>
      <td>
        A version of Ruby being managed by rbenv.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>root_path</td>
      <td>
        The path prefix to rbenv installation, for example:
        <code>/opt/rbenv</code>.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>code</td>
      <td>
        Quoted script of code to execute.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>creates</td>
      <td>
        A file this command creates - if the file exists, the command will not
        be run.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>cwd</td>
      <td>
        Current working director to run the command from.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>environment</td>
      <td>
        A has of environment variables to set before running this command.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>group</td>
      <td>
        A group or group ID that we should change to before running this
        command.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>path</td>
      <td>
        An array of paths to use when searching for the command.
      </td>
      <td><code>nil</code>, uses system path</td>
    </tr>
    <tr>
      <td>returns</td>
      <td>
        The return value of the command (may be an array of accepted values) -
        this resource raises an exception if the return value(s) do not match.
      </td>
      <td><code>0</code></td>
    </tr>
    <tr>
      <td>timeout</td>
      <td>
        How many seconds to let the command run before timing out.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>user</td>
      <td>
        A users's isolated rbenv installation on which to apply an action. The
        default value of <code>nil</code> denotes a system-wide rbenv
        installation is being targeted. <b>Note:</b> if specified, the user
        must already exist.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>umask</td>
      <td>
        Umask for files created by the command.
      </td>
      <td><code>nil</code></td>
    </tr>
  </tbody>
</table>

#### <a name="lwrps-rsc-examples"></a> Examples

##### Run A Rake Task

    rbenv_script "migrate_rails_database" do
      rbenv_version "1.8.7-p352"
      user          "deploy"
      group         "deploy"
      cwd           "/srv/webapp/current"
      code          %{rake RAILS_ENV=production db:migrate}
    end

### <a name="lwrps-rbgem"></a> rbenv_gem

This resource is a close analog of the `gem_package` resource/provider which
is rbenv-aware. See the Opscode [package resource][package_resource] and
[gem package options][gem_package_options] pages for more details.

#### <a name="lwrps-rbgem-actions"></a> Actions

<table>
  <thead>
    <tr>
      <th>Action</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>install</td>
      <td>
        Install a gem - if version is provided, install that specific version.
      </td>
      <td>Yes</td>
    </tr>
    <tr>
      <td><upgrade/td>
      <td>
        Upgrade a gem - if version is provided, upgrade to that specific
        version.
      </td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>remove</td>
      <td>
        Remove a gem.
      </td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>purge</td>
      <td>
        Purge a gem.
      </td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>

#### <a name="lwrps-rbr-attributes"></a> Attributes

<table>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Description</th>
      <th>Default Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>package_name</td>
      <td>
        <b>Name attribute:</b> the name of the gem to install.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>rbenv_version</td>
      <td>
        A version of Ruby being managed by rbenv.
      </td>
      <td><code>"global"</code></td>
    </tr>
    <tr>
      <td>root_path</td>
      <td>
        The path prefix to rbenv installation, for example:
        <code>/opt/rbenv</code>.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>version</td>
      <td>
        The specific version of the gem to install/upgrade.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>options</td>
      <td>
        Add additional options to the underlying gem command.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>source</td>
      <td>
        Provide an additional source for gem providers (such as RubyGems).
        This can also include a file system path to a <code>.gem</code> file
        such as <code>/tmp/json-1.5.1.gem</code>.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>user</td>
      <td>
        A users's isolated rbenv installation on which to apply an action. The
        default value of <code>nil</code> denotes a system-wide rbenv
        installation is being targeted. <b>Note:</b> if specified, the user
        must already exist.
      </td>
      <td><code>nil</code></td>
    </tr>
  </tbody>
</table>

#### <a name="lwrps-rbgem-examples"></a> Examples

##### Install A Gem

    rbenv_gem "thor" do
      rbenv_version   "1.8.7-p352"
      action          :install
    end

    rbenv_gem "json" do
      rbenv_version   "1.8.7-p330"
    end

    rbenv_gem "nokogiri" do
      rbenv_version   "jruby-1.5.6"
      version         "1.5.0.beta.4"
      action          :install
    end

**Note:** the install action is default, so the second example is a more common
usage.

##### Install A Gem From A Local File

    rbenv_gem "json" do
      rbenv_version   "ree-1.8.7-2011.03"
      source          "/tmp/json-1.5.1.gem"
      version         "1.5.1"
    end

##### Keep A Gem Up To Date

    rbenv_gem "homesick" do
      action :upgrade
    end

**Note:** the global rbenv Ruby will be targeted if no `rbenv_version` attribute
is given.

##### Remove A Gem

    rbenv_gem "nokogiri" do
      rbenv_version   "jruby-1.5.6"
      version         "1.4.4.2"
      action          :remove
    end

### <a name="lwrps-rrh"></a> rbenv_rehash

This resource installs shims for all Ruby binaries known to rbenv, as per
the [rbenv rehash docs][rbenv_3_6].

#### <a name="lwrps-rrh-actions"></a> Actions

<table>
  <thead>
    <tr>
      <th>Action</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>run</td>
      <td>Run the script</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>nothing</td>
      <td>Do not run this command</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>

Use `action :nothing` to set a command to only run if another resource
notifies it.

#### <a name="lwrps-rrh-attributes"></a> Attributes

<table>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Description</th>
      <th>Default Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>
        <b>Name attribute:</b> Name of the command to execute.
      </td>
      <td>name</td>
    </tr>
    <tr>
      <td>user</td>
      <td>
        A users's isolated rbenv installation on which to apply an action. The
        default value of <code>nil</code> denotes a system-wide rbenv
        installation is being targeted. <b>Note:</b> if specified, the user
        must already exist.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>root_path</td>
      <td>
        The path prefix to rbenv installation, for example:
        <code>/opt/rbenv</code>.
      </td>
      <td><code>nil</code></td>
    </tr>
  </tbody>
</table>

#### <a name="lwrps-rrh-examples"></a> Examples

##### Rehash A System-Wide rbenv

    rbenv_rehash "Doing the rehash dance"

##### Rehash A User's rbenv

    rbenv_rehash "Rehashing tflowers' rbenv" do
      user  "tflowers"
    end

### <a name="lwrps-rbr"></a> rbenv_ruby

This resource uses the [ruby-build][ruby_build_site] framework to build and install
Ruby versions from definition files.

**Note:** this LWRP requires the [ruby\_build cookbook][ruby_build_cb] to be
in the run list to perform the builds.

#### <a name="lwrps-rbr-actions"></a> Actions

<table>
  <thead>
    <tr>
      <th>Action</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>install</td>
      <td>
        Build and install a Ruby from a definition file. See the ruby-build
        readme<sup>(1)</sup> for more details.
      </td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>reinstall</td>
      <td>
        Force a recompiliation of the Ruby from source. The :install action
        will skip a build if the target install directory already exists.
      </td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>

1. [ruby-build readme][rb_readme]

#### <a name="lwrps-rbr-attributes"></a> Attributes

<table>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Description</th>
      <th>Default Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>definition</td>
      <td>
        <b>Name attribute:</b> the name of a built-in definition<sup>(1)</sup>
        or the name of the ruby installed by a ruby-build defintion file<sup>(2)</sup>
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>definition_file</td>
      <td>
        The path to a ruby-build definition file.  
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>user</td>
      <td>
        A users's isolated rbenv installation on which to apply an action. The
        default value of <code>nil</code> denotes a system-wide rbenv
        installation is being targeted. <b>Note:</b> if specified, the user
        must already exist.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>root_path</td>
      <td>
        The path prefix to rbenv installation, for example:
        <code>/opt/rbenv</code>.
      </td>
      <td><code>nil</code></td>
    </tr>
  </tbody>
</table>

1. [built-in definition][rb_definitions]
2. the recipe checks for the existence of the naming attribute under the root_path, and if not found invokes ruby-build with the definition file as an argument

#### <a name="lwrps-rbr-examples"></a> Examples

##### Install Ruby From ruby-build

    rbenv_ruby "ree-1.8.7-2011.03" do
      action :install
    end

    rbenv_ruby "jruby-1.6.5"

**Note:** the install action is default, so the second example is a more common
usage.

##### Reinstall Ruby

    rbenv_ruby "ree-1.8.7-2011.03" do
      action :reinstall
    end

##### Install a custom ruby

    rbenv_ruby "2.0.0p116" do
      definition_file "/usr/local/rbenv/custom/2.0.0p116"
    end

## <a name="mac-system-note"></a> System-Wide Mac Installation Note

This cookbook takes advantage of managing profile fragments in an
`/etc/profile.d` directory, common on most Unix-flavored platforms.
Unfortunately, Mac OS X does not support this idiom out of the box,
so you may need to [modify][mac_profile_d] your user profile.

## <a name="development"></a> Development

* Source hosted at [GitHub][repo]
* Report issues/Questions/Feature requests on [GitHub Issues][issues]

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make.

## <a name="license"></a> License and Author

Author:: [Fletcher Nichol][fnichol] (<fnichol@nichol.ca>) [![endorse](http://api.coderwall.com/fnichol/endorsecount.png)](http://coderwall.com/fnichol)

Copyright 2011, Fletcher Nichol

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[berkshelf]:        http://berkshelf.com/
[chef_repo]:        https://github.com/opscode/chef-repo
[cheffile]:         https://github.com/applicationsonline/librarian/blob/master/lib/librarian/chef/templates/Cheffile
[gem_package_options]: http://docs.opscode.com/resource_gem_package.html#attributes
[kgc]:              https://github.com/websterclay/knife-github-cookbooks#readme
[librarian]:        https://github.com/applicationsonline/librarian#readme
[lwrp]:             http://docs.opscode.com/lwrp_custom.html
[mac_profile_d]:    http://hints.macworld.com/article.php?story=20011221192012445
[package_resource]: http://docs.opscode.com/resource_package.html
[rb_readme]:        https://github.com/sstephenson/ruby-build#readme
[rb_definitions]:   https://github.com/sstephenson/ruby-build/tree/master/share/ruby-build
[rbenv_site]:       https://github.com/sstephenson/rbenv
[rbenv_3_1]:        https://github.com/sstephenson/rbenv#section_3.1
[rbenv_3_3]:        https://github.com/sstephenson/rbenv#section_3.3
[rbenv_3_6]:        https://github.com/sstephenson/rbenv#section_3.6
[ruby_build_cb]:    http://community.opscode.com/cookbooks/ruby_build
[ruby_build_site]:  https://github.com/sstephenson/ruby-build
[script_resource]:  http://docs.opscode.com/resource_script.html

[fnichol]:      https://github.com/fnichol
[repo]:         https://github.com/fnichol/chef-rbenv
[issues]:       https://github.com/fnichol/chef-rbenv/issues
dmg Cookbook
============
Lightweight resource and provider to install OS X applications (.app) from dmg files.


Requirements
------------
### Platform
- Mac OS X


Resources/Providers
-------------------
### dmg_package

This resource will install a DMG "Package". It will retrieve the DMG from a remote URL, mount it using OS X's `hdid`, copy the application (.app directory) to the specified destination (/Applications), and detach the image using `hdiutil`. The dmg file will be stored in the `Chef::Config[:file_cache_path]`. If you want to install an application that has already been downloaded (not using the `source` parameter), copy it to the appropriate location. You can find out what directory this is with the following command on the node to run chef:

```bash
knife exec -E 'p Chef::Config[:file_cache_path]' -c /etc/chef/client.rb
```

Optionally, the LWRP can install an "mpkg" or "pkg" package using installer(8).

#### Actions
- :install - Installs the application.

#### Parameter attributes:
- `app` - This is the name of the application used by default for the /Volumes directory and the .app directory copied to /Applications.
- `source` - remote URL for the dmg to download if specified. Default is nil.
- `owner` - owner that should own the package installation.
- `destination` - directory to copy the .app into. Default is /Applications.
- `checksum` - sha256 checksum of the dmg to download. Default is nil.
- `type` - type of package, "app", "pkg" or "mpkg". Default is "app". When using "pkg" or "mpkg", the destination must be /Applications.
- `volumes_dir` - Directory under /Volumes where the dmg is mounted. Not all dmgs are mounted into a /Volumes location matching the name of the dmg. If not specified, this will use the name attribute.
- `package_id` - Package id registered with pkgutil when a pkg or mpkg is installed
- `dmg_name` - Specify the name of the dmg if it is not the same as `app`, or if the name has spaces.
- `dmg_passphrase` - Specify a passphrase to use to unencrypt the dmg while mounting.
- `accept_eula` - Specify whether to accept the EULA.  Certain dmgs require acceptance of EULA before mounting.  Can be true or false, defaults to false.

#### Examples
Install `/Applications/Tunnelblick.app` from the primary download site.

```ruby
dmg_package 'Tunnelblick' do
  source   'http://tunnelblick.googlecode.com/files/Tunnelblick_3.1.2.dmg'
  checksum 'a3fae60b6833175f32df20c90cd3a3603a'
  action   :install
end
```

Install Google Chrome. Uses the `dmg_name` because the application name has spaces. Installs in `/Applications/Google Chrome.app`.

```ruby
dmg_package 'Google Chrome' do
  dmg_name 'googlechrome'
  source   'https://dl-ssl.google.com/chrome/mac/stable/GGRM/googlechrome.dmg'
  checksum '7daa2dc5c46d9bfb14f1d7ff4b33884325e5e63e694810adc58f14795165c91a'
  action   :install
end
```

Install Dropbox. Uses `volumes_dir` because the mounted directory is different than the name of the application directory. Installs in `/Applications/Dropbox.app`.

```ruby
dmg_package 'Dropbox' do
  volumes_dir 'Dropbox Installer'
  source      'http://www.dropbox.com/download?plat=mac'
  checksum    'b4ea620ca22b0517b75753283ceb82326aca8bc3c86212fbf725de6446a96a13'
  action      :install
end
```

Install MacIrssi to `~/Applications` from the local file downloaded to the cache path into an Applications directory in the current user's home directory. Chef should run as a non-root user for this.

```ruby
directory "#{ENV['HOME']}/Applications"

dmg_package 'MacIrssi' do
  destination "#{ENV['HOME']}/Applications"
  action      :install
end
```

Install Virtualbox to `/Applications` from the .mpkg:

```ruby
dmg_package 'Virtualbox' do
  source 'http://dlc.sun.com.edgesuite.net/virtualbox/4.0.8/VirtualBox-4.0.8-71778-OSX.dmg'
  type   'mpkg'
end
```

Install pgAdmin to `/Applications` and automatically accept the EULA:

```ruby
dmg_package 'pgAdmin3' do
  source   'http://wwwmaster.postgresql.org/redir/198/h/pgadmin3/release/v1.12.3/osx/pgadmin3-1.12.3.dmg'
  checksum '9435f79d5b52d0febeddfad392adf82db9df159196f496c1ab139a6957242ce9'
  accept_eula true
end
```

Install Pivotal Tracker to `/Applications` using a password-protected dmg:

```ruby
dmg_package 'Pivotal Tracker' do
  volumes_dir    'tracker'
  source         'http://cheffiles.pivotallabs.com/fluid_tracker.dmg'
  dmg_passphrase 'xyz'
end
```

Install Silverlight, with idempotence check based on pkgutil:

```ruby
dmg_package 'Silerlight' do
  source     'http://silverlight.dlservice.microsoft.com/download/D/C/2/DC2D5838-9138-4D25-AA92-52F61F7C51E6/runtime/Silverlight.dmg'
  type       'pkg'
  checksum   '6d4a0ad4552d9815531463eb3f467fb8cf4bffcc'
  package_id 'com.microsoft.installSilverlightPlugin'
end
```


License & Authors
-----------------
- Author:: Joshua Timberman (joshua@opscode.com)

```text
Copyright 2011, Joshua Timberman <cookbooks@housepub.org>

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
[![Build Status](https://recipe-tester.com/repo/spulec/chef-npm/badge.png)](https://recipe-tester.com/repo/spulec/chef-npm/)


# Cookbook for Node Package Manager
http://community.opscode.com/cookbooks/npm

##DESCRIPTION:
This cookbook grown up from mdxp's nodejs::npm recipe
It provides some LWRP's for simple management of node packages

##REQUIREMENTS:
This cookbook depends on https://github.com/mdxp/cookbooks/tree/master/nodejs/

##ATTRIBUTES:
The only attribute default['npm']['version'] specifies a version of npm should be installed.

_NOTE:_ this cookbook will not work with npm <= 1.0.0

##USAGE:
Use recipe['npm'] to install npm it self. 
To install some packge system-wide use

    npm_package "foo@0.3.2"

or

    npm_package "foo" do
      version "0.3.2"
      action :install
    end 

To install some package under your project root try to:

    npm_package "foo" do
	  version "0.3.2"
	  path "/your/project/path/goes/here"
	  action :install_local
	end

or

	npm_package do
  	  path "/path/to/code"
  	  action :install_from_json
	end
	
To uninstall some package - obviously you can do something like

    npm_package "bad_one" do
	  version "0.3.2"
	  action :uninstall
	end
	
or

    npm_package "bad_local_one" do
	  version "0.3.2"
	  path "/your/project/path/goes/here"
	  action :uninstall_local
	end


## TODO
- wrap other features of npm to LWRP
Description
===========

Installs god gem, sets up modular configuration directory and provides
a defininition to monitor processes.

Requirements
============

Sample configuration file uses mongrel_runit for managing mongrels via
runit. Opscode does not have a `mongrel_runit` cookbook, however.

## Platform:

* Debian/Ubuntu


## Cookbooks:

* runit

Usage
=====

This recipe is designed to be used through the `god_monitor` define. Create a god configuration file in your application's cookbook and then call `god_monitor`:

    god_monitor "myproj" do
      config "myproj.god.erb"
    end

A sample mongrel.god.erb is provided, though it assumes `mongrel_runit` is used. This can be used as a baseline for customization.


License and Author
==================

Author:: Joshua Timberman (<joshua@opscode.com>)

Copyright:: 2009, Opscode, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# <a name="title"></a> nodejs-cookbook [![Build Status](https://secure.travis-ci.org/mdxp/nodejs-cookbook.png)](http://travis-ci.org/mdxp/nodejs-cookbook)

DESCRIPTION
===========

Installs Node.JS

REQUIREMENTS
============


## Platform

* Tested on Debian 6 and Ubuntu 10.04
* Should work fine on Centos, RHEL, etc.

## Cookbooks:

* build-essential
* apt

Opscode cookbooks (http://github.com/opscode/cookbooks/tree/master)

ATTRIBUTES
==========

* nodejs['install_method'] = source or package
* nodejs['version'] - release version of node to install
* nodejs['src_url'] - download location for node source tarball
* nodejs['dir'] - location where node will be installed, default /usr/local
* nodejs['npm'] - version of npm to install
* nodejs['npm_src_url'] - download location for npm source tarball
* nodejs['check_sha'] - test for valid sha_sum, default: true

USAGE
=====

Include the nodejs recipe to install node on your system based on the default installation method:

*  include_recipe "nodejs"

Include the install_from_source recipe to install node from sources:

*  include_recipe "nodejs::install_from_source"

Include the install_from_package recipe to install node from packages:
Note that only apt (Ubuntu, Debian) appears to have up to date packages available.
Centos, RHEL, etc are non-functional. (Try install_from_binary for those)

*  include_recipe "nodejs::install_from_package"

Include the install_from_binary recipe to install node from official prebuilt binaries:
(Currently Linux x86, x86_64, armv6l only)

*  include_recipe "nodejs::install_from_binary"

Include the npm recipe to install npm:

*  include_recipe "nodejs::npm"

LICENSE and AUTHOR
==================

Author:: Marius Ducea (marius@promethost.com)
Author:: Nathan L Smith (nlloyds@gmail.com)

Copyright:: 2010-2012, Promet Solutions
Copyright:: 2012, Cramer Development, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# <a name="title"></a> chef-ruby_build

[![Build Status](https://secure.travis-ci.org/fnichol/chef-ruby_build.png?branch=master)](http://travis-ci.org/fnichol/chef-ruby_build)

## <a name="description"></a> Description

Manages the [ruby-build][rb_site] framework and its installed Rubies.
A lightweight resources and providers ([LWRP][lwrp]) is also defined.

## <a name="usage"></a> Usage

Simply include `recipe[ruby_build]` in your run\_list to have ruby-build
installed. You will also have access to the `ruby_build_ruby` resource. See
the [Resources and Providers](#lwrps) section for more details.

## <a name="requirements"></a> Requirements

### <a name="requirements-chef"></a> Chef

Tested on 0.10.8 but newer and older version should work just
fine. File an [issue][issues] if this isn't the case.

### <a name="requirements-platform"></a> Platform

The following platforms have been tested with this cookbook, meaning that
the recipes and LWRPs run on these platforms without error:

* ubuntu (10.04/10.10/11.04/11.10/12.04)
* mac\_os\_x (10.7/10.8)
* debian
* freebsd
* redhat
* centos
* fedora
* amazon
* scientific
* suse

Please [report][issues] any additional platforms so they can be added.

### <a name="requirements-cookbooks"></a> Cookbooks

There are **no** external cookbook dependencies. However, if you are
installing [JRuby][jruby] then a Java runtime will need to be installed.
The Opscode [java cookbook][java_cb] can be used on supported platforms.

## <a name="installation"></a> Installation

Depending on the situation and use case there are several ways to install
this cookbook. All the methods listed below assume a tagged version release
is the target, but omit the tags to get the head of development. A valid
Chef repository structure like the [Opscode repo][chef_repo] is also assumed.

### <a name="installation-platform"></a> From the Opscode Community Platform

To install this cookbook from the Opscode platform, use the *knife* command:

    knife cookbook site install ruby_build

### <a name="installation-berkshelf"></a> Using Berkshelf

[Berkshelf][berkshelf] is a cookbook dependency manager and development
workflow assistant. To install Berkshelf:

    cd chef-repo
    gem install berkshelf
    berks init

To use the Community Site version:

    echo "cookbook 'ruby_build'" >> Berksfile
    berks install

Or to reference the Git version:

    repo="fnichol/chef-ruby_build"
    latest_release=$(curl -s https://api.github.com/repos/$repo/git/refs/tags \
    | ruby -rjson -e '
      j = JSON.parse(STDIN.read);
      puts j.map { |t| t["ref"].split("/").last }.sort.last
    ')
    cat >> Berksfile <<END_OF_BERKSFILE
    cookbook 'ruby_build',
      :git => 'git://github.com/$repo.git', :branch => '$latest_release'
    END_OF_BERKSFILE

### <a name="installation-librarian"></a> Using Librarian-Chef

[Librarian-Chef][librarian] is a bundler for your Chef cookbooks.
To install Librarian-Chef:

    cd chef-repo
    gem install librarian
    librarian-chef init

To use the Opscode platform version:

    echo "cookbook 'ruby_build'" >> Cheffile
    librarian-chef install

Or to reference the Git version:

    repo="fnichol/chef-ruby_build"
    latest_release=$(curl -s https://api.github.com/repos/$repo/git/refs/tags \
    | ruby -rjson -e '
      j = JSON.parse(STDIN.read);
      puts j.map { |t| t["ref"].split("/").last }.sort.last
    ')
    cat >> Cheffile <<END_OF_CHEFFILE
    cookbook 'ruby_build',
      :git => 'git://github.com/$repo.git', :ref => '$latest_release'
    END_OF_CHEFFILE
    librarian-chef install

## <a name="recipes"></a> Recipes

### <a name="recipes-default"></a> default

Installs the ruby-build codebase and initializes Chef to use the Lightweight
Resources and Providers ([LWRPs][lwrp]).

## <a name="attributes"></a> Attributes

### <a name="attributes-git-url"></a> git_url

The Git URL which is used to install ruby-build.

The default is `"git://github.com/sstephenson/ruby-build.git"`.

### <a name="attributes-git-ref"></a> git_ref

A specific Git branch/tag/reference to use when installing ruby-build. For
example, to pin ruby-build to a specific release:

    node['ruby_build']['git_ref'] = "v20111030"

The default is `"master"`.

### <a name="attributes-default-ruby-base-path"></a> default_ruby_base_path

The default base path for a system-wide installed Ruby. For example, the
following resource:

    ruby_build_ruby "1.9.3-p0"

will be installed into
`"#{node['ruby_build']['default_ruby_base_path']}/1.9.3-p0"` unless a
`prefix_path` attribute is explicitly set.

The default is `"/usr/local/ruby"`.

### <a name="attributes-upgrade"></a> upgrade

Determines how to handle installing updates to the ruby-build framework.
There are currently 2 valid values:

* `"none"`, `false`, or `nil`: will not update ruby-build and leave it in its
  current state.
* `"sync"` or `true`: updates ruby-build to the version specified by the
  `git_ref` attribute or the head of the master branch by default.

The default is `"none"`.

## <a name="lwrps"></a> Resources and Providers

### <a name="lwrps-rbr"></a> ruby_build_ruby

#### <a name="lwrps-rbr-actions"></a> Actions

<table>
  <thead>
    <tr>
      <th>Action</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>install</td>
      <td>
        Build and install a Ruby from a definition file. See the ruby-build
        readme<sup>(1)</sup> for more details.
      </td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>reinstall</td>
      <td>
        Force a recompiliation of the Ruby from source. The :install action
        will skip a build if the target install directory already exists.
      </td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>

1. [ruby-build readme][rb_readme]

#### <a name="lwrps-rbr-attributes"></a> Attributes

<table>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Description</th>
      <th>Default Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>definition</td>
      <td>
        <b>Name attribute:</b> the name of a built-in definition<sup>(1)</sup>
        or the path to a ruby-build definition file.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>prefix_path</td>
      <td>The path to which the Ruby will be installed.</td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>user</td>
      <td>
        A user which will own the installed Ruby. The default value of
        <code>nil</code> denotes a system-wide Ruby (root-owned) is being
        targeted. <b>Note:</b> if specified, the user must already exist.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>group</td>
      <td>
        A group which will own the installed Ruby. The default value of
        <code>nil</code> denotes a system-wide Ruby (root-owned) is being
        targeted. <b>Note:</b> if specified, the group must already exist.
      </td>
      <td><code>nil</code></td>
    </tr>
    <tr>
      <td>environment</td>
      <td>
        A Hash of additional environment variables<sup>(2)</sup>, such as
        <code>CONFIGURE_OPTS</code> or <code>RUBY_BUILD_MIRROR_URL</code>.
      </td>
      <td><code>nil</code></td>
    </tr>
  </tbody>
</table>

1. [built-in definition][rb_definitions]
2. [special environment variables][rb_environment]

#### <a name="lwrps-rbr-examples"></a> Examples

##### Install Ruby

    # See: https://github.com/sstephenson/ruby-build/issues/186
    ruby_build_ruby "ree-1.8.7-2012.02" do
      environment({ 'CONFIGURE_OPTS' => '--no-tcmalloc' })
    end

    ruby_build_ruby "1.9.3-p0" do
      prefix_path "/usr/local/ruby/ruby-1.9.3-p0"
      environment({
        'RUBY_BUILD_MIRROR_URL' => 'http://local.example.com'
      })

      action      :install
    end

    ruby_build_ruby "jruby-1.6.5"

**Note:** the install action is default, so the second example is more common.

##### Install A Ruby For A User

    ruby_build_ruby "maglev-1.0.0" do
      prefix_path "/home/deploy/.rubies/maglev-1.0.0"
      user        "deploy"
      group       "deploy"
    end

##### Reinstall Ruby

    ruby_build_ruby "rbx-1.2.4" do
      prefix_path "/opt/rbx-1.2.4"

      action      :reinstall
    end

**Note:** the Ruby will be built whether or not the Ruby exists in the
`prefix_path` directory.

## <a name="development"></a> Development

* Source hosted at [GitHub][repo]
* Report issues/Questions/Feature requests on [GitHub Issues][issues]

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make.

## <a name="license"></a> License and Author

Author:: [Fletcher Nichol][fnichol] (<fnichol@nichol.ca>) [![endorse](http://api.coderwall.com/fnichol/endorsecount.png)](http://coderwall.com/fnichol)

Copyright 2011, Fletcher Nichol

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[berkshelf]:      http://berkshelf.com/
[chef_repo]:      https://github.com/opscode/chef-repo
[cheffile]:       https://github.com/applicationsonline/librarian/blob/master/lib/librarian/chef/templates/Cheffile
[java_cb]:        http://community.opscode.com/cookbooks/java
[jruby]:          http://jruby.org/
[kgc]:            https://github.com/websterclay/knife-github-cookbooks#readme
[librarian]:      https://github.com/applicationsonline/librarian#readme
[lwrp]:           http://wiki.opscode.com/display/chef/Lightweight+Resources+and+Providers+%28LWRP%29
[rb_readme]:      https://github.com/sstephenson/ruby-build#readme
[rb_site]:        https://github.com/sstephenson/ruby-build
[rb_environment]: https://github.com/sstephenson/ruby-build#special-environment-variables
[rb_definitions]: https://github.com/sstephenson/ruby-build/tree/master/share/ruby-build

[fnichol]:      https://github.com/fnichol
[repo]:         https://github.com/fnichol/chef-ruby_build
[issues]:       https://github.com/fnichol/chef-ruby_build/issues
Description
===========

Creates a configured handler path for distributing [Chef report and exception handlers](http://wiki.opscode.com/display/chef/Exception+and+Report+Handlers).  Also exposes an LWRP for enabling Chef handlers from within recipe code (as opposed to hard coding in the client.rb file).  This is useful for cookbook authors who may want to ship a product specific handler (see the `cloudkick` cookbook for an example) with their cookbook.

Attributes
==========

`node["chef_handler"]["handler_path"]` - location to drop off handlers directory, default is `/var/chef/handlers`.

Resource/Provider
=================

`chef_handler`
--------------

Requires, configures and enables handlers on the node for the current Chef run.  Also has the ability to pass arguments to the handlers initializer.  This allows initialization data to be pulled from a node's attribute data.

It is best to declare `chef_handler` resources early on in the compile phase so they are available to fire for any exceptions during the Chef run.  If you have a base role you would want any recipes that register Chef handlers to come first in the run_list.

### Actions

- :enable: Enables the Chef handler for the current Chef run on the current node
- :disable: Disables the Chef handler for the current Chef run on the current node

### Attribute Parameters

- class_name: name attribute. The name of the handler class (can be module name-spaced).
- source: full path to the handler file.  can also be a gem path if the handler ships as part of a Ruby gem.
- arguments: an array of arguments to pass the handler's class initializer
- supports: type of Chef Handler to register as, ie :report, :exception or both. default is `:report => true, :exception => true`

### Example

    # register the Chef::Handler::JsonFile handler
    # that ships with the Chef gem
    chef_handler "Chef::Handler::JsonFile" do
      source "chef/handler/json_file"
      arguments :path => '/var/chef/reports'
      action :enable
    end

    # do the same but during the compile phase
    chef_handler "Chef::Handler::JsonFile" do
      source "chef/handler/json_file"
      arguments :path => '/var/chef/reports'
      action :nothing
    end.run_action(:enable)

    # handle exceptions only
    chef_handler "Chef::Handler::JsonFile" do
      source "chef/handler/json_file"
      arguments :path => '/var/chef/reports'
      supports :exception => true
      action :enable
    end


    # enable the CloudkickHandler which was
    # dropped off in the default handler path.
    # passes the oauth key/secret to the handler's
    # intializer.
    chef_handler "CloudkickHandler" do
      source "#{node['chef_handler']['handler_path']}/cloudkick_handler.rb"
      arguments [node['cloudkick']['oauth_key'], node['cloudkick']['oauth_secret']]
      action :enable
    end


Usage
=====

default
-------

Put the recipe `chef_handler` at the start of the node's run list to make sure that custom handlers are dropped off early on in the Chef run and available for later recipes.

For information on how to write report and exception handlers for Chef, please see the Chef wiki pages:
http://wiki.opscode.com/display/chef/Exception+and+Report+Handlers

json_file
---------

Leverages the `chef_handler` LWRP to automatically register the `Chef::Handler::JsonFile` handler that ships as part of Chef. This handler serializes the run status data to a JSON file located at `/var/chef/reports`.

License and Author
==================

Author:: Seth Chisamore (<schisamo@opscode.com>)

Copyright:: 2011, Opscode, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
This directory contains Chef handlers to distribute to your nodes.
# Dpkg Autostart

`dpkg` likes to start services after installation as the Debian convention
dictates. This can be annoying and problematic, especially when you don't
want services to be immediately started before custom configuration can
be applied. Instead of disabling all services from auto starting on installation
as the `dpkg_deb_unautostart` cookbook does, lets allow specifc services
to be targeted.

## Usage

### LWRP

Include the cookbook as a dependency in your metadata:

```ruby
depends 'dpkg_autostart'
```

Then, within your recipe, disable the service with the LWRP:

```ruby
dpkg_autostart 'mysql-server' do
  allow false
end
```

That's it. When `dpkg` attempts to start the service after install (generally
via `apt`) it will be instructed not to. This allows the proper configuration
files to be generated, and the service to be started after everything is
ready.

### Attribute

You can also provide a list of services to disable via node attribute. Add
the default recipe to the run list:

```ruby
run_list 'recipe[dpkg_autostart]'
```

and set the services you want to restrict from auto starting:

```ruby
node[:dpkg_autostart][:disabled_services] = ['mysql-server', 'apache2']
```

# Info
* Repository: https://github.com/hw-cookbooks/dpkg_autostart
* IRC: Freenode @ #heavywater

## Related
* deb_pkg_unautostart: http://ckbk.it/deb_pkg_unautostart# LXC

Manage linux containers with Chef.

## Recipes

### default

Installs the packages and configuration files needed for lxc on the server. If
the node uses apt-cacher-ng as a client, the server will be reused when building
containers.

### install_dependencies

Installs the packages needed to support lxc's containers.

### containers

This recipe creates all of the containers defined in the `['lxc']['containers']`
hash. Here is an example of an `example` container:

```ruby
node['lxc']['containers']['example'] = { 
  'template' => 'ubuntu',
  'initialize_commands' => ['apt-get update']
}
```

### knife

Install and manage containers via the knife-remotelxc plugin.

## LWRPs

### lxc

Allows for creation, deletion, and cloning of containers

### lxc_config

Allows configuration of the LXC configuration file

### lxc_fstab

Allows defining mounts to be used within the container

### lxc_interface

Allows configurations of network interfaces within a container

### lxc_ephemeral

Run a command within an ephemeral container

### lxc_container

Creates a container using the `lxc` LWRP and configures the container
as requested. This resource also allows nesting `lxc_fstab` and
`lxc_interface` within the container resource.

## Example

```ruby
include_recipe 'lxc'

lxc_container 'my_container' do
  action :create
  validation_client 'my-validator'
  server_uri 'https://api.opscode.com/organizations/myorg'
  validator_pem content_from_encrypted_dbag
  run_list ['role[base]']
  chef_enabled true
  fstab_mount "Persist" do
    file_system '/opt/file_store'
    mount_point '/opt/file_store'
    type 'none'
    options 'bind,rw'
  end
end

lxc_container 'my_container_clone' do
  action :create
  clone 'my_container'
  chef_enabled true
end

lxc_service 'my_container_clone' do
  action :start
end
```

Containers do not have to be Chef enabled but it does make them
extremely easy to configure. If you want the Omnibus installer
cached, you can set the attribute

```ruby
node['omnibus_updater']['cache_omnibus_installer'] = true
```

in a role or environment (default is false). The `lxc_container`
resource also provides `initialize_commands` which an array of
commands can be provided that will be run after the container is
created.

### Repository:

* https://github.com/hw-cookbooks/lxc

### Contributors

* Sean Porter (https://github.com/portertech)
* Matt Ray (https://github.com/mattray)
Description
===========

Installs packages required for compiling C software from source. Use
this cookbook if you wish to compile C programs, or install RubyGems
with native extensions.

Requirements
============

Chef version 0.10.10+ and Ohai 0.6.12+ are required.

## Platform

Supported platforms by platform family:

* debian (debian, ubuntu)
* fedora
* mac_os_x (10.6+)
* rhel (centos, redhat, amazon, scientific)
* smartos
* solaris2
* omnios

**Note for OmniOS**: Currently, OmniOS's Ruby package is built with
GCC 4.6.3, and the path is hardcoded, as the gcc binaries are not
installed in the default $PATH. This means that in order to install
RubyGems into the "system" Ruby, one must install `developer/gcc46`.
[An issue](https://github.com/omniti-labs/omnios-build/issues/19) is
open upstream w/ OmniOS to rebuild the Ruby package with GCC 4.7.2.

## Cookbooks

This cookbook suggests the following external cookbooks:

* [pkgin](http://community.opscode.com/cookbooks/pkgin) (someara) - SmartOS only
* [pkgutil](http://community.opscode.com/cookbooks/pkgutil) (marthag) - Solaris 2 only

Attributes
==========

* `node['build_essential']['compiletime']` - Whether the resources in
the default recipe should be configured at the "Compile" phase of the
Chef run. Defaults to false, see __Usage__ for more information.
* `node['build_essential']['osx']['gcc_installer_url']` - The URL of
  the OS X GCC package installer (.pkg).
* `node['build_essential']['osx']['gcc_installer_checksum']` - The
  SHA256 checksum of the OS X GCC installer.

Recipes
=======

The main entrypoint for this cookbook is the `default` recipe. This
recipe includes a platform specific recipe based on the node's platform
family.

On Linux platforms (see __Platform__ above for a supported list of
families), packages required to build C source projects are installed.
This includes GCC, make, autconf and others. On Debian-family
distributions, the apt-cache may need to be updated, especially during
compile time installation. See __Usage__ for further information.

On Mac OS X, the GCC standalone installer by Kenneth Reitz is
installed. Note that this is *not* the Xcode CLI package, as that does
not include all programs and headers required to build some common
GNU-style C projects, such as those that are available from projects
such as MacPorts or Homebrew. Changing the attributes for the GCC
installer URL and checksum to the Xcode values may work, but this is
untested.

Usage
=====

Simply include the `build-essential` and the required tools will be
installed to the system, and later recipes will be able to compile
software from C source code.

For RubyGems that include native C extensions you wish to use with
Chef, you should do two things.

0. Ensure that the C libraries, include files and other assorted "dev"
type packages are installed. You should do this in the compile phase
after the build-essential recipe.
1. Use the `chef_gem` resource in your recipes. This requires Chef version 0.10.10+.
2. Set the `compiletime` attribute in roles where such recipes are
required. This will ensure that the build tools are available to
compile the RubyGems' extensions, as `chef_gem` happens during the
compile phase, too.

Example installation of a devel package at compile-time in a recipe:

    package "mypackage-dev" do
      action :nothing
    end.run_action(:install)

Example use of `chef_gem`:

    chef_gem "mygem"

Example role:

    name "myapp"
    run_list(
      "recipe[build-essential]",
      "recipe[myapp]"
    )
    default_attributes(
      "build_essential" => {
        "compiletime" => true
      }
    )

The compile time option (via the attribute) is to ensure that the
proper packages are available at the right time in the Chef run. It is
recommended that the build-essential recipe appear early in the run
list.

The Chef wiki has documentation on
[the anatomy of a chef run](http://wiki.opscode.com/display/chef/Anatomy+of+a+Chef+Run).

Limitations
===========

It is not in the scope of this cookbook to handle installing the
required headers for individual software projects in order to compile
them, or to compile RubyGems with native C extensions. You should
create a cookbook for handling that.

License and Author
==================

Author:: Joshua Timberman (<joshua@opscode.com>)
Author:: Seth Chisamore (<schisamo@opscode.com>)

Copyright 2009-2011, Opscode, Inc. (<legal@opscode.com>)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
php Cookbook
============
Installs and configures PHP 5.3 and the PEAR package management system.  Also includes LWRPs for managing PEAR (and PECL) packages along with PECL channels.

Requirements
------------
### Platforms
- Debian, Ubuntu
- CentOS, Red Hat, Fedora, Amazon Linux
- Microsoft Windows

### Cookbooks
- build-essential
- xml
- mysql

These cookbooks are only used when building PHP from source.


Attributes
----------
- `node['php']['install_method']` = method to install php with, default `package`.
- `node['php']['directives']` = Hash of directives and values to append to `php.ini`, default `{}`.

The file also contains the following attribute types:

* platform specific locations and settings.
* source installation settings


Resource/Provider
-----------------
This cookbook includes LWRPs for managing:

- PEAR channels
- PEAR/PECL packages

### `php_pear_channel`
[PEAR Channels](http://pear.php.net/manual/en/guide.users.commandline.channels.php) are alternative sources for PEAR packages.  This LWRP provides and easy way to manage these channels.

#### Actions
- :discover: Initialize a channel from its server.
- :add: Add a channel to the channel list, usually only used to add private channels.  Public channels are usually added using the `:discover` action
- :update: Update an existing channel
- :remove: Remove a channel from the List

#### Attribute Parameters
- channel_name: name attribute. The name of the channel to discover
- channel_xml: the channel.xml file of the channel you are adding

#### Examples
```ruby
# discover the horde channel
php_pear_channel "pear.horde.org" do
  action :discover
end

# download xml then add the symfony channel
remote_file "#{Chef::Config[:file_cache_path]}/symfony-channel.xml" do
  source "http://pear.symfony-project.com/channel.xml"
  mode 0644
end
php_pear_channel "symfony" do
  channel_xml "#{Chef::Config[:file_cache_path]}/symfony-channel.xml"
  action :add
end

# update the main pear channel
php_pear_channel 'pear.php.net' do
  action :update
end

# update the main pecl channel
php_pear_channel 'pecl.php.net' do
  action :update
end
```

### `php_pear`
[PEAR](http://pear.php.net/) is a framework and distribution system for reusable PHP components. [PECL](http://pecl.php.net/) is a repository for PHP Extensions. PECL contains C extensions for compiling into PHP. As C programs, PECL extensions run more efficiently than PEAR packages. PEARs and PECLs use the same packaging and distribution system.  As such this LWRP is clever enough to abstract away the small differences and can be used for managing either.  This LWRP also creates the proper module .ini file for each PECL extension at the correct location for each supported platform.

#### Actions
- :install: Install a pear package - if version is provided, install that specific version
- :upgrade: Upgrade a pear package - if version is provided, upgrade to that specific version
- :remove: Remove a pear package
- :purge: Purge a pear package (this usually entails removing configuration files as well as the package itself).  With pear packages this behaves the same as `:remove`

#### Attribute Parameters
- package_name: name attribute. The name of the pear package to install
- version: the version of the pear package to install/upgrade.  If no version is given latest is assumed.
- preferred_state: PEAR by default installs stable packages only, this allows you to install pear packages in a devel, alpha or beta state
- directives: extra extension directives (settings) for a pecl. on most platforms these usually get rendered into the extension's .ini file
- zend_extensions: extension filenames which should be loaded with zend_extension.
- options: Add additional options to the underlying pear package command

#### Examples
```ruby
# upgrade a pear
php_pear "XML_RPC" do
  action :upgrade
end


# install a specific version
php_pear "XML_RPC" do
  version "1.5.4"
  action :install
end


# install the mongodb pecl
php_pear "mongo" do
  action :install
end

# install the xdebug pecl
php_pear "xdebug" do
  # Specify that xdebug.so must be loaded as a zend extension
  zend_extensions ['xdebug.so']
  action :install
end


# install apc pecl with directives
php_pear "apc" do
  action :install
  directives(:shm_size => 128, :enable_cli => 1)
end


# install the beta version of Horde_Url
# from the horde channel
hc = php_pear_channel "pear.horde.org" do
  action :discover
end
php_pear "Horde_Url" do
  preferred_state "beta"
  channel hc.channel_name
  action :install
end


# install the YAML pear from the symfony project
sc = php_pear_channel "pear.symfony-project.com" do
  action :discover
end
php_pear "YAML" do
  channel sc.channel_name
  action :install
end
```


Recipes
-------
### default
Include the default recipe in a run list, to get `php`.  By default `php` is installed from packages but this can be changed by using the `install_method` attribute.

### package
This recipe installs PHP from packages.

### source
This recipe installs PHP from source.


Deprecated Recipes
------------------
The following recipes are deprecated and will be removed from a future version of this cookbook.

- `module_apc`
- `module_curl`
- `module_fileinfo`
- `module_fpdf`
- `module_gd`
- `module_ldap`
- `module_memcache`
- `module_mysql`
- `module_pgsql`
- `module_sqlite3`

The installation of the php modules in these recipes can now be accomplished by installing from a native package or via the new php_pear LWRP.  For example, the functionality of the `module_memcache` recipe can be enabled in the following ways:

```ruby
# using apt
package "php5-memcache" do
  action :install
end

# using pear LWRP
php_pear "memcache" do
  action :install
end
```


Usage
-----
Simply include the `php` recipe where ever you would like php installed.  To install from source override the `node['php']['install_method']` attribute with in a role:

```ruby
name "php"
description "Install php from source"
override_attributes(
  "php" => {
    "install_method" => "source"
  }
)
run_list(
  "recipe[php]"
)
```


Development
-----------
This section details "quick development" steps. For a detailed explanation, see [[Contributing.md]].

1. Clone this repository from GitHub:

        $ git clone git@github.com:opscode-cookbooks/php.git

2. Create a git branch

        $ git checkout -b my_bug_fix

3. Install dependencies:

        $ bundle install

4. Make your changes/patches/fixes, committing appropiately
5. **Write tests**
6. Run the tests:
    - `bundle exec foodcritic -f any .`
    - `bundle exec rspec`
    - `bundle exec rubocop`
    - `bundle exec kitchen test`

  In detail:
    - Foodcritic will catch any Chef-specific style errors
    - RSpec will run the unit tests
    - Rubocop will check for Ruby-specific style errors
    - Test Kitchen will run and converge the recipes


License & Authors
-----------------
- Author:: Seth Chisamore (<schisamo@opscode.com>)
- Author:: Joshua Timberman (<joshua@opscode.com>)
- Author:: Julian C. Dunn (<jdunn@getchef.com>)

```text
Copyright:: 2013, Chef Software, Inc.

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

Note: This cookbook contains a modified copy of `go-phar.pear` for use on the
Microsoft Windows platform only to correct an (upstream bug)[http://pear.php.net/bugs/bug.php?id=16644]. The original
`go-pear.phar` is licensed under the (PHP License version 2.02)[http://www.php.net/license/2_02.txt]:

```
-------------------------------------------------------------------- 
                  The PHP License, version 2.02
Copyright (c) 1999 - 2002 The PHP Group. All rights reserved.
-------------------------------------------------------------------- 

Redistribution and use in source and binary forms, with or without
modification, is permitted provided that the following conditions
are met:

  1. Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer. 
 
  2. Redistributions in binary form must reproduce the above 
     copyright notice, this list of conditions and the following 
     disclaimer in the documentation and/or other materials provided
     with the distribution.
 
  3. The name "PHP" must not be used to endorse or promote products 
     derived from this software without prior permission from the 
     PHP Group.  This does not apply to add-on libraries or tools
     that work in conjunction with PHP.  In such a case the PHP
     name may be used to indicate that the product supports PHP.
 
  4. The PHP Group may publish revised and/or new versions of the
     license from time to time. Each version will be given a
     distinguishing version number.
     Once covered code has been published under a particular version
     of the license, you may always continue to use it under the
     terms of that version. You may also choose to use such covered
     code under the terms of any subsequent version of the license
     published by the PHP Group. No one other than the PHP Group has
     the right to modify the terms applicable to covered code created
     under this License.

  5. Redistributions of any form whatsoever must retain the following
     acknowledgment:
     "This product includes PHP, freely available from
     http://www.php.net/".

  6. The software incorporates the Zend Engine, a product of Zend
     Technologies, Ltd. ("Zend"). The Zend Engine is licensed to the
     PHP Association (pursuant to a grant from Zend that can be
     found at http://www.php.net/license/ZendGrant/) for
     distribution to you under this license agreement, only as a
     part of PHP.  In the event that you separate the Zend Engine
     (or any portion thereof) from the rest of the software, or
     modify the Zend Engine, or any portion thereof, your use of the
     separated or modified Zend Engine software shall not be governed
     by this license, and instead shall be governed by the license
     set forth at http://www.zend.com/license/ZendLicense/. 



THIS SOFTWARE IS PROVIDED BY THE PHP DEVELOPMENT TEAM ``AS IS'' AND 
ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE PHP
DEVELOPMENT TEAM OR ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------------------------- 

This software consists of voluntary contributions made by many
individuals on behalf of the PHP Group.

The PHP Group can be contacted via Email at group@php.net.

For more information on the PHP Group and the PHP project, 
please see <http://www.php.net>.
```
# chef-docker [![Build Status](https://secure.travis-ci.org/bflad/chef-docker.png?branch=master)](http://travis-ci.org/bflad/chef-docker)

## Description

Installs/Configures [Docker](http://docker.io). Please see [COMPATIBILITY.md](COMPATIBILITY.md) for more information about Docker versions that are tested and supported by cookbook versions along with LWRP features.

This cookbook was inspired by @thoward's docker-cookbook: https://github.com/thoward/docker-cookbook

## Requirements

### Platforms

* Ubuntu 12.04
* Ubuntu 12.10
* Ubuntu 13.04

### Cookbooks

[Opscode Cookbooks](https://github.com/opscode-cookbooks/)

* [apt](https://github.com/opscode-cookbooks/apt)
* [git](https://github.com/opscode-cookbooks/git)

Third-Party Cookbooks

* [golang](https://github.com/NOX73/chef-golang)
* [lxc](https://github.com/hw-cookbooks/lxc)
* [modules](https://github.com/Youscribe/modules-cookbook)

## Attributes

These attributes are under the `node['docker']` namespace.

Attribute | Description | Type | Default
----------|-------------|------|--------
arch | Architecture for docker binary (note: Docker only currently supports x86_64) | String | auto-detected (see attributes/default.rb)
bind_socket | Socket path that docker should bind | String | unix:///var/run/docker.sock
bind_uri | TCP URI docker should bind | String | nil
http_proxy | HTTP_PROXY environment variable | String | nil
install_dir | Installation directory for docker binary | String | auto-detected (see attributes/default.rb)
install_type | Installation type for docker ("binary", "package" or "source") | String | "package"
options | Additional options to pass to docker. These could be flags like "-api-enable-cors". | String | nil

### Binary Attributes

These attributes are under the `node['docker']['binary']` namespace.

Attribute | Description | Type | Default
----------|-------------|------|--------
version | Version of docker binary | String | latest
url | URL for downloading docker binary | String | auto-detected (see attributes/default.rb)

### Package Attributes

These attributes are under the `node['docker']['package']` namespace.

Attribute | Description | Type | Default
----------|-------------|------|--------
distribution | Distribution for docker packages | String | auto-detected (see attributes/default.rb)
repo_url | Repository URL for docker packages | String | auto-detected (see attributes/default.rb)

### Source Attributes

These attributes are under the `node['docker']['source']` namespace.

Attribute | Description | Type | Default
----------|-------------|------|--------
ref | Repository reference for docker source | String | "master"
url | Repository URL for docker source | String | "https://github.com/dotcloud/docker.git"

## Recipes

* `recipe[docker]` Installs/Configures Docker
* `recipe[docker::aufs]` Installs/Loads AUFS Linux module
* `recipe[docker::binary]` Installs Docker binary
* `recipe[docker::package]` Installs Docker via package
* `recipe[docker::source]` Installs Docker via source
* `recipe[docker::upstart]` Installs/Starts Docker via Upstart

## LWRPs

### docker_container

Run a container:

    docker_container "busybox" do
      command "sleep 9999"
      detach true
    end

Stop a running container:

    docker_container "busybox" do
      command "sleep 9999"
      action :stop
    end

Start a stopped container:

    docker_container "busybox" do
      command "sleep 9999"
      action :start
    end

Restart a container:

    docker_container "busybox" do
      command "sleep 9999"
      action :restart
    end

Remove a container:

    docker_container "busybox" do
      command "sleep 9999"
      action :remove
    end

### docker_image

Build image from Dockerfile:

    docker_image "myImage" do
      tag "myTag"
      dockerfile myImageDockerfile
      action :build
    end

Build image from remote repository:

    docker_image "myImage" do
      image_url "example.com/foo/myImage"
      tag "myTag"
      action :build
    end

Pull latest image:

    docker_image "busybox"

Pull tagged image:

    docker_image "bflad/test" do
      tag "not-latest"
    end

Import image from URL:

    docker_image "test" do
      image_url "https://example.com/testimage.tgz"
      action :import
    end

Import image from URL with repository/tag information:

    docker_image "test" do
      repository "bflad/test"
      tag "not-latest"
      action :import
    end

Remove image:

    docker_image "busybox" do
      action :remove
    end

## Usage

### Default Installation

* Add `recipe[docker]` to your node's run list

## Testing and Development

### Vagrant

Here's how you can quickly get testing or developing against the cookbook thanks to [Vagrant](http://vagrantup.com/) and [Berkshelf](http://berkshelf.com/).

    vagrant plugin install vagrant-berkshelf
    vagrant plugin install vagrant-cachier
    vagrant plugin install vagrant-omnibus
    git clone git://github.com/bflad/chef-docker.git
    cd chef-docker
    vagrant up BOX # BOX being centos6, debian7, fedora18, fedora19, ubuntu1204, ubuntu1210, or ubuntu1304

You can then SSH into the running VM using the `vagrant ssh BOX` command.

The VM can easily be stopped and deleted with the `vagrant destroy` command. Please see the official [Vagrant documentation](http://docs.vagrantup.com/v2/cli/index.html) for a more in depth explanation of available commands.

### Test Kitchen

Please see documentation in: [TESTING.md](TESTING.md)

## Contributing

Please use standard Github issues/pull requests and if possible, in combination with testing on the Vagrant boxes or Test Kitchen suite.

## Maintainers

* Brian Flad (<bflad417@gmail.com>)

## License

Please see licensing information in: [LICENSE](LICENSE)
docker_test Cookbook
===================

This cookbook defines acceptance tests for Docker.

Requirements
------------

## Cookbooks:

* docker

## Platforms:

* Ubuntu 12.04

Attributes
----------

See attributes set by this cookbook in attributes/default.rb

Recipes
-------

* `default` - includes `docker::default`

Contributing
------------
TODO: (optional) If this is a public cookbook, detail the process for contributing. If this is a private cookbook, remove this section.

e.g.
1. Fork the repository on Github
2. Create a named feature branch (like `add_component_x`)
3. Write you change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

License and Authors
-------------------

Author:: Brian Flad <bflad417@gmail.com>

    Copyright:: 2013
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
Description
====

Provide a library method to generate secure random passwords in recipes.

Requirements
====

Works on any platform with OpenSSL Ruby bindings installed, which are a requirement for Chef anyway.

Usage
====

Most often this will be used to generate a secure password for an attribute.

    include Opscode::OpenSSL::Password

    set_unless[:my_password] = secure_password

License and Author
====

Author:: Joshua Timberman (<joshua@opscode.com>)

Copyright:: 2009-2011, Opscode, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
Description
===========

Installs runit and provides the `runit_service` service resource for
managing processes (services) under runit.

This cookbook does not use runit to replace system init, nor are there
plans to do so.

For more information about runit:

* http://smarden.org/runit/

About Runit
===========

In brief, Runit is a process supervision suite. It is simple to set
up, and doesn't require complex shell scripts to be written to start
processes running as system services.

To manage a process in runit, create a "service" directory that
contains a "`run`" script. In this cookbook we refer to that directory
as the `sv_dir` (see __Attributes__ and __Resource/Provider__). That
service directory is symbolically linked into runit's own service
directory where its `runsvdir` program looks for processes to manage.
See the [runit documentation](http://smarden.org/runit/) for detailed
information on runit.

Supervised processes are analogous to services under other systems
such as sysvinit or upstart.

Requirements
============

## Platform:

* Debian/Ubuntu
* Gentoo
* RHEL

Attributes
==========

See `attributes/default.rb` for defaults generated per platform.

* `node['runit']['sv_bin']` - Full path to the `sv` binary.
* `node['runit']['chpst_bin']` - Full path to the `chpst` binary.
* `node['runit']['service_dir']` - Full path to the default "services"
  directory where enabled services are linked.
* `node['runit']['sv_dir']` - Full path to the directory where
  service lives, which gets linked to `service_dir`.
* `node['runit']['lsb_init_dir']` - Full path to the directory where
  the LSB-compliant init script interface will be created.
* `node['runit']['start']` - Command to start the runsvdir service
* `node['runit']['stop]` - Command to stop the runsvdir service
* `node['runit']['reload']` - Command to reload the runsvdir service

### Optional Attributes for RHEL systems

* `node['runit']['use_package_from_yum']` - If `true`, attempts to install
  runit without building an RPM first. This is for users who already have
  the package in their own Yum repository.

Recipes
=======

default
-------

The default recipe installs runit and starts `runsvdir` to supervise
the services in runit's service directory (e.g., `/etc/service`).

On RHEL family systems, it will build the runit RPM using [Ian Meyer's
runit RPM SPEC](https://github.com/imeyer/runit-rpm) unless the
attribute `node['runit']['use_package_from_yum']` is set to `true`. In
which case it will try and install runit through the normal package
installation mechanism.

On Debian family systems, the runit packages are maintained by the
runit author, Gerrit Pape, and the recipe will use that for
installation.

On Gentoo, the runit ebuild package is installed.

Resource/Provider
=================

This cookbook has a resource, `runit_service`, for managing services
under runit. This service subclasses the Chef `service` resource.

**This resource replaces the runit_service definition. See the
CHANGELOG.md file in this cookbook for breaking change information
and any actions you may need to take to update cookbooks using
runit_service.**

## Actions:

- **enable** - enables the service, creating the required run scripts
   and symlinks. This is the default action.
- **start** - starts the service with `sv start`
- **stop** - stops the service with `sv stop`
- **disable** - stops the service with `sv down` and removes the service symlink
- **restart** - restarts the service with `sv restart`
- **reload** - reloads the service with `sv force-reload`
- **once** - starts the service with `sv once`.
- **hup** - sends the `HUP` signal to the service with `sv hup`
- **cont** - sends the `CONT` signal to the service
- **term** - sends the `TERM` signal to the service
- **kill** - sends the `KILL` signal to the service
- **up** - starts the service with `sv up`
- **down** - downs the service with `sv down`
- **usr1** - sends the `USR1` signal to the service with `sv 1`
- **usr2** - sends the `USR2` signal to the service with `sv 2`

Service management actions are taken with runit's "`sv`" program.

Read the `sv(8)` [man page](http://smarden.org/runit/sv.8.html) for
more information on the `sv` program.

## Parameter Attributes

The first three parameters, `sv_dir`, `service_dir`, and `sv_bin` will
attempt to use the corresponding node attributes, and fall back to
hardcoded default values that match the settings used on Debian
platform systems.

Many of these parameters are only used in the `:enable` action.

- **sv_dir** - The base "service directory" for the services managed by
   the resource. By default, this will attempt to use the
   `node['runit']['sv_dir']` attribute, and falls back to `/etc/sv`.
- **service_dir** - The directory where services are symlinked to be
   supervised by `runsvdir`. By default, this will attempt to use the
   `node['runit']['service_dir']` attribute, and falls back to
   `/etc/service`.
- **lsb_init_dir** - The directory where an LSB-compliant init script
   interface will be created. By default, this will attempt to use the
   `node['runit']['lsb_init_dir']` attribute, and falls back to
   `/etc/init.d`.
- **sv_bin** - The path to the `sv` program binary. This will attempt
    to use the `node['runit']['sv_bin']` attribute, and falls back to
    `/usr/bin/sv`.
- **service_name** - *Name attribute*. The name of the service. This
   will be used in the directory of the managed service in the
   `sv_dir` and `service_dir`.
- **sv_templates** - If true, the `:enable` action will create the
    service directory with the appropriate templates. Default is
    `true`. Set this to `false` if the service has a package that
    provides its own service directory. See __Usage__ examples.
- **options** - Options passed as variables to templates, for
   compatibility with legacy runit service definition. Default is an
   empty hash.
- **env** - A hash of environment variables with their values as content
   used in the service's `env` directory. Default is an empty hash.
- **log** - Whether to start the service's logger with svlogd, requires
   a template `sv-service_name-log-run.erb` to configure the log's run
   script. Default is true.
- **default_logger** - Whether a default `log/run` script should be set
   up. If true, the default content of the run script will use
   `svlogd` to write logs to `/var/log/service_name`. Default is false.
- **log_size** - The maximum size a log file can grow to before it is
  automatically rotated.  See svlogd(8) for the default value.
- **log_num** - The maximum number of log files that will be retained
  after rotation.  See svlogd(8) for the default value.
- **log_min** - The minimum number of log files that will be retained
  after rotation (if svlogd cannot create a new file and the minimum
  has not been reached, it will block).  Default is no minimum.
- **log_timeout** - The maximum age a log file can get to before it is
  automatically rotated, whether it has reached `log_size` or not.
  Default is no timeout.
- **log_processor** - A string containing a path to a program that
  rotated log files will be fed through.  See the **PROCESSOR** section
  of svlogd(8) for details.  Default is no processor.
- **log_socket** - An string containing an IP:port pair identifying a UDP
   socket that log lines will be copied to.  Default is none.
- **log_prefix** - A string that will be prepended to each line as it
  is logged.  Default is no prefix.
- **log_config_append** - A string containing optional additional lines to add
  to the log service configuration.  See svlogd(8) for more details.
- **cookbook** - A cookbook where templates are located instead of
   where the resource is used. Applies for all the templates in the
   `enable` action.
- **finish** - whether the service has a finish script, requires a
   template `sv-service_name-finish.erb`
- **control** - An array of signals to customize control of the service,
   see [runsv man page](http://smarden.org/runit/runsv.8.html) on how
   to use this. This requires that each template be created with the
   name `sv-service_name-signal.erb`.
- **owner** - user that should own the templates created to enable the
   service
- **group** - group that should own the templates created to enable the
   service
- **run_template_name** - alternate filename of the run run script to
   use replacing `service_name`.
- **log_template_name** - alternate filename of the log run script to
   use replacing `service_name`.
- **finish_script_template_name** - alternate filename of the finish
   script to use, replacing `service_name`.
- **control_template_names** - a hash of control signals (see *control*
   above) and their alternate template name(s) replacing
   `service_name`.
- **status_command** - The command used to check the status of the
   service to see if it is enabled/running (if it's running, it's
   enabled). This hardcodes the location of the sv program to
   `/usr/bin/sv` due to the aforementioned cookbook load order.
- **restart_on_update** - Whether the service should be restarted when
    the run script is updated. Defaults to `true`. Set to `false` if
    the service shouldn't be restarted when the run script is updated.

Unlike previous versions of the cookbook using the `runit_service`
definition, the `runit_service` resource can be notified. See
__Usage__ examples below.

Usage
=====

To get runit installed on supported platforms, use `recipe[runit]`.
Once it is installed, use the `runit_service` resource to set up
services to be managed by runit.

In order to use the `runit_service` resource in your cookbook(s), each
service managed will also need to have `sv-service_name-run.erb` and
`sv-service_name-log-run.erb` templates created. If the `log`
parameter is false, the log run script isn't created. If the `log`
parameter is true, and `default_logger` is also true, the log run
script will be created with the default content:

    #!/bin/sh
    exec svlogd -tt /var/log/service_name

Examples
--------

These are example use cases of the `runit_service` resource described
above. There are others in the `runit_test` cookbook that is included
in the [git repository](https://github.com/opscode-cookbooks/runit).

**Default Example**

This example uses all the defaults in the `:enable` action to set up
the service.

We'll set up `chef-client` to run as a service under runit, such as is
done in the `chef-client` cookbook. This example will be more simple
than in that cookbook. First, create the required run template,
`chef-client/templates/default/sv-chef-client-run.erb`.

    #!/bin/sh
    exec 2>&1
    exec /usr/bin/env chef-client -i 1800 -s 30

Then create the required log/run template,
`chef-client/templates/default/sv-chef-client-log-run.erb`.

    #!/bin/sh
    exec svlogd -tt ./main

__Note__ This will cause output of the running process to go to
`/etc/sv/chef-client/log/main/current`. Some people may not like this,
see the following example. This is preserved for compatibility reasons.

Finally, set up the service in the recipe with:

    runit_service "chef-client"

**Default Logger Example**

To use a default logger with svlogd which will log to
`/var/log/chef-client/current`, instead, use the `default_logger` option.

    runit_service "chef-client" do
      default_logger true
    end

**No Log Service**

If there isn't an appendant log service, set `log` to false, and the
log/run script won't be created.

    runit_service "no-svlog" do
      log false
    end

**Finish Script**

To create a service that has a finish script in its service directory,
set the `finish` parameter to `true`, and create a
`sv-finisher-finish.erb` template.

    runit_service "finisher" do
      finish true
    end

This will create `/etc/sv/finisher/finish`.

**Alternate service directory**

If the service directory for the managed service isn't the `sv_dir`
(`/etc/sv`), then specify it:

    runit_service "custom_service" do
      sv_dir "/etc/custom_service/runit"
    end

**No Service Directory**

If the service to manage has a package that provides its service
directory, such as `git-daemon` on Debian systems, set `sv_templates`
to false.

    package "git-daemon-run"

    runit_service "git-daemon" do
      sv_templates false
    end

This will create the service symlink in `/etc/service`, but it will
not manage any templates in the service directory.

**User Controlled Services**

To set up services controlled by a non-privileged user, we follow the
recommended configuration in the
[runit documentation](http://smarden.org/runit/faq.html#user) (Is it
possible to allow a user other than root to control a service?).

Suppose the user's name is floyd, and floyd wants to run floyds-app.
Assuming that the floyd user and group are already managed with Chef,
create a `runsvdir-floyd` runit_service.

    runit_service "runsvdir-floyd"

Create the `sv-runsvdir-floyd-log-run.erb` template, or add `log
false`. Also create the `sv-runsvdir-floyd-run.erb` with the following
content:

    #!/bin/sh
    exec 2>&1
    exec chpst -ufloyd runsvdir /home/floyd/service

Next, create the `runit_service` resource for floyd's app:

    runit_service "floyds-app" do
      sv_dir "/home/floyd/sv"
      service_dir "/home/floyd/service"
      owner "floyd"
      group "floyd"
    end

And now floyd can manage the service with sv:

    $ id
    uid=1000(floyd) gid=1001(floyd) groups=1001(floyd)
    $ sv stop /home/floyd/service/floyds-app/
    ok: down: /home/floyd/service/floyds-app/: 0s, normally up
    $ sv start /home/floyd/service/floyds-app/
    ok: run: /home/floyd/service/floyds-app/: (pid 5287) 0s
    $ sv status /home/floyd/service/floyds-app/
    run: /home/floyd/service/floyds-app/: (pid 5287) 13s; run: log: (pid 4691) 726s

**Options**

Next, let's set up memcached under runit with some additional options
using the `options` parameter. First, the
`memcached/templates/default/sv-memcached-run.erb` template:

    #!/bin/sh
    exec 2>&1
    exec chpst -u <%= @options[:user] %> /usr/bin/memcached -v -m <%= @options[:memory] %> -p <%= @options[:port] %>

Note that the script uses `chpst` (which comes with runit) to set the
user option, then starts memcached on the specified memory and port
(see below).

The log/run template,
`memcached/templates/default/sv-memcached-log-run.erb`:

    #!/bin/sh
    exec svlogd -tt ./main

Finally, the `runit_service` in our recipe:

    runit_service "memcached" do
      options({
        :memory => node[:memcached][:memory],
        :port => node[:memcached][:port],
        :user => node[:memcached][:user]}.merge(params)
      )
    end

This is where the user, port and memory options used in the run
template are used.

**Notifying Runit Services**

In previous versions of this cookbook where the definition was used,
it created a `service` resource that could be notified. With the
`runit_service` resource, recipes need to use the full resource name.
For example:

    runit_service "my-service"

    template "/etc/my-service.conf" do
      notifies :restart, "runit_service[my-service]"
    end

Because the resource implements actions for various commands that `sv`
can send to the service, any of those actions could be used for
notification. For example, `chef-client` supports triggering a Chef
run with a USR1 signal.

    template "/tmp/chef-notifier" do
      notifies :usr1, "runit_service[chef-client]"
    end

For older implementations of services that used `runit_service` as a
definition, but may support alternate service styles, use a
conditional, such as based on an attribute:

    service_to_notify = case node['nginx']['init_style']
                        when "runit"
                          "runit_service[nginx]"
                        else
                          "service[nginx]"
                        end

    template "/etc/nginx/nginx.conf" do
      notifies :restart, service_to_notify
    end

**More Examples**

For more examples, see the `runit_test` cookbook's `service` recipe in
the [git repository](https://github.com/opscode-cookbooks/runit).

Testing
=======

This cookbook has tests in the GitHub repository. To run the tests:

    git clone git://github.com/opscode-cookbooks/runit.git
    cd runit
    bundle install

There are two kinds of tests, unit tests and integration tests.

## Unit Tests

The resource/provider code is unit tested with rspec. To run these
tests, use rake:

    bundle exec rake spec

## Integration Tests

Integration tests are setup to run under minitest-chef. They are
automatically run under test kitchen.

    bundle exec kitchen test

This tests the default recipe ("default" configuration), and various
uses of the `runit_service` resource ("service" configuration).

License and Author
==================

Author:: Adam Jacob <adam@opscode.com>
Author:: Joshua Timberman <joshua@opscode.com>

Copyright:: 2008-2013, Opscode, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
This cookbook is used with test-kitchen to test the parent, runit cookbok
This cookbook is used with test-kitchen to test the parent, runit cookbok
