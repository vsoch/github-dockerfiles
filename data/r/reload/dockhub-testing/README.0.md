Diff module - http://drupal.org/project/diff
============================================

Diff enhances usage of node revisions by adding the following features:

- Diff between node revisions on the 'Revisions' tab to view all the changes
  between any two revisions of a node.
- Highlight changes inline while viewing a node to quickly see color-coded
  additions, changes, and deletions.
- Preview changes as a diff before updating a node.

It is also an API to compare any entities although this functionality is not
exposed by the core Diff module.

REQUIREMENTS
------------
Drupal 7.x

INSTALLATION
------------
1.  Place the Diff module into your modules directory.
    This is normally the "sites/all/modules" directory.

2.  Go to admin/build/modules. Enable the module.
    The Diff modules is found in the Other section.

Read more about installing modules at http://drupal.org/node/70151

See the configuration section below.

UPGRADING
---------
Any updates should be automatic. Just remember to run update.php!

CONFIGURATION
-------------

Unlike the earlier version, the module now has a lot of configurable settings.

Global settings can be found under Configuration > Content > Diff

i.e. http://www.example.com/admin/config/content/diff

Entity specific settings would be listed under the entities settings. This 
module only handles Node revisioning functionality, and these are detailed 
below.

1) Node revisioning settings

Diff needs to be configured to be used with specific node types on your site.
To enable any of Diff's options on a content type's settings page.

e.g. http://www.example.com/admin/structure/types/manage/page

  a) Diff options

  Under "Compare revisions", enable the settings that you want;
  
    i) "Show View changes button on node edit form" adds a new "Preview" like
        submit button to node editing pages. This shows a diff preview.
  
    ii) "Enable the Revisions page for this content type" adds the revisioning
         tab to content. This allows users to compare between various revisions
         that they have access to.
  
    iii) "Standard comparison preview" option allows you to control how the most
          current revision is show on the revision comparision page.
       
  b) Publishing options

  It is strongly advised that you also enable the automatic creation of
  revisions on any content types you want to use this with. If you do not do
  this, chances are there will be limited revisioning information available to
  compare. 

  Under "Publishing options", enable "Create new revision".

2) Field revisioning settings

   Global settings per field type can be found here:

   http://www.example.com/admin/config/content/diff/fields

   "Show field title" toggles field title visibility on the comparison page.
   
   "Markdown callback" is the callback used to render the field when viewing the
   page in the "Marked down" page view.
   
   "Line counter" is an optional. This shows the approximate line number where
   the change occurred. This is an approximate counter only.
   
   Other fields add additional settings here.
   
3) Entity revisioning settings

  Global configurable settings limited to node entities.

  a) Show entity label header
  
  This provides a field like title for the entity label field.
  
  i.e. For nodes, this provides a header for the node's title. 
  
  b) Treat diff pages as administrative
  
  By default, the revisioning pages are administrative, i.e. they will use the
  administration theme. You can block this by unchecking this option.
  
4) Global settings

A small number of new features have been added to the 7.x-3.x branch, these
include the ability to change the leading and trailing lines in the comparison,
a new CSS theme for the diff pages, new JScript options for the revisioning
selection form and options to help prevent cross operating systems in relation
to line endings.

http://www.example.com/admin/config/content/diff

Technical
---------
- Diff compares the raw data, not the filtered output, making it easier to see
changes to HTML entities, etc.
- The diff engine itself is a GPL'ed php diff engine from phpwiki.

API
---
See diff.api.php

Maintainers
-----------
- realityloop (Brian Gilbert)
- Alan D. (Alan Davison)
- dww (Derek Wright)
- moshe (Moshe Weitzman)
- rötzi (Julian)
- yhahn (Young Hahn)
This directory structure contains the settings and configuration files specific
to your site or sites and is an integral part of multisite configuration.

The sites/all/ subdirectory structure should be used to place your custom and
downloaded extensions including modules, themes, and third party libraries.

Downloaded installation profiles should be placed in the /profiles directory
in the Drupal root.

In multisite configuration, extensions found in the sites/all directory
structure are available to all sites. Alternatively, the sites/your_site_name/
subdirectory pattern may be used to restrict extensions to a specific
site instance.

See the respective README.txt files in sites/all/themes and sites/all/modules
for additional information about obtaining and organizing extensions.

See INSTALL.txt in the Drupal root for information about single-site
installation or multisite configuration.
Place downloaded and custom themes that modify your site's appearance in this
directory to ensure clean separation from Drupal core and to facilitate safe,
self-contained code updates. Contributed themes from the Drupal community may
be downloaded at http://drupal.org/project/themes.

It is safe to organize themes into subdirectories and is recommended to use
Drupal's sub-theme functionality to ensure easy maintenance and upgrades.

In multisite configuration, themes found in this directory are available to
all sites. Alternatively, the sites/your_site_name/themes directory pattern may
be used to restrict themes to a specific site instance.

Refer to the "Appearance" section of the README.txt in the Drupal root
directory for further information on theming.
Deployotron
===========

Deployotron is a Drush command to simplify deploying new code to a
Drupal site.

There's already a lot of ways to deploy ones Drupal site, from FTPing
up the files to having Capistrano deploy the site when the build
passes in Jenkins. Deployotron aims to be simple to use, but also
usable as a part of a bigger setup.

[![Build Status](https://travis-ci.org/reload/deployotron.png?branch=master)](https://travis-ci.org/reload/deployotron)
[![Code Coverage](https://scrutinizer-ci.com/g/reload/deployotron/badges/coverage.png?s=0f0d54845fc1c45affcc0ad8c111e40f4e40c359)](https://scrutinizer-ci.com/g/reload/deployotron/)
[![Scrutinizer Quality Score](https://scrutinizer-ci.com/g/reload/deployotron/badges/quality-score.png?s=cd9fde12be1b74734b00d59618d4eb6c1bf5bfb0)](https://scrutinizer-ci.com/g/reload/deployotron/)

Overview
========

In order to keep things simple, we're working with a few assumptions:

That the code is in GIT, and that the root of the site is checked in.

That you can run Drush commands and GIT on the live webserver and the
root of the site on the webserver is a git checkout, and

That you've set up Drush aliases to reach the live webserver.

For everyone's sanity, we suggest having a Drush alias file in
`sites/all/drush/<short-site-alias>.aliases.drushrc.php` that defines
relevant environments (production, dev, etc.), so that everybody is
using the same settings.

And we suggest that deployotron is installed by copying it into the
`sites/all/drush` folder and committed to the site repository. This
ensures that everyone is running the exact same version of deployotron
when deploying.

Setup
=====

Clone Deployotron into `sites/all/drush`. 

Create a `<sitename>.aliases.drushrc.php` file in the same directory,
with the definition of the different environments.

Deployotron is configured for each alias by adding an array of options
in the `'deployotron'` key of the alias array (see the example later,
if that didn't make any sense). All the double-dash options the deploy
command takes can be specified this way, and it's recommended to at
least define the `'branch'` option to select a default branch to
deploy.

Initialize the environments by doing an initial git clone of the
codebase in the destination directories.

Usage
=====

Deploying
---------

To run the deployment, use a command like:

    /var/www/site$ drush deploy @alias

To get a listing of all supported command line options, do a `drush
help deploy`.

Example configuration:

    $aliases['staging'] = array(
      'remote-host' => 'example.com',
      'remote-user' => 'deploy_user',
      'uri' => 'default',
      'root' => '/path',
      'deployotron' => array(
        'branch' => 'develop',
        'dump-dir' => '/backups', // Defaults to /tmp.
        'num-dumps' => 3, // Defaults to 5. 0 for unlimited.
        'post-deploy' => array(
          'sudo apache2 graceful',
          'drush -y fra',
        ),
      ),
    );

As demonstrated, you can add external commands to be run before (pre-)
or after (post-) the individual actions. All the possible options is
listed in `drush help deploy` and `drush deployotron-actions`.

In addition to command line options you can add messages to be
displayed to the deploying user by using the following keys:

 * `message`: Shown at confirmation and after deployment.
 * `confirm_message`: Shown at confirmation.
 * `done_message`: Shown after deployment.
 * `confirm_message_<command>`: Shown at confirmation for the
   `<command>`.
 * `done_message_<command>`: Shown after deployment for the
   `<command>`.

These can be useful to remind the user of extra manual steps, or other
things they should be aware.

Recovering
----------

In case everything goes to hell after a deployment, you can do another
deployment using a known good revision, or use:

    /var/www/site$ drush omg @alias

This will try to find recent database dumps, ask which to use and
attempt to import the database and revert the codebase to the previous
revision. It will not attempt to clear caches or restarting any
services.

Help
----

Running `drush deployotron-actions` will give a full list of which
commands uses which actions, and the options of all actions.

Sudo setup
==========

To run sudo commands in pre/post hooks, you need to configure sudo to
allow the command without a password.

Run:

    sudo visudo -f /etc/sudoers.d/deployotron

And add something like following to the file (replacing `deploy_user`
with the `remote-user` of the alias used for deployment):

    deploy_user          ALL=(root) NOPASSWD: /usr/sbin/service apache2 graceful,/usr/sbin/service varnish restart

This allows deployotron to run "sudo service apache2 graceful" and
"sudo service varnish restart".
Place downloaded and custom modules that extend your site functionality beyond
Drupal core in this directory to ensure clean separation from core modules and
to facilitate safe, self-contained code updates. Contributed modules from the
Drupal community may be downloaded at http://drupal.org/project/modules.

It is safe to organize modules into subdirectories, such as "contrib" for
contributed modules, and "custom" for custom modules. Note that if you move a
module to a subdirectory after it has been enabled, you may need to clear the
Drupal cache so that it can be found.

In multisite configuration, modules found in this directory are available to
all sites. Alternatively, the sites/your_site_name/modules directory pattern may
be used to restrict modules to a specific site instance.

Refer to the "Developing for Drupal" section of the README.txt in the Drupal
root directory for further information on extending Drupal with custom modules.
Manual Crop
===========

The Manual Crop module exposes a set of image style effects that allow you
to crop (and scale) an image after uploading.

Dependencies
------------
- Libraries 2.x
- jQuery plugins:
    - imagesLoaded:
        + Website: http://desandro.github.io/imagesloaded
        + Download: https://github.com/desandro/imagesloaded/archive/v2.1.2.tar.gz
    - imgAreaSelect:
        + Website: http://odyniec.net/projects/imgareaselect
        + Download: http://odyniec.net/projects/imgareaselect/jquery.imgareaselect-0.9.10.zip

Installation
------------
Start by downloading and installing the Libraries 2.x module.

Next download and extract the imagesLoaded plugin, rename the extracted folder to
"jquery.imagesloaded" and place it under "sites/all/libraries". The plugin should
now be located at "sites/all/libraries/jquery.imagesloaded/jquery.imagesloaded.min.js".

Please note that the 3.x version can also be used, but it depends on jQuery 1.5
which can only be obtained by installing the jQuery Update module.

Now download and extract the imgAreaSelect plugin, rename extracted folder to
"jquery.imgareaselect" and copy it into "sites/all/libraries". The plugin should
now be located at "sites/all/libraries/jquery.imgareaselect/scripts/jquery.imgareaselect.min.js".

When finished you can activate the module via the Modules page!

Configuration
-------------
After installing the module you need to configure your image styles before you
can start cropping. Go to Administration » Configuration » Media » Image styles
and click on the "edit" link for the styles that need a Manual Crop effect.

Add and configure one of the Manual Crop effects, you'll notice that the Manual
Crop effect will always become the first effect in the list. This is because
cropping should always be done first, otherwise the result will be unpredictable.

Next go to Administration » Structure » Content types and click on the "manage fields"
link (the Field UI module should be activated) for the content type that should
allow cropping. Now click on the "edit" link of the image field, so you can enable
and configure Manual Crop (open the "Manual Crop" fieldset) for the current field.

After saving the settings you should return to the content type overview and click
on "manage display" so you can set the (cropped) image style that should be used.
Please read this file and also the INSTALL.txt.  
They contain answers to many common questions.
If you are developing for this module, the API.txt may be interesting.
If you are upgrading, check the CHANGELOG.txt for major changes.

**Description:
The Pathauto module provides support functions for other modules to 
automatically generate aliases based on appropriate criteria, with a 
central settings path for site administrators.

Implementations are provided for core entity types: content, taxonomy terms,
and users (including blogs and tracker pages).

Pathauto also provides a way to delete large numbers of aliases.  This feature 
is available at  Administer > Site building > URL aliases > Delete aliases

**Benefits:
Besides making the page address more reflective of its content than
"node/138", it's important to know that modern search engines give 
heavy weight to search terms which appear in a page's URL. By 
automatically using keywords based directly on the page content in the URL, 
relevant search engine hits for your page can be significantly
enhanced.

**Installation AND Upgrades:
See the INSTALL.txt file.

**Notices:
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

URLs (not) Getting Replaced With Aliases:
Please bear in mind that only URLs passed through Drupal's l() or url()
functions will be replaced with their aliases during page output. If a module
or your template contains hardcoded links, such as 'href="node/$node->nid"'
those won't get replaced with their corresponding aliases. Use the
Drupal API instead:

* 'href="'. url("node/$node->nid") .'"' or
* l("Your link title", "node/$node->nid")

See http://api.drupal.org/api/HEAD/function/url and 
http://api.drupal.org/api/HEAD/function/l for more information.

** Disabling Pathauto for a specific content type (or taxonomy)
When the pattern for a content type is left blank, the default pattern will be 
used. But if the default pattern is also blank, Pathauto will be disabled 
for that content type.

** Bulk Updates Must be Run Multiple Times:
As of 5.x-2.x Pathauto now performs bulk updates in a manner which is more 
likely to succeed on large sites.  The drawback is that it needs to be run 
multiple times.  If you want to reduce the number of times that you need to 
run Pathauto you can increase the "Maximum number of objects to alias in a 
bulk update:" setting under General Settings.

**WYSIWYG Conflicts - FCKEditor, TinyMCE, etc.
If you use a WYSIWYG editor, please disable it for the Pathauto admin page.  
Failure to do so may cause errors about "preg_replace" problems due to the <p>
tag being added to the "strings to replace".  See http://drupal.org/node/175772

**Credits:
The original module combined the functionality of Mike Ryan's autopath with
Tommy Sundstrom's path_automatic.

Significant enhancements were contributed by jdmquin @ www.bcdems.net.

Matt England added the tracker support.

Other suggestions and patches contributed by the Drupal community.

Current maintainers: 
  Greg Knaddison - http://growingventuresolutions.com
  Mike Ryan - http://mikeryan.name
  Frederik 'Freso' S. Olesen - http://freso.dk

**Changes:
See the CHANGELOG.txt file.


-- SUMMARY --

Libraries API provides external library handling for Drupal modules.

For a full description visit the project page:
  http://drupal.org/project/libraries
Bug reports, feature suggestions and latest developments:
  http://drupal.org/project/issues/libraries


-- REQUIREMENTS --

* None.


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.
  Note that installing external libraries is separate from installing this
  module and should happen in the sites/all/libraries directory. See
  http://drupal.org/node/1440066 for more information.


-- CONTACT --

Current maintainers:
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136
* Tobias Stöckler (tstoeckler) - http://drupal.org/user/107158


This project has been sponsored by:
* UNLEASHED MIND
  Specialized in consulting and planning of Drupal powered sites, UNLEASHED
  MIND offers installation, development, theming, customization, and hosting
  to get you started. Visit http://www.unleashedmind.com for more information.


Example library

Version 1

This file is an example file to test version detection.

The various other files in this directory are to test the loading of JavaScript,
CSS and PHP files.
- JavaScript: The filenames of the JavaScript files are asserted to be in the
  raw HTML via SimpleTest. Since the filename could appear, for instance, in an
  error message, this is not very robust. Explicit testing of JavaScript,
  though, is not yet possible with SimpleTest. To allow for easier debugging, we
  place the following text on the page:
  "If this text shows up, no JavaScript test file was loaded."
  This text is replaced via JavaScript by a text of the form:
  "If this text shows up, [file] was loaded successfully."
  [file] is either 'example_1.js', 'example_2.js', 'example_3.js',
  'example_4.js' or 'libraries_test_module.js'. If you have SimpleTest's verbose
  mode enabled and see the above text in one of the debug pages, the noted
  JavaScript file was loaded successfully.
- CSS: The filenames of the CSS files are asserted to be in the raw HTML via
  SimpleTest. Since the filename could appear, for instance, in an error
  message, this is not very robust. Explicit testing of CSS, though, is not yet
  possible with SimpleTest. Hence, the CSS files, if loaded, make the following
  text a certain color:
  "If one of the CSS test files has been loaded, this text will be colored:
  - example_1: red
  - example_2: green
  - example_3: orange
  - example_4: blue
  - libraries_test_module: purple"
  If you have SimpleTest's verbose mode enabled, and see the above text in a
  certain color (i.e. not in black), a CSS file was loaded successfully. Which
  file depends on the color as referenced in the text above.
- PHP: The loading of PHP files is tested by defining a dummy function in the
  PHP files and then checking whether this function was defined using
  function_exists(). This can be checked programatically with SimpleTest.
The loading of integration files is tested with the same method. The integration
files are libraries_test_module.js, libraries_test_module.css,
libraries_test_module.inc and are located in the test module's directory
alongside libraries_test_module.info (i.e. they are not in the same directory as
this file).

Welcome to Views 3. Please see the advanced help for more information.

If you're having trouble installing this module, please ensure that your
tar program is not flattening the directory tree, truncating filenames
or losing files.

Installing Views:

Place the entirety of this directory in sites/all/modules/views
You must also install the CTools module (http://www.drupal.org/project/ctools)  to use Views.

Navigate to administer >> build >> modules. Enable Views and Views UI.

If you're new to Views, try the Simple Views module which can create some
often used Views for you, this might save you some time.

Here you can find many modules extending the functionality of Views:
  http://drupal.org/taxonomy/term/89
This it the abbreviated documentation for http://www.drupal.org/project/update_rules.

FULL DOCUMENTATION: http://www.drupal.org/node/2470039.

This module provides rules events, actions, and conditions related to Drupal project update statuses.
Drupal core offers a simple email notification when the site needs core/module updates. Unfortunately
those emails do not contain any information about the projects or the releases, and you're at the mercy
of the standard update notification configuration. This module solves this problem, and gives you all of
the capabilities (actions, conditions, etc.) of Rules for handling update statuses. Imagine being able to
send an email to your task management app with the server name, project name, and release info every
time a security update is needed. This is a simple example, but was the exact goal I was shooting for
when I wrote this module.Pathologic
----------

Project Page:
http://drupal.org/project/pathologic

By Garrett Albright
http://drupal.org/user/191212

Originally sponsored by Precision Intermedia
http://www.precisionintermedia.com/

Thanks to all who have used this module over the years and provided bug reports
and suggestions via email and the issue queue! I love you all.

Installation & Configuration
----------------------------

For full installation and configuration instructions, please see this page in
the Drupal online manual:
http://drupal.org/node/257026

The CTools Plugin Example is an example for developers of how to CTools
access, argument, content type, context, and relationship plugins.

There are a number of ways to profit from this:

1. The code itself intends to be as simple and self-explanatory as possible. 
   Nothing fancy is attempted: It's just trying to use the plugin API to show
   how it can be used.
   
2. There is a sample panel. You can access it at /ctools_plugin_example/xxxx
   to see how it works.
   
3. There is Advanced Help at admin/advanced_help/ctools_plugin_example.
-- SUMMARY --

The Administration menu module displays the entire administrative menu tree (and
most local tasks) in a drop-down menu, providing administrators one- or
two-click access to most pages.  Other modules may also add menu links to the
menu using hook_admin_menu_output_alter().

For a full description of the module, visit the project page:
  http://drupal.org/project/admin_menu

To submit bug reports and feature suggestions, or to track changes:
  http://drupal.org/project/issues/admin_menu


-- REQUIREMENTS --

None.


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/895232 for further information.

* You likely want to disable Toolbar module, since its output clashes with
  Administration menu.


-- CONFIGURATION --

* Configure user permissions in Administration » People » Permissions:

  - Use the administration pages and help (System module)

    The top-level administration categories require this permission to be
    accessible. The administration menu will be empty unless this permission is
    granted.

  - Access administration menu

    Users in roles with the "Access administration menu" permission will see
    the administration menu at the top of each page.

  - Display Drupal links

    Users in roles with the "Display drupal links" permission will receive
    links to drupal.org issue queues for all enabled contributed modules. The
    issue queue links appear under the administration menu icon.

  Note that the menu items displayed in the administration menu depend on the
  actual permissions of the viewing user. For example, the "People" menu item
  is not displayed to a user who is not a member of a role with the "Administer
  users" permission.

* Customize the menu settings in Administration » Configuration and modules »
  Administration » Administration menu.

* To prevent administrative menu items from appearing twice, you may hide the
  "Management" menu block.


-- CUSTOMIZATION --

* To override the default administration menu icon, you may:

  1) Disable it via CSS in your theme:

     body #admin-menu-icon { display: none; }

  2) Alter the image by overriding the theme function:

     Copy the entire theme_admin_menu_icon() function into your template.php,
     rename it to phptemplate_admin_menu_icon() or THEMENAME_admin_menu_icon(),
     and customize the output according to your needs.

  Remember that the output of the administration menu is cached. To see changes
  from your theme override function, you must clear your site cache (via
  the "Flush all caches" link on the menu).

* To override the font size, add the following line to your theme's stylesheet:

  body #admin-menu { font-size: 10px; }


-- TROUBLESHOOTING --

* If the menu does not display, check the following:

  - Are the "Access administration menu" and "Use the administration pages and help"
    permissions enabled for the appropriate roles?

  - Does html.tpl.php of your theme output the $page_bottom variable?

* If the menu is rendered behind a Flash movie object, add this property to your
  Flash object(s):

  <param name="wmode" value="transparent" />

  See http://drupal.org/node/195386 for further information.


-- FAQ --

Q: When the administration menu module is enabled, blank space is added to the
   bottom of my theme. Why?

A: This is caused by a long list of links to module issue queues at Drupal.org.
   Use Administer >> User management >> Permissions to disable the "display
   drupal links" permission for all appropriate roles. Note that since UID 1
   automatically receives all permissions, the list of issue queue links cannot
   be disabled for UID 1.


Q: After upgrading to 6.x-1.x, the menu disappeared. Why?

A: You may need to regenerate your menu. Visit
   http://example.com/admin/build/modules to regenerate your menu (substitute
   your site name for example.com).


Q: Can I configure the administration menu module to display another menu (like
   the Navigation menu, for instance)?

A: No. As the name implies, administration menu module is for administrative
   menu links only. However, you can copy and paste the contents of
   admin_menu.css into your theme's stylesheet and replace #admin-menu with any
   other menu block id (#block-menu-1, for example).


Q: Sometimes, the user counter displays a lot of anonymous users, but no spike
   of users or requests appear in Google Analytics or other tracking tools.

A: If your site was concurrently spidered by search-engine robots, it may have
   a significant number of anonymous users for a short time. Most web tracking
   tools like Google Analytics automatically filter out these requests.


Q: I enabled "Aggregate and compress CSS files", but admin_menu.css is still
   there. Is this normal?

A: Yes, this is the intended behavior. the administration menu module only loads
   its stylesheet as needed (i.e., on page requests by logged-on, administrative
   users).


Q: Why are sub-menus not visible in Opera?

A: In the Opera browser preferences under "web pages" there is an option to fit
   to width. By disabling this option, sub-menus in the administration menu
   should appear.


Q: How can the administration menu be hidden on certain pages?

A: You can suppress it by simply calling the following function in PHP:

     module_invoke('admin_menu', 'suppress');

   However, this needs to happen as early as possible in the page request, so
   placing it in the theming layer (resp. a page template file) is too late.
   Ideally, the function is called in hook_init() in a custom module.  If you do
   not have a custom module, placing it into some conditional code at the top of
   template.php may work out, too.


-- CONTACT --

Current maintainers:
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136
* Peter Wolanin (pwolanin) - http://drupal.org/user/49851
* Stefan M. Kudwien (smk-ka) - http://drupal.org/user/48898
* Dave Reid (Dave Reid) - http://drupal.org/user/53892

Major rewrite for Drupal 6 by Peter Wolanin (pwolanin).

This project has been sponsored by:
* UNLEASHED MIND
  Specialized in consulting and planning of Drupal powered sites, UNLEASHED
  MIND offers installation, development, theming, customization, and hosting
  to get you started. Visit http://www.unleashedmind.com for more information.

* Lullabot
  Friendly Drupal experts providing professional consulting & education
  services. Visit http://www.lullabot.com for more information.

* Acquia
  Commercially Supported Drupal. Visit http://acquia.com for more information.


README.txt
==========

********************************************************************
This is i18n package 7.x, and will work with Drupal 7.x
********************************************************************
WARNING: DO READ THE INSTALL FILE AND the ON-LINE HANDBOOK
********************************************************************

This is a collection of modules providing multilingual features.
These modules will build onto Drupal 7 core features enabling a full multilingual site

Up to date documentation will be kept on-line at http://drupal.org/node/133977

Additional Support
=================
For support, please create a support request for this module's project:
  http://drupal.org/project/i18n

Support questions by email to the module maintainer will be simply ignored. Use the issue tracker.

Now if you want professional (paid) support the module maintainer may be available occassionally.
Drop me a message to check availability and hourly rates, http://reyero.net/en/contact

====================================================================
Jose A. Reyero, drupal at reyero dot net, http://reyero.net

README.txt
==========
Drupal module: Path translation
==================================

This module provides some basic path translation feature for generic paths.

For paths belonging to objects that have translations, like nodes and taxonomy terms, the system can produce automatic
links for the language switcher.

For the rest of paths, this module allows to define which path is translation of which. Example:

1. We define a new 'path translation set' like
   - English: node/1
   - Spanish: taxonomy/term/3

2. Every time we are on any of these pages, the language switcher will point to the other path for each language.

This module is intended for translation of generic paths that don't have other way of being translated.

Note: path translations must be defined without aliases.

====================================================================
Jose A. Reyero, http://reyero.net
README.txt
==========
Drupal module: i18n_sync (Synchronization)

This module will handle content synchronization accross translations.

The available list of fields to synchronize will include standard node fields and cck fields.
To have aditional fields, add the list in a variable in the settings.php file, like this:

// Available fields for synchronization, for all node types.
$conf['i18n_sync_fields_node'] = array(
  'field1' => t('Field 1 name'),
  'field2' => t('Field 2 name'),
  ...
);

// More fields for a specific content type 'nodetype' only.
$conf['i18n_sync_fields_node_nodetype'] = array(
  'field3' => t('Field 3 name'),
   ...
);
README.txt
==========
Drupal module: Translation set API
==================================

This is a generic API to handle translation sets. It is being used for now
for path translation and taxonomy term translation inside i18n package.

Translation sets can hold a collection of entities or other objects. A translation set is itself
an Entity thus leveraging all the power of the Entity API.

It also provides some basic storage for translation sets and a generator of new translation set id.
However, each module is responsible for storing which objects belong to which translation set for which
it needs to verride some methods of the base i18n_translation_set class.

- load_translations()
- save_translations()
- clean_translations()
- delete_translations()

Once these are implemented, to get the objects belonging to a translation set, indexed by language code,
you can invoke this method on a translation set object:

- get_translations()

To define a new type of translation set, a module must implement hook_i18n_translation_set_info() 
as in this example:

/**
 * Implements hook_i18n_translation_set_info().
 */
function i18n_path_i18n_translation_set_info() {
  return array(
    'path' => array(
      'title' => t('Paths'),
      'class' => 'i18n_path_translation_set',
    )
  );
}

See examples of overriding and extending this API:
- i18n_path/i18n_path.inc
- i18n_taxonomy/i18n_taxonomy.inc

====================================================================
Jose A. Reyero, http://reyero.net
Drupal module: Variable API
===========================

Variable module will provide a registry for meta-data about Drupal variables.

Module Developers: Please declare your variables.

Why?
====
- So other modules can know about your module's variables and they can be translated, exported, etc.
- You'll get automatic variable edit forms, tokens, access control and uninstall for free. 

How?
====
Easy: Implement hook_variable_info();

/**
 * Implements hook_variable_info().
 */
function mymodule_variable_info($options) {

  $variable['mymodule_number'] = array(
    'title' => t('Magic number', array(), $options),
    'description' => t('Magic number, array(), $options),
    'type' => 'number',
    'access' => 'administer menus',
  );
 
  $variable['mymodule_name'] = array(
    'title' => t('Name', array(), $options),
    'description' => t('Enter your name, please.', array(), $options),
    'type' => 'string',
    'default' => t('Drupal user', array(), $options),
  );
  
  $variable['mymodule_mail'] = array(
    'title' => t('Mail'),
    'type' => 'mail_text',
    // This type will spawn into two real variables: mymodule_mail_subject, mymodule_mail_body
    // Everything, included the form elements, will be handled automatically
  );

  return $variable;
}  

Note: You can have your variables declared in a separate file that just will be loaded when needed.

      yourmodule.variable.inc

FAQ
===
  
- Will I need to add a dependency on the variable.module?

  Not neccessarily. Just if you want to enjoy some of the module's features advanced features like:
  - Getting variable values or defaults in different languages. Use variable_get_value().
  - Let other modules alter my variable defaults. Implement hook_variable_info_alter().
  - Let other modules know when variables are changed. Use variable_set_value(). Implement hook_variable_update().
  - Getting automatic forms for all the module's variables, a group of variables, etc..
  - Having variables with multiple values handled automatically like mail body and subject or variables for node types.
  
  Otherwise you can just provide the meta-data for other modules to use. You still get:
  - Tokens for your variables like [variable:myvariable_name]
  - Variables deleted automatically when the module is uninstalled
  - Localizable texts for your variables when using the Internationalization module.
  
- How do I get a form with all of my module's variables?
  
  drupal_get_form('variable_module_form', 'mymodule');
  
- Once I have declared a default for my variable, how can I benefit from it?
  
  variable_get_value('variable_name');
 
- What if I don't want to provide any administration form for my variables?

  That's ok, people will still be able to see and edit them by enabling the 'Variable Admin' module included.

  


Drupal module: Variable Realms
============================================
This is an API module that works as an arbitrator for multiple modules overriding global variables. It can
handle multiple realms defined by different modules. Examples: 'global', 'language', 'country',

Each realm has a weight and a current status. Realms with higher weights will override realms with lower weight.

There's a special 'global/default' realm that is the one storing default global variables. It has a weight of 0
so realms with weights higher than that (default weight for new realms is 10) will override these.

Any number of realms can be defined by different modules. If two modules use the same realm, the last one's variables
and weight will override the previous one. Every time we switch a realm, the $conf global array will be rebuilt.

At any moment the $conf global array of variables will be a combination of the active realms.
If we've got these two reamls defined:
 - global/default, weight 0, which is defined by this module, will hold global default variables
 - mymodule/key, weight 10, which may be defined by any contrib module on hook_boot() or hook_init()
The resulting variable set will be a combination of these two, with the second overriding the first one,
because of a higher weight. This is how we calculate the resulting variables when using variable_realm_switch()

 $conf = $variables['global/default'] + $variables['mymodule/key']

API Example
-----------
This is an example of how realms work:

// We add a language realm with some variables and immediately switch to it
  variable_realm_add('language', 'es', $spanish_variables);
  variable_realm_switch('language', 'es');

// We add a country realm on top of it with some more variables but don't switch to it yet.
// Note the first time we add a domain we can set the weight for it.

  variable_realm_add('country', 'spain', $spain_variables, 100);

// We add another country realm, but don't switch to it.
// The same weight from previous 'country' realm will be used

  variable_realm_add('country', 'mexico', $mexico_variables);

// Now we can switch to the 'spanish/spain' set of variables

  variable_realm_switch('country', 'spain');

// Or we can use the 'spanish/mexico' set

  variable_realm_switch('country', 'mexico');

// Still we can add one more realm which will override some variables for the current node's content type
// These will override all the others because of its higher weight
  variable_realm_add('nodetype', 'story', $story_variables, 200)
  variable_realm_switch('nodetype', 'story')

An example of a module using this API is Internationalization's i18n_variable module.

Variable Realm Union.
====================================

This an API that allows combining two existing realms into a new one
whose keys are a combination of the other two.

An example of this module in action is the 'Domain+I18n Variables Integration' module
which is part of 'Domain Variable' module.

How to use it.
=============
To define a new domain that is a combination of two or more existing ones:

1. Implement hook_variable_realm_info() to define the realm name and properties.

function domain_i18n_variable_variable_realm_info() {
  $realm['domain_language'] = array(
    'title' => t('Domain+Language'),
    // Display on settings forms but without form switcher.
    'form settings' => TRUE,
    'form switcher' => FALSE,
    'variable name' => t('multilingual domain'),
  );
  return $realm;
}

2. Implement hook_variable_realm_controller() to define the Controller class to
    be used and which other realms it is a combination of. Example:

function domain_i18n_variable_variable_realm_controller() {
  $realm['domain_language'] = array(
    'weight' => 200,
    'class' => 'VariableStoreRealmController',
    'union' => array('domain', 'language'),
  );
  return $realm;
}

Drupal module: Variable API Database storage
============================================
Provides database storage for realm variables.

This module provides some CRUD API to store and read your custom variables
and some _set() and _get() methods that are tightly integrated with Variable Realms

An example of a module using this API is Internationalization's i18n_variable module.# Composer Manager

[Composer Manager](https://drupal.org/project/composer_manager) provides a
gateway to the larger PHP community by enabling [Drupal](http://drupal.org)
modules to more easily use best-in-breed libraries that are managed by
[Composer](https://getcomposer.org/).

There are [many challenges](#why-cant-you-just--) when using Composer with
Drupal, so the primary goal of this module is to work around them by wrapping
Composer with common Drupal workflows so that module developers and site
builders can use the [thousands of standards-compliant, platform agnostic PHP
libraries](https://packagist.org/statistics) with as little friction as
possible.

## Installation

* Follow the standard [Drupal module installation](https://drupal.org/documentation/install/modules-themes)
  process
* Refer to the [Maintaining Dependencies](#maintaining-dependencies)
  section for installing and updating third-party libraries required by
  contributed modules
* Refer to the [Best Practices](#best-practices) section for recommended module
  configurations according to your environment

## Usage For Site Builders

### Maintaining Dependencies

As modules are enabled and disabled, Composer Manager gathers their requirements
and generates a consolidated `composer.json` file in the "Composer File
Directory" as configured in Composer Manager's settings page. There are two ways
to install and update the contributed modules' dependencies:

#### Automatically With Drush (Recommended)

Using `drush en` and `drush dis` to enable and disable modules respectively will
automatically generate the consolidated `composer.json` file and run the
appropriate Composer commands to install and update the required dependencies.

This technique introduces the least amount of friction with existing workflows
and is strongly recommended.

The following Drush commands are also available:

* `drush composer-json-rebuild`: Force a rebuild of the consolidated
  `composer.json` file
* `drush composer-manager [COMMAND] [OPTIONS]`: Pass through commands to
  Composer, refer to the [cli tool's documentation](https://getcomposer.org/doc/03-cli.md)
  for available commands and options.

#### Manually With Composer

If you do not wish to use Drush, you must manually use Composer's command line
tool to install and update dependencies whenever modules are enabled or
disabled. The following steps illustrate the workflow to maintain the
dependencies required by contributed module:

* Visit `admin/modules` and enable / disable the modules that have dependencies
* Change into the the "Composer File Directory" as configured in Composer
  Manager's settings page which is where the consolidated `composer.json` file
  was generated
* If necessary, [download and install](https://github.com/composer/composer/blob/master/doc/01-basic-usage.md#installation)
  the Composer tool
* Run `php composer.phar install --no-dev` on the command line, replace
  `install` with `update` when updating dependencies

Refer to [Composer's documentaton](https://getcomposer.org/doc/) for more
details on how Composer works.

### Configuring Composer Manager

Visit `admin/config/system/composer-manager/settings` for Drupal 7 & 8 or
`admin/settings/composer-manager/settings` for Drupal 6 as a user with the
`administer site configuration` permission to configure Composer Manager.

### Best Practices

Unfortunately there is arguably no 80% use case that guides sane defaults. Site
builders will likely have to configure Composer Manager according to their
environment, so this section outlines best practices and techniques to help
guide a sustainable, reliable installation.

#### Recommended Settings

It is recommended to maintain a project structure where the composer files and
`vendor/` directory exist alongside the document root. This can be achieved by
modifying the following options in Composer Manager's settings page.

* Vendor Directory: `../vendor`
* Composer File Directory: `../`

You can also set the options in settings.php by adding the following variables:

```php
// Drupal 6 & 7

$conf['composer_manager_vendor_dir'] = '../vendor';
$conf['composer_manager_file_dir'] = '../';
```

```php
// Drupal 8

$config['composer_manager.settings']['vendor_dir'] = '../vendor';
$config['composer_manager.settings']['file_dir'] = '../';
```

*NOTE:* The recommended settings are not the defaults because we cannot assume
that this structure is viable for all use cases. Furthermore, the "Composer File
Directory" is set to a path we know is writable by the web server so the
automatic building of `composer.json` works out of the box.

#### Multisite

It is recommended that each multisite installation has its own library space
since the dependencies are tied to which modules are enabled or disabled and
can differ between sites. Add the following snippet to `settings.php` to group
the libraries by site in a directory outside of the document root:

```php
// Drupal 6 & 7

// Capture the site dir, e.g. "default", "example.localhost", etc.
$site_dir = basename(__DIR__);
$conf['composer_manager_vendor_dir'] = '../lib/' . $site_dir . '/vendor';
$conf['composer_manager_file_dir'] = '../lib/' . $site_dir;
```

```php
// Drupal 8

// Capture the site dir, e.g. "default", "example.localhost", etc.
$site_dir = basename(__DIR__);
$config['composer_manager.settings']['vendor_dir'] = '../lib/' . $site_dir . '/vendor';
$config['composer_manager.settings']['file_dir'] = '../lib/' . $site_dir;
```

*NOTE:* The `sites/*/` directories may seem like an obvious location for the
libraries, however Drupal removes write permissions to these directories on
every page load which can cause frustration.

#### Production Environments

Dependencies should be managed in development environments and not in production.
Therefore it is recommended to disable the checkboxes that automatically build
the composer.json file and run Composer commands when enabling or disabling
modules on production environments.

Assuming that you can detect whether the site is in production mode via an
environment variable, adding the following snippet to `settings.php` will
disable the options where appropriate:

```php
// Drupal 6 & 7

// Modify the logic according to your environment.
if (getenv('APP_ENV') == 'prod') {
  $conf['composer_manager_autobuild_file'] = 0;
  $conf['composer_manager_autobuild_packages'] = 0;
}
```

```php
// Drupal 8

// Modify the logic according to your environment.
if (getenv('APP_ENV') == 'prod') {
  $config['composer_manager.settings']['autobuild_file'] = 0;
  $config['composer_manager.settings']['autobuild_packages'] = 0;
}
```

## Usage For Module Maintainers

Module maintainers can use Composer Manager to maintain their dependencies by
creating a `composer.json` file in the module's root directory and adding the
appropriate requirements. Refer to [Composer's documentation](https://getcomposer.org/doc/01-basic-usage.md#composer-json-project-setup)
for details on adding requirements.

It is recommended to use [version ranges](https://getcomposer.org/doc/01-basic-usage.md#package-versions)
and [tilde operators](https://getcomposer.org/doc/01-basic-usage.md#next-significant-release-tilde-operator-)
wherever possible to mitigate dependency conflicts.

You can also implement `hook_composer_json_alter(&$json)` to modify the data
used to build the consolidated `composer.json` file before it is written.

### Requiring Full Symfony, Zend Framework Packages(D8 Only)

If your module requires or has a dependency on `symfony/symfony` or
`zendframework/zendframework` you need to take one of the
following actions to avoid duplicate code and potential version mismatches:

* Depend on the `symfony_dependency` or `zendframework_dependency` modules as
  appropriate
* Implement `hook_composer_json_alter()` and perform the same modifications as
  the appropriate "*_dependency" module

A detailed description of why these actions are necessary can be found at
https://drupal.org/comment/8528371#comment-8528371. The discussion afterwards
provides the barriers and rationale that guided the current solution.

*NOTE:* You ONLY have to take the actions above when requiring the full Symfony
or Zend Framework packages and NOT when requiring their components e.g.
`symfony/filesystem`.

### Maintaining A Soft Dependency On Composer Manager

@todo

### Accessing The ClassLoader Object

Once the autoloader is registered, you can retrieve the ClassLoader object by
calling `\ComposerAutoloaderInitComposerManager::getLoader()`. The following
example uses this technique with Doctrine's Annotations library which requires
access to the loader object.

```php

use Doctrine\Common\Annotations\AnnotationRegistry;

$loader = \ComposerAutoloaderInitComposerManager::getLoader();
AnnotationRegistry::registerLoader(array($loader, 'loadClass'));

```

### Relying on composer manager in .install

Composer manager will automatically handle the autoloader in `hook_init()`, so
modules generally don't have to worry about triggering the autoloader. However
there are occasions where `hook_init()` isn't invoked such as during install and
update.php. If you rely on the autoloader in a .install file, you have to make
sure the autoloader is triggered by running
`composer_manager_register_autoloader()` at the beginning of your update
function or your `hook_install()` implementation.

## Why can't you just ... ?

The problems that Composer Manager solves tend to be more complex than they
first appear. This section addresses some of the common questions that are asked
as to why Composer Manager works the way it does.

### Why can't you just run "composer install" in each module's root directory?

If a module contains a `composer.json` file, running `composer install` in its
root directory will download all requirements and dependencies to `vendor/`
directories with their own autoloaders. Relying on this technique poses multiple
challenges:

* Duplicate library code when modules have the same dependencies
* Unexpected classes being sourced depending on which autoloader is registered
  first
* Potential version conflicts that aren't detected since each installation is
  run in isolation

To highlight the challenges, let's say `module_a` requires
`"guzzle/http": "3.7.*"` and `module_b` requires `"guzzle/service": ">=3.7.0"`.
At the time of this post, running `composer install` in each module's directory
will result in version 3.7.4 of `guzzle/http` being installed in `module_a`'s
`vendor/` directory and version 3.8.1 of `guzzle/service` being installed in
`module_b`'s `vendor/` directory.

Because `guzzle/service` depends on `guzzle/http`, you now have duplicate
installs of `guzzle/http`. Furthermore, each installation uses different
versions of the `guzzle/http` component (3.7.4 for `module_a` and 3.8.1 for
`module_b`). If `module_a`'s autoloader is registered first then you have a
situation where version 3.8.1 of `\Guzzle\Service\Client` extends version 3.7.4
of `\Guzzle\Http\Client`.

#### Composer Manager's Solution

Composer Manager finds all `composer.json` files in each enabled module's root
directory and attempts to gracefully merge them into a consolidated
`composer.json` file. This results in a single vendor directory shared across
all modules which prevents code duplication and version mismatches. For the use
case above, Composer will resolve both `guzzle/http` and `guzzle/service` to
version 3.7.4 which is a more consistent, reliable environment.

#### Challenges With Composer Manager

The challenge of Composer Manager's technique is when multiple modules require
different version of the same package, e.g. `"guzzle/http": "3.7.*"` and
`"guzzle/http": "3.8.*"`. Composer Manager will use the version defined in the
`composer.json` file that is associated with the module with the heaviest weight.
Composer Manager will also flag the potential version conflict in the UI so the
site builder is aware of the inconsistency.

The story at https://drupal.org/node/1931200 aims to provide manual resolution
via the UI, and in the future projects such as
https://github.com/dflydev/dflydev-embedded-composer might provide a better
solution to eliminate the need for a merging strategy in Composer Manager.

### Why can't you just manually maintain a composer.json file?

Manually maintaining a `composer.json` file provides a single library space that
all modules can share, however relying on this technique poses multiple
challenges:

* Site builder responsible for updating file when modules are enabled or updated
* Dependencies are decoupled from the module's codebase
* Multiple files must be maintained for each multisite installation

#### Composer Manager's Solution

Composer Manager automatically generates the `composer.json` file when modules
are enabled and disabled, and there is an option in the UI with a corresponding
Drush command that can rebuild the consolidated `composer.json` file on demand.
Furthermore, using a Drush based workflow will automatically run the appropriate
composer commands whenever modules are enabled or disabled, so the need to run
Composer commands outside of normal workflows is reduced to module updates.

For Drupal 8, Composer Manager also prevents the packages included in Drupal
core from being installed in the contributed vendor directory. It also ensures
that the dependencies are compatible with the versions included in Drupal core.
For example, if a module requires `"guzzle/service": "~3.0"`, version 3.7.1 will
be installed which is the version of the Guzzle components in core that
`guzzle/service` depends on.

@todo Provide technical details, reference https://drupal.org/node/2128353

#### Challenges With Composer Manager

There are multiple challenges posed by Composer Manager's technique:

* Web server needs write access to the composer file directory
* Sane multisite configuration requires environment-specific `settings.php`
  configurations
* Must implement `hook_composer_json_alter()` in a module to modify
  `composer.json`

### Why can't you just modify Drupal core's composer.json file (D8 Only)?

Modifying Drupal core's `composer.json` file provides a single library space and
uses the autoloader that is registered in index.php. Relying on this technique
poses multiple challenges:

* Difficult to manage Drupal upgrades that have package updates
* Site builder responsible for updating file when modules are enabled or updated
* Dependencies are decoupled from the module's codebase
* Challenging in multisite environments where different packages / version are
  required

#### Composer Manager's Solution

Refer to the [Why can't you just manually maintain a composer.json file?](#composer-managers-solution-1)
section.

#### Challenges With Composer Manager

Refer to the [Why can't you just manually maintain a composer.json file?](#challenges-with-composer-manager-1)
section.
Search API
----------

This module provides a framework for easily creating searches on any entity
known to Drupal, using any kind of search engine. For site administrators, it is
a great alternative to other search solutions, since it already incorporates
facetting support and the ability to use the Views module for displaying search
results, filters, etc. Also, with the Apache Solr integration [1], a
high-performance search engine is available for use with the Search API.

If you need help with the module, please post to the project's issue queue [2].

[1] http://drupal.org/project/search_api_solr
[2] http://drupal.org/project/issues/search_api


Content:
 - Glossary
 - Information for users
 - Information for developers
 - Included components


Glossary
--------

Terms as used in this module.

- Service class:
  A type of search engine, e.g. using the database, Apache Solr,
  Sphinx or any other professional or simple indexing mechanism. Takes care of
  the details of all operations, especially indexing or searching content.
- Server:
  One specific place for indexing data, using a set service class. Can
  e.g. be some tables in a database, a connection to a Solr server or other
  external services, etc.
- Index:
  A configuration object for indexing data of a specific type. What and how data
  is indexed is determined by its settings. Also keeps track of which items
  still need to be indexed (or re-indexed, if they were updated). Needs to lie
  on a server in order to be really used (although configuration is independent
  of a server).
- Item type:
  A type of data which can be indexed (i.e., for which indexes can be created).
  Most entity types (like Content, User, Taxonomy term, etc.) are available, but
  possibly also other types provided by contrib modules.
- Entity:
  One object of data, usually stored in the database. Might for example
  be a node, a user or a file.
- Field:
  A defined property of an entity, like a node's title or a user's mail address.
  All fields have defined datatypes. However, for indexing purposes the user
  might choose to index a property under a different data type than defined.
- Data type:
  Determines how a field is indexed. While "Fulltext" fields can be completely
  searched for keywords, other fields can only be used for filtering. They will
  also be converted to fit their respective value ranges.
  How types other than "Fulltext" are handled depends on the service class used.
  Its documentation should state how the type-selection affect the indexed
  content. However, service classes will always be able to handle all data
  types, it is just possible that the type doesn't affect the indexing at all
  (apart from "Fulltext vs. the rest").
- Boost:
  Number determining how important a certain field is, when searching for
  fulltext keywords. The higher the value is, the more important is the field.
  E.g., when the node title has a boost of 5.0 and the node body a boost of 1.0,
  keywords found in the title will increase the score as much as five keywords
  found in the body. Of course, this has only an effect when the score is used
  (for sorting or other purposes). It has no effect on other parts of the search
  result.
- Data alteration:
  A component that is used when indexing data. It can add additional fields to
  the indexed entity or prevent certain entities from being indexed. Fields
  added by callbacks have to be enabled on the "Fields" page to be of any use,
  but this is done by default.
- Processor:
  An object that is used for preprocessing indexed data as well as search
  queries, and for postprocessing search results. Usually only work on fulltext
  fields to control how content is indexed and searched. E.g., processors can be
  used to make searches case-insensitive, to filter markup out of indexed
  content, etc.


Information for users
---------------------

IMPORTANT: Access checks
  In general, the Search API doesn't contain any access checks for search
  results. It is your responsibility to ensure that only accessible search
  results are displayed – either by only indexing such items, or by filtering
  appropriately at search time.
  For search on general site content (item type "Node"), this is already
  supported by the Search API. To enable this, go to the index's "Filters" tab
  and activate the "Node access" data alteration. This will add the necessary
  field, "Node access information", to the index (which you have to leave as
  "indexed"). If both this field and "Published" are set to be indexed, access
  checks will automatically be executed at search time, showing only those
  results that a user can view. Some search types (e.g., search views) also
  provide the option to disable these access checks for individual searches.
  Please note, however, that these access checks use the indexed data, while
  usually the current data is displayed to users. Therefore, users might still
  see inappropriate content as long as items aren't indexed in their latest
  state. If you can't allow this for your site, please use the index's "Index
  immediately" feature (explained below) or possibly custom solutions for
  specific search types, if available.

As stated above, you will need at least one other module to use the Search API,
namely one that defines a service class (e.g., search_api_db ("Database search")
which can be found at [3]).

[3] http://drupal.org/project/search_api_db

- Creating a server
  (Configuration > Search API > Add server)

The most basic thing you have to create is a search server for indexing content.
Go to Configuration > Search API in the administration pages and select
"Add server". Name and description are usually only shown to administrators and
can be used to differentiate between several servers, or to explain a server's
use to other administrators (for larger sites). Disabling a server makes it
unusable for indexing and searching and can e.g. be used if the underlying
search engine is temporarily unavailable.
The "service class" is the most important option here, since it lets you select
which backend the search server will use. This cannot be changed after the
server is created.
Depending on the selected service class, further, service-specific settings will
be available. For details on those settings, consult the respective service's
documentation.

- Creating an index
  (Configuration > Search API > Add index)

For adding a search index, choose "Add index" on the Search API administration
page. Name, description and "enabled" status serve the exact same purpose as
for servers.
The most important option in this form is the indexed entity type. Every index
contains data on only a single type of entities, e.g. nodes, users or taxonomy
terms. This is therefore the only option that cannot be changed afterwards.
The server on which the index lies determines where the data will actually be
indexed. It doesn't affect any other settings of the index and can later be
changed with the only drawback being that the index' content will have to be
indexed again. You can also select a server that is at the moment disabled, or
choose to let the index lie on no server at all, for the time being. Note,
however, that you can only create enabled indexes on an enabled server. Also,
disabling a server will disable all indexes that lie on it.
The "Index items immediately" option specifies that you want items to be
directly re-indexed after being changed, instead of waiting for the next cron
run. Use this if it is important that users see no stale data in searches, and
only when your setup enables relatively fast indexing.
Lastly, the "Cron batch size" option allows you to set whether items will be
indexed when cron runs (as long as the index is enabled), and how many items
will be indexed in a single batch. The best value for this setting depends on
how time-consuming indexing is for your setup, which in turn depends mostly on
the server used and the enabled data alterations. You should set it to a number
of items which can easily be indexed in 10 seconds' time. Items can also be
indexed manually, or directly when they are changed, so even if this is set to
0, the index can still be used.

- Indexed fields
  (Configuration > Search API > [Index name] > Fields)

Here you can select which of the entities' fields will be indexed, and how.
Fields added by (enabled) data alterations will be available here, too.
Without selecting fields to index, the index will be useless and also won't be
available for searches. Select the "Fulltext" data type for fields which you
want search for keywords, and other data types when you want to use the field
for filtering (e.g., as facets). The "Item language" field will always be
indexed as it contains important information for processors and hooks.
You can also add fields of related entities here, via the "Add related fields"
form at the bottom of the page. For instance, you might want to index the
author's username to the indexed data of a node, and you need to add the "Body"
entity to the node when you want to index the actual text it contains.

- Indexing workflow
  (Configuration > Search API > [Index name] > Filters)

This page lets you customize how the created index works, and what metadata will
be available, by selecting data alterations and processors (see the glossary for
further explanations).
Data alterations usually only add one or more fields to the entity and their
order is mostly irrelevant.
The order of processors, however, often is important. Read the processors'
descriptions or consult their documentation for determining how to use them most
effectively.

- Index status
  (Configuration > Search API > [Index name] > Status)

On this page you can view how much of the entities are already indexed and also
control indexing. With the "Index now" button (displayed only when there are
still unindexed items) you can directly index a certain number of "dirty" items
(i.e., items not yet indexed in their current state). Setting "-1" as the number
will index all of those items, similar to the cron batch size setting.
When you change settings that could affect indexing, and the index is not
automatically marked for re-indexing, you can do this manually with the
"Re-index content" button. All items in the index will be marked as dirty and be
re-indexed when subsequently indexing items (either manually or via cron runs).
Until all content is re-indexed, the old data will still show up in searches.
This is different with the "Clear index" button. All items will be marked as
dirty and additionally all data will be removed from the index. Therefore,
searches won't show any results until items are re-indexed, after clearing an
index. Use this only if completely wrong data has been indexed. It is also done
automatically when the index scheme or server settings change too drastically to
keep on using the old data.

- Hidden settings

search_api_index_worker_callback_runtime:
  By changing this variable, you can determine the time (in seconds) the Search
  API will spend indexing (for all indexes combined) in each cron run. The
  default is 15 seconds.


Information for developers
--------------------------

 | NOTE:
 | For modules providing new entities: In order for your entities to become
 | searchable with the Search API, your module will need to implement
 | hook_entity_property_info() in addition to the normal hook_entity_info().
 | hook_entity_property_info() is documented in the entity module.
 | For making certain non-entities searchable, see "Item type" below.
 | For custom field types to be available for indexing, provide a
 | "property_type" key in hook_field_info(), and optionally a callback at the
 | "property_callbacks" key.
 | Both processes are explained in [4].
 |
 | [4] http://drupal.org/node/1021466

Apart from improving the module itself, developers can extend search
capabilities provided by the Search API by providing implementations for one (or
several) of the following classes. Detailed documentation on the methods that
need to be implemented are always available as doc comments in the respective
interface definition (all found in their respective files in the includes/
directory). The details for hooks can be looked up in the search_api.api.php
file. Note that all hooks provided by the Search API use the "search_api" hook
group. Therefore, implementations of the hook can be moved into a
MODULE.search_api.inc file in your module's directory.
For all interfaces there are handy base classes which can (but don't need to) be
used to ease custom implementations, since they provide sensible generic
implementations for many methods. They, too, should be documented well enough
with doc comments for a developer to find the right methods to override or
implement.

- Service class
  Interface: SearchApiServiceInterface
  Base class: SearchApiAbstractService
  Hook: hook_search_api_service_info()

The service classes are the heart of the API, since they allow data to be
indexed on different search servers. Since these are quite some work to get
right, you should probably make sure a service class for a specific search
engine doesn't exist already before programming it yourself.
When your module supplies a service class, please make sure to provide
documentation (at least a README.txt) that clearly states the datatypes it
supports (and in what manner), how a direct query (a query where the keys are
a single string, instead of an array) is parsed and possible limitations of the
service class.
The central methods here are the indexItems() and the search() methods, which
always have to be overridden manually. The configurationForm() method allows
services to provide custom settings for the user.
See the SearchApiDbService class provided by [5] for an example implementation.

[5] http://drupal.org/project/search_api_db

- Query class
  Interface: SearchApiQueryInterface
  Base class: SearchApiQuery

You can also override the query class' behaviour for your service class. You
can, for example, change key parsing behaviour, add additional parse modes
specific to your service, or override methods so the information is stored more
suitable for your service.
For the query class to become available (other than through manual creation),
you need a custom service class where you override the query() method to return
an instance of your query class.

- Item type
  Interface: SearchApiDataSourceControllerInterface
  Base class: SearchApiAbstractDataSourceController
  Hook: hook_search_api_item_type_info()

If you want to index some data which is not defined as an entity, you can
specify it as a new item type here. For defining a new item type, you have to
create a data source controller for the type and track new, changed and deleted
items of the type by calling the search_api_track_item_*() functions.
An instance of the data source controller class will then be used by indexes
when handling items of your newly-defined type.

If you want to make external data that is indexed on some search server
available to the Search API, there is a handy base class for your data source
controller (SearchApiExternalDataSourceController in
includes/datasource_external.inc) which you can extend. For a minimal use case,
you will then only have to define the available fields that can be retrieved by
the server.

- Data type
  Hook: hook_search_api_data_type_info()

You can specify new data types for indexing fields. These new types can then be
selected on indexes' „Fields“ tabs. You just have to implement the hook,
returning some information on your data type, and specify in your module's
documentation the format of your data type and how it should be used.

For a custom data type to have an effect, in most cases the server's service
class has to support that data type. A service class can advertize its support
of a data type by declaring support for the "search_api_data_type_TYPE" feature
in its supportsFeature() method. If this support isn't declared, a fallback data
type is automatically used instead of the custom one.

If a field is indexed with a custom data type, its entry in the index's options
array will have the selected type in "real_type", while "type" contains the
fallback type (which is always one of the default data types, as returned by
search_api_default_field_types().

- Data-alter callbacks
  Interface: SearchApiAlterCallbackInterface
  Base class: SearchApiAbstractAlterCallback
  Hook: hook_search_api_alter_callback_info()

Data alter callbacks can be used to change the field data of indexed items, or
to prevent certain items from being indexed. They are only used when indexing,
or when selecting the fields to index. For adding additional information to
search results, you have to use a processor.
Data-alter callbacks are called "data alterations" in the UI.

- Processors
  Interface: SearchApiProcessorInterface
  Base class: SearchApiAbstractProcessor
  Hook: hook_search_api_processor_info()

Processors are used for altering the data when indexing or searching. The exact
specifications are available in the interface's doc comments. Just note that the
processor description should clearly state assumptions or restrictions on input
types (e.g. only tokenized text), item language, etc. and explain concisely what
effect it will have on searches.
See the processors in includes/processor.inc for examples.


Included components
-------------------

- Data alterations

  * URL field
    Provides a field with the URL for displaying the entity.
  * Aggregated fields
    Offers the ability to add additional fields to the entity, containing the
    data from one or more other fields. Use this, e.g., to have a single field
    containing all data that should be searchable, or to make the text from a
    string field, like a taxonomy term, also fulltext-searchable.
    The type of aggregation can be selected from a set of values: you can, e.g.,
    collect the text data of all contained fields, or add them up, count their
    values, etc.
  * Bundle filter
    Enables the admin to prevent entities from being indexed based on their
    bundle (content type for nodes, vocabulary for taxonomy terms, etc.).
  * Complete entity view
    Adds a field containing the whole HTML content of the entity as it is viewed
    on the site. The view mode used can be selected.
    Note, however, that this might not work for entities of all types. All core
    entities except files are supported, though.
  * Index hierarchy
    Allows to index a hierarchical field along with all its parents. Most
    importantly, this can be used to index taxonomy term references along with
    all parent terms. This way, when an item, e.g., has the term "New York", it
    will also be matched when filtering for "USA" or "North America".

- Processors

  * Ignore case
    Makes all fulltext searches (and, optionally, also filters on string values)
    case-insensitive. Some servers might do this automatically, for others this
    should probably always be activated.
  * HTML filter
    Strips HTML tags from fulltext fields and decodes HTML entities. If you are
    indexing HTML content (like node bodies) and the search server doesn't
    handle HTML on its own, this should be activated to avoid indexing HTML
    tags, as well as to give e.g. terms appearing in a heading a higher boost.
  * Tokenizer
    This processor allows you to specify how indexed fulltext content is split
    into seperate tokens – which characters are ignored and which treated as
    white-space that seperates words.
  * Stopwords
    Enables the admin to specify a stopwords file, the words contained in which
    will be filtered out of the text data indexed. This can be used to exclude
    too common words from indexing, for servers not supporting this natively.

- Additional modules

  * Search views
    This integrates the Search API with the Views module [6], enabling the user
    to create views which display search results from any Search API index.
  * Search facets
    For service classes supporting this feature (e.g. Solr search), this module
    automatically provides configurable facet blocks on pages that execute
    a search query.

[6] http://drupal.org/project/views
Search facets
-------------

This module allows you to create facetted searches for any search executed via
the Search API, no matter if executed by a search page, a view or any other
module. The only thing you'll need is a search service class that supports the
"search_api_facets" feature. Currently, the "Database search" and "Solr search"
modules supports this.

This module is built on the Facet API [1], which is needed for this module to
work.

[1] http://drupal.org/project/facetapi


Information for site builders
-----------------------------

For creating a facetted search, you first need a search. Create or find some
page displaying Search API search results, either via a search page, a view or
by any other means. Now go to the configuration page for the index on which
this search is executed.
If the index lies on a server supporting facets (and if this module is enabled),
you'll notice a "Facets" tab. Click it and it will take you to the index' facet
configuration page. You'll see a table containing all indexed fields and options
for enabling and configuring facets for them.
For a detailed explanation of the available options, please refer to the Facet
API documentation.

- Creating facets via the URL

Facets can be added to a search (for which facets are activated) by passing
appropriate GET parameters in the URL. Assuming you have an indexed field with
the machine name "field_price", you can filter on it in the following ways:

- Filter for a specific value. For finding only results that have a price of
  exactly 100, pass the following $options to url() or l():

  $options['query']['f'][] = 'field_price:100';

  Or manually append the following GET parameter to a URL:

  ?f[0]=field_price:100

- Search for values in a specified range. The following example will only return
  items that have a price greater than or equal to 100 and lower than 500.

  Code: $options['query']['f'][] = 'field_price:[100 TO 500]';
  URL:  ?f[0]=field_price%3A%5B100%20TO%20500%5D

- Search for values above a value. The next example will find results which have
  a price greater than or equal to 100. The asterisk (*) stands for "unlimited",
  meaning that there is no upper limit. Filtering for values lower than a
  certain value works equivalently.

  Code: $options['query']['f'][] = 'field_price:[100 TO *]';
  URL:  ?f[0]=field_price%3A%5B100%20TO%20%2A%5D

- Search for missing values. This example will filter out all items which have
  any value at all in the price field, and will therefore only list items on
  which this field was omitted. (This naturally only makes sense for fields
  that aren't required.)

  Code: $options['query']['f'][] = 'field_price:!';
  URL:  ?f[0]=field_price%3A%21

- Search for present values. The following example will only return items which
  have the price field set (regardless of the actual value). You can see that it
  is actually just a range filter with unlimited lower and upper bound.

  Code: $options['query']['f'][] = 'field_price:[* TO *]';
  URL:  ?f[0]=field_price%3A%5B%2A%20TO%20%2A%5D

Note: When filtering a field whose machine name contains a colon (e.g.,
"author:roles"), you'll have to additionally URL-encode the field name in these
filter values:
  Code: $options['query']['f'][] = rawurlencode('author:roles') . ':100';
  URL:  ?f[0]=author%253Aroles%3A100

- Issues

If you find any bugs or shortcomings while using this module, please file an
issue in the project's issue queue [1], using the "Facets" component.

[1] http://drupal.org/project/issues/search_api


Information for developers
--------------------------

- Features

If you are the developer of a SearchApiServiceInterface implementation and want
to support facets with your service class, too, you'll have to support the
"search_api_facets" feature. You can find details about the necessary additions
to your class in the example_servive.php file. In short, you'll just, when
executing a query, have to return facet terms and counts according to the
query's "search_api_facets" option, if present.
In order for the module to be able to tell that your server supports facets,
you will also have to change your service's supportsFeature() method to
something like the following:
  public function supportsFeature($feature) {
    return $feature == 'search_api_facets';
  }

There is also a second feature defined by this module, namely
"search_api_facets_operator_or", for supporting "OR" facets. The requirements
for this feature are also explained in the example_servive.php file.

- Query option

The facets created follow the "search_api_base_path" option on the search query.
If set, this path will be used as the base path from which facet links will be
created. This can be used to show facets on pages without searches – e.g., as a
landing page.

- Hidden variable

The module uses one hidden variable, "search_api_facets_search_ids", to keep
track of the search IDs of searches executed for a given index. It is only
updated when a facet is displayed for the respective search, so isn't really a
reliable measure for this.
In any case, if you e.g. did some test searches and now don't want them to show
up in the block configuration forever after, just clear the variable:
  variable_del("search_api_facets_search_ids")
Search API Views integration
----------------------------

This module integrates the Search API with the popular Views module [1],
allowing users to create views with filters, arguments, sorts and fields based
on any search index.

[1] http://drupal.org/project/views

"More like this" feature
------------------------
This module defines the "More like this" feature (feature key: "search_api_mlt")
that search service classes can implement. With a server supporting this, you
can use the „More like this“ contextual filter to display a list of items
related to a given item (usually, nodes similar to the node currently viewed).

For developers:
A service class that wants to support this feature has to check for a
"search_api_mlt" option in the search() method. When present, it will be an
array containing two keys:
- id: The entity ID of the item to which related items should be searched.
- fields: An array of indexed fields to use for testing the similarity of items.
When these are present, the normal keywords should be ignored and the related
items be returned as results instead. Sorting, filtering and range restriction
should all work normally.

"Facets block" display
----------------------
Most features should be clear to users of Views. However, the module also
provides a new display type, "Facets block", that might need some explanation.
This display type is only available, if the „Search facets“ module is also
enabled.

The basic use of the block is to provide a list of links to the most popular
filter terms (i.e., the ones with the most results) for a certain category. For
example, you could provide a block listing the most popular authors, or taxonomy
terms, linking to searches for those, to provide some kind of landing page.

Please note that, due to limitations in Views, this display mode is shown for
views of all base tables, even though it only works for views based on Search
API indexes. For views of other base tables, this will just print an error
message.
The display will also always ignore the view's "Style" setting, selected fields
and sorts, etc.

To use the display, specify the base path of the search you want to link to
(this enables you to also link to searches that aren't based on Views) and the
facet field to use (any indexed field can be used here, there needn't be a facet
defined for it). You'll then have the block available in the blocks
administration and can enable and move it at leisure.
Note, however, that the facet in question has to be enabled for the search page
linked to for the filter to have an effect.

Since the block will trigger a search on pages where it is set to appear, you
can also enable additional „normal“ facet blocks for that search, via the
„Facets“ tab for the index. They will automatically also point to the same
search that you specified for the display.
If you want to use only the normal facets and not display anything at all in
the Views block, just activate the display's „Hide block“ option.

Note: If you want to display the block not only on a few pages, you should in
any case take care that it isn't displayed on the search page, since that might
confuse users.

Access features
---------------
Search views created with this module contain two query settings (located in
the "Advanced" fieldset) which let you control the access checks executed for
search results displayed in the view.

- Bypass access checks
This option allows you to deactivate access filters that would otherwise be
added to the search, if the index supports this. This is, for instance, the case
for indexes on the "Node" item type, when the "Node access" data alteration is
activated.
Use this either to slightly speed up searches where additional checks are
unnecessary (e.g., because you already filter on "Node: Published") and there is
no other node access mechanism on your site) or to show certain data that users
normally wouldn't have access to (e.g., a list of all matching node titles,
published or not).

- Additional access checks on result entities
When this option is activated, all result entities will be passed to an
additional access check, even if search-time access checks are available for
this index. The advantage is that access rules are guaranteed to be enforced –
stale data in the index, which might make other access checks incorrect, won't
influence this access check. You can also use it for item types for which no
other access mechanisms are available.
However, note that results filtered out this way will mess up paging, result
counts and possibly other things too (like facet counts), as the result row is
only hidden from display after the search has been executed. Where possible,
you should therefore only use this in combination with appropriate filter
settings ensuring that only when the index isn't up-to-date items will be
filtered out this way.
This option is only available for indexes on entity types.

Other features
--------------
- Change parse mode
You can determine how search keys entered by the user will be parsed by going to
"Advanced" > "Query settings" within your View's settings. "Direct" can be
useful, e.g., when you want to give users the full power of Solr. In other
cases, "Multiple terms" is usually what you want / what users expect.
Caution: For letting users use fulltext searches, always use the "Search:
Fulltext search" filter or contextual filter – using a normal filter on a
fulltext field won't parse the search keys, which means multiple words will only
be found when they appear as that exact phrase.

FAQ: Why „*Indexed* Node“?
--------------------------
The group name used for the search result itself (in fields, filters, etc.) is
prefixed with „Indexed“ in order to be distinguishable from fields on referenced
nodes (or other entities). The data displayed normally still comes from the
entity, not from the search index.
INFORMATION FOR DEVELOPERS

Once the Date API is installed, all functions in the API are available to be
used anywhere by any module.

The API uses the PHP 5.2 date functions to create and manipulate dates.

Example, the following will create a date for the local value in one
timezone, adjust it to a different timezone, then return the offset in seconds
in the new timezone for the input date; The offset will be adjusted for both
the timezone difference and daylight savings time, if necessary:

$date = date_create('2007-03-11 02:00:00', timezone_open('America/Chicago'));
$chicago_time = date_format($date, 'Y-m-d H:i');

print 'At '. $chicago_time .' in Chicago, the timezone offset in seconds
  was '. date_offset_get($date);

date_timezone_set($date, timezone_open('Europe/Berlin');
$berlin_time = date_format($date, 'Y-m-d H:i');

print 'It was '. $berlin_time .' in Berlin when it
  was '. $chicago_time .' in Chicago.';
print 'At that time in Berlin, the timezone offset in seconds was
  '. date_offset_get($date);

A helper class is available, new DateObject($string, $timezone, $format), where
$string is a unixtimestamp, an ISO date, or a string like YYYY-MM-DD HH:MM:SS,
$timezone is the name of the timezone this date is in, and $format is the format
of date it is (DATE_FORMAT_UNIX, DATE_FORMAT_ISO, or DATE_FORMAT_DATETIME). It
creates and return a date object set to the right date and timezone.

Simpletest tests for these functions are included in the package.

Available functions include the following (more documentation is provided in
the files):

============================================================================
Preconfigured arrays
============================================================================
Both translated and untranslated values are available. The
date_week_days_ordered() function will shift an array of week day names so it
starts with the site's first day of the week, otherwise the weekday names start
with Sunday as the first value, which is the expected order for many php and sql
functions.

date_month_names();
date_month_names_abbr();
date_month_names_untranslated();
date_week_days();
date_week_days_abbr();
date_week_days_untranslated();
date_week_days_ordered();
date_years();
date_hours();
date_minutes();
date_seconds();
date_timezone_names();
date_ampm();

============================================================================
Miscellaneous date manipulation functions
============================================================================
Pre-defined constants and functions that will handle pre-1970 and post-2038
dates in both PHP 4 and PHP 5, in any OS. Dates can be converted from one
type to another and date parts can be extracted from any date type.

DATE_DATETIME
DATE_ISO
DATE_UNIX
DATE_ARRAY
DATE_OBJECT
DATE_ICAL

date_convert()
date_is_valid();
date_part_is_valid();
date_part_extract();

============================================================================
Date calculation and navigation
============================================================================
date_difference() will find the time difference between any two days, measured
in seconds, minutes, hours, days, months, weeks, or years.

date_days_in_month();
date_days_in_year();
date_weeks_in_year();
date_last_day_of_month();
date_day_of_week();
date_day_of_week_name();
date_difference();

============================================================================
Date regex and format helpers
============================================================================
Pre-defined constants, an array of date format strings and their
equivalent regex strings.

DATE_REGEX_LOOSE is a very loose regex that will pull date parts out
of an ISO date with or without separators, using either 'T' or a space
to separate date and time, and with or without time.

date_format_date() is similar to format_date(), except it takes a
date object instead of a timestamp as the first parameter.

DATE_FORMAT_ISO
DATE_FORMAT_DATETIME
DATE_FORMAT_UNIX
DATE_FORMAT_ICAL

DATE_REGEX_ISO
DATE_REGEX_DATETIME
DATE_REGEX_LOOSE

date_format_date();
date_short_formats();
date_medium_formats();
date_long_formats();
date_format_patterns();

============================================================================
Standardized ical parser and creator
============================================================================
The iCal parser is found in date_api_ical.inc, which is not included by default.
Include that file if you want to use these functions:

Complete rewrite of ical imports to parse vevents, vlocations, valarms,
and all kinds of timezone options and repeat rules for ical imports.
The function now sticks to parsing the ical into an array that can be used
in various ways. It no longer trys to convert timezones while parsing,
instead a date_ical_date_format() function is provided that can be used to
convert from the ical timezone to whatever timezone is desired in the
results. Repeat rules are parsed into an array which other modules can
manipulate however they like to create additional events from the results.

date_ical_export();
date_ical_import();
date_ical_date_format();

============================================================================
Helpers for portable date SQL
============================================================================
The SQL functions are found in date_api_sql.inc, which is not included by
default. Include that file if you want to use these functions:

date_sql();
date_server_zone_adj();
date_sql_concat();
date_sql_pad();

============================================================================
Date forms and validators
============================================================================
Reusable, configurable, self-validating FAPI date elements are found in
date_api_elements.inc, which is not included by default. Include it
if you want to use these elements. To use them, create a form element
and set the '#type' to one of the following:

date_select
 The date_select element will create a collection of form elements, with a
 separate select or textfield for each date part. The whole collection will
 get reformatted back into a date value of the requested type during validation.

date_text
 The date_text element will create a textfield that can contain a whole
 date or any part of a date as text. The user input value will be re-formatted
 back into a date value of the requested type during validation.

date_timezone
 The date_timezone element will create a drop-down selector to pick a
 timezone name.

The custom date elements require a few other pieces of information to work
correctly, like #date_format and #date_type. See the internal documentation
for more information.

============================================================================
Date Popup Module
============================================================================

A new module is included in the package that will enable a popup jQuery
calendar date picker and timepicker in date and time fields.

It is implemented as a custom form element, so set '#type' to 'date_popup'
to use this element. See the internal documentation for more information.

============================================================================
Date Repeat API
============================================================================

An API for repeating dates is available if installed. It can be used by
other modules to create a form element that will allow users to select
repeat rules and store those selections in an iCal RRULE string, and a
calculation function that will parse the RRULE and return an array of dates
that match those rules. The API is implemented in the Date module as a
new date widget if the Date Repeat API is installed.

============================================================================
RDF Integration
============================================================================

To make RDF easier to use, the base date themes (date_display_single and
date_display_range) have been expanded so they pass attributes and
RDF mappings for the field, if any, to the theme. If RDF is installed
and no other mappings are provided, the theme adds RDF information
to mark both the Start and End dates as 'xsd:dateTime' datatypes with the
property of 'dc:date'. This occurs in the theme preprocess layer, in
particular via the functions template_preprocess_date_display_single() and
template_preprocess_date_display_range().

To mark these as events instead, you could install the schemaorg
module, which will load the schema.org vocabulary. The mark the content type
that contains events as an 'Event', using the UI exposed by that
module and set the event start date field with the 'dateStart'
property and tag other fields in the content type with the appropriate
property types. The Date module theme will wrap the start and end
date output with appropriate markup.

If the result is not quite what you need, you should be able to implement your
own theme preprocess functions, e.g. MYTHEME_preprocess_date_display_single()
or MYTHEME_preprocess_date_display_range() and alter the attributes to use the
values you want.
Date Repeat Field

The functionality to integrate the Date Repeat API into date fields is being moved into this module,
which can then be enabled or disabled, depending on whether repeating date fields are needed.This folder includes files that can be used to test imports of date information.
To test them, set up FeedAPI and the Feed Element Mapper with Parser iCal
or Parser CVS and import these files into a date field.

- rrule.ics:
  Creates repeating dates using a wide variety of RRULEs.

- Yahoo.csv:
  This file uses the csv export format from Yahoo Calendar, similar to the
  format created by Outlook's csv export. The sample contains both timed
  and untimed 'All day' events.

- USHolidays.ics:
  An ical export of US Holidays in the 'All day' format used by
  Microsoft and Apple (where the Start date is the date of the event
  and the End date is the following day).
Drupal date_popup.module README.txt
==============================================================================

Javascript popup calendar and timeentry using the
jquery UI calendar and a choice of jquery-timeentry libraries.

================================================================================
Datepicker
================================================================================

This code uses the jQuery UI datepicker that is included in core. Localization
of the interface is handled by core.

The popup will use the site default for the first day of the week.

================================================================================
Timepicker
================================================================================

There are three ways to let users select time in the Date Popup widgets.
You can choose between them by going to admin/config/date/date_popup.

The options are:

1) Manual time entry - a plain textfield where users can type in the time.
2) A 'default' jQuery timepicker, included in the code
   (http://keith-wood.name/timeEntry.html).
3) The wvega timepicker (https://github.com/wvega/timepicker).

To install the alternate dropdown (wvega) timepicker:

Create a 'sites/all/libraries/wvega-timepicker' directory in your site
installation.  Then visit https://github.com/wvega/timepicker/archives/master,
download the latest copy and unzip it. You will see files with names like
jquery.timepicker-1.1.2.js and jquery.timepicker-1.1.2.css. Rename them to
jquery.timepicker.js and jquery.timepicker.css and copy them into
'sites/all/libraries/wvega-timepicker'.

================================================================================
Usage
================================================================================

To include a popup calendar in a form, use the type 'date_popup':

  $form['date'] = array(
    '#type' => 'date_popup':
    '#title => t('My Date'),
    ....
  );

Set the #type to date_popup and fill the element #default_value with
a date adjusted to the proper local timezone, or leave it blank.

The element will create two textfields, one for the date and one for the
time. The date textfield will include a jQuery popup calendar date picker,
and the time textfield uses a jQuery timepicker.

NOTE - Converting a date stored in the database from UTC to the local zone
and converting it back to UTC before storing it is not handled by this
element and must be done in pre-form and post-form processing!!

================================================================================
Customization
================================================================================

To change the default display and functionality of the calendar, set startup
parameters by adding selectors to your element. The configurable options
are:

#date_type
  The type of date to convert the input value to, DATE_DATETIME, DATE_ISO, or
  DATE_UNIX

#date_format
  a standard PHP date format string that represents the way the month, day,
  and year will be displayed in the textfield, like m/d/Y. Months and days
  must be in the 'm' and 'd' formats that include the zero prefix, the year
  must be in the 'Y' (four digit) format.

  Any standard separator can be used, '/', '-', '.', or a space.

  The m, d, and Y elements can be in any order and the order will be preserved.

  The time selector will add AM/PM if 'a' is in the format string.

  The default format uses the short site default format.

#date_year_range
  the number of years to go backwards and forwards from current year
  in year selector, in the format -{years back}:+{years forward},
  like -3:+3

#date_increment
   increment minutes and seconds by this amount, default is 1

================================================================================
Example:
================================================================================

$form['date'] = array(
  '#type' => 'date_popup',
  '#default_value' => '2007-01-01 10:30:00',
  '#date_type' => DATE_DATETIME,
  '#date_timezone' => date_default_timezone(),
  '#date_format' => 'm-d-Y H:i',
  '#date_increment' => 1,
  '#date_year_range' => '-3:+3',
);
Date All Day

This module provides the option to add an 'All Day' checkbox to toggle time on 
and off for date fields. It also contains the theme that displays the 'All Day' 
text on fields that have no time. 

Additionally, this module serves as an example of how other modules can inject 
new functionality into date fields using various hooks provided by Date and by 
the Field API.CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Usage

INTRODUCTION
------------

Current Maintainers:

 * Devin Carlson <http://drupal.org/user/290182>

Media: Vimeo adds Vimeo as a supported media provider.

REQUIREMENTS
------------

Media: Vimeo has one dependency.

Contributed modules
 * Media Internet - A submodule of the Media module.

INSTALLATION
------------

Media: Vimeo can be installed via the standard Drupal installation process
(http://drupal.org/node/895232).

USAGE
-----

Media: Vimeo integrates the Vimeo video-sharing service with the Media module to
allow users to add and manage Vimeo videos as they would any other piece of
media.

Internet media can be added on the Web tab of the Add file page (file/add/web).
With Media: Vimeo enabled, users can add a Vimeo video by entering its URL or
embed code.

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installing
 * Uninstalling
 * Frequently Asked Questions (FAQ)
 * Known Issues
 * More Information
 * How Can You Contribute?


INTRODUCTION
------------

Current Maintainer: Dave Reid <http://drupal.org/user/53892>
Co-maintainer: Kiam <http://drupal.org/user/55077>
Co-maintainer: Earnie <http://drupal.org/user/86710>
Co-maintainer: Darren Oh <http://drupal.org/user/30772>
Original Author: Matthew Loar <http://drupal.org/user/24879>

XML Sitemap automatically creates a sitemap that conforms to the sitemaps.org
specification. This helps search engines keep their search results up to date.


INSTALLING
----------

See http://drupal.org/getting-started/install-contrib for instructions on
how to install or update Drupal modules.

Once XML Sitemap is installed and enabled, you can adjust the settings for your
site's sitemap at admin/config/search/xmlsitemap. Your can view your site's
sitemap at http://yoursite.com/sitemap.xml.

It is highly recommended that you have clean URLs enabled for this module.


UNINSTALLING
------------

Because Drupal does not uninstall modules in reverse order of their
dependencies, if you want to uninstall all the XML sitemap modules, be sure to
disable and uninstall all the sub-modules before the base XML sitemap module.
To help fix this bug in Drupal core, visit http://drupal.org/node/151452.


FREQUENTLY ASKED QUESTIONS (FAQ)
--------------------------------

- There are no frequently asked questions at this time.


KNOWN ISSUES
------------

- See http://drupal.org/node/482550 for a list of the current known issues.


MORE INFORMATION
----------------

- To issue any bug reports, feature or support requests, see the module issue
  queue at http://drupal.org/project/issues/xmlsitemap.

- For additional documentation, see the online module handbook at
  http://drupal.org/handbook/modules/xmlsitemap.

- You can view the sitemap.org specification at http://sitemaps.org.


HOW CAN YOU CONTRIBUTE?
-----------------------

- Report any bugs, feature requests, etc. in the issue tracker.
  http://drupal.org/project/issues/xmlsitemap

- Help translate this module.
  http://localize.drupal.org/translate/projects/xmlsitemap

- Write a review for this module at drupalmodules.com.
  http://drupalmodules.com/module/xml-sitemap

- Help keep development active by dontating to the developer.
  http://davereid.chipin.com/
﻿
-- SUMMARY --

Provides a central transliteration service to other Drupal modules, and
sanitizes file names while uploading.

For a full description visit the project page:
  http://drupal.org/project/transliteration
Bug reports, feature suggestions and latest developments:
  http://drupal.org/project/issues/transliteration


-- INSTALLATION --

1. Install as usual, see http://drupal.org/node/70151 for further information.

2. If you are installing to an existing Drupal site, you might want to fix
   existing file names after installation, which will update all file names
   containing non-ASCII characters. However, if you have manually entered links
   to those files in any contents, these links will break since the original
   files are renamed. Therefore it is a good idea to test the conversion
   first on a copy of your web site. You'll find the retroactive conversion at
   Configuration and modules >> Media >> File system >> Transliteration.


-- CONFIGURATION --

This module doesn't require special permissions.

This module can be configured from the File system configuration page
(Configuration and modules >> Media >> File system >> Settings).

- Transliterate file names during upload: If you need more control over the
  resulting file names you might want to disable this feature here and install
  the FileField Paths module (http://drupal.org/project/filefield_paths)
  instead.

- Lowercase transliterated file names: It is recommended to enable this option
  to prevent issues with case-insensitive file systems.


-- 3RD PARTY INTEGRATION --

Third party developers seeking an easy way to transliterate text or file names
may use transliteration functions as follows:

if (function_exists('transliteration_get')) {
  $transliterated = transliteration_get($text, $unknown, $source_langcode);
}

or, in case of file names:

if (function_exists('transliteration_clean_filename')) {
  $transliterated = transliteration_clean_filename($filename, $source_langcode);
}

Note that the optional $source_langcode parameter specifies the language code
of the input. If the source language is not known at the time of transliter-
ation, it is recommended to set this argument to the site default language:

  $output = transliteration_get($text, '?', language_default('language'));

Otherwise the current display language will be used, which might produce
inconsistent results.


-- LANGUAGE SPECIFIC REPLACEMENTS --

This module supports language specific variations in addition to the basic
transliteration replacements. The following guide explains how to add them:

1. First find the Unicode character code you want to replace. As an example,
   we'll be adding a custom transliteration for the cyrillic character 'г'
   (hexadecimal code 0x0433) using the ASCII character 'q' for Azerbaijani
   input.

2. Transliteration stores its mappings in banks with 256 characters each. The
   first two digits of the character code (04) tell you in which file you'll
   find the corresponding mapping. In our case it is data/x04.php.

3. If you open that file in an editor, you'll find the base replacement matrix
   consisting of 16 lines with 16 characters on each line, and zero or more
   additional language-specific variants. To add our custom replacement, we need
   to do two things: first, we need to create a new transliteration variant
   for Azerbaijani since it doesn't exist yet, and second, we need to map the
   last two digits of the hexadecimal character code (33) to the desired output
   string:

     $variant['az'] = array(0x33 => 'q');

   (see http://people.w3.org/rishida/names/languages.html for a list of
   language codes).

   Any Azerbaijani input will now use the appropriate variant.

Also take a look at data/x00.php which already contains a bunch of language
specific replacements. If you think your overrides are useful for others please
file a patch at http://drupal.org/project/issues/transliteration.


-- CREDITS --

Authors:
* Stefan M. Kudwien (smk-ka) - http://drupal.org/user/48898
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136

Maintainers:
* Andrei Mateescu (amateescu) - http://drupal.org/user/729614

UTF-8 normalization is based on UtfNormal.php from MediaWiki
(http://www.mediawiki.org) and transliteration uses data from Sean M. Burke's
Text::Unidecode CPAN module
(http://search.cpan.org/~sburke/Text-Unidecode-0.04/lib/Text/Unidecode.pm).


-- USEFUL RESOURCES --

Unicode Code Converter:
http://people.w3.org/rishida/tools/conversion/

UTF-8 encoding table and Unicode characters:
http://www.utf8-chartable.de/unicode-utf8-table.pl

Country codes:
http://www.loc.gov/standards/iso639-2/php/code_list.php
The Login Destination module provides a way to customize the destination that a
user is redirected to after logging in, registering to the site, using a
one-time login link or logging out. 

The configuration consists of specifying so called login destination rules that
are evaluated when the login or logout takes place. Those rules are evaluated
against certain conditions and the user is taken to the destination specified
by the first matching rule. If the destination is empty, no redirect is
performed aka user is taken to the default destination. You can define pages
from which a user logs in/out to be a matching criterion. You can also select
certain user roles that are matched against those of a user. Note that only one
role has to match in order for the redirect to take place. If no roles are
selected the redirect is performed regardless of user roles. You can also
provide your own conditions by specifying PHP snippets (the PHP Filter has to
be enabled). The snippet should return TRUE if the condition matches and FALSE
otherwise.

There are no separate triggers for login and registration; instead you can
differentiate them by the specifying the pages that a user comes from:
- user - the user login form.
- user/register - the user registration form.
- user/*/edit - one-time login link, after the user has set the password.
- other - the login block or login forms embedded by other modules.
Please note that a user will be redirected when they register, even though they
may not be logged in afterwards immediately (e.g. because of email validation).
You can use this behavior to send the user to a page that contains further
instructions.

The destination you specify can be an internal page or an external URL.
Remember to precede the url with http://. You can also use the <front> tag to
redirect to the front page or the <current> tag to redirect to the page where
the user was before login/logout, aka the current page. In case of
login/register form the page from which the user entered the form is treaded as
the current page. Note that if you provide your own login/logout links you have
to add the 'current' GET parameter to them so Login Destination knows where
your users come from.

In some cases you will also need to provide the destination in a dynamic way by
using PHP snippets (the PHP Filter has to be enabled). The snippet's return
variable can be a string, for straight pages and urls, or an array for more
advanced options. The array should be in a form that the url function will
understand, e.g. %example. For more information, see the online API entry for
 <a href="@url">url function</a>. In most cases you will use it to specify GET
parameters and an anchor ("#"). Please study the examples below:

Take the user to the administration panel with underlying blog page:

<?php return array('blog', array('fragment' => 'overlay=admin/config', ), ); ?>

Take the user to the front page and specify some custom parameters:

<?php return array('<front>', array('query' => array('param1' => 'value1',
'param2' => 'value2', ), ), ); ?>

Take the user to the default page:

<?php return NULL; ?>

It also possible to set some advanced parameters on the setting page. Every
time in Drupal you can specify the 'destination' GET parameter in url to
redirect the user to a custom page. If you check the option
'Preserve the destination parameter' Login Destination will give priority to
this parameter over its own module settings. However with this option enabled
the redirect from the login block will not work. In some rare cases you can
also redirect the user just after using the one-time login link, before given
the possibility to change their password. Do this by checking the
'Redirect immediately after using one-time login link' option.Views Bulk Operations augments Views by allowing bulk operations
(provided by Drupal core or Rules)  to be executed on the displayed rows.
It does so by showing a checkbox in front of each displayed row, and adding a
select box on top of the View containing operations that can be applied.

Getting started
-----------------
1. Create a View.
2. Add a "Bulk operations" field, available to all entity types.
3. Configure the field by selecting at least one operation.
4. Go to the View page. VBO functionality should be present.

Read the full documentation at http://drupal.org/node/1591342.

History:
  Field_group was written for Drupal 7. For drupal 6, the module is
  located in the CCK module (http://drupal.org/project/cck).
  As drupal core has a fields API drupal > 6, the field_group module
  is considered a contribution.

Description:
  field_group is a module that will group a set of fields. In Drupal7,
  with fields, one means all fields that come from fieldable entities.
  You can add fieldgroups in several types with their own format settings.
  field_group has API functions to add your own formatter and rendering for
  it.
  One of the biggest improvements to previous versions, is that fieldgroups
  have unlimited nesting, better display control.
  Note that field_group will only group fields, it can not be used to hide
  certain fields since this a permission matter.

Module project page:
  http://drupal.org/project/field_group

Documentation page:
  http://drupal.org/node/1017838
  http://drupal.org/node/1017962

Available group types:
  - Fieldsets
  - Horizontal tabs
  - Vertical tabs
  - Accordions
  - Divs
  - Multipage steps: <strong>Note: This is only client side.
  - HTML5 group type
  - Html element

To submit bug reports and feature suggestions, or to track changes:
  http://drupal.org/project/issues/field_group

-- MAINTAINERS --

stalski - http://drupal.org/user/322618
swentel - http://drupal.org/user/107403
zuuperman - http://drupal.org/user/361625

-- INSPIRATORS --

yched - http://drupal.org/user/39567
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Usage

INTRODUCTION
------------

Current Maintainers:

 * Devin Carlson <http://drupal.org/user/290182>

Media: SoundCloud adds SoundCloud as a supported media provider.

REQUIREMENTS
------------

Media: SoundCloud has one dependency.

Contributed modules
 * Media Internet - A submodule of the Media module.

INSTALLATION
------------

Media: SoundCloud can be installed via the standard Drupal installation process
(http://drupal.org/node/895232).

USAGE
-----

Media: SoundCloud integrates the SoundCloud audio-sharing service with the
Media module to allow users to add and manage SoundCloud audio as they would
any other piece of media.

Internet media can be added on the Web tab of the Add file page (file/add/web).
With Media: SoundCloud enabled, users can add SoundCloud audio by entering its
URL or embed code.

Field collection
-----------------
Provides a field collection field, to which any number of fields can be attached.

Each field collection item is internally represented as an entity, which is
referenced via the field collection field in the host entity. While
conceptually field collections are treated as part of the host entity, each
field collection item may also be viewed and edited separately.


 Usage
 ------

  * Add a field collection field to any entity, e.g. to a node. For that use the
   the usual "Manage fields" interface provided by the "field ui" module of
   Drupal, e.g. "Admin -> Structure-> Content types -> Article -> Manage fields".

  * Then go to "Admin -> Structure-> Field collection" to define some fields for
   the created field collection.

  * By the default, the field collection is not shown during editing of the host
    entity. However, some links for adding, editing or deleting field collection
    items is shown when the host entity is viewed.

  * Widgets for embedding the form for creating field collections in the
    host-entity can be provided by any module. In future the field collection
    module might provide such widgets itself too.


Restrictions
-------------

  * As of now, the field collection field does not properly respect field
    translation. Thus, for now it is suggested to only use the field for
    entities that are not translatable.

/**
 *  @file
 *  README for the Media Module.
 */

See http://drupal.org/node/356802
[![Build Status](https://travis-ci.org/VeggieMeat/opcache.svg?branch=7.x-1.x)](https://travis-ci.org/VeggieMeat/opcache)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/VeggieMeat/opcache/badges/quality-score.png?b=7.x-1.x)](https://scrutinizer-ci.com/g/VeggieMeat/opcache/?branch=7.x-1.x)
[![Coverage Status](https://coveralls.io/repos/VeggieMeat/opcache/badge.svg?branch=7.x-1.x)](https://coveralls.io/r/VeggieMeat/opcache?branch=7.x-1.x)

OPcache
=======

This module allows Drupal to report status information about the cache and reset the cache.

REQUIREMENTS
------------

- PHP 5.4
- OPcache extension (see [official installation instructions](http://php.net/manual/en/opcache.installation.php)).
- [Composer Manager](https://www.drupal.org/project/composer_manager)

FEATURES
--------

- Drush integration
- Debugging tools (not yet implemented)

DRUSH COMMANDS
--------------

- opcache-invalidate
  Invalidate scripts currently cached in OPcache. Works across multiple webservers.
  Not yet implemented.
- opcache-status
  Get current OPcache status.
  Not yet implemented.
- opcache-configuration
  Get current OPcache configuration.
  Not yet implemented.

DEBUGGING TOOLS
---------------

Goal is to present a similar interface as the Memcache Admin module.
Not yet implemented.

***********
* README: *
***********

DESCRIPTION:
------------
This module provides an email field type.


INSTALLATION:
-------------
1. Place the entire email directory into your Drupal sites/all/modules/
   directory.

2. Enable the email module by navigating to:

     administer > modules


Features:
---------
  * validation of emails
  * turns addresses into mailto links
  * encryption of email addresses with
      o Invisimail (Drupal 5 + 6) (module needs to be installed)
      o SpamSpan (Drupal 6 only) (module needs to be installed)
  * contact form (see Display settings)
  * provides Tokens
  * exposes fields to Views


Note:
-----
To enable encryption of contact form, see settings under the Display fields tabs 


Author:
-------
Matthias Hutterer
mh86@drupal.org
m_hutterer@hotmail.com
Credits
-------

Thanks to Mark James for the icons
  http://www.famfamfam.com/lab/icons/silk/


Example code:


// Default cron-function, configurable through /admin/config/system/cron
function mymodule_cron() {
  // Do some stuff ...
}


// Define custom cron functions.
function mymodule_cronapi($op, $job = NULL) {
  return array(
    'mymodule_cronjob_1' => array(
      'title' => 'Cron-1 Handler',
      'scheduler' => array(
        'name' => 'crontab',
        'crontab' => array(
          'rules' => array('*/13 * * * *'),
        ),
      ),
    ),
    'mymodule_cronjob_2' => array(
      'title' => 'Cron-2 Handler',
      'callback' => 'mymodule_somefunction',
      'scheduler' => array(
        'name' => 'crontab',
        'crontab' => array(
          'rules' => array('0 0 1 * *'),
        ),
      ),
    ),
    'mymodule_cronjob_3' => array(
      'title' => 'Cron-3 Handler',
    ),
  );
}

// Custom cron-function
function mymodule_cronjob_1($job) {
  // Do some stuff ...
}

// Custom cron-function
function mymodule_somefunction($job) {
  // Do some stuff ...
}

// Custom cron-function
function mymodule_cronjob_3($job) {
  // Do some stuff ...
}

// Easy-hook, uses rule: 0+@ * * * *
function mymodule_cron_hourly($job) {
  // Do some stuff
}

// Easy-hook, uses rule: 0+@ 12 * * *
function mymodule_cron_daily($job) {
  // Do some stuff
}

// Easy-hook, uses rule: 0+@ 0 * * *
function mymodule_cron_nightly($job) {
  // Do some stuff
}

// Easy-hook, uses rule: 0+@ 0 * * 1
function mymodule_cron_weekly($job) {
  // Do some stuff
}

// Easy-hook, uses rule: 0+@ 0 1 * *
function mymodule_cron_monthly($job) {
  // Do some stuff
}

// Easy-hook, uses rule: 0+@ 0 1 1 *
function mymodule_cron_yearly($job) {
  // Do some stuff
}


DESCRIPTION
===========
Provides a field type that can reference arbitrary entities.

SITE BUILDERS
=============
Note that when using a select widget, Entity reference loads all the
entities in that list in order to get the entity's label. If there are
too many loaded entities that site might reach its memory limit and crash
(also known as WSOD). In such a case you are advised to change the widget
to "autocomplete". If you get a WSOD when trying to edit the field
settings, you can reach the widget settings directly by navigation to

  admin/structure/types/manage/[ENTITY-TYPE]/fields/[FIELD-NAME]/widget-type

Replace ENTITY-TYPE and FIELD_NAME with the correct values.

Current state of Features for Drupal 7
--------------------------------------
Work on Features for D7 is currently aimed at getting to a point where Features
can be used on a new install of Drupal 7 with features that were created on D7.
Once this has been achieved, we will begin working on supporting D6 features as
well as possibly supporting upgrades & migrations between legacy components and
new equivalents (e.g. CCK to fields, imagecache to core image styles).

### Working components

- ctools
- dependencies
- field
- filter
- image
- menu_custom
- menu_links
- node
- taxonomy
- user_permission
- user_role
- views

### Has changes to export format between D6 and D7

(@TODO legacy export compatibility)

- filter
- taxonomy

### Requires upgrade/migration path

- imagecache > image
- content > field

Note on the "Generate Feature" capability
-----------------------------------------
Features 7.x-2.x includes the ability to "Generate a feature" which saves it
to the server disk. This can be a time-saving task in development. It requires
the webserver to be able to write to the very code running the site and is
not recommended for any environment other than a firewalled-off, local
development environment (e.g. a person working alone on their laptop).

Features 1.x for Drupal 7.x
---------------------------
The features module enables the capture and management of features in Drupal. A
feature is a collection of Drupal entities which taken together satisfy a
certain use-case.

Features provides a UI and API for taking different site building components
from modules with exportables and bundling them together in a single feature
module. A feature module is like any other Drupal module except that it declares
its components (e.g. views, contexts, CCK fields, etc.) in its `.info` file so
that it can be checked, updated, or reverted programmatically.

Examples of features might be:

- A blog
- A pressroom
- An image gallery
- An e-commerce t-shirt store


Installation
------------
Features can be installed like any other Drupal module -- place it in the
modules directory for your site and enable it on the `admin/build/modules` page.
To take full advantage of some of the workflow benefits provided by Features,
you should install [Drush][1].

If you plan on creating or working with very large features (greater than 1000
items), you may need to increase PHP's max_input_vars configuration directive.
For example, adding the following line to your .htaccess file will increase the
max_input_vars directive to 3000:

php_value max_input_vars 3000

If you are using Suhosin, increasing suhosin.get.max_vars,
suhosin.post.max_vars, and suhosin.request.max_vars may also be necessary.


Basic usage
-----------
Features is geared toward usage by developers and site builders. It
is not intended to be used by the general audience of your Drupal site.
Features provides tools for accomplishing two important tasks:

### Task 1: Export features

You can build features in Drupal by using site building tools that are supported
(see a short list under the *Compatibility* section).

Once you've built and configured functionality on a site, you can export it into
a feature module by using the feature create page at
`admin/structure/features/create`.


### Task 2: Manage features

The features module also provides a way to manage features through a more
targeted interface than `admin/modules`. The interface at
`admin/structure/features` shows you only feature modules, and will also inform you
if any of their components have been overridden. If this is the case, you can
also re-create features to bring the module code up to date with any changes
that have occurred in the database.


Including custom code and adding to your feature
------------------------------------------------
Once you've exported your feature you will see that you have several files:

    myfeature.info
    myfeature.module
    myfeature.[*].inc

You can add custom code (e.g. custom hook implementations, other functionality,
etc.) to your feature in `myfeature.module` as you would with any other module.
Do not change or add to any of the features `.inc` files unless you know what
you are doing. These files are written to by features on updates so any custom
changes may be overwritten.


Using Features to manage development
------------------------------------
Because Features provides a centralized way to manage exportable components and
write them to code it can be used during development in conjunction with a
version control like SVN or git as a way to manage changes between development,
staging and production sites. An example workflow for a developer using Features
is to:

1. Make configuration changes to a feature on her local development site.
2. Update her local feature codebase using `drush features-update`.
3. Commit those changes using `svn commit`.
4. Roll out her changes to the development site codebase by running `svn update`
  on the server. Other collaborating developers can also get her changes with
  `svn update`.
5. Reverting any configuration on the staging site to match the updated codebase
by running `drush features-revert`.
6. Rinse, repeat.

Features also provides integration with the [Diff][3] module if enabled to show
differences between configuration in the database and that in code. For site
builders interested in using Features for development, enabling the diff module
and reading `API.txt` for more details on the inner workings of Features is
highly recommended.


Drush usage
-----------
(requires Drush v4.5 or higher)

Features provides several useful drush commands:

- `drush features`

  List all the available features on your site and their status.

- `drush features-export [feature name] [component list]`

  Write a new feature in code containing the components listed.
  If called with no arguments, display a list of available components.
  If called with one argument, take the argument as a component name and
  attempt to create a feature with the same name.

  The option '--destination=foo' may be used to specify the path (from Drupal
  root) where the feature should be created. The default destination is
  'sites/all/modules', though this can be overridden via the Features
  settings page.

- `drush features-update [feature name]`

  Update the code of an existing feature to include any overrides/changes in
  your database (e.g. a new view).

- `drush features-revert [feature name]`

  Revert the components of a feature in your site's database to the state
  described in your feature module's defaults.

- `drush features-diff [feature name]`

  Show a diff between a feature's database components and those in code.
  Requires the Diff module.

Additional commands and options can be found using `drush help`.


Compatibility
-------------
Features provides integration for the following exportables:

- CTools export API implementers (Context, Spaces, Boxes, Strongarm, Page
  Manager)
- ImageCache
- Views
- [Other contributed modules][2]

Features also provides faux-exportable functionality for the following Drupal
core and contrib components:

- Fields
- Content types
- Input filters
- User roles/permissions
- Custom menus and menu links *
- Taxonomy vocabularies

* Currently in development.


Security Concerns
-----------------
If you are using Features to export Roles and also use those Roles in other
exportable code (like Views filters) you can wind up with an unintended
security hole.  When you import your Feature, if the Roles do not get created
with the exact same Role IDs then your Views filters (or other component) will
be referencing a different Role than you intended.


For developers
--------------
Please read `API.txt` for more information about the concepts and integration
points in the Features module.


Maintainers
-----------
- febbraro (Frank Febbraro)
- hefox (Fox)
- mpotter (Mike Potter)
- timplunkett (Tim Plunkett)


[1]: http://drupal.org/project/drush
[2]: (http://drupal.org/taxonomy/term/11478)
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Usage

INTRODUCTION
------------

Current Maintainers:

 * Devin Carlson <http://drupal.org/user/290182>

Media: YouTube adds YouTube as a supported media provider.

REQUIREMENTS
------------

Media: YouTube has one dependency.

Contributed modules
 * Media Internet - A submodule of the Media module.

INSTALLATION
------------

Media: YouTube can be installed via the standard Drupal installation process
(http://drupal.org/node/895232).

USAGE
-----

Media: YouTube integrates the YouTube video-sharing service with the Media
module to allow users to add and manage YouTube videos as they would any other
piece of media.

Internet media can be added on the Web tab of the Add file page (file/add/web).
With Media: YouTube enabled, users can add a YouTube video by entering its URL
or embed code.
-- SUMMARY --

Chosen uses the Chosen jQuery plugin to make your <select> elements more user-friendly.


-- INSTALLATION --

  1. Download the Chosen jQuery plugin (http://harvesthq.github.io/chosen/ version 1.1.0 is recommended) and extract the file under sites/all/libraries.
  2. Download and enable the module.
  3. Configure at Administer > Configuration > User interface > Chosen (requires administer site configuration permission)

-- INSTALLATION VIA DRUSH --

 A Drush command is provided for easy installation of the Chosen plugin.

 drush chosenplugin

 The command will download the plugin and unpack it in "sites/all/libraries".
 It is possible to add another path as an option to the command, but not
 recommended unless you know what you are doing.

-- ACCESSIBILITY CONCERN --

There are accessibility problems with the main library as identified here:
	https://github.com/harvesthq/chosen/issues/264

-- TROUBLE SHOOTING --

  How to exlude a select field from becoming a chosen select.
    - go to the configuration page and add your field using the jquery "not"
      operator to the textarea with the comma seperated values.
      For date fields this could look like: select:not([name*='day'],[name*='year'],[name*='month'])
Media 23Video

Creates a 23Video PHP Stream Wrapper for Resource and implements the various
formatter and file listing hooks in the Media module.

Prerequisites
-------------
The media_23video requires the media and media_internet to be installed.

Installation
------------
To install, copy the media_23video directory and all its contents to your
modules directory.

Configuration
-------------
To enable this module, visit administer -> modules, and enable media_23video.

Usage
-------------
## File fields

- Add a new "file" type field to your content type or entity. Choose the widget
  type "Multimedia browser". You can also select an existing file field.
- While setting up the field (or after selecting "edit" on an existing field)
  enable:
    - Enabled browser plugins: "Web"
    - Allowed remote media types: "Video"
    - Allowed URI schemes: "media-23video:// (23video videos)"

- On "Manage display" for the file field's content or entity type, choose
  "Rendered file" and a view mode.
- Set up 23video video formatter options for each view mode in Structure ->
  File types -> Manage file display. This is where you can choose size, autoplay
  and etc.
- When using the file field while creating or editing content, paste a 23video
  video url into the Web tab.


## WYSIWYG inserts

- Enable the Media module "Media insert" button on your WYSIWYG profile.
- Enable "Convert Media tags to markup" filter in the appropriate text formats.
- Configure any desired settings in Configuration -> Media -> "Media browser
  settings"
- Set up 23video video formatter options in Structure -> File types -> Manage
  file display. **Note:** for any view mode that will be used in a WYSIWYG,
  enable both the 23video video and preview image formatter. Arrange the Video
  formatter on top. This allows the video to be used when the content is viewed,
  and the preview when the content is being edited.

- When editing a text area with your WYSIWYG, click the "Media insert" button,
  and paste a 23video video url into the Web tab of the media browser.

Localization Update
-------------------
  Automatically download and update your translations by fetching them from
  http://localize.drupal.org or any other Localization server.

  The l10n update module helps to keep the translation of your drupal core and
  contributed modules up to date with the central Drupal translation repository
  at http://localize.drupal.org. Alternatively locally stored translation files
  can be used as translation source too.

  By choice updates are performed automatically or manually. Locally altered
  translations can either be respected or ignored.

  The l10n update module is developed for:
   * Distributions which include their own translations in .po files.
   * Site admins who want to update the translation with each new module revision.
   * Site builders who want an easy tool to download translations for a site.
   * Multi-sites that share one translation source.

  Project page:  http://drupal.org/project/l10n_update
  Support queue: http://drupal.org/project/issues/l10n_update

Installation
------------
  Download, unpack the module the usual way.
  Enable this module and the Locale module (core).

  You need at least one language (besides the default English).
  On Administration > Configuration > Regional and language > Languages:
    Click "Add language".
    Select a language from the select list "Language name".
    Then click the "Add language" button.

  Drupal is now importing interface translations. This can take a few minutes.
  When it's finished, you'll get a confirmation with a summary of the
  translations that have been imported.

  If required, enable the new language as default language.
  Administration > Configuration > Regional and language > Languages:
    Select your new default language.

Update interface translations
-----------------------------
  You want to import translations regularly using cron. You can enable this
  on Administration > Configuration > Regional and language > Languages:
    Choose the "Translation updates" tab.
    Change "Check for updates" to "Daily" or "Weekly" instead of the default "Never".
  From now on cron will check for updated translations, and import them is required.

  The status of the translations is reported on the "Status report" page at
  Administration > Reports.

  To check the translation status and execute updates manually, go to
    Administration > Configuration > Regional and language > Translate inteface
    Choose the "Update" tab.
  You see a list of all modules and their translation status.
  On the bottom of the page, you can manually update using "Update translations".

Use Drush
---------
  You can also use drush to update your translations:
    drush l10n-update           # Update translations.
    drush l10n-update-refresh   # Refresh available information.
    drush l10n-update-status    # Show translation status of available project


Summary of administrative pages
-------------------------------
  Translations status overview can be found at
    Administration > Configuration > Regional and language > Languages > Translation updates

  Update configuration settings can be found at
    Administration > Configuration > Regional and language > Translate interface > Update

Translating Drupal core, modules and themes
-------------------------------------------
  When Drupal core or contributed modules or themes get installed, Drupal core
  checks if .po translation files are present and updates the translations with
  the strings found in these files. After this, the localization update module
  checks the localization server for more recent translations, and updates
  the site translations if a more recent version was found.
  Note that the translations contained in the project packages may become
  obsolete in future releases.

  Changes to translations made locally using the site's build in translation
  interface (Administer > Site building > Translate interface > Search) and
  changes made using the localization client module are marked. Using the
  'Update mode' setting 'Edited translations are kept...', locally edited
  strings will not be overwritten by translation updates.
  NOTE: Only manual changes made AFTER installing Localization Update module
  are preserved. To preserve manual changes made prior to installation of
  Localization Update module, use the option 'All existing translations are kept...'.

po files, multi site and distributions
--------------------------------------
  Multi sites and other installations that share the file system can share
  downloaded translation files. The Localization Update module can save these
  translations to disk. Other installations can use these saved translations
  as their translation source.

  All installations that share the same translation files must be configured
  with the same 'Store downloaded files' file path e.g. 'sites/all/translations'.
  Set the 'Update source' of one installation to 'Local files and remote server'
  or 'Remote server only', all other installations are set to
  'Local files only' or 'Local files and remote server'.

  Translation files are saved with the following file name syntax:

    <module name>-<release>.<language code>.po

  For example:
    masquerade-6.x-1.5.de.po
    tac_lite-7.x-1.0-beta1.nl.po

  Po files included in distributions should match this syntax too.

Alternative source of translation
---------------------------------

  The download path pattern is normally defined in the above defined xml file.
  You may override the download path of the po file on a project by project
  basis by adding this definition in the .info file:

    l10n path = http://example.com/files/translations/%core/%project/%project-%release.%language.po

  Modules can force Locale to load the translation of an other project by
  defining 'interface translation project' in their .info file. This can be
  usefull for custom modules to use for example a common translation file

    interface translation project = my_project

  This can be used in combination with an alternative path to the translation
  file. For example:

    l10n path = sites/all/modules/custom/%project/%project.%language.po

Exclude a project from translation checks and updates
-----------------------------------------------------

  Individual modules can be excluded from translation checks and updates. For
  example custom modules or features. Add the following line to the .info file
  to exclude a module from translation checks and updates:

  interface translation project = FALSE

API
---
  Using hook_l10n_update_projects_alter modules can alter or specify the
  translation repositories on a per module basis.

  See l10n_update.api.php for more information.

Maintainers
-----------
  Erik Stielstra
  Gábor Hojtsy
  Jose Reyero
# jQuery Update Drupal Module

jQuery Update module upgrades Drupal's stable version of jQuery in order to
support the most current jQuery version available.

Once a stable release of Drupal comes out, only minor bug-fix changes may be
added to it, so Drupal's version of jQuery will often lag behind the most recent
release offered by the jQuery project. The jQuery community tends to only
support the most recent version, so this module ensures that your Drupal
installation can run the most up-to-date jQuery plug-ins.


## Installation

1. Copy the jquery_update directory to your sites/SITENAME/modules directory.

2. Enable the module at Administer >> Site building >> Modules.


## Credits

* Matt Farina (mfer)
* Jeff Robbins (jjeff)
* Angela Byron (webchick)
* Addison Berry (add1sun)
* Rob Loach (RobLoach)
Smart Trim implements a new field formatter for textfields (text, text_long,
  and text_with_summary, if you want to get technical) that improved upon the
  "Summary or Trimmed" formatter built into Drupal 7.

After installing and enabling Smart Trim, you should see a "Smart trimmed"
  option in the format dropdown for your text fields. With smart trim, you have
  control over:
    1. The trim length
    2. Whether the trim length is measured in characters or word
    3. Appending an optional suffix at the trim point
    4. Displaying an optional "More" link immediately after the trimmed text.
    5. Stripping out HTML tags from the field

The "More" link functionality may not make sense in many contexts, and may be
 redundant in situations where "Read More" is included in set of links included
 with the node.

Initial release is strictly for Drupal 7. No backport to Drupal 6 is planned.

Note that HTML markup not seen by end-users will still be counted when
  calculating trim length. This may be addressed in future releases.

Smart Trim was initially developed by Ben Byrne while at New Signature
  (bbyrne@newsignature.com) but Ben is now at Cornershop Creative
  (ben@cornershopcreative.com)INTRODUCTION
------------

Provides common and resuable token UI elements and missing core tokens.

 * For a full description of the module, visit the project page:
   https://drupal.org/project/token

 * To submit bug reports and feature suggestions, or to track changes:
   https://drupal.org/project/issues/token


INSTALLATION
------------

Install as usual, see
https://drupal.org/documentation/install/modules-themes/modules-7 for further
information.


TROUBLESHOOTING
---------------

Token module doesn't provide any visible functions to the user on its own, it
just provides token handling services for other modules.


MAINTAINERS
-----------

Current maintainers:

 * Dave Reid (https://drupal.org/user/53892)INSTALLATION

- Install libraries module (dependency).
- Download jQuery-Placeholder library from https://github.com/mathiasbynens/jquery-placeholder
- Place this library in sites/[all/sitename/default]/libraries/placeholder
  so the jquery.placeholder.js is located at sites/[all/sitename/default]/libraries/placeholder/jquery.placeholder.js
  or glone directly; 'git clone --recursive https://github.com/mathiasbynens/jquery-placeholder placeholder'
  in your libraries folder.

USAGE

- Add a '#placeholder' key or a 'placeholder' element to the '#attributes'
  array of textfields or textareas.

EXAMPLES

---------------- BASIC EXAMPLE ---------------
/**
 * Implements hook_form_FORM_ID_alter().
 */
function placeholder_form_search_block_form_alter(&$form, &$form_state) {
  $form['search_block_form']['#placeholder'] = t('Search here');
  // or ....
  $form['search_block_form']['#attributes']['placeholder'] = t('Search here');
}

function my_custom_module_form() {
  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => 'Name',
    '#placeholder' => t('Enter your name here'),
  );
  // ....
}

--------------- ANOTHER EXAMPLE -----------------
/**
 * Implements hook_form_alter().
 */
function mymodule_form_alter(&$form, &$form_state, $form_id) {
  // Add placeholder for link fields
  if (isset($form['field_link_url'])) {
    $form['#after_build'][] = 'mymodule_link_field_after_build';
  }
}
function mymodule_link_field_after_build($form, &$form_state) {
  if (module_exists('placeholder')){

    $lang = isset($form['field_link_url']['#language']) ? $form['field_link_url']['#language'] : LANGUAGE_NONE;
    if (isset($form['field_link_url'][$lang])) {
      // Go through each delta
      foreach($form['field_link_url'][$lang] as $delta => $item) {
        // Make sure this is a delta and not just another element.
        // Gross, but there's no clean list of delta items.
        if (is_numeric($delta)) {
          // Sanity check to make sure this is properly formed.
          if (isset($form['field_link_url'][$lang][$delta]['url'])) {
            // Add the placeholder as an attribute, because otherwise it doesn't work.
            $form['field_link_url'][$lang][$delta]['url']['#attributes']['placeholder'] = t('http://www.example.com');
          }
        }
      }
    }

    // Add the library, if it's available.
    if (($library = libraries_load('placeholder', 'minified')) && !empty($library['loaded'])) {
      // Attach the library files.
      libraries_load_files($library);
      // Attach the module js file. This will actually invoke the library.
      $element['#attached']['js'] = array(
        drupal_get_path('module', 'placeholder') . '/placeholder.js',
      );
    }

  }
  return $form;
}


Strongarm 2.x for Drupal 7.x
----------------------------
Strongarm gives site builders a way to override the default variable values that
Drupal core and contributed modules ship with. It is not an end user tool, but a
developer and site builder tool which provides an API and a limited UI.

An example of such a variable is `site_frontpage`. In Drupal this defaults to
`node`, which ensures that the front page gets content as soon as some exists,
but for many Drupal sites this setting is simply wrong. Strongarm gives the site
builder a place in the equation - an opportunity to set the default value of
`site_frontpage` to something that makes sense for their site.


Installation
------------
Strongarm can be installed like any other Drupal module -- place it in
the modules directory for your site and enable it (and its requirement,
CTools) on the `admin/build/modules` page.

Strongarm is an API module. It does absolutely nothing for the end user out of
the box without other modules that take advantage of its API.


How Strongarm works
-------------------
Strongarm uses the CTools export API to make entries in the system module's
`variable` table exportables. Exportables are Drupal configuration objects that
lead a dual life -- they may be *defaults* set by code exports in modules, they
may be *overridden* if a user chooses to change the value in the database, or
they may be *normal* if the configuration object lives only in the database but
not in code. To learn more about exportables and the CTools export API, see the
CTools advanced help on "Exportable objects tool."


Exporting variables
-------------------
If you are a developer or site builder Strongarm gives you tools to export the
settings of variables in your site database and manage any overrides to default
values.

To export variable values, you will need to enable either the [Features][1]
module or the [Bulk Export][2] module provided by CTools (as of June 29, 2010
you must use a recent checkout CTools `DRUPAL-6--1` in order to use Bulk Export
with Strongarm). Features provides a UI for adding variable exports to a
feature. Bulk Export provides a UI for generating defaults hooks with exported
variables that you can add to your own modules. You do not need to enable both
modules.


Maintainers
-----------

- jmiccolis (Jeff Miccolis)
- yhahn (Young Hahn)


[1]: http://drupal.org/project/features
[2]: http://drupal.org/project/ctools
This module allows you to filter your watchdog messages based on severity level. It can also deduplicate the watchdog messages.

hook_watchdog_filtering() is also exposed by this module. Example from watchdog_filtering.api.php:

/**
 * Filter watchdog log entry. Works similar to hook_node_access().
 *
 * @param array $log_entry
 *   The watchdog log entry
 */
function hook_watchdog_filtering(array $log_entry) {
  // Never watchdog page not found messages.
  if ($log_entry['type'] == 'page not found') {
    return WATCHDOG_FILTERING_EXCLUDE;
  }

  // "Always" watchdog php messages.
  if ($log_entry['type'] == 'php') {
    return WATCHDOG_FILTERING_INCLUDE;
  }

  // Don't affect filtering on other messages.
  return WATCHDOG_FILTERING_IGNORE;
}
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * Usage examples


INTRODUCTION
------------

Providing methods for creating, editing, searching JIRA issues
out of Drupal via REST.

Features:
- search
- create
- modify
- close JIRA-issues

Requirements:
Extension for curl/libcurl must be enabled (http://www.php.net/curl).



INSTALLATION
------------

- make sure you have libcurl extension installed
- setup your jira-url for D7 at  ../admin/config/services/jira_rest





USAGE EXAMPLES
-------------

TODO, as a start, see examples in comments in .module file

Honeypot Module Readme
----------------------


Installation
------------

To install this module, place it in your sites/all/modules folder and enable it
on the modules page.


Configuration
-------------

All settings for this module are on the Honeypot configuration page, under the
Configuration section, in the Content authoring settings. You can visit the
configuration page directly at admin/config/content/honeypot.

Note that, when testing Honeypot on your website, make sure you're not logged in
as an administrative user or user 1; Honeypot allows administrative users to
bypass Honeypot protection, so by default, Honeypot will not be added to forms
accessed by site administrators.


Use in Your Own Forms
---------------------

If you want to add honeypot to your own forms, or to any form through your own
module's hook_form_alter's, you can simply place the following function call
inside your form builder function (or inside a hook_form_alter):

honeypot_add_form_protection($form, $form_state, array('honeypot', 'time_restriction'));

Note that you can enable or disable either the honeypot field, or the time
restriction on the form by including or not including the option in the array.


Credit
------

The Honeypot module was originally developed by Jeff Geerling of Midwestern Mac,
LLC (midwesternmac.com), and sponsored by flockNote (flocknote.com).Description
===========
Elements intends to become a library that provides complex form elements for developers to use in their modules.


Elements provided
=================

1. emailfield
2. searchfield
3. telfield
4. urlfield
5. numberfield
6. rangefield
The module provides an integration between Jira (via the jira_rest
module) and rules.

In the current limited form the module provides a rules action for
creating simple, basic issues in Jira.

You must configure the jira_rest module with username and password at
`admin/config/services/jira_rest`.

In the rules action you can configure:

 - Project key
 - Issuetype name
 - Summary
 - Description

After successfully creating the issue the action provides the issue ID,
issue key, and a link to the REST API endpoint of the newly created
issue.

-- SUMMARY --

Wysiwyg API allows to users of your site to use WYSIWYG/rich-text, and other
client-side editors for editing contents.  This module depends on third-party
editor libraries, most often based on JavaScript.

For a full description of the module, visit the project page:
  http://drupal.org/project/wysiwyg
To submit bug reports and feature suggestions, or to track changes:
  http://drupal.org/project/issues/wysiwyg


-- REQUIREMENTS --

* None.


-- INSTALLATION --

* Install as usual, see
  http://drupal.org/documentation/install/modules-themes/modules-7

* Go to Administration » Configuration » Content authoring » Wysiwyg,
  and follow the displayed installation instructions to download and install one
  of the supported editors.


-- CONFIGURATION --

* Go to Administration » Configuration » Content authoring » Text formats, and

  - either configure the Full HTML format, assign it to trusted roles, and
    disable "HTML filter", "Line break converter", and (optionally) "URL filter".

  - or add a new text format, assign it to trusted roles, and ensure that above
    mentioned input filters are disabled.

* Setup editor profiles in Administration » Configuration » Content authoring
  » Wysiwyg.


-- CONTACT --

Current maintainers:
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136
* Henrik Danielsson (TwoD) - http://drupal.org/user/244227

This project has been sponsored by:
* UNLEASHED MIND
  Specialized in consulting and planning of Drupal powered sites, UNLEASHED
  MIND offers installation, development, theming, customization, and hosting
  to get you started. Visit http://www.unleashedmind.com for more information.


Entity API module
-----------------
by Wolfgang Ziegler, nuppla@zites.net

This module extends the entity API of Drupal core in order to provide a unified
way to deal with entities and their properties. Additionally, it provides an
entity CRUD controller, which helps simplifying the creation of new entity types.


This is an API module. You only need to enable it if a module depends on it or
you are interested in using it for development.

This README is for interested developers. If you are not interested in
developing, you may stop reading now.

--------------------------------------------------------------------------------
                                Entity API
--------------------------------------------------------------------------------

  * The module provides API functions allowing modules to create, save, delete
    or to determine access for entities based on any entity type, for which the
    necessary metadata is available. The module comes with integration for all
    core entity types, as well as for entities provided via the Entity CRUD API
    (see below). However, for any other entity type implemented by a contrib
    module, the module integration has to be provided by the contrib module
    itself.

  * Thus the module provides API functions like entity_save(), entity_create(),
    entity_delete(), entity_revision_delete(), entity_view() and entity_access()
    among others.
    entity_load(), entity_label() and entity_uri() are already provided by
    Drupal core.

 *  For more information about how to provide this metadata, have a look at the
    API documentation, i.e. entity_metadata_hook_entity_info().

--------------------------------------------------------------------------------
               Entity CRUD API - Providing new entity types
--------------------------------------------------------------------------------

 * This API helps you when defining a new entity type. It provides an entity
   controller, which implements full CRUD functionality for your entities.

 * To make use of the CRUD functionality you may just use the API functions
   entity_create(), entity_delete() and entity_save().

   Alternatively you may specify a class to use for your entities, for which the
   "Entity" class is provided. In particular, it is useful to extend this class
   in order to easily customize the entity type, e.g. saving.

 * The controller supports fieldable entities and revisions. There is also a
   controller which supports implementing exportable entities.

 * The Entity CRUD API helps with providing additional module integration too,
   e.g. exportable entities are automatically integrated with the Features
   module. These module integrations are implemented in separate controller
   classes, which may be overridden and deactivated on their own.

 * There is also an optional ui controller class, which assists with providing
   an administrative UI for managing entities of a certain type.

 * For more details check out the documentation in the drupal.org handbook
   http://drupal.org/node/878804 as well as the API documentation, i.e.
   entity_crud_hook_entity_info().


 Basic steps to add a new entity type:
---------------------------------------

  * You might want to study the code of the "entity_test.module".

  * Describe your entities db table as usual in hook_schema().

  * Just use the "Entity" directly or extend it with your own class.
    To see how to provide a separate class have a look at the "EntityClass" from
    the "entity_test.module".

  * Implement hook_entity_info() for your entity. At least specifiy the
    controller class (EntityAPIController, EntityAPIControllerExportable or your
    own), your db table and your entity's keys.
    Again just look at "entity_test.module"'s hook_entity_info() for guidance.

  * If you want your entity to be fieldable just set 'fieldable' in
    hook_entity_info() to TRUE. The field API attachers are then called
    automatically in the entity CRUD functions.

  * The entity API is able to deal with bundle objects too (e.g. the node type
    object). For that just specify another entity type for the bundle objects
    and set the 'bundle of' property for it.
    Again just look at "entity_test.module"'s hook_entity_info() for guidance.

  * Schema fields marked as 'serialized' are automatically unserialized upon
    loading as well as serialized on saving. If the 'merge' attribute is also
    set to TRUE the unserialized data is automatically "merged" into the entity.

  * Further details can be found at http://drupal.org/node/878804.



--------------------------------------------------------------------------------
                Entity Properties & Entity metadata wrappers
--------------------------------------------------------------------------------

  * This module introduces a unique place for metadata about entity properties:
    hook_entity_property_info(), whereas hook_entity_property_info() may be
    placed in your module's {YOUR_MODULE}.info.inc include file. For details
    have a look at the API documentation, i.e. hook_entity_property_info() and
    at http://drupal.org/node/878876.

  * The information about entity properties contains the data type and callbacks
    for how to get and set the data of the property. That way the data of an
    entity can be easily re-used, e.g. to export it into other data formats like
    XML.

  * For making use of this information (metadata) the module provides some
    wrapper classes which ease getting and setting values. The wrapper supports
    chained usage for retrieving wrappers of entity properties, e.g. to get a
    node author's mail address one could use:

       $wrapper = entity_metadata_wrapper('node', $node);
       $wrapper->author->mail->value();

    To update the user's mail address one could use

       $wrapper->author->mail->set('sepp@example.com');

       or

       $wrapper->author->mail = 'sepp@example.com';

    The wrappers always return the data as described in the property
    information, which may be retrieved directly via entity_get_property_info()
    or from the wrapper:

       $mail_info = $wrapper->author->mail->info();

    In order to force getting a textual value sanitized for output one can use,
    e.g.

       $wrapper->title->value(array('sanitize' => TRUE));

    to get the sanitized node title. When a property is already returned
    sanitized by default, like the node body, one possibly wants to get the
    not-sanitized data as it would appear in a browser for other use-cases.
    To do so one can enable the 'decode' option, which ensures for any sanitized
    data the tags are stripped and HTML entities are decoded before the property
    is returned:

       $wrapper->body->value->value(array('decode' => TRUE));

    That way one always gets the data as shown to the user. However if you
    really want to get the raw, unprocessed value, even for sanitized textual
    data, you can do so via:

      $wrapper->body->value->raw();

README
--------------------------------------------------------------------------
This module allows nodes to be published and unpublished on specified dates.

Dates can be entered either as plain text or with Javascript calendar
popups (JSCalendar in Drupal 5, Date Popup in Drupal 6).

JSCalendar is part of the JSTools module (http://drupal.org/project/jstools).
The Date Popup module is part of the the Date module (http://drupal.org/project/date).

Notice:
- Please check if cron is running correctly if scheduler does not publish your
  scheduled nodes.
- Scheduler does only schedule publishing and unpublishing of nodes. If you
  want to schedule any other activity check out Workflow
  (http://drupal.org/project/workflow), Rules (http://drupal.org/project/rules)
  and Actions (http://drupal.org/project/actions).

Scheduler is the work of many people. Some of them are listed here:
http://drupal.org/project/developers/3292. But there are even more: All the
people who created patches but did not check them in themselfs, who posted bug
or feature request and those who provided translations and documentation.

This module has been completely rewritten for Drupal 4.7 by:

Ted Serbinski <hello [at] tedserbinski.com>
  aka "m3avrck" on http://drupal.org


This module was originally written for Drupal 4.5.0 by:

Moshe Weitzman <weitzman [at] tejasa.com>
Gabor Hojtsy <goba [at] php.net>
Tom Dobes <tomdobes [at] purdue.edu>


INSTALLATION
--------------------------------------------------------------------------
1. Copy the scheduler.module to your modules directory
2. Enable module, database schemas will be setup automatically.     
3. Grant users the permission "schedule (un)publishing of nodes" so they can
   set when the nodes they create are to be (un)published.
   
4. Visit admin > settings > content-types and click on any node type and
   check the box "enable scheduled (un)publishing" for this node type
   
5. Repeat for all node types that you want scheduled publishing for

The scheduler will run with Drupal's cron.php, and will (un)publish nodes
timed on or before the time at which cron runs.  If you'd like finer
granularity to scheduler, but don't want to run Drupal's cron more often (due
to its taking too many cycles to run every minute, for example), you can set
up another cron job for the scheduler to run independently.  Scheduler's cron
is at /scheduler/cron; a sample crontab entry to run scheduler every minute
would look like:

* * * * * /usr/bin/wget -O - -q "http://example.com/scheduler/cron"


FEEDS INTEGRATION
--------------------------------------------------------------------------
The module provides integration with the Feeds module [1]. In order to set
scheduling dates for publishing or unpublishing imported content you can map the
source date fields to the "Scheduler: publish on" and "Scheduler: unpublish on"
targets. Make sure the source date fields are using formats that are compatible
with the PHP strtotime() function [2]. If needed the date format can be altered
by writing a custom FeedsProcessor plugin [3] or by using the Feeds Tamper
module [4].

[1] Feeds module: https://www.drupal.org/project/feeds
[2] PHP strtotime() function: http://php.net/manual/en/function.strtotime.php
[3] The developer's guide to Feeds: https://www.drupal.org/node/622700
[4] Feeds Tamper module: https://www.drupal.org/project/feeds_tamper
Metatag
-------
This module allows you to automatically provide structured metadata, aka "meta
tags", about your website and web pages.

In the context of search engine optimization, providing an extensive set of
meta tags may help improve your site's & pages' ranking, thus may aid with
achieving a more prominent display of your content within search engine
results. Additionally, using meta tags can help control the summary content
that is used within social networks when visitors link to your site,
particularly the Open Graph submodule for use with Facebook, Pinterest,
LinkedIn, etc (see below).

This version of the module only works with Drupal 7.28 and newer.


Features
------------------------------------------------------------------------------
The primary features include:

* The current supported basic meta tags are ABSTRACT, DESCRIPTION, CANONICAL,
  GENERATOR, GEO.PLACENAME, GEO.POSITION, GEO.REGION, ICBM IMAGE_SRC, KEYWORDS,
  PUBLISHER, REFRESH, REVISIT-AFTER, RIGHTS, ROBOTS, SHORTLINK, and the page's
  TITLE tag.

* Multi-lingual support using the Entity Translation module.

* Translation support using the Internationalization (i18n) module.

* Full support for entity revisions and workflows based upon revision editing,
  including compatibility with the Revisioning and Workbench Moderation modules.

* Automatically extracts URLs from image fields, no need for extra modules.

* Per-path control over meta tags using the "Metatag: Context" submodule
  (requires the Context module).

* Integration with the Views module allowing meta tags to be controlled for
  individual Views pages, with each display in the view able to have different
  meta tags, by using the "Metatag: Views" submodule.

* Integration with the Panels module allowing meta tags to be controlled for
  individual Panels pages, by using the "Metatag: Panels" submodule.

* The fifteen Dublin Core Basic Element Set 1.1 meta tags may be added by
  enabling the "Metatag: Dublin Core" submodule.

* Forty additional Dublin Core meta tags may be added by enabling the "Metatag:
  Dublin Core Advanced" submodule.

* The Open Graph Protocol meta tags, as used by Facebook, Pinterest, LinkedIn
  and other sites, may be added by enabling the "Metatag: Open Graph" submodule.

* Twenty six additional Open Graph Protocol meta tags are provided for
  describing products in the "Metatag: Open Graph Products" submodule.

* The Twitter Cards meta tags may be added by enabling the "Metatag: Twitter
  Cards" submodule.

* Certain meta tags used by Google+ may be added by enabling the "Metatag:
  Google+" submodule.

* Facebook's fb:app_id and fb:admins meta tags may be added by enabling the
  "Metatag: Facebook" submodule. These are useful for sites which are using
  Facebook widgets or are building custom integration with Facebook's APIs,
  but they are not needed by most sites and have no bearing on the Open Graph
  meta tags.

* The App Links meta tags may be added by enabling the Metatag: App Links
  submodule.

* Site verification meta tags can be added, e.g. as used by the Google search
  engine to confirm ownership of the site; see the "Metatag: Verification"
  submodule.

* The MobileOptimized, HandheldFriendly, viewport, cleartype and theme-color
  meta tags are available via the Metatag: Mobile & UI Adjustments submodule.

* A variety of favicon sizes and styles can be added to the global configuration
  using the Metatag: Favicons submodule.

* An API allowing for additional meta tags to be added, beyond what is provided
  by this module - see metatag.api.php for full details.

* Support for the Migrate module for migrating data from another system - see
  metatag.migrate.inc for full details.

* Support for the Feeds module for importing data from external data sources or
  file uploads.

* Integrates with Devel_Generate, part of the Devel module, to automatically
  generate meta tags for generated nodes, via the Metatag:Devel submodule.

* Integrates with Workbench Moderation (both v1 and v2) allowing meta tags on
  nodes to be managed through the workflow process.

* The Transliteration module (see below) is highly recommended when using image
  meta tags, e.g. og:image, to ensure that filenames are HTML-safe.

* Adds an extra item to the "Flush all caches" menu for the Admin Menu module,
  allowing for a quick way to clear the Metatag module's custom caches.

* A custom pane, called "Node form meta tags", is available for adding the meta
  tags fieldset when the node_edit page is customized using Panels; the
  Metatag: Panels submodule does not need to be enabled in order for this to
  work.

* Several advanced options may be controlled via the Settings page.

* An import script is provided in the Metatag:Importer submodule for D6 sites
  that used Nodewords and need to migrate the data.


Configuration
------------------------------------------------------------------------------
 1. On the People Permissions administration page ("Administer >> People
    >> Permissions") you need to assign:

    - The "Administer meta tags" permission to the roles that are allowed to
      access the meta tags admin pages to control the site defaults.

    - The "Edit meta tags" permission to the roles that are allowed to change
      meta tags on each individual page (node, term, etc).

 2. The main administrative page controls the site-wide defaults, both global
    settings and defaults per entity (node, term, etc), in addition to those
    assigned specifically for the front page:
      admin/config/search/metatags

 3. The list of supported entity types (nodes, taxonomy terms, etc) and bundles
    (content types, vocabularies, etc) may be controlled from the Settings page:
      admin/config/search/metatags/settings

 4. In order to provide a specific configuration per entity bundle (content
    type, vocabulary, etc), click "Add a Metatag default".

 5. Each supported entity object (nodes, terms, users) will have a set of meta
    tag fields available for customization on their respective edit page, these
    will inherit their values from the defaults assigned in #2 above. Any
    values that are not overridden per object will automatically update should
    the defaults be updated.

 6. As the meta tags are output using Tokens, it may be necessary to customize
    the token display for the site's entities (content types, vocabularies,
    etc). To do this go to e.g., admin/structure/types/manage/article/display,
    in the "Custom Display Settings" section ensure that "Tokens" is checked
    (save the form if necessary), then to customize the tokens go to:
    admin/structure/types/manage/article/display/token


Internationalization: i18n.module
------------------------------------------------------------------------------
All default configurations may be translated using the Internationalization
(i18n) module. The custom strings that are assigned to e.g., the "Global: Front
page" configuration will show up in the Translate Interface admin page
(admin/config/regional/translate/translate) and may be customized per language.


Fine Tuning
------------------------------------------------------------------------------
All of these may be controlled from the advanced settings page:
admin/config/search/metatags/settings

* It is possible to "disable" the meta tags provided by Drupal core, i.e.
  "generator", "canonical URL" and "shortlink", though it may not be completely
  obvious. Metatag takes over the display of these tags, thus any changes made
  to them in Metatag will supercede Drupal's normal output. To hide a tag, all
  that is necessary is to clear the default value for that tag, e.g. on the
  global settings for nodes, which will result in the tag not being output for
  those pages.
* By default Metatag will load the global default values for all pages that do
  not have meta tags assigned via the normal entity display or via Metatag
  Context. This may be disabled by setting the variable 'metatag_load_all_pages'
  to FALSE through one of the following methods:
  * Use Drush to set the value:
    drush vset metatag_load_all_pages FALSE
  * Hardcode the value in the site's settings.php file:
    $conf['metatag_load_all_pages'] = FALSE;
  To re-enable this option simply set the value to TRUE.
* By default users will be able to edit meta tags on forms based on the 'Edit
  meta tags' permission. The 'metatag_extended_permissions' variable may be set
  to TRUE to give each individual meta tag a separate permission. This allows
  fine-tuning of the site's editorial control, and for rarely-used fields to be
  hidden from most users. Note: The 'Edit meta tags' permission is still
  required otherwise none of the meta tag fields will display at all. The
  functionality may be disabled again by either removing the variable or
  setting it to FALSE.
* Each entity type (nodes, terms, users, etc) & bundle (content types,
  vocabularies, etc) may have its Metatag integration enabled & disabled from
  the Settings page.
  These UI options correspond to variables. To enable an entity or bundle just
  assign a variable 'metatag_enable_{$entity_type}' or
  'metatag_enable_{$entity_type}__{$bundle}' the value FALSE, e.g.:
    // Disable metatags for files (file_entity module).
    $conf['metatag_enable_file'] = FALSE;
    // Disable metatags for carousel nodes, but leave it enabled for all other
    // content types.
    $conf['metatag_enable_node__carousel'] = FALSE;
  To enable the entity and/or bundle simply set the value to TRUE or remove the
  settings.php line. Note that the Metatag cache will need to be cleared after
  changing these settings, specifically the 'info' records, e.g., 'info:en'; a
  quick version of doing this is to clear the site caches using either Drush,
  Admin Menu (flush all caches -> Metatag), or the "Clear all caches" button on
  admin/config/development/performance. Changing these from the Settings page
  automatically clears the cache.
* By default Metatag will not display meta tags on admin pages. To enable meta
  tags on admin pages simply set the 'metatag_tag_admin_pages' variable to TRUE
  through one of the following methods:
  * Use Drush to set the value:
    drush vset metatag_tag_admin_pages TRUE
  * Hardcode the value in the site's settings.php file:
    $conf['metatag_tag_admin_pages'] = TRUE;
  To re-enable this option simply set the value to FALSE or delete the
  settings.php line.
* When loading an entity with multiple languages for a specific language the
  meta tag values saved for that language will be used if they exist, otherwise
  values assigned to the entity's default language will be used. This
  may be disabled using the enabling the "Don't load entity's default language
  values if no languages match" option on the Settings page, which will cause
  default values to be used should there not be any values assigned for the
  current requested language.
* When using Features to export Metatag configurations, it is suggested to
  override all of the default configurations and then disable the default
  configurations via the advanced settings page; doing so will avoid potential
  conflicts of the same configurations being loaded by both the Metatag module
  and the new Features-based modules.
* By default all meta tag output for individual entities will be cached in a
  separate cache table. This may be disabled by unchecking the "Cache meta tag
  output" option on the Settings page, which will cause all meta tags for
  entities to be generated uniquely for each page load. Note: the entity
  configuration and output for other types of pages will still be cached, but
  this can stop the {cache_metatag} table from growing out of control in some
  scenarios.


Developers
------------------------------------------------------------------------------
Full API documentation is available in metatag.api.php.

It is not necessary to control Metatag via the entity API, any entity that has
view modes defined and is not a configuration entity is automatically suitable
for use.

The meta tags for a given entity object (node, etc) can be obtained as follows:
  $metatags = metatags_get_entity_metatags($entity_id, $entity_type, $langcode);
The result will be a nested array of meta tag structures ready for either output
via drupal_render(), or examining to identify the actual text values.


Troubleshooting / Known Issues
------------------------------------------------------------------------------
* When using custom page template files, e.g., page--front.tpl.php, it is
  important to ensure that the following code is present in the template file:
    <?php render($page['content']); ?>
  or
    <?php render($page['content']['metatags']); ?>
  Without one of these being present the meta tags will not be displayed.
* An alternative method to fixing the missing-tags problem is to change the page
  region used to output the meta tags. The region used may be controlled from
  the settings page, it is recommended to test different options to identify the
  one that works best for a specific site.
* Versions of Drupal older than v7.17 were missing necessary functionality for
  taxonomy term pages to work correctly.
* Using Metatag with values assigned for the page title and the Page Title
  module simultaneously can cause conflicts and unexpected results.
* When customizing the meta tags for user pages, it is strongly recommended to
  not use the [current-user] tokens, these pertain to the person *viewing* the
  page and not e.g., the person who authored a page.
* Certain browser plugins, e.g., on Chrome, can cause the page title to be
  displayed with additional double quotes, e.g., instead of:
    <title>The page title | My cool site</title>
  it will show:
    <title>"The page title | My cool site"</title>
  The solution is to remove the browser plugin - the page's actual output is not
  affected, it is just a problem in the browser.
* Drupal core versions before v7.33 had a bug which caused validation problems
  in the Open Graph output if the RDF module was also enabled. The solution is
  to update to core v7.33 or newer.
* If the Administration Language (admin_language) module is installed, it is
  recommended to disable the "Force language neutral aliases" setting on the
  Admin Language settings page, i.e. set the "admin_language_force_neutral"
  variable to FALSE. Failing to do so can lead to data loss in Metatag.


Related modules
------------------------------------------------------------------------------
Some modules are available that extend Metatag with additional functionality:

* Transliteration
  https://drupal.org/project/transliteration
  Tidies up filenames for uploaded files, e.g. it can remove commas from
  filenames that could otherwise break certain meta tags.

* Alternative hreflang
  https://www.drupal.org/project/hreflang
  Output <link rel="alternate" hreflang="x" href="http://" /> meta tags for
  each language available on the site.

* Domain Meta Tags
  https://drupal.org/project/domain_meta
  Integrates with the Domain Access module, so each site of a multi-domain
  install can separately control their meta tags.

* Select or Other
  https://drupal.org/project/select_or_other
  Enhances the user experience of the metatag_google_plus and metatag_opengraph
  submodules by allowing the creation of custom itemtype and og:types values.

* Node Form Panes
  https://drupal.org/project/node_form_panes
  Create custom node-edit forms and control the location of the Metatag fields.

* Textimage
  https://drupal.org/project/textimage
  Supports using Textimage's custom tokens in meta tag fields.

* Field Multiple Limit
  https://drupal.org/project/field_multiple_limit
  Allows control over how many items are output in a multi-item field, useful
  with meta tags that only allow for one item but which are assigned from fields
  which accept multiple items, e.g. og:audio and og:video.


Credits / Contact
------------------------------------------------------------------------------
Currently maintained by Damien McKenna [1] and Dave Reid [2]; all initial
development was by Dave Reid.

Ongoing development is sponsored by Mediacurrent [3] and Lullabot [4]. All
initial development was sponsored by Acquia [5] and Palantir.net [6].

The best way to contact the authors is to submit an issue, be it a support
request, a feature request or a bug report, in the project issue queue:
  https://www.drupal.org/project/issues/metatag


References
------------------------------------------------------------------------------
1: https://www.drupal.org/u/damienmckenna
2: https://www.drupal.org/u/dave-reid
3: http://www.mediacurrent.com/
4: http://www.lullabot.com/
5: http://www.acquia.com/
6: http://www.palantir.net/
Metatag: App Links
------------------
This module adds the App Links meta tags, provided by the applinks.org [1].

The following tags are provided:
* al:android:package
* al:android:url
* al:android:class
* al:android:app_name
* al:ios:url
* al:ios:app_store_id
* al:ios:app_name
* al:ipad:url
* al:ipad:app_store_id
* al:ipad:app_name
* al:iphone:url
* al:iphone:app_store_id
* al:iphone:app_name
* al:windows_phone:url
* al:windows_phone:app_id
* al:windows_phone:app_name
* al:windows:url
* al:windows:app_id
* al:windows:app_name
* al:windows_universal:url
* al:windows_universal:app_id
* al:windows_universal:app_name
* al:web:url
* al:web:should_fallback


Credits
------------------------------------------------------------------------------
The initial development was by Andrew Berry [2].


References
------------------------------------------------------------------------------
1: http://applinks.org/
2: https://www.drupal.org/u/deviantintegral
Metatag: Dublin Core
--------------------
This module adds the fifteen Dublin Core Metadata Element Set [1] to the
available meta tags, as defined by the Dublin Core Metadata Institute [2]. Forty
additional tags may be added via the Metatag: Dublin Core Advanced submodule.

The following tags are provided:
* dcterms.contributor
* dcterms.coverage
* dcterms.creator
* dcterms.date
* dcterms.description
* dcterms.format
* dcterms.identifier
* dcterms.language
* dcterms.publisher
* dcterms.relation
* dcterms.rights
* dcterms.source
* dcterms.subject
* dcterms.title
* dcterms.type


Credits
------------------------------------------------------------------------------
The initial development was by Marty2081 [3] (sponsored by Gemeentemuseum Den
Haag. [4]), with contributions by many in the community [5].


References
------------------------------------------------------------------------------
1: http://www.dublincore.org/documents/dces/
2: http://www.dublincore.org/
3: https://www.drupal.org/u/marty2081
4: http://www.gemeentemuseum.nl/
5: https://www.drupal.org/node/1491616
Metatag: Importer
-----------------
This module imports data from other modules. An administrative interface is
provided (admin/config/search/metatags/importer), as well as a series of Drush
commands:
* metatag-convert-page-title - Convert data from the Page Title module.


Known Issues
--------------------------------------------------------------------------------
- The admin page (currently) only supports migrating data from Nodewords.
- The Drush commands (currently) only supports migrating data from Page Title.
- Only entities are currently supported, other configuration types will be
  supported soon.


Credits / Contact
--------------------------------------------------------------------------------
Currently maintained by Damien McKenna [1]. Originally developed by jantoine [2]
with contributions by drupalninja99 [3], stuart.crouch [4], subhojit777 [5],
KarlShea [6], stefan.r [7], HyperGlide [8] and jenlampton [9].



References
--------------------------------------------------------------------------------
1: https://www.drupal.org/u/damienmckenna
2: https://www.drupal.org/u/jantoine
3: https://www.drupal.org/u/drupalninja99
4: https://www.drupal.org/u/stuart.crouch
5: https://www.drupal.org/u/subhojit777
6: https://www.drupal.org/u/karlshea
7: https://www.drupal.org/u/stefan.r
8: https://www.drupal.org/u/hyperglide
9: https://www.drupal.org/u/jenlampton
Metatag: Panels
-----------------
This module adds support for meta tag configuration for Panels pages.

Configuration is done within the "Metatag" tab existent in the Page Manager
variant configuration page.


Known Issues
--------------------------------------------------------------------------------
- Only contexts of a type that is supported by the Token API work.
- Only one context for each type is currently supported. If you have two 'node'
contexts, only the first node is elligible for replacement.


Credits / Contact
--------------------------------------------------------------------------------
Originally developed by Diogo Correia [1] and sponsored by DRI — Discovery / Reinvention / Integration [2].

This module is based on Panels Breadcrumbs [3] and the Meta tag: Context module.


References
--------------------------------------------------------------------------------
1: https://www.drupal.org/u/devuo
2: http://dri-global.com
3: https://www.drupal.org/project/panels_breadcrumbs
Metatag: Twitter Cards
----------------------
This module adds the fourteen basic Twitter Cards meta tags [1]. The following
tags are provided:

* twitter:card
* twitter:site
* twitter:creator
* twitter:url
* twitter:title
* twitter:description
* twitter:image:src
* twitter:image:width
* twitter:image:height
* twitter:player
* twitter:player:width
* twitter:player:height
* twitter:player:stream
* twitter:player:stream:content_type


Usage
------------------------------------------------------------------------------
The Twitter Cards meta tags are configured along with all other meta tags;
on-form help is provided to aid with configuring the meta tags.

After enabling and configuring the meta tags it is important to first test [2]
the meta tags for compliance with Twitter's standards, and then apply [3] to
have your site's usage approved.


Credits
------------------------------------------------------------------------------
The initial development was by nico059 [4] with contributions by many in the
community [5].


References
------------------------------------------------------------------------------
1: https://dev.twitter.com/docs/cards
2: https://dev.twitter.com/docs/cards/preview
3: https://www.drupal.org/u/marty2081
4: http://www.gemeentemuseum.nl/
5: https://www.drupal.org/node/1664322
Metatag: Dublin Core Advanced
-----------------------------
This module adds the forty additional Dublin Core Metadata tags to the available
meta tags, as defined by the Dublin Core Metadata Institute [1]; it also adds
forty tags which may be useful for certain sites.

Additional DCMI Metadata Terms meta tags:
* dcterms.abstract
* dcterms.accessRights
* dcterms.accrualMethod
* dcterms.accrualPeriodicity
* dcterms.accrualPolicy
* dcterms.alternative
* dcterms.audience
* dcterms.available
* dcterms.bibliographicCitation
* dcterms.conformsTo
* dcterms.created
* dcterms.dateAccepted
* dcterms.dateCopyrighted
* dcterms.dateSubmitted
* dcterms.educationLevel
* dcterms.extent
* dcterms.hasFormat
* dcterms.hasPart
* dcterms.hasVersion
* dcterms.instructionalMethod
* dcterms.isFormatOf
* dcterms.isPartOf
* dcterms.isReferencedBy
* dcterms.isReplacedBy
* dcterms.isRequiredBy
* dcterms.isVersionOf
* dcterms.issued
* dcterms.license
* dcterms.mediator
* dcterms.medium
* dcterms.modified
* dcterms.provenance
* dcterms.references
* dcterms.replaces
* dcterms.requires
* dcterms.rightsHolder
* dcterms.spatial
* dcterms.tableOfContents
* dcterms.temporal
* dcterms.valid


References
------------------------------------------------------------------------------
1: http://www.dublincore.org/
Metatag: Verification
---------------------
This module adds meta tags used to confirm ownership of the site with various
search engines and online services.


Usage
------------------------------------------------------------------------------
These tags are only available on the Global configuration section of the main
settings interface at admin/config/search/metatag as they affect the site as a
whole rather than portions of it.


Credits
------------------------------------------------------------------------------
Development and maintenance by Damien McKenna.
Metatag Context
---------------
This module is provides a Metatag reaction for Context [1], thus allowing meta
tags to be assigned to specific paths and other conditions.

Configuration can controlled via the normal Context UI module or the new admin
page available at: admin/config/search/metatags/context

Included with the module are default Context configurations that may be enabled
from the Context UI admin page and then customized as necessary. The included
configurations are:
  * user_login - for anonymous users accessing the user and user/login pages.
  * user_register - for anonymous users accessing the user registration page.
  * forum - for the main forum page from the Forum module. Topic pages are
    handled as regular nodes, sub-forum pages are handled as regular term pages.
  * blog - for the main blog page. Note: it does not cover the per-user blog
    pages too.


Credits
------------------------------------------------------------------------------
This module is based on the Context Metadata [2] module. The initial
development was by Marcin Pajdzik [3] (sponsored by Dennis Publishing [4]).


References
------------------------------------------------------------------------------
1: https://www.drupal.org/project/context
2: https://www.drupal.org/project/context_metadata
3: https://www.drupal.org/u/marcin-pajdzik
4: http://www.dennis.co.uk/
Metatag: Google+
-----------------
This module adds support for meta tag configuration for Google+ Snippet [1].

The following Google+ tags are provided:

* itemprop:name
* itemprop:description
* itemprop:image

Also itemtype is provided to add schema in the HTML markup as follows:

<html itemscope itemtype="http://schema.org/Article">


Usage
--------------------------------------------------------------------------------
Page type (itemtype) provides default type options from the Google+ Snippet page
[1]; to add other types either install select_or_other module [2] or use the
Metatag hooks (see metatag.api.php).


Known Issues
--------------------------------------------------------------------------------
- When using Zen or its derived theme, the RDF Namespaces will be serialized
  into an RDFa 1.1 prefix attribute, which means itemtype will be included in
  prefix="...". To avoid this problem, this module will not add a itemtype
  directly to $variable['rdf_namespaces'], instead, it will be necessary to add
  code manually in the template.php or the custom theme.

  Example code to use and adapt as needed:

/**
 * Implements template_preprocess_html().
 *
 * Add itemtype code for Google+ in the 'html_attributes_array' which is only
 * available in Zen theme. Note Zen will convert rdf_namespaces to RDFa 1.1 with
 * prefix, so putting itemtype there will cause it to be added to the
 * prefix="itemtype=..." attribute.
 *
 * @see zen_preprocess_html()
 */
function MYTHEME_preprocess_html(&$variables, $hook) {
  if (module_exists('metatag_google_plus') && isset($variables['itemtype'])) {
    $variables['html_attributes_array']['itemscope itemtype'] = "http://schema.org/{$variables['itemtype']}";
  }
}


Credits / Contact
--------------------------------------------------------------------------------
Originally developed by Eric Chen [3] and sponsored by Monkii [4].


References
--------------------------------------------------------------------------------
1: https://developers.google.com/+/web/snippet/
2. https://drupal.org/project/select_or_other
3: https://drupal.org/user/265729
4: http://monkii.com
Metatag: Views
----------------
This module adds support for meta tag configuration for Views pages.

Configuration is done within the "Metatag" section of the Page Settings in
the Views UI configuration page.


Credits / Contact
--------------------------------------------------------------------------------
Originally developed by Dave Reid [1].


References
--------------------------------------------------------------------------------
1: https://www.drupal.org/u/dave-reid

--------------------------------------------------------------------------------
                                 Rules
--------------------------------------------------------------------------------

Maintainers:
 * Wolfgang Ziegler (fago), nuppla@zites.net

The Rules module allows site administrators to define conditionally executed
actions based on occurring events (ECA-rules).

Project homepage: http://drupal.org/project/rules


Installation
------------

*Before* starting, make sure that you have read at least the introduction - so
you know at least the basic concepts. You can find it here:

                      http://drupal.org/node/298480

 * Rules depends on the Entity API module, download and install it from
   http://drupal.org/project/entity
 * Copy the whole rules directory to your modules directory
   (e.g. DRUPAL_ROOT/sites/all/modules) and activate the Rules and Rules UI
   modules.
 * The administrative user interface can be found at admin/config/workflow/rules


Documentation
-------------
* Check out the general docs at http://drupal.org/node/298476
* Check out the developer targeted docs at http://drupal.org/node/878718


Rules Scheduler
---------------

 * If you enable the Rules scheduler module, you get new actions that allow you
   to schedule the execution of Rules components.
 * Make sure that you have configured cron for your drupal installation as cron
   is used for scheduling the Rules components. For help see
   http://drupal.org/cron
 * If the Views module (http://drupal.org/project/views) is installed, the module
   displays the list of scheduled tasks in the UI.


Upgrade from Rules 6.x-1.x to Rules 7.x-2.x
--------------------------------------------

 * In order to upgrade Rules from 6.x-1.x to 7.x-2.x just run "update.php". This
   is going to make sure Rules 2.x is properly installed, but it will leave your
   Rules 1.x configurations untouched. Thus, your rules won't be upgraded yet.
 * To convert your Rules 1.x configurations to Rules 2.x go to
   'admin/config/workflow/rules/upgrade'.
     * At this page, you may choose the Rules 1.x rules and rule sets to upgrade
       and whether the converted configurations should be immediately saved to
       your database or whether the configuration export should be generated.
     * Note that for importing an export the export needs to pass the
       configuration integrity check, what might be troublesome if the
       conversion was not 100% successful. In that case, try choosing the
       immediate saving method and correct the configuration after conversion.  
     * A rule configuration might require multiple modules to be in place and
       upgraded to work properly. E.g. if you used an action provided
       by a third party module, make sure the module is in place and upgraded
       before you convert the rule.
     * If all required modules are installed and have been upgraded but the rule
       conversion still fails, the cause might be that a module has not yet
       upgraded its Rules integration or does not implement the Rules conversion
       functionality. In that case, file an issue for the module that provided
       the action or condition causing the conversion to fail.
     * Note that any rule configurations containing token replacements or PHP
       input evaluations might need some manual corrections in order to stay
       working. This is, as some used token replacements might not be available
       in Drupal 7 any more and the PHP code might need to be updated in order
       to be compatible with Drupal 7.
     * Once the upgrade was successful, you may delete the left over Rules 1.x
       configurations by going to 'admin/config/workflow/rules/upgrade/clear'.
  * The Rules Scheduler module also comes with an upgrade routine that is
    invoked as usual via "update.php". Its actions can be upgraded via the usual
    Rules upgrade tool, see above.
    However, there is currently no support for upgrading already scheduled
    tasks. That means, all previously on Drupal 6 scheduled tasks won't apply
    for Drupal 7. The Drupal 6 tasks are preserved in the database as long as
    you do not clear your Rules 1.x configuration though.
  * The Rules Forms module has not been updated to Drupal 7 and there are no
    plans to do so, as unfortuntely the module's design does not allow for
    automatic configuration updates.
    Thus, a possible future Rules 2.x Forms module is likely to work
    different, e.g. by working only for entity forms on the field level.

----------------------------------
ADVANCED CSS/JS AGGREGATION MODULE
----------------------------------


CONTENTS OF THIS FILE
---------------------

 - Features & benefits
 - Configuration
 - JSMin PHP Extension
 - JavaScript Bookmarklet
 - Technical Details & Hooks
 - How to get a high PageSpeed score
 - nginx Configuration
 - Troubleshooting


FEATURES & BENEFITS
-------------------

**Advanced CSS/JS Aggregation core features**

 - On demand generation of CSS/JS Aggregates. If the file doesn't exist it will
   be generated on demand.
 - Stampede protection for CSS and JS aggregation. Uses locking so multiple
   requests for the same thing will result in only one thread doing the work.
 - Fully cached CSS/JS assets allow for zero file I/O if the Aggregated file
   already exists. Results in better page generation performance.
 - Smarter aggregate deletion. CSS/JS aggregates only get removed from the
   folder if they have not been used/accessed in the last 30 days.
 - Smarter cache flushing. Scans all CSS/JS files that have been added to any
   aggregate; if that file has changed then flush the correct caches so the
   changes go out. The new name ensures changes go out when using CDNs.
 - One can add JS to any region of the theme & have it aggregated.
 - Url query string to turn off aggregation for that request. ?advagg=0 will
   turn off file aggregation if the user has the "bypass advanced aggregation"
   permission. ?advagg=-1 will completely bypass all of Advanced CSS/JS
   Aggregations modules and submodules. ?advagg=1 will enable Advanced CSS/JS
   Aggregation if it is currently disabled.
 - Button on the admin page for dropping a cookie that will turn off file
   aggregation. Useful for theme development.
 - Gzip support. All aggregated files can be pre-compressed into a .gz file and
   served from Apache. This is faster then gzipping the file on each request.

**Included submodules**

 - advagg_bundler:
   Smartly groups files together - given a target number of CSS/JS aggregates,
   this will try very hard to meet that goal.
 - advagg_css_cdn:
   Load CSS libraries from a public CDN; currently only supports Google's CDN.
 - advagg_css_compress:
   Compress the compiled CSS files using a 3rd party compressor; currently
   supports YUI (included).
 - advagg_js_cdn:
   Load JavaScript libraries from a public CDN; currently only supports Google's
   CDN.
 - advagg_js_compress:
   Compress the compiled JavaScript files using a 3rd party compressor;
   currently supports JSMin+ (included).
 - advagg_mod:
   Includes additional tweaks that may not work for all sites:
   - Force preprocessing for all CSS/JS.
   - Move JS to footer.
   - Add defer tag to all JS.
   - Inline all CSS/JS for given paths.
   - Use a shared directory for a unified multisite.
 - advagg_validator:
   Validate all CSS files using jigsaw.w3.org. Check all CSS files with CSSLint.
   Check all JS files with JSHint.


CONFIGURATION
-------------

Settings page is located at:
`admin/config/development/performance/advagg`

**Global Options**

 - Enable Advanced Aggregation: Check this to start using this module. You can
   also quickly disable the module here. For testing purposes, this has the same
   effect as placing ?advagg=-1 in the URL. Disabled by default.
 - Create .gz files: Check this by default as it will improve your performance.
   For every Aggregated file generated, this will create a gzip version of file
   and then only serve it out if the browser accepts gzip files compression.
   Enabled by default.
 - Use Cores Grouping Logic: Leave this checkbox enabled until you are ready to
   begin exploring the AdvAgg Bundler sub-module which overrides Core's
   functionality. This groups files just like Core does so should just work.
   Enabled by default. You will also have to disable this checkbox if you wish
   to enable some of the CSS Options below on this settings page.
 - Use HTTPRL to generate aggregates: If the HTTPRL module is enabled -
   https://drupal.org/project/httprl - advagg will use it to generate aggregates
   on the fly in a background parallel process. Enabling HTTPRL will improve
   page generation speeds when a new aggregate is created because the CSS/JS
   file creation will happen in a different process. If HTTPRL is installed it
   is Enabled by default; otherwise is it Disabled.
 - AdvAgg Cache Settings: As a reference, core takes about 25 ms to run.
   Development will scan all files for a change on every page load. Normal is
   fine for all use cases. Aggressive should be fine in almost all use cases;
   if your inline css/js changes based off of a variable then the aggressive
   cache hit ratio will be low; if that is the case consider using
   Drupal.settings for a better cache hit ratio.

**CSS Options & JS Options**

 - Combine CSS files by using media queries: "Use cores grouping logic" needs to
   be unchecked in order for this to work. Also noted is that due to an issue
   with IE9, compatibility mode is forced off if this is enabled by adding this
   tag in the html head:

       <!--[if IE]>
       <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
       <![endif]-->

   Disabled by default.
 - Prevent more than 4095 CSS selectors in an aggregated CSS file: Internet
   Explorer before version 10; IE9, IE8, IE7, & IE6 all have 4095 as the limit
   for the maximum number of css selectors that can be in a file. Enabling this
   will prevent CSS aggregates from being created that exceed this limit. For
   more information see
   http://blogs.msdn.com/b/ieinternals/archive/2011/05/14/10164546.aspx Disabled
   by default.
 - Fix improperly set type (CSS/JS): If type is external but does not start with
   http, https, or // change it to be type file. If type is file but it starts
   with http, https, or // change type to be external.

**Information page**

located at `admin/config/development/performance/advagg/info`. This page
provides debugging information. There are no configuration options here.
 - Hook Theme Info: Displays the process_html order. Used for debugging.
 - CSS files: Displays how often a file has changed.
 - JS files: Displays how often a file has changed.
 - Modules implementing AdvAgg CSS/JS hooks: Lets you know what modules are
   using advagg.
 - AdvAgg CSS/JS hooks implemented by modules: Lets you know what advagg hooks
   are in use.
 - Hooks And Variables Used In Hash: Show what is used to calculate the 3rd hash
   of an aggregates filename.
 - Get detailed info about an aggregate file: Look up detailed array about any
   CSS or JS file listed.

**Operations page**

located at `admin/config/development/performance/advagg/operations`. This is a
collection of commands to control the cache and to manage testing of this
module. In general this page is useful when troubleshooting some aggregation
issues. For normal operations, you do not need to do anything on this page below
the Smart Cache Flush. There are no configuration options here.
 - Smart Cache Flush
   - Flush AdvAgg Cache: Scan all files referenced in aggregated files. If
     any of them have changed, increment the counters containing that file and
     rebuild the bundle.

 - Aggregation Bypass Cookie
    - Toggle The "aggregation bypass cookie" For This Browser: This will set or
      remove a cookie that disables aggregation for the remainder of the browser
      session. It acts almost the same as adding ?advagg=0 to every URL.

 - Cron Maintenance Tasks
   - Remove All Stale Files: Scan all files in the advagg_css/js directories and
     remove the ones that have not been accessed in the last 30 days.
   - Clear Missing Files From the Database: Scan for missing files and remove
     the associated entries in the database.
   - Delete Unused Aggregates from Database: Delete aggregates that have not
     been accessed in the last 6 weeks.
   - Delete orphaned/expired advagg locks from the semaphore database table.

 - Drastic Measures
   - Clear All Caches: Remove all data stored in the advagg cache bins.
   - Remove All Generated Files. Remove all files in the advagg_css/js
     directories.
   - Increment Global Counter: Force the creation of all new aggregates by
     incrementing a global counter.

**Hidden Settings**

The following settings are not configurable from the admin UI and must be set in
settings.php. In general they are settings that should not be changed. The
current defaults are shown.

    // Display a message that the bypass cookie is set.
    $conf['advagg_show_bypass_cookie_message'] = TRUE;

    // Skip the 404 check on status page.
    $conf['advagg_skip_404_check'] = FALSE;

    // Force the scripts #aggregate_callback to always be _advagg_aggregate_js.
    $conf['advagg_enforce_scripts_callback'] = TRUE;

    // Default location of AdvAgg configuration items.
    $conf['advagg_admin_config_root_path'] = 'admin/config/development/performance';

    // Run advagg_url_inbound_alter().
    $conf['advagg_url_inbound_alter'] = TRUE;

    // Allow JavaScript insertion into any scope even if theme does not support
    // it.
    $conf['advagg_scripts_scope_anywhere'] = FALSE;

    // Empty the scripts key inside of template_process_html replacement
    // function.
    $conf['advagg_scripts_scope_anywhere'] = FALSE;

    // Do more file operations in main thread if the file system is fast. If
    // AdvAgg's directories are mounted on something like S3, you might want to
    // set this to FALSE.
    $conf['advagg_fast_filesystem'] = TRUE;

    // Pregenerate aggregate files. If disable the browser requesting the file
    // will cause the generation to happen. If advagg 404 handling is broken
    // then setting this to false will break your site in bad ways.
    $conf['advagg_pregenerate_aggregate_files'] = TRUE;

    // Set the jQuery UI version.
    $conf['advagg_css_cdn_jquery_ui_version'] = '1.8.7';

    // See if jQuery UI should be grabbed from the Google CDN.
    $conf['advagg_css_cdn_jquery_ui'] = TRUE;

    // Set the jQuery UI version.
    $conf['advagg_js_cdn_jquery_ui_version'] = '1.8.7';

    // Set the jQuery version.
    $conf['advagg_js_cdn_jquery_version'] = '1.4.4';

    // Use minification.
    $conf['advagg_js_cdn_compression'] = TRUE;

    // See if jQuery UI should be grabbed from the Google CDN.
    $conf['advagg_js_cdn_jquery_ui'] = TRUE;

    // See if jQuery should be grabbed from the Google CDN.
    $conf['advagg_js_cdn_jquery'] = TRUE;

    // Value for the compression ratio test.
    $conf['advagg_js_compress_max_ratio'] = 0.9;

    // Value for the compression ratio test.
    $conf['advagg_js_compress_ratio'] = 0.1;

    // Skip far future check on status page.
    $conf['advagg_skip_far_future_check'] = FALSE;

    // Skip preprocess and enabled checks.
    $conf['advagg_skip_enabled_preprocess_check'] = FALSE;

JSMIN PHP EXTENSION
-------------------

The AdvAgg JS Compress module can take advantage of jsmin.c. JavaScript parsing
and minimizing will be done in C instead of PHP dramatically speeding up the
process. If using PHP 5.3.10 or higher https://github.com/sqmk/pecl-jsmin is
recommended. If using PHP 5.3.9 or lower
http://www.ypass.net/software/php_jsmin/ is recommended.


JAVASCRIPT BOOKMARKLET
----------------------

You can use this JS code as a bookmarklet for toggling the AdvAgg URL parameter.
See http://en.wikipedia.org/wiki/Bookmarklet for more details.

    javascript:(function(){var loc = document.location.href,qs = document.location.search,regex_off = /\&?advagg=-1/,goto = loc;if(qs.match(regex_off)) {goto = loc.replace(regex_off, '');} else {qs = qs ? qs + '&advagg=-1' : '?advagg=-1';goto = document.location.pathname + qs;}window.location = goto;})();


TECHNICAL DETAILS & HOOKS
-------------------------

**Technical Details**

 - There are five database tables and two cache table used by advagg.
   advagg_schema documents what they are used for.
 - Files are generated by this pattern:

       css__[BASE64_HASH]__[BASE64_HASH]__[BASE64_HASH].css

   The first base64 hash value tells us what files are included in the
   aggregate. Changing what files get included will change this value.

   The second base64 hash value is used as a sort of version control; it changes
   if any of the base files contents have changed. Changing a base files content
   (like drupal.js) will change this value.

   The third base64 hash value records what settings were used when generating
   the aggregate. Changing a setting that affects how aggregates get built
   (like toggling "Create .gz files") will change this value.

 - To trigger scanning of the CSS / JS file cache to identify new files, run
   the following:

       // Trigger reloading the CSS and JS file cache in AdvAgg.
       if (module_exists('advagg')) {
         module_load_include('inc', 'advagg', 'advagg.cache');
         advagg_push_new_changes();
       }

 - Aggressive Cache Setting: This will fully cache the rendered html generated
   by AdvAgg. The cache ID is set by this code:

       $hooks_hash = advagg_get_current_hooks_hash();
       $css_cache_id_full = 'advagg:css:full:' . $hooks_hash . ':' . drupal_hash_base64(serialize($full_css));

       $hooks_hash = advagg_get_current_hooks_hash();
       $js_cache_id_full = 'advagg:js:full:' . $hooks_hash . ':' . drupal_hash_base64(serialize($js_scope_array));

   The second and final hash value in this cache id is the css/js_hash value.
   This takes the input from drupal_add_css/js() and creates a hash value from
   it. If a different file is added and/or inline code changed, this hash value
   will be different.

   The first hash value will take the current_hooks_hash value which is the
   third base64 hash value listed above in this section (Technical Details) as
   the first part of the hash. This means that if any value is changed in this
   nested array a different cache id will be used. You can see the contents of
   this nested array by going to
   `admin/config/development/performance/advagg/info` under
   "Hooks And Variables Used In Hash". An example of this being properly used is
   if you enable the core locale module the language key will appear in the
   array. This is needed because the locale_css_alter and locale_js_alter
   functions both use the global $language variable in determining what css or
   js files need to be altered. To add in your own context you can use
   hook_advagg_current_hooks_hash_array_alter to do so. Be careful when doing so
   as including something like the user id will make every user have a different
   set of aggregate files.

**Hooks**

Modify file contents:
 - advagg_get_css_file_contents_alter. Modify the data of each file before it
   gets glued together into the bigger aggregate. Useful for minification.
 - advagg_get_js_file_contents_alter. Modify the data of each file before it
   gets glued together into the bigger aggregate. Useful for minification.
 - advagg_get_css_aggregate_contents_alter. Modify the data of the complete
   aggregate before it gets written to a file. Useful for minification.
 - advagg_get_js_aggregate_contents_alter. Modify the data of the complete
   aggregate before it gets written to a file.Useful for minification.
 - advagg_save_aggregate_alter. Modify the data of the complete aggregate
   allowing one create multiple files from one base file. Useful for gzip
   compression. Also useful for mirroring data.

Modify file names and aggregate bundles:
 - advagg_current_hooks_hash_array_alter. Add in your own settings and hooks
   allowing one to modify the 3rd base64 hash in a filename.
 - advagg_build_aggregate_plans_alter. Regroup files into different aggregates.
 - advagg_css_groups_alter. Allow other modules to modify $css_groups right
   before it is processed.
 - advagg_js_groups_alter. Allow other modules to modify $js_groups right before
   it is processed.

Others:
 - advagg_hooks_implemented_alter. Tell advagg about other hooks related to
   advagg.
 - advagg_get_root_files_dir_alter. Allow other modules to alter css and js
   paths.
 - advagg_modify_css_pre_render_alter. Allow other modules to modify $children
   & $elements before they are rendered.
 - advagg_modify_js_pre_render_alter. Allow other modules to modify $children
   & $elements before they are rendered.
 - advagg_changed_files. Let other modules know about the changed files.
 - advagg_removed_aggregates. Let other modules know about removed aggregates.
 - advagg_scan_for_changes. Let other modules see if files related to this file
   has changed. Useful for detecting changes to referenced images in css.
 - advagg_get_info_on_files_alter. Let other modules modify information about
   the base CSS/JS files.
 - advagg_context_alter. Allow other modules to swap important contextual
   information on generation.
 - advagg_bundler_analysis. If the bundler module is installed allow for other
   modules to change the bundler analysis.


HOW TO GET A HIGH PAGESPEED SCORE
---------------------------------

Go to `admin/config/development/performance/advagg`
 - uncheck "Use cores grouping logic"
 - check "Combine CSS files by using media queries"

Install AdvAgg Modifier if not enabled and go to
`admin/config/development/performance/advagg/mod`
 - Under "Move JS to the footer" Select "All"
 - set "Enable preprocess on all JS/CSS"
 - set "Move JavaScript added by drupal_add_html_head() into drupal_add_js()"
 - set "Move CSS added by drupal_add_html_head() into drupal_add_css()"
 - Enable every checkbox under "Optimize JavaScript/CSS Ordering"

Install AdvAgg Compress Javascript if not enabled and go to
`admin/config/development/performance/advagg/js-compress`
 - Select JSMin if available; otherwise select JSMin+

**Other things to consider**

On the `admin/config/development/performance/advagg/mod` page there is the
setting "Remove unused JavaScript tags if possible". This is a backport of D8
where it will not add any JS to the page if it is not being used.
https://drupal.org/node/1279226

The AdvAgg Bundler module on the
`admin/config/development/performance/advagg/bundler` page. The bundler provides
intelligent bundling of CSS and JS files by grouping files that belong together.
This does what core tried to do; group CSS & JS files together that get used
together. Using this will make your pagespeed score go down as there will be
more css/js files to download but if different css/js files are used on
different pages of your site this will be a net win as a new full aggregate will
not have to be downloaded, instead a smaller aggregate can be downloaded,
ideally with only the css/js that is different on that page. You can select how
many bundles to create and the bundler will do it's best to meet that goal; if
using browser css/js conditionals (js browser conditionals backported from D8
https://drupal.org/node/865536) then the bundler might not meet your set value.


NGINX CONFIGURATION
-------------------

http://drupal.org/node/1116618
Note that @drupal (last line of code below) might be @rewrite or @rewrites
depending on your servers configuration.

    ###
    ### advagg_css and advagg_js support
    ###
    location ~* files/advagg_(?:css|js)/ {
      access_log  off;
      gzip_static on;
      access_log  off;
      expires     max;
      add_header  ETag "";
      add_header  Cache-Control "max-age=31449600, no-transform, public";
      try_files   $uri @drupal;
    }


TROUBLESHOOTING
---------------

If the core Fast 404 Pages functionality is enabled via settings.php, the
settings must be changed in order for the on-demand file compilation to work.
Change this:

    $conf['404_fast_paths_exclude'] = '/\/(?:styles)\//';

to this:

    $conf['404_fast_paths_exclude'] = '/\/(?:styles|advagg_(cs|j)s)\//';

Similarly, if the Fast_404 module is enabled, the 'fast_404_string_whitelisting'
variable must be set inside of settings.php. Add this to your settings.php file:

    $conf['fast_404_string_whitelisting'][] = '/advagg_';


Modules like the Central Authentication Services https://drupal.org/project/cas
will redirect all anonymous requests to a login page. Most of the time there is
a setting that allows certain pages to be excluded from the redirect. You should
add the following to those exclusions. Note that sites/default/files is the
location of you public file system (public://) so you might have to adjust this
to fit your setup. services/* is the default (CAS_EXCLUDE) and
httprl_async_function_callback is needed if httprl will be used.

    services/*
    sites/default/files/advagg_css/*
    sites/default/files/advagg_js/*
    httprl_async_function_callback

In the example of CAS this setting can be found on the `admin/config/people/cas`
page and under Redirection there should be a setting called "Excluded Pages".


If Far-Future headers are not being sent out and you are using Apache here are
some tips to hopefully get it working. For Apache enable mod_rewrite,
mod_headers, and mod_expires. Add the following code to the bottom of Drupal's
core .htaccess file (located at the webroot level).

    <FilesMatch "^(css|js)__[A-Za-z0-9-_]{43}__[A-Za-z0-9-_]{43}__[A-Za-z0-9-_]{43}.(css|js)(\.gz)?">
      # No mod_headers
      <IfModule !mod_headers.c>
        # No mod_expires
        <IfModule !mod_expires.c>
          # Use ETags.
          FileETag MTime Size
        </IfModule>
      </IfModule>

      # Use Expires Directive.
      <IfModule mod_expires.c>
        # Do not use ETags.
        FileETag None
        # Enable expirations.
        ExpiresActive On
        # Cache all aggregated css/js files for 52 weeks after access (A).
        ExpiresDefault A31449600
      </IfModule>

      <IfModule mod_headers.c>
        # Do not use etags for cache validation.
        Header unset ETag
        <IfModule !mod_expires.c>
          # Set a far future Cache-Control header to 52 weeks.
          Header set Cache-Control "max-age=31449600, no-transform, public"
        </IfModule>
        <IfModule mod_expires.c>
          Header append Cache-Control "no-transform, public"
        </IfModule>
      </IfModule>
    </FilesMatch>
    # Force advagg .js file to have the type of application/javascript.
    <FilesMatch "^js__[A-Za-z0-9-_]{43}__[A-Za-z0-9-_]{43}__[A-Za-z0-9-_]{43}.js(\.gz)?">
      ForceType application/javascript
    </FilesMatch>


If pages on the site stop working correctly or looks broken after Advanced
CSS/JS Aggregation is enabled, the first step should be to validate the
individual CSS and/or JS files using the included advagg_validator module -
something as simple as an errant unfinished comment in one file may cause entire
aggregates of files to be ignored.


If AdvAgg was installed via drush sometimes directory permissions need to be
fixed. Using `chown -R` on the advagg directories usually solves this issue.


If hosting on Pantheon, you might need to add this to your settings.php file if
you get Numerous login prompts after enabling Adv Agg module on Pantheon Test
and Live instances.

    if (isset($_SERVER['PANTHEON_ENVIRONMENT'])) {
      // NO trailing slash when setting the $base_url variable.
      switch ($_SERVER['PANTHEON_ENVIRONMENT']) {
        case 'dev':
          $base_url = 'http://dev-sitename.gotpantheon.com';
          break;

        case 'test':
          $base_url = 'http://test-sitename.gotpantheon.com';
          break;

        case 'live':
          $base_url = 'http://www.domain.tld';
          break;
      }
      // Remove a trailing slash if one was added.
      if (!empty($base_url)) {
        $base_url = rtrim($base_url, '/');
      }
    }


If you're getting the "HTTP requests to advagg are not getting though" error,
you can try to fix it by making sure the $base_url is correctly set for
production and not production environments.
/**
 * @file
 * README file for Secure Permissions.
 */

Secure Permissions
Disables the user interface for creating and assigning roles and permissions.

CONTENTS
--------
1.    Use case
2.    Installation
3.    Exporting settings to code
4.    Configuring the module
5.    API Hooks
5.1  hook_secure_permissions_roles()
5.2  hook_secure_permissions($role)
6.    To Do

Secure Permissions is an advanced security module for Drupal 7. Please
read this document before continuing.

This module was inspired by some claims regarding superior security of the
Plone platform. See, in particular, 'Problem A2: Broken Access Control' at
http://plone.org/products/plone/security/overview/security-overview-of-plone

The module was inspired by @djay75 via Twitter.

----
1. Use case

This module is designed for cases where you want control of Roles and
Permissions only in a development environment. When fully enabled, this module
will make it so that the live site cannot have its permissions modified, except
through code.

It may be sufficient for most users to simply enable this module on the live
site, and to disable it when it is no longer needed.

----
2. Installation

Before installing this module you should configure the site Roles and
Permissions as you see fit. After installing and configuring this module,
changes to these settings can only be made through code.

On installation this module will have two immediate effects:

  1. Permissions will no longer be editable through the user interface.
  2. Roles will no longer be editable through the user interface.

On many sites, this is sufficient. However, for advanced security, you
have several additonal options. See sections 3 and 4 for details.

The module will also add a permission to your site, 'Export permission
definitions'. This permission should be given to trusted roles before you
continue.

Users with this permissions may configure this module and may export site
Roles and Permissions to code.

----
3. Exporting settings to code

Give your account the 'Export permission definitions' permission defined by the
module or log in as the Site Maintenance user.

Find the link under People and Permissions >> Secure Permissions

Click the Export Permissions tab. It should take you to a form with two text
areas, filled with PHP code.

The Secure permissions module stores the permissions in a module (file) that is
inaccessible through the user interface.

You now need to create and enable that module in 4 easy steps.

   1. Create directory. cd to /sites/all/modules and issue the command:
       mkdir secure_permissions_data
   2. Create 2 empty files. cd to /sites/all/modules/secure_permissions_data and
       issue the command: touch secure_permissions_data.info secure_permissions_data.module
   3. Copy data. Copy the text from the fields below into the respective files you just
       created using the tools of your choice.
   4. Enable the module. Navigate to admin/build/modules/list and enable your new module.

To change permissions with the module enabled, you must now edit your
secure_permissions_data.module file.

Now you are ready to configure the Secure Permissions module to run.

After editing the file navigate to /admin/user/secure_permissions/view, select
'Load permissions from code'and click 'Save configuration' to update the permissions.

You may rename the module; remember to rename all the functions.

Note that if you have set an administrative role, the permissions for that role will not
be exported.

----
4. Configuring the module

For advanced features of this module, you must export your Roles and Permissions
to code. Since this cannot be done before the module is installed, the module
will not enforce its rules until you tell it to do so.

To activate the module, navigate to:

  Administer > Configuration and Modules > People and Permissions > Secure
  Permissions

Here, you can tell the Secure Permissions module how to behave. You have eight
options that can be set. These are split into two groups, those that control the
User Interface of Drupal, and those that affect how permissions are loaded from
code via the API.

  USER INTERFACE SETTINGS

  'Disable permissions and roles forms'
  Check to make the Roles and Permissions forms unchangeable. Users may
  be able to view them, but cannot edit or submit them. Default is OFF.
  You should enable this setting after granting your account the ability to
  access 'Export permission definitions'.

  'Show permissions page'
  Check to allow the Permissions page to be viewed by administrators.
  Disabling this option will prevent users from seeing permission definitions
  at all. Default is ON.

  'Show roles page'
  Check to allow the Roles page to be viewed by administrators.
  Disabling this option will prevent users from seeing role definitions
  at all. Default is ON.

  'Display permissions updates'
  Check to display messages when Secure Permissions reset site permissions.
  Default is ON.

  API SETTINGS

  'Load permissions from code'
  Check to activate the module's advanced features.
  When set, the module will rebuild Roles and Permissions every time that
  a module is enabled or disabled. Checking this option means that all
  site Roles and Permissions will be managed in code. Default is OFF.

  NOTE: none of the following settings will be in effect if 'Load permissions
  from code' is not enabled. Using these features is not required, however.

  'Reload default permissions on rebuild'
  Check to have the module load Drupal's default permissions for the anonymous
  and authenticated user roles when permissions are rebuilt. Default is OFF.

  'Use administrative role'
  Check to include an administrative role from the site.
  The 'administrator' role ships with Drupal, and has all site permissions. If
  you uncheck this option, this role will be deleted. Default is ON.

  'Administrative role name'
  Set to the name of the administrative role you wish to use.
  If 'Use administrative role' is disabled, this value is not used.
  Default is 'administrator'. Normally, you should not change this value.
  NOTE: If using translations, this string should not be translated through
  this setting.

----
5. API hooks

The module functions by using two API hooks, described below. To use these
functions you must place them in a custom module file and name them properly.

The export function will generate these hooks for you. The API is described
here for developers.

----
5.1 hook_secure_permissions_roles()

Defines the roles used by a site. These are keyed by the uniqueness of the role
name, since we cannot guarantee the role id used by various sites.

WARNING: If you do not implement this hook, the module will reset your site
roles to the roles that ship with Drupal's default install.

Note that the module implements this hook to ensure that the 'anonymous user'
and 'authenticated user' roles always exist.

If the 'Use administrative role' is set to TRUE, the module will also maintain
an administrative role that has all site permissions.

The hook returns a simple positional array of unique role names.

  function example_secure_permissions_roles() {
    return array(
      'editor',
      'producer',
    );
  }

----
5.2 hook_secure_permissions($role)

Defines the permissions assigned to each role. Typically, you will implement
all permissions for your site in this hook.

This hook takes a $role string as an argument. You should respond with the
appropriate permissions grants for that role. You should only return grants
that are TRUE.

  function example_secure_permissions($role) {
    $permissions = array(
      'anonymous user' => array(
        'access content',
        'use text format 1',
      ),
      'authenticated user' => array(
        'access comments',
        'access content',
        'post comments',
        'post comments without approval',
        'use text format 1',
      ),
      'editor' => array(
        'bypass node access',
        'administer nodes',
      ),
      'producer' => array(
        'create page content',
        'edit any page content',
      ),
    );
    if (isset($permissions[$role])) {
      return $permissions[$role];
    }
  }


NOTE: The use of isset() is recommended here, since the hook will fire
once per role, and it is possible that your module will not reply in all cases.

NOTE: If configured to do so, the module will return the default permissions
defined by Drupal's installer. Disable the 'Reload default permissions on
rebuild' setting to disable this behavior.
LiveReload
http://drupal.org/project/livereload
====================================


DESCRIPTION
-----------
LiveReload is a Desktop app + Safari/Chrome/Firefox extension that:
1. Applies CSS and JavaScript file changes without reloading a page.
2. Automatically reloads a page when any other file changes
  (html, image, server-side script, etc).

This module adds a LiveReload javascript to your page, aiming the functuallity
of the Browserplugin. This means that no plugin is needed to use this.
Additionally it gives you the possibilty to load styles with tags instead of
@import, this might be an issue in firefox and orher oler browsers.


REQUIREMENTS
------------
Drupal 7.x
livereload - http://livereload.com/


INSTALLING
----------
1. To install the module copy the 'livereload' folder to your sites/all/modules
   directory.
2. Read more about installing modules at http://drupal.org/node/70151


CONFIGURING AND USING
---------------------
1. Go to admin/people/permissions to give the "Use LiveReload" permission to
   selcted roles.
1. Go to admin/config/development/performance to disable livereload.js manually
   and to force the css to be rendered with <style> instead of @import.


REPORTING ISSUE. REQUESTING SUPPORT. REQUESTING NEW FEATURE
-----------------------------------------------------------
1. Go to the module issue queue at http://drupal.org/project/issues/livereload?text=&status=All
2. Click on CREATE A NEW ISSUE link.
3. Fill the form.
4. To get a status report on your request go to http://drupal.org/project/issues/user
= Masquerade =

The Masquerade module allows users to temporarily switch to another user
account. It keeps a record of the original user account, so users can easily
switch back to the previous account.

== Installation and Configuration ==

To install the Masquerade module, extract the module to your modules folder,
such as sites/all/modules. After enabling the module, it can be configured
under Administer > Configuration > People > Masquerade. To enable users to
masquerade, assign the appropriate "masquerade module" permissions to the roles
available on your site. For example:

 * To allow members of the 'customer support' role to masquerade as any
   non-admin user, add the 'masquerade as user' permission to the role. In the
   Masquerade configuration, set 'administrator' as an administrator role
   to prevent customer support users from masquerading as those users.

 * To allow members of the 'tech support' role to masquerade as 'administrator', add the 'masquerade as admin' permission to the role. Then,
   in the Masquerade configuration, set 'administrator' as an
   administrator role.

== Quick Switch Menu ==

By default, when a user is selected for the 'Menu Quick Switch user', the Masquerade module adds two menu items to the 'Navigation' menu:

 * Masquerade as 'the user selected': When clicked, the user can quick switch to the user selected.

 * Switch back: This menu item appears while masquerading so that you can switch back to your original user.

== Help and Support ==

This module was developed by a number of contributors. For more information
about this module, see:

Project Page: http://drupal.org/project/masquerade
Issue Queue: http://drupal.org/project/issues/masquerade
README.txt
==========

A module containing helper functions for Drupal developers and
inquisitive admins. This module can print a log of
all database queries for each page request at the bottom of each page. The
summary includes how many times each query was executed on a page, and how long
each query took.

 It also offers
 - a block for running custom PHP on a page
 - a block for quickly accessing devel pages
 - a block for masquerading as other users (useful for testing)
 - reports memory usage at bottom of page
 - A mail-system class which redirects outbound email to files
 - more

 This module is safe to use on a production site. Just be sure to only grant
 'access development information' permission to developers.

Also a dpr() function is provided, which pretty prints arrays and strings.
Useful during development. Many other nice functions like dpm(), dvm().

AJAX developers in particular ought to install FirePHP Core from
http://www.firephp.org/ and put it in the devel directory. You may
use the devel-download drush command to download the library. If downloading by hand,
your path to fb.php should look like devel/FirePHPCore/lib/FirePHPCore/fb.php.
You can use svn checkout http://firephp.googlecode.com/svn/trunk/trunk/Libraries/FirePHPCore.
Then you can log php variables to the Firebug console. Is quite useful.

Included in this package is also:

- devel_node_access module which prints out the node_access records for a given node. Also offers hook_node_access_explain for all node access modules to implement. Handy.
- devel_generate.module which bulk creates nodes, users, comment, terms for development.

Some nifty drush integration ships with devel and devel_generate. See drush help for details.

DEVEL GENERATE EXTENSIONS
=========================
Devel Images Provider [http://drupal.org/project/devel_image_provider] allows to configure external providers for images.

COMPATIBILITY NOTES
==================
- Modules that use AHAH may have incompatibility with the query log and other
  footer info. Consider setting $GLOBALS['devel_shutdown'] = FALSE if you run into
  any issues.

DRUSH UNIT TEST
==================
See develDrushTest.php for an example of unit testing of the Drush integration.
This uses Drush's own test framework, based on PHPUnit. To run the tests, use
phpunit --bootstrap=/path/to/drush/tests/drush_testcase.inc. Note that we must name a file
under /tests there.

AUTHOR/MAINTAINER
======================
-moshe weitzman <weitzman at tejasa DOT com>
http://cyrve.com
Hans Salvisberg <drupal at salvisberg DOT com>
README
======

This module contains tools for developers using access control modules
to restrict access to some nodes.  It is intended to help catch some
common mistakes and provide feedback to confirm that restricted nodes
are in fact visible only to the intended users.

Provides a summary page which queries the node_access table and
reports common mistakes such as the presence of Drupal's default entry
which grants all users read access to all nodes.  Also reports the
presence of nodes not represented in node_access table.  This may
occur when an access control module is installed after nodes have
already been created.

Provides a block which shows all node_access entries for the nodes
shown on a given page.  This gives developers a quick check to see
that grants are provided as they should be.  This block auto-enables
to the footer region. You may move it as desired.

If Views module is installed, allows browsing of nodes by realm,
including those nodes not in the node_access table (NULL realm).

WISHLIST
========

Things I'd like to see but haven't had time to do:

* Automatically solve common problems.  I.e. delete the "all" realm
  entry, and automatically save all nodes not in the node_access table.

* Nicer feedback indicating whether nodes are visible to the public or
  not.  I.e. use color coding or icons.

* Summary does not differentiate between view grants and other types
  of grants.  I personally use node_access only for view grants so I'm
  not sure exactly what else it should show.

AUTHOR
======

Dave Cohen AKA yogadex on drupal.org
=============================================================================

                               Krumo
                            version 0.2.1a

=============================================================================

You probably got this package from...
http://www.sourceforge.net/projects/krumo/

If there is no licence agreement with this package please download
a version from the location above. You must read and accept that
licence to use this software. The file is titled simply LICENSE.

OVERVIEW
------------------------------------------------------------------------------
To put it simply, Krumo is a replacement for print_r() and var_dump(). By 
definition Krumo is a debugging tool (for PHP5), which displays structured 
information about any PHP variable.

A lot of developers use print_r() and var_dump() in the means of debugging 
tools. Although they were intended to present human readble information about a 
variable, we can all agree that in general they are not. Krumo is an 
alternative: it does the same job, but it presents the information beautified 
using CSS and DHTML. 

EXAMPLES
------------------------------------------------------------------------------
Here's a basic example, which will return a report on the array variable passed 
as argument to it:

 krumo(array('a1'=> 'A1', 3, 'red'));

You can dump simultaneously more then one variable - here's another example:

 krumo($_SERVER, $_REQUEST);

You probably saw from the examples above that some of the nodes are expandable, 
so if you want to inspect the nested information, click on them and they will 
expand; if you do not need that information shown simply click again on it to 
collapse it. Here's an example to test this:

 $x1->x2->x3->x4->x5->x6->x7->x8->x9 = 'X10';
 krumo($x1);

The krumo() is the only standalone function from the package, and this is 
because basic dumps about variables (like print_r() or var_dump()) are the most 
common tasks such functionality is used for. The rest of the functionality can 
be called using static calls to the Krumo class. Here are several more examples:

 // print a debug backgrace
 krumo::backtrace();

 // print all the included(or required) files
 krumo::includes();
 
 // print all the included functions
 krumo::functions();
 
 // print all the declared classes
 krumo::classes();
 
 // print all the defined constants
 krumo::defines();

 ... and so on, etc.

A full PHPDocumenter API documentation exists both in this package and at the 
project's website.

INSTALL
------------------------------------------------------------------------------
Read the INSTALL file.

DOCUMENTATION
------------------------------------------------------------------------------
As I said, a full PHPDocumenter API documentation can be found both in this
package and at the project's website.

SKINS
------------------------------------------------------------------------------
There are several skins pre-installed with this package, but if you wish you can 
create skins of your own. The skins are simply CSS files that are prepended to 
the result that Krumo prints. If you want to use images in your CSS (for 
background, list-style, etc), you have to put "%URL%" in front of the image URL 
in order hook it up to the skin folder and make the image web-accessible.

Here's an example:

 ul.krumo-first {background: url(%url%bg.gif);}

TODO
------------------------------------------------------------------------------
You can find the list of stuff that is going to be added to this project in the 
TODO file from this very package.

CONTRIBUTION
-----------------------------------------------------------------------------
If you download and use and possibly even extend this tool, please let us know. 
Any feedback, even bad, is always welcome and your suggestions are going to be 
considered for our next release. Please use our SourceForge page for that:
 
 http://www.sourceforge.net/projects/krumo/

-- SUMMARY --

Environment Indicator adds a coloured strip to the site informing the user which
environment they are in (Development, Staging Production etc).

For a full description visit the project page:
  http://drupal.org/project/environment_indicator
  
Bug reports, feature suggestions and latest developments:
  http://drupal.org/project/issues/environment_indicator


-- REQUIREMENTS --

* CTools


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.


-- CONFIGURATION --

You may configure the environment at /admin/settings/environment-indicator

You can also override settings in settings.php, allowing you to have different
settings for each of your environments. If you choose to detect your environment
using settings.php, then all configuration variables can be overridden in
settings.php, but the most common three are:

  - environment_indicator_overwrite
      A boolean value indicating whether the Environment Indicator should use
      the settings.php variables for the indicator. On your production
      environment, you should probably set this to FALSE. e.g:
      $conf['environment_indicator_overwrite'] = FALSE
  - environment_indicator_overwritten_name
      The text that will be displayed on the indicator. e.g:
      $conf['environment_indicator_overwritten_name'] = 'Staging'
  - environment_indicator_overwritten_color
      A valid css color. e.g:
      $conf['environment_indicator_overwritten_color'] = '#ff5555'
  - environment_indicator_overwritten_position
      Where your indicator may appear. Allowed values are "top" and "bottom".
      e.g:
      $conf['environment_indicator_overwritten_position'] = 'top'
  - environment_indicator_overwritten_fixed
      A boolean value indicating whether the Environment Indicator should be
      fixed at the top/bottom of the screen. e.g:
      $conf['environment_indicator_overwritten_fixed'] = FALSE
  - environment_indicator_favicon_overlay
      A boolean value indicating whether the Environment Indicator should
      overlay the favicon with the current environment's information. e.g.:
      $conf['environment_indicator_favicon_overlay'] = TRUE

-- ACQUIA CLOUD INTEGRATION --

Copy the file in samples/environment-indicator.sh to your
hooks/[your-environment]/post-code-deploy folder and give it execution
permissions. Replace [your-environment] by your environment site alias or use
'common' to use it in all your environments (recommended). This integration
relies on the presence of the environment variable AH_SITE_ENVIRONMENT.

You can read more about Cloud Hooks in
https://github.com/acquia/cloud-hooks/blob/master/README.md

-- CONTACT --

Author maintainers:
* Tom Kirkpatrick (mrfelton), www.systemseed.com. Branches 6.x-1.x, 7.x-1.x
* Mateu Aguiló (e0ipso). Branch 7.x-2.x


This project has been partially sponsored by:
* SystemSeed - Visit http://www.systemseed.com for more information. Branches
  6.x-1.x, 7.x-1.x
* Lullabot - Visit http://www.lullabot.com for more information. Branch 7.x-2.x
Description
-----------
This module provides a method for filtering modules on the modules page as well
as for filtering projects on the update status report.

The supplied filter is simpler than using your browsers find feature which
searches the entire page. The provided filter will filter modules/projects that
do not meet your input.

Along with the filter textfield there are additional
checkboxes that help to narrow the search more. The modules page contains four
checkboxes: Enabled, Disabled, Required, and Unavailable. While the first two
are self-explanatory, the latter two can take an explanation. The Required
checkbox affects visibility of modules that are enabled and have other
module(s) that require it also enabled. The Unavailable checkbox affects
visibility of modules that are disabled and depend on module(s) that are
missing.

The update status report filter also contains four checkboxes: Up-to-Date,
Update availabe, Security update, and Unknown. These directly affect the
visibilty of each project; whether it is up-to-date, there is an update
available, a security update is available, or the status is unknown.

Installation
------------
To install this module, do the following:

1. Extract the tar ball that you downloaded from Drupal.org.

2. Upload the entire directory and all its contents to your modules directory.

Configuration
-------------
To enable and configure this module do the following:

1. Go to Admin -> Modules, and enable Module Filter.

2. Go to Admin -> Configuration -> User interface -> Module filter, and make
   any necessary configuration changes. 

Tabs
----
By default Module Filter alters the modules page into tabs (Can be disabled on
configuration page). In the tabs view, each package is converted to a vertical
tab rather than a fieldset which greatly increases the ability to browse them.

There are several benefits to using the tabs view over the standard view for
the modules page. I've listed the key benefits below as well as additional
information that pertains to each.

1.  The increased ease of browsing between packages.

2.  Allows all modules to be listed alphabetically outside of their package,
    making it all the easier to find the module by name rather than package it
    happens to be in.

3.  The operations for a module are moved within the description column giving
    the description more "elbow room".

4.  Filtering is restricted to within the active tab or globally when no tab is
    selected. By default no tab is selected which will list all modules. When a
    tab is active and you want to get back to the 'all' state click on the
    active tab to deselect it.

5.  The number of enabled modules per tab is shown on the active tab. (Can be
    disabled on configuration page)

6.  Nice visual aids become available showing what modules are to be
    enabled/disabled and the number of matching modules in each tab when
    filtering. (Can be disabled on configuration page)

7.  The save configuration button becomes more accessible, either staying at
    the bottom of the window when the tabs exceed past the bottom and at the
    top when scrolling past the tabs. (Can be disabled on configuration page)

8.  When filtering, tabs that do not contain matches can be hidden. (Can be
    enabled on configuration page)

9.  Tab states are remembered like individual pages allowing you to move
    forward and backward within your selections via your browsers
    forward/backward buttons.

10. When viewing all modules (no active tab) and mousing over modules it's tab
    becomes highlighted to signify which tab it belongs to.

Filter operators
----------------
The modules page's filter has three filter operators available. Filter
operators allow alternative filtering techniques. A filter operator is applied
by typing within the filter textfield 'operator:' (where operator is the
operator type) followed immediately with the string to pass to the operator
function (e.g. 'requires:block'). The available operators are:

description:
   Filter based on a module's description.

requiredBy:
   Filter based on what a module is required by.

requires:
   Filter based on what a module requires.

Multiple filters (or queries) can be applied by space delimiting. For example,
the filter string 'description:ctools views' would filter down to modules with
"ctools" in the description and "views" within the module's name. To pass a
space within a single query wrap it within double quotes (e.g. 'requires:"chaos
tools"' or '"bulk export"').
# Create Jira issue for important project updates

Install this module and its dependencies and configure a Jira username
and password either at `admin/config/services/jira_rest` or better in
`settings.php` on the production server:

```php
$conf['jira_rest_username'] = 'marianne';
$conf['jira_rest_password'] = 'correcthorsebatterystaple';
```

Whenever Drupal runs its project update check the module creates an
issue in Jira for newly discovered security updates, revoked modules,
and unsupported modules.

## Dependencies

The dependencies are (including indirect dependencies):

 * `ctools`
 * `entity`
 * `features`
 * `jira_rest`
 * `jira_rest_rules`
 * `rules`
 * `strongarm`
 * `ultimate_cron`
 * `update_rules`
   * Including [patch](https://www.drupal.org/files/issues/update_rules-release_link_for_recommended_release-2477835-4.patch) from [#2477835](https://www.drupal.org/node/2477835).

This directory should be used to place downloaded translations
for installing Drupal core.
# Private folder

This folder is protected by Apache and cannot be accessed via the
webserver.

Use this to place non-public files that must be part of the
repository.

The folder was chosen because this is the only protected part in
Pantheons nginx configuration and we might as well standardize on
that.

Be sure to add it to the `nginx` configuration if you host the site
with nginx elsewhere:

    location /private {
      deny all;
      return 404;
    }
# Behat test be here
# Docker config is here

This directory is reserved for core theme files. Custom or contributed themes
should be placed in their own subdirectory of the sites/all/themes directory.
For multisite installations, they can also be placed in a subdirectory under
/sites/{sitename}/themes/, where {sitename} is the name of your site (e.g.,
www.example.com). This will allow you to more easily update Drupal core files.

For more details, see: http://drupal.org/node/176043


ABOUT STARK
-----------

The Stark theme is provided for demonstration purposes; it uses Drupal's default
HTML markup and CSS styles. It can be used as a troubleshooting tool to
determine whether module-related CSS and JavaScript are interfering with a more
complex theme, and can be used by designers interested in studying Drupal's
default markup without the interference of changes commonly made by more complex
themes.

To avoid obscuring CSS added to the page by Drupal or a contrib module, the
Stark theme itself has no styling, except just enough CSS to arrange the page in
a traditional "Header, sidebars, content, and footer" layout. See the layout.css
file for more information.


ABOUT DRUPAL THEMING
--------------------

To learn how to build your own custom theme and override Drupal's default code,
see the Theming Guide: http://drupal.org/theme-guide

See the sites/all/themes/README.txt for more information on where to place your
custom themes to ensure easy maintenance and upgrades.

This directory is reserved for core module files. Custom or contributed modules
should be placed in their own subdirectory of the sites/all/modules directory.
For multisite installations, they can also be placed in a subdirectory under
/sites/{sitename}/modules/, where {sitename} is the name of your site (e.g.,
www.example.com). This will allow you to more easily update Drupal core files.

For more details, see: http://drupal.org/node/176043

These files are useful in tests that upload files or otherwise need to
manipulate files, in which case they are copied to the files directory as
specified in the site settings. Dummy files can also be generated by tests in
order to save space.
