
CONTENTS OF THIS FILE
---------------------

 * About Drupal
 * Configuration and features
 * Installation profiles
 * Appearance
 * Developing for Drupal

ABOUT DRUPAL
------------

Drupal is an open source content management platform supporting a variety of
websites ranging from personal weblogs to large community-driven websites. For
more information, see the Drupal website at http://drupal.org/, and join the
Drupal community at http://drupal.org/community.

Legal information about Drupal:
 * Know your rights when using Drupal:
   See LICENSE.txt in the same directory as this document.
 * Learn about the Drupal trademark and logo policy:
   http://drupal.com/trademark

CONFIGURATION AND FEATURES
--------------------------

Drupal core (what you get when you download and extract a drupal-x.y.tar.gz or
drupal-x.y.zip file from http://drupal.org/project/drupal) has what you need to
get started with your website. It includes several modules (extensions that add
functionality) for common website features, such as managing content, user
accounts, image uploading, and search. Core comes with many options that allow
site-specific configuration. In addition to the core modules, there are
thousands of contributed modules (for functionality not included with Drupal
core) available for download.

More about configuration:
 * Install, upgrade, and maintain Drupal:
   See INSTALL.txt and UPGRADE.txt in the same directory as this document.
 * Learn about how to use Drupal to create your site:
   http://drupal.org/documentation
 * Download contributed modules to sites/all/modules to extend Drupal's
   functionality:
   http://drupal.org/project/modules
 * See also: "Developing for Drupal" for writing your own modules, below.

INSTALLATION PROFILES
---------------------

Installation profiles define additional steps (such as enabling modules,
defining content types, etc.) that run after the base installation provided
by core when Drupal is first installed. There are two basic installation
profiles provided with Drupal core.

Installation profiles from the Drupal community modify the installation process
to provide a website for a specific use case, such as a CMS for media
publishers, a web-based project tracking tool, or a full-fledged CRM for
non-profit organizations raising money and accepting donations. They can be
distributed as bare installation profiles or as "distributions". Distributions
include Drupal core, the installation profile, and all other required
extensions, such as contributed and custom modules, themes, and third-party
libraries. Bare installation profiles require you to download Drupal Core and
the required extensions separately; place the downloaded profile in the
/profiles directory before you start the installation process. Note that the
contents of this directory may be overwritten during updates of Drupal core;
it is advised to keep code backups or use a version control system.

Additionally, modules and themes may be placed inside subdirectories in a
specific installation profile such as profiles/your_site_profile/modules and
profiles/your_site_profile/themes respectively to restrict their usage to only
sites that were installed with that specific profile.

More about installation profiles and distributions:
 * Read about the difference between installation profiles and distributions:
   http://drupal.org/node/1089736
 * Download contributed installation profiles and distributions:
   http://drupal.org/project/distributions
 * Develop your own installation profile or distribution:
   http://drupal.org/developing/distributions

APPEARANCE
----------

In Drupal, the appearance of your site is set by the theme (themes are
extensions that set fonts, colors, and layout). Drupal core comes with several
themes. More themes are available for download, and you can also create your own
custom theme.

More about themes:
 * Download contributed themes to sites/all/themes to modify Drupal's
   appearance:
   http://drupal.org/project/themes
 * Develop your own theme:
   http://drupal.org/documentation/theme

DEVELOPING FOR DRUPAL
---------------------

Drupal contains an extensive API that allows you to add to and modify the
functionality of your site. The API consists of "hooks", which allow modules to
react to system events and customize Drupal's behavior, and functions that
standardize common operations such as database queries and form generation. The
flexible hook architecture means that you should never need to directly modify
the files that come with Drupal core to achieve the functionality you want;
instead, functionality modifications take the form of modules.

When you need new functionality for your Drupal site, search for existing
contributed modules. If you find a module that matches except for a bug or an
additional needed feature, change the module and contribute your improvements
back to the project in the form of a "patch". Create new custom modules only
when nothing existing comes close to what you need.

More about developing:
 * Search for existing contributed modules:
   http://drupal.org/project/modules
 * Contribute a patch:
   http://drupal.org/patch/submit
 * Develop your own module:
   http://drupal.org/developing/modules
 * Follow best practices:
   http://drupal.org/best-practices
 * Refer to the API documentation:
   http://api.drupal.org/api/drupal/7
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
Bootstrap theme for Drupal

1. Download the Bootstrap library v2 (http://twitter.github.com/bootstrap/), make sure the resulting folder is named "bootstrap." If you are using the Github master branch, you will need to also find a way to compile the LESS and JS files since this module looks for bootstrap.css and bootstrap.js. 
2. Place the bootstrap folder inside the bootstrap theme folder or your subtheme folder: [path_to_themes]/bootstrap/bootstrap/js…
3. Put any plugin files into [path_to_themes]/bootstrap/bootstrap/js/
4. Make sure you have jQuery 1.7, which is available through the jQuery Update module (http://drupal.org/project/jquery_update/) 7.x-2.x-dev version. You need to make sure the 1.7 version is selected on the configuration page for it to work.

Author: http://drupal.org/node/259843/committersPlace downloaded and custom modules that extend your site functionality beyond
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

-- SUMMARY --

Title module allows entity titles/labels to be fully translatable.

For a full description of the module, visit the project page:
  http://drupal.org/project/title
To submit bug reports and feature suggestions, or to track changes:
  http://drupal.org/project/issues/title


-- REQUIREMENTS --

* @todo


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.


-- CONFIGURATION --

* @todo


-- USAGE --

* @todo


-- CONTACT --

Current maintainers:
* Francesco Placella (plach) - http://drupal.org/user/183211
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136

CONTENTS OF THIS FILE
----------------------

  * Introduction
  * Installation
  * Adding Lightbox Functionality to your Images
    - No Grouping
    - With Grouping
    - Slideshow
    - Video
    - HTML Content Support
    - Inline Content Support
    - Turning the Image Caption into a Link
  * Keyboard Shortcuts
  * Translation of Configured Strings
  * Known Issues
    - Keyboard Shortcuts in Opera


INTRODUCTION
------------
Maintainers:
  Stella Power (http://drupal.org/user/66894)
  Daniel F. Kudwien (http://drupal.org/user/54136)
  Mark Ashmead (http://drupal.org/user/52392)
  Fernando Correa da Conceição (http://drupal.org/user/889254)

Documentation: http://drupal.org/node/144469

Licensed under the GNU/GPL License
Based on Lightbox v2.03.3 by Lokesh Dhakar
<http://www.huddletogether.com/projects/lightbox2/>

Originally written to make use of the Prototype framework, and Script.acalo.us,
now altered to use jQuery.

Permission has been granted to Mark Ashmead & other Drupal Lightbox2 module
maintainers to distribute the original lightbox.js via Drupal.org under this
license scheme.  This file has been subsequently modified to make use of jQuery
instead of prototype / script.acalo.us.

This module enables the use of lightbox2 which places images above your
current page, not within. This frees you from the constraints of the layout,
particularly column widths.

This module will include the lightbox CSS and JS files in your Drupal
Installation without the need to edit the theme. The module comes with a
Lightbox2 Lite option which does not use the jQuery libraries; it is therefore
less likely to conflict with anything else.


INSTALLATION
------------
1. Copy lightbox2 folder to modules directory.
2. At admin/build/modules enable the lightbox2 module.
3. Enable permissions at admin/user/permissions.
4. Configure the module at admin/settings/lightbox2.
5. Modify your image links to open in a lightbox where necessary, see "Adding
   Lightbox Functionality to your Images' section below.
6. If you need to play flv files, then you may need to install a FLV player.
   There are a number of freely available ones on the Internet, including
   http://www.jeroenwijering.com/


ADDING LIGHTBOX FUNCTIONALITY TO YOUR IMAGES
--------------------------------------------
No Grouping
===========
Add rel="lightbox" attribute to any link tag to activate the lightbox.
For example:
<a href="images/image-1.jpg" rel="lightbox">image #1</a>
<a href="images/image-1.jpg" rel="lightbox[][my caption]">image #1</a>

Optional: To show a caption either use the title attribute or put in the second
set of [] of the rel attribute.

With Grouping
==============
If you have a set of related images that you would like to group, follow step
one but additionally include a group name between square brackets in the rel
attribute. For example:

<a href="images/image-1.jpg" rel="lightbox[roadtrip]">image #1</a>
<a href="images/image-2.jpg" rel="lightbox[roadtrip][caption 2]">image #2</a>
<a href="images/image-3.jpg" rel="lightbox[roadtrip][caption 3]">image #3</a>

No limits to the number of image sets per page or how many images are allowed
in each set. Go nuts!

If you have a set of images that you would like to group together in a
lightbox, but only wish for one of these images to be visible on your page, you
can assign the "lightbox_hide_image" class to hide the additional images.  For
example:

<a href="images/image-1.jpg" rel="lightbox[roadtrip]">image #1</a>
<a href="images/image-2.jpg" rel="lightbox[roadtrip]" class="lightbox_hide_image">image #2</a>
<a href="images/image-3.jpg" rel="lightbox[roadtrip]" class="lightbox_hide_image">image #3</a>

Slideshow
=========
This is very similar to the grouping functionality described above.  The only
difference is that "rel" attribute should be set to "lightshow" instead of
"lightbox".  Using the same example as above, we could launch the images in a
slideshow by doing:

<a href="images/image-1.jpg" rel="lightshow[roadtrip]">image #1</a>
<a href="images/image-2.jpg" rel="lightshow[roadtrip][caption 2]">image #2</a>
<a href="images/image-3.jpg" rel="lightshow[roadtrip][caption 3]">image #3</a>

Video
=====
It's possible to show video content in the lightbox.  In this case the "rel"
attribute should be set to "lightvideo".  It's possible to group videos and 
to control the size of the lightbox by setting the 'width' and 'height
properties.  The properties can be configured like
"lightvideo[group|width:300px; height: 200px;]" and
"lightvideo[|width:300px; height: 200px;][my caption]".  The properties should
all be of the format "property: value;" - note the closing semi-colon.  If no
properties are set, then the default width and height of 400px will be used.
See below for more detailed examples.

Basic example:
<a href="http://video.google.com/videoplay?docid=1811233136844420765"
rel="lightvideo">Google video example - default size</a>

Basic example with caption:
<a href="http://video.google.com/videoplay?docid=1811233136844420765"
rel="lightvideo[][my caption]">Google video example - default size</a>

Grouped example:
<a href="http://video.google.com/videoplay?docid=29023498723974239479"
rel="lightvideo[group][caption 1]">Grouped example 1</a>
<a href="http://video.google.com/videoplay?docid=1811233136844420765"
rel="lightvideo[group][caption 2]">Grouped example 2</a>

Controlling lightbox size example:
<a href="http://video.google.com/videoplay?docid=1811233136844420765"
rel="lightvideo[|width:400px; height:300px;][my caption]">Google video example -
custom size</a>

Supported Video Formats
asx, wmv, mov and swf videos should all be supported.  A number of video
providers are also supported, for example YouTube and Google Video. For full
details on how to integrate these with lightbox, please see the online
documentation.

HTML Content Support
====================
It's possible to show webpage content in the lightbox, using iframes.  In this
case the "rel" attribute should be set to "lightframe".  Again it's possible to
group the content, (e.g. "lightframe[search]") but in addition to that, it's
possible to control some of the iframe properties.  It's possible to set the
'width', 'height' and 'scrolling' properties of the iframe.  The properties are
separated from the group name by a '|', for example
"lightframe[search|width:100px;]" and
"lightframe[search|width:100px;][my caption]".  If no grouping is being used,
then the '|' is still used and the format would be "lightframe[|width:100px;]".
The properties should all be of the format "property: value;" - note the closing
semi-colon.  If no iframe properties are set, then the default width and height
of 400px will be used. See below for more detailed examples.

Basic example:
<a href="http://www.google.com" rel="lightframe">Search google</a>

Basic example with caption:
<a href="http://www.google.com" rel="lightframe[][my caption]">Search google</a>

Grouped example:
<a href="http://www.google.com" rel="lightframe[search]">Search google</a>
<a href="http://www.yahoo.com" rel="lightframe[search][Search Yahoo]">Search yahoo</a>

Controlling iframe property example:
<a href="http://www.google.com" rel="lightframe[|width:400px; height:300px; scrolling: auto;]">Search google</a>

Controlling iframe property when grouped example:
<a href="http://www.google.com" rel="lightframe[search|width:400px; height:300px; scrolling: auto;][Search Google]">Search google</a>
<a href="http://www.yahoo.com" rel="lightframe[search|width:400px; height:300px;]">Search yahoo</a>
<a href="http://www.yahoo.com" rel="lightframe[search|width:400px; height:300px;][Search Yahoo]">Search yahoo</a>

Inline Content Support
=======================
It's possible to show HTML snippets in the lightbox, that is on the same domain.
In this case the "rel" attribute should be set to "lightmodal".  Again it's
possible to group the content, (e.g. "lightmodal[search]") but in addition to
that, it's possible to control some of the inline / modal properties.  It's
possible to set the 'width', 'height' and 'scrolling' properties of the inline
content.  The properties are separated from the group name by a '|', for example
"lightmodal[search|width:100px;]" and
"lightmodal[search|width:100px;][my caption]".  If no grouping is being used,
then the '|' is still used and the format would be "lightmodal[|width:100px;]".
The properties should all be of the format "property: value;" - note the closing
semi-colon.  If no properties are set, then the default width and height of
400px will be used. See below for more detailed examples.

Basic example:
<a href="search.php" rel="lightmodal">Search</a>

Basic example with caption:
<a href="search.php" rel="lightmodal[][my caption]">Search</a>

Grouped example:
<a href="search.php" rel="lightmodal[search]">Search</a>
<a href="search.php?status=1" rel="lightmodal[search][published]">Search published content</a>

Controlling modal property example:
<a href="search.php" rel="lightmodal[|width:400px; height:300px; scrolling: auto;]">Search</a>

Controlling modal property when grouped example:
<a href="search.php" rel="lightmodal[search|width:400px; height:300px; scrolling: auto;]">Search</a>
<a href="search.php?status=1" rel="lightmodal[search|width:400px; height:300px;][Search published]">Search published content</a>
<a href="search.php?status=0" rel="lightmodal[search|width:400px; height:300px;][Search Unpublished]">Search unpublished content</a>



Turning the Image Caption into a Link
=====================================
If you wish to turn the caption into a link, format your caption in the
following way:

<a href="images/image-1.jpg" rel="lightbox[][&lt;a href=\"http://www.yourlink.com\"&gt;Clicky Visit Link&lt;/a&gt;'>image #1</a>

Note, the < and > characters have been changed to their HTML entities, and the "
have been escaped.


KEYBOARD SHORTCUTS
------------------
Not all of the default keyboard shortcuts work in the Opera browser, for example
'z' for toggling the zoom and 'spacebar' for toggling play / pause in
slideshows.  This can be overcome by updating your shortcut settings in the
Opera preferences editor.

The default keyboard shortcuts are listed below.  You can override these on
admin/settings/lightbox2.

Close : x, o, c, ESC
Previous Image : p, Left Arrow
Next Image : n, Right Arrow
Toggle Zoom : z (not available in slideshow)
Toggle Play / Pause : Spacebar (slideshow only)


TRANSLATION OF CONFIGURED STRINGS
----------------------------------
In order to translate the lightbox2 configuration strings, such as the text for
the "View Image Details" link and the image count, please install the i18n:
internationalization module and follow the instructions at 
http://drupal.org/node/134002.


KNOWN ISSUES
------------

Keyboard Shortcuts in Opera
---------------------------
Not all of the default keyboard shortcuts work in the Opera browser, for example
'z' for toggling the zoom and 'spacebar' for toggling play / pause in
slideshows.  This can be overcome by updating your shortcut settings in the
Opera preferences editor.
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

Allows entities to be translated into different languages.

For a full description of the module, visit the project page:
  http://drupal.org/project/entity_translation
To submit bug reports and feature suggestions, or to track changes:
  http://drupal.org/project/issues/entity_translation


-- REQUIREMENTS --

None.


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.


-- CONFIGURATION --

* @todo


-- USAGE --

* @todo


-- CONTACT --

Current maintainers:
* Francesco Placella (plach) - http://drupal.org/user/183211
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136


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

The CTools Plugin Example is an example for developers of how to CTools
access, argument, content type, context, and relationship plugins.

There are a number of ways to profit from this:

1. The code itself intends to be as simple and self-explanatory as possible. 
   Nothing fancy is attempted: It's just trying to use the plugin API to show
   how it can be used.
   
2. There is a sample panel. You can access it at /ctools_plugin_example/xxxx
   to see how it works.
   
3. There is Advanced Help at admin/advanced_help/ctools_plugin_example.ABOUT CONDITIONAL STYLESHEETS
-----------------------------

Internet Explorer implements a proprietary technology called Conditional
Comments. While web developers frown upon technologies that aren't cross-browser
supported, many CSS developers have found Conditional Comments very useful since
they can be used to fix the rendering of CSS in IE by placing IE-only CSS inside
conditional comments.

This module allows themes to easily add conditional stylesheets to the theme's
.info file.


THEME USERS
-----------

You only need to enable this module if a theme requires that you use it. Once it
is enabled, the module automatically performs all of its work for any theme
requiring it. You don't need to configure anything.


THEME DEVELOPERS
----------------

Without this module, the only way to have IE conditional stylesheets was to add
37 lines of code (more if you want to add more than one stylesheet) in two
horribly-difficult-to-remember function calls to your theme's template.php file:

  /**
   * Implements hook_preprocess_html().
   */
  function MYTHEME_preprocess_html(&$variables) {
    // Add conditional stylesheets for IE.
    drupal_add_css(
      drupal_get_path('theme', 'mytheme') . '/css/ie.css',
      array(
        'group' => CSS_THEME,
        'browsers' => array(
          'IE' => 'lte IE 7',
          '!IE' => FALSE,
        ),
        'weight' => 999,
        'every_page' => TRUE,
      )
    );
  }

  /**
   * Implements hook_preprocess_maintenance_page().
   */
  function MYTHEME_preprocess_maintenance_page(&$variables) {
    // Add conditional stylesheets for IE.
    drupal_add_css(
      drupal_get_path('theme', 'mytheme') . '/css/ie.css',
      array(
        'group' => CSS_THEME,
        'browsers' => array(
          'IE' => 'lte IE 7',
          '!IE' => FALSE,
        ),
        'weight' => 999,
        'every_page' => TRUE,
      )
    );
  }

Blech. Who wants to do that?

This module allows you to add "conditional-stylesheets" in a much simpler
manner, by adding lines to your theme's.info file. The syntax for that is:

  stylesheets-conditional[EXPRESSION][MEDIA][] = stylesheet.css

  where
    EXPRESSION can be any of the "downlevel-hidden" expressions specified in:
      http://msdn.microsoft.com/en-us/library/ms537512.aspx
    MEDIA can be any of the normal CSS media keywords.

For example, to add a stylesheet that only targets IE 6 and below, use:
  stylesheets-conditional[lt IE 7][all][] = ie6-and-below.css

To add a print stylesheet for IE9 only, use:
  stylesheets-conditional[IE 9][print][] = ie9.css

And to add a print stylesheet for all version of IE, use:
  stylesheets-conditional[IE][print][] = ie.css


*** IMPORTANT ***

Drupal 7 stores a cache of the data in .info files. If you modify any lines in
your theme's .info file, you MUST refresh Drupal 7's cache by simply visiting
the Appearance page at admin/appearance.

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

* Install as usual, see http://drupal.org/node/70151 for further information.

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

An example of a module using this API is Internationalization's i18n_variable module.
Welcome to Panels 3.

A little documentation should go here, but Panels 3 is alsoi a beast - you're
best off checking the online handbook on Drupal.org, or this issue:
http://drupal.org/node/887560. 
Description
-----------
This module adds a webform content type to your Drupal site.
A webform can be a questionnaire, contact or request form. These can be used 
by visitor to make contact or to enable a more complex survey than polls
provide. Submissions from a webform are saved in a database table and 
can optionally be mailed to e-mail addresses upon submission.

Requirements
------------
Drupal 7.x

Installation
------------
1. Copy the entire webform directory the Drupal sites/all/modules directory.

2. Login as an administrator. Enable the module in the "Administer" -> "Modules"

3. (Optional) Edit the settings under "Administer" -> "Configuration" ->
   "Content authoring" -> "Webform settings"

4. Create a webform node at node/add/webform.

Upgrading from previous versions
--------------------------------
Note that if you are upgrading from a Drupal 6 installation of Webform, you MUST
have been running Webform 3.x on your Drupal 6 site before upgrading to Drupal
7 and Webform 3.x. You cannot upgrade directly from Webform 6.x-2.x to Webform
7.x-3.x.

1. Copy the entire webform directory the Drupal modules directory.

2. Login as the FIRST user or change the $access_check in update.php to FALSE

3. Run update.php (at http://www.example.com/update.php)

Support
-------
Please use the issue queue for filing bugs with this module at
http://drupal.org/project/issues/webform


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

  You need at least one language other than English.
  On Administration > Configuration > Regional and language:
    Click "Add language"
    Pull-down menu: Choose your new language
    Then click "Add language"

  Drupal is now importing interface translations. This can take a few minutes.
  When it's finished, you'll get a confirmation with a summary of all
  translation files that have been pulled in.

  If required, enable the new language as default language.
  Home > Administration > Configuration > Regional and language:
    Select your new language as default

Update interface translations
-----------------------------
  On Home > Administration > Configuration > Regional and language:
    Choose the "Translation updates" tab
    Change "Check for updates" to Daily or Weekly instead of the default "Never".

  Cron will from now on check for updated translations, and will report the
  update status on the status page (Home > Administration > Reports).

  To check the translation status and execute updates manually, go to
     Administration > Configuration > Regional and language > Translate inteface
  Here you see English and your new language.
    Choose the "Update" tab
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

Alternative sources of translation
----------------------------------

  Each project i.e. modules, themes, etc. can define alternative translation
  servers to retrieve the translation updates from.
  Include the following definition in the projects .info file:

    l10n server = example.com
    l10n url = http://example.com/files/translations/l10n_server.xml

  The download path pattern is normally defined in the above defined xml file.
  You may override this path by adding a third definition in the .info file:

    l10n path = http://example.com/files/translations/%core/%project/%project-%release.%language.po

API
---
  Using hook_l10n_servers the l10n update module can be extended to use other
  translation repositories. Which is usefull for organisations who maintain
  their own translation.

  Using hook_l10n_update_projects_alter modules can alter or specify the
  translation repositories on a per module basis.

  See l10n_update.api.php for more information.

Maintainers
-----------
  Jose Reyero
  Gábor Hojtsy
  Erik Stielstra

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * Credits


INTRODUCTION
------------

jQuery Update module upgrades Drupal's stable version of jQuery in order to
support the most current jQuery version available.

Once a stable release of Drupal comes out, only minor bug-fix changes may be
added to it, so Drupal's version of jQuery will often lag behind the most recent
release offered by the jQuery project. The jQuery community tends to only
support the most recent version, so this module ensures that your Drupal
installation can run the most up-to-date jQuery plug-ins.


INSTALLATION
------------

1. Copy the jquery_update directory to your sites/SITENAME/modules directory.

2. Enable the module at Administer >> Site building >> Modules.


CREDITS
-------
* Matt Farina (mfer)
* Jeff Robbins (jjeff)
* Angela Byron (webchick)
* Addison Berry (add1sun)
* Rob Loach

Provides common and resuable token UI elements and missing core tokens.
Bean (Bean Entities Aren't Nodes)
==================================

The bean module was created to have the flexibility of
Block Nodes without adding to the node space.

Bean Types
----------

A Bean Type (or Block Type) is a bundle of beans (blocks).
Each Bean type is defined by a ctools plugin and are fieldable.
Currently Bean Types are only defined in hook_bean_plugins().

If you enable beans_admin_ui you can add/edit bean types at
admin/structure/block-types

Beans
-----

Beans can be added at block/add

Example Bean Type Plugins
-------------------------
https://github.com/opensourcery/os_slideshow
http://drupal.org/project/beanslide
http://treehouseagency.com/blog/neil-hastings/2011/09/21/building-custom...
http://drupal.org/sandbox/brantwynn/1369224
http://drupal.org/sandbox/brantwynn/1376658
https://gist.github.com/1460818

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

This directory should be used to place downloaded translations
for installing Drupal core.

This directory should be used to place downloaded translations
for installing Drupal core.

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
