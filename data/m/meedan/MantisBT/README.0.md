Mantis Bug Tracker (MantisBT)
=============================

[![Build Status](https://img.shields.io/travis/mantisbt/mantisbt/master.svg)](https://travis-ci.org/mantisbt/mantisbt)
[![Gitter](https://img.shields.io/gitter/room/mantisbt/mantisbt.svg)](https://gitter.im/mantisbt/mantisbt?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Meedan-Specific Fork
--------------------

Added the following features to the original repo:

- Patches for modified functionality (see `patches/`)
- Meedan-specific configuration (see `config/`)
- Plugins that Meedan uses (see `plugins/`)
- Docker Compose file for easy development (see `Dockerfile` and `docker-compose.yml`)

Some common tasks:
- Set local configs on your localhost: `cp config/config_inc.local.php.sample config/config_inc.local.php`
- Build the app: `docker-compose build`
- Run the app: `docker-compose run`
- Install Mantis for the first time: http://localhost:8080/admin/install.php (MySQL admin = `root` / `root`, Mantis admin = `administrator` / `root`)
- Load a database dump from the host: `mysql --protocol tcp -umantis -pmantis mantis < mantis-20170110.sql` (assuming you have a local `mysql` client)

What follows is the original documentation from the fork parent.

Screenshots
-----------

![Build Status](doc/modern_view_issues.png)

![Build Status](doc/modern_my_view.png)

![Build Status](doc/modern_view_issue.png)

Documentation
-------------

For complete documentation, please read the administration guide included with
this release in the doc/<lang> directory.  The guide is available in text, PDF,
and HTML formats.


Requirements
------------

 * MySQL 5.5.35+, PostgreSQL 9.2+, or other supported database
 * PHP 5.5.9+
 * a webserver (e.g. Apache or IIS)

Please refer to section 2.2 in the administration guide for further details.

Installation
------------

 * Extract the tarball into a location readable by your web server
 * Point your browser to http://path/to/mantisbt/admin/check/index.php to ensure
   that your webserver is compatible with MantisBT and configured correctly
 * Point your browser to http://path/to/mantisbt/admin/install.php to begin the
   database installation process
 * Select the database type and enter the credentials to access the database
 * Click install/upgrade
 * Installation is complete -- you may need to copy the default configuration
   to mantisbt/config/config_inc.php if your web server does not have write access
 * Remove the admin/ directory from within the MantisBT installation path. The
   scripts within this directory should not be accessible on a live MantisBT
   site or on any installation that is accessible via the Internet.

UPGRADING
---------

 * Backup your existing installation and database -- really!
 * Extract the tarball into a clean directory; do not extract into an existing
   installation, as some files have been moved or deleted between releases
 * Copy your configuration from the old installation to the new directory,
   including config_inc.php, custom_strings_inc.php, custom_relationships_inc.php,
   custom_functions_inc.php and custom_constants_inc.php if they exist
 * Point your browser to http://path/to/mantisbt/admin/check/index.php to ensure that
   your webserver is compatible with MantisBT and configured correctly
 * Point your browser to http://path/to/mantisbt/admin/install.php to upgrade
   the database schema
 * Click install/upgrade
 * Remove the admin/ directory from within the MantisBT installation path. The
   scripts within this directory should not be accessible on a live MantisBT
   site or on any installation that is accessible via the Internet.
 * Upgrading is complete

CONFIGURATION
-------------

This file contains information to help you customize MantisBT.  A more
detailed doc can be found at http://www.mantisbt.org/docs/

* config_defaults_inc.php
  - this file contains the default values for all the site-wide variables.
* config/config_inc.php
  - You should use this file to change config variable values.  Your
    values from this file will be used instead of the defaults.  This file
    will not be overwritten when you upgrade, but config_defaults_inc.php will.
    Look at config/config_inc.php.sample for an example.

* core/*_api.php - these files contains all the API library functions.

* global variables are prefixed by g_
* parameters in functions are prefixed with p_ -- parameters shouldn't be modified within the function.
* form variables are prefixed with f_
* variables that have been cleaned for db insertiong are prefixed with c_
* temporary variables are prefixed with t_.
* count variables have the word count in the variable name

More detail can be seen in the coding guidelines at:
http://www.mantisbt.org/guidelines.php

* The files are split into three basic categories, viewable pages,
include files and pure scripts. Examining the viewable pages (suffix _page)
should make the basic file format fairly easy to see.  The file names
themselves should make their purpose apparent.  The approach used is to break the
work into many small files rather than have a small number of really
large files.

* Most of the action scripts have a confirmation page to make sure the action
completed successfully.  The pages will automatically redirect you after a
short amount of time.  You can shorten of lengthen the time by editing
$g_default_redirect_delay in config_inc.php.

* You can set $g_top_include_page and $g_bottom_include_page
  to alter what should be visible at the top and bottom of each page.

* All files were edited with TAB SPACES set to 4.
Description of RSSbuilder import into mantis.

See ../readme.libs for summary of all libraries

Removed:

Added:
	readme_mantis.txt - this file ;-)
	index.html - prevent directory browsing on misconfigured servers

Changes:
	none

Description of phputf8 import into mantis.

See ../readme.libs for summary of all libraries

Removed:
	tests/
	docs/
	
Added:
	readme_mantis.txt - this file ;-)
	index.html - prevent directory browsing on misconfigured servers

Changes:
	none

# MantisBT Documentation

This directory contains sources for the Mantis Documentation.

We are using *Docbook XML* to write manuals, and
[Publican](https://fedorahosted.org/publican/) to manage the build
in the final formats (PDF, HTML, etc).

Please refer to our [Wiki](https://www.mantisbt.org/wiki/doku.php/mantisbt:docbook)
for instructions on how to setup the required tools and
further details on how to build the manuals.


## Building

Build the documentation with:

```
cd Admin_Guide
make
```

Or, executing Publican manually

```
cd Admin_Guide
publican build --formats=pdf,html --langs=en-US
```
The MantisBT Entity-Relationship Diagram
========================================

The diagram was built using MySQL Workbench [1] version 6.3.6. The MantisBT
schema was reverse-engineered based on a freshly installed database, then the
relationships between tables and corresponding cardinalities were manually
added.

[1] http://dev.mysql.com/downloads/tools/workbench/


Editing Recommendations
-----------------------

* Make sure that the tables are big enough to display all columns
* Position the tables to minimize the number of intersections between the
  relationships lines (not always easy as the software does not offer much
  flexibility for positioning the connectors).
* Update the MantisBT and Schema version numbers as appropriate in the
  'Title' note (top-left corner) of the diagram
* Do not forget to bump the revision number
* Save the file


Exporting
---------

To save the diagram in a more widely readable format:

  * Start MySQL Workbench and open mantisbt.mwb
  * Go to File / Export
  * Select Export as PNG, SVG or Single Page PDF

Recommended naming convention for exported files:

    mantisbt_VVV_SSS_erd_rR.XXX

where

  * VVV is the MantisBT version (e.g. 1.2)
  * SSS is the corresponding schema version (e.g. 183)
  * R indicates the diagram's revision number
  * XXX is the file's extension (e.g. pdf, png)


Updating the Documentation
--------------------------

To keep the Developers Guide up-to-date as the ERD is modified:

1. Export the diagram as PNG
2. Save the file in /docbook/Developers_Guide/en-US/images/erd.png
3. Build the docbook and check that the updated file is there
4. Commit changes

Also remember to update the PDF on http://mantisbt.org/docs/erd

1. Export the diagram as single-file PDF
2. Save the file to a temp location as per above naming convention
3. Upload the file to the server
4. Remove the old file if necessary
This directory contains some command line scripts useful for performance
or integration issues. Please refer to the mantis manual for a more complete
documentation about their purpose and usage.

Included scripts:

send_emails.php
    Allows sending bug mails asynchronously
MantisBT external libraries
===========================

This directory contains a copy the 3rd-party libraries used by MantisBT.

The version and status of each is summarized below:

## PHP libraries

directory       | project         | version   | status
----------------|-----------------|-----------|---------------
adodb           | adodb           | 5.20.9    | unpatched [1]
disposable      | disposable      | 2.1.1     | unpatched [1]
parsedown       | parsedown       | 1.6.1     | unpatched [1]
phpmailer       | PHPMailer       | 5.2.22    | unpatched [1]
rssbuilder      | RSSBuilder      | 2.2.1     | patched [2]
utf8            | phputf8         | 0.5       | unpatched
securimage      | PHP Captcha     | 3.6.5     | patched [1]


## Javascript/CSS libraries

library / plugin                  | version   | status
----------------------------------|-----------|---------------
jquery                            | 2.2.4     | unpatched
bootstrap                         | 3.3.6     | unpatched
fontawesome                       | 4.6.3     | unpatched
ace-admin theme                   | 1.4.0     | customized
moment.js                         | 2.15.2    | unpatched
bootstrap-datetimepicker          | 4.17.43   | unpatched
dropzone.js                       | 4.3.0     | unpatched
chart.js                          | 2.1.6     | unpatched
typeahead.js                      | 1.1.1     | unpatched 
list.js                           | 1.4.1     | unpatched

  
**Notes**

1. Library is tracked as a *GIT submodule*; refer to the corresponding
   repository for details
2. removed `__autoload` function


Upstream projects
-----------------

project         | URL
----------------|--------------------------------------------------------------------
adodb           | http://adodb.sourceforge.net/ - https://github.com/ADOdb/ADOdb
disposable      | http://github.com/vboctor/disposable_email_checker
parsedown       | https://github.com/erusev/parsedown
phpmailer       | https://github.com/PHPMailer/PHPMailer
rssbuilder      | http://code.google.com/p/flaimo-php/
utf8            | http://sourceforge.net/projects/phputf8
secureimage     | http://www.phpcaptcha.org/ - https://github.com/mantisbt/securimage
jquery          | https://jquery.com/
bootstrap       | http://getbootstrap.com/
fontawesome     | http://fontawesome.io/
moment.js       | https://momentjs.com/ - https://github.com/moment/moment/
datetimepicker  | https://github.com/Eonasdan/bootstrap-datetimepicker
dropzone.js     | http://www.dropzonejs.com/ - https://github.com/enyo/dropzone
chart.js        | http://www.chartjs.org/ - https://github.com/chartjs/Chart.js
typeahead.js    | https://github.com/twitter/typeahead.js
list.js         | http://listjs.com/ - https://github.com/javve/list.js
++PHP UTF-8++

Version 0.5

++DOCUMENTATION++

Documentation in progress in ./docs dir

http://www.phpwact.org/php/i18n/charsets
http://www.phpwact.org/php/i18n/utf-8

Important Note: DO NOT use these functions without understanding WHY
you are using them. In particular, do not blindly replace all use of PHP's
string functions which functions found here - most of the time you will
not need to, and you will be introducing a significant performance
overhead to your application. You can get a good idea of when to use what
from reading: http://www.phpwact.org/php/i18n/utf-8

Important Note: For sake of performance most of the functions here are
not "defensive" (e.g. there is not extensive parameter checking, well
formed UTF-8 is assumed). This is particularily relevant when is comes to
catching badly formed UTF-8 - you should screen input on the "outer
perimeter" with help from functions in the utf8_validation.php and
utf8_bad.php files.

Important Note: this library treats ALL ASCII characters as valid, including ASCII control characters. But if you use some ASCII control characters in XML, it will render the XML ill-formed. Don't be a bozo: http://hsivonen.iki.fi/producing-xml/#controlchar

++BUGS / SUPPORT / FEATURE REQUESTS ++

Please report bugs to:
http://sourceforge.net/tracker/?group_id=142846&atid=753842
- if you are able, please submit a failing unit test
(http://www.lastcraft.com/simple_test.php) with your bug report.

For feature requests / faster implementation of functions found here,
please drop them in via the RFE tracker: http://sourceforge.net/tracker/?group_id=142846&atid=753845
Particularily interested in faster implementations!

For general support / help, use:
http://sourceforge.net/tracker/?group_id=142846&atid=753843

In the VERY WORST case, you can email me: hfuecks gmail com - I tend to be slow to respond though so be warned.

Important Note: when reporting bugs, please provide the following 
information;

PHP version, whether the iconv extension is loaded (in PHP5 it's 
there by default), whether the mbstring extension is loaded. The
following PHP script can be used to determine this information;

<?php
print "PHP Version: " .phpversion()."<br>";
if ( extension_loaded('mbstring') ) {
    print "mbstring available<br>";
} else {
    print "mbstring not available<br>";
}
if ( extension_loaded('iconv') ) {
    print "iconv available<br>";
} else {
    print "iconv not available<br>";
}
?>

++LICENSING++

Parts of the code in this library come from other places, under different
licenses.
The authors involved have been contacted (see below). Attribution for
which code came from elsewhere can be found in the source code itself.

+Andreas Gohr / Chris Smith - Dokuwiki
There is a fair degree of collaboration / exchange of ideas and code
beteen Dokuwiki's UTF-8 library;
http://dev.splitbrain.org/view/darcs/dokuwiki/inc/utf8.php
and phputf8. Although Dokuwiki is released under GPL, its UTF-8
library is released under LGPL, hence no conflict with phputf8

+Henri Sivonen (http://hsivonen.iki.fi/php-utf8/ / 
http://hsivonen.iki.fi/php-utf8/) has also given permission for his
code to be released under the terms of the LGPL. He ported a Unicode / UTF-8
converter from the Mozilla codebase to PHP, which is re-used in phputf8
# MantisBT Gravatar Plugin for Avatars

Copyright (c) 2015  MantisBT Team - mantisbt-dev@lists.sourceforge.net

Released under the [GNU General Public License v2](http://opensource.org/licenses/GPL-2.0)

## Description

The **Gravatar** plugin allows display of user avatars within 
MantisBT. The avatars are retrieved from [Gravatar](http://gravatar.com/) 
based on the user's e-mail address.

## Installation

1. While logged into your Mantis installation as an administrator, go to
   'Manage' -> "Manage Plugins".

2. In the "Available Plugins" list, you'll find the "Gravatar" plugin.
   Click "Install".

3. Set show_avatar to ON.

## Supported Versions

- MantisBT 1.2.x - not supported (though Gravatars are natively supported)
- MantisBT 1.3.x - supported
All files within this directory should use UTF-8 encoding to allow for MantisBT
multilingual operation.

Translations are performed on translatewiki.net at:
https://translatewiki.net/wiki/Translating:MantisBT

If you would like to help translate MantisBT to your native language, a good
place to start is the translatewiki.net introduction guide located at:
https://translatewiki.net/wiki/Translating:Intro
