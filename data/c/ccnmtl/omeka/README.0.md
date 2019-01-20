"Moono" Skin
====================

This skin has been chosen for the **default skin** of CKEditor 4.x, elected from the CKEditor
[skin contest](http://ckeditor.com/blog/new_ckeditor_4_skin) and further shaped by
the CKEditor team. "Moono" is maintained by the core developers.

For more information about skins, please check the [CKEditor Skin SDK](http://docs.cksource.com/CKEditor_4.x/Skin_SDK)
documentation.

Features
-------------------
"Moono" is a monochromatic skin, which offers a modern look coupled with gradients and transparency.
It comes with the following features:

- Chameleon feature with brightness,
- high-contrast compatibility,
- graphics source provided in SVG.

Directory Structure
-------------------

CSS parts:
- **editor.css**: the main CSS file. It's simply loading several other files, for easier maintenance,
- **mainui.css**: the file contains styles of entire editor outline structures,
- **toolbar.css**: the file contains styles of the editor toolbar space (top),
- **richcombo.css**: the file contains styles of the rich combo ui elements on toolbar,
- **panel.css**: the file contains styles of the rich combo drop-down, it's not loaded
until the first panel open up,
- **elementspath.css**: the file contains styles of the editor elements path bar (bottom),
- **menu.css**: the file contains styles of all editor menus including context menu and button drop-down,
it's not loaded until the first menu open up,
- **dialog.css**: the CSS files for the dialog UI, it's not loaded until the first dialog open,
- **reset.css**: the file defines the basis of style resets among all editor UI spaces,
- **preset.css**: the file defines the default styles of some UI elements reflecting the skin preference,
- **editor_XYZ.css** and **dialog_XYZ.css**: browser specific CSS hacks.

Other parts:
- **skin.js**: the only JavaScript part of the skin that registers the skin, its browser specific files and its icons and defines the Chameleon feature,
- **icons/**: contains all skin defined icons,
- **images/**: contains a fill general used images,
- **dev/**: contains SVG source of the skin icons.

License
-------

Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.

Licensed under the terms of any of the following licenses at your choice: [GPL](http://www.gnu.org/licenses/gpl.html), [LGPL](http://www.gnu.org/licenses/lgpl.html) and [MPL](http://www.mozilla.org/MPL/MPL-1.1.html).

See LICENSE.md for more information.
Edit CSS Style plug-in notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlike WYSIWYG editor functionality that operates only on the selected text,
typically by inserting new HTML elements with the specified styles.
This plug-in operates on the HTML blocks surrounding the selected text.
No new HTML elements are created.

This plug-in only operates on the surrounding blocks and not the nearest
parent node.  This means that if a block encapsulates a node,
e.g <p><span>text</span></p>, then only the styles in the block are
recognized, not those in the span.

When selecting text that includes multiple blocks at the same level (peers),
this plug-in accumulates the specified styles in all of the surrounding blocks
and populates the dialogue checkboxes accordingly.  There is no differentiation
between styles set in all the blocks versus styles set in some of the blocks.

When the [Update] or [Apply] buttons are pressed, the styles selected in the
checkboxes are applied to all blocks that surround the selected text.
![Neatline Logo](http://neatline.org/images/neatline-logo-rgb.png)

# Neatline

**Neatline is a lightweight, extensible framework for creating interactive editions of visual materials - maps, paintings, photographs, and anything else that can be captured as an image.**

Built as a plugin for [Omeka](http://omeka.org/), a collection-management framework developed by the [Roy Rosenzweig Center for History and New Media](http://chnm.gmu.edu/), Neatline adds a digital map-making environment that makes it easy to represent geospatial information as a collection of "records" plotted on a map, which can be bound together into interactive exhibits that tell stories and make arguments.

Designed for scholars, archivists, journalists, and students, Neatline provides a flexible set of tools that can be adapted to fit the needs of a wide range of digital mapping projects. In addition to the core content management system, Neatline exposes a flexible programming API and "sub-plugin" system makes it easy for developers to add custom functionality for specific projects - everything from simple UI widgets up to really elaborate modifications that extend the core data model and add completely new interactions.

  - For general information and demos, head over to **[neatline.org](http://neatline.org/)**.

  - Read the docs at **[docs.neatline.org](http://docs.neatline.org/)**.

  - If you found a bug or thought of a new feature, file a ticket on the **[issue tracker](https://github.com/scholarslab/Neatline/issues)**.
CKEditor 4 - Releases
=====================

## Releases Code

This repository contains the official release versions of [CKEditor](http://ckeditor.com).

There are four versions for each release &mdash; `standard-all`, `basic`, `standard`, and `full`.
They differ in the number of plugins that are compiled into the main `ckeditor.js` file as well as the toolbar configuration.

See the [comparison](http://ckeditor.com/presets) of the `basic`, `standard`, and `full` installation presets for more details.

The `standard-all` build includes all official CKSource plugins with only those from the `standard` installation preset compiled into the `ckeditor.js` file and enabled in the configuration. 

All versions available in this repository were built using [CKBuilder](http://ckeditor.com/builder), so they are optimized and ready to be used in a production environment.

## Documentation

Developer documentation for CKEditor is available online at: <http://docs.ckeditor.com>.

## Installation

### Git clone

To install one of the available releases, just clone this repository and switch to the respective branch (see next section):

	git clone -b <release branch> git://github.com/ckeditor/ckeditor-releases.git
	
### Git submodule

If you are using git for your project and you want to integrate CKEditor, we recommend to add this repository as a
[submodule](http://git-scm.com/book/en/Git-Tools-Submodules).

	git submodule add -b <release branch> git://github.com/ckeditor/ckeditor-releases.git <clone dir>
	git commit -m "Added CKEditor submodule in <clone dir> directory."

### Using Package Managers

See the [Installing CKEditor with Package Managers](http://docs.ckeditor.com/#!/guide/dev_package_managers) article for more details about installing CKEditor with Bower and Composer.

## Repository Structure

### Branches

This repository contains the following branches:

  - `master` and `latest` &ndash; the latest release of the `standard-all` preset (including betas).
  - `stable` &ndash; the latest stable release of the `standard-all` preset (non-beta).
  - `A.B.x` (e.g. `4.3.x`) &ndash; the latest release of the `standard-all` preset in the `A.B` branch.
  - `(basic|standard|full)/stable` &ndash; the latest stable release tag point (non-beta).
  - `(basic|standard|full)/latest` &ndash; the latest release tag point (including betas).
  - `(basic|standard|full)/A.B.x` (e.g. `basic/4.0.x`) &ndash; the latest releases in the `A.B` branch.

### Tags

**Since version 4.3.3** this repository uses the following tag naming rules:

  - `x.y.z` &ndash; contains the `standard-all` editor build, e.g. `4.3.3`, `4.4.0` etc.
  - `(basic|standard|full)/x.y.z` &ndash; contains the editor build with a given preset, e.g. `basic/4.3.3`.

The version numbers follow the [Semantic Versioning 2.0.0](http://semver.org/) scheme.

Up to version **4.3.2** the tags were released in the following form `x.y[.z]/(basic|standard|full)`.
For example: `4.0/basic`, `4.0.1/standard`. This convention was changed in CKEditor 4.3.3 to conform to the Semantic Versioning scheme.

## Checking Your Installation

The editor comes with a few sample pages that can be used to verify if the installation succeeded. Take a look at the `samples` directory.

To test your installation, just call the following page for your website:

	http://<your site>/<CKEditor installation path>/samples/index.html

For example:

	http://www.example.com/ckeditor/samples/index.html

### License

Licensed under the GPL, LGPL, and MPL licenses, at your choice.

Please check the `LICENSE.md` file for more information about the license.CKEditor SCAYT Plugin
=====================

This plugin brings Spell Check As You Type (SCAYT) into up to CKEditor 4+.

SCAYT is a "installation-less", using the web-services of [WebSpellChecker.net](http://www.webspellchecker.net/). It's an out of the box solution.

Installation
------------

1. Clone/copy this repository contents in a new "plugins/scayt" folder in your CKEditor installation.
2. Enable the "scayt" plugin in the CKEditor configuration file (config.js):

        config.extraPlugins = 'scayt';

That's all. SCAYT will appear on the editor toolbar and will be ready to use.

License
-------

Licensed under the terms of any of the following licenses at your choice: [GPL](http://www.gnu.org/licenses/gpl.html), [LGPL](http://www.gnu.org/licenses/lgpl.html) and [MPL](http://www.mozilla.org/MPL/MPL-1.1.html).

See LICENSE.md for more information.

Developed in cooperation with [WebSpellChecker.net](http://www.webspellchecker.net/).
CKEditor WebSpellChecker Plugin
===============================

This plugin brings Web Spell Checker (WSC) into CKEditor.

WSC is "installation-less", using the web-services of [WebSpellChecker.net](http://www.webspellchecker.net/). It's an out of the box solution.

Installation
------------

1. Clone/copy this repository contents in a new "plugins/wsc" folder in your CKEditor installation.
2. Enable the "wsc" plugin in the CKEditor configuration file (config.js):

        config.extraPlugins = 'wsc';

That's all. WSC will appear on the editor toolbar and will be ready to use.

License
-------

Licensed under the terms of any of the following licenses at your choice: [GPL](http://www.gnu.org/licenses/gpl.html), [LGPL](http://www.gnu.org/licenses/lgpl.html) and [MPL](http://www.mozilla.org/MPL/MPL-1.1.html).

See LICENSE.md for more information.

Developed in cooperation with [WebSpellChecker.net](http://www.webspellchecker.net/).
OmekaApiImport
=====================

Use Omeka 2.1's API to do an Omeka site-to-site import

Background
----------

Omeka 2.1 introduced an API onto records, including Items, Collections, Elements, and more. Plugins can 
also add their records to the API. The API is located at `youromekasite.org/api`, and can be turned on under 
`Admin->Settings->Api`.

This plugin uses the API to import data from one Omeka site with an active API into another Omeka site.

Usage
-----

Install the plugin in the usual way. Click the `Omeka Api Import` tab in the admin screen. Enter the API URL of the
site from which you want to import data.

Optionally, enter the API you have for the external Omeka site. This will have to be provided by an administrator
of that site. If your key provides sufficient permissions, this will allow Users and non-public Items and
Collections to be imported

Element Sets will be imported. If the external site has edited the comments for Elements, you can check the box to
override the comments that exist in your site. This is only recommended if you are importing into an empty Omeka site.

Examples
--------

For converting data from the API to CSV, look at [OmekaApiToCsv](https://github.com/patrickmj/OmekaApiToCsv) and [Omekadd](https://github.com/wcaleb/omekadd)
# NeatlineSimile

Neatline Simile makes it possible to add the [SIMILE Timeline][simile] widget to Neatline exhibits. Once the timeline has been added, records can be plotted as points and spans on the timeline, and the timeline can be used to control the _visibility_ of records on the map (and in other viewports added by sub-plugins, like the [Waypoints][waypoints] list).

For example, if a record is plotted as a point on the map and has a "After Date" of 1500 and an "Before Date" of 1600, the record will be visible when only the timeline is between those two dates, and will be automatically hidden as soon as it is dragged before 1500 or after 1600. This makes it possible to string together complex time-series sequences and animations that show how things change over time.

## Installation

  1. Download the latest version of the plugin from the Omeka add-ons repository.

  1. Uncompress the `.zip` archive.

  2. Move the `NeatlineSimile` into the `/plugins` folder in you Omeka installation.

  3. In the Omeka administrative interface, click on **Plugins** in the top navigation bar and find the listing for "Neatline Widget ~ SIMILE Timeline". Click on "Install."

  **Note**: Since NeatlineSimile is a "sub-plugin" that extends the core functionality of Neatline (itself a plugin), Neatline has to be installed in order to install NeatlineSimile.

## Usage

### Enabling the widget

NeatlineSimile adds a "widget" to your installation of Neatline that can be turned on and off for each individual exhibit. Widgets can be activated when an exhibit is first created or by clicking on the "Exhibit Settings" link for an exhibit in the main browse view, which opens the same form that is dispalyed when the exhibit is created. In either case:

  1. Scroll down to the "Widgets" field. Click on the input box to display a list of available widgets.

  2. Click on the listing for "SIMILE Timeline." Once selected, the listing will be displayed as a box in the input.

  3. To lock in the change, click "Save Exhibit" at the bottom of the form.

Now, when you open the editor for the exhibit, you'll see the timeline at the bottom right of the screen.

### Plotting points and spans

  1. Open the edit form for the record that you want to plot on the timeline (or create a new record).

  2. Open the **Style** tab and scroll down to the the "Dates" field set.

  3. Mark the record as being active on the timeline by clicking the listing for "SIMILE Timeline" in the list of options in the "Widgets" field.

  4. Enter a date in the "Start Date" field. **Important**: All dates must be entered in a portable, standards-compliant format called [ISO 8601][iso-8601]. For more detail, see the [Neatline documentation][date-docs]. If you just enter a value for "Start Date" and leave "End Date" empty, the record will be rendered as a single point (an instant) on the timeline.

  5. Optionally, enter an "End Date." If an end date is provided, the record will be rendered as a "duration" on the timeline - a line that runs between two dates.

  5. Click **Save** at the bottom of the form. The timeline will automatically update to display the new point.

### Setting visibility intervals

In addition to directly plotting records on the timeline, the timeline can also be used as a control mechanism that hides and displays records according to the "After Date" and "Before Date" fields, which define an interval of time within which records should be rendered in the exhibit. Records are filtered according to these rules:

  - If an "After Date" is defined, the record will be displayed whenever the timeline is centered on a date that falls after that date. For example, if "After Date" is 2000, the record will be visible when the timeline is at 2001, but invisible when it is at 1999.

  - Likewise, if a "Before Date" is defined, the record will be displayed whenever the timeline is centered on a date that falls before that date. For example, if "Before Date" is 2000, the record will be visible when the timeline is at 1999, but invisible when it is at 2001.

  - If both an "After Date" and a "Before Date" are provided, the record will only be visible when the timeline is inside of the interval defined by the two dates.

Once the timeline is enabled for an exhibit, this filtering is applied automatically to all records, regardless of whether or not they are plotted on the timeline itself.

### Editing timeline defaults

To adjust the default appearance, focus date, and zoom of the timeline:, click on the **Plugins** tab (to the right of "Records" and "Styles") and select the **SIMILE Timeline** option from the drop-down list.

#### Default Date

The date where the timeline is initially centered when the user first arrives at the exhibit. Like the date fields in the record edit form, this field takes any [ISO 8601][iso-8601] date.

#### Interval Unit

The unit of time represented by the tick marks on the timeline. In conjunction with the "Interval Pixels" setting, this is effectively the "zoom level" for the timeline - larger units will be more zoomed-out than smaller units.

#### Interval Pixels

The amount of space between the individual tick marks. This determines how zoomed-in the timeline is within the context of a given "Interval Unit." Click on the input and drag the cursor up and down on the page to change the value smoothly. As the value changes, the new setting will be automatically previewed on the timeline.

#### Track Height

When lots of records are plotted in close proximity on the timeline, the plottings will be stacked up vertically to prevent them from overlapping. This setting determines the amount of vertical space between the horizontal "tracks" on which events are positioned. Bump up this value to increase the amount of vertical "padding" between events.

#### Tape Height

The height of the horizontal "tapes" used to represent duration events on the timeline (events that have both a "Start Date" and an "End Date."

  
[simile]: http://www.simile-widgets.org/timeline/
[waypoints]: https://github.com/scholarslab/nl-widget-Waypoints
[iso-8601]: https://en.wikipedia.org/wiki/ISO_8601
[date-docs]: https://github.com/scholarslab/Neatline/blob/develop/docs/style-tab-dates.md
# SIMILE Timeline

Load SIMILE Timeline locally:

```html
<head>
  <script src="ajax/simile-ajax-api.js?bundle=true"></script>
  <script src="js/timeline-api.js?bundle=true"></script>
</head>
```
CSSTidy
---

CSSTidy is a CSS minifier 

v1.5.2
  is PHP 5.4+ compliant, removes use of GLOBALS, fixes some bugs, integrates CSS3 units
  and now available on https://packagist.org/packages/cerdic/css-tidy

v1.4 is the new version coming from master branch (corresponds to the initial trunk of svn repository) after beeing stabilized

v1.3 branch corresponds to the last stable relase published by the author.
It integrates some bugfixes and a 1.3.1 version has been taged
Since the original project (http://csstidy.sourceforge.net/index.php) has been suspended
here is the import of https://csstidy.svn.sourceforge.net/svnroot/csstidy on 2010-11-14

Only PHP version is here maintained

---

CSSTidy

Original Tracker : 
http://sourceforge.net/tracker/?group_id=148404&atid=771415

css_optimiser.php is the web-interface, css_parser.php contains the PHP class (CSSTidy).

This class represents a CSS parser which reads CSS code and saves it in an array.
In opposite to most other CSS parsers, it does not use regular expressions and
thus has full CSS2 support and a higher reliability. The downside of not using regular expressions
is a lower speed though.
Additional to that it applies some optimisations and fixes to the CSS code.
An online version should be available here: http://cdburnerxp.se/cssparse/css_optimiser.php


	Copyright 2005, 2006, 2007 Florian Schmitz

  CSSTidy is free software; you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation; either version 2.1 of the License, or
  (at your option) any later version.
  
  CSSTidy is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
CSST

These test are for CSSTidy's parsing algorithms. They take this form:

--TEST--
Test name
--CSS--
CSS to parse
--EXPECT--
var_export() representation of csstidy->css[41]

Note carefully that EXPECT is for csstidy->css[41], not csstidy->css. This
is because, by default, all declarations are placed inside the 
DEFAULT_AT section. For tests that need to make use of at selectors, use

--FULLEXPECT--
var_export() representation of csstidy->css

...instead.

See also: class.csstidy_csst.php (the implementation of these tests) and
test.csst.php (the caller stub for SimpleTest)
# PDF Embed #
## A plugin for Omeka ##

This is a simple plugin that uses either the browser's built-in or
plugin-added PDF display capabilities or Mozilla's [PDF.js][1] to embed
PDFs on item and file pages.

 [1]: http://mozilla.github.io/pdf.js/
Bulk Metadata Editor
=======

Bulk metadata search and replace for the Omeka platform
# [NeatlineText][plugin]

**NeatlineText** is a extension to the Neatline plugin that makes it possible to connect paragraphs, sentences, and words in text documents with annotations in Neatine exhibits.

For example, imagine you're making an interactive edition of Walt Whitman's "[Salut au Monde][salut-au-monde]," and want to wire up the locations in this passage with annotations on the map:

```
I see the tracks of the rail-roads of the earth;	 
I see them welding State to State, city to city, through North America;
I see them in Great Britain, I see them in Europe;	 
I see them in Asia and in Africa.
```

### Step 1: Create the Neatline records

First, create records in the Neatline exhibit for each of the geographic entities that you want to represent on the map - North America, Great Britain, etc. - and fill in the "Slug" field in the "Text" tab with some sort of semantic, easy-to-remember string:

![Slug](http://dclure.org/wp-content/uploads/2014/03/slug.jpg)

Think of the slug as a plain-text, human-readable identifier that can be used to reference the record in other contexts. Like, for instance, attributes in HTML markup! Which brings us to...

### Step 2: Create the HTML fragment

Fire up your favorite text editor, copy in the text document, and wrap sections of the text with elements with `data-neatline-slug` attributes that point at the record slugs:

```html
I see the tracks of the rail-roads of the earth;	 
I see them welding State to State, city to city, through <span data-neatline-slug="north-america">North America</span>;
I see them in <span data-neatline-slug="great-britain">Great Britain</span>, I see them in <span data-neatline-slug="europe">Europe</span>;	 
I see them in <span data-neatline-slug="asia">Asia</span> and in <span data-neatline-slug="africa">Africa</span>.
```

In this case we're using `<span>` elements, since we're wrapping little inline strings, but you could add the `data-neatline-slug` attributes to any element at all - `<p>`'s, `<div>`'s, etc. The plugin doesn't care - it just queries for the existence of the attribute, not the element type.

### Step 3: Copy the HTML into the exhibit

Once the markup is ready, just paste it into the "Narrative" input in the exhibit's edit form. Be sure to put the text editor in "Source" mode, since we're copying in raw HTML markup:

![Narrative](http://dclure.org/wp-content/uploads/2014/03/narrative.jpg)

And that's it. Now, when you open up the exhibit, NeatlineText will automatically wire up bi-directional connections between the spans in the text document and the corresponding records in Neatline. Out of the box, the plugin implements two basic interactions:

  - **Highlighting**: When the user hovers the cursor over a span in the text, any corresponding objects in the Neatline exhibit (shapes on the map, waypoints, etc.) will be highlighted. And vice versa - when the cursor hovers on an object in the exhibit, the span(s) in the text will highlight.

  - **Selecting**: When the user clicks on a span in the text, the Neatline exhibit will "focus" around the corresponding record in the exhibit - the map will pan and zoom to frame the annotation, the timeline will scroll to show the span, etc. And likewise, when the user selects a record in the Neatline exhibit, the text will automatically scroll to display the corresponding span.

## Theming

Unlike other Neatline extensions like Waypoints and SIMILE, NeatlineText needs to be used in conjunction with a theme that positions the text next to the exhibit inside of a scrollable container element. By default, most themes just display the exhibit narrative above or below the exhibit, which means that the user would need to manually scroll up and down on the page to compare the exhibit with the text, which defeats the purpose.

There are two ways to go about this:

  - **Omeka themes**: To make it easy to get up and running, we've built a really simple started theme called [Neatlight][neatlight], which is specifically designed to house NeatlineText exhibits. Think of Neatlight as the Neatline equivalent of the default "Thanks Roy" theme that ships with Omeka - it's a simple, no-frills foundation that can be easily adapted and expanded.

  - **Neatline themes**: The other approach is to use Neatline's exhibit-specific themeing system, which makes it possible to create completely separate themes for each individual Neatline exhibit. For more information about this, check out the documentation, and take a look at [David McClure's fork of the Neatlight theme][neatlight-mcclure], which contains the source code for the custom themes used in projects at [neatline.dclure.org][neatline-dclure]. 

[plugin]: http://omeka.org/add-ons/plugins/neatlinetext
[salut-au-monde]: http://www.bartelby.com/142/74.html
[neatlight]: https://github.com/scholarslab/neatlight
[neatlight-mcclure]: https://github.com/davidmcclure/neatlight/tree/master/neatline/exhibits/themes
[neatline-dclure]: http://neatline.dclure.org
# Hide Elements #
## A plugin for Omeka ##

This plugin lets administrators choose metadata elements to hide.
Elements can separately be hidden from the edit form, display on the
admin side, display on the public side, and the search form.

### Version History

*1.3*

* Added initial support for Omeka 2.2.
* Fixed hiding on search for localized sites.
* Minor interface improvements (thanks @miniol)

*1.2*

* Added support for hiding elements from items advanced search.
* Added configurable overriding of hide selections by role.

*1.1*

* Fixed hiding of Item Type metadata elements for display.

*1.0*

* Initial release.

# Google Analytics Omeka Plugin

This Omeka plugin allows you to include the JavaScript for Google Analytics at
the bottom of any page.

To get set up for Google Analytics, visit [Google
Analytics](https://www.google.com/analytics/).  You may need to set up an
account and a profile for your Omeka site.

Once you've done that, install this plugin (see [Managing
Plugins](http://omeka.org/codex/Managing_Plugins) for more information). On the
configuration screen, you will need to paste in the Google Analytics
JavaScript. You can do that by following these steps:

 1. Log onto [Google Analytics](https://www.google.com/analytics/);

 2. Click "Edit" for the profile you wish to use;

 3. Click "Check Status" (it will be a small link near the top of the page);

 4. Copy all of the text in the box labelled "Paste this code on your site";
    and

 5. Paste it into the box on the plugin configuration page.

That's it. You should start seeing results in Google Analytics in 24-48 hours.

# NeatlineWaypoints

NeatlineWaypoints makes it possible to add an list of clickable "waypoints" to an exhibit. Waypoints can be put into a specific order, making it possible to guide users through an exhibit in a linear sequence.

## Installation

  1. Download the latest version of the plugin from the Omeka add-ons repository.

  1. Uncompress the `.zip` archive.

  2. Move the `NeatlineSimile` into the `/plugins` folder in you Omeka installation.

  3. In the Omeka administrative interface, click on **Plugins** in the top navigation bar and find the listing for "Neatline Widget ~ Waypoints". Click on "Install."

  **Note**: Since NeatlineWaypoints is a "sub-plugin" that extends the core functionality of Neatline (itself a plugin), Neatline has to be installed in order to install NeatlineWaypoints.

## Usage

### Enabling the widget

NeatlineWaypoints adds a "widget" to your installation of Neatline that can be turned on and off for each individual exhibit. Widgets can be activated when an exhibit is first created or by clicking on the "Exhibit Settings" link for an exhibit in the main browse view, which opens the same form that is dispalyed when the exhibit is created. In either case:

  1. Scroll down to the "Widgets" field. Click on the input box to display a list of available widgets.

  2. Click on the listing for "Waypoints." Once selected, the listing will be displayed as a box in the input.

  3. To add the widget, click "Save Exhibit" at the bottom of the form.

### Adding waypoints

Once you've enabled the widget for an exhibit, individual records can be added to the waypoints panel, a small list of record titles displayed at the top right of the screen:

  1. Open the edit form for the record you want to add to the list of waypoints.

  2. Open the **Style** tab and find the "Widgets" field in the "Groups" field set.

  3. Activate the "Waypoints" option.

  4. Click the "Save" button at the bottom of the form.

As soon as a record is added, the list of waypoints will automatically update to include the new listing.

### Ordering waypoints

To change the order of the listings in the waypoints panel, click on the **Plugins** tab in the editor and select the **Waypoints** in the drop-down menu. To change the order, just click on any of the waypoints in the list and drag it up or down. When you're done, click the "Save" button to commit the change.
# Embed Codes

## Description

Embed codes adds a HTML code for others to embed information about the item in other web pages. The title, thumbnail, and, if set, the rights information is displayed with a link back to the original site. 

Data about other sites where the item has been embedded and the number of page views is available in the admin side. 

This is useful for sites that want to encourage external writing or presentations about their content and would like to gather information about where and how their content is being reused.

## Installation

Copy the files to the plugins directory, and install from the Omeka plugins page# Welcome to Omeka

© 2008-2015 [Roy Rosenzweig Center for History and New Media](http://chnm.gmu.edu/)

This program is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).

Omeka includes:

* [Zend Framework](http://framework.zend.com)
* [getID3](http://getid3.sourceforge.net)
* [jQuery](http://jquery.com)
* [jQuery UI](http://jqueryui.com)
* [TinyMCE](http://tinymce.moxiecode.com)
* [Silk Icons](http://www.famfamfam.com/lab/icons/silk/)

Use and modifications of these libraries must comply with their respective 
licenses.

Release notes for Omeka are available at
[http://omeka.org/codex/Release_Notes](http://omeka.org/codex/Release_Notes).
This is a dummy file to prevent Git from ignoring this empty directory.

    vim: et sw=4 sts=4
