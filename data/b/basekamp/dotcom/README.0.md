Creates calendar displays of Views results.
 
Create a new calendar by enabling or cloning the default calendar,
changing the date argument to use the correct date field(s), and setting
up the year, month, day, week, and block views with the desired styles 
and fields.
 
Unlike previous versions of the Calendar module, there is just a single
Date argument instead of year, month, and day arguments. The argument
value will be YYYY-MM-DD for a day, YYYY-MM for a month, YYYY for a
year, and YYYY-W99 for a week. There is a default option to set the 
argument to the current date when the argument is empty.

A calendar display creates calendar navigation and links to 
multiple displays for the year, month, day, or week views. The actual
displays are created by attaching calendar views that use whatever
styles are desired for those pages. 
 
Calendar views are attachments to create the year, month, day,
and week displays. They can be set to use any style, either a
calendar style or any other Views style, like teasers or lists.
If you don't want to use one of them, don't attach it to
anything. Only the attached views will show up in the calendar.

A calendar block will create a calendar block for the
view results. Attach a block view to the block and set up the
desired style in the block view. 

If the Calendar iCal module is enabled, an iCal feed can be
attached to the view.



// $Id: readme.txt,v 1.1.2.1 2008/09/14 18:33:20 aaron Exp $

THIS MODULE INTENTIONALLY LEFT BLANK.

NOTICE: image_ncck has been replaced by emimage. If you follow the upgrade instructions properly,
i.e., you disable your modules in d5 before upgrading to d6, you should have no problems.
// $Id: readme.txt,v 1.1.2.1 2008/09/14 18:31:41 aaron Exp $

THIS MODULE INTENTIONALLY LEFT BLANK.

NOTICE: video_cck has been replaced by emvideo. If you follow the upgrade instructions properly,
i.e., you disable your modules in d5 before upgrading to d6, you should have no problems.
Creativecommons Lite module

OVERVIEW

This modules allows users to add creativecommons license to any type of drupal node. License will be shown as block on node view page. 

Available license is:

Public Domain License
Developing Nations License
Attribution Non-commercial No Derivatives
Attribution Non-commercial Share Alike
Attribution Non-commercial
Attribution No Derivatives
Attribution Share Alike
Attribution


INSTALLATION

- Activate the module as usual
- Do the personalized setting from admin/settings/creativecommons-lite
- Enable creativecommons block from admin/build/block
- Goto content type page admin/content/types, edit content type for which you want to enable license selection and under workflow category check Allow user to add creativecommon license.

TO DO

- enable site wide licensing 
- update will all available licenses

CREDITS

This module is derived from the creativecommons_lite module for Drupal 5


Diff 2.x for Drupal 6.x
-----------------------
Diff enhances usage of node revisions by adding the following features:

- diff between node revisions on the 'Revisions' tab to view all the changes
  between any two revisions of a node
- highlight changes inline while viewing a node to quickly see color-coded
  additions, changes, and deletions
- preview changes as a diff before updating a node


Installation
------------
Diff can be installed like any other Drupal module -- place it in
the modules directory for your site and enable it on the `admin/build/modules`
page.

Diff needs to be configured to be used with specific node types on your site.
Enable any of diff's options on a content type's settings page (e.g.
`admin/content/node-type/page`).


Technical
---------
- Diff compares the raw data, not the filtered output, making it easier to see
changes to HTML entities, etc.
- The diff engine itself is a GPL'ed php diff engine from phpwiki.

API
---
This module offers `hook_diff()` which modules may use to inject their changes
into the presentation of the diff. For example, this is used by
`content.diff.inc` (see CCK), `upload.inc`, and `taxonomy.inc`.

Maintainers
-----------
- dww (Derek Wright)
- moshe (Moshe Weitzman)
- rötzi (Julian)
- yhahn (Young Hahn)

This directory should be used to place downloaded and custom modules
and themes which are common to all sites. This will allow you to
more easily update Drupal core files. These modules and themes should
be placed in subdirectories called modules and themes as follows:

  sites/all/modules
  sites/all/themes
Full documentation on the Zen theme can be found in Drupal's Handbook:
  http://drupal.org/node/193318

Excellent documentation on Drupal theming can be found in the Theme Guide:
  http://drupal.org/theme-guide


Installation:

  1. Download Zen from http://drupal.org/project/zen

  2. Unpack the downloaded file, take the entire zen folder (which includes
     the README.txt file, a zen_classic folder, etc.) and place it in your
     Drupal installation under one of the following locations:
       sites/all/themes
         making it available to the default Drupal site and to all Drupal sites
         in a multi-site configuration
       sites/default/themes
         making it available to only the default Drupal site
       sites/example.com/themes
         making it available to only the example.com site if there is a
         sites/example.com/settings.php configuration file

  3. Log in as an administrator on your Drupal site and go to Administer > Site
     building > Themes (admin/build/themes) and make Zen or one of its
     sub-themes the default theme.

Build your own sub-theme:

  IMPORTANT: In Drupal 6, the theme system caches template files and which theme
  functions should be called. What that means is if you add a new theme or
  preprocess fuction to your template.php file or add a new template (.tpl.php)
  file to your sub-theme, you will need to rebuild the "theme registry."
  See http://drupal.org/node/173880#theme-registry

  The base Zen theme is designed to be easily extended by its sub-themes. You
  shouldn't modify any of the CSS or PHP files in the zen/ folder; but instead
  you should create a sub-theme of zen which is located in a folder outside of
  the root zen/ folder. The examples below assume zen and your sub-theme will be
  installed in sites/all/themes/.

    Why? To learn why you shouldn't modify any of the files in the zen/ folder,
    see http://drupal.org/node/245802

  1. Copy the STARTERKIT folder out of the zen/ folder and rename it to be your
     new sub-theme. IMPORTANT: Only lowercase letters and underscores should be
     used for the name of your sub-theme.

     For example, copy the sites/all/themes/zen/STARTERKIT folder and rename it
     as sites/all/themes/foo.

       Why? Each theme should reside in its own folder. Unlike in Drupal 5,
       sub-themes can (and should) reside in a folder separate from their base
       theme.

  2. In your new sub-theme folder, rename the STARTERKIT.info file to the name
     of your new sub-theme. Then edit the .info file by changing any occurrence
     of STARTERKIT with the name of your sub-theme and editing the name and
     description field.

     For example, rename the foo/STARTERKIT.info file to foo/foo.info. Edit the
     foo.info file and change "STARTERKIT.css" to "foo.css", change "name = Zen
     Themer's Starter Kit" to "name = Foo", and change "description = Read..."
     to "description = A Zen sub-theme".

       Why? The .info file describes the basic things about your theme: its
       name, description, features, template regions, CSS files, and javascript
       files. See the Drupal 6 Theme Guide for more info:
       http://drupal.org/node/171205

  3. If you want a liquid layout for your theme, copy the layout-liquid.css from
     the zen/zen folder and place it in your sub-theme's folder. If you want a
     fixed-width layout for your theme, copy the layout-fixed.css from the
     zen/zen folder and place it in your sub-theme's folder. Rename the layout
     stylesheet to "layout.css".

     For example, copy zen/zen/layout-fixed.css and rename it as foo/layout.css.
     Note that the .info file already has an entry for your layout.css file.

       Why? In Drupal 6 theming, if you want to modify a stylesheet included
       by the base theme or by a module, you should copy the stylsheet from the
       base theme or module's directory to your sub-theme's directory and then
       add the stylesheet to your .info file. See the Drupal 6 Theme Guide for
       more info: http://drupal.org/node/171209

  4. Copy the zen stylesheet from the zen folder and place it in your
     sub-theme's folder. Rename it to be the name of your sub-theme.

     For example, copy zen/zen/zen.css and rename it as foo/foo.css. Note that
     the .info file already has an entry for your foo.css file and that your
     .info file removes the base theme's zen.css file.

  5. Copy the print stylesheet from the zen folder and place it in your
     sub-theme's folder.

     For example, copy zen/zen/print.css to foo/print.css. Note that the .info
     file already has an entry for your print.css file.

  6. Copy the html-elements stylesheet from the zen folder and place it in your
     sub-theme's folder.

     For example, copy zen/zen/html-elements.css to foo/html-elements.css. Note
     that the .info file already has an entry for your html-elements.css file.

  7. Edit the template.php and theme-settings.php files in your sub-theme's
     folder; replace ALL occurances of "STARTERKIT" with the name of your
     sub-theme.

     For example, edit foo/template.php and foo/theme-settings.php and replace
     "STARTERKIT" with "foo".

  8. Log in as an administrator on your Drupal site and go to Administer > Site
     building > Themes (admin/build/themes) and enable your new sub-theme.

  Optional:

  9. MODIFYING ZEN CORE STYLESHEETS:
     If you decide you want to modify any of the other stylesheets in the zen
     folder, copy them to your sub-theme's folder before making any changes.
     Also, be sure the new stylesheet is included in your .info file and that
     you have rebuilt the theme registry.

     For example, copy zen/zen/wireframes.css to foo/wireframes.css. Then edit
     foo/foo.info and uncomment this line to activate it:
       ;stylesheets[all][]  = block-editing.css
     to:
       stylesheets[all][]   = block-editing.css

  10. MODIFYING ZEN CORE TEMPLATE FILES:
     If you decide you want to modify any of the .tpl.php template files in the
     zen folder, copy them to your sub-theme's folder before making any changes.
     And then rebuild the theme registry.

     For example, copy zen/zen/page.tpl.php to foo/page.tpl.php.

  11. THEMEING DRUPAL'S SEARCH FORM:
     Copy the search-theme-form.tpl.php template file from the modules/search/
     folder and place it in your sub-theme's folder. And then rebuild the theme
     registry.

     You can find a full list of Drupal templates that you can override on:
     http://drupal.org/node/190815

       Why? In Drupal 6 theming, if you want to modify a template included
       by a module, you should copy the template file from the module's
       directory to your sub-theme's directory and then rebuild the theme
       registry. See the Drupal 6 Theme Guide for more info:
       http://drupal.org/node/173880

  12. FURTHER EXTENSIONS OF YOUR SUB-THEME:
     Discover further ways to extend your sub-theme by reading Zen's
     documentation online at:
       http://drupal.org/node/193318
     and Drupal 6's Theme Guide online at:
       http://drupal.org/theme-guide
ABOUT ZEN CLASSIC

  The Zen Classic theme contains the old stylesheets from Zen 5.x-0.7. It was
  made a sub-theme of Zen because, while the theme looked good as-is, everyone
  was tired of undoing all that CSS when using it to develop a new theme. See
  http://groups.drupal.org/node/6353 and http://drupal.org/node/171464

SUPPORT

  The Zen Classic theme is left as-is for historical purposes and as a reference
  for people who used Zen 5.x-0.7 and earlier and have gotten used to themeing
  with it.

  However, since most developers dislike using it as a starting point for theme
  development, fewer people will be available to help with themeing issues you
  may encounter.
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

Implementations are provided for core content types: nodes, taxonomy 
terms, and users (including blogs and tracker pages).

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
Pathauto just adds URL aliases to nodes, users, and taxonomy terms. Because 
it's an alias, the standard Drupal URL (for example node/123 or 
taxonomy/term/1) will still function as normal.  If you have external links 
to your site pointing to standard Drupal URLs, or hardcoded links in a module, 
template, node or menu which point to standard Drupal URLs it will bypass the 
alias set by Pathauto.

There are reasons you might not want two URLs for the same content on your 
site. If this applies to you, please note that you will need to update any 
hard coded links in your nodes or blocks. 

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

** Disabling Pathauto for a specific node type (or taxonomy)
When the pattern for a node type is left blank, the default pattern will be 
used. But if the default pattern is also blank, Pathauto will be disabled 
for that node type.

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

/* $Id: README.txt,v 1.1.2.1 2011/01/27 02:25:40 sun Exp $ */

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


-- CONTACT --

Current maintainers:
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136
* Tobias Stöckler (tstoeckler) - http://drupal.org/user/107158


This project has been sponsored by:
* UNLEASHED MIND
  Specialized in consulting and planning of Drupal powered sites, UNLEASHED
  MIND offers installation, development, theming, customization, and hosting
  to get you started. Visit http://www.unleashedmind.com for more information.


FileField provides an "File" field type to CCK. It provides many advantages over
the Drupal core "Upload" module including:

 * Per-field upload control (file extensions, file size).
 * Per-node upload size limits.
 * Multiple fields per content type.
 * Customizable paths for saving uploads (plus token support for dynamic paths).
 * Icons for uploaded file types.

FileField was written by Darrel Opry (dopry).
Maintained by Nathan Haug (quicksketch) and Andrew Morton (drewish).

Dependencies
------------
 * Content

FileField also provides additional features when used with the following:

 * ImageField (See an image preview during editing.)
 * Token (Generate dynamic paths when saving images.)
 * ImageCache (Create thumbnails of images on output.)

If your site is any larger than a personal blog, you should definitely install
the following modules to increase the security and stability of your uploads.

 * Transliteration (Convert unsafe characters to file system safe names.)
 * MimeDetect (Check the content of files to ensure they match the extension.)

Install
-------

1) Copy the filefield folder to the modules folder in your installation.

2) Enable the module using Administer -> Site building -> Modules
   (/admin/build/modules).

3) Create a new file field in through CCK's interface. Visit Administer ->
   Content management -> Content types (admin/content/types), then click
   Manage fields on the type you want to add an file upload field. Select
   "File" as the field type and "File" as the widget type to create a new
   field.

4) Upload files on the node form for the type that you set up.

-- SUMMARY --

Menu Trails implements primary/secondary links which keep the current menu trail
"active" or highlighted.  The module provides a means of broadly categorizing
nodes (by type or taxonomy) as falling "under" a known menu item.  These nodes
are not added to the menu tree (keeping the menu admin system sane) but they
will trigger the functionality above -- preserving navigation state for the user
-- when being viewed.

For a full description of the module, visit the project page:
  http://drupal.org/project/menutrails

To submit bug reports and feature suggestions, or to track changes:
  http://drupal.org/project/issues/menutrails


-- REQUIREMENTS --

None.


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.


-- CONFIGURATION --

* Classify nodes in Administer >> Site building >> Menus >> Trails.


-- TROUBLESHOOTING --

Menu Trails contains a built-in override for theme_links(), which is necessary
to add the "active" class to the containing <li> for each menu item.  If your
theme already includes an override, this may cause a PHP error, and you will
need to work out the differences between the two theme overrides yourself.

The 5.x version of the module required you to manually override theme_links() in
your theme's template.php file.

Note that if your theme already overrides the theme_links() function in
template.php file, then you need to manually reconcile the differences between
your THEMENAME_links() and Menu Trails' phptemplate_links() function.  The final
result should live in THEMENAME_links() in your template.php file.

Feel free to suggest better alternatives or other ways to tackle the issue if
you have them.


-- CONTACT --

Current maintainers:
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136
* Stefan M. Kudwien (smk-ka) - http://drupal.org/user/48898



Welcome to Views 2. Please see the advanced help for more information.

If you're having trouble installing this module, please ensure that your 
tar program is not flattening the directory tree, truncating filenames
or losing files.

Installing Views:

Place the entirety of this directory in sites/all/modules/views

Navigate to administer >> build >> modules. Enable Views and Views UI.

If upgrading from Drupal 5 and Views 1, your views need to be
converted manually. See administer >> build >> modules >> views >> tools >> convert.

If you're new to Views, try the Simple Views module which can create some
often used Views for you, this might save you some time.

Recommended modules for use with Views:
  CCK
  Voting API
  Views Bonus Pack
  Views Bulk Operations

Experimental modules:
  Views OR$Id: README.txt,v 1.1.6.2 2009/06/27 21:59:06 davereid Exp $

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * Frequently Asked Questions (FAQ)
 * Known Issues
 * How Can You Contribute?


INTRODUCTION
------------

Current Maintainer: Dave Reid <http://drupal.org/user/53892>
Maintainer: hass <http://drupal.org/user/85918>
Maintainer: HorsePunchKid <http://drupal.org/user/95048>
Maintainer: jjeff <http://drupal.org/user/17190>
Contributer: webchick <http://drupal.org/user/24967>
Project Page: http://drupal.org/project/path_redirect

This module allows you to specify a redirect from one path to another, using
any HTTP redirect status (301 - Permanent Redirect, etc.).


INSTALLATION
------------

See http://drupal.org/getting-started/5/install-contrib for instructions on
how to install or update Drupal modules.

Once Path Redirect is installed and enabled, you can add redirections at
admin/build/redirects and check your site's redirection settigns at
admin/build/redirects/settings.


FREQUENTLY ASKED QUESTIONS
--------------------------

There are no frequently asked questions at this time.


KNOWN ISSUES
------------

There are no known issues at this time.

To report new bug reports, feature requests, and support requests, visit
http://drupal.org/project/issues/path_redirect.


HOW CAN YOU CONTRIBUTE?
---------------------

- Write a review for this module at drupalmodules.com.
  http://drupalmodules.com/module/path-redirect

- Help translate this module on launchpad.net.
  http://project.davereid.net/translate/projects/path_redirect

- Report any bugs, feature requests, etc. in the issue tracker.
  http://drupal.org/project/issues/path_redirect
$Id: README.txt,v 1.7.2.4 2009/07/15 19:59:14 fago Exp $

Automatic Nodetitle Module
------------------------
by Wolfgang Ziegler, nuppla@zites.net


Description
-----------
This is a small and efficent module that allows hiding of the content title field in the form.
To prevent empty content title fields it sets the title to the content type name or to an
configurable string. If the token module is installled it's possible to use various content
data for the autogenerated title - e.g. use the text of a CCK field.

Advanced users can also provide some PHP code, that is used for automatically generating an
appropriate title.

Installation 
------------
 * (optional) Download and install the token module.
 * Copy the module's directory to your modules directory and activate the module.
 * For each content type you want to have an automatic title, click on the
   "edit" link for it on 'admin/content/types'
 * At the top of the content type edit form, there is a "Automatic title
   generation" box allowing you to configure the details for the current content
   type.
 
 
 
 
 Advanced Use: PHP Code
------------------------
 You can access $node from your php code. Look at this simple example, which just adds the node's
 author as title:
 
<?php return "Author: $node->name"; ?>

 
 
 Advanced Use: Combining tokens and PHP
 ---------------------------------------
 
 You can combine php evalution with the token module, because tokens are replaced first.
 However be aware to don't use this with any textual values provided by users as this would
 open a security hole. If you are in doubt, don't combine tokens with php evaluation.
 
 Here is an example:
 
<?php
  $token = '[field_testnumber]';
  if (empty($token)) {
    return '[type]';
  }
  else {
    return $token;
  } 
?>

 So if the text of the CCK number [field_testnumber] isn't empty it will be used as title.
 Otherwise the node type will be used.


 
 
 Updating nodetitles from existing nodes
 ---------------------------------------
 If you set the nodetitle to be auto generated for some content type, existing nodes
 are not affected. You can update existing nodes by going to 'admin/content/node',
 then filter for your content type, mark some nodes and choose the "Update option" 
 "Update automatic nodetitles". 
 
 // $Id: README.txt,v 1.5 2009/12/01 22:55:43 xuriz Exp $

MENU BREADCRUMBS
================

Introduction
------------
By default, Drupal 6 will use the Navigation menu for the breadcrumb. This module allows you to use the menu the current page belongs to for the breadcrumb.

As an added bonus, it also allows you to append the page title to the breadcrumb (either as a clickable url or not) and hide the breadcrumb if it only contains the link to the front page.

Installation
------------
1. Copy the menu_breadcrumb folder to your sites/all/modules directory.
2. At Administer -> Site building -> Modules (admin/build/modules) enable the module.
3. Configure the module settings at Administer -> Site configuration -> Menu breadcrumb (admin/settings/menu_breadcrumb).

Upgrading
---------
Replace the older menu_breadcrumb folder with the newer version, and then run update.php in case there are any database updates to apply.

Features
--------
- Allows you to use the menu the node belongs to for the breadcrumb on node pages.
- Append the page title to the breadcrumb.
- Optionally have the appended page title be an URL.

Issues / Feature requests
-------------------------
If you find a bug, or have a feature request, please go to :

http://drupal.org/project/issues/menu_breadcrumb

Contact
-------
This module is being maintained by me, Geoffrey de Vlugt (gdevlugt). 

If you need to contact me, use the contact form at :

http://drupal.org/user/167273/contact 
// $Id: README.txt,v 1.1.2.1.2.1.2.1 2009/11/12 18:04:00 jareyero Exp $

Notifications: README.txt
=========================

This is a complete notifications/subscriptions framework. The Notifications module is the main engine,
but it doesn't provide by itself any subscriptions or UI besides the administration pages. 
You'll need to enable some subscription types (content, taxonomy...) and some UI module (notifications_ui)
for it to work. 

It includes:
- Several types of subscriptions: content, taxonomy
- Event and message queueing
- Pluggable event types
- Pluggable subscription types

Read online handbook at http://drupal.org/node/252592

Dependencies:
- Tokens module, http://drupal.org/project/tokens
- Messaging module, http://drupal.org/project/messaging

SimpleTest:
-----------
Tests for this module will run on SimpleTest 6.x-2.8 (old version).
About this see http://drupal.org/node/584596

This module was originally based on the subscriptions module, http://drupal.org/project/subscriptions
The code has been used as an starting point but the framework has been completely rewritten.

Developers:
-----------
- Tim Cullen
- Jeff Miccolis
- Jose A. Reyero

Development Seed, http://www.developmentseed.org
1.0 --- UNDER DEVELOPMENT
-----------------------------------------
Link Filter - converts [l:URL text] tags

INSTALL
 
 1) Unzip the linkfilter.zip kit in the modules directory of your Drupal
    setup, usually sites/all/modules

 2) This will create:
     modules/linkfilter/
     modules/linkfilter/linkfilter.css
     modules/linkfilter/linkfilter.info
     modules/linkfilter/linkfilter.module
     modules/linkfilter/README
     modules/linkfilter/*.png and *.gif icon files

 3) As admin user, go to administer -> modules, and enable linkfilter module.

 4) Go to administer -> Input Formats, click on "configure" for Filtered
 HTML (and all other required input formats), and enable the "Link Filter".
 
 Now you can use [l:URL text] tags in all the nodes that are using the
 appropriate input formats.

 Click on Input Formats when editing a node for more help - there is a link
 to "Link Filter Tips" section on the filter tips page that provides
 more details and examples.

-----------------------------------------
The goal for this filter is to be somewhat like the URL filter included
with Drupal, with the additional requirement to be Drupal installation
directory independent as well as domain independent so that the URLs in
Drupal nodes don't have to be re-edited when a Drupal site is moved to a
different sub-directory or a different domain. Additionally, it allows
for link text to be specified for the URL, and it preserves the input
characters as much as possible, performing no or minimal HTML entity
conversions of the input characters.

-----------------------------------------
/**
 * "Link filter" Drupal module, replaces [l:URL text] input tags.
 *
 * [l:URL text] text filter for internal Drupal or external Web links.
 * "text" is optional, and can be multiple words. URL can be any URL -
 * an alias, or any Drupal path, or a non-Drupal path with full
 * http://URL notation.
 * This is converted to a HTML href tag, prefixed with:
 * 1) $base_root if the URL begins with a / character
 * 2) no prefix if the URL has a : in it, example: http: or ftp: etc
 * 3) converted with Drupal l() function in all other cases,
 *    for example recipe/boil-potatoes  or node/231
 *    In this case, the URL is considered to be a Drupal system path.
 * 
 * Appropriate class="linkfilter-<type>" tag will be added, from this list:
 * linkfilter-drupal, linkfilter-local, linkfilter-urlfull,
 * linkfilter-mailto, linkfilter-drupal-node-<node_type>
 * See the linkfilter.css file for examples and link icons available for use
 * with these classes.
 * 
 * [l:recipe/boil-potatoes link text]
 *    ==>
 * <a href="http://..../drupal-dir/recipe/boil-potatoes">link text</a>
 * 
 * For non-Drupal paths:
 * Space " " and right square bracket ] need to be escaped in URL and text.
 * in URL:  For space use %20. For right square bracket ] use %5D or &#93;
 * in text: For right square bracket ] use &#93;
 * Note that Drupal l() is not used because it munges special characters
 * and query tags like after the ? character in the URL.
 *
 * For Drupal paths:
 * As of version 0.7, uses Drupal l() function to create HTML for the
 * link. This will allow [l:node/281] to be changed to the alias, if any
 * for node/281.
 *
 * ---
 * syntax borrowed from wiki example: [http://www.example.com Example site]
 *
 * Added l: prefix to allow normal use of square brackets [ ] so that
 * only prefixed content gets transformed.
 * ---
 *
 *License
 *This work is hereby released into the Public Domain.
 *To view a copy of the public domain dedication, visit
 *http://creativecommons.org/licenses/publicdomain/ or send a letter to
 *Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
 *
 *Author: Avinash Chopde <avinash@acm.org>
 *Created: April 2007
 *http://www.aczoom.com/cms/software/web/link-filter-drupal-module
 */
In-place popup to add a new node to Node Reference widget.
Initial inspiration: Add and Reference by tema (http://drupal.org/project/add_n_reference)

TODO 
 * Fix losing highlighted selections on node add with multi-select box.
 
LIMITATIONS
 * http://drupal.org/node/378988 - conflicts with Hierarchical Select.

 ABOUT

  This is a simple filter module. It handles <code></code> and <?php ?> tags so
  that users can post code without having to worry about escaping with &lt; and
  &gt;


INSTALLATION

  See the INSTALL.txt file for important installation instructions.


CURRENT MAINTAINER

  John Wilkins - JohnAlbin on Drupal.org


CREDITS

  This mini-module was made by Steven Wittens <unconed@drupal.org>, based on the
  PHP filter in Kjartan Mannes's <kjartan@drupal.org> project.module.
$Id: README.txt,v 1.2 2009/04/30 23:51:15 garrettalbright Exp $

Zenify
by Garrett Albright
My Drupal user page:
http://drupal.org/user/191212

This module's project page:
http://drupal.org/project/zenophile

This module aids in the initial setup of Zen subthemes. If you don't know what
Zen subthemes are or why you'd want to create one, you probably shouldn't use
this module.


FIFTEEN SECOND HOW-TO:

1. Install this module like any other module.

2. If necessary, go to Administration > Users > Permissions and grant groups the
'create theme with zenophile' permission.

3. Go to Aministration > Site building > Themes and click the "Create Zen
subtheme" tab. Everything on this page should be fairly self-explanatory.

4. When you're done creating themes, you may want to deactivate the module. It
won't stress the server too much if it remains active, but it will take up a
bit of RAM and processor cyclage while providing no added functionality to the
site./* $Id: README.txt,v 1.15.2.5 2009/01/18 04:04:19 sun Exp $ */

-- SUMMARY --

Image Assist provides a user interface for adding images to any textarea that is
aware of input formats.

For a full description visit the project page:
  http://drupal.org/project/img_assist
Bug reports, feature suggestions and latest developments:
  http://drupal.org/project/issues/img_assist


-- REQUIREMENTS --

* Image module <http://drupal.org/project/image>

* Views module <http://drupal.org/project/views>

* Token module (optional) <http://drupal.org/project/token>

* Wysiwyg API module (optional) <http://drupal.org/project/wysiwyg>


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.


-- CONFIGURATION --

* Configure an input format and enable the filter 'Inline images' by visiting:

  Administer >> Site configuration >> Input formats

  If you want to enable Inline images for the input format 'Filtered HTML',
  you additionally need to click the 'Configure' tab and add

  <span> <img>

  to the text field 'Allowed HTML tags'.

* Configure user permissions in Administer >> User management >> Access control
  >> Image assist.

* Optionally go to the Views administration page and edit or clone Image
  Assist's default 'img_assist_browser' view for the image browser. If you
  intend to make major changes to the default view, you should click on 'Clone'
  and modify the new (duplicated) view instead.  When you are done, enable this
  view on Image Assist's settings page.

* Optionally fine tune how Image Assist operates by navigating to:

  Administer >> Site configuration >> Image assist

  If Taxonomy module is enabled, you use a gallery module like Acidfree, and you
  want your users to be able to easily choose images from their galleries, select
  for example "Acidfree albums" as the vocabulary to use for Image assist.

* If Wysiwyg API module is installed, you need to edit your Wysiwyg profiles
  and enable the plugin for Image assist.


-- USAGE --

* Using this module with TinyMCE via Wysiwyg API module:
  1. Click the camera icon on the TinyMCE toolbar.
  2. Upload a new photo or choose an existing image.
  3. Set the properties for how you want the image to display.
  4. Click the Insert button.

* Using this module with any textarea:
  1. Click the "Add image" link or camera icon under any textarea box. 
  2. Upload a new photo or choose an existing image.
  3. Set the properties for how you want the image to display.
  4. Click the Insert button.

* Most browsers, such as Internet Explorer and Mozilla clones, will insert the
  image exactly where you place your cursor in the textarea of your content
  form. Otherwise the image will be appended to the end of your entry.

* Adding images with Image module

  Users with the 'access img_assist' permission will see the 'add image' link
  or icon (configurable). Access to img_assist via the TinyMCE plugin is
  controlled by the Wysiwyg API module.  

  Users with the 'create images' permission will be able to upload images using
  img_assist. All users will be able to see and insert their own pictures, even
  if the image nodes are unpublished. Users with the 'access all images'
  permission will also be able to use other images, but only if they are
  published.

  One possible workflow would be to set images to be UNPUBLISHED by default.
  That way users can upload, categorize, and use images in img_assist without
  the images showing up anyway else on the site. Images that should  also be
  shown elsewhere on the site can manually be published by going to
  administer > content.

* Image presentation

  A full img_assist tag looks like this:

  [img_assist|nid=2|title=My title|desc=My description|align=right|width=200|height=150|link=url,http://www.google.com]


-- TROUBLESHOOTING --

* If your site is accessible from multiple domains, embedded image tags and
  links in contents will point to the domain/URL that was accessed upon first
  view of a content.  In most cases, you want to re-generate this cached content
  after staging from a development server to a live server.  For this purpose,
  go to Image Assist's settings page and click on the link (pointing to
  'img_assist/cache/clear') in the help text at the beginning of the page.

  To circumvent this permanently, as with any other module, you need to setup
  separate database tables for Drupal's cache.  Image Assist primarily works in
  the cache_filter table.  See sites/default/settings.php for more information.

* In front of submitting a new bug report, support or feature request, please
  search the issue queue for already existing issues.

  Note: FAILURE TO DO SO WILL EXTEND THE TIME FOR ISSUES TO BE SOLVED.

* If you are successfully using this module, please consider helping out on
  support requests in the issue queue.

* If you have a development site in progress, please test patches needing review.
  See http://drupal.org/patch/apply for further information.


-- CONTACT --

Current maintainers:
* Daniel F. Kudwien (sun) <http://www.unleashedmind.com>
* Hannes Lilljequist (zoo33) <http://www.perrito.se>
* Darren Oh (darrenoh) <http://darrenoh.dnsalias.com>

Previous maintainers:
* Benjamin Shell (benshell) <http://www.benjaminshell.com>
* Matt Westgate (matt westgate) <http://drupal.org/user/2275>

This project has been sponsored by:
* UNLEASHED MIND
  Specialized in consulting and planning of Drupal powered sites, UNLEASHED
  MIND offers installation, development, theming, customization, and hosting
  to get you started. Visit http://www.unleashedmind.com for more information.

$Id: README.txt,v 1.60.4.3 2009/06/09 14:29:52 weitzman Exp $

DESCRIPTION
--------------------------
Enable users to create and manage their own 'groups'. Each group can have members, and maintains a group home page where members can post into. Posts may be placed into multiple groups (i.e. cross-posting) and individual posts may be shared with non-members or not. Membership to groups may be open, closed, moderated, or invitation only. Add-on modules are available for group image galleries, group calendars, group vocabulary, group stores, and so on.

Groups may choose their own theme and language. Groups have RSS feeds and email notifications and so on. Group admins may customize the layout and contents of their group home page and add additional custom pages (requires the upcoming OG Panels module).

INSTALLATION
---------------
- Enable the Organic groups and Organic groups Views integration modules. If you want to protect some posts so that only certain users may view them, enable the 'Organic Groups access control' module as well. Please make sure OG is working well on its own before enabling other OG related modules.
- On the Administer > Organic groups configuration page, see the content types table at the top. Click edit beside each type to set its 'usage'. Disable comments and attachments for node types which are designated as group nodes. You usually want to create a new node type via admin/content/types page and then designate that content type as a group node. See the first item in NOTES below. 
- Set other preferences on admin/og/og as desired. It may take some experimenting before you arrive at a configuration well suited to your needs.
- On the Administer › Site building > Blocks page, enable the 'Group details' and drag it toward the top of your list. Optionally enable the other 'Group' blocks.
- Grant permissions as needed on the admin/user/permission page 
- Begin creating groups (visit the node/add page), joining those groups, and posting into those groups. The join link appears in the Group details block, for non invite-only groups.
- Consider enabling the following modules which work well with OG: Pathauto, Locale, Notifications. After your install is working nicely, consider enabling more og add-on modules like og_mandatory_group, og_vocab, and og_panels. Those are known to work well with OG. Some of the others on drupal.org are poorly integrated and will cause problems. See http://drupal.org/project/Modules/category/90.

NOTES
----------------
- This module supports designating any content type to act as a group. This content type should be defined by a custom module or via the admin/content/types page. When defining your type, you usually want the title label to be 'Group name' and the body label to be 'Welcome message'. Since all nodes of this type are treated as groups, you will usually not want to designate the standard page, story, or book node types as groups. The feature where custom content types may act as groups enables you to have custom fields for your groups and even different CCK fields for different kinds of groups (i.e. content types). 
- There are a few handy tabs at the path 'group'. You might want to add a link in your Navigation to that url. Each tab also provides a useful RSS feed.
- 'Administer nodes' permission is required for changing the Manager of a group (do so by changing the posts' Author.)
- 'Administer nodes' permission enables viewing of all nodes regardless of private/public status.
- All membership management happens on the 'membership list' page which is linked from the group details Block (while viewing a group page). This includes approving membership requests (for selective groups), adding/removing users and promoting users into group admins.
- If you decide to stop using Organic groups, just disable it as usual. If you ever decide to re-enable, all your prior group access control information will be restored. If you want to start fresh, uninstall og, og_views and og_access modules.

DEVELOPERS & SITE BUILDERS
------------------
- You may craft your own URLs which produce useful behavior. For example, user/register?gids[]=4 will add a checked checkbox for to the user's registration page for subscribing to group nid=4. This feature overrides the usual preference for groups to always appear during registration.
- You may alter the links in the group details block using hook_og_links_alter($links, $group_node). See og_block_details().
- The current group context is available to javascript code at Drupal.settings.og. This is useful for enriching ad tags and analytics calls with group information.
- Use Views Bulk Operations module to mass update user memberships and also content affiliations.

THEMES
------------------
You may wish to stylize nodes which have properties assigned by this module.
--- public vs. private posts are denoted by $node->og_public (og_access provides private posts)
--- provided in this package are two template files for the phptemplate engine. One stylizes group nodes and the other stylizes all other stylizes group posts. These can be starting points for your customization of look and feel of your group. Just copy them to your theme directory and edit as desired. Or you might use the included og_panels module to achieve custom group homepages (and other group pages) that group admins can design themselves.

INTEGRATION
---------------------
- I recommend enabling the cron features of Notifications/Messaging modules. When you do, group email notifications are sent during cron runs, instead of immediately after a post is submitted. This speeds up posting a lot, for big groups. The delay also helps authors fix typos in their posts before the mail is sent.
- This module exposes an API for retrieving and managing membership via direct PHP functions [og_save_subscription()] and via XMLRPC.

UNIT TESTING
----------------------
This module comes with a few unit tests. Please help update and build more of them. See http://drupal.org/simpletest

TODO/BUGS/FEATURE REQUESTS
----------------
- See http://drupal.org/project/issues/og. Please search before filing issues in order to prevent duplicates.

UPGRADING FROM 5.0 TO 6.x
-----------------
- The upgrade auto-enables the new og_views module. This is needed to get the same functionality that was present in D5.
- There is no support for migrating custom Views. Please redo those in Views2. You might need to use a Relationship.
- Group members block (og/2) block is now served by Views: views/og_members_block-block_1
- Group search is now in its own block which must be enabled manually. It used to be integrated into the Group details block.

UPGRADING FROM 4.7 TO 5.x
-----------------
- You must update to 5.x before updating to 6.

CREDITS
----------------------------
Authored and maintained by Moshe Weitzman <weitzman AT tejasa DOT com>
Contributors: Gerhard Killesreiter, Angie Byron, Derek Wright, Thomas Ilsche, Ted Serbinski, damien_vancouver
Sponsored by Bryght - http://www.bryght.com
Sponsored by Broadband Mechanics - http://www.broadbandmechanics.com/
Sponsored by Finnish Broadcasting Company - http://www.yle.fi/fbc/
Sponsored by Post Carbon Institute - http://www.postcarbon.org/
; $Id: README.txt,v 1.2.4.1 2009/06/10 16:23:06 weitzman Exp $

The og_actions module is a collection of actions. Their most common use case is in conjunction with the Views Bulk Operations module. Together, these modules make a terrific admin dashboard for putitng content into and out of groups, and adding removing members from groups. 

Requirements:
og.module

Suggested:
trigger.module OR
workflow.module OR
rules.module OR
views_bulk_options.module

Actions
There are 11 actions in this module. Here is a sampling.

Non-configurable actions:
-------------------------
"Make the node publicly visible" -- This action will make the node visible to the public. This has the same effect as checking the "Public" box on node creation.

"Make the node private to its groups" -- This action has the opposite of "Make the node publicly visible."  This action is equivalent to unchecking the "public" box on node editing.

"Remove the node from all groups" -- This is action will remove all group ties to this node. This will occur even if you have selected "Audience Required" in your organic group settings.

Configurable actions:
---------------------
"Add the node to the specified group..." -- This action allows an administrator to select a group and add nodes to it. Any currently published, organic group node type will be listed. In large lists, this could potentially be a very long list. This action could potentially add a node that is in the excluded content type list.

"Remove the node from the specified group..." -- This action removes the node from the selected groups. Potentially, it could remove the last group from the node, even if "Audience Required" is selected in organic groups.

Notes
If you are using workflow.module with this module, you may find that your actions are not taking effect during node creation. To fix this bug use the following SQL query in your database:

UPDATE SYSTEM SET weight = 10 WHERE name = "workflow"

This will ensure that og adds its data to the node before workflow attempts to act on it. You could alternatively set workflow's weight in the system table using the weight module.$Id: README.txt,v 1.4 2008/11/04 18:55:59 karthik Exp $

og_notifications integrates OG with the notifications and messaging modules
family thereby enabling such features as group subscriptions, administrative
notifications etc.

The notifications and messaging modules extend beyond simple e-mail based
delivery systems and provide other avenues to contact recipients such as
private messages, simple alerts, and, if supported, even SMS. The delivery 
options are customisable by the end user.

INSTALLATION & CONFIGURATION
----------------------------
  * Install organic groups, messaging, token, notifications, notifications_lite,
  notifications_content and any other dependant modules prior to enabling
  og_notifications. Ensure that they are all up to date.

  * In addition to the above, install at least one messaging delivery module
  such as Simple Mail. It is also recommended that the notifications UI module
  is enabled to provide interface options.

  * Enable og_notifications. If this is an upgraded installation, all relevant
  data will be migrated over automatically.

  * The messaging and notifications modules can be configured via
  "admin/messaging". Besides all the generic options, settings particular to
  organic groups can be found in "admin/messaging/notifications/content".

  * The organic groups configuration page at "admin/og/og" contain further
  options for customising notification settings such as auto-subscription and
  default message templates.

  * Group pages now have a broadcast tab (previously the "e-mail" tab) which
  will allow privileged users to broadcast messages to all group members via
  the notifications module.  

  * End users can configure their individual preferences via their account 
  pages. These include auto-subscription and delivery options.

More information can be obtained from the documentation of the notification, 
messaging and other related modules.

CREDITS
-------
Authored by Karthik Kumar / Zen [ http://drupal.org/user/21209 ]
Sponsored by Kevin Millecam [Webwise Solutions]
﻿// $Id: README.txt,v 1.1.2.2 2009/04/23 12:30:13 roidanton Exp $

Linodef - Link nodes & terms and embed fields & terms
-----------------------------------------------------
To install, place the entire Linodef folder into your modules directory.
Then go to Administer -> Site building -> Modules and enable the "Linodef" module.

Requirements
------------
  - Drupal 6
  - CCK - to embed field values
  - Textfield - to embed field values
  - Taxonomy - to embed terms
  - Advanced help - to access the help documentation (optional)

Usage
-----
Use it like any other filter:

1) Activation
Go to Administer -> Settings -> Input types and activate the Filter "Linodef" for
the input type of your choice.

2) Order
Go to the sort/order tab of the input type and move Linodef to the top so it has
the lowest weight. This step is important! Only that way e.g. the HTML filter is
able to remove undesired HTML tags from elements embedded by Linodef.

Now you can use the tags as described at the input type tips page: /filter/tips.

To get more information - e.g. about the provided Buttons API - use the included
help documentation (Advanced help module required) or refer to the official
documentation at http://drupal.org/project/linodef.﻿// $Id: README.txt,v 1.1.2.2 2008/11/30 13:00:31 roidanton Exp $

Linodef - Buttons API
---------------------
This module provides functions which help by creating buttons that are using the capabilities of the Linodef filter tags.

Go to Administer -> Site building -> Modules and enable the "Linodef Buttons API" module.

Requirements
------------
  - Linodef
  - Advanced help - to access the help documentation (optional)

Usage
-----
This module is required by other modules which add buttons. Itself it does nothing that is visible.﻿// $Id: README.txt,v 1.1.2.2 2008/11/30 13:00:30 roidanton Exp $

Linodef - BUEditor
------------------
This module provides functions to create buttons that uses the capabilities of the Linodef filter.

Go to Administer -> Site building -> Modules and enable the "Linodef Buttons - BUEditor" module.

Requirements
------------
  - Linodef
  - BUEditor
  - Advanced help - to access the help documentation (optional)

Usage
-----
To use buttons for the Linodef filter tags, import and customize the button found at linodef_bueditor_button.csv
(included at modules/linodef/modules/linodef_buttons_bueditor) like you do it with other custom buttons.

To get detailed information refer to your editors manual or use the included help documentation
(Advanced help module required).// $Id: README.txt,v 1.16.2.3 2009/04/12 23:17:45 ufku Exp $

- BUEditor:
A plain textarea editor aiming to facilitate code writing.
It's the most customizable text editor of the web because it allows you to;
 - build the editor from scratch.
 - determine the functionality by defining image or text buttons that generate code snippets, html tags, bbcode tags etc.
 - determine the design and layout by defining theme buttons that insert html to the layout.


- WHAT'S NEW IN 6.x:
 - custom icon and library paths for each editor.
 - support using different editor templates for differnet textareas in a page.
 - alternative editor assignment for user roles.
 - theme buttons that provide unlimited theming options.
 - Headers (h1, h2, h3, h4) button and separators in default editor.
 - changed key variable from "editor" to "BUE". (ex: editor.active is now BUE.active)
 - another popup dialog(BUE.quickPop) that has no title or close button.
 - jquery effects. (ex: effects in popup openings)
 In default buttons' library:
 - new eDefTagChooser function that uses BUE.quickPop to allow users choose among predefined tags.
 - new eDefTagger function that toggles(inserts or removes) a predefined tag in the selection.
 - eDefTagDialog accepts a special attribute name, "html", that represents the inner html of the tag.
 - eDefTagDialog accepts "textarea" as a field type.


- HOW TO INSTALL:
1) Copy editor directory to your modules directory.
2) Enable the module at module administration page.
3) Add/edit editors and buttons at: admin/settings/bueditor.
4) There is the default editor you can use as a starting point.
5) You may install IMCE module to use it as a file/image browser in editor's image & link dialogs.
6) Make sure your input format does not filter the tags the editor inserts.


- ADDING BUTTONS:
You can add buttons to an editor by two methods;
1- Manually entering the values for new button fields located at the bottom of the button list.
2- Importing a CSV file that contains previously exported buttons.


- EXPORTING AND DELETING BUTTONS:
You should first select the buttons you want to export or delete, using checkboxes next to them.
Then select the action you want to take in the selectbox below the list and press GO.


- BUTTON PROPERTIES

TITLE:(required) Title or name of the button. Displayed as a hint on mouse over.
A title can be translated by prefixing it with "t:". Ex: t:Bold turns into t('Bold').
If the title starts with "tpl:", the button is considered a theme button. See BUTTON TYPES

CONTENT: Html or javascript code that is processed when the button is clicked. This can also be
php code that is pre evaluated and return html or javascript code. See BUTTON TYPES.

ICON: Image or text to display the button.

KEY: Accesskey that is supported by most browsers as a shortcut on web pages. With the right
key combinations users can fire the button's click event. Use Alt+KEY in Internet Explorer, and
Shift+Alt+KEY in Firefox.

WEIGHT: Required for sorting the buttons. Line-up is from the lightest to the heaviest.


- BUTTON TYPES
There are three types of buttons regarding the CONTENT property;
1- HTML BUTTONS 
2- JAVASCRIPT BUTTONS 
3- PHP BUTTONS
4- THEME BUTTONS


- HTML BUTTONS
These are used for directly inserting plain text or html into the textarea.
It is possible to use the selected text in the textarea by using the place holder %TEXT%
For example, assume that the button content is:
<p>%TEXT%</p>
and it is clicked after selecting the "Hello world!" text in the textarea. Then the result is:
<p>Hello world!</p>
with the selection preserved.
Multiple occurances of %TEXT% is possible and each will be replaced by the selected text. 
These type of buttons are useful for simple html tags or other tag systems like BBCode.
Note: if you want to insert some text containing the phrase %TEXT%, use a javascript button.


- JAVASCRIPT BUTTONS
These type of buttons are used for special cases where it is insufficient to just replace the selected text.
The content of a javascript button must begin with a 3 charater text "js:" to be differentiated from a
html button. The remaining code is treated as a javascript code and executed in a function when the
button is clicked. The function is called with the parameter E which represents the active editor. 
Editor has many ready-to-use methods and variables making it easy to create javascript buttons.
See EDITOR VARIABLES AND METHODS and especially EDITOR INSTANCE variables and methods.


- PHP BUTTONS
The content of a php button must begin with "php:". The remaining code is pre evaluated at the server 
side and expected to return some code. According to the return value of the php code the real type of 
the button is determined. If the php code returns nothing or false, the button is disabled and does not
show up in the editor.
A php button is indeed a html or javascript button. Php execution is for some special purposes. For example,
it is possible to disable or change the content of the button for a specific user role;
Button with content
php: 
if (user_access('access foo')) {
  return 'js: alert("You have the permission to access foo")';
}
turns into a javascript button having the returned content for users having "access foo" permission. for others 
it is disabled and doesnt show up.


- THEME BUTTONS
A theme button is a special type of button that just inserts html into editor interface for theming purposes. It can be
used to insert separators, line breaks or any html code in order to achieve the themed editor interface. For a button to
be considered as a theme button it should have a title starting with "tpl:". Having this title, the button is processed to
insert a piece of html code that is included in button content and button icon(or caption). A theme button, regarding its 
content, can also be a js or php button at the same time.

In order to determine what the button inserts into the layout;
 - first, content is checked and 
    - if it is javascript code(js:) it is executed and the value that returned is inserted into the layout
    - otherwise it is inserted as it is.
 - then, icon or caption is checked and inserted as being wrapped in "<span class="separator"></span>".

Here are some examples;

[title: "tpl:", content: "<br />", caption: ""]
Inserts <br />.(line break)

[title: "tpl:", content: "<br />", icon: "separator.png"]
Inserts <br /><span class="separator"><img src="path-to-sparator.png"></span>.

[title: "tpl:", content: "", caption: "|"] OR [title: "tpl:", content: "<span class="separator">|</span>"]
Inserts <span class="separator">|</span>.

[title: "tpl:", content: "js: return new Date()"]
Inserts new date returned from javascript.

You can also create groups of buttons by creating wrappers around them;

[title: "tpl:", content: "<div class="group1">"] (Start wrapping by opening a div)
[...buttons of the group in between(can be both theme buttons and functional buttons)]
[title: "tpl:", content: "</div>"] (End wrapping by closing the div)


- EDITOR VARIABLES
BUE:
the top most container variable having other variables and methods in it.

BUE.templates
container for editor templates(configurations, buttons and interface)

BUE.instances
array containing the editor instances in the page

BUE.active:
currently active or last used editor istance. When a button is clicked or a textarea is focused, 
the corresponding editor instance becomes the BUE.active. If there are multiple editor instances, accesskeys 
are switched to work on the BUE.active.
BUE.active is widely used in javascript buttons since the methods of the current editor instance are accessed 
using it. Each editor instance has its own variables and methods that can(should) be used by javascript buttons. 
See EDITOR INSTANCE

BUE.dialog:
dialog object of the editor used like a pop-up window for getting user input or displaying data.
It has its own variables and methods. See EDITOR DIALOG

BUE.quickPop:
another dialog object of the editor. It has no title or close button.
It has its own variables and methods. See EDITOR QUICK-POP


- EDITOR METHODS
BUE.processTextarea(T, tplid):
integrates the editor template(BUE.templates[tplid]) into the textarea T.
This can be used for dynamic editor integration at any time after page load.

BUE.openPopup(id, title, content, effect):
Opens a pop-up dialog having the given "id", titled as "title" and containing the "content".
Returns the js object representing the pop-up(a html table object).
This pop-up object has its internal "open(title, content, effect)" and "close(effect)" methods which can be used for 
further opening and closing operations.
Since pop-up object is a html table object, it has all the methods and properties of a regular table.
The difference between a pop-up and editor.dialog is that editor.dialog can only have one instance visible at a time,
and it doesnt allow textarea editing when it is open.
optional effect parameter is one of the jQuery effects (opening: 'slideDown', 'fadeIn', closing: 'slideUp', 'fadeOut')

BUE.createPopup(id, title, content):
This method is used by openPopup method. Creates and returns the pop-up object for further use.(does not open it)


- EDITOR INSTANCE (a must-read for javascript button creators)
Each editor running on the page for a textarea is called an instance. Editor instances have their own variables 
and methods that make it easy to edit textarea content. Active instance on the page can be accessed by the 
variable "BUE.active".

A js button script is executed in a function with the argument E that refers to BUE.active.
Here are the VARIABLES of the istance E:

E.index: index of the instance in the array BUE.instances
E.textArea: textarea of the instance as an HTML object.
E.tpl: editor template that this instance uses.(one of BUE.templates)
E.UI: html object that wraps the instance interface. (<div class="editor-container" id="editor-%index"></div>)
E.buttons: array of buttons of the instance as HTML objects(input objects: type is button or image)
E.bindex: latest/currently clicked button index that can be used in E.buttons. Ex: E.buttons[E.bindex]

Here are the METHODS of the instance E:

E.focus():
Focus on the textarea of the instance.

E.getContent():
Returns the content of the textarea.

E.setContent(text):
Replaces the content of the textarea with the given text.

E.getSelection():
Returns the selected text in the textarea.

E.replaceSelection(text, cursor):
Replace the selected text in the textrea with the given text.
The optinal second argument specifies the position of the caret after replacement.
if cursor='start', it is placed at the begining of the replaced text.
if cursor='end', it is placed at the end of the replaced text.
if cursor is not defined, the selection is preserved containing the replaced text.

E.tagSelection(left, right, cursor):
Encloses the selected text in the textarea with the given left and right texts.
The optional third argument specifies the position of the caret after enclosing.
if cursor='start', it is placed at the begining of the selected text.
if cursor='end', it is placed at the end of the selected text.
if cursor is not defined, the selection is preserved.

E.makeSelection(start, end):
Create a selection by selecting the characters between the indexes "start" and "end".

E.posSelection():
Returns the index values of selection start and selection end.
Returns {start: X, end: Y} where X is the start index and Y is the end index.
Note: No selection is also a selection where start=end=caret position.

E.buttonsDisabled(state, bindex):
Dynamically enable/disable buttons of the instance.
the first argument defines the state of the buttons and should be set to true or false.
the optional second argument defines the index of the button whose state will not change.
Ex: to disable all buttons except the pressed button;
js: E.buttonsDisabled(true, E.bindex);


- EDITOR DIALOG
Editor dialog is an object shared by all editor instances. It can be used to display any kind of data, ie. a html form
to get some user input. 
Here are the methods of editor dialog

BUE.dialog.open(title, content, effect):
Opens the dialog with the given title and content in it.
optional effect parameter is one of the jQuery effects ('slideDown' or 'fadeIn')

BUE.dialog.close(effect):
Closes the dialog.
optional effect parameter is one of the jQuery effects ('slideUp' or 'fadeOut')


- EDITOR QUICK-POP
This is a pop-up object without a title and a close button. It shows just the content and closes automatically
when the user clicks somewhere in the document.
To open a quick-pop:

BUE.quickPop.open(content, effect):
Opens the quick-pop with the content in it.
optional effect parameter is one of the jQuery effects ('slideDown' or 'fadeIn')


- EDITOR ICONS
All images with jpg, gif or png extensions in the editor's icon path (which is bueditor_path/icons by default) are accessible
by the editor and listed in the icon list in the editor editing page.


- EDITOR LIBRARY
While creating a javascript button you may want to use functions or variables from an external javascript library 
in order to shorten the content text and make it clean. The editor library path is the place where you should put 
your javascript files to be loaded with the editor. The default path is bueditor_path/library.


- KNOWN ISSUES
Accesskeys in Internet Explorer:
Pressing an accesskey(Alt+KEY) when there is a selection, deselects it preserving the caret position.

Accesskeys in Firefox:
If there are multiple editors in the page, accesskeys(Shift+Alt+KEY) will work on only the first editor instance. 
This is becouse FF does not allow dynamic adjustment of accesskeys.

New line character:
Since new line is represented by different characters (\r, \r\n, \n) on different platforms, there may be some 
unexpected behaviour of the editor in some platform-browser combos regarding the cursor position after text 
insertion/replacement. Specify new line characters as "\n", if you have to use any in your scripts.

POST variable limit:
Although it's a rare case, consider increasing your server post variable limit if you have problems while adding too many buttons.

- DEFAULT BUTTONS
BUEditor comes with a few default buttons that may help you extend the editor:

Insert/edit image:
Inserts image html after getting the src, width, height, alt attributes from the user. If IMCE module is installed, 
and the user has access to it, a Browse button will appear linking to IMCE image browser.
Editing a previously inserted image is possible if the html code of the image is selected with no extra characters.

Insert/edit link:
Inserts link html after getting the link URL, link text and title from the user. If IMCE module is installed, and the user has 
access to it, a Browse button will appear linking to IMCE file browser.
Editing a previously inserted link is possible if the html code of the link is selected with no extra characters.

Bold:
Encloses the selected text with the tag <strong>

Italic:
Encloses the selected text with the tag <em>

Headers:
Pops a dialog showing h1, h2, h2, h4 header tags to choose among.

Ordered list:
Converts the lines in the selected text to a numbered list. It is also possible to start a new list with no selection. 
If the selection is an ordered list which was previosly created by this button, the lines in the text are restored.

Unordered list:
Converts the lines in the selected text to a bulleted list. It is also possible to start a new list with no selection. 
If the selection is an unordered list which was previosly created by this button, the lines in the text are restored.

Teaser break:
Inserts Drupal teaser break which is <!--break-->

Preview:
Previews the textarea content. By default, lines and paragraphs break automatically.
eDefPreview function accept 2 parameter.
Set first parameter to true to preview pure html. Set second parameter to true to preview only the selected text:
eDefPreview(true);//no automatic line breaking. preview is based on pure HTML.
eDefPreview(false, true);//only the selection is previewed.

Help:
Displays the title(hint) for each button in the editor.


- TIPS AND TRICKS

How to disable a button temporarily?

Make the first line of the button content:
php: return;/*
and the last line:
*/


How to extend image or link dialogs to get values for other attributes of "img" and "a" tags from the user?
How to create a dialog for any tag just like image or link dialogs?

There is the eDefTagDialog(tag, fields, dtitle, stitle, func) function in default buttons library to create a dialog for
any tag. 
tag -> tag name
fields -> an array of attributes that are eiter strings or objects.
dtitle -> dialog title. if not specified, "(tag) Tag Dialog" is used.
stitle -> laber for submit button. if not specified, browser's default is used.
func -> name of the function that will be executed after submission instead of the default one. (for advanced use)

The simplest form, for example:
eDefTagDialog('div', ['id', 'class', 'style', 'html']);//html is a special keyword that represents inner html
will create a DIV Tag Dialog requesting values of attributes id, class and style and also the inner html.
It will also detect if the selection is a proper DIV tag, and if so, will put the values of attributes to the corresponding fields.
After submission, it will enclose/replace the selection in textarea.

You might have noticed that fields in image/link dialogs are declared as objects not as strings. That's a
customized form of declaring attributes. It is ideal to use an object if you want
- a field type other than textfield (type: 'select', options: {'left': 'Left', 'right': 'Right'})
  textarea and select are the two options other than the default.
- a custom label (title: 'Image URL')
- a default value (value: ' ')
- some prefix or suffix text or html (prefix: '[ ', suffix: ' ]')
- to join two fields in a single line like in image width & height fields (getnext: true)
- to set custom attributes for the field (attributes: {size: 10, style: 'width: 200px'})

Note:
- The field object must have a name property that specifies the attribute name. ex:{name: 'href'}
- If a field value has new line character(\n) in it, then the field type automatically becomes "textarea"

So lets add an "align" attribute field to the image dialog(note that it's not XHTML compliant):

The field object to pass to eDefTagDialog is;
{
  name: 'align',//required
  title: 'Image align', // if we dont set it, it will be set as 'Align' automatically.(the name with the first letter uppercase)
  type: 'select', // we use a selectbox instead of a plain textfield.
  options: {'': '', left: 'Left', right: 'Right', center: 'Center'} // set options in the form-> {attribute-value: 'Visible value'}
}

Lets add it to the form in the image button's content:

var form = [
 {name: 'src', title: 'Image URL'},
 {name: 'width', title: 'Width x Height', suffix: ' x ', getnext: true, attributes: {size: 3}},
 {name: 'height', attributes: {size: 3}},
 {name: 'alt', title: 'Alternative text'},
 {name: 'align', title: 'Image align', type: 'select', options: {'': '', left: 'Left', right: 'Right', center: 'Center'}} //align
];
eDefTagDialog('img', form, 'Insert/edit image', 'OK');

That's it. We now have an image dialog which can also get/set the "align" attribute of an image tag.


How to create a button that gets user input and adds it to the textarea?

Button content could be like this:
js:
// function that inserts the user input from the form into the textarea.
BUE.getUserInput = function(form) {
  E.replaceSelection('User input is: '+ form.elements["user_input"].value);
  BUE.dialog.close();//close the dialog when done.
}
//form html. we define an input field named as "user_input".
var userForm = '<form onsubmit="editor.getUserInput(this); return false;">';//run getUserInput on submission
userForm += 'Input : <input type="text" name="user_input" />';
userForm += '<input type="submit" value="Submit" /></form>';
//open editor dialog with a title and the user form.
BUE.dialog.open('User Input', userForm);

The above example uses a form which is more suitable for complex user input. If you want to get just a single input you 
may consider using javascript prompt(). Here is an example that gets image URL as a user input
js:
var url = prompt('URL', '');//prompt for URL
var code = '<img src="'+ url +'" />';//put the url into the code.
E.replaceSelection(code);//replace the selection with the code.


How to create a button to insert XHTML-compliant Underlined text?

Since <u> is not XHTML-compatible, you should use CSS. First of all, you need to define a class in your theme's 
CSS file, for instance; 
.underlined-text {text-decoration: underline;}
As the above class exists, you can use it in your button content:

<span class="underlined-text">%TEXT%</span>

Where %TEXT% will be replaced by the selected text in the textarea.


How to extend the functionality of Headers button to create a specialized tag chooser?
How to create an image chooser(ie. smiley chooser) using eDefTagChooser?

Firstly, we should understand what eDefTagChooser does.
eDefTagChooser(tags, applyTag, wrapEach, wrapAll, effect)
It accepts 5 parameters among which only the first one is required and the rest is optional.

Parameter "tags": is an array of tag infos, each having the format:
 [tag, title, attributes]
  tag: the tag that will enclose the selected text in the textarea
  title: the text or html to help the user choose this tag
  attributes: attriutes that will be inserted inside the tag. ex:{'id': 'site-name', 'class': 'dark'}

ex tags: [ ['span', 'Red', {'style': 'color: red'}], ['span', 'Blue', {'class': 'blue-text'}] ]
this will create two options:
Red (inserting <span style="color: red"></span>)
Blue (inserting <span class="blue-text"></span>)

Parameter "applyTag": if set to true, the title of the tag-info will be enclosed by the tag itself. This will allow
the user to preview the effect of the tag.
Ex: ['span', 'Red', {'style': 'color: red'}] will genarate an option
- with applyTag=false : Red (text only)
- with applyTag=true : <span style="color: red">Red</span>

Parameter "wrapEach": the tag that will enclose each option.
This can be set to 'div' to make sure that each option is in a new line.

Parameter "wrapAll": the tag that will enclose the whole block of options.
Having set the parameter wrapEach to 'li' this can be set to 'ul' in order to create a proper list of options.

Parameter "effect": one of the jQuery effects for opening the dialog ('slideDown' or 'fadeIn')

Knowing the details we can create our customized tag chooser.
Let's, for example, add styled headers to the default header chooser.
js: eDefTagChooser([
 ['h1', 'Header1'],
 ['h1', 'Header1-title', {'class': 'title'}],// this will insert <h1 class="title"></h1>
 ['h2', 'Header2'],
 ['h2', 'Header2-title', {'class': 'title'}],
 ['h3', 'Header3'],
 ['h4', 'Header4']
], true, 'li', 'ul', 'slideDown');

Now, let's create an image chooser
There will be no title for our tags since we will use applyTag to preview the image that will be inserted. However we
will be using a line break for every N(=4 in our example) image in order to create rows of options. Otherwise,
all of them will be placed in a single row.
js: eDefTagChooser([
 ['img', '', {'src': '/path-to-images/img1.png'}],//better to set also the width & height & alt attributes
 ['img', '', {'src': '/path-to-images/img2.png'}],
 ['img', '', {'src': '/path-to-images/img3.png'}],
 ['img', '<br />', {'src': '/path-to-images/img4.png'}],//line break added after 4th
 ['img', '', {'src': '/path-to-images/img5.png'}],
 ['img', '', {'src': '/path-to-images/img6.png'}],
 ['img', '', {'src': '/path-to-images/img7.png'}],
 ['img', '<br />', {'src': '/path-to-images/img8.png'}],//br after 8th
 ['img', '', {'src': '/path-to-images/img9.png'}],
 ['img', '', {'src': '/path-to-images/img10.png'}]
], true, '', '', 'slideDown');


While inserting a single tag should we use the classic <tag>%TEXT%</tag> pattern or the new eDefTagger('tag') ?
What is the difference between <tag>%TEXT%</tag> and js:eDefTagger('tag') ?

First of all, the classic tag insertion method does not require the default buttons library, whereas eDefTagger is a part of
the default buttons library.

- Classic method preserves the selected text after tag insertion, whereas eDefTagger selects the whole insertion.
Classic method: converts the selection "foo" to "<tag>foo</tag>", ("foo" still being selected)
eDefTagger('tag'): converts the selection "foo" to "<tag>foo</tag>" (<tag>foo</tag> is selected)

- Classic method doesnt parse the selection to check if it is an instance of the tag, whereas eDefTagger does and toggles it.
Classic method: converts the selection "<tag>foo</tag>" to "<tag><tag>foo</tag></tag>"
eDefTagger('tag'): converts the selection "<tag>foo</tag>" to "foo"

- In classic method you define the attributes of the tag in the usual way, whereas in eDefTagger you pass them as an object
<tag class="foo" id="bar">%TEXT%</tag> <=> eDefTagger('tag', {'class': 'foo', 'id': 'bar'})

- In classic method It's possible to use the selected text for any purpose, whereas in eDefTagger the only goal is to html.
 Classic method can use the selection multiple times and do anything with it: [bbcode]%TEXT%[/bbcode]: (%TEXT%)

It's up to you which method to use. Select the method that fits best to your needs.//$Id: README.txt,v 1.1 2008/02/27 18:07:55 ufku Exp $

All icons in this directory(not including subdirectories) will be avaliable for
editors that identify this directory as icon path.//$Id: README.txt,v 1.2 2008/02/27 18:07:55 ufku Exp $

All javascript files in this directory(not including subdirectories) will be loaded on
pages displaying editors that identify this directory as library path.// $Id: README.txt,v 1.12.2.4 2008/10/28 01:42:48 yched Exp $

Content Construction Kit
------------------------

NOTE: Install the advanced_help module (http://drupal.org/project/advanced_help)
to access more help (writing still in progress...)

To install, place the entire CCK folder into your modules directory.
Go to Administer -> Site building -> Modules and enable the Content module and one or
more field type modules:

- text.module
- number.module
- userreference.module
- nodereference.module

Now go to Administer -> Content management -> Content types. Create a new
content type and edit it to add some fields. Then test by creating
a new node of your new type using the Create content menu link.

The included optionswidget.module provides radio and check box selectors
for the various field types.

The included fieldgroup.module allows you to group fields together
in fieldsets to help organize them.

A comprehensive guide to using CCK is available as a CCK Handbook
at http://drupal.org/node/101723.

Known incompatibilitie
----------------------

The Devel Themer module that ships with Devel is known to mess with CCK admin pages.
As a general rule, Devel Themer should only be switched on intermittently when doing
theme work on a specific page, and switched off immediately after that, for it adds
massive processing overhead.

Maintainers
-----------
The Content Construction Kit was originally developped by:
John Van Dyk
Jonathan Chaffer

Current maintainers:
Karen Stevenson
Yves Chedemois

; $Id: README.txt,v 1.1.2.4 2009/06/04 18:57:59 yched Exp $

Ongoing work on the multigroup module has moved to the experimental
CCK 3.0 branch.
$Id: README.txt,v 1.1.2.11 2010/01/12 12:08:49 fago Exp $


-----------------------
Content Profile Module
-----------------------
by Wolfgang Ziegler, nuppla@zites.net

With this module you can build user profiles with drupal's content types.


Installation 
------------
 * Copy the module's directory to your modules directory and activate the module.
 
 Usage:
--------
 * There will be a new content type "profile". Customize its settings at
   admin/content/types.
 * At the bottom of each content type edit form, there is a checkbox, which allows
   you to mark a content type as profile.
 * When you edit a profile content type there will be a further tab "Content profile",
   which provides content profile specific settings.
   

 Warning:
---------
 The module uses drupal's content or "nodes" for user profiles, so the access
 permissions applied to view the content profiles are the regular node related
 permissions.
 That means the "access user profiles" permission of the user module still
 applies only to the user account pages at "user/UID" but not to content profiles,
 which can be viewed at node/NID too. Still you can use any regular node access
 module to restrict access to your content profiles, e.g. you may use the Content
 Access module for that (http://drupal.org/project/content_access).



Content profiles per role:
--------------------------
You may, but you need not, mark multiple content types as profile. By customizing 
the permissions of a content type, this allows you to create different profiles for
different roles.


Hints:
------

 * When using content profiles the "title" field is sometimes annoying. You can rename
   it at the content types settings or hide it in the form and auto generate a title by
   using the auto nodetitle module http://drupal.org/project/auto_nodetitle.
   
 * If you want to link to a content profile of a user, you can always link to the path
   "user/UID/profile/TYPE" where UID is the users id and TYPE the machine readable content
   type name, an example path would be "user/1/profile/profile".
   This path is working regardless the user has already profile content created or not.

 * If you want to theme your content profile, you can do it like with any other content.
   Read http://drupal.org/node/266817.
   
 * If you want a content profile to be private while your site content should be available
   to the public, you need a module that allows configuring more fine grained access control
   permissions, e.g. the module Content Access (http://drupal.org/project/content_access)
   allows you to that.
   
 * There is also rules integration which is useful for customizing the behaviour of the
   module. See below for more.



Theming: Easily use profile information in your templates! 
-----------------------------------------------------------
Content Profile adds a new variable $content_profile to most templates related to users.
So this variable allows easy access to the data contained in the users' profiles.
Furthermore it does its job fast by lazy-loading and caching the needed content profile
nodes.

The $content_profile variable is available in the page, node, comment, user_name,
user_profile, user_signature, search_result and some other templates. 

$content_profile lets you access all variables of a profile, which are you used to
have in a common node template. See http://drupal.org/node/11816.

So in any of these templates you may use the $content_profile like this:

<?php
 // Just output the title of the content profile of type 'profile'
 // If there is no such profile, it will output nothing.
 echo $content_profile->get_variable('profile', 'title');

 // Get all variables of the content profile of type 'profile'
 $variables = $content_profile->get_variables('profile');
 
 // Print out a list of all available variables
 // If the user has no profile created yet, $variables will be FALSE.
 print_r($variables);

 if ($variables) {
   // Print the title and the content.
   echo $variables['title'];
   echo $variables['content'];
 }
 else {
   // No profile created yet.
 }
 
 // $content_profile also allows you to easily display the usual content profile's view
 // supporting the same parameters as node_view().
 echo $content_profile->get_view('profile');

?>

 Check the source of content_profile.theme_vars.inc to see what methods $content_profile
 supports else.


Adding $content_profile to further templates
--------------------------------------------

If you miss $content_profile in some templates containing user information (id), just
fill a issue in content profile's queue so we can add it to the module.
Furthermore you may let content_profile its variable to your custom templates by specifying
the setting 'content_profile_extra_templates' in your site's settings.php.

E.g. you may add:
  $conf['content_profile_extra_templates'] = array('my_template');

Where 'my_template' has to be the key of your template's entry in the theme_registry (hook_theme()).



Rules integration
------------------

There is some integration to the rules module (http://drupal.org/project/rules), which offers
a condition to check whether a user has already created a profile of a certain type. Then it
offers an action for loading the content profile of a user, which makes it available to token
replacements as well as to all other existing rules actions which deal with content.

So this integration allows one to build some profile related rules with the rules module. As
example the module ships with one deactivated default rule:

  "Redirect to profile creation page, if users have no profile."
  
If you activate it at the rules "Triggered rules" page, it's going to be evaluated when a user
logs in. Of course you can also alter the default rule and customize it so that it fits your needs,
e.g. you could remove the redirect action so that only a message is displayed.




---------------------------------------------
Content Profile User Registration Integration
----------------------------------------------

There is a small extension module shipping with the main module, which allows one to enable
registration integration per content profile. 


This module builds upon the main content profile module. It allows to integrate
the form of one or more content profile into the user registration page.


Installation 
------------
 * Activiate the module.
 * Be sure to read the usage notes below!
 
 
 Usage:
--------
 * When you edit a profile content type there will be a further tab "Content profile",
   which provides content profile specific settings. There is now a new field group
   called "User Registration" which allows you to enable this feature for a content profile.
   
 * You need not grant anonymous users access to create the content profile. If you would do so,
   anonymous users would be able to create anonymous profiles even without registering.
   
 * If you use the "Content permissions" module, which comes with CCK, make sure you grant access
   to fields that should appear for anonymous users.
   
 * The weight of the profile (configurable at the content profile settings) controls the position
   of the form elements on the registration page. 

 * You may also hide some form elements at the settings. Basically it allows you to hide non-required
   CCK fields as well as the title. If the title is hidden, it is set to the user's name.
    
 * For more control over the title use the "Automatic Nodetitles" module, which can be found
   at http://drupal.org/project/auto_nodetitle. It integrates fine with this module. 

 * Hiding required CCK fields is not supported, as the created content node would have empty
   required fields afterwards, which in affect would make it impossible even for admins to edit
   the content node.
  
 * So the "Hide other form elements" option allows you to hide all form elements not listed there,
   but required CCK fields always stay.
   
   However, you can still hide required CCK fields by restricting anonymous access to them by using the 
   "Content permissions" module of CCK. But be aware of this issue - maybe also restrict access for
   other roles accordingly.

 * If you want to hide the "body" field, just remove it from the content type in general at the content
   type's settings page. Then instead of this, just create a CCK textfield, which can be hidden.  

 * You can enable the registration integration for multiple profiles - however be aware that
   shared form elements like the title only appear once and all created profile nodes get the same
   values assigned.
   
 * For multiple registration paths for different roles, the AutoAssignRole module might help you:
   http://drupal.org/project/autoassignrole. It comes with Content Profile Registration Integration,
   so that you can select the profiles which should appear on each AutoAssignRole path (configurable
   at the content profile settings). You'll need a version of AutoAssignRole released later than 
   June 4, 2009. 

 * If you want to prepopulate some other form elements, maybe hidden CCK fields you can use the rules
   module for that. See http://drupal.org/project/rules.
   Just configure a rule, that reacts on the creation of the content profile (event) and populates
   your fields value (action).

 * Putting file uploads on the registration form is not supported and probably won't work right.
 
 * The CCK "Add more fields" feature is only working for users with javascript turned on in the
   registration form. Users without javascript won't be able to add more fields. Interested developers
   can find the related issue (in drupal itself) here: http://drupal.org/node/634984
 
 
  
-----------------------
Content Profile Tokens
-----------------------

Original author: @author Ádám Lippai - Oghma ltd. (lippai.adam@oghma.hu)


This is a small module that adds content profile tokens for textfields and number CCK fields for
a user as well as to the 'flag friend' modules' requester and requestee.

Warning: This module slows down the generation of users tokens, thus it might have some performance
         implications for your site. Use it with caution. 

Installation 
------------
 * Activiate the module.
 ImageAPI 

A non writing image manipulation API for Drupal. This API is meant to be used in place of the API provided 
by image.inc. You probably do not need to install this module unless another module are you using requires
it. It provides no new features to your drupal site. It only provides an API other modules can leverage.

Changes From image.inc API:
  - Images are objects.
  - Images are not written on each image operation and must be explicitly 
    closed when processing is complete. 
  - Multiple Image ToolKits can be used simultaneously. However, only the image
    toolkit and image was opened with can be used to process it. This is hidden 
    in the imageapi layer.

API Quick Reference:
  imageapi_image_scale_and_crop($image, $width, $height) 
  imageapi_image_scale($image, $width, $height, $upscale = FALSE) 
  imageapi_image_resize($image, $width, $height) 
  imageapi_image_rotate($image, $degrees, $bgcolor = 0x000000) 
  imageapi_image_crop($image, $x, $y, $width, $height) 
  imageapi_image_desaturate($image) 
  imageapi_image_open($file, $toolkit = FALSE) 
  imageapi_image_close($image, $destination) 

  $image is an image object returned from imageapi_image_open();

Expanding ImageAPI:

  If you wish to expand on ImageAPI add a new wrapper function to 
  imageapi.module. Do any common preprocessing for all underlying layers in the 
  wrapper function, then invoke the driver. Pay heed to the function naming in
  ImageAPI and ImageAPI GD. If the toolkit changes the size of an image it must
  update the $image->info['width'] and $image->info['height'] variables. All 
  ToolKit functions should return TRUE on success and FALSE on failure.

For more detailed documentation read imageapi.module.

-dopry
/* $Id $ */

Custom Breadcrumbs 6.x-1.x (See below for 6.x-2.x)
--------------------------------------------------
Summary
-------
* Enable the module
* Assign 'administer custom breadcrumbs' permission to those roles that should
  be allowed to add/edit/delete custom breadcrumbs.
* Assign 'use php in custom breadcrumbs' to roles that should be allowed to use
  php to determine breadcrumb visibility.
* Go to Administer > Site building > Custom breadcrumbs to add new breadcrumbs
* Click "Add a new custom breadcrumb"
* Choose the node type to create a breadcrumb trail for
* For the titles, put each "crumb" one line after another (There is no need to
  put in "home"):

  Item 1
  SubItem A
  SuperSubItem X

* For the paths, put the path to each crumb starting after the domain name.
  Don't include a leading or trailing slash.

  item1
  item-1/subitem-a
  item-1/subitem-a/supersubitem-x

* Click save to save the breadcrumb
* Visit the page and your breadcrumb should appear!

Description
-----------
As the name suggests, Custom Breadcrumbs allows you to create and modify your
own breadcrumbs based on node type. After enabling the module, click on
Administer > Site building > Custom breadcrumbs. You'll be abel to add new
breadcrumbs from this page.

Clicking on that link, you have the option to select the node type the
breadcrumb will apply to. There are two text fields below-- "Titles" and 
"Paths." When creating a breadcrumb, you're simply creating a link. In the
custom breadcrumbs interface "Titles" describes the text of the breadcrumb
while "Paths" describes the Drupal path the breadcrumb links to. Each Title
must have a corresponding Path.

To give a very simple example of how to use this module, let's say I have a
blog on my web site called "Deep Thoughts." To create this, I use the Views
module to create a page at /blog that displays all the node types "blog post."
Whenever a user views a blog post I want the breadcrumb to show
Home > Deep Thoughts instead of simply Home. To do this I would simply type
"Deep Thoughts" in the "Titles" field and and "blog" in the "Paths" field and
save my breadcrumb.

Using the Tokens module, the Custom breadcrumbs module becomes much more
flexible because breadcrumbs can become dynamic. You can create a breadcrumb
like Home > Deep Thoughts > [Month of Blog Post] [Year of Blog Post], where
"Deep Thoughts" links to my main blog page and "[Month of Blog Post]
[Year of Blog Post]" links to a view that shows only blog posts from the month
and year the blog post was created (e.g. June 2007). For this, you would do
the following:

Node Type:
Blog Post

Titles:
Deep Thoughts
[month] [yyyy]

Paths:
blog
blog/[mm]_[yyyy]

(where of course, blog/[mm]_[yyyy] is the path to the view of blog posts from
that month and year). So if you created a blog pos on June 13, 2007 your
breadcrumb would show Home > Deep Thoughts > June 2007 and "June 2007" links
to "blog/06_2007" which is a view of all blog posts from June 2007.

Also, note that Custom Breadcrumbs doesn't actually check to be sure that a
particular path exists, so you'll have to check yourself to avoid 404 errors.

Only users with 'administer custom breadcrumbs' permission will be allowed to
create or modify custom breadcrumbs.

Breadcrumb Visibility
---------------------
Users given 'use php in custom breadcrumbs' permission can include a php code
snippet that returns TRUE or FALSE to control whether or not the breadcrumb is
displayed. Note that this code has access to the $node variable, and can check
its type or any other property. Tokens should not be used in the visibility
code snippet, since they will not be replaced.

Special Identifiers
-------------------
The following identifiers can be used to achieve a special behavior:
<pathauto> - will clean any path using the current pathauto module settings,
             if that module is installed.
<none>     - can be used as a path to have a breadcrumb element that is not
             hyperlinked.

Identifiers should be added to the paths area in the following format:
identifier|path. To be recognized, the identifier must be enclosed in angular
brackets, and proceed any part of the path:

For example: <pathauto>|[ogname-raw]


Custom Breadcrumbs 2.0
----------------------

Summary
-------
* Enable the module and any option submodules (see below for details)
* Assign 'administer custom breadcrumbs' permission to those roles that should
  be allowed to add/edit/delete custom breadcrumbs.
* Assign 'use php in custom breadcrumbs' to roles that should be allowed to use
  php to determine breadcrumb visibility.
* Go to Administer > Site Configuration > Custom breadcrumbs Settings to select
  the 'Home' breacrumb text and possibly other global settings.
* Go to Administer > Site building > Custom breadcrumbs to add new breadcrumbs
* To add a breadcrumb, click on one of the tabs at the top of the page. For
  example, click 'Node' to create a custom breadcrumb based on node type.
* Fill in the required information for the breadcrumb (varies depending on 
  breadcrumb type, see below).
* For the titles, put each "crumb" one line after another (There is no need to
  put in "home")
* (optional) For each crumb title you can specify a title attribute ("tooltip")
  to add to the link. Separate the crumb title and the title attribute with a
  pipe (|) symbol:

  Item 1
  SubItem A|Title attribute for SubItemA (optional)
  SuperSubItem X

* For the paths, put the path to each crumb starting after the domain name.
  Don't include a leading or trailing slash.

  item1
  item-1/subitem-a
  item-1/subitem-a/supersubitem-x

* Click save to save the breadcrumb
* Visit the page and your breadcrumb should appear!

New Features
------------
In the 6.x-2.x release, custom breadcrumbs has many new features which are
available through optional modules in the custom breadcrumbs package. The base
module, required by all the others, is still custom_breadcrumbs. This module
handles custom breadcrumbs based on node type as described above. The following
optional modules can also be installed to provide custom breadcrumbs in a
variety of situations:

+ custom_breadcrumbs_views provides custom breadcrumbs on views pages.
  Once this module is enabled, a new "Views" tab will appear at
  admin/build/custom_breadcrumbs. To add a views page breadcrumb, click on the
  tab and then select the view from list of available views. Fill in the
  visibility, title and paths sections as described above, and your breadcrumb
  should appear on your views page. Note that token substitution is possible
  with global and user tokens only. The $view object is available for use in
  the php_visibility section.

+ custom_breadcrumbs_paths provides custom breadcrumbs on nodes and views at
  a specified path (url). Once this module is enabled, a new "Path" tab will
  appear at admin/build/custom_breadcrumbs.  To add a breadcrumb for a node
  or a view at a specific path, just enter the Drupal path in the Specific
  Path section. Fill in the visibility, title and paths sections as
  described above, and save the breadcrumb. Now your breadcrumb should appear
  on the node or view at the specific path that you selected. Note that custom
  breadcrumbs does not check the validity of the entered path. When entering a
  path for a particular language (see below), do not specify the two-letter
  language prefix. Custom breadcrumbs will assume the correct prefix according
  to the selected language. To use '*' as a wildcard, go to custom breadcrumbs
  configuration page at /admin/settings/custom-breadcrumbs and select the
  'Use wildcard pattern matching in paths' option in the advanced settings
  section. When this option is enabled, the breadcrumb that best matches the
  path will be selected. The best match is determined by the depth at which
  the first wildcard appears. For example, if the path is path/to/some/content
  and breadcrumbs have been defined for path/to/* and path/to/some/*, the
  latter will be chosen as the best match.

+ custom_breadcrumbs_taxonomy provides custom breadcrumbs on taxonomy term
  pages, views, and for nodes that are assigned a taxonomy vocabulary or term.
  Once this module is enabled, two new tabs will appear appear at 
  admin/build/custom_breadcrumbs: Term and Vocabulary. Breadcrumb generation
  can be handled in two different ways. If 'use the taxonomy term hierarchy'
  is checked at custom breadcrumbs configuration page, then breadcrumbs will
  be generated similarly to the taxonomy_breadcrumb module. Otherwise,
  breadcrumb generation will be according to the standard custom breadcrumbs
  approach.

  In taxonomy breadcrumb mode, the breadcrumb trail is automatically
  constructed based on the taxonomy term hierarchy:
  [HOME] >> [VOCABULARY] >> TERM >> [TERM] >> [TITLE]. In this mode the
  breadcrumb titles are the term and vocabulary names. The paths these titles
  are linked to can be assigned via the Term and Vocabulary tabs at
  admin/build/custom_breadcrumbs. Providing a path for a vocabulary will enable
  the [VOCABULARY] portion of the breadcrumb.  The path for a term can
  similarly be set, but if one is not provided the default taxonomy/term/tid
  (where tid is a number, the taxonomy term id) will be used. Select the types
  of nodes to include or exclude at the custom breadcrumbs configuration
  settings page. The option to add the node title at the end of the breadcrumb
  trail can also be enabled on that page. There is also an option to append
  the current taxonomy term to the breadcrumb on taxonomy term pages
  (defined to be any page with drupal path */taxonomy/term/*).

  In the standard custom breadcrumbs mode, you can provide the titles and paths
  for constructing the breadcrumb trail on nodes that have defined taxonomy
  terms. Note that if a node has more than one term, the lightest term in the
  lightest vocabulary with a defined custom breadcrumb will be used.

  Note: do not use this module and the taxonomy_breadcrumb module at the same
  time. Custom_breadcrumbs_taxonomy has extended the functionality of 
  taxonomy_breadcrumb, so that module is not needed if you are using 
  custom_breadcrumbs.

  While at admin/settings/custom-breadcrumbs, go ahead and enable any
  additional taxonomy breadcrumb options that suits your needs. If you are
  using views to override taxonomy term pages, then be sure to enable the
  "Use taxonomy breadcrumbs for views" option.

+ custom_breadcrumbsapi provides a simple api that allows custom breadcrumbs to
  be defined for module pages implementing the api. Module developers need to
  provide a modulename_custom_breadcrumbsapi() function that returns an array
  containing the names of the module pages for which custom breadcrumbs may be
  defined.

  The following is an example that could be used with the forum module.

  /**
   *  Implementation of hook_custom_breadcrumbsapi().
   *  Allow custom breadcrumbs for the following module pages.
   */
  function forum_custom_breadcrumbsapi() {
    return array('forum listing');
  }

  Then, in the callback functions for each of those pages, the following line
  must be inserted within the function (preferably after defining $breadcrumb
  but before setting the breadcrumb):
  
  drupal_alter('breadcrumb', $breadcrumb, 'module_page_name');

  Continuing with the forum module example, 'module_page_name' would be
  replaced with 'forum listing'.
  
  custom_breadcrumbsapi can also provide custom breadcrumbs for modules 
  implementing theme templates (e.g. files ending in .tpl.php). To add a 
  custom breadcrumb when a specific theme template file is called, click
  on the module page tab at admin/build/custom_breadcrumbs. Select the
  template file from the list of theme templates (determined from the 
  theme registry). Then fill in the usual custom breadcrumbs information
  such as titles as paths. If using a php snippet for breadcrumb visibility
  or to specify titles and paths (see below), you have access to the template
  variables through $variables, an associative array defined by the module
  providing the template. See the documentation in the template file for
  details. For example, if a template file uses the variable $foo, then
  access to that variable would be through $variables['foo'].

User Interface
--------------
The user interface has been modified for Custom Breadcrumbs 2.0. Breadcrumbs
from all custom breadcrumbs modules are tabulated at
admin/build/custom_breadcrumbs. The table can be sorted according to
breadcrumb name, type, language (if locale is enabled) by clicking on the
column headers. The table can also be filtered to display breadcrumbs of a
specific type, language, or combination of the two.

A new custom breadcrumbs fieldset has  been added to node edit pages. All
defined breadcrumbs for a particular node are displayed here, with an option to
edit each.  If no breadcrumbs have been defined for a particular node, then a
link can be followed back to admin/build/custom_breacrumbs to add a custom
breadcrumb.

Languages
---------
If the core Locale module is enabled, then an additional option to specify the
language for the breadcrumb is available when constructing the breadcrumb trail
(with any of the custom breadcrumb modules).

HOME breadcrumb
---------------
The text to display at beginning of the breadcrumb trail can be assigned from
the custom breadcrumb configuration settings page. Typically this is Home or
your site name. You can leave it blank to have no home breadcrumb. As with
normal crumb titles, you can optionally specify a title attribute ("tooltip")
for the crumb. Just separate the crumb text and the title attribute text with a
pipe (|) symbol (i.e. Home crumb text|attribute title text). There is
also an advanced setting to set the Home breadcrumb text on ALL pages, not
just those with defined custom breadcrumbs. You can also use this feature to
remove the home breadcrumb on all pages on the site - just enable the advanced
setting and then leave the home breadcrumb text blank.

It is possible to translate the home reference title from custom breadcrumbs
using the i18n module. Just put this in your settings.php:

  $conf['i18n_variables'] = array(
    //custom breadcrumbs
    'custom_breadcrumb_home',
  );

Then you can change it for each language at
http://example.com/#lang-prefix#/admin/settings/custom-breadcrumbs.

See http://drupal.org/node/313272 for additional information.

Use PHP in breadcrumb titles and paths
--------------------------------------
If this advanced option is enabled at admin/settings/custom-breadcrumbs, then
users given 'use php in custom breadcrumbs' permission can include small php
code snippets (less than 250 characters)in the titles and/or paths fields of
the add breadcrumb form. Be careful when enabling this option, as the incorrect
use of php can break your site.

There are a couple of ways to use php in breadcrumbs and titles. One way is to
return an array of breadcrumb titles in the titles text field and a
corresponding array of breadcrumb paths in the paths text field such as

Titles:
<?php return array('title-1','title-2','title-3');?>

Paths:
<?php return array('path/to/title-1','path/to/title-2','path/to/title-3');?>

Sometimes, it may be more convient to assign the titles and paths in the same
code snippet, so you can also return an associate array with elements 'titles'
and 'paths' that contain the titles and paths arrays, respectively.
For example,

Titles:
<?php $titles = array('title-1','title-2','title-3');
$paths = array('path/to/title-1','path/to/title-2','path/to/title-3');
return array('titles' => $titles, 'paths' => $paths); ?>

(In this case, the paths text field will be ignored, so you can leave it
empty).

When defined, appropriate objects such as $node, $term, or $view, will be
available for these code snippets. Note that if this option is enabled and an
array is not returned, then the module defaults to the standard operation of
using each line of the titles and paths text fields to define a part of the
breadcrumb.

For longer code snippets (greater than 250 characters), you can save your code
snippet in an include file and use a php require_once statement in the titles
and/or paths section of your custom breadcrumb to include and evaluate your
code. See http://drupal.org/node/654766 for an example of this.

Add CSS classes to custom breadcrumb elements
---------------------------------------------

You can enable this feature on the custom breadcrumbs configuration screen
under the HTML element identifiers section. There are several options that
provide html class identifiers for theming custom breadcrumb links, including
add a 'custom-breadcrumbs-home' ID attribute to the home breadcrumb item,
adding numbered class attributes 'custom-breadcrumbs-item-N' for each
breadcrumb item, adding even and odd classes to breadcrumb items and storing an
identifier that is unique for each defined custom breadcrumbs. Using this
last option requires modifying your sites phptemplate_breadcrumb (or theme
override) function to actually add the class name to the breadcrumb container.
The class name is returned as a string by the function 
custom_breadcrumbs_unique_breadcrumb_id(). The identifier will be of the form
'custom-breadcrumbs-type-id'where type is the breadcrumb type (node, panels,
path, views or taxonomy) and id is the breadcrumb id number.
See http://drupal.org/node/643796#comment-2532998 for more information on this
feature.

Special Identifiers
-------------------
In Custom Breadcrumbs 2.0, Special identifiers are now provided as a separate,
optional module - custom_breadcrumbs_identifiers. At present, this module
provides the following identifiers:

<none>              - Produces a plain text crumb. This identifier should not
                      be used with the pipe (|) symbol.
<pathauto>          - Cleans the given path using your pathauto replacement
                      rules.
<book-hierarchy>    - Provides crumbs for each parent node of a book page.
                      Whatever is placed in the corresponding position of the
                      title area will be ignored. It should not be used with
                      the pipe (|) symbol.
<page-title>        - Provides a plain text crumb using the page title. Whatever
                      is placed in the corresponding position of the title area
                      will be ignored. It should not be used with the pipe (|)
                      symbol.
<menu-parent-trail> - Produces crumbs for each parent item for the given path.
                      The title information for this line will be ignored
                      because the menu link titles are used. If a path is not
                      provided following the pipe (|) symbol, the current path
                      with be used.

Additional special identifiers can be developed and added by contributed
modules that implement hook_cb_identifier_list(), to provide a description of
the identifer, and hook_cb_identifier_values(), to prepare the appropriate
crumb items. See the custom_breadcrumbs_identifiers.module for examples of
how to do this.

Identifiers should be added to the paths area in the following format:
identifier|path. To be recognized, the identifier must be enclosed in angular
brackets, and proceed any part of the path:

For example: <pathauto>|[ogname-raw]

Note that not all identifiers require the use of |path.

Authors
-------
bennybobw, dbabbage, Michelle, MGN
INFORMATION FOR DEVELOPERS

Once the Date API is installed, all functions in the API are available to be used 
anywhere by any module. If the Date Timezone module is installed, the system site 
timezone selector and the user timezone selectors are overwritten to allow the 
selection of timezone names instead of offsets. Proper timezone conversion 
requires knowledge of those timezone names, something that is not currently 
available in Drupal core, and the change in selectors makes it possible to track it.

In most cases, you should enable the Date Timezone module any time you use the
Date API to be able to set the site and user timezone names. It is not enabled by 
default in case another module is setting timezone names in the database.

The API uses the PHP 5.2 date functions to create and manipulate dates, and 
contains an option module that will emulate those functions in earlier versions
of PHP.

If you are using PHP 4 or PHP 5.0 or 5.1, native date handling won't work right.
Install the Date_PHP4 module to enable wrapper functions so this code will work
in old PHP versions. 

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

A helper function is available, date_make_date($string, $timezone, $type),
where $string is a unixtimestamp, an ISO date, or a string like YYYY-MM-DD HH:MM:SS,
$timezone is the name of the timezone this date is in, and $type is the type
of date it is (DATE_UNIX, DATE_ISO, or DATE_DATETIME). It create and return
a date object set to the right date and timezone.

Simpletest tests for these functions are included in the package.

Available functions include the following (more documentation is provided in 
the files):

============================================================================
Date PHP4 Module
============================================================================
PHP 4 substitutions for the PHP 5 date functions are supplied. Use the PHP 5 
functions in your code as they would normally be used and the PHP 4 
alternatives will be automatically be substituted in when needed. 

You cannot do everything with these functions that can be done in PHP 5, but 
you can create dates, find timezone offsets, and format the results. 
Timezone handling uses native PHP 5 functions when available and degrades 
automatically for PHP 4 to use substitutions like those 
provided in previous versions of the Date and Event modules.

Read the doxygen documentation in this module for more information 
about using the functions in ways that will work in PHP 4.

Simpletest tests for the PHP 4 equivalent functions are included in the package.

The following functions are emulated in PHP4:
date_create()
date_date_set()
date_format()
date_offset_get()
date_timezone_set()
timezone_abbreviations_list()
timezone_identifiers_list()
timezone_offset_get()
timezone_open()

============================================================================
Preconfigured arrays
============================================================================
Both translated and untranslated values are available. The date_week_days_ordered()
function will shift an array of week day names so it starts with the site's
first day of the week, otherwise the weekday names start with Sunday as the first
value, the expected order for many php and sql functions.

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
date_t()
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
The SQL functions are found in date_api_sql.inc, which is not included by default. 
Include that file if you want to use these functions:

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
  get re-formatted back into a date value of the requested type during validation.

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
Install file for dependent modules
============================================================================

The following code is an example of what should go in the .install file for
any module that uses the new Date API. This is needed to be sure the system 
is not using an earlier version of the API that didn't include all these new 
features. Testing for version '5.2' will pick up any version on or after the 
change to the new API.

/**
 * Implementation of hook_requirements().
 */
function calendar_requirements($phase) {
  $requirements = array();
  $t = get_t();

  // This is the minimum required version for the Date API so that it will 
     work with this module.
  $required_version = 5.2;

  // Make sure the matching version of date_api is installed.
  // Use info instead of an error at install time since the problem may
  // just be that they were installed in the wrong order.
  switch ($phase) {
    case 'runtime':
      if (variable_get('date_api_version', 0) < $required_version) {
        $requirements['calendar_api_version'] = array(
          'title' => $t('Calendar requirements'),
          'value' => $t('The Calendar module requires a more current version 
             of the Date API. Please check for a newer version.'),
          'severity' => REQUIREMENT_ERROR,
          );
      }
      break;
     case 'install':
      if (variable_get('date_api_version', 0) < $required_version) {
        $requirements['calendar_api_version'] = array(
          'title' => $t('Calendar requirements'),
          'value' => $t('The Calendar module requires the latest version 
             of the Date API, be sure you are installing the latest versions 
             of both modules.'),
          'severity' => REQUIREMENT_INFO,
          );
      }
      break;
  }
  return $requirements;
}

/**
 * Implementation of hook_install().
 */
function calendar_install() {
  // Make sure this module loads after date_api.
  db_query("UPDATE {system} SET weight = 1 WHERE name = 'calendar'");
}

/**
 * Implementation of hook_update().
 */
function calendar_update_5000() {
  $ret = array();
  $ret[] = update_sql("UPDATE {system} SET weight = 1 WHERE name = 'calendar'");
  return $ret;
}
The tests here were written for an older version of simpletest and
still need to be updated to work with the current version.

This folder includes files that can be used to test imports of date information.
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

CONTENTS OF THIS FILE
-----------------------------------------------------------------------------------------
 * Introduction
 * Installation
 * Usage

INTRODUCTION
-----------------------------------------------------------------------------------------
Author Pane (http://drupal.org/project/author_pane) provides information about the author
of a node, comment, or page. From core, it collects the user picture, name, join
date, online status, contact link, and profile information. In addition, it gathers data
from many user related contributed modules and puts it together in a modifiable template
file.

INSTALLATION
-----------------------------------------------------------------------------------------
1. Copy the entire author_pane module directory into your normal directory for modules,
   usually sites/all/modules.

2. Enable the Author Pane module in ?q=admin/build/modules.

USAGE
-----------------------------------------------------------------------------------------
Advanced Forum:
If you have Advanced Forum installed, it will make use of Author Pane automatically on
forum posts. Advanced Forum provides its own Author Pane template and CSS so it can be
styled specifically for use in the forums.

Advanced Profile Kit:
If you have Advanced Profile Kit installed, it will make use of Author Pane automatically
on the default user page variant. Advanced Profile Kit provides its own Author Pane
template so it can be styled specifically for use on profile pages. Please note that if
you remove and re-add the Author Pane content type, you will need to edit the pane
settings and put "advanced_profile" back in the "Caller" field.

CTools content pane:
If you have Page Manager (from CTools) installed, you can add the Author Pane content
pane to any page variant. It requires the user context. You can choose an imagecache
preset to use for the user picture. You can also use the "caller" field to give this
instance a unique ID that can be accessed from the preprocess functions and the template
file.

Block:
There is an Author Pane block provided that you can enable. The block will show up on
user/NN, blog/NN, and node/NN where the node type is one that you allow in the block
config. If you want to exclude it from one of those page types, use the core block
visibility option. Exclusion of the /edit page happens automatically. 

The block is disabled by default and must be enabled. Further options are available by
configuring the block:

* Node types to display on - Check on which node types the block should be shown. The
  block will show in the region it is placed, not literally on the node, and only on
  full node view pages. (ie: node/42 not when the node is part of a view)

* User picture preset - This is the Imagecache preset that will be used to format the
  user picture. Leave blank to show the full sized picture. Requires Imagecache module.

Theme function:
You can call the theme function directly and print the author pane anywhere in your code.
You must have a fully loaded user object to pass into the function. The rest of the
parameters are optional.

<?php
print theme('author_pane', $account, $caller, $picture_preset, $context, $disable_css);
?>

Parameters:
$account - The fully loaded user object. If all you have is a UID, you can get the object
with $account = user_load($uid); where $uid is a variable holding the user id.

$caller - (optional) This is an ID you can pass in as a way to track who is calling the
function. If you use Author Pane on your user profiles, on your blog pages, and in your
forums, you may want to display slightly different information in each Author Pane. By
passing in the caller, you can tell from within the preprocess functions where this is
going to be displayed.

$picture_preset - (optional) This is an imagecache picture preset that, if given, and
if imagecache is enabled, will be used to size the user picture on the author pane.

$context - (optional) This is usually a node or comment object and gives the context of
where the Author Pane has been placed so information from that context is available to
the template and preprocesses.

$disable_css - (optional) Because the Author Pane preprocess gets called after the code
that calls it, the Author Pane CSS file will be loaded last and clobber any earlier CSS.
This option tells Author Pane not to load its CSS so it uses the CSS of the caller. This
is mainly intended for Advanced Forum because the styles include Author Pane styling but
can be used for custom purposes as well.








-- SUMMARY --

jQuery UI (http://ui.jquery.com/) is a set of cool widgets and effects that
developers can use to add some pizazz to their modules.

This module is more-or-less a utility module that should simply be required by
other modules that depend on jQuery UI being available. It doesn't do anything
on its own.

For a full description of the module, visit the project page:
  http://drupal.org/project/jquery_ui

To submit bug reports and feature suggestions, or to track changes:
  http://drupal.org/project/issues/jquery_ui


-- REQUIREMENTS --

* The jQuery UI library.


-- INSTALLATION --

* Copy the jquery_ui module directory to your sites/all/modules directory, so it
  is located in sites/all/modules/jquery_ui/.

* Download the jQuery UI 1.6 release from:

    http://code.google.com/p/jquery-ui/downloads/list?q=1.6

* Put the downloaded archive into the directory:

    /sites/all/libraries/jquery.ui-1.6.zip

* Extract the archive.  This will create the following sub-directory:

    /sites/all/libraries/jquery.ui-1.6/

* Rename the sub-directory into "jquery.ui":

    /sites/all/libraries/jquery.ui/

  so the actual jQuery UI JavaScript files are located in:

    /sites/all/libraries/jquery.ui/ui/*.js

* Enable the module at Administer >> Site building >> Modules.


-- JQUERY UI 1.7 --

The jQuery UI module uses jQuery UI 1.6 because jQuery UI 1.7 requires at least
jQuery 1.3, which is not shipped with Drupal 6. If you absolutely need to move
to jQuery UI 1.7, you can get around this by doing the following:

* Download and install the corresponding jQuery Update module from:

    http://drupal.org/project/jquery_update

* Download the latest jQuery UI 1.7 release from:

    http://code.google.com/p/jquery-ui/downloads/list?q=1.7

* Put the downloaded archive into the directory:

    /sites/all/libraries/jquery.ui-1.7.zip

* Extract the archive.  This will create the following sub-directory:

    /sites/all/libraries/jquery.ui-1.7/

* Rename the sub-directory into "jquery.ui":

    /sites/all/libraries/jquery.ui/

  so the actual jQuery UI JavaScript files are located in:

    /sites/all/libraries/jquery.ui/ui/*.js

* Enable the module at Administer >> Site building >> Modules.


-- API --

Developers who wish to use jQuery UI effects in their modules need only make
the following changes:

* In your module's .info file, add the following line:

    dependencies[] = jquery_ui

  This will force users to have the jQuery UI module installed before they can
  enable your module.

* In your module, call the following function:

    jquery_ui_add($files);

  For example:

    jquery_ui_add(array('ui.draggable', 'ui.droppable', 'ui.sortable'));

    jquery_ui_add('ui.sortable');  // For a single file

  See the contents of the jquery.ui-X.X sub-directory for a list of available
  files that may be included, and see http://ui.jquery.com/docs for details on
  how to use them. The required ui.core file is automatically included, as is
  effects.core if you include any effects files.

-- CONTACT --

Current maintainers:
* Jeff Robbins (jjeff)
* Angela Byron (webchick)
* Addison Berry (add1sun)
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136

// $Id: README.txt,v 1.6 2009/10/29 01:51:48 davereid Exp $

CONTENTS OF THIS FILE
---------------------

 * Description and Benefits
 * Upgrading from 1.x
 * Installation and Usage
 * More Information


DESCRIPTION AND BENEFITS
------------------------

The SEO Checklist module provides a list of good SEO actions that you should
take to maximize the presence of your website in the major search engines. It
provides little functionality itself but rather it helps you keep track of what
needs to be done and what has been completed already.

Search Engines Drive 90% of the traffic on the web. The more "findable" you are,
the easier it is for you to get customers. This module helps you with on-page
SEO - a necessary component of a good online marketing campaign.


UPGRADING FROM 1.x
------------------

If you are upgrading from the previous SEO Checklist 1.x versions, you will
need to follow a couple important steps:

1. Make sure you remove the entire SEO Checklist module's folder before copying
   in the new files.
2. Execute the following SQL in your site's database, making sure to prefix
   the 'system' table name if your site uses a table prefix:
   UPDATE system SET name = 'seochecklist', filename = REPLACE(filename, 'SEOChecklist', 'seochecklist'), status = 1 WHERE type = 'module' AND name = 'SEOChecklist'

3. Make sure you run update.php immediately afterwards.


INSTALLATION AND USAGE
----------------------

See http://drupal.org/getting-started/5/install-contrib for instructions on
how to install or update Drupal modules.

Summary:
1. Download and extract the module package into your sites/all/modules directory.
2. Go to admin/build/modules and enable the "SEO Checklist" module which should
   be in the 'Other' category.
3. To start using the SEO Checklist, go to admin/settings/seochecklist. The
   module should automatically check if you have already installed any of the
   modules required for a task.
4. Start checking off some tasks!

Optional:
- Install the Vertical Tabs module (http://drupal.org/project/vertical_tabs) to
  help improve your SEO Checklist interface. It helps collapse the interface
  into vertical tabs instead of one huge long list of fieldsets. This module
  also works on the add or edit content forms, which is helpful for your site's
  content creators and editors!


MORE INFORMATION
----------------

- A very handy companion for this module is the Drupal 6 Search Engine
  Optimization book by Ben Finklea. For more information and to purchase, go to
  http://www.drupalseobook.com/.

- To issue any bug reports, feature or support requests, see the module issue
  queue at http://drupal.org/project/issues/seo_checklist.

- This module is potentially controversial as many people have ideas about good
  and bad SEO. If you have an idea of a module or task that should be included,
  please file an issue with the above link to the module's issue queue.

- Volacci spent numerous hours in research and development on this module. We
  want to maintain it and keep good SEO advice available to the entire
  community. Instead of asking for donations or bounties for this module, we
  request that you include a simple link back to us somewhere on your website.
  When you're done (or before) go down to the "Link to Volacci" task and check
  it! That will automatically add a link in your website's footer to Volacci.
  If you want to link to use, but not in your footer, uncheck the box and put
  the link to http://www.volacci.com/ where you want to. And thanks for the
  link! If you e-mail us (seochecklist [at] volacci.com) and tell us where your
  link is, then we'll link back to you! And as you may know, links help move
  your site up in the search engines.

- Enjoy using the module!
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Views Fluid Grid
;; $Id: README.txt,v 1.1.2.2 2009/09/27 13:07:47 markuspetrux Exp $
;;
;; Original author: markus_petrux (http://drupal.org/user/39593)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTENTS OF THIS FILE
=====================
* OVERVIEW
* VIEWS INTEGRATION
* REQUIREMENTS
* INSTALLATION
* CUSTOMIZATION
  * TEMPLATES
  * STYLESHEETS
  * ADVANCED


OVERVIEW
========

This module provides the Fluid Grid style plugin for Views. This plugin displays
the view as a fluid grid using an HTML list element.

The plugin settings form provides options to define the width and height of the
elements in the grid. But it also provides advanced layout options implemented
in separate CSS classes that allow you to define item margins, alignment and a
couple of CSS3 properties (box-shadow and border-radius).


VIEWS INTEGRATION
=================

A fluid grid style plugin could be included in Views in the future. For further
information, please see the following issue in the Views queue:

http://drupal.org/node/377574


REQUIREMENTS
============

- Views.
  http://drupal.org/project/views


INSTALLATION
============

- Be sure to install all dependent modules.

- Copy all contents of this package to your modules directory preserving
  subdirectory structure.

- Go to Administer -> Site building -> Modules to install module.

- You can now start using the Fluid grid style plugin in your views.


CUSTOMIZATION - TEMPLATES
=========================

Please, see the "Theme: Information" option in Views UI. Information about
the template used by this style plugin is available under the "Style output"
entry.

The template shipped with the module is views-fluid-grid-plugin-style.tpl.php
located under the theme subdirectory of the package.


CUSTOMIZATION - STYLESHEETS
===========================

The following stylesheets are provided:

- views_fluid_grid.base.css

  It contains the base CSS classes to style the fluid grid.

- views_fluid_grid.size.css

  It contains additional CSS classes that are used to define the width and
  height of the items in the grid. These sizes are defined for each option
  in the settings form of the style plugin. If you need to add more sizes to
  the list, please see ADVANCED section below.

- views_fluid_grid.advanced.css

  If contains additional CSS classes to implement the advanced layout options
  available from the settings form of the style plugin. This file is loaded
  only if any of these advanced options are really used.


CUSTOMIZATION - ADVANCED
========================

You may want to use a different set of values for a few style plugin options.
To do so, you need to add the proper entries to your settings.php file.

@code
// Custom options for Views Fluid Grid style plugin.
$conf['views_fluid_grid_plugin_style_widths']  = array(100, 150, 180, 200, 250, 300, 350, 400, 450, 500);
$conf['views_fluid_grid_plugin_style_heights'] = array(100, 150, 200, 250, 300, 350, 400, 450, 500);
$conf['views_fluid_grid_plugin_style_margins'] = array('0', '2px', '4px', '6px', '8px', '10px', '0.2em', '0.5em', '0.8em', '1em', '1.2em', '1.5em', '1.8em', '2em');
@endcode

You can add more items to any of these variables to suit your needs. Then, you
also need to provide the proper CSS classes. See the stylesheets shipped with
this module to find out how these values match CSS classes. See examples for
classes used for width and height in css/views_fluid_grid.size.css.

Note that dots in $conf['views_fluid_grid_plugin_style_margins'] will be
converted to dashes. See examples in css/views_fluid_grid.advanced.css.

Examples:

@code
/* This class is used for width 120. */
ul.views-fluid-grid-items-width-120 li.views-fluid-grid-item { width: 120px; }

/* This class is used for horizontal margin 0.6em. */
ul.views-fluid-grid-items-h-margin-0-6em li.views-fluid-grid-item { margin-left: 0.6em; margin-right: 0.6em; }
@endcode
Better formats is a module to add more flexibility to Drupal's core input format system.
Features

    * Set the default format per role.
    * Set the default format per content type.
    * Control allowed formats per content type.
    * Hide format tips.
    * Hide format selection, forcing the default to be used.
    * Expand the selection fieldset by default.
    * Disable the expand/collapse of the selection fieldset.
    * Set selection fieldset title.
    * Set default formats for nodes, comments, and blocks separately.
    * Works with CCK textareas.
    * Panels comment support.
    * I18n module support.
    * and more.

-------------------------------------------------------------------

Installation:

1. Copy the module folder to your server.
2. Enable the module via the modules page.

-------------------------------------------------------------------

Simple 4-step usage:

1. Go to user permissions (/admin/user/permissions) and set your permissions.
2. Navigate to Site Configuration > Input formats (/admin/settings/filters)
3. There you will find 2 tabs where you can change your settings.
    Defaults (/admin/settings/filters/defauts)
    Settings (/admin/settings/filters/settings)
4. If you enable the "Control formats per node type" option. Go to your content
   type admin page to set those settings (example /admin/content/node-type/page).
   The settings are under the Input format settings fieldset.

-------------------------------------------------------------------

Important:

When setting default formats ensure that you arranged the roles correctly
placing roles in their order of precedence. This is used to determine what
default a user will get when they have more than 1 role.

NOTE:
All logged in users are automatically assigned the authenticated user role
so this role must be below all other roles that you want to set a default for or
they will get the authenticated user role default instead.

Example:
Let's say you have the 2 roles that come with Drupal and have added an
'admin' role. You would most likely want to arrange the roles in this order:

  admin
  authenticated user
  anonymous user

-------------------------------------------------------------------

Extended usage and notes:

* The default format will only be set on NEW nodes and comments. The format
  selected when the form is submitted is used for future editing purposes.

* The module is designed to always fall back to default settings when needed.
  This means that when you enable the module before you change any settings,
  it will use your current Drupal settings. Also when you enable conrol per node
  type it will use your global settings until you save the content type with new
  settings.

* The permissions "collapse format fieldset by default" and
  "collapsible format selection" will only work if "Show format selection" is
  also given. This is because those 2 perms only have an effect when there is
  a format selection.

* The permission "collapse format fieldset by default" will only work if
  "collapsible format selection" is also given. This is because the
  fieldset can only be collapsed by default if it is collapsible.

* If you dis-allow a format that is already being used by content, the module
  will do its best to set the correct format. The precidence of the formats are:
  1. Existing format selected when last saved
  2. Content type default format
  3. Global default format
  4. First allowed format
  5. Drupal core site default format

* User 1 is treated the same as all other users when it comes to a default
  format. If user 1 has not been assigned any roles then it will be assigned
  the authenticated user role's default format. If you want user 1 to have the
  default of another role assign that role to user 1.

* Ensure you read the important notes in the previous section marked important.
  It explains how you must order your roles to effectively get your defaults.
The link_node module allows users to link to another node from
the body of another node.  

The syntax of these links ("[node:NNNN]") is incompatible with the attached_node module.

INSTALLATION

1. Unpack the link_node distribution into the modules directory.

2. Enable the link_node module in the administer --> modules page 
of the admin section.

3. Once enabled, there will be new option within the "input formats" area of the
"administer" area of Drupal.  To get to it, go "input formats" (admin/filters), and
then click on the first "Configure" link, under "permissions and settings".  This is
the configure link for "filtered HTML". 

Within this page (admin/filters/1), be sure that the box for "Link Node Filter" 
is checked off.  Then click the "Save configuration" button.

Alternatively, you can pick whichever filter you want (not just "Filtered HTML") to
add the functionality to.


WHAT IT DOES

Once you have enabled the attached node filter as described above, you (or any user
who can post) can add an embedded reference to any page using the syntax:

[node:##]

To do this, the page/node must be using "Filtered HTML" as its input format.  That
can be set as the default, or it can be turned on a node by node basis.



ADVANCED CONFIGURATION/USAGE

If you want your users to be able to configure how the nodes are rendered, you
can click on the "configure filters" tab of the same "Filtered HTML" filter.
Here, in the "Attached Nodes codes" section, you can specify node properties 
that users are allowed to override. A common thing to override is the "title"
property.

Click on the "rearrange filters" tab to set the order in which filters are
applied.  Since the Attached Node filter outputs HTML with line breaks and other
things, you'll probably want this filter to be the last one applied to the output.
If, for instance, the HTML filter is run after the Attached Node filter, then
much of the output could be rearranged or removed.  Just give it a large (heavy)
weight.  The default is 10, which should send it to the bottom of the 
list (where it belongs).


ADVANCED USAGE

The tag format is fairly simple.  The most basic tag would be in the following form:

      [node:<node id>]

Parameters follow the <node id> part and are comma separated name="value" pairs:

      [node:123]
      [node:123,title="Original version of the picture"]

Note that the values must be encased in double quotes.  This is to allow users
to include commas in the value.  The side effect is that double quotes cannot
be used (currently) without causing problems. 

Closing square brackets are not allowed inside the tag.

Thanks to:
Mark Howell for attached_node, on which we are based
Chris Searle for the initial Drupal 6 port

Questions/comments/etc:
Leave them where you found this module
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Autocomplete Widgets for CCK Text and Number fields
;; $Id: README.txt,v 1.1.2.2 2009/08/16 13:11:41 markuspetrux Exp $
;;
;; Module Author: markus_petrux (http://drupal.org/user/39593)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

OVERVIEW
========

This module adds 2 autocomplete widgets for CCK fields.

- Autocomplete for allowed values list: This widget can be used for Text and
  Number fields and it takes candidate values from the defined list of Allowed
  values of the fields.

- Autocomplete for existing field data: This widget can be used for Text only
  and it takes candidate values from existing values in the database for that
  field.

Both widgets allow you to choose the size of the text element and the method
used to match values between 'Starts with' and 'Contains'.

When the Internationalization module [1] is enabled, the 'Autocomplete for
existing field data' widget also provides an option to filter values by the
language assigned to their corresponding nodes. This option allows you to
provide a different set of allowed values per language.

[1] http://drupal.org/project/i18n


REQUIREMENTS
============

- CCK (http://drupal.org/project/cck)
- CCK Text and/or Number modules provided by CCK itself.


INSTALLATION
============

- Copy all contents of this package to your modules directory preserving
  subdirectory structure.

- Goto Administer > Site building > Modules to install this module.

- Create or edit content types and start using the widgets for your Text and/or
  Number fields. :)
// $Id: README.txt,v 1.2 2009/05/13 22:48:29 quicksketch Exp $

This filter makes it easy to resize images, especially when combined with a
WYSIWYG editor such as tinyMCE or FCKeditor. Users never have to worry about
scaling image sizes again, just insert an image and set it's height and width
properties in HTML and the image is resized on output.

Author: Nathan Haug (quicksketch)

This module Built By Robots: http://www.lullabot.com.

Dependencies
------------
 * Drupal 5 or 6

Install
-------
1) Place the entire image_resize_filter directory in sites/all/modules. Then
   enable the module in Drupal.

2) Visit the Adminsiter->Site configuration->Input formats
   (admin/settings/filters). Click "configure" next to the input format you want
   to enable the image resize filter on.

3) Check the box for "Image resize filter" under the list of filters and save
   the configuration.

4) IMPORTANT: Click the "Rearrange" tab to check the order of the filters.

   If using the Image Resize Filter on the "Filtered HTML" input format, you
   MUST ensure A) that the <img> tag is in the list of allowed tags and B) The
   "Image resize filter" is run BEFORE the "HTML filter".

   If using the Image Resize Filter with BBCode or some other non-HTML filter,
   the "Image resize filter" must be run AFTER the BBCode filter.

5) Optional. Click "configure" next to the input format the image resize filter
   has been enabled on, then click the "Configure" tab so set additional
   configuration for the the image resize filter.

Support
-------
If you experience a problem with Image Resize Filter, file a request or issue in
the Image Resize Filter queue at
http://drupal.org/project/issues/image_resize_filter.
DO NOT POST IN THE FORUMS. Posting in the issue queues is a direct line of
communication with the module authors.

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
site's sitemap at admin/settings/xmlsitemap. Your can view your site's sitemap
at http://yoursite.com/sitemap.xml.

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
  http://drupal.org/handbook/modules/gsitemap.

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
   Site configuration >> File system >> Transliteration.


-- CONFIGURATION --

This module doesn't require special permissions.

This module can be configured from the File system configuration page
(Site configuration >> File system >> Settings).

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
$Id: README.txt,v 1.1.6.4 2009/12/02 09:50:06 davereid Exp $

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * Frequently Asked Questions (FAQ)
 * Known Issues
 * How Can You Contribute?


INTRODUCTION
------------

Current Maintainer: Dave Reid <http://drupal.org/user/53892>
Maintainer: hass <http://drupal.org/user/85918>
Maintainer: HorsePunchKid <http://drupal.org/user/95048>
Maintainer: jjeff <http://drupal.org/user/17190>
Contributer: webchick <http://drupal.org/user/24967>
Project Page: http://drupal.org/project/path_redirect

This module allows you to specify a redirect from one path to another, using
any HTTP redirect status (301 - Permanent Redirect, etc.).


INSTALLATION
------------

See http://drupal.org/getting-started/install-contrib for instructions on
how to install or update Drupal modules.

Once Path redirect is installed and enabled, you can add and configure your
site's redirections at admin/build/path-redirect.


FREQUENTLY ASKED QUESTIONS
--------------------------

There are no frequently asked questions at this time.


KNOWN ISSUES
------------

There are no known issues at this time.

To report new bug reports, feature requests, and support requests, visit
http://drupal.org/project/issues/path_redirect.


HOW CAN YOU CONTRIBUTE?
---------------------

- Help with the effort to bring path redirection functionality into core.
  http://drupal.org/node/133552

- Write a review for this module at drupalmodules.com.
  http://drupalmodules.com/module/path-redirect

- Help translate this module on launchpad.net.
  http://localize.drupal.org/translate/projects/path_redirect

- Report any bugs, feature requests, etc. in the issue tracker.
  http://drupal.org/project/issues/path_redirect
QUICK START GUIDE
-----------------
Click Site building > Views > Add
View name = "test", View type = "Node"
Click "Add display" to create a new page
Click Style: Unformatted and select "Bulk Operations", then click "Update"
In Page: Style options > Selected operations, select a few operations then click "Update default display"
In Fields, press +, then select "Node: Title", then click "Add" then "Update default display"
if you're using Views 6.x-3.x, you also need to add the "Node: Nid" field. You can set it as "Exclude from display", as VBO only needs it internally.
In Page settings, click Path: None and type "test", then click "Update"
Click "Save", then "View Page" (top-right corner)
Enjoy your first VBO!

TECHNICAL DETAILS
-----------------
The module works by exposing a new Views 2 Style plugin called "Bulk Operations".
The settings for this plugin allow to choose the operations that should appear on the view.
Operations are gathered from two sources: 1) Action API 2) hook_node_operations and hook_user_operations.
The module also allows to use Batch API or the Job queue module to process the selected nodes, in order to avoid timeouts.

VBO can support all object types supported by Views. Natively, VBO comes with support for nodes, users and comments.
Through the new VBO-defined hook_views_bulk_operations_object_info(), other modules can help VBO handle arbitrary object types.
Refer to function views_bulk_operations_views_bulk_operations_object_info() for information.

EXAMPLE VBO
-----------
As an example, the module comes with a re-implementation of the Content admin page.
To access it, just go to the URL admin/content/node2.
You can modify the path to admin/content/node to override the default Content admin page.

INCLUDED ACTIONS
--------------
- Modify node taxonomy terms
The module comes with a new action to manipulate nodes' taxonomy terms.
Unlike Taxonomy Node Operations, which creates a new action for each single term,
this module exposes a single configurable action that allows the user to choose which term(s) should be added to the selected nodes.
The user can also choose to keep existing terms or to erase them.

- Delete node, user, comment
Actions to delete these objects.

- Rulesets -> actions
Detect rulesets created with the Rules module and expose them as actions that VBO can invoke.

- Arbitrary PHP script
Write PHP code that is applied to each node in VBO.
This action requires the 'administer site configuration' permission - even if actions_permissions.module says otherwise.

- Modify node fields
Bulk-modify CCK and other node fields.

- Modify profile fields
Bulk-modify user profile fields.

- Modify user roles
Assign and unassign roles to users.

- Managing blocks
The Views Block module (part of Views Hacks) exposes block data to Views, allowing VBO to manage blocks just as nodes or users. Try it out!

FAQ
---
- Even though the action gets called on my selected nodes, these nodes still retain their old values! What's going on?
Actions in D6 use a flag called 'changes_node_property' to give a hint to Drupal whether this action modifies node contents
or performs a read-only operation on the node. VBO uses that flag to determine whether node_save() should be called or not after executing the action.
Actions that modify node contents but don't expose this flag in hook_action_info() will not be properly handled by VBO!
Checkout node.module's node_action_info() implementation for an example.

- How can I write an action that performs a function on all selected nodes AT ONCE?
You need to write a node operation instead of an action. Whereas actions get called *once for every selected node*, node operations are called once only,
and they are passed an array of selected nodes. Check out sirkitree's article for the same concept applied to user operations.
Note: If you use Batch API to execute your actions, VBO will revert to calling the action once per node instead.
This is because it doesn't make sense to batch one single action.

- I need VBO to modify thousands of nodes at once! Help!
VBO is designed to handle large numbers of nodes, without causing memory errors or timeouts.
When you select thousands of nodes, you can choose to execute the operations using Batch API, which provides visual feedback on VBO's progress.
To select Batch API, edit your view, open the "Bulk Operation" style settings and in the section "To execute operations:", select "Use Batch API".
You can also choose to execute the operations during cron runs via the Job queue module if you have it enabled.

- How can I use VBO to copy values from one field to another?
You will need to write simple PHP code.

Install Devel, and open the "Dev load" tab on a node of the type you want to manipulate.
Write down the name of the source field, as well as the array key that contains the field value. E.g.
'field_contact' => array(
  0 => array('value' => 'Some value'),
);
Use the stock VBO at /admin/content/node2 and filter the nodes by the desired type. Then choose the action "Modify node fields" and press "Execute".
On the "Set parameters for 'Modify node fields'" page, locate the destination field and check it ON.
In the "Code" area of that field, write the script needed to copy the value from the source field.
The help text below the code area shows you the expected format, and you can access the node being manipulated using the variable $node. E.g.
return array(
  0 => array('value' => $node->field_contact[0]['value']),
);
Press "Next" then "Confirm"

- How can I make sure that unauthorized users are prevented from destroying nodes or any other parts of my Drupal installation?
VBO gives a lot of power to admins, so it's important that security measures be enforced. There are currently 3 different ways to restrict access to VBO:

1) Using the bundled actions_permissions module, the admin can set permissions on each individual action.
   VBO honors those permissions by hiding the unauthorized actions *and* checking permissions again when it is about to execute an action.
2) VBO also calls node_access on each node that is about to be acted upon. Nodes for which the user does not have appropriate permissions
   are discarded from the execution list. The action flag changes_node_property is mapped to node_access('update').
   There are other mappings as well described in the VBO development guide.
3) The author of actions can specify additional permissions in hook_action_info under the attribute 'permissions' => array(perm1, perm2, ...).

- What is the difference between these pairs of actions:
  -- Make post sticky (node_make_sticky_action) vs Make sticky (node_mass_update:c4d...794)
  -- Promote post to front page (node_promote_action) vs Promote to front page (node_mass_update:14de7d028b4bffdf2b4a266562ca18ac)
  -- Publish (node_mass_update:9c5...047) vs Publish post (node_publish_action)
  -- Unpublish (node_mass_update:0cc...080) vs Unpublish post (node_unpublish_action)
These pairs are functionally equivalent. Technically, they differ in that the node_mass_update function is a core node operation used in
the original content administration screen, whereas the node_xxx_action functions are core actions.
As a site administrator, feel free to choose either for your VBO content administration screen.

- How can I edit fields created for the Content Profile module?
Create a Node view and filter by the content types that are attached to Content Profile. Then use the "Modify node fields" action to edit those fields.

KNOWN ISSUES
------------
- "Access denied" when selecting all (or many) rows
This occurs because too much data is sent to the database server. For MySQL, increase max_allowed_packet (e.g. to 32M). See also: https://drupal.org/node/845618.
// $Id: README.txt,v 1.2 2009/12/08 01:09:49 aaron Exp $

Readme for Media: Archive

The Media: Archive project allows the embedded media field user to embed video
and audio hosted on Archive.org. Embedded Media Field module
(http://drupal.org/project/emfield) is a pre-requisite for this module.  To use
this module install both this module and Embedded Media Field. You'll also need
to install either Embedded Video Field and/or Embedded Audio Field as
appropriate (both are packaged with Embedded Media Field). Enable emfield, and
either emvideo or emaudio - then enable "Media: Archive".

After that, editors will be able to paste a URL or the embed code for an
Archive.org video or audio posting into the field, and it will be displayed
automatically. Additionally, that URL will be parsed automatically, so the
module will know the difference between an Archive.org posting and one from
another video or audio provider.

By default, for audio, this module uses the default embed code as used on the
Archive.org site which is currently a version of Flowplayer.  Users wishing to
use a different flash player have a number of choices both free/open source and
others.  Two free options are the Wordpress audio player (hey, it's open
source), and 1pixelout which I believe is currently public domain.  These
players would have to be downloaded separately.  You would also need to
override the theme function supplied by this module to change the default
output.  I will document this in this readme file or in the documentation at
Drupal.org soon.

Note: archive.org supports having multiple tracks associated with one item.  I
will be adding support for that shortly.  Right now it will just pick out the
first track it finds in the code you supply.
// $Id: README.txt,v 1.1 2009/05/02 07:38:56 deciphered Exp $

The ImageField Tokens module extends the default functionality of ImageField
module by adding the ability to use node tokens in the ALT and Title text.

ImageField Tokens was written and is maintained by Stuart Clark (deciphered).
- http://stuar.tc/lark


Features
--------------------------

* Configurable ALT and Title text now use node tokens instead of user tokens.
* Support for Imagefield Crop
* Support for Image FUpload.


Required Modules
--------------------------

* FileField Paths - http://drupal.org/project/filefield_paths
* ImageField      - http://drupal.org/project/imagefield


Frequently Asked Questions
--------------------------

Q. Aren't tokens already supported in the ImageField module?

A. Only User tokens are supported in the ImageField module.

   Node tokens allow you to use the Node ID, Node Title, Node creation date and
   much more in your ALT/Title text where User tokens are very limited.


Q. Is there going to be a Drupal 5 version?

A. Yes, I have already completed a Development build for Drupal 5, however it is
   dependent on a patch for ImageField 5.x-2.x-dev.

   The sooner it is reviewed/tested and committed the sooner the Drupal 5
   version of ImageField Tokens will be released, so if you have the know how,
   head over to the issue: http://drupal.org/node/406874
------------------The Computed Field Drupal Module----------------------------

Computed Field is a cck module which lets you add a computed field to custom
content types. You can choose whether to store your computed field in the
database. You can also choose whether to display the field, and how to format
it. The value of the field is set using php code, so it can draw on anything
available to drupal, including other fields, the current user, database
tables, etc. The drawback of this is of course that you need to know some php
to use it.

Computed Field requires the content module (cck).

-------------------------Update-------------------------------

As of 2006-8-11 the 'display format' setting has changed. You'll need to
update any existing computed fields: If your display format was 'This is the
value: %value', then change it to '$display = "This is the value: " .
$node_field_item['value'];'


-------------------------Usage--------------------------------

----------Getting Started-----------------------------------

Before you can use Computed Field, you'll need to get CCK and enable (at the
very least) the 'content' module. You will probably also want to enable the
other cck modules, such as 'text', 'number', 'date', etc.

To add a computed field to a content type, go to administer > content >
content types, select the content type you want to add to, and click on the
'add field' tab. One of the field types available should be 'Computed', and it
should have one bullet point under it, also labelled 'Computed'. If you select
this, give your field a name, and submit the form, you will get to the
configuration page for your new computed field.


--------Configuration---------------------------------------

A Computed Field can be configured with the usual cck field options, as well
as the following extra options:

Computed Code -- This is the code that will assign a value to your computed
field. It should be valid php without the <?php ?> tags.

Display Format -- This is also php code which should assign a string to the
$display variable. It has '$node_field_item['value']' available, which is the
value of the computed field. It also has '$field' available, and you can call
any drupal functions you want to display your field.

Store using the database settings below -- If this is checked then the field
is computed on node save and stored. If it isn't stored then it will be
recomputed every time you view a node containing this field.

Database Storage Settings
	Data Type -- This is the sql data type to use to store the field. Let us
	know if you need any other storage types, or if you would like an 'other'
	option :).

	Data Length (varchar/text) -- The length of the field in the database. For 
	storing usernames or other short text with a varchar field, 32 may be 
	appropriate. Only valid for varchar or text fields.
	
	Data Size (int/float) -- The size of the field stored in the database.
	Only valid for int or float fields.
	
	Data Precision (decimal) -- The total number of digits to store in the 
	database, including those to the right of the decimal. Only valid for 
	decimal fields. 
	
	Data Scale (decimal) -- The number of digits to the right of the decimal.
	Only valid for decimal fields. 

	Default Value -- Leave this blank if you don't want the database to store
	a default value if your computed field's value isn't set.

	Not NULL -- Leave unchecked if you want to allow NULL values in the
	database field.

	Sortable  -- Used in Views to allow sorting a column of this field.


--------Examples------------------------------------------

Here are some usage examples to get you started with Computed
Field. 

-----Make a node link to itself-----------------

This example isn't very useful, but it demonstrates how to get
hold of the nid.

In your computed field's configuration:

- Computed Code:
// store the nid in our computed field
$node_field[0]['value'] = $node->nid;

- Check 'Display this field'

- Display Format:
$display = l('A link to this node', 'node/'.$node_field_item['value']);

- Uncheck 'Store using the database settings below'. You could store this if
  you wanted to, but it's not costly to compute this field and is already
  stored in the node table. One reason why you may want to store it is if you
  want the value available to Views.

When you display a node of the content type containing this field it should
now have a link to itself.

-----Adding two other fields----------------------
Imagine you have two existing number fields, called field_product_price and
field_postage_price. You want to create a computed field field_total_cost
which adds these two fields. Create a new computed field with the name 'Total
Cost', and in your computed field's configuration set the following:

- Computed Code:
$node_field[0]['value'] =
$node->field_product_price[0]['value'] +
$node->field_postage_price[0]['value'];

- Check 'Display this field'

- Display Format:
$display = '$' . $node_field_item['value'];

- Check 'Store using the database settings below'

- Data Type: decimal

- Decimal Precision: 10

- Decimal Scale: 2

- Default Value: 0.00

- Check 'Not NULL'

- Check 'Sortable'


-----Calculating a Duration given a start and end time-----

This example uses KarenS' date module (http://drupal.org/project/date) to
create two date fields field_start_time and field_end_time which record hours
and minutes. We then create a new computed field to work out the duration as a
decimal number of hours (so 1.5 is 1hour, 30minutes).

Computed field settings:

- Computed Code:
$start = $node->field_start_time[0]['value'];
$end = $node->field_end_time[0]['value'];
$start_decimal = $start['hours'] + ($start['minutes'] / 60);
$end_decimal = $end['hours'] + ($end['minutes'] / 60);
$node_field[0]['value'] = $end_decimal - $start_decimal;

- Check 'Display this field'</li>

- Display Format:</b><code>
$display = $node_field_item['value'] . " hours";

- Check 'Store using the database settings below

- Data Type:</b> float

- Data Size:</b> normal

- Check 'Sortable'

Now if you set the start time field to 9am and the end time to 11:30am, your
computed field will store the value '2.5' and display '2.5 hours'.


-----Send more examples!---------------------------------

If you have another useful (or instructive) example send it to me
(http://drupal.org/user/59132/contact) and I'll add it here for the benefit of
humankind.

-----------------------About Computed Field-----------------------------------
Computed Field was created by Agileware (http://www.agileware.net).

Quote.module
------------

This module adds a 'quote' link below nodes and comments. When clicked, the 
contents of the node or comment are placed into a new comment enclosed with 
special markup that indicates it is quoted material. 

This module also features a filter which translates the special markup into html
code.

When output by Drupal, the quote will be displayed with special formatting to 
indicate the material has been quoted.


Installation
------------

The "quote.module" and "quote.css" files should be uploaded to "modules/quote/".

Quote.module must be enabled via the 'administer/modules' interface. 


Filter
------

The Quote filter should be activated for each input format that you want to have
it available (input filters are edited via the 'administer/filters' interface).

For best effect, the Quote filter must be applied *after* any filters that 
replace HTML, and *before* the Linebreak filter. Or conversely, if
HTML filters consider <div> tags to be valid, the quote filter can be placed
before them. Filters can be rearranged by using the weight selectors within the
'rearrange filters' tab.

Additionally, the Quote filter must be applied *before* the BBCode filter if you
have the optional bbcode.module installed.

As the quote filter accesses the node (being quoted) directly, any content 
within will be displayed without any processing. For example, if a user is 
quoting a page node containing PHP (which by default is evaluated by the PHP 
filter) or any other sensitive code, it is quoted as is without the PHP (or any
other) filter being applied. While the PHP code is never evaluated in a comment,
it is nevertheless possible that sensitive server side information is made 
available to the public. To avoid this situation, quote links can be 
enabled/disabled for the parent node via the settings page. This does not affect
comment quote links.

Settings
--------

The Quote module can be configured further through its settings page at
admin/quote. This page allows the filter to be associated with specific node 
types, control if the quote link is displayed for nodes (as opposed to comments)
and so on.

Format
------

Quoted content can be placed between [quote] tags in order to be displayed as a
quote:

[quote]This is a simple quote.[/quote]

There is an optional attribute which allows quotes to cite the author:

[quote=author's name]This is a quote with an attribution line.[/quote]


Theme
-----

There are two css rules located in "quote.css" which can be altered to change
the display of the quotes.

'quote-msg' controls the display of the quote content.
'quote-author' controls the display of the attribution line.

The default "quote.css" rules are designed for Drupal's default Bluemarine 
theme. By default, quoted content is placed into an indented box, which has a 
light gray background.

Alternatively, the rules from "quote.css" can be copied into your theme's
"style.css" files. If you do this, remember to remove "quote.css" from the
"modules/quote/" folder.


Project navigation
------------------

Quote module settings page: admin -> quote.
Filter management: admin -> input formats

Project URL: http://drupal.org/project/quote
// $Id: README.txt,v 1.6.2.5 2008/02/06 15:42:36 morbus Exp $

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * IRC API Hooks
 * Design Decisions


INTRODUCTION
------------

Current Maintainer: Morbus Iff <morbus@disobey.com>

Druplicon is an IRC bot that has been servicing #drupal, #drupal-support,
and many other IRC channels since 2005, proving itself an invaluable resource.
Originally a Perl Bot::BasicBot::Pluggable application coded by Morbus Iff,
he always wanted to make the official #drupal bot an actual Drupal module.

This is the fruit of these labors. Whilst the needs of Druplicon are driving
the future and design of the module, this is intended as a generic framework
for IRC bots within Drupal, and usage outside of Druplicon is encouraged.


INSTALLATION
------------

The bot.module is not like other Drupal modules and requires a bit more
effort than normal to get going. Unlike a regular Drupal page load, an
IRC bot has to run forever and, for reasons best explained elsewhere, this
entails running the bot through a shell, NOT through web browser access.

1. This module REQUIRES Net_SmartIRC, a PHP class available from PEAR.
   In most cases, you can simply run "pear install Net_SmartIRC".

2. Copy this bot/ directory to your sites/SITENAME/modules directory.

3. Enable the module(s) and then configure them at admin/settings/bot.

4. Inside the bot/ directory is a bot_start.php script which is a wrapper
   around Drupal and the IRC network libraries. To run this script, you'll
   need to open up a shell to that directory and use the following command:

     php bot_start.php --root /path/to/drupal/root --url http://www.example.com

   --root refers to the full path to your Drupal installation directory
   and allows you to execute bot_start.php without moving it to the root
   directory. --url is required (and is equivalent to Drupal's base URL)
   to trick Drupal into thinking that it is being run as through a web
   browser. It sets HTTP_HOST and PHP_SELF, as required by Drupal.

5. Your bot is now started and is trying to connect.

6. Once your bot is connected, you can query it for more information:

     <Morbus> YOUR_BOTNAME: help

     <YOUR_BOTNAME>: Detailed information is available by asking for
       "help <feature>" where <feature> is one of: Botagotchi, Drupal URLs,
       Factoids, Seen.

     <Morbus> YOUR_BOTNAME: help Seen

     <YOUR_BOTNAME> If someone asks "seen Morbus", the bot will report the
       last time they've been seen, where, and what their last known message
       was. Directly addressing the bot will also allow the more complex
       syntax of "seen Morbus? seen d8uv?", "have you seen sbp?" and similar
       forms. * can be used as a wildcard, but only with a minimum of three
       other characters. A maximum of three results are displayed for any
       one request.

   You can also go to http://www.SITENAME.com/bot/ for a web-based version
   of all the feature help available through the IRC syntax above.


IRC API HOOKS
-------------

The following message types are supported by Net_SmartIRC:

  UNKNOWN     CHANNEL  QUERY     CTCP         NOTICE        WHO
  JOIN        INVITE   ACTION    TOPICCHANGE  NICKCHANGE    KICK
  QUIT        LOGIN    INFO      LIST         NAME          MOTD
  MODECHANGE  PART     ERROR     BANLIST      TOPIC         NONRELEVANT
  WHOIS       WHOWAS   USERMODE  CHANNELMODE  CTCP_REQUEST  CTCP_REPLY

A module may create a function in the form of:

  MODULENAME_irc_msg_MESSAGETYPE

such that a module named "bot_example" could respond or act upon all channel
messages with a function called bot_example_irc_msg_channel(). Passed to
this function is $data, an object reference that contains the message, who
said it, in what channel, and more.

Modules can respond to the user or channel with bot_message($to, $message),
where $to is either a channel name ("#drupal") or user ("Morbus Iff"). Other
IRC actions are demonstrated in the modules shipped with this package. In a
worse case scenario (ie., there's no helper function in bot.module that will
accomplish your desired tasks), you can use "global $irc;" to get the actual
Net_SmartIRC object that represents the IRC connection. Under the most ideal
conditions, you'd contribute back a patch to bot.module that'd let you
accomplish your needs without using the $irc global. Generally speaking,
try not to use the $irc global.

There is another hook available called irc_bot_reply_message (such that, in
our above example, it'd be bot_example_irc_bot_reply_message()). This function
allows you to act whenever the bot sends a message. Primarily, this was added
to allow us to log bot responses in bot_log.module. If you use this, be sure
NOT to use bot_message() within your implementation, else you'll cause an
infinite loop. Another hook, irc_bot_reply_action, does the same for actions.

The final hook of interest is irc_bot_cron, which is run every five minutes.
This is very similar to Drupal's own hook_cron, but is intended only for
bot-related operations (though, naturally, any hook_cron you add to your
own bot plugins will function as expected).

In addition to the actual utility of your module, you also should add a
few lines describing how to use your module. This is done via Drupal's
hook_help(), and the use of two special strings:

 irc:features
   Returns an array of feature names your modules provides.

 irc:features#FEATURE_NAME
   Returns an explanation of a specific feature of your module.

FEATURE_NAME will be lowercased, trimmed of whitespace, and anything not a
letter or number will be turned into an underscore. For an example in code,
take a look at the shipped bot_project.module. This information is provided
by the bot under the following conditions:

  <Morbus> bot_module: help

  <bot_module> Detailed information is available by asking for
    "help <feature>" where <feature> is one of:
    Project URLs, dns, karma.

  <Morbus> bot_module: help Project URLs

  <bot_module> Displays the title of project URLs ...


DESIGN DECISIONS
----------------

 * We do not enforce command prefixes such as !.

 * We do not enforce direct addressing like "botname: <command>".

Since the entire raw IRC message is passed off to each module, you are more
than welcome to enforce either of the above in your own code. Note that you
WILL have to insure that "botname: <command>" and simply "<command>" both do
as you'd expect - we do not remove "botname:" from the start of messages (and
thus a simple test of "^command$" will fail if the bot is addressed). Most
of our shipped modules cater to these two possibilities.

This is an IRC bot... in PHP. PHP is not especially awesome with regards to
memory management, and it certainly wasn't intended to run a script for any
respectable period of time (like, say, longer than the default 30 seconds).
Likewise, there's no way to uninclude a file, so any change to the loaded
modules (either codewise or enabled/disabled) will require the bot to be
restarted entirely.

Love the limitations, and craziness, of this project.
;$Id: README.txt,v 1.1 2008/11/26 03:03:23 augustin Exp $
README.txt for outline module.


==============================
== Your support is welcome  ==
==============================

The module outline is charity-ware.
--------------------------------------

Please contribute back by supporting the charity work of the following web sites. 
None of the web sites listed here are for profit, and none of them carry advertising.
They are all web sites dedicated to creating a better tomorrow for the whole society.

 * http://activistsolutions.org/ Activist Solutions: harvesting grassroots power.
 * htpp://www.reuniting.info/ Reuniting: healing with sexual relationships.
 * http://overshoot.tv/ Overshoot TV: making high quality videos and documentaries promoting environmental and economical sustainability.
 * http://minguo.info/ Minguo.info: promotting better voting systems, and an experiment in direct democracy.
 * http://www.wechange.org/ We Change: because we live in a world of solutions...


You can support those web sites in the following ways:

 * Blog about them.
 * Put links in a block in a sidebar.
 * Put links in any other logical place in your web site, where your visitors will find the information useful.
 * Register and participate if they match your own interest!
 * We also appreciate if, on behalf of this maintainer, you help any charity of your choice, or/and make a donation to them.

Please let the maintainer know about the options you chose. 

Thank you for your support and cooperation.




==================
== Permissions  ==
==================

______________________________________
1) Permissions defined by book.module:
______________________________________

add content to books
--------------------
The users see the link "Add child page" below a node, allowing them to create a new node which will automatically be added to the book outline.



administer book outlines
------------------------
The users see the link "Add child page" below a node, allowing them to create a new node which will automatically be added to the book outline.
They see the "Outline tab" in a node.
They can add any node into any outline, even nodes that are not regularly allowed in book outlines.


create new books 
----------------
The users can create new books, e.g. new top level nodes acting as book covers of new outlines.


access printer-friendly version
-------------------------------
The users see the link "Show a printer-friendly version of this book page and its sub-pages." below a node.


_________________________________________
2) Permissions defined by outline.module:
_________________________________________

The following book.module permissions are not modified in any way by outline.module:
  - administer book outlines.
  - create new books
  - access printer-friendly version 

By default, outline.module does not modify the permission 'add content to books' set by book.module. 
If you have been using book.module for a while, when you enable outline.module for the first time, none of the current permissions will be affected.
Only when you edit the permissions for a specific book, will the outline.module affect the default permissions.

With outline module, you can edit the 'add content to books'  permissions or a per-book basis.
You can set which roles can add content to which books.
You can also set which individual users can add content to which books.
Thus users who didn't have the 'add content to books' can add content to specific books.
Inversely, users who had that permission, can be denied adding content to specific books.



Note, the link "Create child page" at the bottom of an outlined node will show up if the two following conditions are met:
- the user must be allowed to add content to the current book.
- the user is allowed to create content of the default type set for that book.




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Views Fluid Grid
;;
;; Original author: markus_petrux (http://drupal.org/user/39593)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTENTS OF THIS FILE
=====================
* OVERVIEW
* VIEWS INTEGRATION
* REQUIREMENTS
* INSTALLATION
* CUSTOMIZATION
  * TEMPLATES
  * STYLESHEETS
  * ADVANCED


OVERVIEW
========

This module provides the Fluid Grid style plugin for Views. This plugin displays
the view as a fluid grid using an HTML list element.

The plugin settings form provides options to define the width and height of the
elements in the grid. But it also provides advanced layout options implemented
in separate CSS classes that allow you to define item margins, alignment and a
couple of CSS3 properties (box-shadow and border-radius).


VIEWS INTEGRATION
=================

A fluid grid style plugin could be included in Views in the future. For further
information, please see the following issue in the Views queue:

http://drupal.org/node/377574


REQUIREMENTS
============

- Views.
  http://drupal.org/project/views


INSTALLATION
============

- Be sure to install all dependent modules.

- Copy all contents of this package to your modules directory preserving
  subdirectory structure.

- Go to Administer -> Site building -> Modules to install module.

- You can now start using the Fluid grid style plugin in your views.


CUSTOMIZATION - TEMPLATES
=========================

Please, see the "Theme: Information" option in Views UI. Information about
the template used by this style plugin is available under the "Style output"
entry.

The template shipped with the module is views-fluid-grid-plugin-style.tpl.php
located under the theme subdirectory of the package.


CUSTOMIZATION - STYLESHEETS
===========================

The following stylesheets are provided:

- views_fluid_grid.base.css

  It contains the base CSS classes to style the fluid grid.

- views_fluid_grid.size.css

  It contains additional CSS classes that are used to define the width and
  height of the items in the grid. These sizes are defined for each option
  in the settings form of the style plugin. If you need to add more sizes to
  the list, please see ADVANCED section below.

- views_fluid_grid.advanced.css

  If contains additional CSS classes to implement the advanced layout options
  available from the settings form of the style plugin. This file is loaded
  only if any of these advanced options are really used.


CUSTOMIZATION - ADVANCED
========================

You may want to use a different set of values for a few style plugin options.
To do so, you need to add the proper entries to your settings.php file.

@code
// Custom options for Views Fluid Grid style plugin.
$conf['views_fluid_grid_plugin_style_widths']  = array(100, 150, 180, 200, 250, 300, 350, 400, 450, 500);
$conf['views_fluid_grid_plugin_style_heights'] = array(100, 150, 200, 250, 300, 350, 400, 450, 500);
$conf['views_fluid_grid_plugin_style_margins'] = array('0', '2px', '4px', '6px', '8px', '10px', '0.2em', '0.5em', '0.8em', '1em', '1.2em', '1.5em', '1.8em', '2em');
@endcode

You can add more items to any of these variables to suit your needs. Then, you
also need to provide the proper CSS classes. See the stylesheets shipped with
this module to find out how these values match CSS classes. See examples for
classes used for width and height in css/views_fluid_grid.size.css.

Note that dots in $conf['views_fluid_grid_plugin_style_margins'] will be
converted to dashes. See examples in css/views_fluid_grid.advanced.css.

Examples:

@code
/* This class is used for width 120. */
ul.views-fluid-grid-items-width-120 li.views-fluid-grid-item { width: 120px; }

/* This class is used for horizontal margin 0.6em. */
ul.views-fluid-grid-items-h-margin-0-6em li.views-fluid-grid-item { margin-left: 0.6em; margin-right: 0.6em; }
@endcode
// $Id: README.txt,v 1.1.4.2.2.1 2009/11/11 18:07:24 jareyero Exp $

README.txt - Drupal Module - Messaging
======================================

Drupal Messaging Framework

This is a messaging framework to allow message sending in a channel independent way
It will provide a common API for sending while allowing plugins for multiple channels

This Messaging Framework has been primarily developed to be used by the Notifications Framework.
See Drupal notifications module for an usage usage example implementing the full messaging capabilities.

Online documentation, includes end user and development handbooks: http://drupal.org/node/252582

SimpleTest:
-----------
Tests for this module will run on SimpleTest 6.x-2.8 (old version).
About this see http://drupal.org/node/584596

Features:
---------
- Provides a method agnostic API for composing and sending messages
- Handles message composition and formatting depending on sending method
- Supports multiple plug-ins for different message methods
- Supports 'push' and 'pull' message delivery

Plug-ins provided in this package:
---------------------------------
- messaging_mail: Integration with Drupal core mail API
- messaging_private: Integration with Privatemsg
- messaging_simple: Provides a simple UI for viewing pending messages for a user
- messaging_mime_mail: Mime mail integration
- messaging_phpmailer: HTML mails through PHPMailer
- messaging_debug: Debugging tools for developers
...

Note: some of the plug-ins depend on other packages and may not be available yet for Drupal 6

Developers:
-----------
- Tim Cullen
- Jeff Miccolis
- Jose A. Reyero

Development Seed, http://www.developmentseed.org/* $Id: */

IMPORTANT:
----------
This is an extended xmpp messaging module. It needs the patched xmppframework included with the module.

It is currently under heavy development, unsupported and not advised for production sites.

Included modules:
- messaging_xmpp 		Basic handling of in/out XMPP messages
- messaging_xmppchat	Post and read to/from xmpp chat

These modules may depend on other modules included in these packages:
- http://svn3.cvsdude.com/devseed/sandbox/drupal-6/messaging_incoming/
- http://svn3.cvsdude.com/devseed/sandbox/drupal-6/messaging_processor/

The xmpp messaging module provides a hook into the messaging framework so you can send xmpp headline messages
for providing information and notifications.

For any other use, please use the original XMPPFramework by Darren Ferguson, http://drupal.org/project/xmppframework
###   ABOUT   #############################################################################

messaging_phpmailer, Version 1.0

Author:
  Brian Neisler, aka, bneisler
  brian@theamoebaproject.com
  http://www.theamoebaproject.com
  http://www.mothersclick.com

Contributors:
  Ted Serbinski, aka, m3avrck
  hello@tedserbinski.com
  http://tedserbinski.com

Requirements: Drupal 5.0


###   FEATURES   #############################################################################

- uses PHPMailer <http://phpmailer.codeworxtech.com/> as the mailer
- works as an extension of the messaging module <http://drupal.org/project/messaging/>
- provides an alternate method to sending html email in Drupal
- cuts out drupal_mail so that drupal can send both html emails and plain text emails.



###   INSTALLATION   #############################################################################

1. Download and unzip the messaging_phpmailer module into your modules directory.

2. Download the PHPMailer class: http://phpmailer.codeworxtech.com/
   Unzip the PHPMailer folder into you messaging_phpmailer folder.
   Rename folder to PHPMailer

3. Goto Administer > Site Building > Modules and enable Messaging PHPMailer

4. Goto Administer > Site Configuration > Messaging
   Select the settings tab.
   Select Full HTML as the filer for Messaging PHPMailer. Save settings.


###   NOTES   #############################################################################

- This module does NOT use drupal_mail. This is done on purpose so that mail can be sent as both plain text and HTML. 
  If you wish to override drupal_mail you will have to implement drupal_mail_wrapper() yourself to call the 
  messaging_phpmailer_send() function. Also you will need to set the stmp variable.
IMAGE MODULE
-------------

Image.module is responsible for the creation & maintenance of "image
nodes" that can be used for several purposes - such as embedding in
other nodes, or used on their own to display photographs, screenshots or
diagrams. 

Author:
James Walker <james@lullabot.com>
# $Id: README.txt,v 1.5 2008/07/15 23:59:36 merlinofchaos Exp $

Welcome to Panels 2.

A little documentation should go here, but Panels 2 is a beast - you're best
off checking the online handbook on Drupal.org, or the developer/API docs,
which are available at http://doxy.samboyer.org/panels2/ 
  This module gives Drupal the ability to easily change links into popup dialog boxes.

  IMPORTANT INSTRUCTIONS
  ------------------------------------------------------------------------------------
  Ajax updating only works with themes that have selectable content areas. 
  If you are not using garland, you will need to figure out the selector for your theme, 
  and enter it into the "Content Selector" field on the admin/build/themes/settings page
  for your theme. Open the page.tpl.php file for your theme, and search for "print $content".
  The $content should be surrounded by a div with an id. Ex:
    <div id="content-content">
      <?php print $content; ?>
    </div> <!-- /content-content -->
  In this case, just enter '#content-content' into the Content Selector field.
  Unfortunately, a lot of themes do not have well defined content areas.  Just add the div yourself,
  and then complain on the issue queue for the theme.  It is important that there are no other
  print statements inside the div.

  LIMITATIONS
  ------------------------------------------------------------------------------------  
  Does not work with tinymce. Unlikely to work with other WYSIWYG's. (Is this still true?)
  Conflicts with: 
    Devel Theme Developer module.

  HOW TO USE THE POPUPS API
  ------------------------------------------------------------------------------------  
  If you just want to use the built in admin links, just enable the Popups: Admin Links
  module and you are good to go.
  If you want to add popups behavior to new links, or incorporate popups into your module,
  there are a couple of ways to do it.
  
  #1) Attach popup behavior to a link with popups_add_popups() call.
  ----------------------------------------------------------------  
  <!-- In html or theme -->
  <a href="popups/test/response" id="mylink"> 
  <a href="popups/test/response" id="mylink2"> 
  
  // In your module
  popups_add_popups(array('#mylink', '#mylink2=>array('width'=>'200px')));  
  This is the simplest method if you want to pass in per-link options.
  The first key is a jQuery selector. It should select an 'a' element (unless you 
  are using the 'href' option). See http://docs.jquery.com/Selectors to learn more 
  about jQuery selectors.
  The array is a set of Options. See below for the list of options.
  No array means just use the defualts. 
  
  #2) Add the class="popup" to an existing link.
  -------------------------------------------
  And then either be sure popups_add_popups() is called sometime for the page,
  or use the "Scan all pages for popup links" checkbox on the popups settings page. 
  
  Example on the theme level ("Scan all pages for popups links" must be checked):
    <a href="popups/test/response" class="popups">

  Example in code:
    popups_add_popups();
    $output .= l("Pop up entire local page.", 'popups/test/response', array('attributes'=>array('class' => 'popups')));
  
  Here are the classes that you can use:
  class="popups" requests an informational popup (or a form that doesn't want ajax processing).
  class="popups-form" requests a popup with a form that modifies the content of the original page.
  class="popups-form-reload" requests a popup with a form, and reloads the entire page when done.
  class="popups-form-noupdate" requests a popup with a form, and leaves the original page as-is.
  
  You can use the pseudo-attribute, "on-popups-options" to send options, if you don't mind having non-validating HTML.
  Note: this attribute gets removed from user content by the HTML filter.
  Example:
    print l("Pop with options (width=200px).", 'popups/test/response', 
             array('attributes'=>array(array('class' => 'popups', 'on-popups-options' => '{width: "200px"}'))))
  See popups_test.module for more examples.    
  
  #3) Add a custom module that implements hook_popups().
  ---------------------------------------------------------------------
  hook_popups() returns an array of popup rules, keyed by the id of a form, 
  or the url of a page (which can use the wildcard '*').
  Each rule is an array of options, keyed by a jQuery selector.  
  Leaving off the options array is equal to a link with class="popup-form".
  This is equivent to using a series of popup_add_popups() calls.
  
  Rule Format Example:
    'admin/content/taxonomy' => array( // Act only on the links on this page. 
      'div#tabs-wrapper a:eq(1)',  // No options, so use defaults.
      'table td:nth-child(2) a' => array( 
        'noUpdate' => true, // Popup will not modify original page.
      ),
    );
  
  #4) Make your module alter the default popup rules with hook_popups_alter().
  ----------------------------------------------------------------------------
  hook_popups_alter() allows you to modify how the popup rules are
  registered. This is useful to modify the default behavior of some
  already existing popup rules.

  See hook_popups_alter() in popups.api.php for an example.


  LIST OF POPUP OPITIONS
  ------------------------------------------------------------------------------------ 
  DEPRECATED OPTIONS
//   noUpdate: Does the popup NOT modify the original page (Default: FALSE).
//   reloadWhenDone: Force the entire page to reload after the popup form is submitted (Default: FALSE)
//   nonModel: Not working.
//   forceReturn: url to force a stop to work flow (Advanced. Use in conjunction with noUpdate or targetSelectors).  
//   afterSubmit: function to call when updating after successful form submission.   
   
   doneTest: how do we know when the multiform flow is done?
     null: flow is done when returned path = original path (default).
     *path*: 
     *regexp*: done when returned path matches regexp.
   updateMethod:
     none: do not update the initial page 
     ajax: targeted replacement of parts of the initial page (default).
     reload: full replacement of initial page with new page.
     callback: use onUpdate(data, options, element).
   updateSource (only used if updateMethod is not none):
     initial: use the initial page (default).
     final: use the path returned at the end of the multiform flow.
   href: Override the href in the a element, or attach an href to a non-link element.
   width: Override the width specified in the css.
   targetSelectors: Hash of jQuery selectors that define the content to be swapped out.
   titleSelectors: Array of jQuery selectors to place the new page title.
   reloadOnError: Force the entire page to reload if the popup href is unaccessable (Default: FALSE)
   noMessage: Don't show drupal_set_message messages.
   onUpdate: function to call when updating after successful form submission.   
   skipDirtyCheck: If true, this popup will not check for edits on the originating page.  
                   Often used with custom target selectors. Redundant is noUpdate is true. (Default: FALSE)
   hijackDestination: Use the destiination param to force a form submit to return to the originating page.
                      Overwrites any destination already set one the link (Default: TRUE)
   
 ImageCache is a dynamic image manipulation and cache tool. It allows you to
create a namespace that corresponds to a set of image manipulation actions. It
generates a derivative image the first time it is requested from a namespace
until the namespace or the entire imagecache is flushed.

Getting Started:

1. Upload and enable both the ImageCache and ImageCache UI modules.

2. Go to Administer -> Site Building -> ImageCache. Click on the local task tab
labeled "Add New Preset" to build a new set of image manipulation actions.

3. Enter a descriptive name of your choice (e.g. 'product_thumbnail') into the
"Preset Namespace" box and click "Create New Preset".

4. Add actions to your preset that tell ImageCache how to manipulate the
original image when it is rendered for display. Available actions include
crop, scale, desaturate (grey scale), resize, and rotate. Multiple actions
may be added to a preset.

5. Each action is configured in its own form, and the actions may be reordered
from the preset's configuration form. If you need to make any changes to the
order of actions in a preset, remember to click "Update Preset" when you're
finished.

Viewing Manipulated Images:

Your modified image can be viewed by visiting a URL in this format:

http://example.com/files/imagecache/preset-name/files/image-name.jpg

For example, if your preset is named 'product_thumbnail' and your image is
named 'green-widget.jpg', you could view your modified image at:

http://example.com/files/imagecache/product_thumbnail/files/green-widget...

NOTE: Each role that wishes to view the images generated by a
particular preset must be given permission on the admin/user/permissions
page.

ImageCache also defines a theme function that you can use in your modules and
themes to automatically display a manipulated image. For example, to use the
theme function in a .tpl.php file, add the following line where you would like
the image to appear:

<?php
print theme('imagecache', 'preset_namespace', $image_filepath, $alt, $title, $attributes);
?>

Change 'preset_namespace' to the name of your imagecache preset and make sure
that $image_filepath or some other variable contains the actual filepath to
the image you would like to display.

$alt, $title and $attributes are optional parameters that specify ALT/TITLE
text for the image element in the HTML or other attributes as specified in the
$attributes array.

Using ImageCache with Contributed Modules:

ImageCache presets can be put to use in various other modules. For example, when
using CCK with the Imagefield module, you can use the "Display fields" local
task tab to choose a preset to apply to images in that field. Similarly, you
can specify a preset when displaying images attached to nodes using Imagefield
in a View through the Views UI.

For more information, refer to http://drupal.org/node/163561.

(Images, page names, and form field names may refer to previous versions of
ImageCache, but the concepts are the same.)

DESCRIPTION
===========
This module gets around two quirks in the 6.x core Node module.
Currently the Node module:
- causes access grants to be ignored for unpublished content;
- ORs together access grants coming from multiple modules; this results
  in content being made accessible by one module when access had already
  been restricted by another, which is undesirable in most cases.

The module ensures that access grants are tested for unpublished content just
as they are for published content, so that using the Workflow module (or any
other module that uses the node_access table) you can implement workflows that
deal effectively with content moving from author via moderator to publisher 
BEFORE it is published (which is where it's needed most, once content is 
visible for all to see, it's a bit late to start a publication workflow
process!).
Using Taxonomy Access Control (or -Lite) you can restrict access to content
to user-defined "vocabularies" such as departments or regions. With Module
Grants this will work for unpublished content just as it does for published
content.
Moreover when Workflow and TAC or (TAC-Lite) are used together this module
makes sure that the combination exhibits the expected behaviour: access is
granted to content only when it is in the correct state AND of the appropriate
vocabulary "term" (such as department, country, etc.).
The module_grants module achieves this by AND-ing rather than OR-ing the grants.

Module Grants comes bundled with Module Grants Monitor (optional), which
provides users with a new menu item, "Accessible Content" that shows a list of
all content accessible to the logged-in user based on the permissions and
access grants as determined by enabled modules. This list may be filtered using
a double row of tabs residing at the top of the page, see point 3a below.

INSTALLATION AND CONFIGURATION
==============================
1. Place the "module_grants" folder in your "sites/all/modules" directory.
2. Under Administer >> Site building >> Modules, enable Module Grants and
   optionally Module Grants Monitor (recommended).
3a Visit Administer >> User management >> Permissions. Make sure that roles
   that are meant to be able to view unpublished and not yet published content
   have one of the following permissions:
   o "view revisions" (section "node module"), or
   o "view any|all <content-type> content" (section "revisioning module", if
   Revisioning installed).
   Make sure that the role of anonymous user does NOT have any of the above
   permissions.
3b There's usually no need to tick "administer nodes" for any role, which is
   good because "administer nodes" equates to almost god-like powers that you
   wouldn't normally give to normal users.
4. If required, install and enable as many modules for content access control
   as you need for your situation. Typical examples are Taxonomy Access Control
   (or use TAC Lite) and Workflow.
5. Optional, but highly recommended, especially when using Revisioning. Under
   Administer >> User management >> Permissions, section "module_grants_monitor
   module" select for each role which filtering tab they will get to use. The
   permissions, which are in alphabetical rahter than logical order, relate to
   two rows of tabs that appear on the 'Accessible content' page.
   The first row of up to 4 tabs filter content the logged-in user
     created,
     modified, 
     can edit,
     can view
   The second row of up to 3 tabs further filter content according to it being
     published,
     unpublished (includes previously published as well as not yet published)
     either ("all", that is: no additional filtering)

   NOTE 1: you must tick at least one permission box for each of the 2 rows
   NOTE 2: these tick boxes only determine whether the role in question gets
   to see the tabs, they do not in any way affect access to content. So in
   that sense you can safely tick any or all of the tab boxes for all
   authenticated users. However you may not want to confuse certain roles
   with too many tabs and too much output.

USAGE
=====
Module Grants Monitor creates a new navigation menu item, 'Accessible content'
visible to the administrator and to roles to which the administrator granted
access as per the above section, point 5. The content shown under 'Accessible
content' reflects the access grants given by modules installed on your system
to the current user.

You can use Module Grants in combination with TAC or TAC-Lite for fine-grained
access control based on vocabularies (such as "department") assigned to the
various content types. You can then create department-specific roles (eg
Sports Author, Music Author) and enforce that these roles can only access
content belonging to their departments, whether it's published or not.
Create your grants "schemes" on this page: Administer >> User management >>
Access control by taxonmy.
In addition you may want to install the Workflow module to further segragate
roles (eg author and moderator) via access control based on states such as
"in draft", "in review" and "published". See Administer >> Site building >>
Workflow.
The module makes sure that access to content is given only when BOTH the
TAC (Lite) and the Workflow Access modules grant it (as opposed to one OR
the other).

This module also works well with the Revisioning module for creating effective
publication workflows operating on published as well as unpublished content
revisions. 
See the Revisioning project page at http://drupal.org/project/revisioning
for three step-by-step tutorials.

Be aware that any permissions given in the "node module" section override the
access grants given by the Workflow and TAC-Lite modules, so you probably only
want to assign a few creation permissions in the node module and grant 
view, update and delete via TAC/TAC-Lite and/or Workflow.

Additional configuration options are found at Administer >> Site configuration
>> Module Grants.

API
===
Module Grants features one hook, hook_user_node_access($revision_op, $node),
which module developers may implement to alter or add to the behaviour of
Module Grants as it determines whether access to a supplied node or revision
should be granted using the requested operation.
See the module_grants.api.php file.

AUTHOR
======
Rik de Boer, Melbourne, Australia.
$Id: README.txt,v 1.1 2007/06/07 13:47:15 timgambell Exp $


What is Typogrify.module?
=========================

Typogrify.module brings the typographic refinements of Typogrify to Drupal.

* Wraps ampersands (the "&" character) with <span class="amp">&amp</span>.

* Prevents single words from wrapping onto their own line using Shaun Inman's Widont technique.

* Converts straight quotation marks to typographer's quotation marks, using SmartyPants.

* Converts multiple hyphens to en dashes and em dashes (according to your preferences), using SmartyPants.

* Wraps multiple capital letters with <span class="caps">CAPS</span>.

* Wraps initial quotation marks with <span class="quo"></span> or <span class="dquo"></span>.

* Adds a css style sheet that uses the <span> tags to substitute a showy ampersand in headlines, switch caps to small caps, and hang initial quotation marks.


Learn more about Typogrify
==========================

Typogrify originated as Python code by Christian Metts. Typogrify.module uses Hamish Macpherson's port, php-typogrify.

Announcement:
http://www2.jeffcroft.com/sidenotes/2007/may/29/typogrify-easily-produce-web-typography-doesnt-suc/

Example Page:
http://static.mintchaos.com/projects/typogrify/

Project Page:
http://code.google.com/p/typogrify/

Typogrify.module uses PHP Typogrify:
http://blog.hamstu.com/

Typogrify.module uses PHP SmartyPants:
http://www.michelf.com/projects/php-smartypants/

To learn more about Widont:
http://www.shauninman.com/archive/2006/08/22/widont_wordpress_plugin


Learn more about setting type for the web
=========================================

The Elements of Typographic Style Applied to the Web
http://webtypography.net/

Five simple steps to better typography
http://www.markboulton.co.uk/journal/comments/five_simple_steps_to_better_typography/

Thinking With Type
http://www.thinkingwithtype.com/

And if you're going to buy one book...
http://www.amazon.com/Elements-Typographic-Style-Robert-Bringhurst/dp/0881791326Markdown Preview provides a preview pane that displays the rendered HTML output of your Markdown input. 

Markdown Preview consists of two submodules:

Markdown Preview - Provides a preview pane for textarea form fields.

Markdown Preview for BUEditor - Provides a preview pane for BUEditor. This works best with solipsist's markdowneditor add-on for BUEditor (http://drupal.org/project/markdowneditor).
Note that the Showdown Markdown implementation that Markdown Preview uses doesn't support Markdown Extra. You may wish to disable the unsupported toolbar buttons in BUEditor.



Installation instructions
-------------------------

Markdown Preview:

1. Download and Showdown and copy showdown.js to the "showdown" directory inside the markdownpreview module directory.
2. Download and install Markdown filter module: http://drupal.org/project/markdown
3. Enable the module and change the settings as needed: admin/settings/markdownpreview

Markdown Preview for BUEditor:
1. Download and Showdown and copy showdown.js to the "showdown" directory inside the markdownpreview module directory.
2. Download, install and configure the required modules:
   - Markdown filter module: http://drupal.org/project/markdown
   - BUEditor: http://drupal.org/project/bueditor
   - Markdown Editor: http://drupal.org/project/markdowneditor
3. Enable the module and change the settings as needed: admin/settings/markdownpreview_bueditor


Requirements
------------
Showdown - a JavaScript Markdown implementation by John Fraser. Link: http://attacklab.net/showdown/
Markdown - Link: http://drupal.org/markdown

$Id: README.txt,v 1.4.4.2 2009/11/03 04:23:10 thehunmonkgroup Exp $

****************************************************
User Protect Module -- README

written by Chad Phillips: thehunmonkgroup at yahoo dot com
****************************************************

This module provides various editing protection for users. The protections can
be specific to a user, or applied to all users in a role. The following protections
are supported:

  -- username
  -- e-mail address
  -- password
  -- status changes
  -- roles
  -- deletion
  -- OpenID identities (both adding and deleting) 
  -- all edits (any accessed via user/X/edit)

When a protection is enabled for a specified user (or the protection is enabled
because the user belongs to a role that has the protection), it prevents the
editing operation in question that anyone might try to perform on the
user -- unless an administrator who is permitted to bypass the protection is
editing the specified user. The module will protect fields by disabling them at
user/X/edit.

User administrators may be configured to bypass specified protections, on
either a global or per-administrator basis.

These protections are valid both when trying to edit the user directly from
their user/X/edit page, or using the mass user editing operations.

The module also provides protection at the paths user/X/edit and user/X/delete,
should anyone try to visit those paths directly.

Note: this module is compatible with the RoleAssign module.

SETTINGS:
At administer -> user management -> userprotect, you'll find the settings for the
module. When the module is initially enabled, the default settings are such:

  -- User administrators bypass all protections.
  -- The root user specifically bypasses all protections.
  -- The anonymous user (uid 0) and root user (uid 1) are protected from all
     edits, deletion, and OpenID operations.
  -- All role protections are disabled.
  -- The 'change own e-mail', 'change own password', and 'change own openid'
     permissions are enabled for authenticated users in the userprotect section
     at administer -> user management -> access control.

This effectively amounts to no protections. It is suggested that you turn off
as many default administrator bypass settings as possible, and set bypass
settings for specific user administrators--this allows you to take advantage
of the status, roles, deletion, openid and edit protections in a meaningful
way. Because of the per-user bypass/protection settings for the anonymous and
root user, this will also begin protecting those users, without compromising
the root user's access to the entire site.

Important note: In order to protect a user from deletion (by visiting
user/X/delete directly) and/or OpenID edits (by visiting user/X/openid
directly), you must enable the 'delete' and/or 'openid' protection specifically.
Enabling 'all account edits' does not enable these protections!

Also note that this module only provides protection against actions via the
website interface--operations that a module takes directly are not protected!
This module should play well with other contributed modules, but there is no
guarantee that all protections will remain intact if you install modules outside
of the drupal core installation.

ADDING PROTECTIONS FOR A SINGLE USER:
This is done at administer -> user management -> userprotect -> protected users.
Any time a user is added for protection, they will initially receive the default
protections enabled at 
administer -> user management -> userprotect -> protection defaults.

ADDING PROTECTIONS FOR ROLES:
This is done at administer -> user management -> userprotect -> protected roles.
Be cautious about adding protections by role, or you can lock out users from
things unintentionally!

In particular, note the if you enable role protections for a specific role, and you
have no bypasses enabled, you've effectively locked out any role editing for
that role by anybody, unless you come back to the settings page and disable
the role protection!

ADDING ADMINISTRATOR BYPASS RULES:
One of the more powerful features of the module are the administrator bypass
settings. Any user that has been granted the 'administer users' permission can
be configured to bypass any protection, either via the default administrator
bypass settings at 
administer -> user management -> userprotect -> protection defaults, or via
a per-administrator setting at 
administer -> user management -> userprotect -> administrator bypass. If a
bypass is enabled for a user administrator, they will be given editing rights on
that protection regardless if it is enabled for a single user or an entire role.

Note that the per-administrator bypass settings override the default bypass
settings.

DEFAULT PROTECTION SETTINGS:
Set the default protections for newly protected users at
administer -> user management -> userprotect -> protection defaults. In
addition, you can enable the auto-protect feature, which will automatically
add the default protections to any newly created user accounts, and set default
bypass options for all user administrators.

HOW THE MODULE DETERMINES A PROTECTION:
In order to properly use User Protect, it's important to understand how the
module determines if a specified field is to be protected. Here is the basic
logic:

  -- If the current user is a user administrator, check if they have per-administrator
     bypass settings. If so, then check to see if they are allowed to bypass the
     protection. If so, then stop the checks and allow editing of the field.

  -- If not, then if the current user is a user administrator, check if the default
     administrator bypass is enabled for the protection in question. If so, then
     stop the checks and allow editing of the field.

  -- If not, check if the user is editing their own account. If so, determine the
     protections for e-mail, password and openid by examining the userprotect
     permissions for 'change own e-mail', 'change own password' and 'change own
     openid', then continue with the rest of the checks below.

  -- If not, check if the protection is set for the individual user being edited.
     If so, then stop the checks here, and prevent editing of the field (this
     effectively means that individual protections override role protections).

  -- If not, then examine all the roles for the user being edited. If any of those
     roles have the protection enabled, then prevent editing of the field.

  -  If not, then allow the field to be edited.

Note: If a user is editing their own account, they are never protected from editing
their own username, e-mail, password or OpenID. Administrators can still limit the
ability of users to change their username via the role-based permission at
administer -> user management -> access control.
/* $Id: README.txt,v 1.1.6.6 2008/11/12 18:14:37 aaron Exp $ */

/*********************/
 Embedded Media Field
/*********************/

Author: Aaron Winborn (aaron)
Maintainers: Aaron Winborn (aaron) + Alex Urevick-Ackelsberg (Alex UA)
Development Began 2007-06-13

Requires: Drupal 5 or 6, Content (CCK)
Optional: Views, FeedAPI/FeedAPI Element Mapper (see this for instructions for importing Embedded Video Feeds: http://zivtech.com/blog/module-mashup-creating-a-feed-embedded-videos-using-emfield-feedapi-and-feedapimapper ), Media Actions, Asset, & Thickbox.

The Embedded Media Field creates a field for nodes created with CCK to accept pasted URL's or embed code from various third party media content providers, such as YouTube and Flickr. It will then parse the URL to determine the provider, and display the media appropriately.

Currently, the module ships with Embedded Video Field, Embedded Image Field, and Embedded Audio Field. In addition, it has Embedded Media Import, to import photosets and playlists into individual nodes, when allowed by specific providers. Finally, it also ships with Embedded Media Thumbnail, which allows editors to override provider-supplied thumbnails with their own custom image thumbnails.

The module also allows field & provider specific settings and overrides, such as autoplay, resized thumbnails or videos for teasers, RSS support, and YouTube's 'related videos'. You can turn off individual provider support on a field or global basis.

/***************/
 Refreshing Data
/***************/

There are some instances in which your third-party data may need to be refreshed. That should be the first step to take if you notice media not working (that used to work before). You can refresh an individual node's third-party multimedia data by editing its node and resubmitting the info. You can also do this for multiple nodes by visiting the Content Management Administration page, by browsing to Administer > Content Management > Content (at /admin/content/node). Then select the nodes you wish to refresh, checking their respective check boxes, selecting Reload Embedded Media Data from the Update options drop-down, and pressing the Update button.

If you have the Job Queue module enabled (from http://drupal.org/project/job_queue), you will be able to similarly refresh all nodes on your site, by visiting the 'Reload data' tab that will then appear on the Embedded Media Field configuration page, by browsing to Administer > Content management > Embedded Media Field configuration > Reload data (at /admin/content/emfield/reload). Then select the content type(s) you wish to refresh and press the Submit button. All nodes will then be refreshed on your next cron batch (or several crons if you have a lot of nodes on your site).

/*********/
 Providers
/*********/

Currently supported providers:

Video:

    * Blip.TV
    * Brightcove
    * Daily Motion
    * Google
    * Guba
    * JumpCut
    * imeem
    * Lastfm
    * LiveVideo
    * MetaCafe
    * MySpace
    * Revver
    * SevenLoad
    * Spike.TV
    * Tudou
    * Veoh
    * Vimeo
    * YouTube
    * Local videos (when already uploaded in the files directory)

Image:

    * Flickr
    * ImageShack
    * PhotoBucket
    * Picasa

Audio:

    * Odeo
    * Podcast Alley
    * podOmatic

You can:

    * Administer emfield's general settings at administer >> content >> emfield
    * Add embedded media fields to your content types at administer >> content >> types >> %YourType% >> add_field
    * Manage teaser and full node display settings at administer >> content >> types >> %YourType% >> fields

For the most up-to-date documentation, please see http://drupal.org/node/184346/* $Id: README.txt,v 1.1.2.1 2009/10/13 13:26:44 aaron Exp $ */

/********************/
 Embedded Wave Field
/********************/

Author: Noah Biavaschi

Requires: Drupal 6, Content (CCK), Embedded Media Field
Optional: Views

This extensible module will create a field for node content types that can be used to display waves from providers
such as google.
/* $Id: README.txt,v 1.1.4.5 2009/09/22 15:11:07 aaron Exp $ */

/**********************/
 Embedded Media Import
/**********************/

****PLEASE NOTE: EMIMPORT IS DEPRECATED IN DRUPAL 6 IN FAVOR OF FEEDAPI INTEGRATION********
// $Id: README.txt,v 1.1.2.1 2009/11/08 13:26:13 aaron Exp $

Embedded Media Thumbnail

This allows the server to store a local copy of a provider's thumbnail, for use
with ImageCache and faster retrieval of images for the browser. You can also
override a thumbnail with a custom upload by the editor.

Note that you must have the PHP variable allow_url_fopen set to ON for this
module to function, and it will not function in PHP Safe Mode.
// $Id: README.txt,v 1.1.4.3 2009/09/24 13:41:05 aaron Exp $

README for Embedded Inline Media

This module provides the ability to parse URLs of third party media providers
from a node or comment content, and display the media appropriately.

Experimental; currently only works for video.

After enabling the module, you need to go to your Input Filters administration
at /admin/settings/filters, configure the format you wish (such as Full HTML at
/admin/settings/filters/2), check the box to allow Embedded Inline Media, and
then configure the filter (such as at /admin/settings/filters/2/configure).

In the filter's configuration, you'll then check the providers you wish to
allow, and any other desired settings. Finally, when submitting a node, you'll
need to ensure the proper filter is selected, and simply paste the URL (no
brackets). Note that this will conflict with the URL filter if that is enabled,
so you'll need to rearrange the filters to ensure the Embedded Inline Media
filter is above that.
/* $Id: README.txt,v 1.1.4.5 2008/06/04 12:08:03 alexua Exp $ */

/********************/
 Embedded Audio Field
/********************/

Author: Aaron Winborn
Development Began 2008-01-06

Requires: Drupal 5, Content (CCK)
Optional: Views

This extensible module will create a field for node content types that can be used to display audio music and podcasts
from various third party video providers. When entering the content, the user will simply paste the URL or embed code
of the audio, and the module will automatically determine which content provider is being used. When displaying
the audio, the proper embedding format will be used.

The module already supports podOmatic, Odeo, and Last.FM audio formats. More are planned to be supported soon. An api allows
other third party video providers to be supported using simple include files and provided hooks. (Developers: examine the
documentation of /providers/podomatic.inc for help in adding support for new providers).

The administer of a site may decide whether to allow all content providers, or only a certain number of them. They may
further be limited when configuring the field.

On the Display Fields settings page, the administrator may further choose how to display the audio, for teasers and body.
Any necessary API calls to third party providers are cached.

Other features available are allowing a podcast to autoplay, or changing the size of the player. Those features will be set
when creating or editing the specific field. Note that not all options are supported by all providers. You can see a list
of what features are currently supported by a provider at admin/content/emfield.

Some providers may provide other features that are supported by Embedded Audio Field, such as affiliate programs or related
podcasts. You can find those settings at admin/content/emfield, in the fieldset for the specific provider.

Questions can be directed to winborn at advomatic dot com
/* $Id: README.txt,v 1.1.2.1 2008/07/18 20:22:44 alexua Exp $ */

/***********/
 Embedded Video Field
/***********/

Author: Aaron Winborn
Development Began 2007-02-23

Requires: Drupal 6, Content (CCK), emfield
Optional: Views

This extensible module will create a field for node content types that can be used to display video and thumbnails
from various third party video providers. When entering the content, the user will simply paste the URL or embed code
of the video, and the module will automatically determine which content provider is being used. When displaying
the video, the proper embedding format will be used.

The module already supports YouTube, Google, Revver, MySpace, MetaCafe, JumpCut, BrightCove, SevenLoad, iFilm and Blip.TV
video formats. More are planned to be supported soon. An api allows other third party video providers to be supported using
simple include files and provided hooks. (Developers: examine the documentation of /providers/youtube.inc for help in adding
support for new providers).

The administer of a site may decide whether to allow all content providers, or only a certain number of them. They may
further be limited when configuring the field.

On the Display Fields settings page, the administrator may further choose how to display the video, for teasers and body.
Videos may be displayed in a preview or full size, each of configurable sizes. When available by a provider, thumbnails may
also be displayed, and sized appropriately. Any necessary API calls to third party providers are cached.

Other features available are allowing a video to autoplay, or changing the size of the video. Those features will be set
when creating or editing the specific field. Note that not all options are supported by all providers. You can see a list
of what features are currently supported by a provider at admin/content/emfield.

Some providers may provide other features that are supported by Video CCK, such as affiliate programs with Revver, or related
video thumbnails with YouTube, embedded within the video. You can find those settings at admin/content/emfield, in the
fieldset for the specific provider.

Questions can be directed to winborn at advomatic dot com
/* $Id: README.txt,v 1.1.2.1 2008/07/18 20:22:44 alexua Exp $ */

/********************/
 Embedded Image Field
/********************/

Author: Aaron Winborn
Development Began 2007-06-13

Requires: Drupal 5, Content (CCK), Embedded Media Field
Optional: Views

This extensible module will create a field for node content types that can be used to display images from various third party
image providers. When entering the content, the user will simply paste the URL or embed code of the image, and the module will
automatically determine which content provider is being used. When displaying the image, the proper embedding format will be
used, calling any necessary API's.

The module already supports Flicker, Imageshack, and Photobucket image formats. More are planned to be supported soon. An api allows other
third party providers to be supported using simple include files and provided hooks. (Developers: examine the documentation of
/providers/flikr.inc for help in adding support for new providers).

The administer of a site may decide whether to allow all content providers, or only a certain number of them. They may
further be limited when configuring the field.

On the Display Fields settings page, the administrator may further choose how to display the image, for teasers and body.
Images may be displayed in a thumbnail, preview, or full size, each of configurable sizes. Unfortunately, for now, because
images are not stored locally, we don't have access to the powerful features of imagecache.

Some providers may provide other features that are supported by Image Neighborhood CCK. You can find those settings at
admin/content/emfield, in the fieldset for the specific provider.

Questions can be directed to winborn at advomatic dot com

-------------------------------------------------------------------------------
Backup and Migrate 2 for Drupal 6.x
  by Ronan Dowling, Gorton Studios - ronan (at) gortonstudios (dot) com
-------------------------------------------------------------------------------

DESCRIPTION:
This module makes the task of backing up your Drupal database and migrating data
from one Drupal install to another easier. It provides a function to backup the
entire database to file or download, and to restore from a previous backup. You
can also schedule the backup operation. Compression of backup files is also
supported.

There are options to exclude the data from certain tables (such as cache or
search index tables) to increase efficiency by ignoring data that does not need
to be backed up or migrated.

The backup files are a list of SQL statements which can be executed with a tool
such as phpMyAdmin or the command-line mysql client.

-------------------------------------------------------------------------------

INSTALLATION:
* Put the module in your drupal modules directory and enable it in 
  admin/build/modules. 
* Go to admin/user/permissions and grant permission to any roles that need to be 
  able to backup or restore the databse.
* Configure and use the module at admin/content/backup_migrate

OPTIONAL:
* Enable token.module to allow token replacement in backup file names.
* To Backup to Amazon S3:
    - Download the S3 library from http://undesigned.org.za/2007/10/22/amazon-s3-php-class
      and place the file 'S3.php' in the includes directory in this module.
      The stable version (0.4.0 – 20th Jul 2009) works best with Backup and Migrate.

LIGHTTPD USERS:
Add the following code to your lighttp.conf to secure your backup directories:
  $HTTP["url"] =~ "^/sites/default/files/backup_migrate/" {
       url.access-deny = ( "" )
  }
You may need to adjust the path to reflect the actual path to the files.

IIS 7 USERS:
Add the following code to your web.config code to secire your backup directories:
<rule name="postinst-redirect" stopProcessing="true">
   <match url="sites/default/files/backup_migrate" />
   <action type="Rewrite" url=""/>
</rule>
You may need to adjust the path to reflect the actual path to the files.

-------------------------------------------------------------------------------

VERY IMPORTANT SECURITY NOTE:
Backup files may contain sensitive data and by default, are saved to your web
server in a directory normally accessible by the public. This could lead to a
very serious security vulnerability. Backup and Migrate attempts to protect
backup files using a .htaccess file, but this is not guaranteed to work on all
environments (and is guaranteed to fail on web servers that are not apache). You
should test to see if your backup files are publicly accessible, and if in doubt
do not save backups to the server, or use the destinations feature to save to a 
folder outside of your webroot.

OTHER WARNINGS:
A failed restore can destroy your database and therefore your entire Drupal
installation. ALWAYS TEST BACKUP FILES ON A TEST ENVIRONMENT FIRST. If in doubt
do not use this module.

This module has only be tested with MySQL and does not work with anyother dbms. 
If you have experiences with Postres or any other dbms and are willing to help 
test and modify the module to work with it, please contact the developer at 
ronan (at) gortonstudios (dot) com.

Make sure your php timeout is set high enough to complete a backup or restore
operation. Larger databases require more time. Also, while the module attempts
to keep memory needs to a minimum, a backup or restore will require
significantly more memory then most Drupal operations.

If your backup file contains the 'sessions' table all other users will be logged
out after you run a restore. To avoid this, exclude the sessions table when 
creating your backups. Be aware though that you will need to recreate the 
sessions table if you use this backup on an empty database.

Do not change the file extension of backup files or the restore function will be
unable to determine the compression type the file and will not function
correctly.

IF A RESTORE FAILS:
Don't panic, the restore file should work with phpMyAdmin's import function, or
with the mysql command line tool. If it does not, then it is likely corrupt; you
may panic now. MAKE SURE THAT THIS MODULE IS NOT YOUR ONLY FORM OF BACKUP.

-------------------------------------------------------------------------------

Markdown filter Drupal module
================================================================================

Provides Markdown filter integration for Drupal input formats. The Markdown
syntax is designed to co-exist with HTML, so you can set up input formats with
both HTML and Markdown support. It is also meant to be as human-readable as
possible when left as "source".

This module is a continuation of the Markdown with Smartypants module (at
http://drupal.org/project/marksmarty), and only includes Markdown support
to simplify configuration. It is now suggested that you use Tipogrify module
(see http://drupal.org/project/typogrify) if you are interested in Smartypants
support.

Note that if you use the GeSHI filter for code syntax highlighting, arrange
this filter after that one.

For more information on Markdown, read:

 - http://daringfireball.net/projects/markdown/syntax
 - http://michelf.com/projects/php-markdown/extra/

Quickstart
--------------------------------------------------------------------------------

1. Move the entire "markdown" directory into your Drupal installation's
   sites/all/modules folder (or your site specific directory).

2. Enable the module on Administer >> Site building >> Modules

3. Set up a new input format or add Markdown support to an existing format at
   Administer >> Site configuration >> Input formats

4. For best security, ensure that the HTML filter is after the Markdown filter
   on the "Reorder" page of the input format and that only markup you would
   like to allow in via HTML and/or Markdown is configured to be allowed via the
   HTML filter.

Credits
--------------------------------------------------------------------------------
Markdown created                     by John Gruber: <http://daringfireball.net>  
PHP executions                       by Michel Fortin: <http://www.michelf.com/>  
Drupal filter originally             by Noah Mittman: <http://www.teradome.com/>  

ImageField provides an "Image" widget type to CCK. This module leverages the
functionality of FileField and behaves nearly identically. ImageField widgets
will give you a nice thumbnail preview of the image when uploaded, and provides
a few display options (formatters) within CCK to display the images when the
content is viewed.

ImageField was written by Darrel Opry (dopry).
Maintained by Nathan Haug (quicksketch) and Andrew Morton (drewish).

Dependencies
------------
 * FileField
 * Content

ImageField also provides additional features when used with the following:

 * Token (Generate dynamic paths when saving images.)
 * ImageCache (Create thumbnails of images on output.)

Install
-------

1) Copy the imagefield folder to the modules folder in your installation.

2) Enable the module using Administer -> Site building -> Modules
   (/admin/build/modules).

3) Create a new image field in through CCK's interface. Visit Administer ->
   Content management -> Content types (admin/content/types), then click
   Manage fields on the type you want to add an image upload field. Select
   "File" as the field type and "Image" as the widget type to create a new
   field.
// $Id: README.txt,v 1.2 2008/08/27 13:16:39 weitzman Exp $

OVERVIEW

Nodes hold content. Views save queries. Wouldn't be great if a node could hold a
saved query? Now it can. Viewfield is a CCK field module that allows
administrators to put views directly into nodes. When creating a node, users can
select from a list of views. When the node is displayed, the view is run and the
content is inserted into the body of the node.



INSTALLATION

This module requires the views.module and content.module. Enable these modules,
then enable viewfield.module. You're ready to go.

TODO

1. Provide better control over each view in multiselect fields.
2. Use exposed views to allow for more point and click control over the view at
node add time.
3. Integrate this module back into views when CCK becomes part of core.

AUTHOR

Mark Fredrickson
mark.m.fredrickson@advantagelabs.com
Description
-----------
This module adds a webform content type to your Drupal site.
A webform can be a questionnaire, contact or request form. These can be used 
by visitor to make contact or to enable a more complex survey than polls
provide. Submissions from a webform are saved in a database table and 
can optionally be mailed to e-mail addresses upon submission.

Requirements
------------
Drupal 6.16 or higher

Installation
------------
1. Copy the entire webform directory the Drupal sites/all/modules directory.

2. Login as an administrator. Enable the module in the "Administer" -> "Site
   Building" -> "Modules"

3. (Optional) Edit the settings under "Administer" -> "Site configuration" ->
   "Webform"

4. Create a webform node at node/add/webform.

Upgrading from previous versions
--------------------------------
1. Copy the entire webform directory the Drupal modules directory.

2. Login as the FIRST user or change the $access_check in update.php to FALSE

3. Run update.php (at http://www.example.com/update.php)

Support
-------
Please use the issue queue for filing bugs with this module at
http://drupal.org/project/issues/webform

// $Id: README.txt,v 1.9 2010/04/03 23:28:58 soxofaan Exp $

============================
GeSHi Filter (Drupal Module)
============================


DESCRIPTION
-----------
The GeShi Filter is a Drupal module for syntax highlighting of pieces of
source code. It implements a filter that formats and highlights the syntax of
source code between for example <code>...</code>.


DEPENDENCY
----------
This module requires the third-party library GeShi 1.0.x (Generic Syntax
Highlighter, written by Nigel McNie) which can be found at
  http://qbnz.com/highlighter
See installation procedure below for more information.


INSTALLATION
------------
1. Extract the GeSHi Filter module tarball and place the entire geshifilter
  directory into your Drupal setup (e.g. in sites/all/modules).

2. Download the GeSHi library from
  http://sourceforge.net/projects/geshi/files/geshi
  Make sure you download a version of the branch 1.0.x and not a version
  from the branch 1.1.x (also described as geshi-dev), which is not yet
  supported by the GeSHi filter module.
  Place the entire extracted 'geshi' folder (which contains geshi.php)
  in the geshifilter directory (e.g. as sites/all/modules/geshifilter/geshi),
  or better, in a libraries directory (e.g. as sites/all/libraries/geshi).

3. Enable this module as any other Drupal module by navigating to
  administer > site building > modules


CONFIGURATION
-------------
1. The general GeSHi Filter settings can be found by navigating to:
  administer > site configuration > geshifilter.
  Set the path to the GeSHi library on that page, if it is not detected
  automatically already.
2. Further configuration instructions can be found by following the
  "more help..." link at the top of that general settings page, which leads
  to www.example.com/?q=admin/help/geshifilter . This requires you have the
  'help' module enabled.


USAGE
-----
The basic usage (with the default settings) is:
  <code language="java">
  for (int i; i<10; ++i) {
    dothisdothat(i);
  }
  </code>
When language tags are enabled (like "<java>" for Java) you can also do
  <java>
  for (int i; i<10; ++i) {
    dothisdothat(i);
  }
  </java>
More options and tricks can be found in the filter tips of the input format at
www.example.com/?q=filter/tips .


AUTHORS
-------
Original module by:
  Vincent Filby <vfilby at gmail dot com>

Drupal.org hosted version for Drupal 4.7:
  Vincent Filby <vfilby at gmail dot com>
  Michael Hutchinson (http://compsoc.dur.ac.uk/~mjh/contact)
  Damien Pitard <dpdev00 at gmail dot com>

Port to Drupal 5:
  rötzi (http://drupal.org/user/73064)
  Stefaan Lippens (http://drupal.org/user/41478)
$Id: README,v 1.2 2007/12/12 16:00:37 soxofaan Exp $

README file for geshi-extra directory
-------------------------------------

This directory is meant to store custom GeSHi language definition files that
are not part of the default GeSHi library. Separating custom files from a
pristine GeSHi library eases upgrading and maintenance of the GeSHi library.

If you add/remove language definition files, you need to flush the cache
of available languages before the GeSHi filter module will pick these up.
You'll find a link for this on the "Languages" tab of the GeSHi filter
module settings.
The CVS deploy module makes Drupal work better for sites that checkout
Drupal source directly from CVS.  If you run "cvs checkout ..." to
setup the directory where your Drupal installation lives, this module
is for you.

The first improvement is that at the module administration page
(administer >> build >> modules or 'admin/build/modules'), the version
column will be filled in with human-readable strings.  If there is no
version information in the .info files, this module will look for the
sticky tag in the CVS directory for each module, and attempt to
resolve the version string based on the tag or branch you have checked
out from. If you happen to have an older checkout of a module that
used 'version = "$Name ..." in the .info file, CVS deploy will resolve
that into a human-readable version string, too.

The other major improvement is the interaction with the Update status
module included in Drupal 6.x core.  If you deploy your site from CVS,
you can still use Update status to warn you about newer versions, so
long as you have the CVS deploy module enabled.

Send feature requests and bug reports to the issue queue for the
CVS deploy module: http://drupal.org/node/add/project_issue/cvs_deploy

Written by: Derek Wright ("dww") http://drupal.org/user/46549

$Id: README.txt,v 1.2 2008/02/16 17:22:43 dww Exp $

Description
===========
Token module provides a centralized API for text substitution. Unless
you're installing another Drupal module that requires it, this software
is probably unnecessary.

For more information on tokens see http://groups.drupal.org/tokens

Benefits
========
If you're a Drupal developer, check out API.txt for detailed instructions
on using the Token API. It allows every module to announce the placeholder
tokens they can handle, uses simple caching to prevent duplicated work in
a given page-view, and is pretty lightweight. It's nice. You'll like it.

tokenSTARTER
============
Want to add your own custom tokens to a site? Not sure how to write a 
module? Worry no more, it's now quite easy.

1. Copy and rename the tokenSTARTER.info and tokenSTARTER.module replacing
   every instance of STARTER with a descriptive, appropriate word.

2. Edit the .module file and change hook_token_list and hook_token_values
   to provide whatever additional tokens or logic your site needs.

3. Enable the module and enjoy!

You should also want to read the API.txt.
DESCRIPTION
===========
This modules forces new unpublished content as well as edits to current content
to first go into a queue for review by a moderator/publisher, rather than
immediately becoming "live", i.e. visible to the public.

We took our inspiration from the Revision Moderation module by Angie Byron,
but found that a patch could not implement the deviating functionality our
customers required, which would change the current behaviour of the RM module
and surprise existing users.

In the RM module the permissions to edit and revert/publish content are lumped
together, so that it isn't possible to enforce separation of these
responsibilites by role. This module allows you to assign distinct permissions
for authors (to only create and edit content) and moderator roles (to review,
publish, revert, unpublish and optionally delete content).
No unnessary revisions are created when saving a revision that is pending.
Menu navigation has been altered so that users first pick the desired 
revision before being allowed to view, edit, publish, revert, unpublish or 
delete.
Triggers are provided for the publish, unpublish and revert events.
By taking advantage of the Module Grants module this module integrates better
with the Workflow and Taxonomy Access Control (Lite) modules. This means that
you can easily implement fine-grained content access control based on
categories as well as workflow states. With both Module Grants and Revisioning
installed this all works for both published and unpublished content.
There's also a "publish-pending-revision" action that may be triggered from
a workflow state transition (like "in review"->"publish").
Unlike RM, Revisioning does not require any additional database tables.

INSTALLATION
============
0. Install the Module Grants module. This is a package containing 4 modules.
   Although highly recommended the main module in this package is not required,
   but the Node Tools submodule is. Module Grants Monitor is also recommended,
   although Revisioning features similar functionality through a canned view
   (for which, you'll naturally have to install Views).
1. Optionally install the Diff module if you want to compare revisions and
   highlight the differences.
2. Place the "revisioning" folder in your "sites/all/modules" directory.
   Enable Revisioning under Administer >> Site building >> Modules.

CONFIGURATION
=============
3. Under Administer >> Content >> Content types, click "edit" next to the
   content types for which you wish to enable/disable revisioning. Under
   "Workflow Settings", Default Options, tick both the "Create new revision"
   and "New revision in draft, pending moderation" checkboxes. Also in this
   section UNtick "Published", so that all new content is created in an 
   unpubished state, i.e. invisible to the public.
   "New revision in draft, pending moderation" means that when a user edits and
   saves a piece of content the new revision isn't automatically made current.
   The previous copy remains unchanged and visible to the public until the 
   newer revision is published in its place.
   There is an additional radio-button on the same page that augments the above
   behaviour giving you the option to "Only create a new revision when saving
   content that is not already in draft/pending moderation". This will save you
   some disk space, because until the draft is published all modifications will
   be applied to the same copy, i.e. no new revision is created when one 
   already exists. On the other hand there are situations, for instance with a
   Wiki page with multiple authors editing the same copy, where you do want 
   every Save to create a new draft (revision), so that contributors can
   compare what was changed between saves. The Diff module is a good addition
   to Revisioning for this.
4. Revisioning builds on the Accessible content menu item (if you have enabled
   Module Grants Monitor), adding the "In draft/Pending publication" filter to
   the double row of tabs.
5. Grant to the various roles the view/delete/revert revisions permissions
   (node access section) and the "edit revisions" permission (revisioning
   section). Typically you'd give authors the "view revisions" and
   "edit revisions" permissions, while moderators will get the same as well
   as the "publish/revert revisions" permission. Neither require the 
   "administer nodes" permission, which is a good thing as this gives ordinary
   users excessive rights.

USAGE
=====
You should now be in business. Log in as one of the authors and Create content.
Save. Log out, then log in as a moderator to publish the content via the
Accessile content >> Pending tab (if you installed Module Grants Monitor) or via
the Content summary menu option (if you installed Views). Click on the title of
the post, then open the desired revision by clicking on the date. Check the
content, the press the "Publish this" tab.
Note that up to this point content isn't visible to the public.
Log in as an author again and revise the content. You will notice that upon
saving the new revision, the one visible to the public remains unchanged.
Log in as a moderator again to promote (publish), the revised content to live.
As an alternative to the Accessible content menu item, you may want to activate
the "pending revisions" block. This block is particularly useful for moderators
as it constantly shows the latest content requiring moderator attention in an 
inobtrusive corner of the screen. Configure and enable the block like any other
on the Administer >> Site building >> Blocks page.
You can use this module in combination with TAC or TAC-Lite for fine-grained
access control based on vocabularies (such as "region" or "department")
associated with the various content types. Be aware that any permissions
given in the "node module" section override those granted via TAC/TAC-Lite,
so you probably only want to assign a few creation permissions in the node
module and do the view, update and delete grants via TAC/TAC-Lite.
In addition you may want to install the Workflow module to further segragate
the author and moderator roles via access control based on states such as
"in draft", "in review" and "live". Workflow also allows you to notify users
when state transitions occur (e.g. when a moderator declines or publishes a
submitted revision).
Step-by-step guides on the usage of the Revisioning module in combination
with the TAC-Lite and Workflow modules can be found on the Revisioning project
page http://drupal.org/project/revisioning. 

AUTHOR
======
Rik de Boer, Melbourne, Australia; inspired by the Revision Moderation module.
$Id: README.txt,v 1.1.2.1.2.2 2009/01/02 20:05:27 fago Exp $

Content Access Module
-----------------------
by Wolfgang Ziegler, nuppla@zites.net

Yet another node access module.
This module allows you to manage permissions for content types by role. It allows you to specifiy
custom view, view own, edit, edit own, delete and delete own permissions for each content type.
Optionally you can enable per content access settings, so you can customize the access for each
content node.

In particular
  * it comes with sensible defaults, so you need not configure anything and everything stays working
  * it is as flexible as you want. It can work with per content type settings, per content node settings
    as well as with flexible Access Control Lists (with the help of the ACL module).
  * it trys to reuse existing functionality instead of reimplementing it. So one can install the ACL
    module and set per user access control settings per content node.
    Furthermore the module provides conditions and actions for the rules module, which allows one
    to configure even rule-based access permissions.
  * it optimizes the written content node grants, so that only the really necessary grants are written.
    This is important for the performance of your site.
  * it takes access control as important as it is. E.g. the module has a bunch of simpletests to ensure
    everything is working right.
  * it respects and makes use of drupal's built in permissions as far as possible. Which means the
    access control tab provided by this module takes them into account and provides you a good overview
    about the really applied access control settings. [1]


So the module is simple to use, but can be configured to provide really fine-grained permissions!


Installation
------------
 * Copy the content access module's directory to your modules directory and activate the module.
 * Optionally download and install the ACL module too.
 * Edit a content type at admin/content/types. There will be a new tab "Access Control".


ACL Module
-----------
You can find the ACL module at http://drupal.org/project/acl. To make use of Access Control Lists
you'll need to enable per content node access control settings for a content type. At the access
control tab of such a content node you are able to grant view, edit or delete permission for specific
users.


Running multiple node access modules on a site (Advanced!)
-----------------------------------------------------------
A drupal node access module can only grant access to content nodes, but not deny it. So if you
are using multiple node access modules, access will be granted to a node as soon as one of the
module grants access to it.
However you can influence the behaviour by changing the priority of the content access module as
drupal applies *only* the grants with the highest priority. So if content access has the highest
priority *alone*, only its grants will be applied. 

By default node access modules use priority 0.



Footnotes
----------

[1] Note that this overview can't take other modules into account, which might also alter node access.
    If you have multiple modules installed that alter node access, read the paragraph about "Running 
    multiple node access modules on a site".
/* $Id: README.txt,v 1.3.2.5 2009/06/07 22:19:31 sun Exp $ */

-- SUMMARY --

Switchtheme allows you to create a block to allow users to switch themes on the
fly.  The module will present users with a list of all enabled themes and allow
them to choose between them. Anonymous users have their choices tracked in a
session variable.  For logged in users, the user record is updated with their
choice so that their last selection will stay the same the next time they log in. 

For a full description visit the project page:
  http://drupal.org/project/switchtheme
Bug reports, feature suggestions and latest developments:
  http://drupal.org/project/issues/switchtheme


-- REQUIREMENTS --

None.


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.

* Enable the module in Administer >> Modules.


-- CONFIGURATION --

* Configure user permissions in Administer >> User management >> Permissions
  >> Switchtheme.
  Enable the user roles are allowed to see the switchtheme block.  You may only
  want authenticated users to see it, for instance.

  If the chosen theme should be stored permanently for registered users, please
  note that you have to grant the "select different theme" permission in Drupal
  core for (selected) user roles of authenticated users.

* Customize the settings in Administer >> Site configuration >> Switchtheme and
  enable all themes that you want users to choose from.

  The theme names may not be very meaningful to regular users, so the settings
  page allows you to create custom titles to use for each theme.  If no titles
  are setup the original theme name is displayed instead.

* Go to Administer >> Site building >> Blocks and make sure that the "select
  switchtheme" block is enabled, and also enabled in every enabled theme. 


-- NOTES --

The module has been designed to defer to themes created by the Sections module
(http://drupal.org/project/sections).  In other words, if you use the
sections module to create a special theme for the admin section, the
switchtheme module will use that theme rather than the individual theme chosen
by the user.

If you are setting up a lot of themes, you may find the Block Region module 
(http://drupal.org/project/blockregion) to be a helpful way of setting up
blocks to work the same way across many themes.  That will save you the time of
setting up every block in every theme.


-- USAGE --

You can use this module to present users with a small, medium, and large text
version of your site.  To do that:

* Select the theme that you want to use for this purpose.  Create a subfolder
  below the theme folder for every subtheme that you want to create (i.e.
  medium, large, and extra-large).  The folder names will be used as the theme
  names, so make sure they don't duplicate any existing themes.  One way to do
  that is to use the regular theme name as a prefix, then append something to
  the name (i.e. bluemarine_large).

* Copy the style.css and any theme images from the main folder to each of these
  sub-folders.

* Change style.css in each subfolder to display appropriately for the chosen
  font size.  Well-designed CSS may only need to be changed in a few places.
  For instance, the Bluemarine theme sets a basic font size at the very top of
  the CSS to 76%.  Make that percentage higher and almost everything in the
  theme will be displayed in larger text.  (You may need to change a few other
  CSS settings to get it working completely.)

  Any style.css files and images in the subfolders will override those in the
  main folder, but all folders will use the template.php and tpl.php files in
  the main theme folder, so you don't need to duplicate all the template files,
  only the css and image files.

* Go to the settings page and give the themes user-friendly names like
  'Regular', 'Medium', and 'Large', and turn the blocks on as noted above.

Now your users will have a drop-down selection list they can use to increase
the font size of their pages.


-- CUSTOMIZATION --

* When Switchtheme module is enabled, users are able to switch to a different
  theme any time they follow a link that includes a query string like in this
  URL: http://www.example.com/foo/bar?theme=exampletheme

  That means, you can implement specially crafted links into your site or themes
  which allow users to switch to pre-defined themes.  For example, using
  Drupal's l() function in page.tpl.php (without code tags):
<code>
print l('Red theme', $_GET['q'], array(), 'theme=red');
</code>


-- CONTACT --

Current maintainers:
* Daniel F. Kudwien (sun) - dev@unleashedmind.com

Previous maintainers:
* Karen Stevenson (KarenS) - http://drupal.org/user/45874

This project has been sponsored by:
* UNLEASHED MIND
  Specialized in consulting and planning of Drupal powered sites, UNLEASHED
  MIND offers installation, development, theming, customization, and hosting
  to get you started. Visit http://www.unleashedmind.com for more information.

Nodewords: The Drupal 6 Meta Tags module
----------------------------------------

This module allows you to set some meta tags for the different content
available on your site, including nodes, users, views, taxonomy filters and
error pages.

Giving more attention to the important keywords and/or description on your site
may help you to get better positioning within public search engines.

This version of the module only works with Drupal 6.x.


Features
------------------------------------------------------------------------------
The primary features include:

* The current supported basic meta tags are ABSTRACT, CANONICAL, COPYRIGHT,
  GEO.POSITION, DESCRIPTION, ICBM, KEYWORDS, REVISIT-AFTER, ROBOTS.
  These meta tags are provided by the module Basic meta tags.

* The Dublin Core meta tag schema may be added by enabling the "Nodewords
  extra meta tags" module.

* The Open Graph Protocol meta tags, as used by Facebook, may be added by
  enabling the "Open Graph meta tags" module (see below).

* A pluggable system allow the inclusion of new meta tags in addition to the
  ones provided by this module.

* Meta tags can be assigned site-wide defaults and then overridden on a
  per-node, per-tag and per-path basis.

* It is possible to control which of the available tags will be available for
  editing versus only using the previously configured values.

* All text of the DESCRIPTION and KEYWORDS meta tags are added to the search
  system so they are searchable too; other meta tags could be added to the
  search system too (depending on the code implemented from the module).


Integration with other modules
------------------------------------------------------------------------------
Nodewords integrates with other modules for automatic selection of meta tags.

* On node pages all terms of some specified vocabularies associated can be
  added to the KEYWORDS meta tag.

* On taxonomy pages, the term description is used as the meta tag DESCRIPTION.
  The term itself is added to the list of KEYWORDS. You can override the
  description to use, if you wish.

* Previous versions of this module provided support for Views and Panels. This
  feature has been removed from Nodewords 6.x-1.x (since August 15, 2009) as
  the module now provides an API allowing other modules to integrate with it.

* This module may also integrate with Tagadelic, CCK, and others.

* The Meta tags Node Type module [1] allows defaults to be assigned to each
  content type, which can then be overridden on individual nodes.

* The Domain Meta module [2] provides integration with the Domain Access
  module [3].


Installing Nodewords (first time installation)
------------------------------------------------------------------------------
 1. Backup your database.

 2. Copy the module as normal.
   More information about installing contributed modules could be found at
   "Install contributed modules" [4].

 3. Enable the "Nodewords" module from the module administration page
   (Administer >> Site configuration >> Modules).

 4. Enable other modules which provide meta tags. The following are included:
    - Nodewords basic meta tags: for "abstract", "canonical", "copyright",
      "description", "keywords", "revisit-after" and "robots" meta tags.
    - Nodewords extra meta tags: for Dublin Core, "geo.position", "icbm" and
      "shorturl" meta tags.
    - Nodewords Open Graph meta tags: for the Open Graph Protocol meta tags,
      used for integration with Facebook's API.

 5. Configure the module (see "Configuration" below).


Updating Nodewords (module version upgrade)
------------------------------------------------------------------------------
 1. Verify that the version you are going to upgrade contains all the features
    your are using in your Drupal setup. Some features could have been removed
    or replaced by others.

 2. Backup your database.

 3. Update current module code with latest recommended version. Previous
    versions could have bugs already reported and fixed in the last version.

 4. Complete the update process: set the site into maintenance mode, visit the
    update.php script and finish the update operation. For more information
    please see: http://groups.drupal.org/node/19513

 5. Verify your module configuration and check that the features you are using
    work as expected. Also verify that all required modules are enabled, and
    permissions are set as desired.

Note: Whenever you have the chance, try an update in a local or development
      copy of your site.


Configuration
------------------------------------------------------------------------------
 1. On the access control administration page ("Administer >> User management
    >> Access control") you need to assign:

    - The "administer meta tags" permission to the roles that are allowed to
      administer the meta tags (such as setting the default values and/or
      enabling the possibility to edit them),

    - The "edit XYZ tag" permission to the roles that are allowed to set and
      edit meta tags for the content (there is a permission for each of the
      meta tags currently defined).

    All users will be able to see the assigned meta tags.

 2. On the settings page ("Administer >> Content management >> Meta tags") you
    can specify the default settings for the module. To access this page users
    need the "administer meta tags" permission.

 3. You should enable meta tags for editing before they are available for use.
    The same operation should be done for meta tag output. Only allowed Meta
    tags are available for editing or exposed in the HTML of your site.

 4. The front page is an important page for each website, therefore you can
    specifically set the meta tags to use on the front page meta tags settings
    page ("Administer >> Content management >> Meta tags >> Default and
    specific meta tags >> Front page"). Users need the "administer meta tags"
    permission to do this. When there are resources providing meta tags
    promoted in the front page, you may force the usage of "Front page" meta
    tags superseding all of them.

    Alternatively, you can opt not to set the meta tags for the front page on
    this page, but to use the meta tags of the node, term or other page the
    used to control the front page. To do this, uncheck the "Use front page
    meta tags" option on the main settings page.

    Note that, in contrast to previous versions of this module, the site
    mission and/or site slogan are no longer used as DESCRIPTION or ABSTRACT
    on the front page!


Open Graph Protocol Extra Steps
------------------------------------------------------------------------------
Because of a limitation in Drupal 6, if the Open Graph meta tags module is
enabled the site's theme will have to be customized. In order to work
correctly, and pass XHTML validation, the page.tpl.php for any theme(s) in use
must to be customized to add the following attribute to the HTML tag:

  prefix="og: http://ogp.me/ns#"

As an example, to make it work with the Garland theme the HTML tag must be
changed to the following:

  <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="<?php print $language->language ?>" lang="<?php print $language->language ?>" dir="<?php print $language->dir ?>" prefix="og: http://ogp.me/ns#">

Unless this change is made the page output will fail XHTML validation and the
Open Graph meta tags may not be properly identified by Facebook.


Using With non-PHPTemplate Themes (Chameleon, Marvin)
------------------------------------------------------------------------------
Because Nodewords depends upon PHPTemplate hooks in order to output the meta
tags it will not work with themes that do not use that template engine, e.g.
the core Chameleon or Marvin themes. In order for these to work a Nodewords
function must be called so it can insert the necessary tags into Drupal's
internal list of head tags. To insert the tags, edit the main theme file, e.g.
chameleon.theme, and insert the following at the top of the hook_page()
implementation, e.g. chameleon_page:

function chameleon_page($content, $show_blocks = TRUE, $show_messages = TRUE) {
  /**
   * Start Nodewords Changes.
   */
  // Allow Nodewords to add its tags to the internal HTML head tags array.
  if (module_exists('nodewords')) {
    $vars = array();
    nodewords_preprocess_page($vars);
  }
  /**
   * End Nodewords Changes.
   */

Once that is added the tags will be inserted into the HTML output as expected.


Known Issues
------------------------------------------------------------------------------
* Meta tags cannot be output with non-PHPTemplate themes like Chameleon or
  Marvin without customization (see above).
* Use of the Open Graph meta tags sub-module requires customizing the
  page.tpl.php file for the site's theme(s) (see above for details).
* Versions 6.x-1.9, 6.x-1.10 and 6.x-1.11 had a severe bug that could cause
  data loss when updating from 6.x-1.8 or older. The problem was in how
  nodewords_update_6162() changed the format of the 'id' field, causing records
  with an 'id' (nid, tid, uid) over 65,536 to be lost. The bug has been fixed
  in this release but any data lost as a result of this bug is irretrievable.
  The maintainers are terribly sorry about this and humbly apologize if your
  site(s) suffered data loss as a result of this and vow to do our utmost to
  ensure errors of this magnitude never happen again.


Related modules
------------------------------------------------------------------------------
Starting from nodewords-5.x-1.9 the following modules extend the nodewords
functionality:

- Meta tags Node Type, by Ariel Barreiro
- Meta Tags by Path, by Shannon Lucas

The latest development snapshot (6.x-1.x-dev), and version 6.x-1.1 or higher
implement a functionality similar to the one implemented in the module
Meta Tags by Path, which is not anymore required for those versions.

To assure compatibility between Nodewords and Meta tags Node Type, use the
latest version available of Nodewords and Meta tags Node Type; previous
versions were not compatible with the recent changes in Nodewords.


Credits / Contact
------------------------------------------------------------------------------
The current maintainers are Damien McKenna [5] and Dave Reid [6].

The original author of this module is Andras Barthazi. Mike Carter [7],
Gabor Hojtsy [8] and Robrecht Jacques [9] provided some feature enhancements,
while Alberto Paderno [10] maintained the module for much of its Drupal 6
lifecycle.

The best way to contact the authors is to submit an issue, be it a support
request, a feature request or a bug report, in the project issue queue:
  http://drupal.org/project/issues/nodewords


References
------------------------------------------------------------------------------
[1] http://drupal.org/project/nodewords_nodetype
[2] http://drupal.org/project/domain_meta
[3] http://drupal.org/project/domain
[4] http://drupal.org/documentation/install/modules-themes/modules-5-6
[5] http://drupal.org/user/108450
[6] http://drupal.org/user/53892
[7] http://drupal.org/user/13164
[8] http://drupal.org/user/4166
[9] http://drupal.org/user/22598
[10] http://drupal.org/user/55077
// $Id: README.txt,v 1.4 2010/03/25 18:43:43 johnalbin Exp $

ABOUT
-----

On 404 Not Found pages, Drupal will skip rendering of several pieces of your
website for performance reasons. These include:

1. The "Left" and "Right" regions of your theme.
2. The "Primary links" block and any other menu links block.*
3. The Primary links and Secondary links of your theme.*

* Unless you have configured a "Default 404 (not found) page" on
  admin/settings/error-reporting.

But many websites find those items invaluable. Especially on 404 pages, when
they want to show users how to get to real pages.

So this module simply revives those features on 404 pages.


INSTALLATION
------------

Simply install and enable the module. No configuration needed.
README.txt
==========

A module containing helper functions for Drupal developers and
inquisitive admins. This module can print a log of
all database queries for each page request at the bottom of each page. The
summary includes how many times each query was executed on a page, and how long each query
 took.
 
 It also
 - a block for running custom PHP on a page
 - a block for quickly accessing devel pages
 - a block for masquerading as other users (useful for testing)
 - reports memory usage at bottom of page
 - more
 
 This module is safe to use on a production site. Just be sure to only grant
 'access development information' permission to developers.

Also a dpr() function is provided, which pretty prints arrays and strings. Useful during
development. Many other nice functions like dpm(), dvm().

AJAX developers in particular ought to install FirePHP Core from http://www.firephp.org/ and put it in the devel directory. Your path to fb.php should looks like devel/FirePHPCore/lib/FirePHPCore/fb.php. You can use svn checkout http://firephp.googlecode.com/svn/trunk/trunk/Libraries/FirePHPCore. Then you can log php variables to the firebug console. Is quite useful. 

Included in this package is also: 
- devel_node_access module which prints out the node_access records for a given node. Also offers hook_node_access_explain for all node access modules to implement. Handy.
- devel_generate.module which bulk creates nodes, users, comment, terms for development

Some nifty drush integration ships with devel and devel_generate. See drush help for details.

COMPATIBILITY NOTES
==================
- Modules that use AHAH may have incompatibility with the query log and other footer info. Consider setting $GLOBALS['devel_shutdown'] = FALSE in order to avoid issues.
-  Modules that use AJAX should idenify their response as Content-type: text/javascript. The easiest way to do that is run your reply through drupal_json().


DRUSH UNIT TEST
==================
See develDrushTest.php for an example of unit testing of the Drush integration.
This uses Drush's own test framework, based on PHPUnit. To run the tests, use
phpunit --bootstrap=/path/to/drush/tests/drush_testcase.inc. Note that we must name a file
under /tests there.

AUTHOR/MAINTAINER
======================
Moshe Weitzman <weitzman at tejasa DOT com> http://cyrve.com
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
to the footer region. You may move it as desired. If you enable DBA
Debug Mode on the Devel Settings page, you will get more information.

Provides a second block that shows and explains the CRUD access rights
of the 10 most recently active users. This block is disabled by default
because it has a huge overhead.

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

STAFF
=====

Original author: Dave Cohen AKA yogadex on drupal.org
Current maintainer: Hans Salvisberg AKA salvis on drupal.org

=============================================================================

                               Krumo
                            version 0.1a

=============================================================================

You probably got this package from...
http://www.sourceforge.net/projects/krumo/

If there is no licence agreement with this package please download
a version from the location above. You must read and accept that
licence to use this software. The file is titled simply LICENSE.

OVERVIEW
------------------------------------------------------------------------------
To put it simply, Krumo is a replacement for print_r() and var_dump(). By 
definition Krumo is a debugging tool (PHP4/PHP5), which displays structured 
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
$Id: README.txt,v 1.11.2.8 2009/03/31 21:27:52 michellec Exp $

CONTENTS OF THIS FILE
---------------------
 * Introduction
 * Installation
 * Other configuration
 * Credits
 
INTRODUCTION
------------
Advanced Forum (http://drupal.org/project/advanced_forum) enhances Drupal's forum module to provide the look and, with the help of other modules, much of the functionality found in common forum software. Because it uses the core forum module, it uses the node and comment system built into Drupal and is completely integrated, not a bridge.

INSTALLATION
------------

1. Enable all dependencies: Author Pane ( http://drupal.org/project/author_pane ), Forum, 
   Taxonomy, Comment. (Optionally: Statistics)
   
2. Copy the entire advanced_forum project directory (not just the contents) to your 
   normal module directory (ie: sites/all/modules)
   
3. Enable the advanced forum module at ?q=admin/build/modules

4. Visit the Advanced Forum settings page at ?q=admin/settings/advanced-forum 
   # General:
     * "Advanced forum style directory" Select the style you are using. 
       See http://drupal.org/node/234042 for more information on this.
     * "Use graphical buttons for links" Check this if you want links to use graphical 
        buttons (where available).
     * "Treat all site comments like forum comments" If you would like advanced forum to 
       take over the theming of all comments, even those outside the forum, choose yes.
   # Forum and topic lists
     * "Hide the created column on the topic list" This option hides the created column
       on the topic list page, which can't be done purely in theming due to the header
       tablesort. If you hide this column, it is up to you to change the tenplate to
       display the information elsewhere.
     * "Get the number of new comments per forum on the forum list" Core forum shows the 
       number of new topics. If checked, Advanced Forum will get the number of new 
       comments as well and show it under "posts" on the forum overview. Slow query not 
       recommended on large forums.
     * "Number of characters to display for the topic title" On the main forums page, the
       title of the last topic is shown. Because this is a narrow column, it is 
       truncated. This option sets how many characters are shown.
     * "Number of hours before switching to date posted in displays" In the forum / topic
       listing, recent posts are shown like "1 day, 3 hours ago" and older posts will
       have the actual date. You control the cutoff here.
   # Topics
     * "Use topic navigation" Core forum gets the next and previous topics and shows 
       links to them under the top post. This is turned off by default as the query has 
       performance issues and the placement of the links is poor.
     * "User picture preset" You will only see this option if you have imagecache 2
        enabled. If you choose a preset here, it will be used for the avatars in forum
        posts. This can be used to give a more uniform appearance if people have many
        different sizes for avatars. If you don't want to use a preset, just leave it
        blank.

OTHER CONFIGURATION
-------------------
   
1. Forum settings ( ?q=admin/content/forum/settings ) 
    * Hot topic threshold: Up to you.
    * Topics per page: Up to you.
    * Default order: "Date - newest first" so the most recent posts are at the top of the 
      topic list.
2. Select content types to use in forums ( ?q=admin/content/taxonomy ) 
3. Edit the forum vocabulary
   * Check all content types you want to use in forums.
4. Comment settings ( ?q=admin/content/node-type/forum ) [Note: do this for each content 
   type used in forums] 
   * Expand "Comment settings" fieldset.
   * Default comment setting: "Read/write"
   * Set Default display mode: Flat list - expanded. (Advforum is intended to be used 
     flat. Using it threaded should mostly work but is unsupported and may have some 
     issues.) 
   * Default display order: Date - oldest first 
   * Default comments per page: Up to you. (If you chose to have a threaded forum, 
     setting this number to the maximum will reduce issues with pagination and threading.) 
   * Comment controls: "Do not display" is recommended.
   * Anonymous commenting: Up to you.
   * Comment subject field: Up to you. If disabled, advforum will not display the Drupal 
     default subject, which is the first few words of the comment.
   * Preview comment: Up to you.
   * Location of comment submission form: Up to you. Displaying below provides a non-ajax 
     quick reply.
5. User settings ( ?q=admin/user/settings ) 
   * Signature support: Enabled
   * Picture support: Enable this for avatars in the forum.
   * Picture maximum dimensions: If you change this from the default 85x85, you will want 
     to size it in either CSS or with imagecache to avoid breaking the forum layout.
6. Statistics settings ( ?q=admin/reports/settings ) 
   * Enable access log: Enabled
   * Count content views: Enabled - Needed for topic views count.   
    
CREDITS
-------
Developer and maintainer: Michelle Cox ( http://drupal.org/user/23570 )

Advanced forum was originally based on flatforum. Though there is little or no code left
from that module, its authors deserve credit for the idea.

The Naked styles, which are the basis of all the other styles, were created by 
stephthegeek (http://drupal.org/user/47874). Previous theme work was done by eigentor 
(http://drupal.org/user/96718) and jacine (http://drupal.org/user/88931)

Icons provided by paris (http://drupal.org/user/14747) and yoroy 
(http://drupal.org/user/41502)

// $Id: README.txt,v 1.1.4.1 2009/02/10 09:23:57 acm Exp $

Cluetip module:
-------------------------
Author - Chris Shattuck (www.impliedbydesign.com)
Co-Author - Alex McFadyen (www.openlyconnected.com)
License - GPL


Overview:
-------------------------
The cluetip module is a wrapper for the jquery cluetip plugin which can
be found here: http://plugins.learningjquery.com/cluetip/ and downloaded
here: http://plugins.jquery.com/project/cluetip/. The Cluetip plugin
provides nice, configurable hover-overs using the "title" attribute. The
plugin has many options, and includes a "demo" folder, which you should
check out to learn about how it works.

The "dimentions" and "hover intent" plugins are includes in the cluetip
plugin distribution.


As of D6 this module is now dependent on the JQ module 
(http://drupal.org/project/jq), as cluetips contains the "hover intent" 
it will be used, however if you have the dedicated "hover intent" module 
(http://drupal.org/project/hoverintent) then you can simply set the bool 
on line 18 of cluetip.module to true. 



Installation:
-------------------------
- Download the Cluetip module and copy it into your 'modules'
directory.
- Download Cluetip from http://plugins.jquery.com/project/cluetip/
, unzip and put the entire directory in the cluetip module folder. 
- Go to Administer >> Modules and enable the module.
- Go to the JQ module settings page /admin/settings/jq and enable cluetip

Example:
-------------------------
The Cluetip module will handle including all the dependent files 
required for cluetip to work. To use, use the following instructions:
- In your module, use the cluetip_load() function to load a js file
that includes the parameters for your cluetip. As an example, you can
do the following:
1. Add the following code to your module or template.php file:
jq_add('cluetip');
2. To use the cluetip, you need to add the class "cluetip-title" to 
your element, and form the title attribute in the following way:
<div class="cluetip-title" title="Header|The body of the title".


Last updated:
------------
; $Id: README.txt,v 1.1.4.1 2009/02/10 09:23:57 acm Exp $Introduction
============
Twitter module allows listing tweets in blocks or pages. Its integration with Views opens the
door to all sorts of formatting (ie. as an automatic slideshow with views_slideshow). It also
provides useful input filters to easily link Twitter accounts and searches within text.

Twitter's submodules allow posting to twitter, executing actions/rules when tweeting or login 
with a Twitter account.

OAuth
=====
Except for just listing tweets, OAuth module is required to authenticate against Twitter. If you 
just want to list tweets in a block, follow the steps at http://drupal.org/node/1253026.

If you download the OAuth module, get version 3.0 or higher as previous ones are not compatible
anymore. You can find it here: http://drupal.org/project/oauth.

Once OAuth has been enabled, go to admin/settings/twitter and follow instructions.

How to create a block with Tweets
=================================
Read the following step by step guide: http://drupal.org/node/1253026

How to add a Twitter account to a Drupal user account
=====================================================
Read http://drupal.org/node/1253026 for details.

How to use the username and hashtag input filters
=================================================
1. Go to admin/config/content/formats.
2. Select the text format where you want to use the filters.
3. At "Enabled filters" check the Twitter converters.

After that, clear cache and try to create a page with the following body:

#drupal @drupal

The above links to a search in Twitter over the #drupal tag and a to the @drupal profile.
These filters are avilable when configuring a tweets Views.


How to post to Twitter
======================
1. Read the OAuth section to install and configure OAuth.
2. Once OAuth has been configured, go to admin/settings/twitter/post and select from which
   node types a user may post to Twitter and the default message.
3. Verify permissions at admin/user/permissions.
4. Add a Twitter account and try to edit or post content.

How to sign in with Twitter
===========================
Existing and new users can sign in with Twitter by enabling the twitter_signin module. The
following scenarios are being contemplated so far:

* A visitor logs in with his Twitter account and, once authenticated at Twitter.com, he fills in
  his email in the Drupal registration form and receives an email to log in and set his account
  password.
* An existing user signs in with Twitter and then logs in into his Drupal user account. This results
  in the Twitter account getting related to the user account so next time Twitter sign in will work.
* An existing user with an already configured Twitter account can log in automatically by clicking
  on the Sign in with Twitter button.

An step by step guide can be found at http://drupal.org/node/649714
User Mailman Register
---------------------

This is a module for mailman subscribing which extends the Mailman Manager module features.
Project homepage: http://drupal.org/node/195527


Documentation
-------------

Documentation:    http://drupal.org/node/463508


Donation
--------

The User Mailman Register module is not sponsored by anyone but i develop and support it during my spare time for free. If you gain something thanks to it or you want to support its development, you can consider to make a donation following instructions in the module project page.


Author and Credits
------------------

The User Mailman Register module is developed by Samuele Tognini <samuele@samuele.netsons.org>
Blackout your Drupal site on January 18, 2012 as part of the global
anti-SOPA/PIPA protest! Politicians have reportedly backed down on
SOPA, but PIPA still remains so best to proceed with the blackout.

This module automates this via a quick hack.

Your site will look like:

  http://mikecantelon.com/?sopa_test=1

Your site will work normally until January 18, but on January 18 you
will only be able to access URLs starting with "user" and "admin"
without seeing the SOPA blackout page. After January 18 your site will
be back to normal.

Developed for/tested with Drupal 6 or Drupal 7. If using it with Drupal 7
just change "6.x" to "7.x" in the sopa.info file and you should be good
to go.

Inspired by WP-SOPA-Blackout:

  https://github.com/chrisguitarguy/WP-SOPA-Blackout

SOPA template from:

  http://www.zachstronaut.com/lab/text-shadow-box/stop-sopa.html

Let me know if there's any problems with this version.

-Mike

Module: Google Analytics
Author: Alexander Hass <http://drupal.org/user/85918>


Description
===========
Adds the Google Analytics tracking system to your website.

Requirements
============

* Google Analytics user account


Installation
============
* Copy the 'googleanalytics' module directory in to your Drupal
sites/all/modules directory as usual.


Usage
=====
In the settings page enter your Google Analytics account number.

All pages will now have the required JavaScript added to the
HTML footer can confirm this by viewing the page source from
your browser.

New approach to page tracking in 5.x-1.5 and 6.x-1.1
====================================================
With 5.x-1.5 and 6.x-1.1 there are new settings on the settings page at
admin/settings/googleanalytics. The "Page specific tracking" area now
comes with an interface that copies Drupal's block visibility settings.

The default is set to "Add to every page except the listed pages". By
default the following pages are listed for exclusion:

admin
admin/*
batch
node/add*
node/*/*
user/*/*

These defaults are changeable by the website administrator or any other
user with 'administer google analytics' permission.

Like the blocks visibility settings in Drupal core, there is now a
choice for "Add if the following PHP code returns TRUE." Sample PHP snippets
that can be used in this textarea can be found on the handbook page
"Overview-approach to block visibility" at http://drupal.org/node/64135.

Custom variables
=================
One example for custom variables tracking is the "User roles" tracking. Enter
the below configuration data into the custom variables settings form under
admin/settings/googleanalytics.

Slot: 1
Name: User roles
Value: [user-role-names]
Scope: Visitor

More details about Custom variables can be found in the Google API documentation at
http://code.google.com/intl/en/apis/analytics/docs/tracking/gaTrackingCustomVariables.html

Advanced Settings
=================
You can include additional JavaScript snippets in the custom javascript
code textarea. These can be found on the official Google Analytics pages
and a few examples at http://drupal.org/node/248699. Support is not
provided for any customisations you include.

To speed up page loading you may also cache the Analytics ga.js
file locally. You need to make sure the site file system is in public
download mode.Drupal bbcode.module README.txt
==============================================================================

The Drupal bbcode.module adds a BBCode filter to Drupal. This allows you
to use HTML-like tags as an alternative to HTML itself for adding markup
to your posts. BBCode is easier to use than HTML and helps to prevent
malicious users from disrupting your site's formatting.

See the help screen of the module (or the code) for information on which
tags and variants are supported. This implementation is not necessarily the
same as the original BBCode implementaion.
 
Note that this filter also recognizes and converts URLs and email addresses
to links automatically.

Installation
------------------------------------------------------------------------------
 
  - Download the BBCode module from http://drupal.org/project/bbcode

  - Create a .../modules/bbcode/ subdirectory and copy the files into it.

  - Enable the module as usual from Drupal's admin pages 
    (Administer » Modules)
 
Configuration
------------------------------------------------------------------------------

  - Before using BBCode you need to enable the BBCode filter in an input
    format (see Administer » Input formats » add input format)

  - You can enable/ disable the following features in the configuration page
    of the input format in which BBCode is enabled:

    * Convert web and email addresses to links
    * Javascript encoding of emails
    * Smart paragraph and line breaks
    * Print debugging info

  - If you've disabled "smart paragraph and line breaks", you need to enable
    Drupal's "Line break converter" with the BBCode filter. Don't use both
    together!

  - If you would like to use BBCode as a replacement for HTML, you could
    enable Drupal's "HTML filter" to remove or escape user entered HTML tags.

  - If you've enabled multiple filters, you may need to rearrange them to
    ensure they execute in the correct order. For example, if HTML filtering 
    is enabled, it is essential that BBCode be sorted AFTER the HTML filter. 
    If not this module will change the BBCode into HTML, and the HTML filter 
    will disallow and remove the code again.

Complementing Modules
------------------------------------------------------------------------------

The following optional modules may be used to enhance your BBCode 
installation:

  - Quicktags - http://drupal.org/project/quicktags
    Adds a BBCode formatting bar above all your textareas. 

  - Smileys module - http://drupal.org/project/smileys

Note: these are independent projects. Please do not report issues with them 
as BBCode problems!

Additional tags:
------------------------------------------------------------------------------

Here are some tags that's not part of the official BBCode implementation. 
You may want to add them to your bbcode-filter.inc file:

  - '#\[move(?::\w+)?\](.*?)\[/move(?::\w+)?\]#si' => '<marquee>\\1</marquee>',
  - '#\[mp3\](.*?)\[/mp3(?::\w+)?\]#si' => '<swf file="\\1">',

Credits / Contacts
------------------------------------------------------------------------------

  - The original author of this module is Alastair Maw, who can be reached at
    drupal-bbcode[at]almaw.com. 

  - Gabor Hojtsy (goba[at]php.net) also contributed to the module.

  - Javascript encoding of emails by László Bácsi (lackac[at]math.bme.hu).

  - Frank Naude converted this module to Drupal 4.7 and 5.0, added several
    BBCode tags, a linebreak converter, quicktags integration, etc.

TODO List
------------------------------------------------------------------------------

 - Translate this module into other languages.

 - Fix non-compliant HTML when "Smart paragraph and line breaks:" is set to 
   "Line and paragraph breaks". If HTML validation is important to you, use 
   one of the other options or submit a patch.

 - Configuration of which BBCode tags are allowed 
   (will require a complete rewrite).


Description
-----------

Poormanscron is a module which runs the Drupal cron operations without
needing the cron application.

For every page view, this module checks to see if our last cron run was more
than 1 hour ago (this period is configurable). If so, the cron hooks are
executed (which, for example, update RSS/syndication blocks), and Drupal
is happy. These cron hooks fire after all HTML is returned to the browser,
so the user who kicks off the cron jobs should not notice any delay.


Requirements
------------

This module requires Drupal 4.7 or a later version.


Installation
------------

1) Extract the package.
2) Copy/upload the Poormanscron folder to your sites/all/modules directory of
   your Drupal installation (e.g. sites/all/modules/poormanscron).
3) Enable the Poormanscron module in Drupal (administer -> modules).


Configuration
-------------

Poormanscron can be configured at:
  Administer -> Site configuration -> Poormanscron


Authors
-------

 * Moshe Weitzman <weitzman@tejasa.com> - original author
 * Uwe Hermann <uwe@hermann-uwe.de> - current maintainer

Admin 2.x
=========
The admin module provides UI improvements to the standard Drupal admin interface. The 2.x branch focuses on the following goals:

1. Sustainability - avoid excessive overrides of code, markup, and
   interface strings to ensure the module keeps the workload overhead
   on the maintainers and community to a minimum.

2. Pluggable/extensible architecture - ensure that admin serves as a
   starting point for other modules in contrib to implement admin
   interfaces.

3. Expose Drupal's strengths and downplay its weaknesses where possible.
   An honest approach to the underlying framework and architecture
   of Drupal will be less confusing to the user down the road.

Admin is not an original work - many of its decisions have had direct
influences from other work in the community:

- [Administration menu](http://drupal.org/project/admin_menu)
  Daniel Kudwien (sun)

- [Navigate](http://drupal.org/project/navigate)
  Chris Shattuck (chrisshattuck)

- [d7ux](http://www.d7ux.org)
  Mark Boulton & Leisa Reichelt


Installation
============
1. Install & enable the module.

2. Admin makes a permission available that allows only properly
   permissioned users to make use of the admin toolbar. Users with the
   'use admin toolbar' permission will be able to use the toolbar.

3. You can configure the layout, position, and enabled tools for the
   admin toolbar on `admin/settings/admin`.


Implementing your own Admin "plugins"
=====================================
Admin's "plugins" are simply Drupal blocks. In order to expose one of your
module's blocks as one suitable for use in the admin toolbar you can set the `admin` key in your `hook_block()` to `TRUE`. Note that users can add any blocks to the admin toolbar if they wish at `admin/settings/admin`, though not all will work well in the context of the admin toolbar.

    /**
     * Implementation of hook_block().
     */
    function my_module_block($op = 'list', $delta = 0, $edit = array()) {
      switch ($op) {
        case 'list':
          $blocks = array();
          $blocks['example'] = array(
            'info' => t('Example block'),
            'admin' => TRUE
          );
          return $blocks;
      }
    }


Theming your block and other tips
=================================
Your block should provide general rules for either of the admin toolbar
layouts (horizontal or vertical). You can specify CSS rules using the
following selectors:

    #admin-toolbar.horizontal {}
    #admin-toolbar.vertical {}

Admin provides fairly decent defaults for the following Drupal core
theme functions:

  - `theme('item_list')`
  - menu output (e.g. `menu_tree_output()`).
  - most form elements (with the exception of fieldsets)
  - admin panes (see below)

Admin provides an additional FormAPI element type `admin_panes`. Admin
panes allow you to fit multiple elements of content into a togglable
interface. The panes will automatically adjust to the layout to the toolbar
and display as either vertical tabs (horizontal layout) or accordian boxes
(vertical layout).

Here is an example of using admin panes in a form API array:

    $form['panes'] = array(
      '#tree' => FALSE,
      '#type' => 'admin_panes',
      'foo' => array(
        '#title' => t('Pane 1'),
        ...
      ),
      'bar' => array(
        '#title' => t('Pane 2'),
        ...
      ),
    );

Note that each child element must have a #title attribute to be labeled
properly.


Contributors
============
- yhahn (Young Hahn)
- ajashton (AJ Ashton)

-- SUMMARY --

Wysiwyg API allows to users of your site to use WYSIWYG/rich-text, and other
client-side editors for editing contents.  This module depends on third-party
editor libraries, most often based on JavaScript.

For a full description visit the project page:
  http://drupal.org/project/wysiwyg
Bug reports, feature suggestions and latest developments:
  http://drupal.org/project/issues/wysiwyg


-- REQUIREMENTS --

* None.


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.

* Go to Administer > Site configuration > Wysiwyg, and follow the displayed
  installation instructions to download and install one of the supported
  editors.


-- CONFIGURATION --

* Go to Administer > Site configuration > Input formats and

  - either configure the Full HTML format, assign it to trusted roles, and
    disable "HTML filter", "Line break converter", and (optionally) "URL filter".

  - or add a new input format, assign it to trusted roles, and ensure that above
    mentioned input filters are disabled.

* Setup editor profiles in Administer > Site configuration > Wysiwyg.


-- CONTACT --

Current maintainers:
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136
* Henrik Danielsson (TwoD) - http://drupal.org/user/244227

This project has been sponsored by:
* UNLEASHED MIND
  Specialized in consulting and planning of Drupal powered sites, UNLEASHED
  MIND offers installation, development, theming, customization, and hosting
  to get you started. Visit http://www.unleashedmind.com for more information.


INSTALLATION
  Hopefully, you know the drill by now :)
  1. Download the module and extract the files.
  2. Upload the entire mimemail folder into your Drupal sites/all/modules/
     or sites/my.site.folder/modules/ directory if you are running a multi-site
     installation of Drupal and you want this module to be specific to a
     particular site in your installation.
  3. Enable the Mime Mail module by navigating to:
     Administer > Site building > Modules
  4. Adjust settings by navigating to:
     Administer > Site configuration > Mime Mail

USAGE
  This module may be required by other modules, but is not terribly
  useful by itself. Once installed, any module can send messages by
  calling the mimemail() function:

  $sender      - a user object, text email address or an array with name, mail
  $recipient   - a user object, text email address or an array with name, mail
  $subject     - subject line
  $body        - body text in HTML format
  $plaintext   - boolean, whether to send messages in plaintext-only (default FALSE)
  $headers     - a keyed array with headers (optional)
  $text        - plaintext portion of a multipart e-mail (optional)
  $attachments - array of arrays with the file's path, MIME type (optional)
  $mailkey     - message identifier
  $send        - boolean, whether to send or only prepare the message (default TRUE)

  return       - an array containing the MIME-encoded message, including headers and body

  This module creates a user preference for receiving plaintext-only messages.
  This preference will be honored by all calls to mimemail() if the format is not
  explicitly set and the user has access to edit this preference (allowed by default).

  E-mail messages are formatted using the mimemail-message.tpl.php template.
  This includes a CSS style sheet and uses an HTML version of the text.
  The included CSS is either:
    the mail.css file found in your default theme or
    the combined CSS style sheets of your default theme and

  CSS style sheets with "email" media are always included.

  To create a custom mail template copy the mimemail-message.tpl.php file from
  the mimemail/theme directory into your default theme's folder. Both general and
  by-mailkey theming can be performed:
    mimemail-message.tpl.php (for all messages)
    mimemail-message--[mailkey].tpl.php (for messages with a specific mailkey)
  Note that if you are using a different administration theme than your default theme,
  you should place the same template files into that theme folder too.

  Images with absolute path will be available as remote content. To embed images
  into emails you have to use relative paths.
  For example:
    instead of http://www.mysite.com/sites/default/files/mypicture.jpg
    use /sites/default/files/mypicture.jpg

  Since some email clients (namely Outlook 2007 and GMail) is tend to only regard
  inline CSS, you can use the Compressor to convert CSS styles into inline style
  attributes. It transmogrifies the HTML source by parsing the CSS and inserting the
  CSS definitions into tags within the HTML based on the CSS selectors. To use the
  Compressor, just enable it.

CREDITS

  MAINTAINER: Allie Micka < allie at pajunas dot com >

  * Allie Micka
    Mime enhancements and HTML mail code

  * Gerhard Killesreiter
    Original mail and mime code

  * Robert Castelo
    HTML to Text and other functionality

// $Id: README.txt,v 1.20.2.1 2010/07/05 21:37:21 soxofaan Exp $

Readme file for the CAPTCHA module for Drupal
---------------------------------------------

captcha.module is the basic CAPTCHA module, offering general CAPTCHA
administration and a simple math challenge.

Submodule image_captcha.module offers an image based challenge.

Installation:
  Installation is like with all normal drupal modules:
  extract the 'captcha' folder from the tar ball to the
  modules directory from your website (typically sites/all/modules).

Dependencies:
  The basic CAPTCHA module has no dependencies, nothing special is required.

Conflicts/known issues:
  CAPTCHA and page caching do not work together currently.
  However, the CAPTCHA module does support the Drupal core page
  caching mechanism: it just disables the caching of the pages
  where it has to put its challenges.
  If you use other caching mechanisms, it is possible that CAPTCHA's
  won't work, and you get error messages like 'CAPTCHA validation
  error: unknown CAPTCHA session ID'.

Configuration:
  The configuration page is at admin/user/captcha,
  where you can configure the CAPTCHA module
  and enable challenges for the desired forms.
  You can also tweak the image CAPTCHA to your liking.
// $Id: README.txt,v 1.5 2009/09/23 21:23:00 soxofaan Exp $

It possible to put your own fonts for the Image CAPTCHA in this folder.
However, this is not the recommended way, as they can get lost easily during
a module update. The recommended way to provide your own fonts is putting them
in the files directory of your Drupal setup or, just like with contributed
modules and themes, in the "libraries" folders sites/all/libraries/fonts
or sites/<site>/libraries/fonts. 
// $Id: README.txt,v 1.1 2009/09/19 12:51:20 soxofaan Exp $

This directory contains a subset (Regular and Bold) of the Tuffy typeface
created by Thatcher Ulrich (http://tulrich.com/fonts) and released in the
public domain.

Original licensing statement of the creator
-------------------------------------------
Here are my dabblings in font design. I have placed them in the Public Domain. 
This is all 100% my own work. Usage is totally unrestricted. 
If you want to make derivative works for any purpose, please go ahead.

I welcome comments & constructive criticism.

Put another way, a la PD-self (http://en.wikipedia.org/wiki/Template:PD-self):
  I, the copyright holder of this work, hereby release it into the public 
  domain. This applies worldwide.

  In case this is not legally possible,

  I grant any entity the right to use this work for any purpose, 
  without any conditions, unless such conditions are required by law.

-Thatcher Ulrich <tu@tulrich.com> http://tulrich.com
// $Id: README.txt,v 1.22.2.3 2010/04/28 02:36:01 jmiccolis Exp $

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Features
 * Installation
 * Case Tracker URLs
 * Case Tracker Caveats!


INTRODUCTION
------------

Current Maintainer: jmiccolis <http://drupal.org/user/31731>

Previous Maintainer: zero2one <http://drupal.org/user/105066>
Original Sponsor: Digital202
Original Developers: India-based team
Oversight: DaveNotik (http://drupal.org/user/18129/contact), killes, zero2one

This module enables teams to track outstanding cases which need resolution.

This is a rewrite of the project.module and is very similar to that module
but varies in important ways. The project.module is specific to software
development and the need for a more generic issue tracker had been expressed.
As such, the casetracker.module only includes relevant functionality, but
also uses regular Drupal comments and integrates cleanly with Views, Organic
Groups, Mailhander, CCK, and more.


FEATURES
------------

Case Tracker enables teams to track outstanding cases. A case could be a bug
report, a feature request, or a general task. You can also define new case
types. Using Case Tracker, you can set the status of cases and their priority.

Case Tracker lets you have multiple projects and each case is tied to a project. 
The module includes default Project and Case node types. However, you can also
define existing node types to act as Project and Case node types in the
administrative interface. 

Case Tracker includes three modules:
 * Case Tracker: Enables the handling of projects and their cases
 * Case Tracker Basic: Enables a basic project node type for use with Case Tracker
 * Case Tracker Actions: Provides actions for Case Tracker

Case Tracker comes with a default interface that is powered by the Views module,
which can be customized and extended.

Using the administrative interface, you can use Case Tracker to:
 * Assign a user to all new cases by default
 * Assign a default case priority, status, and type to all cases
 * Define existing node types to act as Project and Case node types
 * Define new case states. Case state realms include priority, status, and type

Users can be assigned the following permissions at admin/user/permissions:
 * "administer case tracker"
 * "assign cases"
 * "create projects"
 * "create cases"
 * "edit own projects"
 * "edit own cases"

INSTALLATION
------------

1. Copy the files to your sites/all/modules/ directory.

2. Enable the casetracker module at admin/modules.

3. Assign the project and case node type and other relevant case options at
   admin/settings/casetracker. Case Tracker ships with simplistic "Project"
   and "Case" types in its casetracker_basic.module; although you can use
   these, you will get stronger flexibility by assigning it to a
   content type of your own creation, or an Organic Group.

4. Customize case types, priorities, and states at admin/casetracker.

5. Enable permissions in admin/access.

Note: for more project.module-like functionality, try installing the
comment_upload.module and enabling comment attachments for case nodes.


CASE TRACKER URLS
-----------------

The project based URLs we provide are briefly described below. These displays
are completely powered by the Views module and can be completely disabled or
reworked for completely different displays.

  /casetracker/
    Displays a list of all cases.

  /casetracker/my
    Displays a list of cases assigned to the current user.

  /casetracker/projects/
    Displays a list of all projects.


CASE TRACKER CAVEATS!
---------------------

Some common gotchas which are, at the moment, "by design":

 * The "Last modified" value of Case Tracker cases is determined by the
   timestamp of the last comment attached to them (or, in the absence of
   a single comment, the node creation time). This requires that the
   comment.module (and node_comment_statistics table) are enabled and
   created. We CAN think of some use cases for not requiring comments on
   a case, but we think them edge cases and not enough to cater to. If
   you feel otherwise, don't hesitate to voice your opinion.

 * Case Tracker does not provide any access control to nodes or fields.
   There are other fine modules which provide varying kinds of access control
   which can be used with Case Tracker.


// $Id: README.txt,v 1.1 2009/04/22 15:39:51 jareyero Exp $

Notifications Add-on: README.txt
=========================

This is a collection of add-on modules for the notifications package, http://drupal.org/project/notifications

The idea is to keep here a miscelaneous collection of modules that are:
- Not part of the core Notifications engine so they won't be required by Notifications itself
- Not as mature as the main package and as such can enjoy a faster development speed
- Maybe depending on some other modules so we want to keep them in sync with them

Read the project page for the latest information about the modules contained here.

Development Seed, http://www.developmentseed.org
// $Id: README.txt,v 1.1.2.2 2009/06/27 09:54:16 jareyero Exp $

Notifications Nice Links: README.txt
====================================
This is a js widget for Notifications module. It will display a js overlay with Subscription links.
The original idea and most of the code come from http://groups.drupal.org/node/17779

Installation:
-------------
- After unpacking the module into your 'modules' folder you need to download the jQuery Cluetip plug-in.
- Get it from http://plugins.jquery.com/project/cluetip (version 1.0.3)
- Unpack it inside the module in a 'cluetip' folder

Notes:
------
- This is the 'use it or leave it' kind of module. Feature requests will be ignored unless coming with a good patch.
- It has been tested with Cluetip 1.0.2. Other versions are *unsupported* = issues will be just ignored.

If anyone else wants to maintain this module, just drop me a line: http://drupal.org/user/4299/contact


// $Id: README.txt,v 1.1.2.2 2009/06/27 09:54:16 jareyero Exp $

This is the folder where you should unpack jQuery-Cluetip 1.0.3
After that the jquery.cluetip.js file should be in this folderThis directory is reserved for core theme files. Custom or contributed
themes should be placed in their own subdirectory of the sites/all/themes
directory. For multisite installations, they can also be placed in a subdirectory
under /sites/{sitename}/themes/, where {sitename} is the name of your site
(e.g., www.example.com). This will allow you to more easily update Drupal core files.

For more details, see: http://drupal.org/node/176043

This directory is reserved for core module files. Custom or contributed
modules should be placed in their own subdirectory of the sites/all/modules
directory. For multisite installations, they can also be placed in a subdirectory
under /sites/{sitename}/modules/, where {sitename} is the name of your site
(e.g., www.example.com). This will allow you to more easily update Drupal core files.

For more details, see: http://drupal.org/node/176043

