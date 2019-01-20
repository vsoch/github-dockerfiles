This directory structure contains the settings and configuration files specific
to your site or sites and is an integral part of multisite configurations.

It is now recommended to place your custom and downloaded extensions in the
/modules, /themes, and /profiles directories located in the Drupal root. The
sites/all/ subdirectory structure, which was recommended in previous versions
of Drupal, is still supported.

See core/INSTALL.txt for information about single-site installation or
multisite configuration.
The core/lib directory is for classes provided by Drupal Core that are original
to Drupal.  All Drupal-originated code must follow the PSR-0 naming convention
for classes and namespaces as documented here:

https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md

The vendor namespace for Drupal-originated code is "Drupal".
Code in the Drupal\Core namespace represents Drupal Subsystems provided by the
base system.  These subsystems MAY depend on Drupal Components and other
Subsystems, but MAY NOT depend on any code in a module.

Each Subsystem should be in its own namespace, and should be as self-contained
as possible.
Drupal Components are independent libraries that do not depend on the rest of
Drupal in order to function.

Components MAY depend on other Drupal Components or external libraries/packages,
but MUST NOT depend on any other Drupal code.

In other words, only dependencies that can be specified in a composer.json file
of the Component are acceptable dependencies.  Every Drupal Component presents a
valid dependency, because it is assumed to contain a composer.json file (even
if it may not exist yet).

Each Component should be in its own namespace, and should be as self-contained
as possible.  It should be possible to split a Component off to its own
repository and use as a stand-alone library, independently of Drupal.
The Drupal Gettext Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal EventDispatcher Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Utility Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Proxy Builder Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Bridge Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Render Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal FileCache Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Uuid Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal PhpStorage Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Discovery Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Annotation Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Dependency Injection Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Plugin Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal HttpFoundation Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Assertion Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Datetime Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Serialization Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal ClassFinder Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal FileSystem Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Diff Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Graph Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
The Drupal Transliteration Component

Thanks for using this Drupal component.

You can participate in its development on Drupal.org, through our issue system:
https://www.drupal.org/project/issues/drupal

You can get the full Drupal repo here:
https://www.drupal.org/project/drupal/git-instructions

You can browse the full Drupal repo here:
http://cgit.drupalcode.org/drupal
# [jQuery UI](http://jqueryui.com/) - Interactions and Widgets for the web

jQuery UI is a curated set of user interface interactions, effects, widgets, and themes built on top of jQuery. Whether you're building highly interactive web applications, or you just need to add a date picker to a form control, jQuery UI is the perfect choice.

If you want to use jQuery UI, go to [jqueryui.com](http://jqueryui.com) to get started, [jqueryui.com/demos/](http://jqueryui.com/demos/) for demos, [api.jqueryui.com](http://api.jqueryui.com/) for API documentation, or the [Using jQuery UI Forum](http://forum.jquery.com/using-jquery-ui) for discussions and questions.

If you want to report a bug/issue, please visit [bugs.jqueryui.com](http://bugs.jqueryui.com).

If you are interested in helping develop jQuery UI, you are in the right place.
To discuss development with team members and the community, visit the [Developing jQuery UI Forum](http://forum.jquery.com/developing-jquery-ui) or [#jqueryui-dev on irc.freenode.net](http://irc.jquery.org/).


## For Contributors

If you want to help and provide a patch for a bugfix or new feature, please take
a few minutes and look at [our Getting Involved guide](http://wiki.jqueryui.com/w/page/35263114/Getting-Involved).
In particular check out the [Coding standards](http://wiki.jqueryui.com/w/page/12137737/Coding-standards)
and [Commit Message Style Guide](http://contribute.jquery.org/commits-and-pull-requests/#commit-guidelines).

In general, fork the project, create a branch for a specific change and send a
pull request for that branch. Don't mix unrelated changes. You can use the commit
message as the description for the pull request.

For more information, see the [contributing page](CONTRIBUTING.md).

## Running the Unit Tests

Run the unit tests manually with appropriate browsers and any local web server. See our [environment setup](CONTRIBUTING.md#environment-minimum-required) and [information on running tests](CONTRIBUTING.md#running-the-tests).

You can also run the unit tests inside phantomjs by [setting up your environment](CONTRIBUTING.md#user-content-environment-recommended-setup).

## Building jQuery UI

jQuery UI uses the [Grunt](http://gruntjs.com/) build system.

To build jQuery UI, [setup your environment]([setting up your environment](CONTRIBUTING.md#environment-minimum-required)) and then run the following commands:

```sh
# Run the concat task to concatenate files
grunt concat

# There are many other tasks that can be run through Grunt.
# For a list of all tasks:
grunt --help
```
# Running tests

## Functional tests

* Start PhantomJS:
  ```
  phantomjs --ssl-protocol=any --ignore-ssl-errors=true ./vendor/jcalderonzumba/gastonjs/src/Client/main.js 8510 1024 768 2>&1 >> /dev/null &
  ```
* Run the functional tests:
  ```
  export SIMPLETEST_DB='mysql://root@localhost/dev_d8'
  export SIMPLETEST_BASE_URL='http://d8.dev'
  ./vendor/bin/phpunit -c core --testsuite functional
  ./vendor/bin/phpunit -c core --testsuite functional-javascript
  ```

Note: functional tests have to be invoked with a user in the same group as the
web server user. You can either configure Apache (or nginx) to run as your own
system user or run tests as a privileged user instead.

To develop locally, a straigtforward - but also less secure - approach is to run
tests as your own system user. To achieve that, change the default Apache user
to run as your system user. Typically, you'd need to modify
`/etc/apache2/envvars` on Linux or `/etc/apache2/httpd.conf` on Mac.

Example for Linux:

```
export APACHE_RUN_USER=<your-user>
export APACHE_RUN_GROUP=<your-group>
```

Example for Mac:

```
User <your-user>
Group <your-group>
```

If the default user is e.g. `www-data`, the above functional tests will have to
be invoked with sudo instead:

```
export SIMPLETEST_DB='mysql://root@localhost/dev_d8'
export SIMPLETEST_BASE_URL='http://d8.dev'
sudo -u www-data -E ./vendor/bin/phpunit -c core --testsuite functional
sudo -u www-data -E ./vendor/bin/phpunit -c core --testsuite functional-javascript
```
ABOUT CLASSY
-----------

Classy is a base theme that provides many classes in its markup. For cleaner
markup (fewer classes), the default Stable base theme can be used instead.

To use Classy as your base theme, set the 'base theme' in your theme's .info.yml
file to "classy":
  base theme: classy

See https://www.drupal.org/theme-guide/8/classy for more information on using
the Classy theme.

ABOUT DRUPAL THEMING
--------------------

See https://www.drupal.org/theme-guide/8 for more information on Drupal theming.

ABOUT STABLE
------------

Stable is the default base theme; it provides minimal markup and very few
CSS classes. If you prefer more structured markup see the Classy base theme.

Stable allows core markup and styling to evolve by functioning as a backwards
compatibility layer for themes against changes to core markup and CSS. If you
browse Stable's contents, you will find copies of all the Twig templates and
CSS files provided by core.

Stable will be used as the base theme if no base theme is set in a theme's
.info.yml file. To opt out of Stable you can set the base theme to false in
your theme's .info.yml file (see the warning below before doing this):
  base theme: false

Warning: Themes that opt out of using Stable as a base theme will need
continuous maintenance as core changes, so only opt out if you are prepared to
keep track of those changes and how they affect your theme.

ABOUT DRUPAL THEMING
--------------------

For more information, see Drupal.org's theming guide.
https://www.drupal.org/theme-guide/8

ABOUT STARK
-----------

The Stark theme is provided for demonstration purposes; it uses Drupal's
default HTML markup and CSS styles. It can be used as a troubleshooting tool to
determine whether module-related CSS and JavaScript are interfering with a more
complex theme, and can be used by designers interested in studying Drupal's
default markup without the interference of changes commonly made by more
complex themes.

To avoid obscuring CSS added to the page by Drupal or a contrib module, the
Stark theme itself has no styling.


ABOUT DRUPAL THEMING
--------------------

To learn how to build your own custom theme and override Drupal's default code,
see the Theming Guide: https://www.drupal.org/theme-guide

See the themes/README.txt for more information on where to place your
custom themes to ensure easy maintenance and upgrades.

These files are useful in tests that upload files or otherwise need to
manipulate files, in which case they are copied to the files directory as
specified in the site settings. Dummy files can also be generated by tests in
order to save space.
The classes in this directory act as a mock plugin type to test annotated class
discovery. See the corresponding test file:
/core/modules/system/src/Tests/Plugin/Discovery/AnnotatedClassDiscoveryTest.php
Installation profiles define additional steps that run after the base
installation of Drupal is completed. They may also offer additional
functionality and change the behavior of the site.

WHAT TO PLACE IN THIS DIRECTORY?
--------------------------------

Place downloaded and custom installation profiles in this directory.
Note that installation profiles are generally provided as part of a Drupal
distribution.

DOWNLOAD ADDITIONAL DISTRIBUTIONS
---------------------------------

Contributed distributions from the Drupal community may be downloaded at
https://www.drupal.org/project/project_distribution.

MULTISITE CONFIGURATION
-----------------------

In multisite configurations, installation profiles found in this directory are
available to all sites during their initial site installation.

MORE INFORMATION
----------------

Refer to the "Installation profiles" section of the README.txt in the Drupal
root directory for further information on extending Drupal with custom profiles.
Themes allow you to change the look and feel of your Drupal site. You can use
themes contributed by others or create your own.

WHAT TO PLACE IN THIS DIRECTORY?
--------------------------------

Placing downloaded and custom themes in this directory separates downloaded and
custom themes from Drupal core's themes. This allows Drupal core to be updated
without overwriting these files.

DOWNLOAD ADDITIONAL THEMES
--------------------------

Contributed themes from the Drupal community may be downloaded at
https://www.drupal.org/project/project_theme.

MULTISITE CONFIGURATION
-----------------------

In multisite configurations, themes found in this directory are available to
all sites. You may also put themes in the sites/all/themes directory, and the
versions in sites/all/themes will take precedence over versions of the same
themes that are here. Alternatively, the sites/your_site_name/themes directory
pattern may be used to restrict themes to a specific site instance.

MORE INFORMATION
-----------------

Refer to the "Appearance" section of the README.txt in the Drupal root directory
for further information on customizing the appearance of Drupal with custom
themes.
Modules extend your site functionality beyond Drupal core.

WHAT TO PLACE IN THIS DIRECTORY?
--------------------------------

Placing downloaded and custom modules in this directory separates downloaded and
custom modules from Drupal core's modules. This allows Drupal core to be updated
without overwriting these files.

DOWNLOAD ADDITIONAL MODULES
---------------------------

Contributed modules from the Drupal community may be downloaded at
https://www.drupal.org/project/project_module.

ORGANIZING MODULES IN THIS DIRECTORY
------------------------------------

You may create subdirectories in this directory, to organize your added modules,
without breaking the site. Some common subdirectories include "contrib" for
contributed modules, and "custom" for custom modules. Note that if you move a
module to a subdirectory after it has been enabled, you may need to clear the
Drupal cache so it can be found.

There are number of directories that are ignored when looking for modules. These
are 'src', 'lib', 'vendor', 'assets', 'css', 'files', 'images', 'js', 'misc',
'templates', 'includes', 'fixtures' and 'Drupal'.

MULTISITE CONFIGURATION
-----------------------

In multisite configurations, modules found in this directory are available to
all sites. You may also put modules in the sites/all/modules directory, and the
versions in sites/all/modules will take precedence over versions of the same
module that are here. Alternatively, the sites/your_site_name/modules directory
pattern may be used to restrict modules to a specific site instance.

MORE INFORMATION
----------------

Refer to the “Developing for Drupal” section of the README.txt in the Drupal
root directory for further information on extending Drupal with custom modules.
#Pathauto

If you are developing for this module, have a look at pathauto.api.php.

##Description

The Pathauto module provides support functions for other modules to
automatically generate aliases based on appropriate criteria, with a
central settings path for site administrators.

Implementations are provided for core entity types: content, taxonomy terms,
and users (including blogs and forum pages).

Pathauto also provides a way to delete large numbers of aliases.  This feature
is available at  Administer > Configuration > Search and metadata > URL aliases >
Delete aliases.

##Benefits

Besides making the page address more reflective of its content than
"node/138", it's important to know that modern search engines give
heavy weight to search terms which appear in a page's URL. By
automatically using keywords based directly on the page content in the URL,
relevant search engine hits for your page can be significantly
enhanced.

##Notices

Pathauto just adds URL aliases to content, users, and taxonomy terms.
Because it's an alias, the standard Drupal URL (for example node/123 or
taxonomy/term/1) will still function as normal.  If you have external links
to your site pointing to standard Drupal URLs, or hardcoded links in a module,
template, content or menu which point to standard Drupal URLs it will bypass
the alias set by Pathauto.

There are reasons you might not want two URLs for the same content on your
site. If this applies to you, please note that you will need to update any
hard coded links in your content or blocks.

If you use the "system path" (i.e. node/10) for menu items and settings like
that, Drupal will replace it with the url_alias.

For external links, you might want to consider the Path Redirect or
Global Redirect modules, which allow you to set forwarding either per item or
across the site to your aliased URLs.

###URLs (not) Getting Replaced With Aliases:
Please bear in mind that only URLs passed through Drupal's Drupal's URL and
Link APIs will be replaced with their aliases during page output. If
a module or your template contains hardcoded links, such as
'href="node/$node->nid"', those won't get replaced with their corresponding
aliases.

## Disabling Pathauto for a specific content type (or taxonomy)

When the pattern for a content type is left blank, the default pattern will be
used. But if the default pattern is also blank, Pathauto will be disabled
for that content type.

## Installing Pathauto
1. Install the module as normal, note that there are two dependencies.
2. Configure the module at admin/config/search/path/patterns - add a new pattern by creating by clicking "Add Pathauto pattern".
3. Fill out "Path pattern" with fx [node:title], choose which content types this applies to, give it a label (the name) and save it.
4. When you save new content from now on, it should automatically be assigned an alternative URL

##Credits:

The original module combined the functionality of Mike Ryan's autopath with
Tommy Sundstrom's path_automatic.

Significant enhancements were contributed by jdmquin @ www.bcdems.net.

Matt England added the tracker support (tracker support has been removed in
recent changes).

Other suggestions and patches contributed by the Drupal community.

Current maintainers:

- Dave Reid - http://www.davereid.net
- Greg Knaddison - http://www.knaddison.com
- Mike Ryan - http://mikeryan.name
- Frederik 'Freso' S. Olesen - http://freso.dk
Configuration Update Manager project
------------------------------------

The Configuration Update Manager project consists of two modules:

Configuration Update Base: A base module providing functionality related to
  updating and computing differences between configuration versions. No
  user interface; used by other modules such as Features.

Configuration Update Reports (in the config_ui sub-directory of this project):
  Adds an updates report and revert functionality to configuration management.
  Depends on Configuration Update Base. For more information, see the
  README.txt file in the subdirectory.
Configuration Update Reports module
-----------------------------------

CONTENTS OF THIS README FILE
- Introduction
- Installation
- Generating reports in the user interface
- Generating reports using Drush commands
- Important notes  *** Be sure to read this section ***


INTRODUCTION

This module provides a report that allows you to see the differences between the
default configuration items provided by the current versions of your installed
modules, themes, and install profile, and the active configuration of your
site. From this report, you can also import new configuration provided by
updates, and revert your site configuration to the provided values.

The main use case is: You update a module, and it has either changed default
configuration that it provides, or added new default configuration items that
you didn't get when you first installed the module. You want to be able to
import the new items, view the differences between the active site configuration
and the changed configuration, and possibly "revert" (or it may be an update) to
the newly-provided default configuration.


INSTALLATION

Install the module in the normal way for Drupal modules. The only dependencies
are the Configuration Manager module (Drupal core), and the Configuration Update
Base module (part of this same project download).


GENERATING REPORTS IN THE USER INTERFACE

You can generate configuration reports at Administration >> Configuration >>
Development >> Configuration management >> Update report (path:
admin/config/development/configuration/report ).

You can generate a report for a particular type of configuration object, such as
Actions, Tours, Views, etc. Or, you can generate a report for an installed
module, theme, or install profile. Finally, you can generate a report that
contains all configuration in one report.

The report has three sections, depending on what type you choose:

1. Missing configuration items: Configuration items that are provided as
   defaults by your currently-installed modules, themes, and install profile
   that are missing from your active site configuration.

   Any items listed here can be imported into your site.

2. Added configuration items: Configuration items that you added to the site
   (not provided by a currently-installed module, theme, or install
   profile). This section is only shown when you are running the report based on
   a configuration type.

   Items listed here can be exported, which is useful for developers or if you
   want to keep your site configuration in a version control system.

3. Changed configuration items: Configuration items that are in your active site
   configuration that differ from the same item currently being provided by an
   installed module, theme, or install profile.

   You can export these items, see the differences between what is on your site
   and what the module/theme/profile is currently providing, or "revert" to the
   version currently being provided by the module/theme/profile in its default
   configuration.

   Note that the differences may be a bit hard to read, but hopefully they'll
   give you the general idea of what has changed.


GENERATING REPORTS USING DRUSH COMMANDS

The reports detailed in the previous section can also be generated, in pieces,
using Drush commands (https://drupal.org/project/drush):

drush config-list-types (clt)
  Lists all the config types on your system. Reports can be run for
  'system.simple' (simple configuration), and 'system.all' (all types), in
  addition to the types listed by this command.

drush config-added-report (cra)
drush config-missing-report (crm)
drush config-different-report (crd)
  Run config reports (see below).

drush config-diff (cfd)
  Show config differences for one item between active and imported (see below).

The report commands run reports that tell what config has been added, is
missing, or is different between your active site configuration and the imported
default configuration from config/install directories of your installed profile,
modules, and themes.

For each report except "added", the first argument is one of:
- type: Runs the report for a configuration type; use drush config-list-types to
  list them.
- module: Runs the report for an installed module.
- theme: Runs the report for an installed theme.
- profile: Runs the report for the install profile.

The second argument for reports is the machine name of the configuration type,
module, theme, or install profile you want to run the report for. For the
"added" report, this is the only argument, as the added report is always by
configuration type.

These are the same as the reports you get in the UI, which is described above;
the only difference is that in Drush the report is separated into pieces.

Once you have found a configuration item with differences, you can view the
differences using the config-diff command. This is a normalized/formatted diff
like in the UI of this module, so see above for details.

Drush examples:

drush clt
drush crm module node
drush cra block
drush crd theme bartik
drush crd type system.all
drush crd type system.simple
drush crd profile standard
drush cfd block.block.bartik_search

Once you have figured out which configuration items are added, missing, or
different, you can:

- Export them - see drush config-export.

- Import missing configuration or revert to provided default values. To do this:

  (1) Locate the configuration file in the install profile, module, or theme
      config/install directory.

  (2) Copy this file to your configuration staging directory.

  (3) Run drush config-import. You might want to use the --preview option to see
      what differences you are about to import, before running the import, or
      use the drush config-diff command to look at individual differences.


IMPORTANT NOTES

Here are some notes about how this module functions:

* This module is always looking at the base configuration items, without
  overrides (from settings.php, for example) or translations.

* It is possible for an install profile on a site to provide configuration that
  overrides configuration from a module or theme. The install profile version
  always takes precedence. As an example, consider the case where module Foo
  provides a configuration item called foo.settings, and install profile Bar
  overrides this with its own file. Any reports that include foo.settings will
  be based on the differences between your site's active configuration and the
  version in the install profile. This is not usually a problem, but it can be
  confusing if you're looking at the Foo module report. The foo.settings item
  will be present, but the differences reported will be between the install
  profile's version and your site's active configuration, not the differences
  between the Foo module version and your site's active configuration.
# conditional_fields
Drupal 8 Conditional Fields

# TODO
Sorted by priority (descending)
- [ ] Use services instead of global functions
- [ ] Values input mode: widget (in progress)
- [x] Values input mode: regular expression
- [ ] Values input mode: set of values (AND) (in progress)
- [x] Values input mode: set of values (OR)
- [x] Values input mode: set of values (XOR)
- [x] Values input mode: set of values (NOT)
- [x] Tabs menu
- [ ] Add all conditions (js)
- [ ] Add all states (js)
- [ ] Add permissions
- [ ] User roles dependency (edit context)
- [ ] User roles dependency (view context)
- [ ] View context
- [ ] Tabs on edit content type pages
- [ ] JS effects settings
- [ ] Enhancement: Multiple dependents for a single dependency

# Working conditions
- [x] is filled/empty
- [ ] is touched/untouched
- [ ] is focused/unfocused
- [ ] is checked/unchecked
- [ ] has value (in progress)

# Working states
- [x] visible/invisible
- [x] required/optional
- [ ] filled with a value/emptied
- [ ] enabled/disabled
- [x] checked/unchecked
- [ ] expanded/collapsed

# Known issues
- [ ] XOR: saving data from hidden field if it was filled. (discuss it)
- [ ] filter available fields for creating conditions
The migrate_plus module extends the core migration system with API enhancements
and additional functionality, as well as providing practical examples.

Extensions to base API
======================
* A Migration configuration entity is provided, enabling persistance of dynamic
  migration configuration.
* A ConfigEntityDiscovery class is implemented which enables plugin
  configuration to be based on configuration entities. This is fully general -
  it can be used for any configuration entity type, not just migrations.
* A MigrationConfigEntityPluginManager class and corresponding
  plugin.manager.config_entity_migration service is provided, to enable
  discovery and instantiation of migration plugins based on the Migration
  configuration entity.
* A MigrationGroup configuration entity is provided, which enables migrations to
  be organized in groups, and to maintain shared configuration in one place.
* A MigrateEvents::PREPARE_ROW event is provided to dispatch hook_prepare_row()
  invocations as events.
* A SourcePluginExtension class is provided, enabling one to define fields and
  IDs for a source plugin via configuration rather than requiring PHP code.

Plugin types
============
migrate_plus provides the following plugin types, for use with the url source
plugin.

* A data_parser type, for parsing different formats on behalf of the url source
  plugin.
* A data_fetcher type, for fetching data to feed into a data_parser plugin.
* An authentication type, for adding authentication headers with the http
  data_fetcher plugin.

Plugins
=======

Process
-------
* The entity_lookup process plugin allows you to populate references to entities
  which already exist in Drupal, whether they were migrated or not.
* The entity_generate process plugin extends entity_lookup to also create the
  desired entity when it doesn't already exist.
* The file_blob process plugin supports creating file entities from blob data.
* The merge process plugin allows the merging of multiple arrays into a single
  field.
* The skip_on_value process plugin allows you to skip a row, or a given field,
  for specific source values.

Source
------
* A url source plugin is provided, implementing a common structure for
  file-based data providers.

Data parsers
------------
* The xml parser plugin uses PHP's XMLReader interface to incrementally parse
  XML files. This should be used for XML sources which are potentially very
  large.
* The simple_xml parser plugin uses PHP's SimpleXML interface to fully parse
  XML files. This should be used for XML sources where you need to be able to
  use complex xpaths for your item selectors, or have to access elements outside
  of the current item element via xpaths.
* The json parser plugin supports JSON sources.
* The soap parser plugin supports SOAP sources.

Data fetchers
-------------
* The file fetcher plugin works for most URLs regardless of protocol, as well as
  local filesystems.
* The http fetcher plugin provides the ability to add headers to an HTTP
  request (particularly through authentication plugins).

Authentication
--------------
* The basic authentication plugin provides HTTP Basic authentication.
* The digest authentication plugin provides HTTP Digest authentication.
* The oauth2 authencitation plugin provides OAuth2 authentication over HTTP.

Examples
========
* The migrate_example submodule provides a fully functional and runnable
example migration scenario demonstrating the basic concepts and most common
techniques for SQL-based migrations.
* The migrate_example_advanced submodule provides examples of migration from
different kinds of sources, as well as less common techniques.
INTRODUCTION
------------
The migrate_example_advanced module demonstrates some techniques for Drupal 8
migrations beyond the basics in migrate_example. It includes a group of
migrations with a wine theme.

SETUP
-----
To demonstrate XML migrations as realistically as possible, the setup module
provides the source data as REST services. So the migrations' references to these
services can be set up accurately, if you install migrate_example_advanced via
drush be sure to use the --uri parameter, e.g.

drush en -y migrate_example_advanced --uri=http://d8.local:8083/

THE WINE SITE
-------------
In this scenario, we have a wine aficionado site which stores data in SQL tables
as well is pulling in additional data from XML services.

To make the example as simple as to run as possible, the SQL data is placed in
tables directly in your Drupal database - in most real-world scenarios, your
source data will be in an external database. The migrate_example_advanced_setup
submodule creates and populates these tables, as well as configuring your Drupal
8 site (creating node types, vocabularies, fields, etc.) to receive the data,
and providing service endpoints for XML data.

STRUCTURE
---------
As with most custom migrations, there are two primary components to this
example:

1. Migration configuration, in the config/install directory. These YAML files
   describe the migration process and provide the mappings from the source data
   to Drupal's destination entities.

2. Source plugins, in src/Plugin/migrate/source. These are referenced from the
   configuration files, and provide the source data to the migration processing
   pipeline, as well as manipulating that data where necessary to put it into
   a canonical form for migrations.

UNDERSTANDING THE MIGRATIONS
----------------------------
Basic techniques demonstrated in the migrate_example module are not rehashed
here - it is expected that if you are learning Drupal 8 migration, you will
study and understand those examples first, and use migrate_example_advanced to
learn about specific techniques beyond those basics. This example doesn't have
the narrative form of migrate_example - it's more of a grab-bag demonstrating
varous features, and is more of a reference for, say, copying the code to set
up an XML migration. An index of things demonstrated by this module:

Multiple vocabularies populated in one migration
------------------------------------------------
See migrate_plus.migration.wine_terms.yml.

Importing from XML services
---------------------------
See migrate_plus.migration.wine_role_xml.yml.
INTRODUCTION
------------
The migrate_example module demonstrates how to implement custom migrations
for Drupal 8. It includes a group of "beer" migrations demonstrating a complete
simple migration scenario.

THE BEER SITE
-------------
In this scenario, we have a beer aficionado site which stores its data in MySQL
tables - there are content items for each beer on the site, user accounts with
profile data, categories to classify the beers, and user-generated comments on
the beers. We want to convert this site to Drupal with just a few modifications
to the basic structure.

To make the example as simple as to run as possible, the source data is placed
in tables directly in your Drupal database - in most real-world scenarios, your
source data will be in an external database. The migrate_example_setup submodule
creates and populates these tables, as well as configuring your Drupal 8 site
(creating a node type, vocabulary, fields, etc.) to receive the data.

STRUCTURE
---------
There are two primary components to this example:

1. Migration configuration, in the config/install directory. These YAML files
   describe the migration process and provide the mappings from the source data
   to Drupal's destination entities. The YAML file names are prefixed with
   'migrate_plus.migration.' (because, reading from right to left, they define
   "migration" configuration entities, and the configuration entity type is
   defined by the "migrate_plus" module).

2. Source plugins, in src/Plugin/migrate/source. These are referenced from the
   configuration files, and provide the source data to the migration processing
   pipeline, as well as manipulating that data where necessary to put it into
   a canonical form for migrations.

UNDERSTANDING THE MIGRATIONS
----------------------------
The YAML and PHP files are copiously documented in-line. To best understand
the concepts described in a more-or-less narrative form, it is recommended you
read the files in the following order:

1. migrate_plus.migration_group.beer.yml
2. migrate_plus.migration.beer_term.yml
3. BeerTerm.php
4. migrate_plus.migration.beer_user.yml
5. BeerUser.php
6. migrate_plus.migration.beer_node.yml
7. BeerNode.php
8. migrate_plus.migration.beer_comment.yml
9. BeerComment.php

RUNNING THE MIGRATIONS
----------------------
The migrate_tools module (https://www.drupal.org/project/migrate_tools) provides
the tools you need to perform migration processes. At this time, the web UI only
provides status information - to perform migration operations, you need to use
the drush commands.

# Enable the tools and the example module if you haven't already.
drush en -y migrate_tools,migrate_example

# Look at the migrations. Just look at them. Notice that they are displayed in
# the order they will be run, which reflects their dependencies. For example,
# because the node migration references the imported terms and users, it must
# run after those migrations have been run.
drush ms               # Abbreviation for migrate-status

# Run the import operation for all the beer migrations.
drush mi --group=beer  # Abbreviation for migrate-import

# Look at what you've done! Also, visit the site and see the imported content,
# user accounts, etc.
drush ms

# Look at the duplicate username message.
drush mmsg beer_user   # Abbreviation for migrate-messages

# Run the rollback operation for all the migrations (removing all the imported
# content, user accounts, etc.). Note that it will rollback the migrations in
# the opposite order as they were imported.
drush mr --group=beer  # Abbreviation for migrate-rollback

# You can import specific migrations.
drush mi beer_term,beer_user
# At this point, go look at your content listing - you'll see beer nodes named
# "Stub", generated from the user's favbeers references.

drush mi beer_node,beer_comment
# Refresh your content listing - the stub nodes have been filled with real beer!

# You can rollback specific migrations.
drush mr beer_comment,beer_node

README.txt for ACL 8.x-1.x



>>>> Please feel free to suggest improvements and additions to this file! <<<<




Overview
--------

ACL has no UI of its own and unless some other module uses it, it won't appear
to add anything to your site. Only bother with this module if some other module
tells you to.

For client modules that want to implement by-user node access in a robust and
compatible way, ACL provides the required functionality.
For a sample implementation see the Forum Access module:
http://drupal.org/project/forum_access




Acknowledgements
----------------

Originally written for Drupal 5 and maintained by merlinofchaos.
Ported to Drupal 6 and 7 and maintained by salvis.
Ported to Drupal 8 by id.tarzanych (Serge Skripchuk).



Upgrading from Drupal 6 or Drupal 7
-----------------------------------

Update to the latest Drupal 6/7 release, then upgrade as outlined in the
Drupal 8 Migrate docs (follow https://www.drupal.org/upgrade/migrate).



Troubleshooting
---------------

Even though ACL does not do anything by its own, Core recognizes it as a node
access module, and it requires you to rebuild permissions upon installation.

The client module is fully responsible for the correct use of ACL. It is very
unlikely that ACL should cause errors. 

If there is a node access problem, or if you intend to implement a module that
uses ACL, we highly recommend to use the Devel Node Access module as outlined
in the step-by-step instructions in
http://drupal.org/node/add/project-issue/acl




Support/Customizations
----------------------

Support by volunteers is available on

   http://drupal.org/project/issues/acl?status=All&version=8.x

Please consider helping others as a way to give something back to the community
that provides Drupal and the contributed modules to you free of charge.


For paid support and customizations of this module, help with implementing an
ACL client module, or other Drupal work, contact the maintainer through his
contact form:

   http://drupal.org/user/82964


# Field Permissions module

Original author: [markus_petrux](http://drupal.org/user/39593)


## CONTENTS OF THIS FILE

* OVERVIEW
* USAGE
* REQUIREMENTS
* INSTALLATION


## OVERVIEW

The Field Permissions module allows site administrators to set field-level
permissions for fields that are attached to any kind of entity (such as nodes
or users).

Permissions can be set for editing or viewing the field (either in all
contexts, or only when it is attached to an entity owned by the current user).
Permissions can also be set for editing the field while creating a new entity.

Permissions for each field are not created by default. Instead, administrators
can enable these permissions explicitly for the fields where this feature is
needed.


## USAGE

Once Field Permissions module is installed, you need to edit the field settings
form to enable permissions for each field where you need this feature. You can
choose from three options:

  * Public (author and administrators can edit, everyone can view)
  * Private (only author and administrators can edit and view)
  * Custom permissions

The default value ("Public") does not impose any field-level access control,
meaning that permissions are inherited from the entity view or edit
permissions. For example, users who are allowed to view a particular node that
the field is attached to will also be able to view the field.

"Private" provides quick and easy access to a commonly used form of field
access control.

Finally, if "Custom permissions" is chosen, a standard permissions matrix will
be revealed allowing you full flexibility to assign the following permissions
to any role on your site:

  * Create own value for field FIELD
  * Edit own value for field FIELD
  * Edit anyone's value for field FIELD
  * View own value for field FIELD
  * View anyone's value for field FIELD

These permissions will also be available on the standard permissions page at
Administer -> People -> Permissions.


## INSTALLATION

1) Copy all contents of this package to your modules directory preserving
   subdirectory structure.

2) Go to Administer -> Modules to install module. If the (Drupal core) Field UI
   module is not enabled, do so.

3) Review the settings of your fields. You will find a new option labelled
   "Field visibility and permissions" that allows you to control access to the
   field.

4) If you chose the setting labelled "Custom permissions", you will be able to
   set this field's permissions for any role on your site directly from the
   field edit form, or later on by going to the Administer -> People ->
   Permissions page.

5) Get an overview of the Field Permissions at:
   Administer -> Reports -> Field list -> Permissions
REST UI
=======

This module provides a user interface to manage REST resources.

Installation
============

Place this module at <drupal root>/modules/contrib/ and then install it.
In order to be able to create content, you need the HAL module to be
installed too.

Once the module has been installed, navigate to admin/config/services/rest
(Configuration > Web Services > REST through the administration panel) and configure the available resources.

-- SUMMARY --

The "Simple hierarchical select" module displays selected taxonomy fields as
hierarchical selects on entity forms and as exposed filter in views.


-- REQUIREMENTS --

The module "Taxonomy" (Drupal core) needs to be enabled for SHS to work
properly.


-- INSTALLATION --

* Install as usual, see https://www.drupal.org/documentation/install/modules-themes/modules-8
  for further information.


-- CONFIGURATION --

* Create a new field ("Reference > Taxonomy term") and select
  "Simple hierarchical select" on the form display settings for the new field.

* Form display settings
  - "Allow creating new items" (disabled)
    Items may be created directly from within the widget (user needs to have
    permission to create items in the configured bundle).
  - "Allow creating new levels" (disabled)
    Users with permission to create items in the configured bundle will be
    able to create a new item as child of the currently selected item.
  - "Force selection of deepest level"
    Force users to select items from the deepest level.


-- INTERGRATION WITH OTHER MODULES --

 * Views (Drupal core)
   - You are able to use the Simple hierarchical select widget as an exposed
     filter in Views.
     Simply add a filter for your term reference field or a term reference
     filter ("Has taxonomy terms" or "Has taxonomy  terms (with depth)") in your
     view and select "Simple hierarchical select" as selection type.
 * Chosen
   To use the Chosen library (https://www.drupal.org/project/chosen) you need to
   enable "Simple hierarchical select: Chosen" (shs_chosen) and configure the
   form display of your field to use Chosen.


-- MISSING FEATURES --

* Form display settings:
  Some options are current disabled because the underlying features are not
  implemented yet. This will be done until version 8.x-1.0.


-- CONTACT --

Current maintainers:
* Stefan Borchert (stborchert) - http://drupal.org/user/36942

This project has been sponsored by:
* undpaul
  Drupal experts providing professional Drupal development services.
  Visit http://www.undpaul.de for more information.

A simple empty page solution. Assists in creating empty menu callbacks,
mostly used for pages that only consist of blocks.

Authors:
  Nick Robillard <http://drupal.org/user/176017>

Sponsors:
  80 Elements <http://80elements.com>


Requirements
------------

1. Menu - Drupal core optional


Installation
------------

1. Place this module directory in your modules folder
(usually modules/contrib/).

2. Go to "Administer" > "Extend" and enable the module.

3. Manage callbacks at "Structure" > "Empty Page callbacks"
<admin/structure/empty-page>


Example: Create an empty front page
-------------------------------

1. Create an Empty Page callback. <admin/structure/empty-page/add>

2. Enter "node" in the Internal Path field (if that is what you have
under Default Front Page on the Site Information page).
<admin/config/system/site-information>

3. Add a Page Title (optional) and Save.


The standard list of the latest 10 nodes promoted to the front page is now
gone.
INTRODUCTION
------------
 
 Provides common and resuable token UI elements and missing core tokens.

 * For a full description of the module, visit the project page:
   https://drupal.org/project/token

 * To submit bug reports and feature suggestions, or to track changes:
   https://drupal.org/project/issues/token


INSTALLATION
------------

Install as usual, see
 https://www.drupal.org/docs/8/extending-drupal-8/installing-contributed-modules-find-import-enable-configure-drupal-8 for further
information.


TROUBLESHOOTING
---------------

Token module doesn't provide any visible functions to the user on its own, it
just provides token handling services for other modules.


MAINTAINERS
-----------

Current maintainers:

 * Dave Reid (https://drupal.org/user/53892)
# Migrate Manifest

This project provides tools for running Drupal 8 migrations using the manifest format. 

## Usage

This command allows you to specify a list of migrations and their config in
a YAML file. An example of a simple migration may look like this:

````
- d6_action_settings
- d6_aggregator_feed
````

You can also provide configuration to a migration for both source and the
destination. An example as such:

````
- d6_file:
  source:
    conf_path: sites/assets
  destination:
    source_base_path: destination/base/path
    destination_path_property: uri
- d6_action_settings
````

# Author

- Author:: Mike Ryan
- Author:: James Gilliland (<jgilliland@apqc.org>)
The migrate_upgrade module provides drush support for performing upgrades from
previous versions of Drupal to Drupal 8. It implements two drush commands:

* migrate-upgrade - performs a complete import of the source site's congiuration
and content into the target Drupal 8 site. Optionally, with the --configure-only
flag, it may create migration configurations for such an import without actually
running them, to permit customization of the import process.

* migrate-upgrade-rollback - removes content and certain configuration
previously imported either by the migrate-upgrade command or by the core
upgrade UI.

migrate-upgrade
===============
The upgrade command requires a Drupal 6-style database URL of the source site's
database, and the location of the source site's public files.

drush migrate-upgrade --legacy-db-url=mysql://user:pw@127.0.0.1/d6db --legacy-root=http://example.com

The --legacy-root option may be either the domain of your existing Drupal site
(with the public files pulled by HTTP), or a local file directory into which you
have copied the files directory from your source site.

If your source site used a database prefix for all tables, you may specify the
prefix with --legacy-db-prefix. Migration from sites with partial or mixed
prefixing is not supported. Note that if the source site is stored in a Postgres
schema, you must set the prefix to the schema with a period appended (e.g.,
--legacy-db-prefix=drupal.).

The migrate-upgrade command, like the core upgrade UI, is designed to be run on
a freshly installed and empty Drupal 8 site (where the only site configuration
that has been done is enabling any modules for which you wish to migrate data).

migrate-upgrade-rollback
========================

The rollback command has no arguments or options:

drush migrate-upgrade-rollback

If it detects that an upgrade has been performed, either by migrate-upgrade or
by the core UI, it removes all content imported via the migration process (it
identifies the upgrade by the presence of the migrate_drupal_ui.performed state
key). In addition, any configuration entites created by the migration process
(such as content type and field definitions) are also removed. Because simple
configuration settings (such as the site title) are generally modified rather
than created by the upgrade process, and the original values are not preserved,
those changes are not rolled back. To completely return to the previous state,
you need to restore the site from backup, or reinstall a fresh empty site.

migrate-upgrade --configure-only
================================
At the time of this release, tools have not yet been developed (along the lines
of the migrate_d2d_ui module under Drupal 7) for customizing Drupal-to-Drupal
migrations in Drupal 8. For now, the best option short of doing custom
development is to use the --configure-only option on migrate-upgrade to replace
the actual execution of the migrations with export of their configuration to
configuration entities, which can then be modified as needed for a particular
migration scenario. A suggested workflow:

1. Install a fresh empty D8 site, enabling all modules for which you wish to
   migrate data.
2. Run the drush migrate-upgrade command with the --configure-only option. This
   generates migration configuration entities in the D8 database (config table).
3. Create a custom module containing only a .info.yml file (with dependencies on
   migrate_plus and migrate_drupal) and a config/install directory.
4. Export your site configuration, e.g. drush cex --destination=/tmp/export
5. Copy the migration configuration that was generated by migrate-upgrade into
   the custom module - be sure *not* to copy the default group configuration,
   which is defined by migrate_plus:
    cp /tmp/export/migrate_plus.migration.* /tmp/export/migrate_plus.migration_group.migrate_*.yml migrate_custom/config/install/
6. Look at that migrate_plus.migration_group.* file - you'll see your database
   configuration captured there. In most cases, what you'll want to do is define
   your database connection in settings.php with those credentials under the key
   that is configured there - you won't want to commit the credentials to your
   git repo.
7. Edit the generated .yml files to reflect your custom migration path.
8. Reinstall D8, enable your custom module and migrate_tools, and proceed to
   work with your Drupal migrations as you would with any custom migration.
   Hint: you'll probably want config_devel so you can edit .yml files in
   config/install and immediately test your changes.

Note that the configuration entities generated above need to be prefixed to
avoid conflict with the core migration plugins they originated from. For
example, by default the core d6_user plugin generates the upgrade_d6_user
configuration entity. You may modify the 'upgrade_' prefix by providing a
--migration-prefix option.
The Migrate Tools module provides tools for running and managing Drupal 8
migrations.

Drush commands supported include:

* migrate-status - Lists migrations and their status.
* migrate-import - Performs import operations.
* migrate-rollback - Performs rollback operations.
* migrate-stop - Cleanly stops a running operation.
* migrate-reset-status - Sets a migration status to Idle if it's gotten stuck.
* migrate-messages - Lists any messages associated with a migration import.

The UI at this point provides a front-end equivalent to the migrate-status and
migrate-messages commands. It will be enhanced to allow running the other
operations, as well as provide the ability to create and alter migrations.
Devel
==========
Devel module contains helper functions and pages for Drupal developers and inquisitive admins:

 - A block for running custom PHP on a page
 - A block for quickly accessing devel pages
 - A block for masquerading as other users (useful for testing)
 - A mail-system class which redirects outbound email to files
 - Drush commands such as fn-hook, fn-event, ...
 - Docs at https://api.drupal.org/api/devel
 - more

This module is safe to use on a production site. Just be sure to only grant
'access development information' permission to developers.

Devel Kint
===================
Provides a dpr() function, which pretty prints variables.
Useful during development. Also see similar helpers like dpm(), dvm().

Webprofiler
==============
Adds a debug bar at bottom of all pages with tons of useful information like a query list,
cache hit/miss data, memory profiling, page speed, php info, session info, etc.

Devel Generate
=================
Bulk creates nodes, users, comment, terms for development. Has Drush integration.

Devel Generate Extensions
=========================
Devel Images Provider [http://drupal.org/project/devel_image_provider] allows to configure external providers for images.

Drush Unit Testing
==================
See develDrushTest.php for an example of unit testing of the Drush integration.
This uses Drush's own test framework, based on PHPUnit. To run the tests, use
run-tests-drush.sh. You may pass in any arguments that are valid for `phpunit`.

Author/Maintainers
======================
- Moshe Weitzman <weitzman at tejasa DOT com> http://www.acquia.com
- Hans Salvisberg <drupal at salvisberg DOT com>
- Pedro Cambra https://drupal.org/user/122101/contact http://www.ymbra.com/
- Juan Pablo Novillo https://www.drupal.org/u/juampynr
- lussoluca https://www.drupal.org/u/lussoluca
- willzyx https://www.drupal.org/u/willzyx
This module creates the "DevelGenerate" plugin type.

All you need to do to provide a new instance for "DevelGenerate" plugin type
is to create your class extending "DevelGenerateBase" and following the next steps.

1 - Declaring your plugin with annotations:

/**
 * Provides a ExampleDevelGenerate plugin.
 *
 * @DevelGenerate(
 *   id = "example",
 *   label = @Translation("example"),
 *   description = @Translation("Generate a given number of example elements. Optionally delete current example elements."),
 *   url = "example",
 *   permission = "administer example",
 *   settings = {
 *     "num" = 50,
 *     "kill" = FALSE,
 *     "another_property" = "default_value"
 *   }
 * )
 */

2 - Implement "settingsForm" method to create a form using the properties from annotations.

3 - Implement "handleDrushParams" method. It should return an array of values.

4 - Implement "generateElements" method. You can write here your business logic
using the array of values.

Notes:

You can alter existing properties for every plugin implementing hook_devel_generate_info_alter.

DevelGenerateBaseInterface details base wrapping methods that most DevelGenerate implementations
will want to directly inherit from Drupal\devel_generate\DevelGenerateBase.

To give support for a new field type the field type base class should properly
implements \Drupal\Core\Field\FieldItemInterface::generateSampleValue().
Devel generate automatically use the values returned by this method during the
generate process for generate placeholder field values. For more information
see:
https://api.drupal.org/api/drupal/core%21lib%21Drupal%21Core%21Field%21FieldItemInterface.php/function/FieldItemInterface::generateSampleValue
!! README.md is a work in progress !!

#Dependencies:

- d3.js: Webprofiler module requires D3 library 3.x (not 4.x) to render data.
  Download https://github.com/d3/d3 into /libraries/d3/d3.min.js
  
- highlight.js: Webprofiler module requires highlight 9.7.x library to syntax highlight collected queries.
  Download http://highlightjs.org into /libraries/highlight
  
If you use composer to manage dependencies and composer/installers plugin you could add those lines to composer.json:

```
"d3/d3": "3.5.*",
"components/highlightjs": "9.7.*"
```

to require section.

```
"libraries/{$name}": ["type:drupal-library"],
```

to installer-paths section.

```
{
      "type": "package",
      "package": {
        "name": "d3/d3",
        "version": "v3.5.17",
        "type": "drupal-library",
        "source": {
          "url": "https://github.com/d3/d3",
          "type": "git",
          "reference": "v3.5.17"
        }
      }
    },
    {
      "type": "package",
      "package": {
        "name": "components/highlightjs",
        "version": "9.7.0",
        "type": "drupal-library",
        "source": {
          "url": "https://github.com/components/highlightjs",
          "type": "git",
          "reference": "9.7.0"
        }
      }
    }
```

to repositories section.

#IDE link:

Every class name discovered while profiling (controller class, event class) are linked to an url for directly open in
an IDE, you can configure the url of those link based on the IDE you are using:

- Sublime text (2 and 3): see https://github.com/dhoulb/subl for Mac OS X
- Textmate: should be supported by default, use txmt://open?url=file://@file&line=@line as link
- PhpStorm 8+: use phpstorm://open?file=@file&line=@line as link

#Timeline:

Now it is possible to also collect the time needed to instantiate every single service used in a request, to make it 
work you need to add these two lines to settings.php (or, event better, to settings.local.php):

```
$class_loader->addPsr4('Drupal\\webprofiler\\', [ __DIR__ . '/../../modules/contrib/devel/webprofiler/src']);
$settings['container_base_class'] = '\Drupal\webprofiler\DependencyInjection\TraceableContainer';
```

Check if the path from the Webprofiler module in your settings.php file matches the location of the installed Webprofiler module in your project.
WHAT IS IT?
-----------
Kint for PHP is a tool designed to present your debugging data in the absolutely
best way possible.

In other words, it's var_dump() and debug_backtrace() on steroids. Easy to use,
but powerful and customizable. An essential addition to your development
toolbox.

USAGE
-----
This module allows to use these aliases:
    kint($data1, $data2, $data3, ...);
    ksm($data1, $data2, $data3, ...)
    kint_trace();

But to get the most out of Kint, you will want to use directly the Kint class:
    kint_require();
    Kint::dump($data);

Learn more about Kint: http://raveren.github.io/kint/


The Kint class function dd() will not work as expected, because this alias
is already defined in devel.module for other purposes.

CONTACTS
--------
Module author:
    Alexander Danilenko
    danilenko.dn@gmail.com
    https://drupal.org/user/1072104

Kint author:
    Rokas Šleinius a.k.a. Raveren
    raveren@gmail.com
    https://github.com/raveren# Kint - debugging helper for PHP developers

[![Total Downloads](https://poser.pugx.org/raveren/kint/downloads.png)](https://packagist.org/packages/raveren/kint)

> **New version** v1.0.0 is released with more than two years of active development - changes are too numerous to list, but there's CLI output and literally hundreds of improvements and additions.

![Screenshot](http://raveren.github.com/kint/img/preview.png)

## What am I looking at?

At first glance Kint is just a pretty replacement for **[var_dump()](http://php.net/manual/en/function.var-dump.php)**, **[print_r()](http://php.net/manual/en/function.print-r.php)** and **[debug_backtrace()](http://php.net/manual/en/function.debug-backtrace.php)**. 

However, it's much, *much* more than that. Even the excellent `xdebug` var_dump improvements don't come close - you will eventually wonder how you developed without it. 

Just to list some of the most useful features:

 * The **variable name and place in code** where Kint was called from is displayed;
 * You can **disable all Kint output easily and on the fly** - so you can even debug live systems without anyone knowing (even though you know you shouldn't be doing that!:). 
 * **CLI is detected** and formatted for automatically (but everything can be overridden on the fly) - if your setup supports it, the output is colored too:
  ![Kint CLI output](http://i.imgur.com/6B9MCLw.png)
 * **Debug backtraces** are finally fully readable, actually informative and a pleasure to the eye.
 * Kint has been **in active development for more than six years** and is shipped with [Drupal 8](https://www.drupal.org/) by default as part of its devel suite. You can trust it not being abandoned or getting left behind in features.
 * Variable content is **displayed in the most informative way** - and you *never, ever* miss anything! Kint guarantees you see every piece of physically available information about everything you are dumping*; 
   * <sup>in some cases, the content is truncated where it would otherwise be too large to view anyway - but the user is always made aware of that;</sup>
 * Some variable content types have an alternative display - for example you will be able see `JSON` in its raw form - but also as an associative array:
  ![Kint displays data intelligently](http://i.imgur.com/9P57Ror.png)
  There are more than ten custom variable type displays inbuilt and more are added periodically.


## Installation and Usage

One of the main goals of Kint is to be **zero setup**. 

[Download the archive](https://github.com/raveren/kint/releases/download/1.0.2/kint.zip) and simply
```php
<?php
require '/kint/Kint.class.php';
```

**Or, if you use Composer:**

```json
"require": {
   "raveren/kint": "^1.0"
}
```

Or just run `composer require raveren/kint`

**That's it, you can now use Kint to debug your code:**

```php
########## DUMP VARIABLE ###########################
Kint::dump($GLOBALS, $_SERVER); // pass any number of parameters

// or simply use d() as a shorthand:
d($_SERVER);


########## DEBUG BACKTRACE #########################
Kint::trace();
// or via shorthand:
d(1);


############# BASIC OUTPUT #########################
# this will show a basic javascript-free display
s($GLOBALS);


######### WHITESPACE FORMATTED OUTPUT ##############
# this will be garbled if viewed in browser as it is whitespace-formatted only
~d($GLOBALS); // just prepend with the tilde


########## MISCELLANEOUS ###########################
# this will disable kint completely
Kint::enabled(false);

ddd('Get off my lawn!'); // no effect

Kint::enabled(true);
ddd( 'this line will stop the execution flow because Kint was just re-enabled above!' );


```

Note, that Kint *does* have configuration (like themes and IDE integration!), but it's in need of being rewritten, so I'm not documenting it yet.

## Tips & Tricks

  * Kint is enabled by default, call `Kint::enabled(false);` to turn its funcionality completely off. The *best practice* is to enable Kint in DEVELOPMENT environment only (or for example `Kint::enabled($_SERVER['REMOTE_ADDR'] === '<your IP>');`) - so even if you accidentally leave a dump in production, no one will know.
  * `sd()` and `ddd()` are shorthands for `s();die;` and `d();die;` respectively. 
    * **Important:** The older shorthand `dd()` is deprecated due to compatibility issues and will eventually be removed. Use the analogous `ddd()` instead.
  * When looking at Kint output, press <kbd>D</kbd> on the keyboard and you will be able to traverse the tree with arrows and tab keys - and expand/collapse nodes with space or enter.
  * Double clicking the `[+]` sign in the output will expand/collapse ALL nodes; triple clicking big blocks of text will select it all.
  * Clicking the tiny arrows on the right of the output open it in a separate window where you can keep it for comparison.
  * To catch output from Kint just assign it to a variable<sup>beta</sup>
```php
$o = Kint::dump($GLOBALS); 
// yes, the assignment is automatically detected, and $o 
// now holds whatever was going to be printed otherwise.

// it also supports modifiers (read on) for the variable:
~$o = Kint::dump($GLOBALS); // this output will be in whitespace
```
  * There are a couple of real-time modifiers you can use:
    * `~d($var)` this call will output in plain text format.
    * `+d($var)` will disregard depth level limits and output everything (careful, this can hang your browser on huge objects)
    * `!d($var)` will show expanded rich output.
    * `-d($var)` will attempt to `ob_clean` the previous output so if you're dumping something inside a HTML page, you will still see Kint output.
  You can combine modifiers too: `~+d($var)`
  * To force a specific dump output type just pass it to the `Kint::enabled()` method. Available options are: `Kint::MODE_RICH` (default), `Kint::MODE_PLAIN`, `Kint::MODE_WHITESPACE` and `Kint::MODE_CLI`:
```php
Kint::enabled(Kint::MODE_WHITESPACE);
$kintOutput = Kint::dump($GLOBALS); 
// now $kintOutput can be written to a text log file and 
// be perfectly readable from there
```
  * To change display theme, use `Kint::$theme = '<theme name>';` where available options are: `'original'` (default), `'solarized'`, `'solarized-dark'` and `'aante-light'`. Here's an (outdated) preview:
  ![Kint themes](http://raveren.github.io/kint/img/theme-preview.png)
  * Kint also includes a naïve profiler you may find handy. It's for determining relatively which code blocks take longer than others:
```php
Kint::dump( microtime() ); // just pass microtime()
sleep( 1 );
Kint::dump( microtime(), 'after sleep(1)' );
sleep( 2 );
ddd( microtime(), 'final call, after sleep(2)' );
```
  ![Kint profiling feature](http://i.imgur.com/tmHUMW4.png)
----

[Visit the project page](http://raveren.github.com/kint/) for documentation, configuration, and more advanced usage examples.

### Author

**Rokas Šleinius** (Raveren)

### License

Licensed under the MIT License

This is the new module home for a unified redirection API (also replaces
path_redirect and globalredirect).
DELETE ALL
----------
 
CONTENTS OF THIS FILE
---------------------
 * Introduction
 * Requirements
 * Installation
 * Maintainers

INTRODUCTION
------------
This module is used to delete all content and/or users from a site.
This is mainly
a developer tool, which can come in handy in several cases, listed below.

The usual way to do this is to go to Administer -> Content then select all the
nodes and delete them. This works if you have a handful of nodes only. If you
have hundreds or thousands of nodes, then it is not a practical solution.

Another option is to directly delete the nodes from the node table in
the database. This does not work properly, since there are also comments,
and many tables for add on modules that needs to be cleaned.

This is a test site that the client was using for a period of time, and they
must clean it up before starting with real data.
You are testing something that creates a lot of nodes (e.g. aggregator), and
want to do it over and over again.
You created a site in the past and want to replicate it again,
but with new content.

Note that for nodes, comments and all additions to nodes that contributed
modules may have added. For users, any additional module data
will also be deleted.

REQUIREMENTS
------------
None.

INSTALLATION
------------
 * Install as usual,
 see https://www.drupal.org/documentation/install/modules-themes/modules-8
 for further information.

MAINTAINERS
-----------
 * Dipak Yadav (dipakmdhrm) - https://www.drupal.org/u/dipakmdhrm
 * Hammad Ghani (hammad-ghani) - https://www.drupal.org/u/hammad-ghani
 * Khalid Baheyeldin (kbahey) - https://www.drupal.org/u/kbahey
 * Brian Gilbert (realityloop) - https://www.drupal.org/u/realityloop
 * Kevin O'Brien (coderintherye) - https://www.drupal.org/u/coderintherye
 * Git Migration - https://www.drupal.org/u/git-migration
 * Doug Green (douggreen) - https://www.drupal.org/u/douggreen



