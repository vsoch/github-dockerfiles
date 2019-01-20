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

Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.

Licensed under the terms of any of the following licenses at your choice: [GPL](http://www.gnu.org/licenses/gpl.html), [LGPL](http://www.gnu.org/licenses/lgpl.html) and [MPL](http://www.mozilla.org/MPL/MPL-1.1.html).

See LICENSE.md for more information.
A jQuery plugin to create a URL slug as you type a page title (like Django slugify())

Say you have form that looks like this:

    <label for="title">Title, e.g. "My Cool Blog Post"</label>
    <input type="text" name="title" id="title">
    ...

    <label for="slug">Slug, e.g. "my-cool-blog-post"</label>
    <input type="text" name="slug" id="slug">

Use slugify() to automatically fill out the slug field as the user types a title.

    $('#slug').slugify('#title');

More docs and live examples at http://patrickmcelhaney.com/jQuery-Slugify-PluginGo to the <a href="https://github.com/Gizra/restful">project page</a> in GitHub.
<h2>Om denne oversettelsen</h2>

<p>Dette er en (delvis) oversettelse til <em>norsk</em> (bokmål) av
hjelpeteksene for <strong>Avansert hjelp</strong>.  Den er i første
rekke laget for å vise hvordan en oversettelse av hjelpetekstene ser
ut.</p>

<h2 id="project-description">Synopsis</h2>

<p>Modulen <strong>Avansert hjelp</strong> tilbyr et rammeverk som gjør
det mulig for modul- og theme-utviklere å integrere hjelpetekster i et
Drupal-nettsted.</p>

<p>Disse hjelpetekstene lagres som vanlige <code>.html</code>-filer
som lever i filsystemet (ikke i databasen).  Disse filene distribueres
fra prosjektes repo på Drupal.org i den samme pakken som prosjektets
øvrige filer, og plasseres i en en underkatalog med navnet
<code>help</code> i prosjektets katalog.  Det innebærer at
hjelpetekstene på en enkel måte kan holdes synkronisert med det
prosjektet hjelpen er knyttet til, men også at tilgangen til disse
filene ikke er underlagt de tilgangsbegrensningene som Drupal
administrerer.</p>

<p>Hjelpetekstene kan bruke standard HTML-markeringer De vil bli vist
med ditt nettsteds theme.</p>

<p>Dersom prosjektets forfatter ikke bruker HTML-rammeverket for
<em>Avansert hjelp</em>, men det finnes en 
<code>README.md</code> eller <code>README.txt</code> i pakken,
så vil innholdet av den filen vises i stedet.</p>
  
<p>Hjelpetekstene kan vises i et sprettopp-vindu eller ikke, ut fra
prosjektets preferanser.  Ved å fjerne tilgangen til å se
sprettopp-vinduer kan nedstedet skjule sprettopp-vinduer fra
brukere.</p>

<p>Hjelpetekstene kan organiseres hierarkisk, noe som gjør det mulig
og navigere fra toppen av og nedover for hjelp.</p>

<p>Hjelpetekstene kan gjøres søkbare.  Dersom søk av avansert hjelp er
slått på, vil all hjelpetekst indekseres. Dette innebærer at alt
innhold på sidene med avansert hjelp er søkbart med nøkkelord.</p>

<h2 id="use">Bruk av modulen</h2>

<p>When you enable the module, a new tab with the legend “Advanced
help” will show up under “Help”:

<div class="ta-center">
<img class="help-img-center" alt="ahelp_tab.png" src="&path&ahelp_tab.png" width="661" height="225" border="1" />
</div>

<p>By itself, this module doesn't do much.  The <strong>Avansert
hjelp</strong> assists other modules and themes in showing help texts.
Nothing will show up until you enable at least one other module that
makes use of the advanced help framework or comes with a file
named <code>README.md</code> or <code>README.txt</code>.  However, it
comes with a small companion demo module named
<strong>Eksempel på hjelp</strong> to demonstrate how it works.
For more extensive example of use of the advanced help features, see
the <strong>Views</strong> project.</p>

<!--
<h2 id="project-recommended">Anbefalte moduler</h2>

<ul>
<li><a href="https://www.drupal.org/project/markdown">Markdown filter</a>:<br>
When this module is enabled, display of any <code>README.md</code> the
module shows will be rendered with markdown.</li>
<li><a href="https://www.drupal.org/project/attributions">Attributions</a>:<br>
When this module is enabled, attributions of third party content used
by the project (i.e. some text from Wikipedia) will be available in an
attribution block and on an atribution page.</li>
</ul>
-->

<h2 id="support-status">Status for oppfølging</h2>

<p>Reported bugs for the Drupal 7 branch will be fixed in a timely
manner.  Bugs in the issue queue for the Drupal 6 branch will only be
fixed if accompanied with a patch, after the patch has been reviewed
and tested by the community.  No Drupal 8 version is currently under
development.  Post a message in
the <a href="https://www.drupal.org/node/1928218">issue queue</a> if
you're interested in managing a port of the project to to Drupal
8. Older versions are no longer supported.</p>

<p>Community support in the form of patches are very welcome for both
Drupal 6 and Drupal 7 versions, and will be given priority. For QA,
the project needs community support in the form of reviews of patches,
development versions and releases.</p>

<p>The primary goal of the module is to remain <strong>light-weight
and simple</strong>.  This means that not all feature requests will be
implemented, even if they are a good idea.  Feature requests
accompanied by patches are more likely to make it into a release.</p>

<p>The maintainer hopes that the community is willing to help out by
answering &amp; closing support requests.</p>

<!--
<h2 id="project-problems">Kjente problemer</h2>
-->



<h2 id="project-maintainers">Kreditering</h2>

<ul>
<li><a href="https://www.drupal.org/u/merlinofchaos"">merlinofchaos</a> (52 commits, opprinnelig forfatter)</li>
<li><a href="https://www.drupal.org/u/redndahead">redndahead</a> (8 commits)</li>
<li><a href="https://www.drupal.org/u/dmitrig01">dmitrig01</a> (3 commits)</li>
<li><a href="https://www.drupal.org/u/amitgoyal">amitgoyal </a> (5 commits)</li>
<li><a href="https://www.drupal.org/u/gisle">gisle</a> (nåværende administrator, D7)</li>
<li><a href="https://www.drupal.org/u/gnuget">gnuget</a> (nåværende administrator, D8)</li>
</ul>
<h2 id="project-description">Synopsis</h2>

<p>The <strong>Advanced help</strong> module provides a framework that allows
module and theme developers integrate help texts in a Drupal site.</p>

<p>These help texts are stored in ordinary <code>.html</code>-files
that lives in the file system (as opposed to the database).  These
files are distributed from the project Drupal.org repo in the same
package as the module or theme, and placed in a subdirectory named
<code>help</code> in the project or theme directory.  This means that
the help texts can be easiely kept in sync with the project they
provide help texts for, but also that read access to these files
are not managed by any content access restrictions imposed by Drupal.</p>
  
<p>The help texts can be marked up with standard HTML. They will be
rendered using your site's theme.</p>

<p>If the module or theme author does not make use of the
<em>Advanced help</em> HTML-framework, but if there is a
<code>README.md</code> or <code>README.txt</code> in the package,
the content of that file will be shown instead.</p>
  
<p>The help texts may appear in a popup or not as the project prefers.
By taking away access to view the popups, a site can hide popups from
users.</p>

<p>The help texts can be placed in a hierarchy, allowing for top down
navigation of help.</p>

<p>The help texts may be made searchable. If advanced help search is
enabled, all help texts are fully indexed. This means that the entire
contents of the advanced help set of pages can be searched for
keywords.</p>

<h2 id="use">Using the module</h2>

<p>When you enable the module, a new tab with the legend “Advanced
help” will show up under “Help”:

<div class="ta-center">
<img class="help-img-center" alt="ahelp_tab.png" src="&path&ahelp_tab.png" width="661" height="225" border="1" />
</div>

<p>By itself, this module doesn't do much.  The <strong>Advanced
help</strong> assists other modules and themes in showing help texts.
Nothing will show up until you enable at least one other module that
makes use of the advanced help framework or comes with a file
named <code>README.md</code> or <code>README.txt</code>.  However, it
comes with a small companion demo module named
<strong>Advanced help example</strong> to demonstrate how it works.
For more extensive example of use of the advanced help features, see
the <strong>Views</strong> project.</p>

<!--
<h2 id="project-recommended">Recommended modules</h2>

<ul>
<li><a href="https://www.drupal.org/project/markdown">Markdown filter</a>:<br>
When this module is enabled, display of any <code>README.md</code> the
module shows will be rendered with markdown.</li>
<li><a href="https://www.drupal.org/project/attributions">Attributions</a>:<br>
When this module is enabled, attributions of third party content used
by the project (i.e. some text from Wikipedia) will be available in an
attribution block and on an atribution page.</li>
</ul>
-->

<h2 id="support-status">Support status</h2>

<p>Reported bugs for the Drupal 7 branch will be fixed in a timely
manner.  Bugs in the issue queue for the Drupal 6 branch will only be
fixed if accompanied with a patch, after the patch has been reviewed
and tested by the community.  No Drupal 8 version is currently under
development.  Post a message in
the <a href="https://www.drupal.org/node/1928218">issue queue</a> if
you're interested in managing a port of the project to to Drupal
8. Older versions are no longer supported.</p>

<p>Community support in the form of patches are very welcome for both
Drupal 6 and Drupal 7 versions, and will be given priority. For QA,
the project needs community support in the form of reviews of patches,
development versions and releases.</p>

<p>The primary goal of the module is to remain <strong>light-weight
and simple</strong>.  This means that not all feature requests will be
implemented, even if they are a good idea.  Feature requests
accompanied by patches are more likely to make it into a release.</p>

<p>The maintainer hopes that the community is willing to help out by
answering &amp; closing support requests.</p>

<!--
<h2 id="project-problems">Known problems</h2>
-->



<h2 id="project-maintainers">Credits</h2>

<ul>
<li><a href="https://www.drupal.org/u/merlinofchaos"">merlinofchaos</a> (52 commits, original creator)</li>
<li><a href="https://www.drupal.org/u/redndahead">redndahead</a> (8 commits)</li>
<li><a href="https://www.drupal.org/u/dmitrig01">dmitrig01</a> (3 commits)</li>
<li><a href="https://www.drupal.org/u/amitgoyal">amitgoyal </a> (5 commits)</li>
<li><a href="https://www.drupal.org/u/gisle">gisle</a> (current maintainer, D7)</li>
<li><a href="https://www.drupal.org/u/gnuget">gnuget</a> (current maintainer, D8)</li>
</ul>
Go to the <a href="https://github.com/Gizra/restful">project page</a> in GitHub.
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
        
        This can be conditionally restricted per role using the user permission
        "Access View changes button".
  
    ii) "Enable the Revisions page for this content type" adds the revisioning
         tab to content. This allows users to compare between various revisions
         that they have access to.
  
    iii) "Standard comparison preview" option allows you to control how the most
          current revision is shown on the revision comparison page.
       
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
This directory should be used to place downloaded and custom libraries (such as
JavaScript libraries) which are used by contributed or custom modules.
## CSV.js

Simple javascript CSV library focused on the browser with **zero
dependencies**.

Originally developed as part of [ReclineJS][] but now fully standalone.

[ReclineJS]: http://okfnlabs.org/recline/

## Usage

Grab the `csv.js` file and include it in your application.

Depends on jQuery or underscore.deferred (for deferred) in fetch (and jQuery if
you need ajax). `parse` and `serialize` have zero dependencies.

### fetch

A convenient way to load a CSV file from various different sources. fetch
supports 3 options depending on the attribute provided on the info argument:

    CSV.fetch({
        data: 'raw csv string'
        // or ...
        url: 'url to a csv file'
        // or ...
        file: an HTML 5 file object

        // optional options about structure of the CSV file
        // following the CSV Dialect Description Format 
        // http://dataprotocols.org/csv-dialect/
        dialect: {
          ...
        }
      }
    ).done(function(dataset) {
      // dataset object doc'd below
      console.log(dataset);
    });

Some more detail on the argument object:

* `data` is a string in CSV format. This is passed directly to
  the CSV parser
* `url`: a url to an online CSV file that is ajax accessible (note this
  usually requires either local or on a server that is CORS enabled). The file
  is then loaded using jQuery.ajax and parsed using the CSV parser (NB: this
  requires jQuery) All options generates similar data and use the memory store
  outcome, that is they return something like:
* `file`: is an HTML5 file object. This is opened and parsed with the CSV
  parser.
* `dialect`: hash / dictionary following the same structure as for `parse`
  method below.

[csvddf]: http://dataprotocols.org/csv-dialect/

Returned `dataset` object looks like:

<pre>
{
  // an array of arrays - one array each row in the CSV
  // (excluding header row - i.e. first row)
  records: [ [...], [...], ... ],
  // list of fields
  fields: [ 'field-name-1', 'field-name-2', ... ],
  metadata: { may be some metadata e.g. file name }
}
</pre>

### Raw parsing

    var out = CSV.parse(csvString, dialect);

Converts a Comma Separated Values string into an array of arrays.  Each line in
the CSV becomes an array.

Empty fields are converted to nulls and non-quoted numbers are converted to
integers or floats.

* `csvString`: the csv string to parse
* `dialect`: [optional] hash with keys as per the [CSV dialect description
  format][csvddf]. It also supports the following additional keys:

  * `skipInitialRows`: [optional] integer number of rows to skip (default 0)

  For backwards compatability with earlier versions of the library the `dialect`
  also supports the following:

  * `trim`: mapped to `skipInitialSpace` in [CSV dialect description
    format][csvddf]

### Serialize

Convert an Object or a simple array of arrays into a Comma
Separated Values string.

    var out = CSV.serialize(dataToSerialize, dialect);

Returns a string representing the array serialized as a CSV.

`dataToSerialize` is an Object or array of arrays to convert. Object structure
must be as follows:

    {
      fields: [ {id: .., ...}, {id: ..., 
      records: [ { record }, { record }, ... ]
      ... // more attributes we do not care about
    }

  Nulls are converted to empty fields and integers or floats are converted to
  non-quoted numbers.

* `dialect`: dialect options for serializing the CSV file as per [CSV Dialect
  Description Format][csvddf]

----

## Other JS CSV Libs

* http://www.uselesscode.org/javascript/csv/ - basic CSV parser on which this library was originally based 
* https://github.com/maxogden/browser-csv-stream - Pure browser version of node-csv from @maxogden via browserify 
* https://github.com/onyxfish/csvkit.js - pure JS CSV reader from @onyxfish (author of the "legendary" python csvkit)

### Node

* https://github.com/wdavidw/node-csv - this is the Node CSV lib we use by preference
* https://github.com/maxogden/binary-csv - new CSV lib from @maxogden with a focus on being very fast

<img src="http://leafletjs.com/docs/images/logo.png" alt="Leaflet" />

Leaflet is an open source JavaScript library for **mobile-friendly interactive maps**.
It is developed by [Vladimir Agafonkin][] of [MapBox][] with a team of dedicated [contributors][].
Weighing just about 30 KB of gzipped JS code, it has all the [features][] most developers ever need for online maps.

Leaflet is designed with *simplicity*, *performance* and *usability* in mind.
It works efficiently across all major desktop and mobile platforms out of the box,
taking advantage of HTML5 and CSS3 on modern browsers while being accessible on older ones too.
It can be extended with a huge amount of [plugins][],
has a beautiful, easy to use and [well-documented][] API
and a simple, readable [source code][] that is a joy to [contribute][] to.

For more info, docs and tutorials, check out the [official website][].<br>
For **Leaflet downloads** (including the built master version), check out the [download page][].

We're happy to meet new contributors.
If you want to **get involved** with Leaflet development, check out the [contribution guide][contribute].
Let's make the best mapping library that will ever exist,
and push the limits of what's possible with online maps!

[![Build Status](https://travis-ci.org/Leaflet/Leaflet.png?branch=master)](https://travis-ci.org/Leaflet/Leaflet)

 [Vladimir Agafonkin]: http://agafonkin.com/en
 [contributors]: https://github.com/Leaflet/Leaflet/graphs/contributors
 [features]: http://leafletjs.com/features.html
 [plugins]: http://leafletjs.com/plugins.html
 [well-documented]: http://leafletjs.com/reference.html "Leaflet API reference"
 [source code]: https://github.com/Leaflet/Leaflet "Leaflet GitHub repository"
 [hosted on GitHub]: http://github.com/Leaflet/Leaflet
 [contribute]: https://github.com/Leaflet/Leaflet/blob/master/CONTRIBUTING.md "A guide to contributing to Leaflet"
 [official website]: http://leafletjs.com
 [download page]: http://leafletjs.com/download.html
 [MapBox]: https://mapbox.com
# Important
Leaflet.draw 0.2.3+ requires [Leaflet 0.7](https://github.com/Leaflet/Leaflet/archive/v0.7.zip) or higher.

#Leaflet.draw
Adds support for drawing and editing vectors and markers on [Leaflet maps](https://github.com/Leaflet/Leaflet). Check out the [demo](http://leaflet.github.com/Leaflet.draw/).

#### Upgrading from Leaflet.draw 0.1

Leaflet.draw 0.2.0 changes a LOT of things from 0.1. Please see [BREAKING CHANGES](https://github.com/Leaflet/Leaflet.draw/blob/master/BREAKINGCHANGES.md) for how to upgrade.

## Table of Contents
[Using the plugin](#using)  
[Advanced Options](#options)  
[Common tasks](#commontasks)  
[Thanks](#thanks)

<a name="using" />
## Using the plugin

The default state for the control is the draw toolbar just below the zoom control. This will allow map users to draw vectors and markers. **Please note the edit toolbar is not enabled by default.**

To add the draw toolbar set the option `drawControl: true` in the map options.

````js
// create a map in the "map" div, set the view to a given place and zoom
var map = L.map('map', {drawControl: true}).setView([51.505, -0.09], 13);

// add an OpenStreetMap tile layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
````

### Adding the edit toolbar

To use the edit toolbar you must initialise the Leaflet.draw control and manually add it to the map.

````js
// create a map in the "map" div, set the view to a given place and zoom
var map = L.map('map').setView([51.505, -0.09], 13);

// add an OpenStreetMap tile layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Initialise the FeatureGroup to store editable layers
var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);

// Initialise the draw control and pass it the FeatureGroup of editable layers
var drawControl = new L.Control.Draw({
	edit: {
		featureGroup: drawnItems
	}
});
map.addControl(drawControl);
````

The key here is the `featureGroup` option. This tells the plugin which `FeatureGroup` contains the layers that should be editable.

### Events

Once you have successfully added the Leaflet.draw plugin to your map you will want to respond to the different actions users can initiate. The following events will be triggered on the map:

#### draw:created

| Property | Type | Description
| --- | --- | ---
| layer | [Polyline](http://leafletjs.com/reference.html#polyline)/[Polygon](http://leafletjs.com/reference.html#polygon)/[Rectangle](http://leafletjs.com/reference.html#rectangle)/[Circle](http://leafletjs.com/reference.html#circle)/[Marker](http://leafletjs.com/reference.html#marker) | Layer that was just created.
| layerType | String | The type of layer this is. One of: `polyline`, `polygon`, `rectangle`, `circle`, `marker`


Triggered when a new vector or marker has been created.

````js
map.on('draw:created', function (e) {
	var type = e.layerType,
		layer = e.layer;

	if (type === 'marker') {
		// Do marker specific actions
	}

	// Do whatever else you need to. (save to db, add to map etc)
	map.addLayer(layer);
});
````

#### draw:edited

| Property | Type | Description
| --- | --- | ---
| layers | [LayerGroup](http://leafletjs.com/reference.html#layergroup) | List of all layers just edited on the map.

Triggered when layers in the FeatureGroup, initialised with the plugin, have been edited and saved.

````js
map.on('draw:edited', function (e) {
	var layers = e.layers;
	layers.eachLayer(function (layer) {
		//do whatever you want, most likely save back to db
	});
});
````

#### draw:deleted

Triggered when layers have been removed (and saved) from the FeatureGroup.

| Property | Type | Description
| --- | --- | ---
| layers | [LayerGroup](http://leafletjs.com/reference.html#layergroup) | List of all layers just removed from the map.

#### draw:drawstart

Triggered when the user has chosen to draw a particular vector or marker.

| Property | Type | Description
| --- | --- | ---
| layerType | String | The type of layer this is. One of: `polyline`, `polygon`, `rectangle`, `circle`, `marker`

#### draw:drawstop

Triggered when the user has finished a particular vector or marker.

| Property | Type | Description
| --- | --- | ---
| layerType | String | The type of layer this is. One of: `polyline`, `polygon`, `rectangle`, `circle`, `marker`

#### draw:editstart

Triggered when the user starts edit mode by clicking the edit tool button.

| Property | Type | Description
| --- | --- | ---
| handler | String | The type of edit this is. One of: `edit`

#### draw:editstop

Triggered when the user has finshed editing (edit mode) and saves edits.

| Property | Type | Description
| --- | --- | ---
| handler | String | The type of edit this is. One of: `edit`

#### draw:deletestart

Triggered when the user starts remove mode by clicking the remove tool button.

| Property | Type | Description
| --- | --- | ---
| handler | String | The type of edit this is. One of: `remove`

#### draw:deletestop

Triggered when the user has finished removing shapes (remove mode) and saves.

| Property | Type | Description
| --- | --- | ---
| handler | String | The type of edit this is. One of: `remove`

<a name="options" />
## Advanced options

You can configure the plugin by using the different options listed here.

### Control.Draw

These options make up the root object that is used when initialising the Leaflet.draw control.

| Option | Type | Default | Description
| --- | --- | --- | ---
| position | String | `'topleft'` | The initial position of the control (one of the map corners). See [control positions](http://leafletjs.com/reference.html#control-positions).
| draw | [DrawOptions](#drawoptions) | `{}` | The options used to configure the draw toolbar.
| edit | [EditOptions](#editoptions) | `false` | The options used to configure the edit toolbar.

<a name="drawoptions" />
### DrawOptions

These options will allow you to configure the draw toolbar and its handlers.

| Option | Type | Default | Description
| --- | --- | --- | ---
| polyline | [PolylineOptions](#polylineoptions) | `{ }` | Polyline draw handler options. Set to `false` to disable handler.
| polygon | [PolygonOptions](#polygonoptions) | `{ }` | Polygon draw handler options. Set to `false` to disable handler.
| rectangle | [RectangleOptions](#rectangleoptions) | `{ }` | Rectangle draw handler options. Set to `false` to disable handler.
| circle | [CircleOptions](#circleoptions) | `{ }` | Circle draw handler options. Set to `false` to disable handler.
| marker | [MarkerOptions](#markeroptions) | `{ }` | Marker draw handler options. Set to `false` to disable handler.

### Draw handler options

The following options will allow you to configure the individual draw handlers.

<a name="polylineoptions" />
#### PolylineOptions

Polyline and Polygon drawing handlers take the same options.

| Option | Type | Default | Description
| --- | --- | --- | ---
| allowIntersection | Bool | `true` | Determines if line segments can cross.
| drawError | Object | [See code](https://github.com/Leaflet/Leaflet.draw/blob/master/src/draw/handler/Draw.Polyline.js#L10) | Configuration options for the error that displays if an intersection is detected.
| guidelineDistance | Number | `20` | Distance in pixels between each guide dash.
| shapeOptions | [Leaflet Polyline options](http://leafletjs.com/reference.html#polyline-options) | [See code](https://github.com/Leaflet/Leaflet.draw/blob/master/src/draw/handler/Draw.Polyline.js#L20) | The options used when drawing the polyline/polygon on the map.
| metric | Bool | `true` | Determines which measurement system (metric or imperial) is used.
| zIndexOffset | Number | `2000` | This should be a high number to ensure that you can draw over all other layers on the map.
| repeatMode | Bool | `false` | Determines if the draw tool remains enabled after drawing a shape.

<a name="polygonoptions" />
#### PolygonOptions

Polygon options include all of the Polyline options plus the option to show the approximate area.

| Option | Type | Default | Description
| --- | --- | --- | ---
| showArea | Bool | `false` | Show the area of the drawn polygon in m², ha or km². **The area is only approximate and become less accurate the larger the polygon is.**

<a name="rectangleoptions" />
#### RectangleOptions

| Option | Type | Default | Description
| --- | --- | --- | ---
| shapeOptions | [Leaflet Path options](http://leafletjs.com/reference.html#path-options) | [See code](https://github.com/Leaflet/Leaflet.draw/blob/master/src/draw/handler/Draw.Rectangle.js#L7) | The options used when drawing the rectangle on the map.
| repeatMode | Bool | `false` | Determines if the draw tool remains enabled after drawing a shape.

<a name="circleoptions" />
#### CircleOptions

| Option | Type | Default | Description
| --- | --- | --- | ---
| shapeOptions | [Leaflet Path options](http://leafletjs.com/reference.html#path-options) | [See code](https://github.com/Leaflet/Leaflet.draw/blob/master/src/draw/handler/Draw.Circle.js#L7) | The options used when drawing the circle on the map. 
| repeatMode | Bool | `false` | Determines if the draw tool remains enabled after drawing a shape.

<a name="markeroptions" />
#### MarkerOptions

| Option | Type | Default | Description
| --- | --- | --- | ---
| icon | [Leaflet Icon](http://leafletjs.com/reference.html#icon) | `L.Icon.Default()` | The icon displayed when drawing a marker.
| zIndexOffset | Number | `2000` | This should be a high number to ensure that you can draw over all other layers on the map.
| repeatMode | Bool | `false` | Determines if the draw tool remains enabled after drawing a shape.

<a name="editoptions" />
### EditOptions

These options will allow you to configure the draw toolbar and its handlers.

| Option | Type | Default | Description
| --- | --- | --- | ---
| featureGroup | [Leaflet FeatureGroup](http://leafletjs.com/reference.html#featuregroup) | `null` | This is the FeatureGroup that stores all editable shapes. **THIS IS REQUIRED FOR THE EDIT TOOLBAR TO WORK**
| edit | [EditHandlerOptions](#edithandleroptions) | `{ }` | Edit handler options. Set to `false` to disable handler.
| remove | [DeleteHandlerOptions](#deletehandleroptions) | `{ }` | Delete handler options. Set to `false` to disable handler.

<a name="edithandleroptions" />
#### EditHandlerOptions

| Option | Type | Default | Description
| --- | --- | --- | ---
| selectedPathOptions | [Leaflet Path options](http://leafletjs.com/reference.html#path-options) | [See code](https://github.com/Leaflet/Leaflet.draw/blob/master/src/edit/handler/EditToolbar.Edit.js#L9) | The path options for how the layers will look while in edit mode. If this is set to null the editable path options will not be set.

**Note:** To maintain the original layer color of the layer use `maintainColor: true` within `selectedPathOptions`.

E.g. The edit options below will maintain the layer color and set the edit opacity to 0.3.

````js
{
	selectedPathOptions: {
		maintainColor: true,
		opacity: 0.3
	}
}
````

<a name="deletehandleroptions" />
#### DeleteHandlerOptions

| Option | Type | Default | Description
| --- | --- | --- | ---

<a name="drawlocal" />
#### Customizing language and text in Leaflet.draw

Leaflet.draw uses the `L.drawLocal` configuration object to set any text used in the plugin. Customizing this will allow support for changing the text or supporting another language.

See [Leaflet.draw.js](https://github.com/Leaflet/Leaflet.draw/blob/master/src/Leaflet.draw.js) for the default strings.

E.g.

````js
// Set the button title text for the polygon button
L.drawLocal.draw.toolbar.buttons.polygon = 'Draw a sexy polygon!';

// Set the tooltip start text for the rectangle
L.drawLocal.draw.handlers.rectangle.tooltip.start = 'Not telling...';
````

<a name="commontasks" />
## Common tasks

The following examples outline some common tasks.

### Example Leaflet.draw config

The following example will show you how to:

1. Change the position of the control's toolbar.
2. Customize the styles of a vector layer.
3. Use a custom marker.
4. Disable the delete functionality.

````js
var cloudmadeUrl = 'http://{s}.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/997/256/{z}/{x}/{y}.png',
	cloudmade = new L.TileLayer(cloudmadeUrl, {maxZoom: 18}),
	map = new L.Map('map', {layers: [cloudmade], center: new L.LatLng(-37.7772, 175.2756), zoom: 15 });

var editableLayers = new L.FeatureGroup();
map.addLayer(editableLayers);

var MyCustomMarker = L.Icon.extend({
	options: {
		shadowUrl: null,
		iconAnchor: new L.Point(12, 12),
		iconSize: new L.Point(24, 24),
		iconUrl: 'link/to/image.png'
	}
});

var options = {
	position: 'topright',
	draw: {
		polyline: {
			shapeOptions: {
				color: '#f357a1',
				weight: 10
			}
		},
		polygon: {
			allowIntersection: false, // Restricts shapes to simple polygons
			drawError: {
				color: '#e1e100', // Color the shape will turn when intersects
				message: '<strong>Oh snap!<strong> you can\'t draw that!' // Message that will show when intersect
			},
			shapeOptions: {
				color: '#bada55'
			}
		},
		circle: false, // Turns off this drawing tool
		rectangle: {
			shapeOptions: {
				clickable: false
			}
		},
		marker: {
			icon: new MyCustomMarker()
		}
	},
	edit: {
		featureGroup: editableLayers, //REQUIRED!!
		remove: false
	}
};

var drawControl = new L.Control.Draw(options);
map.addControl(drawControl);

map.on('draw:created', function (e) {
	var type = e.layerType,
		layer = e.layer;

	if (type === 'marker') {
		layer.bindPopup('A popup!');
	}

	drawnItems.addLayer(layer);
});
````

### Disabling a toolbar

If you do not want a particular toolbar in your app you can turn it off by setting the toolbar to false.

````js
var drawControl = new L.Control.Draw({
	draw: false,
	edit: {
		featureGroup: editableLayers
	}
});
````

### Disabling a toolbar item

If you want to turn off a particular toolbar item, set it to false. The following disables drawing polygons and markers. It also turns off the ability to edit layers.

````js
var drawControl = new L.Control.Draw({
	draw: {
		polygon: false,
		marker: false
	},
	edit: {
		featureGroup: editableLayers,
		edit: false
	}
});
````

### Changing a drawing handlers options

You can change a draw handlers options after initialisation by using the `setDrawingOptions` method on the Leaflet.draw control.

E.g. to change the colour of the rectangle:

````js
drawControl.setDrawingOptions({
    rectangle: {
    	shapeOptions: {
        	color: '#0000FF'
        }
    }
});
````

### Creating a custom build

If you only require certain handlers (and not the UI), you may wish to create a custom build. You can generate the relevant jake command using the [build html file](https://github.com/Leaflet/Leaflet.draw/blob/master/build/build.html). 

See [edit handlers example](https://github.com/Leaflet/Leaflet.draw/blob/master/examples/edithandlers.html) which uses only the edit handlers.

<a name="thanks" />
## Thanks

Thanks so much to [@brunob](https://github.com/brunob), [@tnightingale](https://github.com/tnightingale), and [@shramov](https://github.com/shramov). I got a lot of ideas from their Leaflet plugins.

All the [contributors](https://github.com/Leaflet/Leaflet.draw/graphs/contributors) and issue reporters of this plugin rock. Thanks for tidying up my mess and keeping the plugin on track.

The icons used for some of the toolbar buttons are either from http://glyphicons.com/ or inspired by them. <3 Glyphicons!

Finally, [@mourner](https://github.com/mourner) is the man! Thanks for dedicating so much of your time to create the gosh darn best JavaScript mapping library around.
CKEditor 4
==========

Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.  
http://ckeditor.com - See LICENSE.md for license information.

CKEditor is a text editor to be used inside web pages. It's not a replacement
for desktop text editors like Word or OpenOffice, but a component to be used as
part of web applications and websites.

## Documentation

The full editor documentation is available online at the following address:
http://docs.ckeditor.com

## Installation

Installing CKEditor is an easy task. Just follow these simple steps:

 1. **Download** the latest version from the CKEditor website:
    http://ckeditor.com. You should have already completed this step, but be
    sure you have the very latest version.
 2. **Extract** (decompress) the downloaded file into the root of your website.

**Note:** CKEditor is by default installed in the `ckeditor` folder. You can
place the files in whichever you want though.

## Checking Your Installation

The editor comes with a few sample pages that can be used to verify that
installation proceeded properly. Take a look at the `samples` directory.

To test your installation, just call the following page at your website:

	http://<your site>/<CKEditor installation path>/samples/index.html

For example:

	http://www.example.com/ckeditor/samples/index.html
CKEditor SCAYT Plugin
=====================

This plugin brings Spell Check As You Type (SCAYT) into CKEditor.

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
### Recline Deeplink

Saves the current multiview state allowing to share a visualization by url.

## Requirements
* Recline multiview

**To save time we recommend to install this tools:**

* npm
* grunt
* bower

## Usage
You only have to pass a valid multiview object as value to recline.DeepLink.Router constructor.

```javascript
var router = new recline.DeepLink.Router(multiview);
router.start();
```

## Installation

```bash
git clone https://github.com/NuCivic/recline-deeplink.git
cd recline-deeplink
bower install
npm install
```

## Run demo

```bash
grunt
```

## Lint code

```bash
grunt lint
```

## Build example

```bash
make
```

## Plugins
A plugin is a javascript constructor that currently only need two methods to manipulate the url state and
react based on that state. You can add a new plugin just calling the addDependency method of router object in this way:

```javascript
router.addDependency(new recline.DeepLink.Deps.Map(map, router));
```

To define a new plugin you have to create a javascript constructor with the update and alterState methods and a property name set to the name that you want.

The alterState method allow you to add new data in the url under a key. The key used for that purpose is the name of the plugin.

Also you have to implement the update method that will be called when the name key is detected in the url.

You can check map.dep.js plugin implementation at src directory for more details.

## TODO
* Create unit tests

## Caveats
Since the state is shared through url, data edition (eg. add, delete or edit a row in the dataset) is not saved at all.
Superfish library

About:
------
This is the Superfish library for the Superfish module of the Drupal CMS.
http://drupal.org/project/superfish

The homepage of the jQuery Superfish plug-in is located at:
http://users.tpg.com.au/j_birch/plugins/superfish


Important:
----------
Do not modify any files of the Superfish library. The only acceptable change is addition of new CSS
files to the /style directory. Read the module README or the documentation for more information.


Requirements:
-------------
- jQuery version 1.3.x or later.
- jQuery version 1.6.1 or later if you are going to use the jQuery Easing plugin.


Contents:
---------
- superfish.js 
-- The jQuery Superfish plug-in version 1.4.8.
-- It is slightly modified in order to make it compatible with screen reader software.
-- The original Superfish plug-in can be found at the homepage of the jQuery Superfish plugin.

- supersubs.js
-- The jQuery Supersubs plug-in version 0.2-beta.
-- It is slightly modified because of the Superfish project of the Drupal CMS.
-- The original Supersubs plug-in can be found at the homepage of the jQuery Superfish plug-in.

- supposition.js
-- The jQuery Supposition plug-in version 0.2.
-- It is heavily modified in order to work flawlessly.
-- The original Supposition plug-in can be found at:
   http://users.tpg.com.au/j_birch/plugins/superfish/supposition-test/

- sftouchscreen.js
-- The jQuery sf-Touchscreen plug-in version 1.2-beta.
-- It is developed as a part of the Superfish project of the Drupal CMS.

- sfsmallscreen.js
-- The jQuery sf-Smallscreen plug-in version 1.0-beta.
-- It is developed as a part of the Superfish project of the Drupal CMS.

- jquery.bgiframe.min.js
-- The jQuery bgIframe plug-in version 2.1.2.

- jquery.hoverIntent.minified.js
-- The jQuery hoverIntent plug-in r6.


Changes:
--------
May, 2013
---------
- Added a few help pages to the /style directory.
- Added a file to check the library version.
- Fixed an image.

February, 2013
--------------
- sfSmallscreen plug-in.
- sfTouchscreen overhaul.
- Potential bug fixed.
- Color change for the .sf-description in all the styles in the /styles folder.

February, 2012
--------------
- Some important CSS improvements.
- supposition.js improved.
- /style/simple/simple.css improved.
- Added a centre-aligned version of the Simple style.

January, 2012
-------------
- superfish.js slightly modified in order to work with screen reader software.

December, 2011
--------------
- Several changes to the core CSS files.
- Introducing Simple, a beautiful new style.

September, 2011
---------------
- style/light-blue.css image path fixed.
- style/spring.css image path fixed.
- style/white.css image path fixed.

March, 2011
-----------
- supersubs.js slightly modified in order to ignore the Mega-menus.

January, 2011
-------------
- supersubs.js slightly modified to skip one level if the menu was a Navbar.<img src="http://leafletjs.com/docs/images/logo.png" alt="Leaflet" />

Leaflet is an open source JavaScript library for **mobile-friendly interactive maps**.
It is developed by [Vladimir Agafonkin][] of [MapBox][] with a team of dedicated [contributors][].
Weighing just about 30 KB of gzipped JS code, it has all the [features][] most developers ever need for online maps.

Leaflet is designed with *simplicity*, *performance* and *usability* in mind.
It works efficiently across all major desktop and mobile platforms out of the box,
taking advantage of HTML5 and CSS3 on modern browsers while being accessible on older ones too.
It can be extended with a huge amount of [plugins][],
has a beautiful, easy to use and [well-documented][] API
and a simple, readable [source code][] that is a joy to [contribute][] to.

For more info, docs and tutorials, check out the [official website][].<br>
For **Leaflet downloads** (including the built master version), check out the [download page][].

We're happy to meet new contributors.
If you want to **get involved** with Leaflet development, check out the [contribution guide][contribute].
Let's make the best mapping library that will ever exist,
and push the limits of what's possible with online maps!

[![Build Status](https://travis-ci.org/Leaflet/Leaflet.png?branch=master)](https://travis-ci.org/Leaflet/Leaflet)

 [Vladimir Agafonkin]: http://agafonkin.com/en
 [contributors]: https://github.com/Leaflet/Leaflet/graphs/contributors
 [features]: http://leafletjs.com/features.html
 [plugins]: http://leafletjs.com/plugins.html
 [well-documented]: http://leafletjs.com/reference.html "Leaflet API reference"
 [source code]: https://github.com/Leaflet/Leaflet "Leaflet GitHub repository"
 [hosted on GitHub]: http://github.com/Leaflet/Leaflet
 [contribute]: https://github.com/Leaflet/Leaflet/blob/master/CONTRIBUTING.md "A guide to contributing to Leaflet"
 [official website]: http://leafletjs.com
 [download page]: http://leafletjs.com/download.html
 [MapBox]: https://mapbox.com
# FlexSlider 2
http://www.woothemes.com/flexslider/ - Copyright (c) 2012 WooThemes

## Updates

** Version 2.2.0**

- Fixed event handler conflicts with devices that are both click and touch enabled. e.g., Windows 8.
- Made all slider variables public, stored in `slider.vars`. This allows manipulation of `slider.vars.minItems` and `slider.vars.maxItems` on the fly to create different fluid grids at certain breakpoints. [Check out this example demonstrating a basic technique](http://flexslider.woothemes.com/dynamic-carousel-min-max.html)
- Fixed calculations that were causing strange issues with paging and certain FlexSliders to move out of alignment.

*Be sure to test v2.2.0 with your current slider, before pushing live, to ensure everything is playing nicely.*

-----

## General Notes
FlexSlider is no longer licensed under the MIT license. FlexSlider now shares the common licensed used for all WooThemes themes, GPLv2.

In an effort to move the plugin forward, support for jQuery 1.3.2 has been dropped. The plugin now requires jQuery 1.4.2+. If you don't have access to the later versions of jQuery, [FlexSlider 1.8](https://github.com/woothemes/FlexSlider/tree/flexslider1) should be a perfectly suitable substitute for your needs!

Your old styles and properties *might not work out of the box*. Some property names have been changed, noted below, as well as namespacing prefixes being applied to all elements. This means that `.flex-direction-nav .next` is now `.flex-direction-nav .flex-next` by default. The namespacing property is exposed, free for you to change.

No more overflow hidden woes! The plugin now generates a viewport element to handle the tedious task of working around overflow hidden. Yay!

The slider element is now accessible outside of the callback API via the jQuery .data() method. Example use: `$('#slider').data('flexslider')`

Helper strings have been added for performing actions quickly on FlexSlider elements. Example uses:

- `$('#slider').flexslider("play")  //Play slideshow`
- `$('#slider').flexslider("pause") //Pause slideshow`
- `$('#slider').flexslider("stop") //Stop slideshow`
- `$('#slider').flexslider("next")  //Go to next slide`
- `$('#slider').flexslider("prev")  //Go to previous slide`
- `$('#slider').flexslider(3)       //Go fourth slide`

Two new methods are available for adding/removing slides, `slider.addSlide()` and `slider.removeSlide()`. More details about this coming soon.

- `slider.addSlide(obj, pos)` accepts two parameters, a string/jQuery object and an index.
- `slider.removeSlide(obj)` accepts one parameter, either an object to be removed, or an index.

## Examples

- [Basic Slider](http://flexslider.woothemes.com/)
- [Slider w/thumbnail controlNav pattern](http://flexslider.woothemes.com/thumbnail-controlnav.html)
- [Slider w/thumbnail slider](http://flexslider.woothemes.com/thumbnail-slider.html)
- [Basic Carousel](http://flexslider.woothemes.com/basic-carousel.html)
- [Carousel with min and max ranges](http://flexslider.woothemes.com/carousel-min-max.html)
- [Video with Vimeo API](http://flexslider.woothemes.com/video.html)
- [Video with Wistia API](http://flexslider.woothemes.com/video-wistia.html)


## Properties

### namespace: *{new}*
`namespace` controls the prefixes attached to elements created by the plugin. In previous releases, only certain elements were tagged with a prefix class, which was causing class generalization issues for some users. FlexSlider now prefixes all generated elements with the appropriate namespace.

*Hint: `namespace` can be an empty string.*

### selector: *{new}*
The markup structure for FlexSlider has been limited to a "ul.slide li" pattern in previous versions of FlexSlider; no longer. You can now take full control of the markup structure used for your FlexSlider. The `selector` pattern "{container} > {slide}" is mandatory, allowing the plugin to predictably interpret the selector property. Omitting the ">" from the selector is not suggested, but is possible if your markup doesn't follow the immediate descendant pattern.

*Examples: "section > article", ".slides > .slide", "#hero .slide"*

### easing: *{new}*
`easing` allows support for jQuery easing! Default options provided by jQuery are "swing" and "linear," but more can be used by included the jQuery Easing plugin. *If you chose a non-existent easing method, the slider will break.*

*Note: You need to set `useCSS: false` to force transitions in browsers that support translate3d.*
*Optional: [jQuery Easing Plugin](http://gsgd.co.uk/sandbox/jquery/easing/)*

### direction: *{changed}*
Previously called "slideDirection" in v1.8 and below.

### reverse: *{new}*
`reverse` will reverse the animation direction of the slider. Meaning, horizontal sliders can move from right to left, and vertical sliders can move bottom to top.

### smoothHeight: *{new}*
`smoothHeight` allows for smooth height transitions between slides. This property currently works for the fade and horizontal slide animation. The property has no effect on horizontal sliding carousels, however.

### startAt: *{changed}*
Previously called "slideToStart" in v1.8 and below.

### animationSpeed: *{changed}*
Previously called "animationDuration" in v1.8 and below.

### initDelay: *{new}*
`initDelay` will delay the initial slideshow of a slider, given in milliseconds. The slider will still initialize, generating controls and displaying the first image, but the slideshow will wait until the `initDelay` time has completed before starting the slideshow.

### useCSS: *{new}*
`useCSS` allow users to override using CSS3 for animation. Translate3d still has numerous bugs that can crop up and wreak havoc, so this is a great property to play with if you are experiencing unexplainable issues in Webkit browsers.

*Hint: Use conditionals to enable/disable the use of CSS3 on desktops and mobile devices. Mobile devices, in my experience, do not share many of the translate3d bugs seen on desktop browsers.*

### touch: *{new}*
`touch` allows users to exclude touch swipe functionality from their sliders.

### keyboard: *{changed}*
Previously called "keyboardNav" in v1.8 and below.

### multipleKeyboard *{new}*
`multipleKeyboard` allows users to override the default plugin keyboard behavior, enabling keyboard control of more than one slider on the page. This means that all visible sliders will animate, at the same time, via keyboard input.

*Hint: You can use `multipleKeyboard` to allow keyboard navigation on pages where multiple sliders are present, but only one is visible.*

### mousewheel: *{updated}*
`mousewheel` now requires the jQuery Mousewheel plugin. There are a few reasons for this, but primarily because there is no need for FlexSlider itself to reinvent the awkward complexity of mousewheel interactivity that is handled perfectly by the Mousewheel plugin.

*Required: [jQuery Mousewheel Plugin](https://github.com/brandonaaron/jquery-mousewheel)*

### controlsContainer: *{updated}*
`controlsContainer` is one of the more painstaking, potentially confusing properties within FlexSlider. First, the property is no longer required to workaround `overflow: hidden` on slide animation. Second, the property now accepts a **jQuery object**, giving you precise control over the object you want. The plugin no longer attempts to guess what element you are selecting.

### sync: *{new}*
`sync` is a new property that will allow other slider(s) to hook into the current slider via a given selector. The selector should describe an object that has already been initialized as a FlexSlider. Right now, `sync` will synchronize animation, play, and pause behaviors. More behaviors can be added in the future as the property matures.

*[Example of sync being used](http://flex.madebymufffin.com/examples/basic-carousel.html)*

### asNavFor: *{new}*
Description to be added.

### itemWidth: *{new}*
`itemWidth` is the primary property for the new carousel options. Without this property, your slider is not considered a carousel. To use `itemWidth`, give an integer value of the width of your individual slides. This should include borders and paddings applied to your slides; a total width measurement.

### itemMargin: *{new}*
`itemMargin` describes the gutter between the slide elements. If each slide has a margin-left of 10px, your itemMargin value would be 10. If elements have margin: 0 10px, your itemMargin would be 20.

### minItems: *{new}*
`minItems` describes the minimum number of slide elements that should be visible in the carousel. When the slider reaches the minimum item count, the slides will resize fluidly with the slider.

### maxItems: *{new}*
`maxItems` describes the maximum number of slide elements that should be visible in the carousel. When the slider reaches the maximum item count, the slides will resize fluidly with the sider.

### move: *{new}*
`move` determines how many slides should be animated within the carousel. When left at 0, the slider will animate the number of visible slides. If any value greater than 0 is given, the slider will animate that number of slides in the carousel on each animation interval.

*Hint: The move property will be ignored if the value is higher than the number of visible slides, which can be utilized in responsive design.*

### added: *{new}*
`added()` is a new callback event fired in the new slider.addSlide() function.

### removed: *{new}*
`removed()` is a new callback event fired in the new slider.removeSlide() function.

### allowOneSlide: *{new}*
Boolean. Whether or not you'd like FlexSlider to initialize as usual if only one slide is present.
# Flot [![Build status](https://travis-ci.org/flot/flot.png)](https://travis-ci.org/flot/flot)

## About ##

Flot is a Javascript plotting library for jQuery.  
Read more at the website: <http://www.flotcharts.org/>

Take a look at the the examples in examples/index.html; they should give a good
impression of what Flot can do, and the source code of the examples is probably
the fastest way to learn how to use Flot.


## Installation ##

Just include the Javascript file after you've included jQuery.

Generally, all browsers that support the HTML5 canvas tag are
supported.

For support for Internet Explorer < 9, you can use [Excanvas]
[excanvas], a canvas emulator; this is used in the examples bundled
with Flot. You just include the excanvas script like this:

```html
<!--[if lte IE 8]><script language="javascript" type="text/javascript" src="excanvas.min.js"></script><![endif]-->
```

If it's not working on your development IE 6.0, check that it has
support for VML which Excanvas is relying on. It appears that some
stripped down versions used for test environments on virtual machines
lack the VML support.

You can also try using [Flashcanvas][flashcanvas], which uses Flash to
do the emulation. Although Flash can be a bit slower to load than VML,
if you've got a lot of points, the Flash version can be much faster
overall. Flot contains some wrapper code for activating Excanvas which
Flashcanvas is compatible with.

You need at least jQuery 1.2.6, but try at least 1.3.2 for interactive
charts because of performance improvements in event handling.


## Basic usage ##

Create a placeholder div to put the graph in:

```html
<div id="placeholder"></div>
```

You need to set the width and height of this div, otherwise the plot
library doesn't know how to scale the graph. You can do it inline like
this:

```html
<div id="placeholder" style="width:600px;height:300px"></div>
```

You can also do it with an external stylesheet. Make sure that the
placeholder isn't within something with a display:none CSS property -
in that case, Flot has trouble measuring label dimensions which
results in garbled looks and might have trouble measuring the
placeholder dimensions which is fatal (it'll throw an exception).

Then when the div is ready in the DOM, which is usually on document
ready, run the plot function:

```js
$.plot($("#placeholder"), data, options);
```

Here, data is an array of data series and options is an object with
settings if you want to customize the plot. Take a look at the
examples for some ideas of what to put in or look at the 
[API reference](API.md). Here's a quick example that'll draw a line 
from (0, 0) to (1, 1):

```js
$.plot($("#placeholder"), [ [[0, 0], [1, 1]] ], { yaxis: { max: 1 } });
```

The plot function immediately draws the chart and then returns a plot
object with a couple of methods.


## What's with the name? ##

First: it's pronounced with a short o, like "plot". Not like "flawed".

So "Flot" rhymes with "plot".

And if you look up "flot" in a Danish-to-English dictionary, some of
the words that come up are "good-looking", "attractive", "stylish",
"smart", "impressive", "extravagant". One of the main goals with Flot
is pretty looks.


## Notes about the examples ##

In order to have a useful, functional example of time-series plots using time
zones, date.js from [timezone-js][timezone-js] (released under the Apache 2.0
license) and the [Olson][olson] time zone database (released to the public
domain) have been included in the examples directory.  They are used in
examples/axes-time-zones/index.html.


[excanvas]: http://code.google.com/p/explorercanvas/
[flashcanvas]: http://code.google.com/p/flashcanvas/
[timezone-js]: https://github.com/mde/timezone-js
[olson]: ftp://ftp.iana.org/tz/
<!doctype html>
<html>
<head>
<title>README: JW Player</title>
<style>
    body { padding: 50px 100px; width: 700px; font: 13px/20px Arial; background: #FFF; }
    a, h1, h2 { color: #369; }
    h2 { margin-top: 50px; }
    pre { font-size: 12px; background:#E5F3C8; padding:5px 10px; border: 1px solid #D3EAA4; }
    dt { font-weight: bold; }
</style>
</head><body>

<h1>README: JW Player</h1>

<p>Thank you for downloading JW Player 6, the world's most popular HTML5/Flash video player! See <a href="http://www.longtailvideo.com/support/jw-player/28832/about-jw-player">About JW Player</a> for an overview of supported browsers/devices, as well as a more detailed feature list. See the <a href="http://www.longtailvideo.com/support/jw-player/28835/release-notes">Release Notes</a> if you want to learn what changed with this latest release.</p>

<h2>Quick Start</h2>

<p>Copy the <strong>jwplayer</strong> folder that contains this README to the www root of your website. Next, include the <em>jwplayer.js</em> script in the &lt;head&gt; of your HTML page.</p>

<p>If you have purchased the <a href="http://www.longtailvideo.com/jw-player/pricing/">Pro, Premium or Ads edition</a> of JW Player, its features can be activated by inserting your server-less JW Player license key in the second line:</p>

<pre>
&lt;script type="text/javascript" src="/jwplayer/jwplayer.js"&gt;&lt;/script&gt;
&lt;script type="text/javascript"&gt;jwplayer.key="ABCDEFGHIJKLMOPQ";&lt;/script&gt;
</pre>

<p>Note: A key is not required to use the Free edition, but will still be available from your <a href="https://account.longtailvideo.com/">JW Player Account</a>. Including your key will enable the free <a href="http://www.longtailvideo.com/support/jw-player/28852/using-jw-player-analytics">JW Player Analytics</a> for your account.</p>

<h3>Embed Code</h3>

<p>When the script and key are set, scroll down to the &lt;body&gt; of your HTML page and insert the JW Player embed code at the place you want your video to appear:</p>

<pre>
&lt;div id="myElement"&gt;Loading the player...&lt;/div&gt;

&lt;script type="text/javascript"&gt;
    jwplayer("myElement").setup({
        file: "/uploads/myVideo.mp4",
        image: "/uploads/myPoster.jpg"
    });
&lt;/script&gt;
</pre>

<p>See <a href="http://www.longtailvideo.com/support/jw-player/28839/embedding-the-player">Embedding JW Player</a> for a more elaborate description of options and some example embeds.</p>

<p><em>Note two very common issues prevent smooth video playback in Internet Explorer 9/10. First, you need to set <strong>&lt;!DOCTYPE html&gt;</strong> to prevent triggering IE's compatibility mode. Second, your videos must be served with the <strong>video/mp4</strong> mimetype. Not doing so will cause IE not to play them. See our <a href="http://www.longtailvideo.com/support/jw-player/28840/troubleshooting-your-setup">troubleshooting guide</a> for more common issues.</em></p>

<h3>Premium Skins</h3>

<p>If you have purchased the Premium or Ads edition of the player, your player includes a set of Premium skins. These skins can be downloaded from your <a href="https://account.longtailvideo.com/">JW Player Account</a>, but you can also load them off our CDN by simply inserting the skin name:</p>
<pre>    skin: "bekle"</pre>

<p>See <a href="http://www.longtailvideo.com/support/jw-player/28846/using-jw-player-skins">Using JW Player Skins</a> for more info.</p>



<h2>Documentation</h2>

<p>If you need help, the LongTail Support Community contains a wealth of information, including guides on:</p>

<ul>
<li>Supported <a href="http://www.longtailvideo.com/support/jw-player/28836/media-format-support">Media Formats</a> and <a href="http://www.longtailvideo.com/support/jw-player/28837/browser-device-support">Browsers &amp; Devices</a>.</li>
<li> How to <a href="http://www.longtailvideo.com/support/jw-player/28839/embedding-the-player">Customize</a> and <a href="http://www.longtailvideo.com/support/jw-player/28840/troubleshooting-your-setup">Troubleshoot</a> your embeds.</li>
<li>Configuring <a href="http://www.longtailvideo.com/support/jw-player/28842/working-with-playlists">Inline Playlists</a> or <a href="http://www.longtailvideo.com/support/jw-player/28843/loading-rss-feeds">RSS Feeds</a> (with multiple formats/qualities).</li>
<li>The <a href="http://www.longtailvideo.com/support/jw-player/28846/using-jw-player-skins">PNG Skinning Model</a> and <a href="http://www.longtailvideo.com/support/jw-player/28850/using-the-javascript-api">JavaScript API</a>.</li>
<li>Using <a href="http://www.longtailvideo.com/support/jw-player/28854/using-rtmp-streaming">RTMP Streaming</a> and <a href="http://www.longtailvideo.com/support/jw-player/28856/using-apple-hls-streaming/">Apple HLS</a> (Premium/Ads edition only).</li>
<li>How to <a href="http://www.longtailvideo.com/support/jw-player/28862/configuring-video-ads">Configure Video Ads</a> (Ads edition only).</li>
</ul>

<p>Visit our <a href="http://www.longtailvideo.com/support/forums/jw-player/">Support Forums</a> for setup problems, bug reports or suggestions for new features or enhancements. The forums are very active and frequently visited by members of the JW Player development team. Please see your <a href="http://account.longtailvideo.com">JW Player Account</a> for more information on obtaining technical support.</p>

<p>Follow the <a href="http://www.longtailvideo.com/blog/">LongTail Video Blog</a> for news on the JW Player and online video in general. We frequently publish posts on topics such as HTML5, video SEO, H.264, VAST advertising, etc. You can also <a href="http://twitter.com/longtailvideo">follow us on Twitter</a> or <a href="http://www.facebook.com/longtailvideo">like us on Facebook</a> to stay connected.</p>



<h2>Licensing</h2>

<p>Please be aware that each player edition has its own license:</p>

<dl>
<dt>JW Player Free</dt>
<dd>Under the terms of our <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons license</a>, you can use, modify and redistribute the player for non-commercial purposes only. 
Commercial sites must <a href=" http://www.longtailvideo.com/jw-player/pricing/">purchase a license</a> for the <strong>Pro</strong>, <strong>Premium</strong> or <strong>Ads</strong> editions. See the <a href="http://www.longtailvideo.com/jw-player/license/jw-player-license-text">JW Player 6 License</a> for further details.</dd>
<dt>JW Player Pro</dt>
<dd>
Under the terms of our <a href="http://www.longtailvideo.com/jw-player/license/jw-player-license-text">Commercial License</a>, you can deploy your copy of JW Player <strong>Pro</strong> for commercial use on 1 domain.  See our <a href="http://www.longtailvideo.com/jw-player/pricing/">pricing page</a> for more information on edition features and pricing.
</dd>
<dt>JW Player Premium</dt>
<dd>
  Under the terms of our <a href="http://www.longtailvideo.com/jw-player/license/jw-player-license-text">Commercial License</a>, you can deploy your copy of JW Player <strong>Premium</strong> for commercial use on up to 10 domains. See our <a href="http://www.longtailvideo.com/jw-player/pricing/">pricing page</a> for more information on edition features and pricing.
</dd>
<dt>JW Player Ads</dt>
<dd>
Under the terms of our <a href="http://www.longtailvideo.com/jw-player/license/jw-player-license-text">Commercial License</a>, you can deploy your copy of JW Player <strong>Ads</strong> for commercial use on up to 10 domains, with an additional restriction of up to 250.000 filled ad impressions per month. See our <a href="http://www.longtailvideo.com/jw-player/pricing/">pricing page</a> for more information on edition features and price.</dd>
</dl>

<p>Examples of <strong>commercial use</strong> includes websites with any advertisements, websites owned or operated by businesses, websites designed to promote products or services, and tools (e.g. a CMS) that bundle JW Player in their offering.</p>

<p>Note all editions of JW Player incorporate the <a href="http://www.movable-type.co.uk/scripts/tea-block.html">Block TEA library</a> from Movable Type (CC-BY license).</p>


</body>
</html>ExplorerCanvas
Copyright 2006 Google Inc.

-------------------------------------------------------------------------------
DESCRIPTION

Firefox, Safari and Opera 9 support the canvas tag to allow 2D command-based 
drawing operations. ExplorerCanvas brings the same functionality to Internet 
Explorer; web developers only need to include a single script tag in their 
existing canvas webpages to enable this support.


-------------------------------------------------------------------------------
INSTALLATION

Include the ExplorerCanvas tag in the same directory as your HTML files, and 
add the following code to your page, preferably in the <head> tag.

<!--[if IE]><script type="text/javascript" src="excanvas.js"></script><![endif]-->

If you run into trouble, please look at the included example code to see how
to best implement thisLeaflet.markercluster
=====================

Provides Beautiful Animated Marker Clustering functionality for [Leaflet](http://leafletjs.com), a JS library for interactive maps.

*Requires Leaflet 0.7.0 or newer.*

For a Leaflet 0.5 compatible version, [Download b128e950](https://github.com/Leaflet/Leaflet.markercluster/archive/b128e950d8f5d7da5b60bd0aa9a88f6d3dd17c98.zip)<br>
For a Leaflet 0.4 compatible version, [Download the 0.2 release](https://github.com/Leaflet/Leaflet.markercluster/archive/0.2.zip)

## Using the plugin

Install with Bower: `bower install leaflet.markercluster`

See the included examples for usage.

The [realworld example](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-realworld.388.html) is a good place to start, it uses all of the defaults of the clusterer.
Or check out the [custom example](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-custom.html) for how to customise the behaviour and appearance of the clusterer

### Usage
Create a new MarkerClusterGroup, add your markers to it, then add it to the map

```javascript
var markers = new L.MarkerClusterGroup();
markers.addLayer(new L.Marker(getRandomLatLng(map)));
... Add more layers ...
map.addLayer(markers);
```

### Defaults
By default the Clusterer enables some nice defaults for you:
* **showCoverageOnHover**: When you mouse over a cluster it shows the bounds of its markers.
* **zoomToBoundsOnClick**: When you click a cluster we zoom to its bounds.
* **spiderfyOnMaxZoom**: When you click a cluster at the bottom zoom level we spiderfy it so you can see all of its markers. (*Note: the spiderfy occurs at the current zoom level if all items within the cluster are physically located at the same latitude and longitude.*)
* **removeOutsideVisibleBounds**: Clusters and markers too far from the viewport are removed from the map for performance.

You can disable any of these as you want in the options when you create the MarkerClusterGroup:
```javascript
var markers = new L.MarkerClusterGroup({ spiderfyOnMaxZoom: false, showCoverageOnHover: false, zoomToBoundsOnClick: false });
```

### Customising the Clustered Markers
As an option to MarkerClusterGroup you can provide your own function for creating the Icon for the clustered markers.
The default implementation changes color at bounds of 10 and 100, but more advanced uses may require customising this.
You do not need to include the .Default css if you go this way.
You are passed a MarkerCluster object, you'll probably want to use getChildCount() or getAllChildMarkers() to work out the icon to show

```javascript
var markers = new L.MarkerClusterGroup({
	iconCreateFunction: function(cluster) {
		return new L.DivIcon({ html: '<b>' + cluster.getChildCount() + '</b>' });
	}
});
```
Check out the [custom example](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-custom.html) for an example of this.

### All Options
Enabled by default (boolean options):
* **showCoverageOnHover**: When you mouse over a cluster it shows the bounds of its markers.
* **zoomToBoundsOnClick**: When you click a cluster we zoom to its bounds.
* **spiderfyOnMaxZoom**: When you click a cluster at the bottom zoom level we spiderfy it so you can see all of its markers. (*Note: the spiderfy occurs at the current zoom level if all items within the cluster are physically located at the same latitude and longitude.*)
* **removeOutsideVisibleBounds**: Clusters and markers too far from the viewport are removed from the map for performance.

Other options
* **animateAddingMarkers**: If set to true then adding individual markers to the MarkerClusterGroup after it has been added to the map will add the marker and animate it in to the cluster. Defaults to false as this gives better performance when bulk adding markers. addLayers does not support this, only addLayer with individual Markers.
* **disableClusteringAtZoom**: If set, at this zoom level and below markers will not be clustered. This defaults to disabled. [See Example](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-realworld-maxzoom.388.html)
* **maxClusterRadius**: The maximum radius that a cluster will cover from the central marker (in pixels). Default 80. Decreasing will make more, smaller clusters. You can also use a function that accepts the current map zoom and returns the maximum cluster radius in pixels.
* **polygonOptions**: Options to pass when creating the L.Polygon(points, options) to show the bounds of a cluster
* **singleMarkerMode**: If set to true, overrides the icon for all added markers to make them appear as a 1 size cluster
* **spiderfyDistanceMultiplier**: Increase from 1 to increase the distance away from the center that spiderfied markers are placed. Use if you are using big marker icons (Default:1)
* **iconCreateFunction**: Function used to create the cluster icon [See default as example](https://github.com/Leaflet/Leaflet.markercluster/blob/15ed12654acdc54a4521789c498e4603fe4bf781/src/MarkerClusterGroup.js#L542).

## Events
If you register for click, mouseover, etc events just related to Markers in the cluster.
To receive events for clusters listen to 'cluster' + 'eventIWant', ex: 'clusterclick', 'clustermouseover'.

Set your callback up as follows to handle both cases:

```javascript
markers.on('click', function (a) {
	console.log('marker ' + a.layer);
});

markers.on('clusterclick', function (a) {
	console.log('cluster ' + a.layer.getAllChildMarkers().length);
});
```

#### Additional MarkerClusterGroup Events

- **animationend**: Fires when marker clustering/unclustering animation has completed
- **spiderfied**: Fires when overlapping markers get spiderified

## Methods

### Getting the bounds of a cluster
When you receive an event from a cluster you can query it for the bounds.
See [example/marker-clustering-convexhull.html](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-convexhull.html) for a working example.
```javascript
markers.on('clusterclick', function (a) {
	map.addLayer(new L.Polygon(a.layer.getConvexHull()));
});
```

### Zooming to the bounds of a cluster
When you receive an event from a cluster you can zoom to its bounds in one easy step.
If all of the markers will appear at a higher zoom level, that zoom level is zoomed to instead.
See [marker-clustering-zoomtobounds.html](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-zoomtobounds.html) for a working example.
```javascript
markers.on('clusterclick', function (a) {
	a.layer.zoomToBounds();
});
```

### Getting the visible parent of a marker
If you have a marker in your MarkerClusterGroup and you want to get the visible parent of it (Either itself or a cluster it is contained in that is currently visible on the map).
This will return null if the marker and its parent clusters are not visible currently (they are not near the visible viewpoint)
```
var visibleOne = markerClusterGroup.getVisibleParent(myMarker);
console.log(visibleOne.getLatLng());
```

### Adding and removing Markers
addLayer, removeLayer and clearLayers are supported and they should work for most uses.

### Bulk adding and removing Markers
addLayers and removeLayers are bulk methods for adding and removing markers and should be favoured over the single versions when doing bulk addition/removal of markers. Each takes an array of markers

If you are removing a lot of markers it will almost definitely be better to call clearLayers then call addLayers to add the markers you don't want to remove back in. See [#59](https://github.com/Leaflet/Leaflet.markercluster/issues/59#issuecomment-9320628) for details.

### Other Methods
````
hasLayer(layer): Returns true if the given layer (marker) is in the MarkerClusterGroup
zoomToShowLayer(layer, callback): Zooms to show the given marker (spidifying if required), calls the callback when the marker is visible on the map
addLayers(layerArray): Adds the markers in the given array from the MarkerClusterGroup in an efficent bulk method.
removeLayers(layerArray): Removes the markers in the given array from the MarkerClusterGroup in an efficent bulk method.
````

## Handling LOTS of markers
The Clusterer can handle 10000 or even 50000 markers (in chrome). IE9 has some issues with 50000.
[realworld 10000 example](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-realworld.10000.html)
[realworld 50000 example](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-realworld.50000.html)
Performance optimizations could be done so these are handled more gracefully (Running the initial clustering over multiple JS calls rather than locking the browser for a long time)

### License

Leaflet.markercluster is free software, and may be redistributed under the MIT-LICENSE.

[![Build Status](https://travis-ci.org/Leaflet/Leaflet.markercluster.png?branch=master)](https://travis-ci.org/Leaflet/Leaflet.markercluster)
# Lo-Dash v2.4.1
A utility library delivering consistency, [customization](http://lodash.com/custom-builds), [performance](http://lodash.com/benchmarks), & [extras](http://lodash.com/#features).

## Download

Check out our [wiki]([https://github.com/lodash/lodash/wiki/build-differences]) for details over the differences between builds.

* Modern builds perfect for newer browsers/environments:<br>
[Development](https://raw.github.com/lodash/lodash/2.4.1/dist/lodash.js) &
[Production](https://raw.github.com/lodash/lodash/2.4.1/dist/lodash.min.js)

* Compatibility builds for older environment support too:<br>
[Development](https://raw.github.com/lodash/lodash/2.4.1/dist/lodash.compat.js) &
[Production](https://raw.github.com/lodash/lodash/2.4.1/dist/lodash.compat.min.js)

* Underscore builds to use as a drop-in replacement:<br>
[Development](https://raw.github.com/lodash/lodash/2.4.1/dist/lodash.underscore.js) &
[Production](https://raw.github.com/lodash/lodash/2.4.1/dist/lodash.underscore.min.js)

CDN copies are available on [cdnjs](http://cdnjs.com/libraries/lodash.js/) & [jsDelivr](http://www.jsdelivr.com/#!lodash). For smaller file sizes, create [custom builds](http://lodash.com/custom-builds) with only the features needed.

Love modules? We’ve got you covered with [lodash-amd](https://npmjs.org/package/lodash-amd), [lodash-es6](https://github.com/lodash/lodash-es6), [lodash-node](https://npmjs.org/package/lodash-node), & [npm packages](https://npmjs.org/browse/keyword/lodash-modularized) per method.

## Dive in

There’s plenty of **[documentation](http://lodash.com/docs)**, [unit tests](http://lodash.com/tests), & [benchmarks](http://lodash.com/benchmarks).<br>
Check out <a href="http://devdocs.io/lodash/">DevDocs</a> as a fast, organized, & searchable interface for our documentation.

The full changelog for this release is available on our [wiki](https://github.com/lodash/lodash/wiki/Changelog).<br>
A list of upcoming features is available on our [roadmap](https://github.com/lodash/lodash/wiki/Roadmap).

## Features *not* in Underscore

 * AMD loader support ([curl](https://github.com/cujojs/curl), [dojo](http://dojotoolkit.org/), [requirejs](http://requirejs.org/), etc.)
 * [_(…)](http://lodash.com/docs#_) supports intuitive chaining
 * [_.at](http://lodash.com/docs#at) for cherry-picking collection values
 * [_.bindKey](http://lodash.com/docs#bindKey) for binding [*“lazy”*](http://michaux.ca/articles/lazy-function-definition-pattern) defined methods
 * [_.clone](http://lodash.com/docs#clone) supports shallow cloning of `Date` & `RegExp` objects
 * [_.cloneDeep](http://lodash.com/docs#cloneDeep) for deep cloning arrays & objects
 * [_.constant](http://lodash.com/docs#constant) & [_.property](http://lodash.com/docs#property) function generators for composing functions
 * [_.contains](http://lodash.com/docs#contains) accepts a `fromIndex`
 * [_.create](http://lodash.com/docs#create) for easier object inheritance
 * [_.createCallback](http://lodash.com/docs#createCallback) for extending callbacks in methods & mixins
 * [_.curry](http://lodash.com/docs#curry) for creating [curried](http://hughfdjackson.com/javascript/2013/07/06/why-curry-helps/) functions
 * [_.debounce](http://lodash.com/docs#debounce) & [_.throttle](http://lodash.com/docs#throttle) accept additional `options` for more control
 * [_.findIndex](http://lodash.com/docs#findIndex) & [_.findKey](http://lodash.com/docs#findKey) for finding indexes & keys
 * [_.forEach](http://lodash.com/docs#forEach) is chainable & supports exiting early
 * [_.forIn](http://lodash.com/docs#forIn) for iterating own & inherited properties
 * [_.forOwn](http://lodash.com/docs#forOwn) for iterating own properties
 * [_.isPlainObject](http://lodash.com/docs#isPlainObject) for checking if values are created by `Object`
 * [_.mapValues](http://lodash.com/docs#mapValues) for [mapping](http://lodash.com/docs#map) values to an object
 * [_.memoize](http://lodash.com/docs#memoize) exposes the `cache` of memoized functions
 * [_.merge](http://lodash.com/docs#merge) for a deep [_.extend](http://lodash.com/docs#extend)
 * [_.noop](http://lodash.com/docs#noop) for function placeholders
 * [_.now](http://lodash.com/docs#now) as a cross-browser `Date.now` alternative
 * [_.parseInt](http://lodash.com/docs#parseInt) for consistent behavior
 * [_.pull](http://lodash.com/docs#pull) & [_.remove](http://lodash.com/docs#remove) for mutating arrays
 * [_.random](http://lodash.com/docs#random) supports returning floating-point numbers
 * [_.runInContext](http://lodash.com/docs#runInContext) for easier mocking
 * [_.sortBy](http://lodash.com/docs#sortBy) supports sorting by multiple properties
 * [_.support](http://lodash.com/docs#support) for flagging environment features
 * [_.template](http://lodash.com/docs#template) supports [*“imports”*](http://lodash.com/docs#templateSettings_imports) options & [ES6 template delimiters](http://people.mozilla.org/~jorendorff/es6-draft.html#sec-literals-string-literals)
 * [_.transform](http://lodash.com/docs#transform) as a powerful alternative to [_.reduce](http://lodash.com/docs#reduce) for transforming objects
 * [_.where](http://lodash.com/docs#where) supports deep object comparisons
 * [_.xor](http://lodash.com/docs#xor) as a companion to [_.difference](http://lodash.com/docs#difference), [_.intersection](http://lodash.com/docs#intersection), & [_.union](http://lodash.com/docs#union)
 * [_.zip](http://lodash.com/docs#zip) is capable of unzipping values
 * [_.omit](http://lodash.com/docs#omit), [_.pick](http://lodash.com/docs#pick), &
   [more](http://lodash.com/docs "_.assign, _.clone, _.cloneDeep, _.first, _.initial, _.isEqual, _.last, _.merge, _.rest") accept callbacks
 * [_.contains](http://lodash.com/docs#contains), [_.toArray](http://lodash.com/docs#toArray), &
   [more](http://lodash.com/docs "_.at, _.countBy, _.every, _.filter, _.find, _.forEach, _.forEachRight, _.groupBy, _.invoke, _.map, _.max, _.min, _.pluck, _.reduce, _.reduceRight, _.reject, _.shuffle, _.size, _.some, _.sortBy, _.where") accept strings
 * [_.filter](http://lodash.com/docs#filter), [_.map](http://lodash.com/docs#map), &
   [more](http://lodash.com/docs "_.countBy, _.every, _.find, _.findKey, _.findLast, _.findLastIndex, _.findLastKey, _.first, _.groupBy, _.initial, _.last, _.max, _.min, _.reject, _.rest, _.some, _.sortBy, _.sortedIndex, _.uniq") support *“_.pluck”* & *“_.where”* shorthands
 * [_.findLast](http://lodash.com/docs#findLast), [_.findLastIndex](http://lodash.com/docs#findLastIndex), &
   [more](http://lodash.com/docs "_.findLastKey, _.forEachRight, _.forInRight, _.forOwnRight, _.partialRight") right-associative methods

## Resources

 * Podcasts
  - [JavaScript Jabber](http://javascriptjabber.com/079-jsj-lo-dash-with-john-david-dalton/)

 * Posts
  - [Say “Hello” to Lo-Dash](http://kitcambridge.be/blog/say-hello-to-lo-dash/)
  - [Custom builds in Lo-Dash 2.0](http://kitcambridge.be/blog/custom-builds-in-lo-dash-2-dot-0/)

 * Videos
  - [Introduction](https://vimeo.com/44154599)
  - [Origins](https://vimeo.com/44154600)
  - [Optimizations & builds](https://vimeo.com/44154601)
  - [Native method use](https://vimeo.com/48576012)
  - [Testing](https://vimeo.com/45865290)
  - [CascadiaJS ’12](http://www.youtube.com/watch?v=dpPy4f_SeEk)

 A list of other community created podcasts, posts, & videos is available on our [wiki](https://github.com/lodash/lodash/wiki/Resources).

## Support

Tested in Chrome 5~31, Firefox 2~25, IE 6-11, Opera 9.25~17, Safari 3-7, Node.js 0.6.21~0.10.22, Narwhal 0.3.2, PhantomJS 1.9.2, RingoJS 0.9, & Rhino 1.7RC5.<br>
Automated browser test results [are available](https://saucelabs.com/u/lodash) as well as [Travis CI](https://travis-ci.org/) builds for [lodash](https://travis-ci.org/lodash/lodash/), [lodash-cli](https://travis-ci.org/lodash/lodash-cli/), [lodash-amd](https://travis-ci.org/lodash/lodash-amd/), [lodash-node](https://travis-ci.org/lodash/lodash-node/), & [grunt-lodash](https://travis-ci.org/lodash/grunt-lodash).

Special thanks to [Sauce Labs](https://saucelabs.com/) for providing automated browser testing.<br>
[![Sauce Labs](http://lodash.com/_img/sauce.png)](https://saucelabs.com/ "Sauce Labs: Selenium Testing & More")

## Installation & usage

In browsers:

```html
<script src="lodash.js"></script>
```

Using [`npm`](http://npmjs.org/):

```bash
npm i --save lodash

{sudo} npm i -g lodash
npm ln lodash
```

In [Node.js](http://nodejs.org/) & [Ringo](http://ringojs.org/):

```js
var _ = require('lodash');
// or as Underscore
var _ = require('lodash/dist/lodash.underscore');
```

**Notes:**
 * Don’t assign values to [special variable](http://nodejs.org/api/repl.html#repl_repl_features) `_` when in the REPL
 * If Lo-Dash is installed globally, run [`npm ln lodash`](http://blog.nodejs.org/2011/03/23/npm-1-0-global-vs-local-installation/) in your project’s root directory *before* requiring it

In [Rhino](http://www.mozilla.org/rhino/):

```js
load('lodash.js');
```

In an AMD loader:

```js
require({
  'packages': [
    { 'name': 'lodash', 'location': 'path/to/lodash', 'main': 'lodash' }
  ]
},
['lodash'], function(_) {
  console.log(_.VERSION);
});
```

## Author

| [![twitter/jdalton](http://gravatar.com/avatar/299a3d891ff1920b69c364d061007043?s=70)](https://twitter.com/jdalton "Follow @jdalton on Twitter") |
|---|
| [John-David Dalton](http://allyoucanleet.com/) |

## Contributors

| [![twitter/blainebublitz](http://gravatar.com/avatar/ac1c67fd906c9fecd823ce302283b4c1?s=70)](https://twitter.com/blainebublitz "Follow @BlaineBublitz on Twitter") | [![twitter/kitcambridge](http://gravatar.com/avatar/6662a1d02f351b5ef2f8b4d815804661?s=70)](https://twitter.com/kitcambridge "Follow @kitcambridge on Twitter") | [![twitter/mathias](http://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|---|---|
| [Blaine Bublitz](http://www.iceddev.com/) | [Kit Cambridge](http://kitcambridge.be/) | [Mathias Bynens](http://mathiasbynens.be/) |

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/lodash/lodash/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
# <a href="http://lodash.com/">Lo-Dash</a> <span>v2.4.1</span>

<!-- div -->


<!-- div -->

## <a id="arrays"></a>`Arrays`
* <a href="#_compactarray">`_.compact`</a>
* <a href="#_differencearray-values">`_.difference`</a>
* <a href="#_restarray-callback1-thisarg" class="alias">`_.drop` -> `rest`</a>
* <a href="#_findindexarray-callbackidentity-thisarg">`_.findIndex`</a>
* <a href="#_findlastindexarray-callbackidentity-thisarg">`_.findLastIndex`</a>
* <a href="#_firstarray-callback-thisarg">`_.first`</a>
* <a href="#_flattenarray-isshallowfalse-callbackidentity-thisarg">`_.flatten`</a>
* <a href="#_firstarray-callback-thisarg" class="alias">`_.head` -> `first`</a>
* <a href="#_indexofarray-value-fromindex0">`_.indexOf`</a>
* <a href="#_initialarray-callback1-thisarg">`_.initial`</a>
* <a href="#_intersectionarray">`_.intersection`</a>
* <a href="#_lastarray-callback-thisarg">`_.last`</a>
* <a href="#_lastindexofarray-value-fromindexarraylength-1">`_.lastIndexOf`</a>
* <a href="#_zipobjectkeys-values" class="alias">`_.object` -> `zipObject`</a>
* <a href="#_pullarray-value">`_.pull`</a>
* <a href="#_rangestart0-end-step1">`_.range`</a>
* <a href="#_removearray-callbackidentity-thisarg">`_.remove`</a>
* <a href="#_restarray-callback1-thisarg">`_.rest`</a>
* <a href="#_sortedindexarray-value-callbackidentity-thisarg">`_.sortedIndex`</a>
* <a href="#_restarray-callback1-thisarg" class="alias">`_.tail` -> `rest`</a>
* <a href="#_firstarray-callback-thisarg" class="alias">`_.take` -> `first`</a>
* <a href="#_unionarray">`_.union`</a>
* <a href="#_uniqarray-issortedfalse-callbackidentity-thisarg">`_.uniq`</a>
* <a href="#_uniqarray-issortedfalse-callbackidentity-thisarg" class="alias">`_.unique` -> `uniq`</a>
* <a href="#_ziparray" class="alias">`_.unzip` -> `zip`</a>
* <a href="#_withoutarray-value">`_.without`</a>
* <a href="#_xorarray">`_.xor`</a>
* <a href="#_ziparray">`_.zip`</a>
* <a href="#_zipobjectkeys-values">`_.zipObject`</a>

<!-- /div -->


<!-- div -->

## `Chaining`
* <a href="#_value">`_`</a>
* <a href="#_chainvalue">`_.chain`</a>
* <a href="#_tapvalue-interceptor">`_.tap`</a>
* <a href="#_prototypechain">`_.prototype.chain`</a>
* <a href="#_prototypetostring">`_.prototype.toString`</a>
* <a href="#_prototypevalueof" class="alias">`_.prototype.value` -> `valueOf`</a>
* <a href="#_prototypevalueof">`_.prototype.valueOf`</a>

<!-- /div -->


<!-- div -->

## `Collections`
* <a href="#_everycollection-callbackidentity-thisarg" class="alias">`_.all` -> `every`</a>
* <a href="#_somecollection-callbackidentity-thisarg" class="alias">`_.any` -> `some`</a>
* <a href="#_atcollection-index">`_.at`</a>
* <a href="#_mapcollection-callbackidentity-thisarg" class="alias">`_.collect` -> `map`</a>
* <a href="#_containscollection-target-fromindex0">`_.contains`</a>
* <a href="#_countbycollection-callbackidentity-thisarg">`_.countBy`</a>
* <a href="#_findcollection-callbackidentity-thisarg" class="alias">`_.detect` -> `find`</a>
* <a href="#_foreachcollection-callbackidentity-thisarg" class="alias">`_.each` -> `forEach`</a>
* <a href="#_foreachrightcollection-callbackidentity-thisarg" class="alias">`_.eachRight` -> `forEachRight`</a>
* <a href="#_everycollection-callbackidentity-thisarg">`_.every`</a>
* <a href="#_filtercollection-callbackidentity-thisarg">`_.filter`</a>
* <a href="#_findcollection-callbackidentity-thisarg">`_.find`</a>
* <a href="#_findlastcollection-callbackidentity-thisarg">`_.findLast`</a>
* <a href="#_findcollection-callbackidentity-thisarg" class="alias">`_.findWhere` -> `find`</a>
* <a href="#_reducecollection-callbackidentity-accumulator-thisarg" class="alias">`_.foldl` -> `reduce`</a>
* <a href="#_reducerightcollection-callbackidentity-accumulator-thisarg" class="alias">`_.foldr` -> `reduceRight`</a>
* <a href="#_foreachcollection-callbackidentity-thisarg">`_.forEach`</a>
* <a href="#_foreachrightcollection-callbackidentity-thisarg">`_.forEachRight`</a>
* <a href="#_groupbycollection-callbackidentity-thisarg">`_.groupBy`</a>
* <a href="#_containscollection-target-fromindex0" class="alias">`_.include` -> `contains`</a>
* <a href="#_indexbycollection-callbackidentity-thisarg">`_.indexBy`</a>
* <a href="#_reducecollection-callbackidentity-accumulator-thisarg" class="alias">`_.inject` -> `reduce`</a>
* <a href="#_invokecollection-methodname-arg">`_.invoke`</a>
* <a href="#_mapcollection-callbackidentity-thisarg">`_.map`</a>
* <a href="#_maxcollection-callbackidentity-thisarg">`_.max`</a>
* <a href="#_mincollection-callbackidentity-thisarg">`_.min`</a>
* <a href="#_pluckcollection-property">`_.pluck`</a>
* <a href="#_reducecollection-callbackidentity-accumulator-thisarg">`_.reduce`</a>
* <a href="#_reducerightcollection-callbackidentity-accumulator-thisarg">`_.reduceRight`</a>
* <a href="#_rejectcollection-callbackidentity-thisarg">`_.reject`</a>
* <a href="#_samplecollection-n">`_.sample`</a>
* <a href="#_filtercollection-callbackidentity-thisarg" class="alias">`_.select` -> `filter`</a>
* <a href="#_shufflecollection">`_.shuffle`</a>
* <a href="#_sizecollection">`_.size`</a>
* <a href="#_somecollection-callbackidentity-thisarg">`_.some`</a>
* <a href="#_sortbycollection-callbackidentity-thisarg">`_.sortBy`</a>
* <a href="#_toarraycollection">`_.toArray`</a>
* <a href="#_wherecollection-props">`_.where`</a>

<!-- /div -->


<!-- div -->

## `Functions`
* <a href="#_aftern-func">`_.after`</a>
* <a href="#_bindfunc-thisarg-arg">`_.bind`</a>
* <a href="#_bindallobject-methodname">`_.bindAll`</a>
* <a href="#_bindkeyobject-key-arg">`_.bindKey`</a>
* <a href="#_composefunc">`_.compose`</a>
* <a href="#_curryfunc-arityfunclength">`_.curry`</a>
* <a href="#_debouncefunc-wait-options-optionsmaxwait">`_.debounce`</a>
* <a href="#_deferfunc-arg">`_.defer`</a>
* <a href="#_delayfunc-wait-arg">`_.delay`</a>
* <a href="#_memoizefunc-resolver">`_.memoize`</a>
* <a href="#_oncefunc">`_.once`</a>
* <a href="#_partialfunc-arg">`_.partial`</a>
* <a href="#_partialrightfunc-arg">`_.partialRight`</a>
* <a href="#_throttlefunc-wait-options">`_.throttle`</a>
* <a href="#_wrapvalue-wrapper">`_.wrap`</a>

<!-- /div -->


<!-- div -->

## `Objects`
* <a href="#_assignobject-source-callback-thisarg">`_.assign`</a>
* <a href="#_clonevalue-isdeepfalse-callback-thisarg">`_.clone`</a>
* <a href="#_clonedeepvalue-callback-thisarg">`_.cloneDeep`</a>
* <a href="#_createprototype-properties">`_.create`</a>
* <a href="#_defaultsobject-source">`_.defaults`</a>
* <a href="#_assignobject-source-callback-thisarg" class="alias">`_.extend` -> `assign`</a>
* <a href="#_findkeyobject-callbackidentity-thisarg">`_.findKey`</a>
* <a href="#_findlastkeyobject-callbackidentity-thisarg">`_.findLastKey`</a>
* <a href="#_forinobject-callbackidentity-thisarg">`_.forIn`</a>
* <a href="#_forinrightobject-callbackidentity-thisarg">`_.forInRight`</a>
* <a href="#_forownobject-callbackidentity-thisarg">`_.forOwn`</a>
* <a href="#_forownrightobject-callbackidentity-thisarg">`_.forOwnRight`</a>
* <a href="#_functionsobject">`_.functions`</a>
* <a href="#_hasobject-key">`_.has`</a>
* <a href="#_invertobject">`_.invert`</a>
* <a href="#_isargumentsvalue">`_.isArguments`</a>
* <a href="#_isarrayvalue">`_.isArray`</a>
* <a href="#_isbooleanvalue">`_.isBoolean`</a>
* <a href="#_isdatevalue">`_.isDate`</a>
* <a href="#_iselementvalue">`_.isElement`</a>
* <a href="#_isemptyvalue">`_.isEmpty`</a>
* <a href="#_isequala-b-callback-thisarg">`_.isEqual`</a>
* <a href="#_isfinitevalue">`_.isFinite`</a>
* <a href="#_isfunctionvalue">`_.isFunction`</a>
* <a href="#_isnanvalue">`_.isNaN`</a>
* <a href="#_isnullvalue">`_.isNull`</a>
* <a href="#_isnumbervalue">`_.isNumber`</a>
* <a href="#_isobjectvalue">`_.isObject`</a>
* <a href="#_isplainobjectvalue">`_.isPlainObject`</a>
* <a href="#_isregexpvalue">`_.isRegExp`</a>
* <a href="#_isstringvalue">`_.isString`</a>
* <a href="#_isundefinedvalue">`_.isUndefined`</a>
* <a href="#_keysobject">`_.keys`</a>
* <a href="#_mapvaluesobject-callbackidentity-thisarg">`_.mapValues`</a>
* <a href="#_mergeobject-source-callback-thisarg">`_.merge`</a>
* <a href="#_functionsobject" class="alias">`_.methods` -> `functions`</a>
* <a href="#_omitobject-callback-thisarg">`_.omit`</a>
* <a href="#_pairsobject">`_.pairs`</a>
* <a href="#_pickobject-callback-thisarg">`_.pick`</a>
* <a href="#_transformobject-callbackidentity-accumulator-thisarg">`_.transform`</a>
* <a href="#_valuesobject">`_.values`</a>

<!-- /div -->


<!-- div -->

## `Utilities`
* <a href="#_now">`_.now`</a>
* <a href="#_constantvalue">`_.constant`</a>
* <a href="#_createcallbackfuncidentity-thisarg-argcount">`_.createCallback`</a>
* <a href="#_escapestring">`_.escape`</a>
* <a href="#_identityvalue">`_.identity`</a>
* <a href="#_mixinobjectlodash-source-options">`_.mixin`</a>
* <a href="#_noconflict">`_.noConflict`</a>
* <a href="#_noop">`_.noop`</a>
* <a href="#_parseintvalue-radix">`_.parseInt`</a>
* <a href="#_propertykey">`_.property`</a>
* <a href="#_randommin0-max1-floatingfalse">`_.random`</a>
* <a href="#_resultobject-key">`_.result`</a>
* <a href="#_runincontextcontextroot">`_.runInContext`</a>
* <a href="#_templatetext-data-options-optionsescape-optionsevaluate-optionsimports-optionsinterpolate-sourceurl-variable">`_.template`</a>
* <a href="#_timesn-callback-thisarg">`_.times`</a>
* <a href="#_unescapestring">`_.unescape`</a>
* <a href="#_uniqueidprefix">`_.uniqueId`</a>

<!-- /div -->


<!-- div -->

## `Methods`
* <a href="#_templatesettingsimports_">`_.templateSettings.imports._`</a>

<!-- /div -->


<!-- div -->

## `Properties`
* <a href="#_version">`_.VERSION`</a>
* <a href="#_support">`_.support`</a>
* <a href="#_supportargsclass">`_.support.argsClass`</a>
* <a href="#_supportargsobject">`_.support.argsObject`</a>
* <a href="#_supportenumerrorprops">`_.support.enumErrorProps`</a>
* <a href="#_supportenumprototypes">`_.support.enumPrototypes`</a>
* <a href="#_supportfuncdecomp">`_.support.funcDecomp`</a>
* <a href="#_supportfuncnames">`_.support.funcNames`</a>
* <a href="#_supportnonenumargs">`_.support.nonEnumArgs`</a>
* <a href="#_supportnonenumshadows">`_.support.nonEnumShadows`</a>
* <a href="#_supportownlast">`_.support.ownLast`</a>
* <a href="#_supportspliceobjects">`_.support.spliceObjects`</a>
* <a href="#_supportunindexedchars">`_.support.unindexedChars`</a>
* <a href="#_templatesettings">`_.templateSettings`</a>
* <a href="#_templatesettingsescape">`_.templateSettings.escape`</a>
* <a href="#_templatesettingsevaluate">`_.templateSettings.evaluate`</a>
* <a href="#_templatesettingsinterpolate">`_.templateSettings.interpolate`</a>
* <a href="#_templatesettingsvariable">`_.templateSettings.variable`</a>
* <a href="#_templatesettingsimports">`_.templateSettings.imports`</a>

<!-- /div -->


<!-- /div -->


<!-- div -->


<!-- div -->

## `“Arrays” Methods`

<!-- div -->

### <a id="_compactarray"></a>`_.compact(array)`
<a href="#_compactarray">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4479 "View in source") [&#x24C9;][1]

Creates an array with all falsey values removed. The values `false`, `null`, `0`, `""`, `undefined`, and `NaN` are all falsey.

#### Arguments
1. `array` *(Array)*: The array to compact.

#### Returns
*(Array)*: Returns a new array of filtered values.

#### Example
```js
_.compact([0, 1, false, 2, '', 3]);
// => [1, 2, 3]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_differencearray-values"></a>`_.difference(array, [values])`
<a href="#_differencearray-values">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4508 "View in source") [&#x24C9;][1]

Creates an array excluding all values of the provided arrays using strict equality for comparisons, i.e. `===`.

#### Arguments
1. `array` *(Array)*: The array to process.
2. `[values]` *(...Array)*: The arrays of values to exclude.

#### Returns
*(Array)*: Returns a new array of filtered values.

#### Example
```js
_.difference([1, 2, 3, 4, 5], [5, 2, 10]);
// => [1, 3, 4]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_findindexarray-callbackidentity-thisarg"></a>`_.findIndex(array, [callback=identity], [thisArg])`
<a href="#_findindexarray-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4553 "View in source") [&#x24C9;][1]

This method is like `_.find` except that it returns the index of the first element that passes the callback check, instead of the element itself.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `array` *(Array)*: The array to search.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(number)*: Returns the index of the found element, else `-1`.

#### Example
```js
var characters = [
  { 'name': 'barney',  'age': 36, 'blocked': false },
  { 'name': 'fred',    'age': 40, 'blocked': true },
  { 'name': 'pebbles', 'age': 1,  'blocked': false }
];

_.findIndex(characters, function(chr) {
  return chr.age < 20;
});
// => 2

// using "_.where" callback shorthand
_.findIndex(characters, { 'age': 36 });
// => 0

// using "_.pluck" callback shorthand
_.findIndex(characters, 'blocked');
// => 1
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_findlastindexarray-callbackidentity-thisarg"></a>`_.findLastIndex(array, [callback=identity], [thisArg])`
<a href="#_findlastindexarray-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4607 "View in source") [&#x24C9;][1]

This method is like `_.findIndex` except that it iterates over elements of a `collection` from right to left.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `array` *(Array)*: The array to search.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(number)*: Returns the index of the found element, else `-1`.

#### Example
```js
var characters = [
  { 'name': 'barney',  'age': 36, 'blocked': true },
  { 'name': 'fred',    'age': 40, 'blocked': false },
  { 'name': 'pebbles', 'age': 1,  'blocked': true }
];

_.findLastIndex(characters, function(chr) {
  return chr.age > 30;
});
// => 1

// using "_.where" callback shorthand
_.findLastIndex(characters, { 'age': 36 });
// => 0

// using "_.pluck" callback shorthand
_.findLastIndex(characters, 'blocked');
// => 2
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_firstarray-callback-thisarg"></a>`_.first(array, [callback], [thisArg])`
<a href="#_firstarray-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4669 "View in source") [&#x24C9;][1]

Gets the first element or first `n` elements of an array. If a callback is provided elements at the beginning of the array are returned as long as the callback returns truey. The callback is bound to `thisArg` and invoked with three arguments; *(value, index, array)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Aliases
*_.head, _.take*

#### Arguments
1. `array` *(Array)*: The array to query.
2. `[callback]` *(Function|Object|number|string)*: The function called per element or the number of elements to return. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the first element(s) of `array`.

#### Example
```js
_.first([1, 2, 3]);
// => 1

_.first([1, 2, 3], 2);
// => [1, 2]

_.first([1, 2, 3], function(num) {
  return num < 3;
});
// => [1, 2]

var characters = [
  { 'name': 'barney',  'blocked': true,  'employer': 'slate' },
  { 'name': 'fred',    'blocked': false, 'employer': 'slate' },
  { 'name': 'pebbles', 'blocked': true,  'employer': 'na' }
];

// using "_.pluck" callback shorthand
_.first(characters, 'blocked');
// => [{ 'name': 'barney', 'blocked': true, 'employer': 'slate' }]

// using "_.where" callback shorthand
_.pluck(_.first(characters, { 'employer': 'slate' }), 'name');
// => ['barney', 'fred']
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_flattenarray-isshallowfalse-callbackidentity-thisarg"></a>`_.flatten(array, [isShallow=false], [callback=identity], [thisArg])`
<a href="#_flattenarray-isshallowfalse-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4729 "View in source") [&#x24C9;][1]

Flattens a nested array *(the nesting can be to any depth)*. If `isShallow` is truey, the array will only be flattened a single level. If a callback is provided each element of the array is passed through the callback before flattening. The callback is bound to `thisArg` and invoked with three arguments; *(value, index, array)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `array` *(Array)*: The array to flatten.
2. `[isShallow=false]` *(boolean)*: A flag to restrict flattening to a single level.
3. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a new flattened array.

#### Example
```js
_.flatten([1, [2], [3, [[4]]]]);
// => [1, 2, 3, 4];

_.flatten([1, [2], [3, [[4]]]], true);
// => [1, 2, 3, [[4]]];

var characters = [
  { 'name': 'barney', 'age': 30, 'pets': ['hoppy'] },
  { 'name': 'fred',   'age': 40, 'pets': ['baby puss', 'dino'] }
];

// using "_.pluck" callback shorthand
_.flatten(characters, 'pets');
// => ['hoppy', 'baby puss', 'dino']
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_indexofarray-value-fromindex0"></a>`_.indexOf(array, value, [fromIndex=0])`
<a href="#_indexofarray-value-fromindex0">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4766 "View in source") [&#x24C9;][1]

Gets the index at which the first occurrence of `value` is found using strict equality for comparisons, i.e. `===`. If the array is already sorted providing `true` for `fromIndex` will run a faster binary search.

#### Arguments
1. `array` *(Array)*: The array to search.
2. `value` *(&#42;)*: The value to search for.
3. `[fromIndex=0]` *(boolean|number)*: The index to search from or `true` to perform a binary search on a sorted array.

#### Returns
*(number)*: Returns the index of the matched value or `-1`.

#### Example
```js
_.indexOf([1, 2, 3, 1, 2, 3], 2);
// => 1

_.indexOf([1, 2, 3, 1, 2, 3], 2, 3);
// => 4

_.indexOf([1, 1, 2, 2, 3, 3], 2, true);
// => 2
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_initialarray-callback1-thisarg"></a>`_.initial(array, [callback=1], [thisArg])`
<a href="#_initialarray-callback1-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4827 "View in source") [&#x24C9;][1]

Gets all but the last element or last `n` elements of an array. If a callback is provided elements at the end of the array are excluded from the result as long as the callback returns truey. The callback is bound to `thisArg` and invoked with three arguments; *(value, index, array)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `array` *(Array)*: The array to query.
2. `[callback=1]` *(Function|Object|number|string)*: The function called per element or the number of elements to exclude. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a slice of `array`.

#### Example
```js
_.initial([1, 2, 3]);
// => [1, 2]

_.initial([1, 2, 3], 2);
// => [1]

_.initial([1, 2, 3], function(num) {
  return num > 1;
});
// => [1]

var characters = [
  { 'name': 'barney',  'blocked': false, 'employer': 'slate' },
  { 'name': 'fred',    'blocked': true,  'employer': 'slate' },
  { 'name': 'pebbles', 'blocked': true,  'employer': 'na' }
];

// using "_.pluck" callback shorthand
_.initial(characters, 'blocked');
// => [{ 'name': 'barney',  'blocked': false, 'employer': 'slate' }]

// using "_.where" callback shorthand
_.pluck(_.initial(characters, { 'employer': 'na' }), 'name');
// => ['barney', 'fred']
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_intersectionarray"></a>`_.intersection([array])`
<a href="#_intersectionarray">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4857 "View in source") [&#x24C9;][1]

Creates an array of unique values present in all provided arrays using strict equality for comparisons, i.e. `===`.

#### Arguments
1. `[array]` *(...Array)*: The arrays to inspect.

#### Returns
*(Array)*: Returns an array of shared values.

#### Example
```js
_.intersection([1, 2, 3], [5, 2, 1, 4], [2, 1]);
// => [1, 2]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_lastarray-callback-thisarg"></a>`_.last(array, [callback], [thisArg])`
<a href="#_lastarray-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4957 "View in source") [&#x24C9;][1]

Gets the last element or last `n` elements of an array. If a callback is provided elements at the end of the array are returned as long as the callback returns truey. The callback is bound to `thisArg` and invoked with three arguments; *(value, index, array)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `array` *(Array)*: The array to query.
2. `[callback]` *(Function|Object|number|string)*: The function called per element or the number of elements to return. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the last element(s) of `array`.

#### Example
```js
_.last([1, 2, 3]);
// => 3

_.last([1, 2, 3], 2);
// => [2, 3]

_.last([1, 2, 3], function(num) {
  return num > 1;
});
// => [2, 3]

var characters = [
  { 'name': 'barney',  'blocked': false, 'employer': 'slate' },
  { 'name': 'fred',    'blocked': true,  'employer': 'slate' },
  { 'name': 'pebbles', 'blocked': true,  'employer': 'na' }
];

// using "_.pluck" callback shorthand
_.pluck(_.last(characters, 'blocked'), 'name');
// => ['fred', 'pebbles']

// using "_.where" callback shorthand
_.last(characters, { 'employer': 'na' });
// => [{ 'name': 'pebbles', 'blocked': true, 'employer': 'na' }]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_lastindexofarray-value-fromindexarraylength-1"></a>`_.lastIndexOf(array, value, [fromIndex=array.length-1])`
<a href="#_lastindexofarray-value-fromindexarraylength-1">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5003 "View in source") [&#x24C9;][1]

Gets the index at which the last occurrence of `value` is found using strict equality for comparisons, i.e. `===`. If `fromIndex` is negative, it is used as the offset from the end of the collection.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `array` *(Array)*: The array to search.
2. `value` *(&#42;)*: The value to search for.
3. `[fromIndex=array.length-1]` *(number)*: The index to search from.

#### Returns
*(number)*: Returns the index of the matched value or `-1`.

#### Example
```js
_.lastIndexOf([1, 2, 3, 1, 2, 3], 2);
// => 4

_.lastIndexOf([1, 2, 3, 1, 2, 3], 2, 3);
// => 1
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_pullarray-value"></a>`_.pull(array, [value])`
<a href="#_pullarray-value">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5033 "View in source") [&#x24C9;][1]

Removes all provided values from the given array using strict equality for comparisons, i.e. `===`.

#### Arguments
1. `array` *(Array)*: The array to modify.
2. `[value]` *(...&#42;)*: The values to remove.

#### Returns
*(Array)*: Returns `array`.

#### Example
```js
var array = [1, 2, 3, 1, 2, 3];
_.pull(array, 2, 3);
console.log(array);
// => [1, 1]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_rangestart0-end-step1"></a>`_.range([start=0], end, [step=1])`
<a href="#_rangestart0-end-step1">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5084 "View in source") [&#x24C9;][1]

Creates an array of numbers *(positive and/or negative)* progressing from `start` up to but not including `end`. If `start` is less than `stop` a zero-length range is created unless a negative `step` is specified.

#### Arguments
1. `[start=0]` *(number)*: The start of the range.
2. `end` *(number)*: The end of the range.
3. `[step=1]` *(number)*: The value to increment or decrement by.

#### Returns
*(Array)*: Returns a new range array.

#### Example
```js
_.range(4);
// => [0, 1, 2, 3]

_.range(1, 5);
// => [1, 2, 3, 4]

_.range(0, 20, 5);
// => [0, 5, 10, 15]

_.range(0, -4, -1);
// => [0, -1, -2, -3]

_.range(1, 4, 0);
// => [1, 1, 1]

_.range(0);
// => []
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_removearray-callbackidentity-thisarg"></a>`_.remove(array, [callback=identity], [thisArg])`
<a href="#_removearray-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5137 "View in source") [&#x24C9;][1]

Removes all elements from an array that the callback returns truey for and returns an array of removed elements. The callback is bound to `thisArg` and invoked with three arguments; *(value, index, array)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `array` *(Array)*: The array to modify.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a new array of removed elements.

#### Example
```js
var array = [1, 2, 3, 4, 5, 6];
var evens = _.remove(array, function(num) { return num % 2 == 0; });

console.log(array);
// => [1, 3, 5]

console.log(evens);
// => [2, 4, 6]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_restarray-callback1-thisarg"></a>`_.rest(array, [callback=1], [thisArg])`
<a href="#_restarray-callback1-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5206 "View in source") [&#x24C9;][1]

The opposite of `_.initial` this method gets all but the first element or first `n` elements of an array. If a callback function is provided elements at the beginning of the array are excluded from the result as long as the callback returns truey. The callback is bound to `thisArg` and invoked with three arguments; *(value, index, array)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Aliases
*_.drop, _.tail*

#### Arguments
1. `array` *(Array)*: The array to query.
2. `[callback=1]` *(Function|Object|number|string)*: The function called per element or the number of elements to exclude. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a slice of `array`.

#### Example
```js
_.rest([1, 2, 3]);
// => [2, 3]

_.rest([1, 2, 3], 2);
// => [3]

_.rest([1, 2, 3], function(num) {
  return num < 3;
});
// => [3]

var characters = [
  { 'name': 'barney',  'blocked': true,  'employer': 'slate' },
  { 'name': 'fred',    'blocked': false,  'employer': 'slate' },
  { 'name': 'pebbles', 'blocked': true, 'employer': 'na' }
];

// using "_.pluck" callback shorthand
_.pluck(_.rest(characters, 'blocked'), 'name');
// => ['fred', 'pebbles']

// using "_.where" callback shorthand
_.rest(characters, { 'employer': 'slate' });
// => [{ 'name': 'pebbles', 'blocked': true, 'employer': 'na' }]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_sortedindexarray-value-callbackidentity-thisarg"></a>`_.sortedIndex(array, value, [callback=identity], [thisArg])`
<a href="#_sortedindexarray-value-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5270 "View in source") [&#x24C9;][1]

Uses a binary search to determine the smallest index at which a value should be inserted into a given sorted array in order to maintain the sort order of the array. If a callback is provided it will be executed for `value` and each element of `array` to compute their sort ranking. The callback is bound to `thisArg` and invoked with one argument; *(value)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `array` *(Array)*: The array to inspect.
2. `value` *(&#42;)*: The value to evaluate.
3. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(number)*: Returns the index at which `value` should be inserted  into `array`.

#### Example
```js
_.sortedIndex([20, 30, 50], 40);
// => 2

// using "_.pluck" callback shorthand
_.sortedIndex([{ 'x': 20 }, { 'x': 30 }, { 'x': 50 }], { 'x': 40 }, 'x');
// => 2

var dict = {
  'wordToNumber': { 'twenty': 20, 'thirty': 30, 'fourty': 40, 'fifty': 50 }
};

_.sortedIndex(['twenty', 'thirty', 'fifty'], 'fourty', function(word) {
  return dict.wordToNumber[word];
});
// => 2

_.sortedIndex(['twenty', 'thirty', 'fifty'], 'fourty', function(word) {
  return this.wordToNumber[word];
}, dict);
// => 2
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_unionarray"></a>`_.union([array])`
<a href="#_unionarray">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5301 "View in source") [&#x24C9;][1]

Creates an array of unique values, in order, of the provided arrays using strict equality for comparisons, i.e. `===`.

#### Arguments
1. `[array]` *(...Array)*: The arrays to inspect.

#### Returns
*(Array)*: Returns an array of combined values.

#### Example
```js
_.union([1, 2, 3], [5, 2, 1, 4], [2, 1]);
// => [1, 2, 3, 5, 4]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_uniqarray-issortedfalse-callbackidentity-thisarg"></a>`_.uniq(array, [isSorted=false], [callback=identity], [thisArg])`
<a href="#_uniqarray-issortedfalse-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5349 "View in source") [&#x24C9;][1]

Creates a duplicate-value-free version of an array using strict equality for comparisons, i.e. `===`. If the array is sorted, providing `true` for `isSorted` will use a faster algorithm. If a callback is provided each element of `array` is passed through the callback before uniqueness is computed. The callback is bound to `thisArg` and invoked with three arguments; *(value, index, array)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Aliases
*_.unique*

#### Arguments
1. `array` *(Array)*: The array to process.
2. `[isSorted=false]` *(boolean)*: A flag to indicate that `array` is sorted.
3. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a duplicate-value-free array.

#### Example
```js
_.uniq([1, 2, 1, 3, 1]);
// => [1, 2, 3]

_.uniq([1, 1, 2, 2, 3], true);
// => [1, 2, 3]

_.uniq(['A', 'b', 'C', 'a', 'B', 'c'], function(letter) { return letter.toLowerCase(); });
// => ['A', 'b', 'C']

_.uniq([1, 2.5, 3, 1.5, 2, 3.5], function(num) { return this.floor(num); }, Math);
// => [1, 2.5, 3]

// using "_.pluck" callback shorthand
_.uniq([{ 'x': 1 }, { 'x': 2 }, { 'x': 1 }], 'x');
// => [{ 'x': 1 }, { 'x': 2 }]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_withoutarray-value"></a>`_.without(array, [value])`
<a href="#_withoutarray-value">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5377 "View in source") [&#x24C9;][1]

Creates an array excluding all provided values using strict equality for comparisons, i.e. `===`.

#### Arguments
1. `array` *(Array)*: The array to filter.
2. `[value]` *(...&#42;)*: The values to exclude.

#### Returns
*(Array)*: Returns a new array of filtered values.

#### Example
```js
_.without([1, 2, 1, 0, 3, 1, 4], 0, 1);
// => [2, 3, 4]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_xorarray"></a>`_.xor([array])`
<a href="#_xorarray">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5398 "View in source") [&#x24C9;][1]

Creates an array that is the symmetric difference of the provided arrays. See http://en.wikipedia.org/wiki/Symmetric_difference.

#### Arguments
1. `[array]` *(...Array)*: The arrays to inspect.

#### Returns
*(Array)*: Returns an array of values.

#### Example
```js
_.xor([1, 2, 3], [5, 2, 1, 4]);
// => [3, 5, 4]

_.xor([1, 2, 5], [2, 3, 5], [3, 4, 5]);
// => [1, 4, 5]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_ziparray"></a>`_.zip([array])`
<a href="#_ziparray">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5429 "View in source") [&#x24C9;][1]

Creates an array of grouped elements, the first of which contains the first elements of the given arrays, the second of which contains the second elements of the given arrays, and so on.

#### Aliases
*_.unzip*

#### Arguments
1. `[array]` *(...Array)*: Arrays to process.

#### Returns
*(Array)*: Returns a new array of grouped elements.

#### Example
```js
_.zip(['fred', 'barney'], [30, 40], [true, false]);
// => [['fred', 30, true], ['barney', 40, false]]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_zipobjectkeys-values"></a>`_.zipObject(keys, [values=[]])`
<a href="#_zipobjectkeys-values">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5459 "View in source") [&#x24C9;][1]

Creates an object composed from arrays of `keys` and `values`. Provide either a single two dimensional array, i.e. `[[key1, value1], [key2, value2]]` or two arrays, one of `keys` and one of corresponding `values`.

#### Aliases
*_.object*

#### Arguments
1. `keys` *(Array)*: The array of keys.
2. `[values=[]]` *(Array)*: The array of values.

#### Returns
*(Object)*: Returns an object composed of the given keys and  corresponding values.

#### Example
```js
_.zipObject(['fred', 'barney'], [30, 40]);
// => { 'fred': 30, 'barney': 40 }
```

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `“Chaining” Methods`

<!-- div -->

### <a id="_value"></a>`_(value)`
<a href="#_value">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L647 "View in source") [&#x24C9;][1]

Creates a `lodash` object which wraps the given value to enable intuitive method chaining.

In addition to Lo-Dash methods, wrappers also have the following `Array` methods:<br>
`concat`, `join`, `pop`, `push`, `reverse`, `shift`, `slice`, `sort`, `splice`, and `unshift`

Chaining is supported in custom builds as long as the `value` method is implicitly or explicitly included in the build.

The chainable wrapper functions are:<br>
`after`, `assign`, `bind`, `bindAll`, `bindKey`, `chain`, `compact`, `compose`, `concat`, `countBy`, `create`, `createCallback`, `curry`, `debounce`, `defaults`, `defer`, `delay`, `difference`, `filter`, `flatten`, `forEach`, `forEachRight`, `forIn`, `forInRight`, `forOwn`, `forOwnRight`, `functions`, `groupBy`, `indexBy`, `initial`, `intersection`, `invert`, `invoke`, `keys`, `map`, `max`, `memoize`, `merge`, `min`, `object`, `omit`, `once`, `pairs`, `partial`, `partialRight`, `pick`, `pluck`, `pull`, `push`, `range`, `reject`, `remove`, `rest`, `reverse`, `shuffle`, `slice`, `sort`, `sortBy`, `splice`, `tap`, `throttle`, `times`, `toArray`, `transform`, `union`, `uniq`, `unshift`, `unzip`, `values`, `where`, `without`, `wrap`, and `zip`

The non-chainable wrapper functions are:<br>
`clone`, `cloneDeep`, `contains`, `escape`, `every`, `find`, `findIndex`, `findKey`, `findLast`, `findLastIndex`, `findLastKey`, `has`, `identity`, `indexOf`, `isArguments`, `isArray`, `isBoolean`, `isDate`, `isElement`, `isEmpty`, `isEqual`, `isFinite`, `isFunction`, `isNaN`, `isNull`, `isNumber`, `isObject`, `isPlainObject`, `isRegExp`, `isString`, `isUndefined`, `join`, `lastIndexOf`, `mixin`, `noConflict`, `parseInt`, `pop`, `random`, `reduce`, `reduceRight`, `result`, `shift`, `size`, `some`, `sortedIndex`, `runInContext`, `template`, `unescape`, `uniqueId`, and `value`

The wrapper functions `first` and `last` return wrapped values when `n` is provided, otherwise they return unwrapped values.

Explicit chaining can be enabled by using the `_.chain` method.

#### Arguments
1. `value` *(&#42;)*: The value to wrap in a `lodash` instance.

#### Returns
*(Object)*: Returns a `lodash` instance.

#### Example
```js
var wrapped = _([1, 2, 3]);

// returns an unwrapped value
wrapped.reduce(function(sum, num) {
  return sum + num;
});
// => 6

// returns a wrapped value
var squares = wrapped.map(function(num) {
  return num * num;
});

_.isArray(squares);
// => false

_.isArray(squares.value());
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_chainvalue"></a>`_.chain(value)`
<a href="#_chainvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6788 "View in source") [&#x24C9;][1]

Creates a `lodash` object that wraps the given value with explicit method chaining enabled.

#### Arguments
1. `value` *(&#42;)*: The value to wrap.

#### Returns
*(Object)*: Returns the wrapper object.

#### Example
```js
var characters = [
  { 'name': 'barney',  'age': 36 },
  { 'name': 'fred',    'age': 40 },
  { 'name': 'pebbles', 'age': 1 }
];

var youngest = _.chain(characters)
    .sortBy('age')
    .map(function(chr) { return chr.name + ' is ' + chr.age; })
    .first()
    .value();
// => 'pebbles is 1'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_tapvalue-interceptor"></a>`_.tap(value, interceptor)`
<a href="#_tapvalue-interceptor">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6814 "View in source") [&#x24C9;][1]

Invokes `interceptor` with the `value` as the first argument and then returns `value`. The purpose of this method is to "tap into" a method chain in order to perform operations on intermediate results within the chain.

#### Arguments
1. `value` *(&#42;)*: The value to provide to `interceptor`.
2. `interceptor` *(Function)*: The function to invoke.

#### Returns
*(&#42;)*: Returns `value`.

#### Example
```js
_([1, 2, 3, 4])
 .tap(function(array) { array.pop(); })
 .reverse()
 .value();
// => [3, 2, 1]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_prototypechain"></a>`_.prototype.chain()`
<a href="#_prototypechain">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6844 "View in source") [&#x24C9;][1]

Enables explicit method chaining on the wrapper object.

#### Returns
*(&#42;)*: Returns the wrapper object.

#### Example
```js
var characters = [
  { 'name': 'barney', 'age': 36 },
  { 'name': 'fred',   'age': 40 }
];

// without explicit chaining
_(characters).first();
// => { 'name': 'barney', 'age': 36 }

// with explicit chaining
_(characters).chain()
  .first()
  .pick('age')
  .value();
// => { 'age': 36 }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_prototypetostring"></a>`_.prototype.toString()`
<a href="#_prototypetostring">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6861 "View in source") [&#x24C9;][1]

Produces the `toString` result of the wrapped value.

#### Returns
*(string)*: Returns the string result.

#### Example
```js
_([1, 2, 3]).toString();
// => '1,2,3'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_prototypevalueof"></a>`_.prototype.valueOf()`
<a href="#_prototypevalueof">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6878 "View in source") [&#x24C9;][1]

Extracts the wrapped value.

#### Aliases
*_.prototype.value*

#### Returns
*(&#42;)*: Returns the wrapped value.

#### Example
```js
_([1, 2, 3]).valueOf();
// => [1, 2, 3]
```

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `“Collections” Methods`

<!-- div -->

### <a id="_atcollection-index"></a>`_.at(collection, [index])`
<a href="#_atcollection-index">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3296 "View in source") [&#x24C9;][1]

Creates an array of elements from the specified indexes, or keys, of the `collection`. Indexes may be specified as individual arguments or as arrays of indexes.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[index]` *(...(number|number&#91;&#93;|string|string&#91;&#93;)*: The indexes of `collection` to retrieve, specified as individual indexes or arrays of indexes.

#### Returns
*(Array)*: Returns a new array of elements corresponding to the  provided indexes.

#### Example
```js
_.at(['a', 'b', 'c', 'd', 'e'], [0, 2, 4]);
// => ['a', 'c', 'e']

_.at(['fred', 'barney', 'pebbles'], 0, 2);
// => ['fred', 'pebbles']
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_containscollection-target-fromindex0"></a>`_.contains(collection, target, [fromIndex=0])`
<a href="#_containscollection-target-fromindex0">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3339 "View in source") [&#x24C9;][1]

Checks if a given value is present in a collection using strict equality for comparisons, i.e. `===`. If `fromIndex` is negative, it is used as the offset from the end of the collection.

#### Aliases
*_.include*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `target` *(&#42;)*: The value to check for.
3. `[fromIndex=0]` *(number)*: The index to search from.

#### Returns
*(boolean)*: Returns `true` if the `target` element is found, else `false`.

#### Example
```js
_.contains([1, 2, 3], 1);
// => true

_.contains([1, 2, 3], 1, 2);
// => false

_.contains({ 'name': 'fred', 'age': 40 }, 'fred');
// => true

_.contains('pebbles', 'eb');
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_countbycollection-callbackidentity-thisarg"></a>`_.countBy(collection, [callback=identity], [thisArg])`
<a href="#_countbycollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3394 "View in source") [&#x24C9;][1]

Creates an object composed of keys generated from the results of running each element of `collection` through the callback. The corresponding value of each key is the number of times the key was returned by the callback. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns the composed aggregate object.

#### Example
```js
_.countBy([4.3, 6.1, 6.4], function(num) { return Math.floor(num); });
// => { '4': 1, '6': 2 }

_.countBy([4.3, 6.1, 6.4], function(num) { return this.floor(num); }, Math);
// => { '4': 1, '6': 2 }

_.countBy(['one', 'two', 'three'], 'length');
// => { '3': 2, '5': 1 }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_everycollection-callbackidentity-thisarg"></a>`_.every(collection, [callback=identity], [thisArg])`
<a href="#_everycollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3439 "View in source") [&#x24C9;][1]

Checks if the given callback returns truey value for &#42;&#42;all&#42;&#42; elements of a collection. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Aliases
*_.all*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(boolean)*: Returns `true` if all elements passed the callback check,  else `false`.

#### Example
```js
_.every([true, 1, null, 'yes']);
// => false

var characters = [
  { 'name': 'barney', 'age': 36 },
  { 'name': 'fred',   'age': 40 }
];

// using "_.pluck" callback shorthand
_.every(characters, 'age');
// => true

// using "_.where" callback shorthand
_.every(characters, { 'age': 36 });
// => false
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_filtercollection-callbackidentity-thisarg"></a>`_.filter(collection, [callback=identity], [thisArg])`
<a href="#_filtercollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3500 "View in source") [&#x24C9;][1]

Iterates over elements of a collection, returning an array of all elements the callback returns truey for. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Aliases
*_.select*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a new array of elements that passed the callback check.

#### Example
```js
var evens = _.filter([1, 2, 3, 4, 5, 6], function(num) { return num % 2 == 0; });
// => [2, 4, 6]

var characters = [
  { 'name': 'barney', 'age': 36, 'blocked': false },
  { 'name': 'fred',   'age': 40, 'blocked': true }
];

// using "_.pluck" callback shorthand
_.filter(characters, 'blocked');
// => [{ 'name': 'fred', 'age': 40, 'blocked': true }]

// using "_.where" callback shorthand
_.filter(characters, { 'age': 36 });
// => [{ 'name': 'barney', 'age': 36, 'blocked': false }]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_findcollection-callbackidentity-thisarg"></a>`_.find(collection, [callback=identity], [thisArg])`
<a href="#_findcollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3567 "View in source") [&#x24C9;][1]

Iterates over elements of a collection, returning the first element that the callback returns truey for. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Aliases
*_.detect, _.findWhere*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the found element, else `undefined`.

#### Example
```js
var characters = [
  { 'name': 'barney',  'age': 36, 'blocked': false },
  { 'name': 'fred',    'age': 40, 'blocked': true },
  { 'name': 'pebbles', 'age': 1,  'blocked': false }
];

_.find(characters, function(chr) {
  return chr.age < 40;
});
// => { 'name': 'barney', 'age': 36, 'blocked': false }

// using "_.where" callback shorthand
_.find(characters, { 'age': 1 });
// =>  { 'name': 'pebbles', 'age': 1, 'blocked': false }

// using "_.pluck" callback shorthand
_.find(characters, 'blocked');
// => { 'name': 'fred', 'age': 40, 'blocked': true }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_findlastcollection-callbackidentity-thisarg"></a>`_.findLast(collection, [callback=identity], [thisArg])`
<a href="#_findlastcollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3612 "View in source") [&#x24C9;][1]

This method is like `_.find` except that it iterates over elements of a `collection` from right to left.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the found element, else `undefined`.

#### Example
```js
_.findLast([1, 2, 3, 4], function(num) {
  return num % 2 == 1;
});
// => 3
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_foreachcollection-callbackidentity-thisarg"></a>`_.forEach(collection, [callback=identity], [thisArg])`
<a href="#_foreachcollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3650 "View in source") [&#x24C9;][1]

Iterates over elements of a collection, executing the callback for each element. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*. Callbacks may exit iteration early by explicitly returning `false`.

Note: As with other "Collections" methods, objects with a `length` property are iterated like arrays. To avoid this behavior `_.forIn` or `_.forOwn` may be used for object iteration.

#### Aliases
*_.each*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function)*: The function called per iteration.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array, Object, string)*: Returns `collection`.

#### Example
```js
_([1, 2, 3]).forEach(function(num) { console.log(num); }).join(',');
// => logs each number and returns '1,2,3'

_.forEach({ 'one': 1, 'two': 2, 'three': 3 }, function(num) { console.log(num); });
// => logs each number and returns the object (property order is not guaranteed across environments)
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_foreachrightcollection-callbackidentity-thisarg"></a>`_.forEachRight(collection, [callback=identity], [thisArg])`
<a href="#_foreachrightcollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3683 "View in source") [&#x24C9;][1]

This method is like `_.forEach` except that it iterates over elements of a `collection` from right to left.

#### Aliases
*_.eachRight*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function)*: The function called per iteration.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array, Object, string)*: Returns `collection`.

#### Example
```js
_([1, 2, 3]).forEachRight(function(num) { console.log(num); }).join(',');
// => logs each number from right to left and returns '3,2,1'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_groupbycollection-callbackidentity-thisarg"></a>`_.groupBy(collection, [callback=identity], [thisArg])`
<a href="#_groupbycollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3744 "View in source") [&#x24C9;][1]

Creates an object composed of keys generated from the results of running each element of a collection through the callback. The corresponding value of each key is an array of the elements responsible for generating the key. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns the composed aggregate object.

#### Example
```js
_.groupBy([4.2, 6.1, 6.4], function(num) { return Math.floor(num); });
// => { '4': [4.2], '6': [6.1, 6.4] }

_.groupBy([4.2, 6.1, 6.4], function(num) { return this.floor(num); }, Math);
// => { '4': [4.2], '6': [6.1, 6.4] }

// using "_.pluck" callback shorthand
_.groupBy(['one', 'two', 'three'], 'length');
// => { '3': ['one', 'two'], '5': ['three'] }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_indexbycollection-callbackidentity-thisarg"></a>`_.indexBy(collection, [callback=identity], [thisArg])`
<a href="#_indexbycollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3787 "View in source") [&#x24C9;][1]

Creates an object composed of keys generated from the results of running each element of the collection through the given callback. The corresponding value of each key is the last element responsible for generating the key. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns the composed aggregate object.

#### Example
```js
var keys = [
  { 'dir': 'left', 'code': 97 },
  { 'dir': 'right', 'code': 100 }
];

_.indexBy(keys, 'dir');
// => { 'left': { 'dir': 'left', 'code': 97 }, 'right': { 'dir': 'right', 'code': 100 } }

_.indexBy(keys, function(key) { return String.fromCharCode(key.code); });
// => { 'a': { 'dir': 'left', 'code': 97 }, 'd': { 'dir': 'right', 'code': 100 } }

_.indexBy(characters, function(key) { this.fromCharCode(key.code); }, String);
// => { 'a': { 'dir': 'left', 'code': 97 }, 'd': { 'dir': 'right', 'code': 100 } }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_invokecollection-methodname-arg"></a>`_.invoke(collection, methodName, [arg])`
<a href="#_invokecollection-methodname-arg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3813 "View in source") [&#x24C9;][1]

Invokes the method named by `methodName` on each element in the `collection` returning an array of the results of each invoked method. Additional arguments will be provided to each invoked method. If `methodName` is a function it will be invoked for, and `this` bound to, each element in the `collection`.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `methodName` *(Function|string)*: The name of the method to invoke or the function invoked per iteration.
3. `[arg]` *(...&#42;)*: Arguments to invoke the method with.

#### Returns
*(Array)*: Returns a new array of the results of each invoked method.

#### Example
```js
_.invoke([[5, 1, 7], [3, 2, 1]], 'sort');
// => [[1, 5, 7], [1, 2, 3]]

_.invoke([123, 456], String.prototype.split, '');
// => [['1', '2', '3'], ['4', '5', '6']]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_mapcollection-callbackidentity-thisarg"></a>`_.map(collection, [callback=identity], [thisArg])`
<a href="#_mapcollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3865 "View in source") [&#x24C9;][1]

Creates an array of values by running each element in the collection through the callback. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Aliases
*_.collect*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a new array of the results of each `callback` execution.

#### Example
```js
_.map([1, 2, 3], function(num) { return num * 3; });
// => [3, 6, 9]

_.map({ 'one': 1, 'two': 2, 'three': 3 }, function(num) { return num * 3; });
// => [3, 6, 9] (property order is not guaranteed across environments)

var characters = [
  { 'name': 'barney', 'age': 36 },
  { 'name': 'fred',   'age': 40 }
];

// using "_.pluck" callback shorthand
_.map(characters, 'name');
// => ['barney', 'fred']
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_maxcollection-callbackidentity-thisarg"></a>`_.max(collection, [callback=identity], [thisArg])`
<a href="#_maxcollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3923 "View in source") [&#x24C9;][1]

Retrieves the maximum value of a collection. If the collection is empty or falsey `-Infinity` is returned. If a callback is provided it will be executed for each value in the collection to generate the criterion by which the value is ranked. The callback is bound to `thisArg` and invoked with three arguments; *(value, index, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the maximum value.

#### Example
```js
_.max([4, 2, 8, 6]);
// => 8

var characters = [
  { 'name': 'barney', 'age': 36 },
  { 'name': 'fred',   'age': 40 }
];

_.max(characters, function(chr) { return chr.age; });
// => { 'name': 'fred', 'age': 40 };

// using "_.pluck" callback shorthand
_.max(characters, 'age');
// => { 'name': 'fred', 'age': 40 };
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_mincollection-callbackidentity-thisarg"></a>`_.min(collection, [callback=identity], [thisArg])`
<a href="#_mincollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3998 "View in source") [&#x24C9;][1]

Retrieves the minimum value of a collection. If the collection is empty or falsey `Infinity` is returned. If a callback is provided it will be executed for each value in the collection to generate the criterion by which the value is ranked. The callback is bound to `thisArg` and invoked with three arguments; *(value, index, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the minimum value.

#### Example
```js
_.min([4, 2, 8, 6]);
// => 2

var characters = [
  { 'name': 'barney', 'age': 36 },
  { 'name': 'fred',   'age': 40 }
];

_.min(characters, function(chr) { return chr.age; });
// => { 'name': 'barney', 'age': 36 };

// using "_.pluck" callback shorthand
_.min(characters, 'age');
// => { 'name': 'barney', 'age': 36 };
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_pluckcollection-property"></a>`_.pluck(collection, property)`
<a href="#_pluckcollection-property">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4053 "View in source") [&#x24C9;][1]

Retrieves the value of a specified property from all elements in the collection.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `property` *(string)*: The name of the property to pluck.

#### Returns
*(Array)*: Returns a new array of property values.

#### Example
```js
var characters = [
  { 'name': 'barney', 'age': 36 },
  { 'name': 'fred',   'age': 40 }
];

_.pluck(characters, 'name');
// => ['barney', 'fred']
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_reducecollection-callbackidentity-accumulator-thisarg"></a>`_.reduce(collection, [callback=identity], [accumulator], [thisArg])`
<a href="#_reducecollection-callbackidentity-accumulator-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4085 "View in source") [&#x24C9;][1]

Reduces a collection to a value which is the accumulated result of running each element in the collection through the callback, where each successive callback execution consumes the return value of the previous execution. If `accumulator` is not provided the first element of the collection will be used as the initial `accumulator` value. The callback is bound to `thisArg` and invoked with four arguments; *(accumulator, value, index|key, collection)*.

#### Aliases
*_.foldl, _.inject*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function)*: The function called per iteration.
3. `[accumulator]` *(&#42;)*: Initial value of the accumulator.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the accumulated value.

#### Example
```js
var sum = _.reduce([1, 2, 3], function(sum, num) {
  return sum + num;
});
// => 6

var mapped = _.reduce({ 'a': 1, 'b': 2, 'c': 3 }, function(result, num, key) {
  result[key] = num * 3;
  return result;
}, {});
// => { 'a': 3, 'b': 6, 'c': 9 }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_reducerightcollection-callbackidentity-accumulator-thisarg"></a>`_.reduceRight(collection, [callback=identity], [accumulator], [thisArg])`
<a href="#_reducerightcollection-callbackidentity-accumulator-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4128 "View in source") [&#x24C9;][1]

This method is like `_.reduce` except that it iterates over elements of a `collection` from right to left.

#### Aliases
*_.foldr*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function)*: The function called per iteration.
3. `[accumulator]` *(&#42;)*: Initial value of the accumulator.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the accumulated value.

#### Example
```js
var list = [[0, 1], [2, 3], [4, 5]];
var flat = _.reduceRight(list, function(a, b) { return a.concat(b); }, []);
// => [4, 5, 2, 3, 0, 1]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_rejectcollection-callbackidentity-thisarg"></a>`_.reject(collection, [callback=identity], [thisArg])`
<a href="#_rejectcollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4177 "View in source") [&#x24C9;][1]

The opposite of `_.filter` this method returns the elements of a collection that the callback does &#42;&#42;not&#42;&#42; return truey for.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a new array of elements that failed the callback check.

#### Example
```js
var odds = _.reject([1, 2, 3, 4, 5, 6], function(num) { return num % 2 == 0; });
// => [1, 3, 5]

var characters = [
  { 'name': 'barney', 'age': 36, 'blocked': false },
  { 'name': 'fred',   'age': 40, 'blocked': true }
];

// using "_.pluck" callback shorthand
_.reject(characters, 'blocked');
// => [{ 'name': 'barney', 'age': 36, 'blocked': false }]

// using "_.where" callback shorthand
_.reject(characters, { 'age': 36 });
// => [{ 'name': 'fred', 'age': 40, 'blocked': true }]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_samplecollection-n"></a>`_.sample(collection, [n])`
<a href="#_samplecollection-n">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4203 "View in source") [&#x24C9;][1]

Retrieves a random element or `n` random elements from a collection.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to sample.
2. `[n]` *(number)*: The number of elements to sample.

#### Returns
*(Array)*: Returns the random sample(s) of `collection`.

#### Example
```js
_.sample([1, 2, 3, 4]);
// => 2

_.sample([1, 2, 3, 4], 2);
// => [3, 1]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_shufflecollection"></a>`_.shuffle(collection)`
<a href="#_shufflecollection">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4231 "View in source") [&#x24C9;][1]

Creates an array of shuffled values, using a version of the Fisher-Yates shuffle. See http://en.wikipedia.org/wiki/Fisher-Yates_shuffle.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to shuffle.

#### Returns
*(Array)*: Returns a new shuffled collection.

#### Example
```js
_.shuffle([1, 2, 3, 4, 5, 6]);
// => [4, 1, 6, 3, 5, 2]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_sizecollection"></a>`_.size(collection)`
<a href="#_sizecollection">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4264 "View in source") [&#x24C9;][1]

Gets the size of the `collection` by returning `collection.length` for arrays and array-like objects or the number of own enumerable properties for objects.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to inspect.

#### Returns
*(number)*: Returns `collection.length` or number of own enumerable properties.

#### Example
```js
_.size([1, 2]);
// => 2

_.size({ 'one': 1, 'two': 2, 'three': 3 });
// => 3

_.size('pebbles');
// => 7
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_somecollection-callbackidentity-thisarg"></a>`_.some(collection, [callback=identity], [thisArg])`
<a href="#_somecollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4311 "View in source") [&#x24C9;][1]

Checks if the callback returns a truey value for &#42;&#42;any&#42;&#42; element of a collection. The function returns as soon as it finds a passing value and does not iterate over the entire collection. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Aliases
*_.any*

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(boolean)*: Returns `true` if any element passed the callback check,  else `false`.

#### Example
```js
_.some([null, 0, 'yes', false], Boolean);
// => true

var characters = [
  { 'name': 'barney', 'age': 36, 'blocked': false },
  { 'name': 'fred',   'age': 40, 'blocked': true }
];

// using "_.pluck" callback shorthand
_.some(characters, 'blocked');
// => true

// using "_.where" callback shorthand
_.some(characters, { 'age': 1 });
// => false
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_sortbycollection-callbackidentity-thisarg"></a>`_.sortBy(collection, [callback=identity], [thisArg])`
<a href="#_sortbycollection-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4381 "View in source") [&#x24C9;][1]

Creates an array of elements, sorted in ascending order by the results of running each element in a collection through the callback. This method performs a stable sort, that is, it will preserve the original sort order of equal elements. The callback is bound to `thisArg` and invoked with three arguments; *(value, index|key, collection)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an array of property names is provided for `callback` the collection will be sorted by each property value.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `[callback=identity]` *(Array|Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a new array of sorted elements.

#### Example
```js
_.sortBy([1, 2, 3], function(num) { return Math.sin(num); });
// => [3, 1, 2]

_.sortBy([1, 2, 3], function(num) { return this.sin(num); }, Math);
// => [3, 1, 2]

var characters = [
  { 'name': 'barney',  'age': 36 },
  { 'name': 'fred',    'age': 40 },
  { 'name': 'barney',  'age': 26 },
  { 'name': 'fred',    'age': 30 }
];

// using "_.pluck" callback shorthand
_.map(_.sortBy(characters, 'age'), _.values);
// => [['barney', 26], ['fred', 30], ['barney', 36], ['fred', 40]]

// sorting by multiple properties
_.map(_.sortBy(characters, ['name', 'age']), _.values);
// = > [['barney', 26], ['barney', 36], ['fred', 30], ['fred', 40]]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_toarraycollection"></a>`_.toArray(collection)`
<a href="#_toarraycollection">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4427 "View in source") [&#x24C9;][1]

Converts the `collection` to an array.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to convert.

#### Returns
*(Array)*: Returns the new converted array.

#### Example
```js
(function() { return _.toArray(arguments).slice(1); })(1, 2, 3, 4);
// => [2, 3, 4]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_wherecollection-props"></a>`_.where(collection, props)`
<a href="#_wherecollection-props">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L4461 "View in source") [&#x24C9;][1]

Performs a deep comparison of each element in a `collection` to the given `properties` object, returning an array of all elements that have equivalent property values.

#### Arguments
1. `collection` *(Array|Object|string)*: The collection to iterate over.
2. `props` *(Object)*: The object of property values to filter by.

#### Returns
*(Array)*: Returns a new array of elements that have the given properties.

#### Example
```js
var characters = [
  { 'name': 'barney', 'age': 36, 'pets': ['hoppy'] },
  { 'name': 'fred',   'age': 40, 'pets': ['baby puss', 'dino'] }
];

_.where(characters, { 'age': 36 });
// => [{ 'name': 'barney', 'age': 36, 'pets': ['hoppy'] }]

_.where(characters, { 'pets': ['dino'] });
// => [{ 'name': 'fred', 'age': 40, 'pets': ['baby puss', 'dino'] }]
```

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `“Functions” Methods`

<!-- div -->

### <a id="_aftern-func"></a>`_.after(n, func)`
<a href="#_aftern-func">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5504 "View in source") [&#x24C9;][1]

Creates a function that executes `func`, with  the `this` binding and arguments of the created function, only after being called `n` times.

#### Arguments
1. `n` *(number)*: The number of times the function must be called before `func` is executed.
2. `func` *(Function)*: The function to restrict.

#### Returns
*(Function)*: Returns the new restricted function.

#### Example
```js
var saves = ['profile', 'settings'];

var done = _.after(saves.length, function() {
  console.log('Done saving!');
});

_.forEach(saves, function(type) {
  asyncSave({ 'type': type, 'complete': done });
});
// => logs 'Done saving!', after all saves have completed
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_bindfunc-thisarg-arg"></a>`_.bind(func, [thisArg], [arg])`
<a href="#_bindfunc-thisarg-arg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5537 "View in source") [&#x24C9;][1]

Creates a function that, when called, invokes `func` with the `this` binding of `thisArg` and prepends any additional `bind` arguments to those provided to the bound function.

#### Arguments
1. `func` *(Function)*: The function to bind.
2. `[thisArg]` *(&#42;)*: The `this` binding of `func`.
3. `[arg]` *(...&#42;)*: Arguments to be partially applied.

#### Returns
*(Function)*: Returns the new bound function.

#### Example
```js
var func = function(greeting) {
  return greeting + ' ' + this.name;
};

func = _.bind(func, { 'name': 'fred' }, 'hi');
func();
// => 'hi fred'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_bindallobject-methodname"></a>`_.bindAll(object, [methodName])`
<a href="#_bindallobject-methodname">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5567 "View in source") [&#x24C9;][1]

Binds methods of an object to the object itself, overwriting the existing method. Method names may be specified as individual arguments or as arrays of method names. If no method names are provided all the function properties of `object` will be bound.

#### Arguments
1. `object` *(Object)*: The object to bind and assign the bound methods to.
2. `[methodName]` *(...string)*: The object method names to bind, specified as individual method names or arrays of method names.

#### Returns
*(Object)*: Returns `object`.

#### Example
```js
var view = {
  'label': 'docs',
  'onClick': function() { console.log('clicked ' + this.label); }
};

_.bindAll(view);
jQuery('#docs').on('click', view.onClick);
// => logs 'clicked docs', when the button is clicked
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_bindkeyobject-key-arg"></a>`_.bindKey(object, key, [arg])`
<a href="#_bindkeyobject-key-arg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5613 "View in source") [&#x24C9;][1]

Creates a function that, when called, invokes the method at `object[key]` and prepends any additional `bindKey` arguments to those provided to the bound function. This method differs from `_.bind` by allowing bound functions to reference methods that will be redefined or don't yet exist. See http://michaux.ca/articles/lazy-function-definition-pattern.

#### Arguments
1. `object` *(Object)*: The object the method belongs to.
2. `key` *(string)*: The key of the method.
3. `[arg]` *(...&#42;)*: Arguments to be partially applied.

#### Returns
*(Function)*: Returns the new bound function.

#### Example
```js
var object = {
  'name': 'fred',
  'greet': function(greeting) {
    return greeting + ' ' + this.name;
  }
};

var func = _.bindKey(object, 'greet', 'hi');
func();
// => 'hi fred'

object.greet = function(greeting) {
  return greeting + 'ya ' + this.name + '!';
};

func();
// => 'hiya fred!'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_composefunc"></a>`_.compose([func])`
<a href="#_composefunc">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5649 "View in source") [&#x24C9;][1]

Creates a function that is the composition of the provided functions, where each function consumes the return value of the function that follows. For example, composing the functions `f()`, `g()`, and `h()` produces `f(g(h()))`. Each function is executed with the `this` binding of the composed function.

#### Arguments
1. `[func]` *(...Function)*: Functions to compose.

#### Returns
*(Function)*: Returns the new composed function.

#### Example
```js
var realNameMap = {
  'pebbles': 'penelope'
};

var format = function(name) {
  name = realNameMap[name.toLowerCase()] || name;
  return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
};

var greet = function(formatted) {
  return 'Hiya ' + formatted + '!';
};

var welcome = _.compose(greet, format);
welcome('pebbles');
// => 'Hiya Penelope!'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_curryfunc-arityfunclength"></a>`_.curry(func, [arity=func.length])`
<a href="#_curryfunc-arityfunclength">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5697 "View in source") [&#x24C9;][1]

Creates a function which accepts one or more arguments of `func` that when invoked either executes `func` returning its result, if all `func` arguments have been provided, or returns a function that accepts one or more of the remaining `func` arguments, and so on. The arity of `func` can be specified if `func.length` is not sufficient.

#### Arguments
1. `func` *(Function)*: The function to curry.
2. `[arity=func.length]` *(number)*: The arity of `func`.

#### Returns
*(Function)*: Returns the new curried function.

#### Example
```js
var curried = _.curry(function(a, b, c) {
  console.log(a + b + c);
});

curried(1)(2)(3);
// => 6

curried(1, 2)(3);
// => 6

curried(1, 2, 3);
// => 6
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_debouncefunc-wait-options-optionsmaxwait"></a>`_.debounce(func, wait, [options], [options.maxWait])`
<a href="#_debouncefunc-wait-options-optionsmaxwait">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5741 "View in source") [&#x24C9;][1]

Creates a function that will delay the execution of `func` until after `wait` milliseconds have elapsed since the last time it was invoked. Provide an options object to indicate that `func` should be invoked on the leading and/or trailing edge of the `wait` timeout. Subsequent calls to the debounced function will return the result of the last `func` call.

Note: If `leading` and `trailing` options are `true` `func` will be called on the trailing edge of the timeout only if the the debounced function is invoked more than once during the `wait` timeout.

#### Arguments
1. `func` *(Function)*: The function to debounce.
2. `wait` *(number)*: The number of milliseconds to delay.
3. `[options]` *(Object)*: The options object.
4. `[options.leading=false]` *(boolean)*: Specify execution on the leading edge of the timeout.
5. `[options.maxWait]` *(number)*: The maximum time `func` is allowed to be delayed before it's called.
6. `[options.trailing=true]` *(boolean)*: Specify execution on the trailing edge of the timeout.

#### Returns
*(Function)*: Returns the new debounced function.

#### Example
```js
// avoid costly calculations while the window size is in flux
var lazyLayout = _.debounce(calculateLayout, 150);
jQuery(window).on('resize', lazyLayout);

// execute `sendMail` when the click event is fired, debouncing subsequent calls
jQuery('#postbox').on('click', _.debounce(sendMail, 300, {
  'leading': true,
  'trailing': false
});

// ensure `batchLog` is executed once after 1 second of debounced calls
var source = new EventSource('/stream');
source.addEventListener('message', _.debounce(batchLog, 250, {
  'maxWait': 1000
}, false);
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_deferfunc-arg"></a>`_.defer(func, [arg])`
<a href="#_deferfunc-arg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5857 "View in source") [&#x24C9;][1]

Defers executing the `func` function until the current call stack has cleared. Additional arguments will be provided to `func` when it is invoked.

#### Arguments
1. `func` *(Function)*: The function to defer.
2. `[arg]` *(...&#42;)*: Arguments to invoke the function with.

#### Returns
*(number)*: Returns the timer id.

#### Example
```js
_.defer(function(text) { console.log(text); }, 'deferred');
// logs 'deferred' after one or more milliseconds
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_delayfunc-wait-arg"></a>`_.delay(func, wait, [arg])`
<a href="#_delayfunc-wait-arg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5881 "View in source") [&#x24C9;][1]

Executes the `func` function after `wait` milliseconds. Additional arguments will be provided to `func` when it is invoked.

#### Arguments
1. `func` *(Function)*: The function to delay.
2. `wait` *(number)*: The number of milliseconds to delay execution.
3. `[arg]` *(...&#42;)*: Arguments to invoke the function with.

#### Returns
*(number)*: Returns the timer id.

#### Example
```js
_.delay(function(text) { console.log(text); }, 1000, 'later');
// => logs 'later' after one second
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_memoizefunc-resolver"></a>`_.memoize(func, [resolver])`
<a href="#_memoizefunc-resolver">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5926 "View in source") [&#x24C9;][1]

Creates a function that memoizes the result of `func`. If `resolver` is provided it will be used to determine the cache key for storing the result based on the arguments provided to the memoized function. By default, the first argument provided to the memoized function is used as the cache key. The `func` is executed with the `this` binding of the memoized function. The result cache is exposed as the `cache` property on the memoized function.

#### Arguments
1. `func` *(Function)*: The function to have its output memoized.
2. `[resolver]` *(Function)*: A function used to resolve the cache key.

#### Returns
*(Function)*: Returns the new memoizing function.

#### Example
```js
var fibonacci = _.memoize(function(n) {
  return n < 2 ? n : fibonacci(n - 1) + fibonacci(n - 2);
});

fibonacci(9)
// => 34

var data = {
  'fred': { 'name': 'fred', 'age': 40 },
  'pebbles': { 'name': 'pebbles', 'age': 1 }
};

// modifying the result cache
var get = _.memoize(function(name) { return data[name]; }, _.identity);
get('pebbles');
// => { 'name': 'pebbles', 'age': 1 }

get.cache.pebbles.name = 'penelope';
get('pebbles');
// => { 'name': 'penelope', 'age': 1 }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_oncefunc"></a>`_.once(func)`
<a href="#_oncefunc">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5959 "View in source") [&#x24C9;][1]

Creates a function that is restricted to execute `func` once. Repeat calls to the function will return the value of the first call. The `func` is executed with the `this` binding of the created function.

#### Arguments
1. `func` *(Function)*: The function to restrict.

#### Returns
*(Function)*: Returns the new restricted function.

#### Example
```js
var initialize = _.once(createApplication);
initialize();
initialize();
// `initialize` executes `createApplication` once
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_partialfunc-arg"></a>`_.partial(func, [arg])`
<a href="#_partialfunc-arg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L5997 "View in source") [&#x24C9;][1]

Creates a function that, when called, invokes `func` with any additional `partial` arguments prepended to those provided to the new function. This method is similar to `_.bind` except it does &#42;&#42;not&#42;&#42; alter the `this` binding.

#### Arguments
1. `func` *(Function)*: The function to partially apply arguments to.
2. `[arg]` *(...&#42;)*: Arguments to be partially applied.

#### Returns
*(Function)*: Returns the new partially applied function.

#### Example
```js
var greet = function(greeting, name) { return greeting + ' ' + name; };
var hi = _.partial(greet, 'hi');
hi('fred');
// => 'hi fred'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_partialrightfunc-arg"></a>`_.partialRight(func, [arg])`
<a href="#_partialrightfunc-arg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6028 "View in source") [&#x24C9;][1]

This method is like `_.partial` except that `partial` arguments are appended to those provided to the new function.

#### Arguments
1. `func` *(Function)*: The function to partially apply arguments to.
2. `[arg]` *(...&#42;)*: Arguments to be partially applied.

#### Returns
*(Function)*: Returns the new partially applied function.

#### Example
```js
var defaultsDeep = _.partialRight(_.merge, _.defaults);

var options = {
  'variable': 'data',
  'imports': { 'jq': $ }
};

defaultsDeep(options, _.templateSettings);

options.variable
// => 'data'

options.imports
// => { '_': _, 'jq': $ }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_throttlefunc-wait-options"></a>`_.throttle(func, wait, [options])`
<a href="#_throttlefunc-wait-options">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6063 "View in source") [&#x24C9;][1]

Creates a function that, when executed, will only call the `func` function at most once per every `wait` milliseconds. Provide an options object to indicate that `func` should be invoked on the leading and/or trailing edge of the `wait` timeout. Subsequent calls to the throttled function will return the result of the last `func` call.

Note: If `leading` and `trailing` options are `true` `func` will be called on the trailing edge of the timeout only if the the throttled function is invoked more than once during the `wait` timeout.

#### Arguments
1. `func` *(Function)*: The function to throttle.
2. `wait` *(number)*: The number of milliseconds to throttle executions to.
3. `[options]` *(Object)*: The options object.
4. `[options.leading=true]` *(boolean)*: Specify execution on the leading edge of the timeout.
5. `[options.trailing=true]` *(boolean)*: Specify execution on the trailing edge of the timeout.

#### Returns
*(Function)*: Returns the new throttled function.

#### Example
```js
// avoid excessively updating the position while scrolling
var throttled = _.throttle(updatePosition, 100);
jQuery(window).on('scroll', throttled);

// execute `renewToken` when the click event is fired, but not more than once every 5 minutes
jQuery('.interactive').on('click', _.throttle(renewToken, 300000, {
  'trailing': false
}));
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_wrapvalue-wrapper"></a>`_.wrap(value, wrapper)`
<a href="#_wrapvalue-wrapper">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6104 "View in source") [&#x24C9;][1]

Creates a function that provides `value` to the wrapper function as its first argument. Additional arguments provided to the function are appended to those provided to the wrapper function. The wrapper is executed with the `this` binding of the created function.

#### Arguments
1. `value` *(&#42;)*: The value to wrap.
2. `wrapper` *(Function)*: The wrapper function.

#### Returns
*(Function)*: Returns the new function.

#### Example
```js
var p = _.wrap(_.escape, function(func, text) {
  return '<p>' + func(text) + '</p>';
});

p('Fred, Wilma, & Pebbles');
// => '<p>Fred, Wilma, &amp; Pebbles</p>'
```

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `“Objects” Methods`

<!-- div -->

### <a id="_assignobject-source-callback-thisarg"></a>`_.assign(object, [source], [callback], [thisArg])`
<a href="#_assignobject-source-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2084 "View in source") [&#x24C9;][1]

Assigns own enumerable properties of source object(s) to the destination object. Subsequent sources will overwrite property assignments of previous sources. If a callback is provided it will be executed to produce the assigned values. The callback is bound to `thisArg` and invoked with two arguments; *(objectValue, sourceValue)*.

#### Aliases
*_.extend*

#### Arguments
1. `object` *(Object)*: The destination object.
2. `[source]` *(...Object)*: The source objects.
3. `[callback]` *(Function)*: The function to customize assigning values.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns the destination object.

#### Example
```js
_.assign({ 'name': 'fred' }, { 'employer': 'slate' });
// => { 'name': 'fred', 'employer': 'slate' }

var defaults = _.partialRight(_.assign, function(a, b) {
  return typeof a == 'undefined' ? b : a;
});

var object = { 'name': 'barney' };
defaults(object, { 'name': 'fred', 'employer': 'slate' });
// => { 'name': 'barney', 'employer': 'slate' }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_clonevalue-isdeepfalse-callback-thisarg"></a>`_.clone(value, [isDeep=false], [callback], [thisArg])`
<a href="#_clonevalue-isdeepfalse-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2137 "View in source") [&#x24C9;][1]

Creates a clone of `value`. If `isDeep` is `true` nested objects will also be cloned, otherwise they will be assigned by reference. If a callback is provided it will be executed to produce the cloned values. If the callback returns `undefined` cloning will be handled by the method instead. The callback is bound to `thisArg` and invoked with one argument; *(value)*.

#### Arguments
1. `value` *(&#42;)*: The value to clone.
2. `[isDeep=false]` *(boolean)*: Specify a deep clone.
3. `[callback]` *(Function)*: The function to customize cloning values.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the cloned value.

#### Example
```js
var characters = [
  { 'name': 'barney', 'age': 36 },
  { 'name': 'fred',   'age': 40 }
];

var shallow = _.clone(characters);
shallow[0] === characters[0];
// => true

var deep = _.clone(characters, true);
deep[0] === characters[0];
// => false

_.mixin({
  'clone': _.partialRight(_.clone, function(value) {
    return _.isElement(value) ? value.cloneNode(false) : undefined;
  })
});

var clone = _.clone(document.body);
clone.childNodes.length;
// => 0
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_clonedeepvalue-callback-thisarg"></a>`_.cloneDeep(value, [callback], [thisArg])`
<a href="#_clonedeepvalue-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2189 "View in source") [&#x24C9;][1]

Creates a deep clone of `value`. If a callback is provided it will be executed to produce the cloned values. If the callback returns `undefined` cloning will be handled by the method instead. The callback is bound to `thisArg` and invoked with one argument; *(value)*.

Note: This method is loosely based on the structured clone algorithm. Functions and DOM nodes are &#42;&#42;not&#42;&#42; cloned. The enumerable properties of `arguments` objects and objects created by constructors other than `Object` are cloned to plain `Object` objects. See http://www.w3.org/TR/html5/infrastructure.html#internal-structured-cloning-algorithm.

#### Arguments
1. `value` *(&#42;)*: The value to deep clone.
2. `[callback]` *(Function)*: The function to customize cloning values.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the deep cloned value.

#### Example
```js
var characters = [
  { 'name': 'barney', 'age': 36 },
  { 'name': 'fred',   'age': 40 }
];

var deep = _.cloneDeep(characters);
deep[0] === characters[0];
// => false

var view = {
  'label': 'docs',
  'node': element
};

var clone = _.cloneDeep(view, function(value) {
  return _.isElement(value) ? value.cloneNode(true) : undefined;
});

clone.node == view.node;
// => false
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_createprototype-properties"></a>`_.create(prototype, [properties])`
<a href="#_createprototype-properties">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2224 "View in source") [&#x24C9;][1]

Creates an object that inherits from the given `prototype` object. If a `properties` object is provided its own enumerable properties are assigned to the created object.

#### Arguments
1. `prototype` *(Object)*: The object to inherit from.
2. `[properties]` *(Object)*: The properties to assign to the object.

#### Returns
*(Object)*: Returns the new object.

#### Example
```js
function Shape() {
  this.x = 0;
  this.y = 0;
}

function Circle() {
  Shape.call(this);
}

Circle.prototype = _.create(Shape.prototype, { 'constructor': Circle });

var circle = new Circle;
circle instanceof Circle;
// => true

circle instanceof Shape;
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_defaultsobject-source"></a>`_.defaults(object, [source])`
<a href="#_defaultsobject-source">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2249 "View in source") [&#x24C9;][1]

Assigns own enumerable properties of source object(s) to the destination object for all destination properties that resolve to `undefined`. Once a property is set, additional defaults of the same property will be ignored.

#### Arguments
1. `object` *(Object)*: The destination object.
2. `[source]` *(...Object)*: The source objects.

#### Returns
*(Object)*: Returns the destination object.

#### Example
```js
var object = { 'name': 'barney' };
_.defaults(object, { 'name': 'fred', 'employer': 'slate' });
// => { 'name': 'barney', 'employer': 'slate' }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_findkeyobject-callbackidentity-thisarg"></a>`_.findKey(object, [callback=identity], [thisArg])`
<a href="#_findkeyobject-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2292 "View in source") [&#x24C9;][1]

This method is like `_.findIndex` except that it returns the key of the first element that passes the callback check, instead of the element itself.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `object` *(Object)*: The object to search.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(string, undefined)*: Returns the key of the found element, else `undefined`.

#### Example
```js
var characters = {
  'barney': {  'age': 36, 'blocked': false },
  'fred': {    'age': 40, 'blocked': true },
  'pebbles': { 'age': 1,  'blocked': false }
};

_.findKey(characters, function(chr) {
  return chr.age < 40;
});
// => 'barney' (property order is not guaranteed across environments)

// using "_.where" callback shorthand
_.findKey(characters, { 'age': 1 });
// => 'pebbles'

// using "_.pluck" callback shorthand
_.findKey(characters, 'blocked');
// => 'fred'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_findlastkeyobject-callbackidentity-thisarg"></a>`_.findLastKey(object, [callback=identity], [thisArg])`
<a href="#_findlastkeyobject-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2345 "View in source") [&#x24C9;][1]

This method is like `_.findKey` except that it iterates over elements of a `collection` in the opposite order.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `object` *(Object)*: The object to search.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(string, undefined)*: Returns the key of the found element, else `undefined`.

#### Example
```js
var characters = {
  'barney': {  'age': 36, 'blocked': true },
  'fred': {    'age': 40, 'blocked': false },
  'pebbles': { 'age': 1,  'blocked': true }
};

_.findLastKey(characters, function(chr) {
  return chr.age < 40;
});
// => returns `pebbles`, assuming `_.findKey` returns `barney`

// using "_.where" callback shorthand
_.findLastKey(characters, { 'age': 40 });
// => 'fred'

// using "_.pluck" callback shorthand
_.findLastKey(characters, 'blocked');
// => 'pebbles'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_forinobject-callbackidentity-thisarg"></a>`_.forIn(object, [callback=identity], [thisArg])`
<a href="#_forinobject-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2388 "View in source") [&#x24C9;][1]

Iterates over own and inherited enumerable properties of an object, executing the callback for each property. The callback is bound to `thisArg` and invoked with three arguments; *(value, key, object)*. Callbacks may exit iteration early by explicitly returning `false`.

#### Arguments
1. `object` *(Object)*: The object to iterate over.
2. `[callback=identity]` *(Function)*: The function called per iteration.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns `object`.

#### Example
```js
function Shape() {
  this.x = 0;
  this.y = 0;
}

Shape.prototype.move = function(x, y) {
  this.x += x;
  this.y += y;
};

_.forIn(new Shape, function(value, key) {
  console.log(key);
});
// => logs 'x', 'y', and 'move' (property order is not guaranteed across environments)
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_forinrightobject-callbackidentity-thisarg"></a>`_.forInRight(object, [callback=identity], [thisArg])`
<a href="#_forinrightobject-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2420 "View in source") [&#x24C9;][1]

This method is like `_.forIn` except that it iterates over elements of a `collection` in the opposite order.

#### Arguments
1. `object` *(Object)*: The object to iterate over.
2. `[callback=identity]` *(Function)*: The function called per iteration.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns `object`.

#### Example
```js
function Shape() {
  this.x = 0;
  this.y = 0;
}

Shape.prototype.move = function(x, y) {
  this.x += x;
  this.y += y;
};

_.forInRight(new Shape, function(value, key) {
  console.log(key);
});
// => logs 'move', 'y', and 'x' assuming `_.forIn ` logs 'x', 'y', and 'move'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_forownobject-callbackidentity-thisarg"></a>`_.forOwn(object, [callback=identity], [thisArg])`
<a href="#_forownobject-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2458 "View in source") [&#x24C9;][1]

Iterates over own enumerable properties of an object, executing the callback for each property. The callback is bound to `thisArg` and invoked with three arguments; *(value, key, object)*. Callbacks may exit iteration early by explicitly returning `false`.

#### Arguments
1. `object` *(Object)*: The object to iterate over.
2. `[callback=identity]` *(Function)*: The function called per iteration.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns `object`.

#### Example
```js
_.forOwn({ '0': 'zero', '1': 'one', 'length': 2 }, function(num, key) {
  console.log(key);
});
// => logs '0', '1', and 'length' (property order is not guaranteed across environments)
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_forownrightobject-callbackidentity-thisarg"></a>`_.forOwnRight(object, [callback=identity], [thisArg])`
<a href="#_forownrightobject-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2478 "View in source") [&#x24C9;][1]

This method is like `_.forOwn` except that it iterates over elements of a `collection` in the opposite order.

#### Arguments
1. `object` *(Object)*: The object to iterate over.
2. `[callback=identity]` *(Function)*: The function called per iteration.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns `object`.

#### Example
```js
_.forOwnRight({ '0': 'zero', '1': 'one', 'length': 2 }, function(num, key) {
  console.log(key);
});
// => logs 'length', '1', and '0' assuming `_.forOwn` logs '0', '1', and 'length'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_functionsobject"></a>`_.functions(object)`
<a href="#_functionsobject">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2507 "View in source") [&#x24C9;][1]

Creates a sorted array of property names of all enumerable properties, own and inherited, of `object` that have function values.

#### Aliases
*_.methods*

#### Arguments
1. `object` *(Object)*: The object to inspect.

#### Returns
*(Array)*: Returns an array of property names that have function values.

#### Example
```js
_.functions(_);
// => ['all', 'any', 'bind', 'bindAll', 'clone', 'compact', 'compose', ...]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_hasobject-key"></a>`_.has(object, key)`
<a href="#_hasobject-key">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2532 "View in source") [&#x24C9;][1]

Checks if the specified property name exists as a direct property of `object`, instead of an inherited property.

#### Arguments
1. `object` *(Object)*: The object to inspect.
2. `key` *(string)*: The name of the property to check.

#### Returns
*(boolean)*: Returns `true` if key is a direct property, else `false`.

#### Example
```js
_.has({ 'a': 1, 'b': 2, 'c': 3 }, 'b');
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_invertobject"></a>`_.invert(object)`
<a href="#_invertobject">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2549 "View in source") [&#x24C9;][1]

Creates an object composed of the inverted keys and values of the given object.

#### Arguments
1. `object` *(Object)*: The object to invert.

#### Returns
*(Object)*: Returns the created inverted object.

#### Example
```js
_.invert({ 'first': 'fred', 'second': 'barney' });
// => { 'fred': 'first', 'barney': 'second' }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isargumentsvalue"></a>`_.isArguments(value)`
<a href="#_isargumentsvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L1909 "View in source") [&#x24C9;][1]

Checks if `value` is an `arguments` object.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is an `arguments` object, else `false`.

#### Example
```js
(function() { return _.isArguments(arguments); })(1, 2, 3);
// => true

_.isArguments([1, 2, 3]);
// => false
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isarrayvalue"></a>`_.isArray(value)`
<a href="#_isarrayvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L1938 "View in source") [&#x24C9;][1]

Checks if `value` is an array.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is an array, else `false`.

#### Example
```js
(function() { return _.isArray(arguments); })();
// => false

_.isArray([1, 2, 3]);
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isbooleanvalue"></a>`_.isBoolean(value)`
<a href="#_isbooleanvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2575 "View in source") [&#x24C9;][1]

Checks if `value` is a boolean value.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is a boolean value, else `false`.

#### Example
```js
_.isBoolean(null);
// => false
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isdatevalue"></a>`_.isDate(value)`
<a href="#_isdatevalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2593 "View in source") [&#x24C9;][1]

Checks if `value` is a date.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is a date, else `false`.

#### Example
```js
_.isDate(new Date);
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_iselementvalue"></a>`_.isElement(value)`
<a href="#_iselementvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2610 "View in source") [&#x24C9;][1]

Checks if `value` is a DOM element.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is a DOM element, else `false`.

#### Example
```js
_.isElement(document.body);
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isemptyvalue"></a>`_.isEmpty(value)`
<a href="#_isemptyvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2635 "View in source") [&#x24C9;][1]

Checks if `value` is empty. Arrays, strings, or `arguments` objects with a length of `0` and objects with no own enumerable properties are considered "empty".

#### Arguments
1. `value` *(Array|Object|string)*: The value to inspect.

#### Returns
*(boolean)*: Returns `true` if the `value` is empty, else `false`.

#### Example
```js
_.isEmpty([1, 2, 3]);
// => false

_.isEmpty({});
// => true

_.isEmpty('');
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isequala-b-callback-thisarg"></a>`_.isEqual(a, b, [callback], [thisArg])`
<a href="#_isequala-b-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2692 "View in source") [&#x24C9;][1]

Performs a deep comparison between two values to determine if they are equivalent to each other. If a callback is provided it will be executed to compare values. If the callback returns `undefined` comparisons will be handled by the method instead. The callback is bound to `thisArg` and invoked with two arguments; *(a, b)*.

#### Arguments
1. `a` *(&#42;)*: The value to compare.
2. `b` *(&#42;)*: The other value to compare.
3. `[callback]` *(Function)*: The function to customize comparing values.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(boolean)*: Returns `true` if the values are equivalent, else `false`.

#### Example
```js
var object = { 'name': 'fred' };
var copy = { 'name': 'fred' };

object == copy;
// => false

_.isEqual(object, copy);
// => true

var words = ['hello', 'goodbye'];
var otherWords = ['hi', 'goodbye'];

_.isEqual(words, otherWords, function(a, b) {
  var reGreet = /^(?:hello|hi)$/i,
      aGreet = _.isString(a) && reGreet.test(a),
      bGreet = _.isString(b) && reGreet.test(b);

  return (aGreet || bGreet) ? (aGreet == bGreet) : undefined;
});
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isfinitevalue"></a>`_.isFinite(value)`
<a href="#_isfinitevalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2724 "View in source") [&#x24C9;][1]

Checks if `value` is, or can be coerced to, a finite number.

Note: This is not the same as native `isFinite` which will return true for booleans and empty strings. See http://es5.github.io/#x15.1.2.5.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is finite, else `false`.

#### Example
```js
_.isFinite(-101);
// => true

_.isFinite('10');
// => true

_.isFinite(true);
// => false

_.isFinite('');
// => false

_.isFinite(Infinity);
// => false
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isfunctionvalue"></a>`_.isFunction(value)`
<a href="#_isfunctionvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2741 "View in source") [&#x24C9;][1]

Checks if `value` is a function.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is a function, else `false`.

#### Example
```js
_.isFunction(_);
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isnanvalue"></a>`_.isNaN(value)`
<a href="#_isnanvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2804 "View in source") [&#x24C9;][1]

Checks if `value` is `NaN`.

Note: This is not the same as native `isNaN` which will return `true` for `undefined` and other non-numeric values. See http://es5.github.io/#x15.1.2.4.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is `NaN`, else `false`.

#### Example
```js
_.isNaN(NaN);
// => true

_.isNaN(new Number(NaN));
// => true

isNaN(undefined);
// => true

_.isNaN(undefined);
// => false
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isnullvalue"></a>`_.isNull(value)`
<a href="#_isnullvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2826 "View in source") [&#x24C9;][1]

Checks if `value` is `null`.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is `null`, else `false`.

#### Example
```js
_.isNull(null);
// => true

_.isNull(undefined);
// => false
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isnumbervalue"></a>`_.isNumber(value)`
<a href="#_isnumbervalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2845 "View in source") [&#x24C9;][1]

Checks if `value` is a number.

Note: `NaN` is considered a number. See http://es5.github.io/#x8.5.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is a number, else `false`.

#### Example
```js
_.isNumber(8.4 * 5);
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isobjectvalue"></a>`_.isObject(value)`
<a href="#_isobjectvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2771 "View in source") [&#x24C9;][1]

Checks if `value` is the language type of Object. *(e.g. arrays, functions, objects, regexes, `new Number(0)`, and `new String('')`)*

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is an object, else `false`.

#### Example
```js
_.isObject({});
// => true

_.isObject([1, 2, 3]);
// => true

_.isObject(1);
// => false
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isplainobjectvalue"></a>`_.isPlainObject(value)`
<a href="#_isplainobjectvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2874 "View in source") [&#x24C9;][1]

Checks if `value` is an object created by the `Object` constructor.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if `value` is a plain object, else `false`.

#### Example
```js
function Shape() {
  this.x = 0;
  this.y = 0;
}

_.isPlainObject(new Shape);
// => false

_.isPlainObject([1, 2, 3]);
// => false

_.isPlainObject({ 'x': 0, 'y': 0 });
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isregexpvalue"></a>`_.isRegExp(value)`
<a href="#_isregexpvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2899 "View in source") [&#x24C9;][1]

Checks if `value` is a regular expression.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is a regular expression, else `false`.

#### Example
```js
_.isRegExp(/fred/);
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isstringvalue"></a>`_.isString(value)`
<a href="#_isstringvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2916 "View in source") [&#x24C9;][1]

Checks if `value` is a string.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is a string, else `false`.

#### Example
```js
_.isString('fred');
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_isundefinedvalue"></a>`_.isUndefined(value)`
<a href="#_isundefinedvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2934 "View in source") [&#x24C9;][1]

Checks if `value` is `undefined`.

#### Arguments
1. `value` *(&#42;)*: The value to check.

#### Returns
*(boolean)*: Returns `true` if the `value` is `undefined`, else `false`.

#### Example
```js
_.isUndefined(void 0);
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_keysobject"></a>`_.keys(object)`
<a href="#_keysobject">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L1972 "View in source") [&#x24C9;][1]

Creates an array composed of the own enumerable property names of an object.

#### Arguments
1. `object` *(Object)*: The object to inspect.

#### Returns
*(Array)*: Returns an array of property names.

#### Example
```js
_.keys({ 'one': 1, 'two': 2, 'three': 3 });
// => ['one', 'two', 'three'] (property order is not guaranteed across environments)
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_mapvaluesobject-callbackidentity-thisarg"></a>`_.mapValues(object, [callback=identity], [thisArg])`
<a href="#_mapvaluesobject-callbackidentity-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L2974 "View in source") [&#x24C9;][1]

Creates an object with the same keys as `object` and values generated by running each own enumerable property of `object` through the callback. The callback is bound to `thisArg` and invoked with three arguments; *(value, key, object)*.

If a property name is provided for `callback` the created "_.pluck" style callback will return the property value of the given element.

If an object is provided for `callback` the created "_.where" style callback will return `true` for elements that have the properties of the given object, else `false`.

#### Arguments
1. `object` *(Object)*: The object to iterate over.
2. `[callback=identity]` *(Function|Object|string)*: The function called per iteration. If a property name or object is provided it will be used to create a "_.pluck" or "_.where" style callback, respectively.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns a new object with values of the results of each `callback` execution.

#### Example
```js
_.mapValues({ 'a': 1, 'b': 2, 'c': 3} , function(num) { return num * 3; });
// => { 'a': 3, 'b': 6, 'c': 9 }

var characters = {
  'fred': { 'name': 'fred', 'age': 40 },
  'pebbles': { 'name': 'pebbles', 'age': 1 }
};

// using "_.pluck" callback shorthand
_.mapValues(characters, 'age');
// => { 'fred': 40, 'pebbles': 1 }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_mergeobject-source-callback-thisarg"></a>`_.merge(object, [source], [callback], [thisArg])`
<a href="#_mergeobject-source-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3035 "View in source") [&#x24C9;][1]

Recursively merges own enumerable properties of the source object(s), that don't resolve to `undefined` into the destination object. Subsequent sources will overwrite property assignments of previous sources. If a callback is provided it will be executed to produce the merged values of the destination and source properties. If the callback returns `undefined` merging will be handled by the method instead. The callback is bound to `thisArg` and invoked with two arguments; *(objectValue, sourceValue)*.

#### Arguments
1. `object` *(Object)*: The destination object.
2. `[source]` *(...Object)*: The source objects.
3. `[callback]` *(Function)*: The function to customize merging properties.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns the destination object.

#### Example
```js
var names = {
  'characters': [
    { 'name': 'barney' },
    { 'name': 'fred' }
  ]
};

var ages = {
  'characters': [
    { 'age': 36 },
    { 'age': 40 }
  ]
};

_.merge(names, ages);
// => { 'characters': [{ 'name': 'barney', 'age': 36 }, { 'name': 'fred', 'age': 40 }] }

var food = {
  'fruits': ['apple'],
  'vegetables': ['beet']
};

var otherFood = {
  'fruits': ['banana'],
  'vegetables': ['carrot']
};

_.merge(food, otherFood, function(a, b) {
  return _.isArray(a) ? a.concat(b) : undefined;
});
// => { 'fruits': ['apple', 'banana'], 'vegetables': ['beet', 'carrot] }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_omitobject-callback-thisarg"></a>`_.omit(object, [callback], [thisArg])`
<a href="#_omitobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3091 "View in source") [&#x24C9;][1]

Creates a shallow clone of `object` excluding the specified properties. Property names may be specified as individual arguments or as arrays of property names. If a callback is provided it will be executed for each property of `object` omitting the properties the callback returns truey for. The callback is bound to `thisArg` and invoked with three arguments; *(value, key, object)*.

#### Arguments
1. `object` *(Object)*: The source object.
2. `[callback]` *(Function|...string|string&#91;&#93;)*: The properties to omit or the function called per iteration.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns an object without the omitted properties.

#### Example
```js
_.omit({ 'name': 'fred', 'age': 40 }, 'age');
// => { 'name': 'fred' }

_.omit({ 'name': 'fred', 'age': 40 }, function(value) {
  return typeof value == 'number';
});
// => { 'name': 'fred' }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_pairsobject"></a>`_.pairs(object)`
<a href="#_pairsobject">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3132 "View in source") [&#x24C9;][1]

Creates a two dimensional array of an object's key-value pairs, i.e. `[[key1, value1], [key2, value2]]`.

#### Arguments
1. `object` *(Object)*: The object to inspect.

#### Returns
*(Array)*: Returns new array of key-value pairs.

#### Example
```js
_.pairs({ 'barney': 36, 'fred': 40 });
// => [['barney', 36], ['fred', 40]] (property order is not guaranteed across environments)
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_pickobject-callback-thisarg"></a>`_.pick(object, [callback], [thisArg])`
<a href="#_pickobject-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3172 "View in source") [&#x24C9;][1]

Creates a shallow clone of `object` composed of the specified properties. Property names may be specified as individual arguments or as arrays of property names. If a callback is provided it will be executed for each property of `object` picking the properties the callback returns truey for. The callback is bound to `thisArg` and invoked with three arguments; *(value, key, object)*.

#### Arguments
1. `object` *(Object)*: The source object.
2. `[callback]` *(Function|...string|string&#91;&#93;)*: The function called per iteration or property names to pick, specified as individual property names or arrays of property names.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Object)*: Returns an object composed of the picked properties.

#### Example
```js
_.pick({ 'name': 'fred', '_userid': 'fred1' }, 'name');
// => { 'name': 'fred' }

_.pick({ 'name': 'fred', '_userid': 'fred1' }, function(value, key) {
  return key.charAt(0) != '_';
});
// => { 'name': 'fred' }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_transformobject-callbackidentity-accumulator-thisarg"></a>`_.transform(object, [callback=identity], [accumulator], [thisArg])`
<a href="#_transformobject-callbackidentity-accumulator-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3227 "View in source") [&#x24C9;][1]

An alternative to `_.reduce` this method transforms `object` to a new `accumulator` object which is the result of running each of its own enumerable properties through a callback, with each callback execution potentially mutating the `accumulator` object. The callback is bound to `thisArg` and invoked with four arguments; *(accumulator, value, key, object)*. Callbacks may exit iteration early by explicitly returning `false`.

#### Arguments
1. `object` *(Array|Object)*: The object to iterate over.
2. `[callback=identity]` *(Function)*: The function called per iteration.
3. `[accumulator]` *(&#42;)*: The custom accumulator value.
4. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(&#42;)*: Returns the accumulated value.

#### Example
```js
var squares = _.transform([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], function(result, num) {
  num *= num;
  if (num % 2) {
    return result.push(num) < 3;
  }
});
// => [1, 9, 25]

var mapped = _.transform({ 'a': 1, 'b': 2, 'c': 3 }, function(result, num, key) {
  result[key] = num * 3;
});
// => { 'a': 3, 'b': 6, 'c': 9 }
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_valuesobject"></a>`_.values(object)`
<a href="#_valuesobject">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L3261 "View in source") [&#x24C9;][1]

Creates an array composed of the own enumerable property values of `object`.

#### Arguments
1. `object` *(Object)*: The object to inspect.

#### Returns
*(Array)*: Returns an array of property values.

#### Example
```js
_.values({ 'one': 1, 'two': 2, 'three': 3 });
// => [1, 2, 3] (property order is not guaranteed across environments)
```

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `“Utilities” Methods`

<!-- div -->

### <a id="_now"></a>`_.now`
<a href="#_now">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6351 "View in source") [&#x24C9;][1]

*(unknown)*: Gets the number of milliseconds that have elapsed since the Unix epoch *(1 January `1970 00`:00:00 UTC)*.

#### Example
```js
var stamp = _.now();
_.defer(function() { console.log(_.now() - stamp); });
// => logs the number of milliseconds it took for the deferred function to be called
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_constantvalue"></a>`_.constant(value)`
<a href="#_constantvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6125 "View in source") [&#x24C9;][1]

Creates a function that returns `value`.

#### Arguments
1. `value` *(&#42;)*: The value to return from the new function.

#### Returns
*(Function)*: Returns the new function.

#### Example
```js
var object = { 'name': 'fred' };
var getter = _.constant(object);
getter() === object;
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_createcallbackfuncidentity-thisarg-argcount"></a>`_.createCallback([func=identity], [thisArg], [argCount])`
<a href="#_createcallbackfuncidentity-thisarg-argcount">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6162 "View in source") [&#x24C9;][1]

Produces a callback bound to an optional `thisArg`. If `func` is a property name the created callback will return the property value for a given element. If `func` is an object the created callback will return `true` for elements that contain the equivalent object properties, otherwise it will return `false`.

#### Arguments
1. `[func=identity]` *(&#42;)*: The value to convert to a callback.
2. `[thisArg]` *(&#42;)*: The `this` binding of the created callback.
3. `[argCount]` *(number)*: The number of arguments the callback accepts.

#### Returns
*(Function)*: Returns a callback function.

#### Example
```js
var characters = [
  { 'name': 'barney', 'age': 36 },
  { 'name': 'fred',   'age': 40 }
];

// wrap to create custom callback shorthands
_.createCallback = _.wrap(_.createCallback, function(func, callback, thisArg) {
  var match = /^(.+?)__([gl]t)(.+)$/.exec(callback);
  return !match ? func(callback, thisArg) : function(object) {
    return match[2] == 'gt' ? object[match[1]] > match[3] : object[match[1]] < match[3];
  };
});

_.filter(characters, 'age__gt38');
// => [{ 'name': 'fred', 'age': 40 }]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_escapestring"></a>`_.escape(string)`
<a href="#_escapestring">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6211 "View in source") [&#x24C9;][1]

Converts the characters `&`, `<`, `>`, `"`, and `'` in `string` to their corresponding HTML entities.

#### Arguments
1. `string` *(string)*: The string to escape.

#### Returns
*(string)*: Returns the escaped string.

#### Example
```js
_.escape('Fred, Wilma, & Pebbles');
// => 'Fred, Wilma, &amp; Pebbles'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_identityvalue"></a>`_.identity(value)`
<a href="#_identityvalue">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6229 "View in source") [&#x24C9;][1]

This method returns the first argument provided to it.

#### Arguments
1. `value` *(&#42;)*: Any value.

#### Returns
*(&#42;)*: Returns `value`.

#### Example
```js
var object = { 'name': 'fred' };
_.identity(object) === object;
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_mixinobjectlodash-source-options"></a>`_.mixin([object=lodash], source, [options])`
<a href="#_mixinobjectlodash-source-options">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6261 "View in source") [&#x24C9;][1]

Adds function properties of a source object to the destination object. If `object` is a function methods will be added to its prototype as well.

#### Arguments
1. `[object=lodash]` *(Function|Object)*: object The destination object.
2. `source` *(Object)*: The object of functions to add.
3. `[options]` *(Object)*: The options object.
4. `[options.chain=true]` *(boolean)*: Specify whether the functions added are chainable.

#### Example
```js
function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}

_.mixin({ 'capitalize': capitalize });
_.capitalize('fred');
// => 'Fred'

_('fred').capitalize().value();
// => 'Fred'

_.mixin({ 'capitalize': capitalize }, { 'chain': false });
_('fred').capitalize();
// => 'Fred'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_noconflict"></a>`_.noConflict()`
<a href="#_noconflict">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6317 "View in source") [&#x24C9;][1]

Reverts the '_' variable to its previous value and returns a reference to the `lodash` function.

#### Returns
*(Function)*: Returns the `lodash` function.

#### Example
```js
var lodash = _.noConflict();
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_noop"></a>`_.noop()`
<a href="#_noop">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6334 "View in source") [&#x24C9;][1]

A no-operation function.

#### Example
```js
var object = { 'name': 'fred' };
_.noop(object) === undefined;
// => true
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_parseintvalue-radix"></a>`_.parseInt(value, [radix])`
<a href="#_parseintvalue-radix">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6374 "View in source") [&#x24C9;][1]

Converts the given value into an integer of the specified radix. If `radix` is `undefined` or `0` a `radix` of `10` is used unless the `value` is a hexadecimal, in which case a `radix` of `16` is used.

Note: This method avoids differences in native ES3 and ES5 `parseInt` implementations. See http://es5.github.io/#E.

#### Arguments
1. `value` *(string)*: The value to parse.
2. `[radix]` *(number)*: The radix used to interpret the value to parse.

#### Returns
*(number)*: Returns the new integer value.

#### Example
```js
_.parseInt('08');
// => 8
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_propertykey"></a>`_.property(key)`
<a href="#_propertykey">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6403 "View in source") [&#x24C9;][1]

Creates a "_.pluck" style function, which returns the `key` value of a given object.

#### Arguments
1. `key` *(string)*: The name of the property to retrieve.

#### Returns
*(Function)*: Returns the new function.

#### Example
```js
var characters = [
  { 'name': 'fred',   'age': 40 },
  { 'name': 'barney', 'age': 36 }
];

var getName = _.property('name');

_.map(characters, getName);
// => ['barney', 'fred']

_.sortBy(characters, getName);
// => [{ 'name': 'barney', 'age': 36 }, { 'name': 'fred',   'age': 40 }]
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_randommin0-max1-floatingfalse"></a>`_.random([min=0], [max=1], [floating=false])`
<a href="#_randommin0-max1-floatingfalse">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6436 "View in source") [&#x24C9;][1]

Produces a random number between `min` and `max` *(inclusive)*. If only one argument is provided a number between `0` and the given number will be returned. If `floating` is truey or either `min` or `max` are floats a floating-point number will be returned instead of an integer.

#### Arguments
1. `[min=0]` *(number)*: The minimum possible value.
2. `[max=1]` *(number)*: The maximum possible value.
3. `[floating=false]` *(boolean)*: Specify returning a floating-point number.

#### Returns
*(number)*: Returns a random number.

#### Example
```js
_.random(0, 5);
// => an integer between 0 and 5

_.random(5);
// => also an integer between 0 and 5

_.random(5, true);
// => a floating-point number between 0 and 5

_.random(1.2, 5.2);
// => a floating-point number between 1.2 and 5.2
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_resultobject-key"></a>`_.result(object, key)`
<a href="#_resultobject-key">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6494 "View in source") [&#x24C9;][1]

Resolves the value of property `key` on `object`. If `key` is a function it will be invoked with the `this` binding of `object` and its result returned, else the property value is returned. If `object` is falsey then `undefined` is returned.

#### Arguments
1. `object` *(Object)*: The object to inspect.
2. `key` *(string)*: The name of the property to resolve.

#### Returns
*(&#42;)*: Returns the resolved value.

#### Example
```js
var object = {
  'cheese': 'crumpets',
  'stuff': function() {
    return 'nonsense';
  }
};

_.result(object, 'cheese');
// => 'crumpets'

_.result(object, 'stuff');
// => 'nonsense'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_runincontextcontextroot"></a>`_.runInContext([context=root])`
<a href="#_runincontextcontextroot">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L469 "View in source") [&#x24C9;][1]

Create a new `lodash` function using the given context object.

#### Arguments
1. `[context=root]` *(Object)*: The context object.

#### Returns
*(Function)*: Returns the `lodash` function.

* * *

<!-- /div -->


<!-- div -->

### <a id="_templatetext-data-options-optionsescape-optionsevaluate-optionsimports-optionsinterpolate-sourceurl-variable"></a>`_.template(text, data, [options], [options.escape], [options.evaluate], [options.imports], [options.interpolate], [sourceURL], [variable])`
<a href="#_templatetext-data-options-optionsescape-optionsevaluate-optionsimports-optionsinterpolate-sourceurl-variable">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6587 "View in source") [&#x24C9;][1]

A micro-templating method that handles arbitrary delimiters, preserves whitespace, and correctly escapes quotes within interpolated code.

Note: In the development build, `_.template` utilizes sourceURLs for easier debugging. See http://www.html5rocks.com/en/tutorials/developertools/sourcemaps/#toc-sourceurl

For more information on precompiling templates see:<br>
http://lodash.com/custom-builds

For more information on Chrome extension sandboxes see:<br>
http://developer.chrome.com/stable/extensions/sandboxingEval.html

#### Arguments
1. `text` *(string)*: The template text.
2. `data` *(Object)*: The data object used to populate the text.
3. `[options]` *(Object)*: The options object.
4. `[options.escape]` *(RegExp)*: The "escape" delimiter.
5. `[options.evaluate]` *(RegExp)*: The "evaluate" delimiter.
6. `[options.imports]` *(Object)*: An object to import into the template as local variables.
7. `[options.interpolate]` *(RegExp)*: The "interpolate" delimiter.
8. `[sourceURL]` *(string)*: The sourceURL of the template's compiled source.
9. `[variable]` *(string)*: The data object variable name.

#### Returns
*(Function, string)*: Returns a compiled function when no `data` object  is given, else it returns the interpolated text.

#### Example
```js
// using the "interpolate" delimiter to create a compiled template
var compiled = _.template('hello <%= name %>');
compiled({ 'name': 'fred' });
// => 'hello fred'

// using the "escape" delimiter to escape HTML in data property values
_.template('<b><%- value %></b>', { 'value': '<script>' });
// => '<b>&lt;script&gt;</b>'

// using the "evaluate" delimiter to generate HTML
var list = '<% _.forEach(people, function(name) { %><li><%- name %></li><% }); %>';
_.template(list, { 'people': ['fred', 'barney'] });
// => '<li>fred</li><li>barney</li>'

// using the ES6 delimiter as an alternative to the default "interpolate" delimiter
_.template('hello ${ name }', { 'name': 'pebbles' });
// => 'hello pebbles'

// using the internal `print` function in "evaluate" delimiters
_.template('<% print("hello " + name); %>!', { 'name': 'barney' });
// => 'hello barney!'

// using a custom template delimiters
_.templateSettings = {
  'interpolate': /{{([\s\S]+?)}}/g
};

_.template('hello {{ name }}!', { 'name': 'mustache' });
// => 'hello mustache!'

// using the `imports` option to import jQuery
var list = '<% jq.each(people, function(name) { %><li><%- name %></li><% }); %>';
_.template(list, { 'people': ['fred', 'barney'] }, { 'imports': { 'jq': jQuery } });
// => '<li>fred</li><li>barney</li>'

// using the `sourceURL` option to specify a custom sourceURL for the template
var compiled = _.template('hello <%= name %>', null, { 'sourceURL': '/basic/greeting.jst' });
compiled(data);
// => find the source of "greeting.jst" under the Sources tab or Resources panel of the web inspector

// using the `variable` option to ensure a with-statement isn't used in the compiled template
var compiled = _.template('hi <%= data.name %>!', null, { 'variable': 'data' });
compiled.source;
// => function(data) {
  var __t, __p = '', __e = _.escape;
  __p += 'hi ' + ((__t = ( data.name )) == null ? '' : __t) + '!';
  return __p;
}

// using the `source` property to inline compiled templates for meaningful
// line numbers in error messages and a stack trace
fs.writeFileSync(path.join(cwd, 'jst.js'), '\
  var JST = {\
    "main": ' + _.template(mainText).source + '\
  };\
');
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_timesn-callback-thisarg"></a>`_.times(n, callback, [thisArg])`
<a href="#_timesn-callback-thisarg">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6710 "View in source") [&#x24C9;][1]

Executes the callback `n` times, returning an array of the results of each callback execution. The callback is bound to `thisArg` and invoked with one argument; *(index)*.

#### Arguments
1. `n` *(number)*: The number of times to execute the callback.
2. `callback` *(Function)*: The function called per iteration.
3. `[thisArg]` *(&#42;)*: The `this` binding of `callback`.

#### Returns
*(Array)*: Returns an array of the results of each `callback` execution.

#### Example
```js
var diceRolls = _.times(3, _.partial(_.random, 1, 6));
// => [3, 6, 4]

_.times(3, function(n) { mage.castSpell(n); });
// => calls `mage.castSpell(n)` three times, passing `n` of `0`, `1`, and `2` respectively

_.times(3, function(n) { this.cast(n); }, mage);
// => also calls `mage.castSpell(n)` three times
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_unescapestring"></a>`_.unescape(string)`
<a href="#_unescapestring">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6737 "View in source") [&#x24C9;][1]

The inverse of `_.escape` this method converts the HTML entities `&amp;`, `&lt;`, `&gt;`, `&quot;`, and `&#39;` in `string` to their corresponding characters.

#### Arguments
1. `string` *(string)*: The string to unescape.

#### Returns
*(string)*: Returns the unescaped string.

#### Example
```js
_.unescape('Fred, Barney &amp; Pebbles');
// => 'Fred, Barney & Pebbles'
```

* * *

<!-- /div -->


<!-- div -->

### <a id="_uniqueidprefix"></a>`_.uniqueId([prefix])`
<a href="#_uniqueidprefix">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L6757 "View in source") [&#x24C9;][1]

Generates a unique ID. If `prefix` is provided the ID will be appended to it.

#### Arguments
1. `[prefix]` *(string)*: The value to prefix the ID with.

#### Returns
*(string)*: Returns the unique ID.

#### Example
```js
_.uniqueId('contact_');
// => 'contact_104'

_.uniqueId();
// => '105'
```

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Methods`

<!-- div -->

### <a id="_templatesettingsimports_"></a>`_.templateSettings.imports._`
<a href="#_templatesettingsimports_">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L867 "View in source") [&#x24C9;][1]

A reference to the `lodash` function.

* * *

<!-- /div -->


<!-- /div -->


<!-- div -->

## `Properties`

<!-- div -->

### <a id="_version"></a>`_.VERSION`
<a href="#_version">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L7078 "View in source") [&#x24C9;][1]

*(string)*: The semantic version number.

* * *

<!-- /div -->


<!-- div -->

### <a id="_support"></a>`_.support`
<a href="#_support">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L676 "View in source") [&#x24C9;][1]

*(Object)*: An object used to flag environments features.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportargsclass"></a>`_.support.argsClass`
<a href="#_supportargsclass">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L693 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if an `arguments` object's &#91;&#91;Class&#93;&#93; is resolvable *(all but Firefox < `4`, IE < `9`)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportargsobject"></a>`_.support.argsObject`
<a href="#_supportargsobject">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L701 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if `arguments` objects are `Object` objects *(all but Narwhal and Opera < `10.5`)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportenumerrorprops"></a>`_.support.enumErrorProps`
<a href="#_supportenumerrorprops">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L710 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if `name` or `message` properties of `Error.prototype` are enumerable by default. *(IE < `9`, Safari < `5.1`)*

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportenumprototypes"></a>`_.support.enumPrototypes`
<a href="#_supportenumprototypes">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L723 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if `prototype` properties are enumerable by default.

Firefox < `3.6`, Opera > `9.50` - Opera < `11.60`, and Safari < `5.1` *(if the prototype or a property on the prototype has been set)* incorrectly sets a function's `prototype` property &#91;&#91;Enumerable&#93;&#93; value to `true`.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportfuncdecomp"></a>`_.support.funcDecomp`
<a href="#_supportfuncdecomp">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L732 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if functions can be decompiled by `Function#toString` *(all but PS3 and older Opera mobile browsers & avoided in Windows `8` apps)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportfuncnames"></a>`_.support.funcNames`
<a href="#_supportfuncnames">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L740 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if `Function#name` is supported *(all but IE)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportnonenumargs"></a>`_.support.nonEnumArgs`
<a href="#_supportnonenumargs">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L749 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if `arguments` object indexes are non-enumerable *(Firefox < `4`, IE < `9`, PhantomJS, Safari < `5.1`)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportnonenumshadows"></a>`_.support.nonEnumShadows`
<a href="#_supportnonenumshadows">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L760 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if properties shadowing those on `Object.prototype` are non-enumerable.

In IE < `9` an objects own properties, shadowing non-enumerable ones, are made non-enumerable as well *(a.k.a the JScript &#91;&#91;DontEnum&#93;&#93; bug)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportownlast"></a>`_.support.ownLast`
<a href="#_supportownlast">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L768 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if own properties are iterated after inherited properties *(all but IE < `9`)*.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportspliceobjects"></a>`_.support.spliceObjects`
<a href="#_supportspliceobjects">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L782 "View in source") [&#x24C9;][1]

*(boolean)*: Detect if `Array#shift` and `Array#splice` augment array-like objects correctly.

Firefox < `10`, IE compatibility mode, and IE < `9` have buggy Array `shift()` and `splice()` functions that fail to remove the last element, `value[0]`, of array-like objects even though the `length` property is set to `0`. The `shift()` method is buggy in IE `8` compatibility mode, while `splice()` is buggy regardless of mode in IE < `9` and buggy in compatibility mode in IE `9`.

* * *

<!-- /div -->


<!-- div -->

### <a id="_supportunindexedchars"></a>`_.support.unindexedChars`
<a href="#_supportunindexedchars">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L793 "View in source") [&#x24C9;][1]

*(boolean)*: Detect lack of support for accessing string characters by index.

IE < `8` can't access characters by index and IE `8` can only access characters by index on string literals.

* * *

<!-- /div -->


<!-- div -->

### <a id="_templatesettings"></a>`_.templateSettings`
<a href="#_templatesettings">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L819 "View in source") [&#x24C9;][1]

*(Object)*: By default, the template delimiters used by Lo-Dash are similar to those in embedded Ruby *(ERB)*. Change the following template settings to use alternative delimiters.

* * *

<!-- /div -->


<!-- div -->

### <a id="_templatesettingsescape"></a>`_.templateSettings.escape`
<a href="#_templatesettingsescape">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L827 "View in source") [&#x24C9;][1]

*(RegExp)*: Used to detect `data` property values to be HTML-escaped.

* * *

<!-- /div -->


<!-- div -->

### <a id="_templatesettingsevaluate"></a>`_.templateSettings.evaluate`
<a href="#_templatesettingsevaluate">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L835 "View in source") [&#x24C9;][1]

*(RegExp)*: Used to detect code to be evaluated.

* * *

<!-- /div -->


<!-- div -->

### <a id="_templatesettingsinterpolate"></a>`_.templateSettings.interpolate`
<a href="#_templatesettingsinterpolate">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L843 "View in source") [&#x24C9;][1]

*(RegExp)*: Used to detect `data` property values to inject.

* * *

<!-- /div -->


<!-- div -->

### <a id="_templatesettingsvariable"></a>`_.templateSettings.variable`
<a href="#_templatesettingsvariable">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L851 "View in source") [&#x24C9;][1]

*(string)*: Used to reference the data object in the template text.

* * *

<!-- /div -->


<!-- div -->

### <a id="_templatesettingsimports"></a>`_.templateSettings.imports`
<a href="#_templatesettingsimports">#</a> [&#x24C8;](https://github.com/lodash/lodash/blob/2.4.1/lodash.js#L859 "View in source") [&#x24C9;][1]

*(Object)*: Used to import variables into the compiled template.

* * *

<!-- /div -->


<!-- /div -->


<!-- /div -->


  [1]: #arrays "Jump back to the TOC."
ARC2
====

ARC2 is a PHP 5.3 library for working with RDF.
It also provides a MySQL-based triplestore with SPARQL support.

Feature-wise, ARC2 is now in a stable state with no further feature additions planned. 
Issues are still being fixed and Pull Requests are welcome, though.# mustache.js - Logic-less {{mustache}} templates with JavaScript

> What could be more logical awesome than no logic at all?

[![Gitter chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/janl/mustache.js)

[mustache.js](http://github.com/janl/mustache.js) is an implementation of the [mustache](http://mustache.github.com/) template system in JavaScript.

[Mustache](http://mustache.github.com/) is a logic-less template syntax. It can be used for HTML, config files, source code - anything. It works by expanding tags in a template using values provided in a hash or object.

We call it "logic-less" because there are no if statements, else clauses, or for loops. Instead there are only tags. Some tags are replaced with a value, some nothing, and others a series of values.

For a language-agnostic overview of mustache's template syntax, see the `mustache(5)` [manpage](http://mustache.github.com/mustache.5.html).

## Where to use mustache.js?

You can use mustache.js to render mustache templates anywhere you can use JavaScript. This includes web browsers, server-side environments such as [node](http://nodejs.org/), and [CouchDB](http://couchdb.apache.org/) views.

mustache.js ships with support for both the [CommonJS](http://www.commonjs.org/) module API and the [Asynchronous Module Definition](https://github.com/amdjs/amdjs-api/wiki/AMD) API, or AMD.

And this will be your templates after you use Mustache:

!['stache](http://d24w6bsrhbeh9d.cloudfront.net/photo/aZPNGon_460sa.gif)

## Who uses mustache.js?

An updated list of mustache.js users is kept [on the Github wiki](http://wiki.github.com/janl/mustache.js/beard-competition). Add yourself or your company if you use mustache.js!

## Contributing

mustache.js is a mature project, but it continues to actively invite maintainers. You can help out a high-profile project that is used in a lot of places on the web. There is [plenty](https://github.com/janl/mustache.js/issues) of [work](https://github.com/janl/mustache.js/pulls) to do. No big commitment required, if all you do is review a single [Pull Request](https://github.com/janl/mustache.js/pulls), you are a maintainer. And a hero.

### Your First Contribution

- review a [Pull Request](https://github.com/janl/mustache.js/pulls)
- fix an [Issue](https://github.com/janl/mustache.js/issues)
- update the [documentation](https://github.com/janl/mustache.js#usage)
- make a website
- write a tutorial

* * *

## Usage

Below is quick example how to use mustache.js:

```js
var view = {
  title: "Joe",
  calc: function () {
    return 2 + 4;
  }
};

var output = Mustache.render("{{title}} spends {{calc}}", view);
```

In this example, the `Mustache.render` function takes two parameters: 1) the [mustache](http://mustache.github.com/) template and 2) a `view` object that contains the data and code needed to render the template.

## Templates

A [mustache](http://mustache.github.com/) template is a string that contains any number of mustache tags. Tags are indicated by the double mustaches that surround them. `{{person}}` is a tag, as is `{{#person}}`. In both examples we refer to `person` as the tag's key. There are several types of tags available in mustache.js, described below.

There are several techniques that can be used to load templates and hand them to mustache.js, here are two of them:

#### Include Templates

If you need a template for a dynamic part in a static website, you can consider including the template in the static HTML file to avoid loading templates separately. Here's a small example using `jQuery`:

```html
<html>
<body onload="loadUser">
<div id="target">Loading...</div>
<script id="template" type="x-tmpl-mustache">
Hello {{ name }}!
</script>
</body>
</html>
```

```js
function loadUser() {
  var template = $('#template').html();
  Mustache.parse(template);   // optional, speeds up future uses
  var rendered = Mustache.render(template, {name: "Luke"});
  $('#target').html(rendered);
}
```

#### Load External Templates

If your templates reside in individual files, you can load them asynchronously and render them when they arrive. Another example using `jQuery`:

```js
function loadUser() {
  $.get('template.mst', function(template) {
    var rendered = Mustache.render(template, {name: "Luke"});
    $('#target').html(rendered);
  });
}
```

### Variables

The most basic tag type is a simple variable. A `{{name}}` tag renders the value of the `name` key in the current context. If there is no such key, nothing is rendered.

All variables are HTML-escaped by default. If you want to render unescaped HTML, use the triple mustache: `{{{name}}}`. You can also use `&` to unescape a variable.

View:

```json
{
  "name": "Chris",
  "company": "<b>GitHub</b>"
}
```

Template:

```html
* {{name}}
* {{age}}
* {{company}}
* {{{company}}}
* {{&company}}
```

Output:

```html
* Chris
*
* &lt;b&gt;GitHub&lt;/b&gt;
* <b>GitHub</b>
* <b>GitHub</b>
```

JavaScript's dot notation may be used to access keys that are properties of objects in a view.

View:

```json
{
  "name": {
    "first": "Michael",
    "last": "Jackson"
  },
  "age": "RIP"
}
```

Template:

```html
* {{name.first}} {{name.last}}
* {{age}}
```

Output:

```html
* Michael Jackson
* RIP
```

### Sections

Sections render blocks of text one or more times, depending on the value of the key in the current context.

A section begins with a pound and ends with a slash. That is, `{{#person}}` begins a `person` section, while `{{/person}}` ends it. The text between the two tags is referred to as that section's "block".

The behavior of the section is determined by the value of the key.

#### False Values or Empty Lists

If the `person` key does not exist, or exists and has a value of `null`, `undefined`, `false`, `0`, or `NaN`, or is an empty string or an empty list, the block will not be rendered.

View:

```json
{
  "person": false
}
```

Template:

```html
Shown.
{{#person}}
Never shown!
{{/person}}
```

Output:

```html
Shown.
```

#### Non-Empty Lists

If the `person` key exists and is not `null`, `undefined`, or `false`, and is not an empty list the block will be rendered one or more times.

When the value is a list, the block is rendered once for each item in the list. The context of the block is set to the current item in the list for each iteration. In this way we can loop over collections.

View:

```json
{
  "stooges": [
    { "name": "Moe" },
    { "name": "Larry" },
    { "name": "Curly" }
  ]
}
```

Template:

```html
{{#stooges}}
<b>{{name}}</b>
{{/stooges}}
```

Output:

```html
<b>Moe</b>
<b>Larry</b>
<b>Curly</b>
```

When looping over an array of strings, a `.` can be used to refer to the current item in the list.

View:

```json
{
  "musketeers": ["Athos", "Aramis", "Porthos", "D'Artagnan"]
}
```

Template:

```html
{{#musketeers}}
* {{.}}
{{/musketeers}}
```

Output:

```html
* Athos
* Aramis
* Porthos
* D'Artagnan
```

If the value of a section variable is a function, it will be called in the context of the current item in the list on each iteration.

View:

```js
{
  "beatles": [
    { "firstName": "John", "lastName": "Lennon" },
    { "firstName": "Paul", "lastName": "McCartney" },
    { "firstName": "George", "lastName": "Harrison" },
    { "firstName": "Ringo", "lastName": "Starr" }
  ],
  "name": function () {
    return this.firstName + " " + this.lastName;
  }
}
```

Template:

```html
{{#beatles}}
* {{name}}
{{/beatles}}
```

Output:

```html
* John Lennon
* Paul McCartney
* George Harrison
* Ringo Starr
```

#### Functions

If the value of a section key is a function, it is called with the section's literal block of text, un-rendered, as its first argument. The second argument is a special rendering function that uses the current view as its view argument. It is called in the context of the current view object.

View:

```js
{
  "name": "Tater",
  "bold": function () {
    return function (text, render) {
      return "<b>" + render(text) + "</b>";
    }
  }
}
```

Template:

```html
{{#bold}}Hi {{name}}.{{/bold}}
```

Output:

```html
<b>Hi Tater.</b>
```

### Inverted Sections

An inverted section opens with `{{^section}}` instead of `{{#section}}`. The block of an inverted section is rendered only if the value of that section's tag is `null`, `undefined`, `false`, *falsy* or an empty list.

View:

```json
{
  "repos": []
}
```

Template:

```html
{{#repos}}<b>{{name}}</b>{{/repos}}
{{^repos}}No repos :({{/repos}}
```

Output:

```html
No repos :(
```

### Comments

Comments begin with a bang and are ignored. The following template:

```html
<h1>Today{{! ignore me }}.</h1>
```

Will render as follows:

```html
<h1>Today.</h1>
```

Comments may contain newlines.

### Partials

Partials begin with a greater than sign, like {{> box}}.

Partials are rendered at runtime (as opposed to compile time), so recursive partials are possible. Just avoid infinite loops.

They also inherit the calling context. Whereas in ERB you may have this:

```html+erb
<%= partial :next_more, :start => start, :size => size %>
```

Mustache requires only this:

```html
{{> next_more}}
```

Why? Because the `next_more.mustache` file will inherit the `size` and `start` variables from the calling context. In this way you may want to think of partials as includes, or template expansion, even though it's not literally true.

For example, this template and partial:

    base.mustache:
    <h2>Names</h2>
    {{#names}}
      {{> user}}
    {{/names}}

    user.mustache:
    <strong>{{name}}</strong>

Can be thought of as a single, expanded template:

```html
<h2>Names</h2>
{{#names}}
  <strong>{{name}}</strong>
{{/names}}
```

In mustache.js an object of partials may be passed as the third argument to `Mustache.render`. The object should be keyed by the name of the partial, and its value should be the partial text.

```js
Mustache.render(template, view, {
  user: userTemplate
});
```

### Set Delimiter

Set Delimiter tags start with an equals sign and change the tag delimiters from `{{` and `}}` to custom strings.

Consider the following contrived example:

```
* {{ default_tags }}
{{=<% %>=}}
* <% erb_style_tags %>
<%={{ }}=%>
* {{ default_tags_again }}
```

Here we have a list with three items. The first item uses the default tag style, the second uses ERB style as defined by the Set Delimiter tag, and the third returns to the default style after yet another Set Delimiter declaration.

According to [ctemplates](http://google-ctemplate.googlecode.com/svn/trunk/doc/howto.html), this "is useful for languages like TeX, where double-braces may occur in the text and are awkward to use for markup."

Custom delimiters may not contain whitespace or the equals sign.

## Pre-parsing and Caching Templates

By default, when mustache.js first parses a template it keeps the full parsed token tree in a cache. The next time it sees that same template it skips the parsing step and renders the template much more quickly. If you'd like, you can do this ahead of time using `mustache.parse`.

```js
Mustache.parse(template);

// Then, sometime later.
Mustache.render(template, view);
```

## Plugins for JavaScript Libraries

mustache.js may be built specifically for several different client libraries, including the following:

  - [jQuery](http://jquery.com/)
  - [MooTools](http://mootools.net/)
  - [Dojo](http://www.dojotoolkit.org/)
  - [YUI](http://developer.yahoo.com/yui/)
  - [qooxdoo](http://qooxdoo.org/)

These may be built using [Rake](http://rake.rubyforge.org/) and one of the following commands:

    $ rake jquery
    $ rake mootools
    $ rake dojo
    $ rake yui3
    $ rake qooxdoo

## Command line tool

mustache.js is shipped with a node based command line tool. It might be installed as a global tool on your computer to render a mustache template of some kind

```bash
$ npm install -g mustache
$ mustache dataView.json myTemplate.mustache > output.html

# also supports stdin
$ cat dataView.json | mustache - myTemplate.mustache > output.html
```

or as a package.json `devDependency` in a build process maybe?

```bash
$ npm install mustache --save-dev
```
```json
{
  "scripts": {
    "build": "mustache dataView.json myTemplate.mustache > public/output.html"
  }
}
```
```bash
$ npm run build
```

The command line tool is basically a wrapper around `Mustache.render` so you get all the aformentioned features.

## Testing

In order to run the tests you'll need to install [node](http://nodejs.org/).

You also need to install the sub module containing [Mustache specifications](http://github.com/mustache/spec) in the project root.

    $ git submodule init
    $ git submodule update

Install dependencies.

    $ npm install

Then run the tests.

    $ npm test

The test suite consists of both unit and integration tests. If a template isn't rendering correctly for you, you can make a test for it by doing the following:

  1. Create a template file named `mytest.mustache` in the `test/_files`
     directory. Replace `mytest` with the name of your test.
  2. Create a corresponding view file named `mytest.js` in the same directory.
     This file should contain a JavaScript object literal enclosed in
     parentheses. See any of the other view files for an example.
  3. Create a file with the expected output in `mytest.txt` in the same
     directory.

Then, you can run the test with:

    $ TEST=mytest npm run test-render

### Troubleshooting

#### npm install fails

Ensure to have a recent version of npm installed. While developing this project requires npm with support for `^` version ranges.

    $ npm install -g npm

## Thanks

mustache.js wouldn't kick ass if it weren't for these fine souls:

  * Chris Wanstrath / defunkt
  * Alexander Lang / langalex
  * Sebastian Cohnen / tisba
  * J Chris Anderson / jchris
  * Tom Robinson / tlrobinson
  * Aaron Quint / quirkey
  * Douglas Crockford
  * Nikita Vasilyev / NV
  * Elise Wood / glytch
  * Damien Mathieu / dmathieu
  * Jakub Kuźma / qoobaa
  * Will Leinweber / will
  * dpree
  * Jason Smith / jhs
  * Aaron Gibralter / agibralter
  * Ross Boucher / boucher
  * Matt Sanford / mzsanford
  * Ben Cherry / bcherry
  * Michael Jackson / mjijackson
storify
=======

This is a PHP library for Storify.
Description will come later.# Welcome to SlickGrid

Find documentation and examples in [the wiki](https://github.com/mleibman/SlickGrid/wiki).


**UPDATE:  March 5th, 2014 - I have too many things going on in my life right now to really give SlickGrid support and development the time and attention it deserves.  I am not stopping it, but I will most likely be unresponsive for some time.  Sorry.**

## SlickGrid is an advanced JavaScript grid/spreadsheet component

Some highlights:

* Adaptive virtual scrolling (handle hundreds of thousands of rows with extreme responsiveness)
* Extremely fast rendering speed
* Supports jQuery UI Themes
* Background post-rendering for richer cells
* Configurable & customizable
* Full keyboard navigation
* Column resize/reorder/show/hide
* Column autosizing & force-fit
* Pluggable cell formatters & editors
* Support for editing and creating new rows.
* Grouping, filtering, custom aggregators, and more!
* Advanced detached & multi-field editors with undo/redo support.
* “GlobalEditorLock” to manage concurrent edits in cases where multiple Views on a page can edit the same data.
* Support for [millions of rows](http://stackoverflow.com/a/2569488/1269037)
FileSaver.js
============

FileSaver.js implements the HTML5 W3C `saveAs()` FileSaver interface in browsers that do
not natively support it. There is a [FileSaver.js demo][1] that demonstrates saving
various media types.

FileSaver.js is the solution to saving files on the client-side, and is perfect for
webapps that need to generate files, or for saving sensitive information that shouldn't be
sent to an external server.

Looking for `canvas.toBlob()` for saving canvases? Check out
[canvas-toBlob.js][2] for a cross-browser implementation.

Supported browsers
------------------

| Browser        | Constructs as | Filenames    | Max Blob Size | Dependencies |
| -------------- | ------------- | ------------ | ------------- | ------------ |
| Firefox 20+    | Blob          | Yes          | 800 MiB       | None         |
| Firefox < 20   | data: URI     | No           | n/a           | [Blob.js](https://github.com/eligrey/Blob.js) |
| Chrome         | Blob          | Yes          | [500 MiB][3]  | None         |
| Chrome for Android | Blob      | Yes          | [500 MiB][3]  | None         |
| IE 10+         | Blob          | Yes          | 600 MiB       | None         |
| Opera 15+      | Blob          | Yes          | 500 MiB       | None         |
| Opera < 15     | data: URI     | No           | n/a           | [Blob.js](https://github.com/eligrey/Blob.js) |
| Safari 6.1+*   | Blob          | No           | ?             | None         |
| Safari < 6     | data: URI     | No           | n/a           | [Blob.js](https://github.com/eligrey/Blob.js) |

Feature detection is possible:

```js
try {
    var isFileSaverSupported = !!new Blob;
} catch (e) {}
```

### IE < 10

It is possible to save text files in IE < 10 without Flash-based polyfills.
See [ChenWenBrian and koffsyrup's `saveTextAs()`](https://github.com/koffsyrup/FileSaver.js#examples) for more details.

### Safari 6.1+

Blobs may be opened instead of saved sometimes—you may have to direct your Safari users to manually
press <kbd>⌘</kbd>+<kbd>S</kbd> to save the file after it is opened. Using the `application/octet-stream` MIME type to force downloads [can cause issues in Safari](https://github.com/eligrey/FileSaver.js/issues/12#issuecomment-47247096).

### iOS

saveAs must be run within a user interaction event such as onTouchDown or onClick; setTimeout will prevent saveAs from triggering. Due to restrictions in iOS saveAs opens in a new window instead of downloading, if you want this fixed please [tell Apple](https://bugs.webkit.org/show_bug.cgi?id=102914) how this bug is affecting you.

Syntax
------

```js
FileSaver saveAs(in Blob data, in DOMString filename)
```

Examples
--------

### Saving text

```js
var blob = new Blob(["Hello, world!"], {type: "text/plain;charset=utf-8"});
saveAs(blob, "hello world.txt");
```

The standard W3C File API [`Blob`][4] interface is not available in all browsers.
[Blob.js][5] is a cross-browser `Blob` implementation that solves this.

### Saving a canvas

```js
var canvas = document.getElementById("my-canvas"), ctx = canvas.getContext("2d");
// draw to canvas...
canvas.toBlob(function(blob) {
    saveAs(blob, "pretty image.png");
});
```

Note: The standard HTML5 `canvas.toBlob()` method is not available in all browsers.
[canvas-toBlob.js][6] is a cross-browser `canvas.toBlob()` that polyfills this.


![Tracking image](https://in.getclicky.com/212712ns.gif)

  [1]: http://eligrey.com/demos/FileSaver.js/
  [2]: https://github.com/eligrey/canvas-toBlob.js
  [3]: https://code.google.com/p/chromium/codesearch#chromium/src/storage/browser/blob/blob_storage_context.cc&type=cs&sq=package:chromium&l=37&rcl=1418672972
  [4]: https://developer.mozilla.org/en-US/docs/DOM/Blob
  [5]: https://github.com/eligrey/Blob.js
  [6]: https://github.com/eligrey/canvas-toBlob.js

Contributing
------------

The `FileSaver.js` distribution file is compiled with Uglify.js like so:

```bash
uglifyjs FileSaver.js --comments /@source/ > FileSaver.min.js
```

Please make sure you build a production version before submitting a pull request.
[![Build Status](https://travis-ci.org/okfn/recline.png)](https://travis-ci.org/okfn/recline)

A simple but powerful library for building data applications in pure Javascript and HTML.

<h3><a href="http://okfnlabs.org/recline/">Recline Website - including Overview, Documentation, Demos etc</a></h3>

## Features

* Open-source (and heavy reuser of existing open-source libraries)
* Pure javascript (no Flash) and designed for integration -- so it is easy to
  embed in other sites and applications
* View and edit your data in clean grid interface
* Bulk update/clean your data using an easy scripting UI
* Visualize your data
* And more ... see <http://okfnlabs.org/recline/>

## Contributing

See CONTRIBUTING.md.

### Contributors

* [Rufus Pollock](http://rufuspollock.org/)
* [Max Ogden](http://maxogden.com/)
* [John Glover](https://github.com/johnglover)
* [James Casbon](http://casbon.me/)
* [Adrià Mercader](http://amercader.net/)
* [Dominik Moritz](https://github.com/domoritz)
* [Friedrich Lindenberg](http://pudo.org/)
* [Alioune Dia](https://github.com/aliounedia)
* [kielni](https://github.com/kielni)
* And [many more](https://github.com/okfn/recline/graphs/contributors)

## Changelog


### v0.7 - Summer 2014 (tbc)

[v0.7 milestone](https://github.com/okfn/recline/issues?milestone=7)

Possible breaking changes

* Support for row/add/delete/Reorder for recline slickGrid check `_includes/recline-deps.html` for slcikGrid plugins required #396
* Upgraded timelinejs lib - #316
* Removed csv backend (as now in separate repo) #444

### v0.6 - Summer 2013

[v0.6 milestone](https://github.com/okfn/recline/issues?milestone=5) (more than 40 issues)

Possible breaking changes

* Many backends moved to their own repositories #314
* Upgarde to Backbone v1.0 #351
* Updated Leaflet to latest version 0.4.4 #220
* Added marker clustering in map view to handle a large number of markers (and allowed it to disabled)
* Dataset.restore method removed (not used internally except from Multiview.restore)
* Views no longer call render in initialize but must be called client code
* Backend.Memory.Store attribute for holding 'records' renamed to `records` from `data`
* Option to use underscore.deferred vendor library and not use jQuery (jQuery no longer required if just using recline.dataset.js)
* View.el is now the raw DOM element. If you want a jQuery-wrapped version, use view.$el. #350
* Pager widget now takes Dataset object rather than QueryState object #386

### v0.5 - July 5th 2012 (first public release)

[40 closed issues](https://github.com/okfn/recline/issues?milestone=2&page=1&state=closed)

Lots of breaking changes to the API from v0.4 (should be very few going forwards) including:

* State only stores backend (name) and dataset url (in url field) rather than entire dataset object
* Backends heavily reorganized
* Rename Document -> Record
* Rename DataExplorer view to MultiView
* ...

### v0.4 - April 26th 2012

[23 closed issues](https://github.com/okfn/recline/issues?milestone=2&page=1&state=closed) including:

* Map view using Leaflet - #69, #64, #89, #97
* Term filter support - #66
* Faceting support- #62
* Tidy up CSS and JS - #81 and #78
* Manage and serialize view and dataset state (plus support for embed and permalinks) - #88, #67
* Graph view improvements e.g. handle date types correctly - #75
* Write support for ES backend - #61
* Remove JQuery-UI dependency in favour of bootstrap modal - #46
* Improved CSV import support - #92

### v0.3 - March 31st 2012

[16 closed issues](https://github.com/okfn/recline/issues?milestone=1&state=closed) including:

* ElasticSearch (and hence DataHub/CKAN) backend - #54
* Loading of local CSV files - #36
* Fully worked out Data Query support - #34, #49, #53, #57
* New Field model object for richer field information - #25
* Upgrade to Bootstrap v2.0 - #55
* Recline Data Explorer app improvements e.g. #39 (import menu)
* Graph improvements - #58 (more graph types, graph interaction)

### v0.2 - Feb 24th 2012

[17 closed issues](https://github.com/okfn/recline/issues?milestone=3&state=closed) including:

* Major refactor of backend and model relationship - #35 and #43
* Support Google Docs Spreadsheets as a Backend - #15
* Support for online CSV and Excel files via DataProxy backend - #31
* Data Explorer is customizable re loaded views - #42
* Start of documentation - #33
* Views in separate files - #41
* Better error reporting from backends on JSONP errors - #30
* Sorting and show/hide of columns in data grid - #23, #29
* Support for pagination - #27
* Split backends into separate files to make them easier to maintain and reuse separately #50

### v0.1 - Jan 28th 2012

* Core models and structure including Dataset and Document
* Memory and webstore backends
* Grid, Graph and Data Explorer views
* Bootstrap-based theme - #22

## Copyright and License

Copyright 2011 Max Ogden and Rufus Pollock.

Licensed under the MIT license:

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


This compiled version of SlickGrid has been obtained with the Google Closure
Compiler, using the following command:

java -jar compiler.jar --js=slick.core.js --js=slick.grid.js --js=slick.editors.js --js_output_file=slick.grid.min.js

There are two other files required for the SlickGrid view to work properly:

 * jquery-ui-1.8.16.custom.min.js 
 * jquery.event.drag-2.0.min.js

These are included in the Recline source, but have not been included in the
built file to make easier to handle compatibility problems.

Please check SlickGrid license in the included MIT-LICENSE.txt file.

[1] https://developers.google.com/closure/compiler/
Verite TimelineJS v2.25
[![NPM version][npm-version-image]][npm-url] [![NPM downloads][npm-downloads-image]][npm-url] [![MIT License][license-image]][license-url] [![Build Status][travis-image]][travis-url]

A lightweight JavaScript date library for parsing, validating, manipulating, and formatting dates.

- - - - - - -

**Important notice**: Moment is undergoing major refactoring for version
**2.10**, that would result in ES6 code that is transpiled to ES5 for
different environments: node, browser global, AMD, various build/packaging
systems.

You might be required to rewrite your pull request on top once we merge it in.

- - - - - - -

## [Documentation](http://momentjs.com/docs/)

## Upgrading to 2.0.0

There are a number of small backwards incompatible changes with version 2.0.0. [See the full descriptions here](https://gist.github.com/timrwood/e72f2eef320ed9e37c51#backwards-incompatible-changes)

 * Changed language ordinal method to return the number + ordinal instead of just the ordinal.

 * Changed two digit year parsing cutoff to match strptime.

 * Removed `moment#sod` and `moment#eod` in favor of `moment#startOf` and `moment#endOf`.

 * Removed `moment.humanizeDuration()` in favor of `moment.duration().humanize()`.

 * Removed the lang data objects from the top level namespace.

 * Duplicate `Date` passed to `moment()` instead of referencing it.

## [Changelog](https://github.com/moment/moment/blob/develop/CHANGELOG.md)

## [Contributing](https://github.com/moment/moment/blob/develop/CONTRIBUTING.md)

## License

Moment.js is freely distributable under the terms of the [MIT license](https://github.com/moment/moment/blob/develop/LICENSE).

[license-image]: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
[license-url]: LICENSE

[npm-url]: https://npmjs.org/package/moment
[npm-version-image]: http://img.shields.io/npm/v/moment.svg?style=flat
[npm-downloads-image]: http://img.shields.io/npm/dm/moment.svg?style=flat

[travis-url]: http://travis-ci.org/moment/moment
[travis-image]: http://img.shields.io/travis/moment/moment/develop.svg?style=flat
Packaging [Moment](momentjs.org) for [Meteor.js](http://meteor.com).


# Meteor

If you're new to Meteor, here's what the excitement is all about -
[watch the first two minutes](https://www.youtube.com/watch?v=fsi0aJ9yr2o); you'll be hooked by 1:28.

That screencast is from 2012. In the meantime, Meteor has become a mature JavaScript-everywhere web
development framework. Read more at [Why Meteor](http://www.meteorpedia.com/read/Why_Meteor).


# Issues

If you encounter an issue while using this package, please CC @dandv when you file it in this repo.


# DONE

* Simple test. Should be enough.


# TODO

* Add other tests; however, that is overkill, and the responsibiity of Moment, not of the Meteor integration.
     ____                     __      __
    /\  _`\                  /\ \    /\ \                                   __
    \ \ \ \ \     __      ___\ \ \/'\\ \ \____    ___     ___      __      /\_\    ____
     \ \  _ <'  /'__`\   /'___\ \ , < \ \ '__`\  / __`\ /' _ `\  /'__`\    \/\ \  /',__\
      \ \ \ \ \/\ \ \.\_/\ \__/\ \ \\`\\ \ \ \ \/\ \ \ \/\ \/\ \/\  __/  __ \ \ \/\__, `\
       \ \____/\ \__/.\_\ \____\\ \_\ \_\ \_,__/\ \____/\ \_\ \_\ \____\/\_\_\ \ \/\____/
        \/___/  \/__/\/_/\/____/ \/_/\/_/\/___/  \/___/  \/_/\/_/\/____/\/_/\ \_\ \/___/
                                                                           \ \____/
                                                                            \/___/
    (_'_______________________________________________________________________________'_)
    (_.———————————————————————————————————————————————————————————————————————————————._)


Backbone supplies structure to JavaScript-heavy applications by providing models with key-value binding and custom events, collections with a rich API of enumerable functions, views with declarative event handling, and connects it all to your existing application over a RESTful JSON interface.

For Docs, License, Tests, pre-packed downloads, and everything else, really, see:
http://backbonejs.org

To suggest a feature, report a bug, or general discussion:
https://github.com/jashkenas/backbone/issues

Backbone is an open-sourced component of DocumentCloud:
https://github.com/documentcloud

Many thanks to our contributors:
https://github.com/jashkenas/backbone/graphs/contributors

Special thanks to Robert Kieffer for the original philosophy behind Backbone.
https://github.com/broofa
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
all sites. Alternatively, the sites/your_site_name/themes directory pattern
may be used to restrict themes to a specific site instance.

MORE INFORMATION
-----------------

Refer to the "Appearance" section of the README.txt in the Drupal root directory
for further information on customizing the appearance of Drupal with custom
themes.

This directory should be used to place downloaded and custom fonts
for your theme.
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
Drupal cache so it can be found. (Alternatively, you can disable the module
before moving it and then re-enable it after the move.)

MULTISITE CONFIGURATION
-----------------------

In multisite configurations, modules found in this directory are available to
all sites. Alternatively, the sites/your_site_name/modules directory pattern
may be used to restrict modules to a specific site instance.

MORE INFORMATION
----------------

Refer to the "Developing for Drupal" section of the README.txt in the Drupal
root directory for further information on extending Drupal with custom modules.
Sometimes when you use relationships in views you get a number of rows with the
same content in some of the fields. This results in a huge table (grid, list,
etc.) that affects the usability of your view.

The Views Merge Rows module provides a way to combine rows with the same content
in the specified fields.

Installation and Configuration
------------------------------
After installing the module you get the “Merge rows” item in the OTHER section
of the Views UI.

To configure the row merging click the link next to the “Merge rows” item.

In the configuration dialog you can enable/disable row merging with the
“Merge rows with the same content in the specified fields” checkbox.
After you enable the merging you will see the table with all the available
fields. You can specify the “Merge option” for each field.

The fields with “Merge option” set to “Use values of this field as a filter” are
used to check which rows should be merged. If several rows contain exactly the
same values in all of these fields, they are merged together. The values for
other fields are calculated as follows:

For fields with “Merge option” set to “Use the first value of this field” only
the value from the first merged rows is used. The values in other rows are
disregarded.
For fields with “Merge option” set to “Merge values of this field” all the
values appears in the resulting row.
Custom search 7.x-1.x
--------------------------

Install
-------
* Enable the module
* Go to Configuration > Search And Metadata > Custom Search (admin/config/search/custom_search) to change settings
* Don't forget to set permissions, otherwise nobody will see the changes

Description
-----------
This module alters the default search box in many ways.
If you need to have options available like in advanced search,
but directly in the search box, this module is for you.

The module adds options to select:

- which content type(s) to search,
- which specific module search to use
(node, help, user or any module that implements search),
- which taxonomy term to search in the results (by vocabulary).
- For all these choices, there are options to switch between a select box,
checkboxes or radio buttons, and also customize the selector
label and the default - Any - text.

There are also options to:

- change the default search box label,
- adds a default text in the search box,
- change the default submit button text,
- use an image instead of the submit button,
- via a "tabledrag", the ordering of all the added options can be changed.

Finally, there's some javascript to:

- check if the search box is not empty on submit,
- clear the default text on focus, and put it back on blur
(if search box is empty),
- handle checkboxes (deselect some checkbox if -Any-,
or a special module search, is checked),
- reselect options in the advanced search options (in results page).


The module integrates well with Internationalization (i18n_string).

This module is inspired by some modules that implements some of these options
(search_config, search_type, custom_seach_box).

Author
------
jdanthinne
COD Alpha3
COD is the Conference Organizing Distribution of Drupal.
For more information, see http://usecod.com and @usecod on Twitter (http://twitter.com/usecod).
To report issues or get support, visit http://drupal.org/project/cod_support or #drupal-cod on IRC.
-- SUMMARY --

The References project contains straight ports of the node_reference and 
user_reference modules to the Drupal 7 API.

For a full description of the module, visit the project page:
  http://drupal.org/project/references
  
-- REQUIREMENTS --

None. 

CCK for Drupal 7 is /not/ a requirement for these modules.

-- GOALS AND LIMITATIONS -- 
  
It is not envisioned as a final solution, but as a way to actually deploy 
Drupal 7 from release day on sites using node and user references much as on 
Drupal 6, until a native entity relationships Drupal 7 module becomes a usable 
alternative.

As of 2010-11-30, is looks like a candidate for that usable alternative might
someday be project Relation: 
  http://drupal.org/project/relation

In short: use these modules now, but be ready to migrate to a different entity
referencing solution during the D7 life cycle.

-- CONTACT --

Current maintainers:

* References: Frederic G. MARAND (fgm) - http://drupal.org/user/27985
* CCK D7: Yves CHEDEMOIS (yched) - http://drupal.org/user/39567

For latest documentation visit: http://drupal.org/node/1432894
Introduction
------------
This module allows creating the front-end forms using Drupal's Field systems.

For more information on adding fields see the Field UI documentation here: http://drupal.org/documentation/modules/field-ui




Installation
-------------
Once you activate the module it sets up an entity administration interface under
Administration > Content > Entityform Types


Usage
---------------
1. Enable the module
2. Goto admin/structure/entityform_types
3. Click "Add an Entityform Type"
4. Fill out basic form information. Under Access Settings make sure at least 1 role can submit the form
5. Click "Save Entityform Type"
6. Click manage fields and add fields the same way you would for a node content type.
7. Once you have added fields you can view the form by clicking the Submit Link on admin/structure/entityform_types


Module Intergration
---------------------
The aim of this module is create a form creation method that leverages that power of entities and fields.  For this reason instead of writting custom code
Drupal entityform_anonymous.module README.txt
================================================================================
***Warning***
Anonymous tracking has not be fully tested yet.

It may allow expose the Entityform Submissions to other users.
Please test throughly.

See: https://drupal.org/node/2181691

@todo add more detailed warning
================================================================================
** Anonymous Links **
================================================================================
This functionality allows for accessing anonymous submissions via anonymous links
with access keys.

This links are available via tokens.

**Anonymous Submission Edit Link
[entityform:anonymous_submission_edit_link]
Link to allow editing anonymous submission.
**Anonymous Submission Submit Link
[entityform:anonymous_submission_submit_link]
Link to allow resubmitting anonymous submission, used when resubmit action is edit old submission.
**Anonymous Submission View Link
[entityform:anonymous_submission_view_link]
Link to allow viewing anonymous submission.

================================================================================
** Anonymous Submission in Browser Sessions **
================================================================================
This functionality allows for tracking anonymous submission through the current
browser sessions.
[![Build Status](https://travis-ci.org/RESTful-Drupal/restful.svg?branch=7.x-2.x)](https://travis-ci.org/RESTful-Drupal/restful)

# RESTful best practices for Drupal

This module allows Drupal to be operated via RESTful HTTP requests, using best
practices for security, performance, and usability.

## Concept
Here are the differences between RESTful and other modules, such as RestWs and
Services Entity:

* RESTful requires explicitly declaring the exposed API. When enabling
the module, nothing happens until a plugin declares it.
* Resources are exposed by bundle, rather than by entity.  This would allow a
developer to expose only nodes of a certain type, for example.
* The exposed properties need to be explicitly declared. This allows a _clean_
output without Drupal's internal implementation leaking out. This means the
consuming client doesn't need to know if an entity is a node or a term, nor will
 they be presented with the ``field_`` prefix.
* Resource versioning is built-in, so that resources can be reused with multiple
consumers.  The versions are at the resource level, for more flexibility and
control.
* It has configurable output formats. It ships with JSON (the default one), JSON+HAL and as an example also XML.
* Audience is developers and not site builders.
* Provide a key tool for a headless Drupal. See the [AngularJs form](https://github.com/Gizra/restful/blob/7.x-1.x/modules/restful_angular_example/README.md) example module.


## Module dependencies

  * [Entity API](https://drupal.org/project/entity), with the following patches:
  * [Prevent notice in entity_metadata_no_hook_node_access() when node is not saved](https://drupal.org/node/2086225#comment-8768373)

## Recipes
Read even more examples on how to use the RESTful module in the [module documentation
node](https://www.drupal.org/node/2380679) in Drupal.org. Make sure you read the _Recipes_
section. If you have any to share, feel free to add your own recipes.

## Declaring a REST Endpoint

A RESTful endpoint is declared via a custom module that includes a plugin which
describes the resource you want to make available.  Here are the bare
essentials from one of the multiple examples in
[the example module](./modules/restful_example):

####restful\_custom/restful\_custom.info
```ini
name = RESTful custom
description = Custom RESTful resource.
core = 7.x
dependencies[] = restful

registry_autoload[] = PSR-4
```

####restful\_custom/src/Plugin/resource/Custom__1_0.php
```php

namespace Drupal\restful_custom\Plugin\resource;

/**
 * Class Custom__1_0
 * @package Drupal\restful_custom\Plugin\resource
 *
 * @Resource(
 *   name = "custom:1.0",
 *   resource = "custom",
 *   label = "Custom",
 *   description = "My custom resource!",
 *   authenticationTypes = TRUE,
 *   authenticationOptional = TRUE,
 *   dataProvider = {
 *     "entityType": "node",
 *     "bundles": {
 *       "article"
 *     },
 *   },
 *   majorVersion = 1,
 *   minorVersion = 0
 * )
 */
class Custom__1_0 extends ResourceEntity implements ResourceInterface {

  /**
   * Overrides EntityNode::publicFields().
   */
  public function publicFields() {
    $public_fields = parent::publicFields();

    $public_fields['body'] = array(
      'property' => 'body',
      'sub_property' => 'value',
    );

    return $public_fields;
  }
}
```

After declaring this plugin, the resource could be accessed at its root URL,
which would be `http://example.com/api/v1.0/custom`.

### Security, caching, output, and customization

See the [Defining a RESTful Plugin](./docs/plugin.md) document for more details.


## Using your API from within Drupal

The following examples use the _articles_ resource from the _restful\_example_
module.

#### Getting a specific version of a RESTful handler for a resource

```php
// Get handler v1.1
$handler = restful()->getResourceManager()->getPlugin('articles:1.1');
```

#### Create and update an entity
```php
$handler = restful()
  ->getResourceManager()
  ->getPlugin('articles:1.0');
// POST method, to create.
$result = restful()
  ->getFormatterManager()
  ->format($handler->doPost(array('label' => 'example title')));
$id = $result['id'];

// PATCH method to update only the title.
$request['label'] = 'new title';
restful()
  ->getFormatterManager()
  ->format($handler->doPatch($id, $request));
```

#### List entities
```php
$handler = restful()->getResourceManager()->getPlugin('articles:1.0');
$handler->setRequest(Request::create(''));
$result = restful()->getFormatterManager()->format($handler->process(), 'json');

// Output:
array(
  'data' => array(
    array(
      'id' => 1,
      'label' => 'example title',
      'self' => 'https://example.com/node/1',
    );
    array(
      'id' => 2,
      'label' => 'another title',
      'self' => 'https://example.com/node/2',
    );
  ),
);
```

### Sort, Filter, Range, and Sub Requests
See the [Using your API within drupal](./docs/api_drupal.md) documentation for
more details.

## Consuming your API
The following examples use the _articles_ resource from the _restful\_example_
module.

#### Consuming specific versions of your API
```shell
# Handler v1.0
curl https://example.com/api/articles/1 \
  -H "X-API-Version: v1.0"
# or
curl https://example.com/api/v1.0/articles/1

# Handler v1.1
curl https://example.com/api/articles/1 \
  -H "X-API-Version: v1.1"
# or
curl https://example.com/api/v1.1/articles/1
```


#### View multiple articles at once
```shell
# Handler v1.1
curl https://example.com/api/articles/1,2 \
  -H "X-API-Version: v1.1"
```


#### Returning autocomplete results
```shell
curl https://example.com/api/articles?autocomplete[string]=mystring
```


#### URL Query strings, HTTP headers, and HTTP requests
See the [Consuming Your API](./docs/api_url.md) document for more details.

## CORS
RESTful provides support for preflight requests (see the
[Wikipedia example](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing#Preflight_example)
for more details).

To configure the allowed domains, you can:

  - Go to `admin/config/services/restful` and set _CORS Preflight_ to the
allowed domain. This will apply globally unless overridden with the method
below.
  - Set the `allowOrigin` key in your resource definition (in the annotation)
to the allowed domain. This setting will only apply to this resource.

Bear in mind that this check is only performed to the top-level resource.
If you are composing resources with competing `allowOrigin` settings, the
top-level resource will be applied.

## Documenting your API
Clients can access documentation about a resource by making an `OPTIONS` HTTP
request to its root URL. The resource will respond with the field information
in the body, and the information about the available output formats and the
permitted HTTP methods will be contained in the headers.


### Automatic documentation
If your resource is an entity, then it will be partially self-documented,
without you needing to do anything else. This information is automatically
derived from the Entity API and Field API.

Here is a snippet from a typical JSON response using only the automatic
documentation:

```json
{
  "myfield": {
    "info": {
      "label": "My Field",
      "description": "A field within my resource."
    },
    "data": {
      "type": "string",
      "read_only": false,
      "cardinality": 1,
      "required": false
    },
    "form_element": {
      "type": "textfield",
      "default_value": "",
      "placeholder": "",
      "size": 255,
      "allowed_values": null
    }
  }
  // { ... other fields would follow ... }
}
```

Each field you've defined in `publicFields` will output an object similar
to the one listed above.


### Manual documentation
In addition to the automatic documentation provided to you out of the box, you
have the ability to manually document your resources.  See the [Documenting your API](./docs/documentation.md)
documentation for more details.


## Modules integration
* [Entity validator 2.x](https://www.drupal.org/project/entity_validator): Integrate
with a robust entity validation (RESTful 1.x requires Entity Validator 1.x).


## Credits
* [Gizra](http://gizra.com)
* [Mateu Aguiló Bosch](https://github.com/e0ipso)
Tweet Feed v3.0 - Overview
--------------------------
The Tweet Feed module is an advanced importing, displaying and data association module that allows you to pull in tweets by search, user, or list. The parameters of what is pulled in falls under the guidelines of [Twitter's REST API](https://dev.twitter.com/rest/public/rate-limiting)  

Tweets can be displayed as nodes or in views as well as displayed by hash tag or user mention. All hash tags and user mentions are stored as references im the tweet nodes to their corresponding taxonomy term. This gives you great power in terms of displaying tweets with specific content in specific places by leveraging the power of contextual filters and taxonomies.  

Additional documentation and example use cases can be found on the Help Pages after the module has been installed. For additional installation including some important information on uninstalling previous versions of Tweet Feed, please see the Installation section.  

Highlights include:  

* ability to import multiple tweet feeds
* tweets and tweet data are saved as nodes
* option to delete existing data when new tweets are imported
* option to import a node for each user in your tweet feed
* creates linked URLs from URLs, hash tags, and usernames inside the feed itself
* views integration
* contextual filters integration for views

This module exists thanks to the generous support of HighWire Press and Stanford University.

Contextual views inspiration and refinement compliments of Ashley Hall in conjunction with the development of the Symposiac conference platform, supported by the Institute for the Arts and Humanities and UNC.

** Dependencies **
* entityreference
* oauth
* date

There are other dependencies based on these.

* ctools
* date_api
* entity_api

** Highly Recommended **
* views
* views ui (only for setting up your views)

The following access tokens from Twitter are also required:

* API Key
* API Secret Key
* Access Token
* Access Token Secret
* Install

For complete documentation on this module, please visit the Tweet Feed module Wiki located at: 

https://github.com/ElusiveMind/tweet_feed/wiki
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
---------------------

 * Introduction
 * Installation
 * How to use


INTRODUCTION
------------

Current Maintainer: Ian Whitcomb - http://drupal.org/user/771654

Views Responsive Grid provides a views plugin for displaying content in a
responsive(mobile friendly) grid layout. Rather than trying to force the
standard Views grid display to work for mobile this provides the same
functionality, but in DIVs instead of tables. Provided is also the ability to
specify a horizontal or vertical grid layout which will properly stack the
content on a mobile display.


INSTALLATION
------------

1. Download module and copy views_responsive_grid folder to sites/all/modules

2. Enable Views and Views Responsive Grid modules.


HOW TO USE
------------

After enabling the module, create a new view with the responsive grid display
format. Specify the number of columns, and the alignment of the grid.

You'll need to understand that the the module won't provide any default styling
to the grid so you may think it's not working, this is by design. In order for
the columns to work you'll need to specify the class name of your columns. For
example, if your theme utilizes a grid, like Twitter Bootstrap does, you would
specify "span3" as the column class(making sure to use the correct span size).
This will make sure your column adhere to the grid in your Bootstrap based
theme.
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
  "If this text shows up, [[file] was loaded successfully."
  [file] is either 'example_1.js', 'example_2.js', 'example_3.js',
  'example_4.js' or 'libraries_test.js'. If you have SimpleTest's verbose mode
  enabled and see the above text in one of the debug pages, the noted JavaScript
  file was loaded successfully.
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
  - libraries_test: purple"
  If you have SimpleTest's verbose mode enabled, and see the above text in a
  certain color (i.e. not in black), a CSS file was loaded successfully. Which
  file depends on the color as referenced in the text above.
- PHP: The loading of PHP files is tested by defining a dummy function in the
  PHP files and then checking whether this function was defined using
  function_exists(). This can be checked programatically with SimpleTest.
The loading of integration files is tested with the same method. The integration
files are libraries_test.js, libraries_test.css, libraries_test.inc and are
located in the tests directory alongside libraries_test.module (i.e. they are
not in the same directory as this file).
reCAPTCHA for Drupal
====================

The reCAPTCHA module uses the reCAPTCHA web service to
improve the CAPTCHA system and protect email addresses. For
more information on what reCAPTCHA is, please visit:
    https://www.google.com/recaptcha


DEPENDENCIES
------------

* reCAPTCHA depends on the CAPTCHA module.
  https://drupal.org/project/captcha
* Some people have found that they also need to use jQuery Update module.
  https://drupal.org/project/jquery_update


CONFIGURATION
-------------

1. Enable reCAPTCHA and CAPTCHA modules in:
       admin/modules

2. You'll now find a reCAPTCHA tab in the CAPTCHA
   administration page available at:
       admin/config/people/captcha/recaptcha

3. Register for a public and private reCAPTCHA key at:
       https://www.google.com/recaptcha/whyrecaptcha

4. Input the keys into the reCAPTCHA settings. The rest of
   the settings should be fine as their defaults.

5. Visit the Captcha administration page and set where you
   want the reCAPTCHA form to be presented:
       admin/config/people/captcha


MAILHIDE INPUT FORMAT
---------------------

The reCAPTCHA module also comes with an input format to
protect email addresses. This, of course, is optional to
use and is only there if you want it. The following is how
you use that input filter:

1. Enable the reCAPTCHA Mailhide module:
       admin/modules

2. Head over to your text format settings:
       admin/config/content/formats

3. Edit your default input format and add the reCAPTCHA
   Mailhide filter.

4. Click on the Configure tab and put in a public and
   private Mailhide key obtained from:
       https://www.google.com/recaptcha/mailhide/apikey

5. Use the Rearrange tab to rearrange the weight of the
   filter depending on what filters already exist.  Make
   sure it is before the URL Filter.

Note: You will require the installation of the mcrypt
      PHP module in your web server for Mailhide to work:
         http://php.net/manual/en/ref.mcrypt.php


MULTI-DOMAIN SUPPORT
--------------------

Since reCAPTCHA uses API keys that are unique to each
domain, if you're using a multi-domain system using the
same database, the reCAPTCHA module won't work when
querying the reCAPTCHA web service.  If you put the
following into your sites/mysite/settings.php file for
each domain, it will override the API key values and make
it so multi-domain systems are capable.

  $conf = array(
    'recaptcha_public_key' =>  'my other public key',
    'recaptcha_private_key' =>  'my other private key',
  );


CUSTOM RECAPTCHA THEME
----------------------

You can create a custom reCAPTCHA theme widget by setting
the theme of the reCAPTCHA form to "custom" in the
reCAPTCHA administration page.  This will output a custom
form that is themeable through the theme function:
  theme_recaptcha_custom_widget().

If you don't implement this function, it is still quite
easily customizable through manipulating the CSS.

For more information on this, visit:
https://developers.google.com/recaptcha/docs/customization


THANK YOU
---------

 * Thank you goes to the reCAPTCHA team for all their
   help, support and their amazing Captcha solution
       https://www.google.com/recaptcha
reCAPTCHA README
================

The reCAPTCHA PHP Lirary helps you use the reCAPTCHA API. Documentation
for this library can be found at

	http://recaptcha.net/plugins/php

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

# Video module 2 for Drupal 7

This readme file is still under construction.

## Using Zencoder locally

If you testing out the Video module and Zencoder on localhost, you'll need to
use Zencoder's Fetcher script to be notified when a video is finished.

See [the complete instructions](https://app.zencoder.com/docs/guides/advanced-integration/getting-zencoder-notifications-while-developing-locally).

## Troubleshooting

### FFmpeg errors

#### "File for preset 'xyz' not found"

Select "None" in the "FFmpeg video preset" drop down for your preset.

#### "broken ffmpeg default settings detected" "use an encoding preset (vpre)"

Select "libx264-default" in the "FFmpeg video preset" drop down for your preset.

#### "Could not write header for output file #0"

You probably selected the wrong codec for your extension. For instance,
for MP4 you need to select the libx264 video codec and AAC audio codec.

#### "constant rate-factor is incompatible with 2pass"

Either enable "Force one-pass encoding" for your preset, or set the 
"Video bitrate" setting to some bitrate.

#### "Additional information: rc_twopass_stats_in requires at least two packets."

Enable "Force one-pass encoding" for your preset.

#### "video codec not compatible with flv"

Choose a different video codec for your FLV preset.

Examples of codecs that should work:

- Flash Video (FLV) / Sorenson Spark / Sorenson H.263
- libx264 H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10

#### "[aac @ 0x______] Too many bits per frame requested"

The sample rate of your input video is not valid for AAC audio encoding.
Edit your preset and set "Audio sample rate" to 44100 in the
"Advanced audio settings" section.
﻿GeoPHP is a open-source native PHP library for doing geometry operations. It is written entirely in PHP and 
can therefore run on shared hosts. It can read and write a wide variety of formats: WKT (including EWKT), WKB (including EWKB), GeoJSON, 
KML, GPX, GeoRSS). It works with all Simple-Feature geometries (Point, LineString, Polygon, GeometryCollection etc.)
and can be used to get centroids, bounding-boxes, area, and a wide variety of other useful information. 

geoPHP also helpfully wraps the GEOS php extension so that applications can get a transparent performance 
increase when GEOS is installed on the server. When GEOS is installed, geoPHP also becomes
fully compliant with the OpenGIS® Implementation Standard for Geographic information. With GEOS you get the 
full-set of openGIS functions in PHP like Union, IsWithin, Touches etc. This means that applications
get a useful "core-set" of geometry operations that work in all environments, and an "extended-set"of operations 
for environments that have GEOS installed. 

See the 'getting started' section below for references and examples of everything that geoPHP can do.

This project is currently looking for co-maintainers. If you think you can help out, please send me a 
message. Forks are also welcome, please issue pull requests and I will merge them into the main branch.

Getting Started
-----------------------

 * The lastest stable version can always be downloaded at: <https://github.com/downloads/phayes/geoPHP/geoPHP.tar.gz>
 * Read the API Reference at: <https://github.com/phayes/geoPHP/wiki/API-Reference>
 * Examples
   * Using geoPHP as a GIS format converter: <http://github.com/phayes/geoPHP/wiki/Example-format-converter>
 * Other Interesting Links:
   * Learn about GEOS integration at: <https://github.com/phayes/geoPHP/wiki/GEOS>

Example usage
-------------------------------------------------

```php
<?php
include_once('geoPHP.inc');

// Polygon WKT example
$polygon = geoPHP::load('POLYGON((1 1,5 1,5 5,1 5,1 1),(2 2,2 3,3 3,3 2,2 2))','wkt');
$area = $polygon->getArea();
$centroid = $polygon->getCentroid();
$centX = $centroid->getX();
$centY = $centroid->getY();

print "This polygon has an area of ".$area." and a centroid with X=".$centX." and Y=".$centY;

// MultiPoint json example
print "<br/>";
$json = 
'{
   "type": "MultiPoint",
   "coordinates": [
       [100.0, 0.0], [101.0, 1.0]
   ]
}';

$multipoint = geoPHP::load($json, 'json');
$multipoint_points = $multipoint->getComponents();
$first_wkt = $multipoint_points[0]->out('wkt');

print "This multipoint has ".$multipoint->numGeometries()." points. The first point has a wkt representation of ".$first_wkt;
```
=======
	
More Examples
-------------------------------------------------
	
The Well Known Text (WKT) and Well Known Binary (WKB) support is ideal for integrating with MySQL's or PostGIS's spatial capability. 
Once you have SELECTed your data with `'AsText('geo_field')'` or `'AsBinary('geo_field')'`, you can put it straight into 
geoPHP (can be wkt or wkb, but must be the same as how you extracted it from your database):

    $geom = geoPHP::load($dbRow,'wkt');

You can collect multiple geometries into one (note that you must use wkt for this):

    $geom = geoPHP::load("GEOMETRYCOLLECTION(".$dbString1.",".$dbString2.")",'wkt');

Calling get components returns the sub-geometries within a geometry as an array.

    $geom2 = geoPHP::load("GEOMETRYCOLLECTION(LINESTRING(1 1,5 1,5 5,1 5,1 1),LINESTRING(2 2,2 3,3 3,3 2,2 2))");
    $geomComponents = $geom2->getComponents();    //an array of the two linestring geometries
    $linestring1 = $geomComponents[0]->getComponents();	//an array of the first linestring's point geometries
    $linestring2 = $geomComponents[1]->getComponents();
    echo $linestring1[0]->x() . ", " . $linestring1[0]->y();    //outputs '1, 1'

An alternative is to use the `asArray()` method. Using the above geometry collection of two linestrings, 
    
	$geometryArray = $geom2->asArray();
	echo $geometryArray[0][0][0] . ", " . $geometryArray[0][0][1];    //outputs '1, 1'

Clearly, more complex analysis is possible.
    
	echo $geom2->envelope()->area();


Working with PostGIS
---------------------
geoPHP, through it's EWKB adapter, has good integration with postGIS. Here's an example of reading and writing postGIS geometries

```php
<?php
include_once('geoPHP.inc');
$host =     'localhost';
$database = 'phayes';
$table =    'test';
$column =   'geom';
$user =     'phayes';
$pass =     'supersecret';

$connection = pg_connect("host=$host dbname=$database user=$user password=$pass");

// Working with PostGIS and Extended-WKB
// ----------------------------

// Using asBinary and GeomFromWKB in PostGIS
$result = pg_fetch_all(pg_query($connection, "SELECT asBinary($column) as geom FROM $table"));
foreach ($result as $item) {
  $wkb = pg_unescape_bytea($item['geom']); // Make sure to unescape the hex blob
  $geom = geoPHP::load($wkb, 'ewkb'); // We now a full geoPHP Geometry object
  
  // Let's insert it back into the database
  $insert_string = pg_escape_bytea($geom->out('ewkb'));
  pg_query($connection, "INSERT INTO $table ($column) values (GeomFromWKB('$insert_string'))");
}

// Using a direct SELECT and INSERTs in PostGIS without using wrapping functions
$result = pg_fetch_all(pg_query($connection, "SELECT $column as geom FROM $table"));
foreach ($result as $item) {
  $wkb = pack('H*',$item['geom']);   // Unpacking the hex blob
  $geom = geoPHP::load($wkb, 'ewkb'); // We now have a geoPHP Geometry
  
  // To insert directly into postGIS we need to unpack the WKB
  $unpacked = unpack('H*', $geom->out('ewkb'));
  $insert_string = $unpacked[1];
  pg_query($connection, "INSERT INTO $table ($column) values ('$insert_string')");
}
```


Credit
-------------------------------------------------

Maintainer: Patrick Hayes

This library was written entirely in my free time as a volunteer. If you find it really useful, please consider making a donation by [clicking here] (https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=geomemes%40gmail%2ecom&lc=US&item_name=Patrick%20Hayes%20-%20geoPHP&no_note=0&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHostedGuest).

Additional Contributors:

 * GeoMemes Research <http://www.geomemes.com>
 * Arnaud Renevier (gisconverter.php) <https://github.com/arenevier/gisconverter.php>
 * Dave Tarc <https://github.com/dtarc>
 * Elliott Hunston (documentation) <https://github.com/ejh>

This library is open-source and dual-licensed under both the Modified BSD License and GPLv2. Either license may be used at your option.           
DESCRIPTION:
------------
Instead of showing a standard "404 Page not found", this module
performs a search on the keywords in the URL.

INSTALLATION:
-------------
1. Extract the tar.gz into your 'modules' or directory.
2. Enable the module at 'administer >> site building >> modules'.
3. The module will automaticly replace the path to your 404 page with "search404"

CONFIGURATION
-------------
1. Visit 'administer >> site configuration >> search 404 settings'

UNINSTALLTION:
--------------
1. Disable the module.
2. Uninstall the module, which will blank the the 404 page

CREDITS:
--------
Written by Lars Sehested Geisler <drupal@larsgeisler.dk>
Maintained by Zyxware, http://www.zyxware.com/
Some code from Steven (found at http://drupal.org/node/12668)
Originally maintained by Johan Forngren, http://johan.forngren.com/


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
Workaround for:

- https://www.drupal.org/node/2450447
- https://www.drupal.org/node/2415991


Files of this folder cannot be included inside the views/tests directory because
they are included as tests cases and make testbot crash.

This files could be moved to tests/templates once
https://www.drupal.org/node/2415991 be properly fixed.
COD Alpha3
COD is the Conference Organizing Distribution of Drupal.
For more information, see http://usecod.com and @usecod on Twitter (http://twitter.com/usecod).
To report issues or get support, visit http://drupal.org/project/cod_support or #drupal-cod on IRC.-- SUMMARY --
This module adds a formatter to the link field that adds a
favicon image infront of the link

-- REQUIREMENTS --
Link module - http://drupal.org/project/link

-- ICON SERVICES USED --
custom php function
http://www.google.com/s2/favicons?domain=
http://getfavicon.appspot.com/

-- INSTALLATION --
Install as usual, see http://drupal.org/node/70151 for further information.

-- CONFIGURATION --
Select 'link with favicon' under the display settings for a link field

Automatic Nodetitle Module
------------------------
by Wolfgang Ziegler, nuppla@zites.net


Description
-----------
This is a small and efficent module that allows hiding of the content title field in the form.
To prevent empty content title fields it sets the title to the content type name or to an
configurable string. It is possible to use various content data for the autogenerated title,
e.g. the token [current-user:name] is going to be replaced with the currently logged in
users name. If the token module is installed, a list of possible replacement patterns
will be shown.

Advanced users can also provide some PHP code, that is used for automatically generating an
appropriate title.

Installation 
------------
 * (optional) Download and install the token module in order to get token
   replacement help.
 * Copy the module's directory to your modules directory and activate the module.
 * For each content type you want to have an automatic title, configure the
   module at 'admin/structure/types'.


Note
-----
 Due to the way the module works, it is not possible to make use of some replacement
 tokens that are not available before the content node is saved the first time, e.g.
 like the node id ([node:nid]).

 

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

 So if the text of the number field [field_testnumber] isn't empty it will be used as title.
 Otherwise the node type will be used.
 
 
 Updating nodetitles from existing nodes
 ---------------------------------------
 If you set the nodetitle to be auto generated for some content type, existing nodes
 are not affected. You can update existing nodes by going to 'admin/content',
 then filter for your content type, mark some nodes and choose the "Update option" 
 "Update automatic nodetitles". 
 
 Features Override (Drupal 7-2.x)
--------------------------------

This module add a new Features exportable called "Feature Overrides" that 
are used to export overridden changes to other Features.  It requires at
least the 7.x-1.0-rc1 release of Features.

To use, install this module and enable it.  When you create a new feature from 
the Structure/Features page, two new exportables called "Feature Overrides" 
will be displayed in the drop-down list.  The first one allows you to override
all of the changes of a specific component.  The second "Individual Advanced"
allows you to select exactly which line-by-line changes are exported.
Select the Overrode exportable and then select which components you wish to 
export  overrides for.  Only components that are currently overridden will be 
shown as checkboxes.

Maintainers
-----------
- mpotter (Mike Potter)


Basic Usage
-----------
1) Create normal features and enable them.  

2) Make changes to the site using the normal Drupal UI.

3) Go to the admin/structure/features page and you should see some of your 
Features marked as "Overridden"

4) Click the "Create Feature" tab.

5) Enter a name for your Override feature.  

6) Click the "Edit components" drop-down and select "Feature Overrides".  
A list of overridden components will be shown.  For example, if you changed a 
field in a content type, that field name will be shown in the list of 
overrides.  If you changed something in a view, that view name will be in the 
list.  Check the boxes next to the overrides you wish to save.

7) Click the "Download Feature" button at the bottom of the screen.  This will 
create your Override Feature module code and save it to a local file.  Upload 
that file to your server and place it into your normal sites/all/modules 
directory.

8) Go to the Modules page and Enable your new override module.

9) Clear the Drupal cache.

10) Now when you visit the admin/structure/features you should see your new 
override feature and the original features should no longer be marked as 
"Overridden".


Merging new changes into an existing Override
---------------------------------------------
Once you have created an Override feature, it's easy to add additional changes 
to it:

1) Make changes to the site via the Drupal UI

2) Visit admin/structure/features and you should see both the original code 
feature marked as "Overridden" as well as the Override feature marked as 
"Overridden"

3) Click the Recreate link for the Override feature.  

4) Select any new overrides from the Component dropdown list as needed.  
Download your new feature.

You can accomplish this same task using Drush:

drush features-update override-feature

5) Now visit the Features admin page and nothing should be marked as Overridden
again.

NOTE: You want to update/recreate the Override feature and NOT the original 
feature.  If you recreate the original feature, then ALL of the overrides (the
existing ones in the Override module and the new changes) will be written to 
the original feature.  Probably not what you wanted (see next section)

Rebuilding the Original Feature without the Overrides
-----------------------------------------------------
Sometimes you want to make a change and have that change saved with the 
original feature and not with the Override.  Here are the steps to accomplish 
this:

1) Make the changes you need to the site via the Drupal UI

2) Visit admin/structure/features and you should see both the original code 
feature marked as "Overridden" as well as the Override feature marked as 
"Overridden"

3) Click the "Create Feature" tab to create a new feature

4) Create a new Override feature by entering a name and description, then 
select the overrides you want to save from the Feature Override section of the
Components drop-down menu

5) Click Download Feature and install this new module on your site.  Let's 
call it "New Changes".  So now we have the "Original Feature", the first 
"Override Feature", and the new "New Changes" feature.  All three should 
display in the Features Admin page in their Default state.

6) From the Features Admin page, uncheck the "New Changes" feature you created
in step 5, then click Save.  This will undo the recent changes.

7) From the Features Admin page, uncheck the box next to the "Override Feature"
that you originally created (NOT the New one you made in step 5) and click 
Save.  This will undo the changes made by the first Override module.

8) If the original feature shows as "Overridden" or "Needs Review", click on 
it and click the Revert button to ensure it is in it's original state.

9) From the Features Admin page, check the box next to the "New Changes" 
feature you created in step 5 to enable is and click Save.  Now the database 
reflects the original feature plus the new changes.

10) Click the Recreate link for the original Feature.  Click the Download link
and install the updated feature.  Or use the drush command: 
"drush features-update original-feature".  This will export the original
feature code along with the New Changes code.

11) You no longer need the New Changes feature.  You can disable it and remove
it from your site if you wish.  If you don't remove it completely, at least 
ensure that it is disabled in the Feature Admin page.

12) Finally, check the box next to the Override feature to re-enable that 
feature.  Now you have the original code plus the New changes stored in the 
original feature, but you still have the additional Overrides in the seperate 
Override module.

Once you understand the above steps you will also realize that there are other
ways to accomplish this same task.  For example, you could have disabled the 
Override module first, then made your changes and just recreated the original 
feature directly.  However, the above procedure is the most complete and 
reflects the real-life situation where the changes have already been made to 
the site and you need to somehow capture those changes back into the original 
feature.

Adding or Removing specific Override lines
------------------------------------------
An Override feature is simply a list of code changes that need to be made to 
the current configuration. Only code *differences* are stored in the Override 
feature.

To view these specific line-by-line code differences, click the Default link 
next to your Override module from the Features admin page, then click the  
Review Overrides tab.  This will show the Overrides currently exported as 
individual lines (along with the normal "diff" listing below).

To change which specific lines are exported, click the Recreate tab, then
open the Components dropdown.  Select the "Features Overrides Individual" 
(advanced) tab.  Then click the "Refine" link next to the component you want
to adjust.  Each specific override line will be shown as a checkbox.  Simply
check or uncheck the lines desired.  Then click the Download button to create
a new version of your Override feature.

In the main Features Admin page there is also a new Review Overrides tab.  
This will show a list of any new overrides no matter which module that relate 
to.  This is a very useful debugging tool for determining where changes have 
been made to your site.  The Overrides tab will tell you the exact Component 
being overridden. The normal "Review Overrides" tab in Features only shows the 
raw code "diffs" and sometimes cannot show the full context of the change.  The 
new Review Overrides tab can show you exactly what the change is and where it 
is made (which View changed, which field changed, etc).
Drupal-to-Drupal migration
==========================

This is a framework based on the Migrate API to ease building migrations
from one Drupal site to another. It is only supported at this time on Drupal 7
(i.e., Drupal 7 is the only destination). Besides addressing contemporary needs
to migrate to Drupal 7, it is intended to help serve as a proof-of-concept for
incorporating the migration approach into core as an upgrade path
(http://drupal.org/node/1052692).

migrate_d2d
===========

The core framework provided here is used by providing your own module, which
will register instances of the migrate_d2d classes (or derivations of them).
See migrate_d2d_example for one approach, where instances are registered when
the Drupal caches are cleared (note that registration updates previously-
registered classes with any argument changes).
CKEDITOR LINK - A PLUGIN TO EASILY CREATE LINKS TO DRUPAL INTERNAL PATHS
http://drupal.org/project/ckeditor_link



REQUIREMENTS
The CKEditor module or the Wysiwyg module
The CKEditor editor
Clean URLs need to be enabled.



INSTALLATION
Copy the ckeditor_link folder to your sites/all/modules directory.
Go to admin/modules and enable the module.

*Set permissions*
Go to admin/people/permissions and grant the CKEditor Link related permissions
to the desired roles.

*When using the CKEditor module*
Go to admin/config/content/ckeditor and edit the desired profile.
Under "Editor appearance" > "Plugins", check the "CKEditor Link" box.
Save changes.

*When using the Wysiwyg module*
Go to admin/config/content/wysiwyg and edit the desired CKEditor-enabled input
format.
Under "Buttons and plugins", check both "Link" and "CKEditor Link" boxes.
Save changes.

*Set up CKEditor Link Filter*
Go to admin/config/content/formats and edit the desired text format.
Check the "CKEditor Link Filter" box.
If you use other path converting filters like Pathologic or Path Filter, make
sure that CKEditor Link Filter comes before them:
Under "Filter processing order", drag and drop CKEditor Link Filter before
these filters in the list.
Save changes.

*Configure CKEditor Link*
Go to admin/config/content/ckeditor_link.
Change settings as desired.
Save changes.



EXTENDING CKEDITOR LINK
Developers, see the ckeditor_link.api.php file.



CONTACT
Henri MEDOT <henri.medot[AT]absyx[DOT]fr>
http://www.absyx.fr
Countries module - http://drupal.org/project/countries
======================================================

DESCRIPTION
------------
This module provides country related tasks. It replaces the Countries API and
CCK Country modules from Drupal 6.

The region data parts can be obtained using one of

Location Taxonomize: http://drupal.org/project/location_taxonomize
Countries regions (Sandbox project): http://drupal.org/sandbox/aland/1311114

Features include:
 * A countries database with an administrative interface.
 * To alter Drupals core country list.
 * A countries field.
 * Ability to add any additional Fields to a country.
 * Integration with Views, Token, Apache solr search and Feeds modules.
 * Numerous methods to handle and filter the data.
 * A country FAPI element.

Countries 7.x-2.x only
 * Entity API integration.
 * A countries field with continent filter.
 * New continent and continent code formatters
 * Integration with CountryIcons v2 with more features for less loc.

New hooks for listening to country changes.
* hook_country_insert()
* hook_country_update()
* hook_country_delete()

REQUIREMENTS
------------
Drupal 7.x

For Countries 7.x-2.x and above

 * Entity API
   http://drupal.org/project/entity

INSTALLATION
------------
1.  Place both the Entity API and Countries modules into your modules directory.
    This is normally the "sites/all/modules" directory.

2.  Go to admin/build/modules. Enable both modules.
    The Countries modules is found in the Fields section.

Read more about installing modules at http://drupal.org/node/70151

3.  Updating the core list
    The module does not override the standard name that is defined by the core
    Drupal country list during installation. If you want to bulk update all
    standard names to those of ISO 3166-1, visit the bulk update page and select
    the countries to update. Selecting all updates should bring the database in
    sync with the ISO standard.
    
    The bulk update page is found here:
    http://www.example.com/admin/config/regional/countries/import

UPGRADING
---------
Any updates should be automatic. Just remember to run update.php!

To reset your countries database with the ISO defined countries list, visit
http://www.example.com/admin/config/regional/countries/import to manually
select which country properties to update.

FEATURES
--------

1 - Countries database

This is a simple table based on the ISO 3166-1 alpha-2 codes [1]. It covers the
countries standard name, official name, ISO 3166-1 alpha-3 code, UN numeric code
(ISO 3166-1 numeric-3) and continent (Africa, Antarctica, Asia, Europe, North
America, Oceania, South America). An enabled flag defines a countries status.
 
For example, Taiwan has the following values:

 * Name           - Taiwan
 * Official name   - Taiwan, Republic of China
 * ISO alpha-2    - TW
 * ISO alpha-3    - TWN
 * ISO numeric-3  - 158
 * Continent      - Asia
 * Enabled        - Yes

The official names were originally taken from WikiPedia [2] and the majority of
the continent information was imported from Country codes API project [3]. This
have been since standardized with the ISO 3166-1 standard. 

Country updates are added when the ISO officially releases these. This process
may be up to 2 - 6 months. South Sudan's inclusion took around a month. Kosovo
is taking many months, but this should be added in the near future as Kosovo is
a member both the IMF and World Bank.

Please report any omissions / errors.

2 - Alter Drupals core country list

The module implement hook_countries_alter() which updates any list generated
using country_get_list() to filter out any disabled countries and adds the
potential to rename these based on your personal or political preferences.

To avoid potential clashes with future modifications to the ISO list, use one of
the following user-assigned codes:

Alpha-2: AA, QM to QZ, XA to XZ, and ZZ

Optionally add other codes:

Alpha-3: AAA to AAZ, QMA to QZZ, XAA to XZZ, and ZZA to ZZZ
Numeric codes: There are no reserved numeric codes in the ISO 3166-1 standard.

See http://en.wikipedia.org/wiki/ISO_3166-1 for more details

Example one: Disable the UK and enable England, Scotland, Wales, Nth Ireland.

The UK (United Kingdom) is a sovereign state that consists of the following
countries England, Scotland, Wales and Northern Ireland. 

a) Disable United Kingdom

Go to admin/config/regional/countries and find and edit the UK.

b) Add the other countries

Go to admin/config/regional/countries/add and add the four countries

Name: England / ISO Alpha-2 Code: XA / Continent: Europe
- Optionally add others: ISO Alpha-3 Code: XAA, etc
Name: Scotland / ISO Alpha-2 Code: XB / Continent: Europe
- Optionally add others: ISO Alpha-3 Code: XBA, etc
Name: Wales / ISO Alpha-2 Code: XC / Continent: Europe
- Optionally add others: ISO Alpha-3 Code: XCA, etc
Name: Northern Ireland / ISO Alpha-2 Code: XD / Continent: Europe
- Optionally add others: ISO Alpha-3 Code: XDA, etc

All default lists will hide the UK and show the other countries.

Example two: Custom lists with England, Scotland, Wales, Nth Ireland but no UK.

For example, you wanted to add a list of countries playing Rugby Union but to
leave the other country lists as per the ISO standard.

Do not disable the UK, rather add the other states as per example one, this time
leave all Disabled.

Create a new field and select what countries should be present. Ensure that the
Country status is set to both, selecting all countries that play Rugby Union and
make sure you exclude the UK.

## Developers note: ##

There is no need to make this module a dependency unless you use the API or
Field element. See the countries_example module for examples.

3 - A country FAPI element

After programming yet another select list with a country drop down, I
encapsulated the logic into a simple FAPI element. By default it uses
country_get_list(), so filters based on the countries status.

Custom filters are available to bypass the default country_get_list(), to filter
based on status and continent.

--------------------------------------------------------------------------------
<?php
  $element = array(
    '#type' => 'country',
    '#default_value' => 'AU',
    '#multiple' => TRUE, // multiple select
    '#cardinality' => 4, // max. selection allowed is 4 values
    '#filters' => array(
      // enabled options should be one of these constants:
      // COUNTRIES_ALL, COUNTRIES_ENABLED, or COUNTRIES_DISABLED
      'enabled' => COUNTRIES_ENABLED,
      // The restrict by continent filter accepts an array of continent codes.
      // The default continents that are defined are [code - name]:
      // AF - Africa, AN - Antarctica, AS - Asia, EU - Europe,
      // NA - North America, OC - Oceania, SA - South America, UN - Unknown
      'continents' => array('EU', 'OC'),
    ),
  );
?>
--------------------------------------------------------------------------------

For Countries 7.x-2.x and latter, we recommend using a select element instead.

However, there are no plans to drop this, especially now with the new continents
country widget that uses it (it is easier and cleaner).

--------------------------------------------------------------------------------
<?php
  $element = array(
    '#type' => 'select',
    '#title' => t('Country'),
    '#default_value' => 'AU',
    '#options' => countries_get_countries('name', array('enabled' => COUNTRIES_ENABLED)),
  );

  $filters = array(
    // enabled options should be one of these constants:
    // COUNTRIES_ALL, COUNTRIES_ENABLED, or COUNTRIES_DISABLED
    'enabled' => COUNTRIES_ENABLED,
    // The restrict by continent filter accepts an array of continent codes.
    // The default continents that are defined are [code - name]:
    // AF - Africa, AN - Antarctica, AS - Asia, EU - Europe,
    // NA - North America, OC - Oceania, SA - South America, UN - Unknown
    'continents' => array('EU', 'OC'),
    // If you want a very granular control of the available countries.
    'countries' => array('AU', 'CA', 'CN', 'MX', 'NZ', 'US'),
  );
  $element = array(
    '#type' => 'select',
    '#title' => t('Country'),
    '#default_value' => 'AU',
    '#options' => countries_get_countries('name', $filters),
    '#multiple' => TRUE, // multiple select
    '#size' => 6,
  );
?>
--------------------------------------------------------------------------------

4 - A country field

Provides a standard field called "Country", with a widget "Country select list".
This expands the core Drupal Options list provide the functionality of either
a select list, radios or checkboxes.

The default display options are:

Default (The country name)
Official name
ISO alpha-2 code
ISO alpha-3 code
ISO numeric-3 code
Continent
Continent code

HOWTO / FAQ
-----------

1 - Revert the database to the original values.

To reset your countries database with the ISO defined countries list, visit
http://www.example.com/admin/config/regional/countries/import to manually
select which countries to update. Replace www.example.com with your sites URL.

2 - Change the continent list.

These are generated using a variable_get() like this:

--------------------------------------------------------------------------------
<?php
  $continents = variable_get('countries_continents',
      countries_get_default_continents());
?>
--------------------------------------------------------------------------------

To update these, you need to set the system variable 'countries_continents'. The
easiest way to do this is to cut and paste the following into your themes
template.php, changing the array values to suit your requirements. Load one page
on your site that uses the theme, then delete the code.

--------------------------------------------------------------------------------
<?php
  variable_set('countries_continents', array(
    'AF' => t('Africa'),
    'EA' => t('Asia & Europe'),
    'AM' => t('America'),
    'OC' => t('Oceania'),
    'AN' => t('Antarctica'),
    'UN' => t('Unknown'),
  ));
?>
--------------------------------------------------------------------------------

Any invalid continent keys that are found are converted to t('Unknown'), so
update all respective countries before deleting any existing values.

For I18n sites, to ensure that the new continents are translated correctly, use
codes from the following list.

* Default
  'AF' => t('Africa'),
  'AS' => t('Asia'),
  'EU' => t('Europe'),
  'NA' => t('North America'),
  'SA' => t('South America'),
  'OC' => t('Oceania'),
  'AN' => t('Antarctica'),
  'UN' => t('Unknown', array(), array('context' => 'countries')),

* Additionally defined  
  'AE' => t('Afro-Eurasia'),
  'AM' => t('Americas'),
  'AU' => t('Australasia'),
  'CA' => t('Caribbean'),
  'CE' => t('Continental Europe'),
  'ER' => t('Eurasia'),
  'IC' => t('Indian subcontinent'),

If you need another continent listed, please lodge an issue and we will consider
it for inclusion.

3 - Hiding columns in the administrative country overview page.

Like the continents, these are dynamically generated from the system variables.
They can also be changed in a similar variable_set, like 'countries_continents'.

The name, ISO alpha-2 and enabled columns can not be removed.

--------------------------------------------------------------------------------
<?php
  // Remove the columns that you want to hide.
  variable_set('countries_admin_overview_columns', array(
    'iso3' => t('ISO3'),
    'numcode' => t('Number code'),
    'continent' => t('Continent'),
    'official_name' => t('Official name'),
  ));
?>
--------------------------------------------------------------------------------

4 - I18n support (Countries 7.x-2.x only)

This is in the early implementation stages using the Entity API integration.

5 - Why is the delete link hidden on some countries?
  - Why is the edit ISO alpha-2 code disabled on some countries?

These are the countries that Drupal defines. To disable a country in the list of
countries that Drupal generates, these must be present in the database. Also
done to ensure that existing references to these countries still exist, even if
you can no longer select them when they are disabled.

6 - How does this differ from countries_api?

The countries_api is a just that, an API locked into a back-end country and
regions database that has no configurable options. It main purpose is converting
country code data from one format to another.

From the Country codes API modules project page:

    "Typical usage would be converting a country name to its ISO2
    (or ISO3) country code."

The Countries module is based on the philosophy that only the ISO2 code can be
trusted. All other data can be modified by the sites administrator, and the ISO2
is the primary key. Then the most common country requirements are built on top
of this base, providing the input elements, etc.

Function                           Drupal 6                Drupal 7
Provide a list of countries        Countries API           Drupal
Update the countries list          N/A                     Countries
Provide a field element            CCK Country             Countries
Country getter API                 Countries API           Countries


Here is an approximate mapping of the Country API functions in the Countries
module. Note that the Country API module generally returns an array, while the
Countries module returns an object.

Countries API module
--------------------------------------------------------------------------------
<?php

# 1 - All countries (an array of country arrays)
$countries = countries_api_get_list();

# 2 - Load a country (an array)
$country = countries_api_get_country($iso2_or_iso3);
$country = countries_api_iso2_get_country($iso2);
$country = countries_api_iso3_get_country($iso3);
$country = _countries_api_iso_get_country($property, $value);

# 3 - Get a countries name
$name = countries_api_get_name($iso2_or_iso3);
$name = countries_api_iso2_get_name($iso2);
$name = countries_api_iso3_get_name($iso3);

# 4 - Toggle between ISO character codes
$iso3 = countries_api_iso2_get_iso3($iso2);
$iso2 = countries_api_iso3_get_iso2($code);

# 5 - Option lists
$list = countries_api_get_array($list_key_property, $list_option_property);
$standard_list = countries_api_get_options_array();
?>
--------------------------------------------------------------------------------

Countries module
--------------------------------------------------------------------------------
<?php
# 1 - All countries (an array of country objects)
$countries = countries_get_countries();

# 2 - Load a country (an object)
$country = country_load($iso2);
$country = countries_country_lookup($value);
$country = countries_country_lookup($value, $property);

# 3 - Get a countries name

// The recommended method for an existing country using ISO 2 code
$name = country_load($iso2)->name;

// If the ISO 2 code can not be trusted:
$name = ($country = country_load($iso2) ? $country->name : '');

// Any property (iso2, iso3, num code or name) supplied by an end user
$name = $country = countries_country_lookup($value) ? $country->name : '';

# 4 - Toggle between ISO character codes
$iso3 = country_load($iso2)->iso3;
$iso2 = $country = countries_country_lookup($iso3, 'iso3') ? $country->iso2 : '';

# 5 - Option lists
// If keyed by iso2 value.
$list = countries_get_countries($list_option_property);

// Other lists that are keyed differently would need to be generated manually.
$list = array();
foreach (countries_get_countries() as $country) {
  $list[$country->numcode] = $country->name;
}

$standard_list = array('' => t('Please Choose')) + countries_get_countries('name');

# Please note that the following are equivalent.

  // Core Drupal iso2/name listing.
  // Returns a list of countries passed through hook_countries_alter().
  include_once DRUPAL_ROOT . '/includes/locale.inc';
  $list = country_get_list();

  // Countries module.
  // Get a list of enabled countries and then allow other modules to update this
  // list via hook_countries_alter(). This avoids loading 'include/locale.inc'.
  $list = countries_get_countries('name', array('enabled' => COUNTRIES_ENABLED));
  countries_invoke_additional_countries_alter($list);

?>
--------------------------------------------------------------------------------

7 - Related modules (as of early 2010) see http://drupal.org/node/1412962


CHANGE LOG
----------

Countries 7.x-1.x to 7.x-2.x
1) Entity API integration

   This is now an dependency.  

2) countries_get_country() is been depreciated.

   Use country_load() instead.

3) countries_get_countries() will throw an Exception if you attempt to
   use it to lookup an invalid property.

4) CRUD functions have been completely refactored.

AUTHORS
-------
Alan D. - http://drupal.org/user/198838.
Florian Weber (webflo) - http://drupal.org/user/254778.

Thanks to everybody else who have helped test and contribute patches!

REFERENCES
----------
[1] http://www.iso.org/iso/country_codes/iso_3166_code_lists.htm
[2] http://en.wikipedia.org/wiki/List_of_countries
[3] http://drupal.org/project/countries_api
--------------------------
Storypal module for Drupal
--------------------------

Introduction
------------
Drupal & Storify are two amazing products and two very popular technologies.
No module were done to link the two technologies, until now :-)
This module has been done to let you incorporate stories from Storify.com
into your nodes in a really easy way.

How Storypal works
------------------
Storypal is a module who provides two things:
 - a "Storify field"
 - an input filter.

The field:
When the user will fill that field, Drupal will transform the url into HTML
when a user visit the page, yes sir, as simple as that.

The filter
Storypal allows you now to enable a 'Storify' filter for each available
text formats. It means that when you write a text in a node, you can add
Storify tokens like: [storify:StoryUrl].
Those tokens will be replaced with the story as you would see it on
Storify.com.

To work properly, Storypal is using a standard Storify PHP class which
can be used not only in Drupal, but in any PHP project.
I'm planning to improve it a lot and release it as a single project later.
Storypal is not a copycat of the Wordpress module, example, It's using
the Drupal's native cache for each request to lighten the load on
Storify's servers.

The Storypal class extends the Storify class and provides the Drupal's caching
system.
So, when you use the module, you better use Storypal instead of Storify.

Requirements
------------
 - Libraries module
 - Storify PHP library: https://github.com/Polzme/storify

What's next ?
-------------
I have some good ideas for this module before putting it live.

 - Enable contextual links on Story so we can inline edit the Story,
   using the Storify interface in a overlay.
 - ... your idea ?
This is a fork of http://drupal.org/node/1480204

Will try to merge efforts.

The CTools Plugin Example is an example for developers of how to CTools
access, argument, content type, context, and relationship plugins.

There are a number of ways to profit from this:

1. The code itself intends to be as simple and self-explanatory as possible. 
   Nothing fancy is attempted: It's just trying to use the plugin API to show
   how it can be used.
   
2. There is a sample panel. You can access it at /ctools_plugin_example/xxxx
   to see how it works.
   
3. There is Advanced Help at admin/advanced_help/ctools_plugin_example.

INSTALLATION


Simply save this module's subdir in your contrib module directory,
and enable the module.


USAGE


Within the Facet API UI of a specific facet, go to "Dependency" or "Filters" to
add one of this module's plugins. The usage of the specific plugins are well
explained within their settings forms.


MODULE DESCRIPTION


Facet API Bonus for Drupal 7 is a collection of additional Facet API plugins and
functionality, foremost filter and dependency plugins – And a place to collect
more additional Facet API extensions.

Currently Facet API Bonus includes:

* Facet Dependency

  Dependency plugin to make one facet (say "product category")
  to show up depending on other facets or specific facet items being active
  (say "content type" is "product" or "service"). Very flexible,
   supports multiple facets to be dependencies, as well as regexp for specifying
   facet item dependencies, as well as option how to behave if a dependency is
   being lost.

* Filter "Exclude Items"

  Filter plugin to exclude certain facet items by their
  markup/title or internal value (say excluding "page" from "content types").
  Regexp are also possible.

* Filter "Rewrite Items"

  Filter plugin to rewrite labels or other data of the facet items by
  implementing a new dedicated hook_facet_items_alter (in a structured array,
  before rendering). Very handy to rewrite list field values or totally custom
  encoded facet values for user friendly output.

  By enabling this filter, items of this facet can be
  rewritten prior to rendering by implementing the hook:

    function HOOK_facet_items_alter(&$build, &$settings) {
      if ($settings->facet == "YOUR_FACET_NAME") {
        foreach($build as $key => $item) {
          $build[$key]["#markup"] = drupal_strtoupper($item["#markup"]);
        }
      }
    }

  (This example simply rewrites all facet items output to be uppercase.)

  Replace "HOOK" with the name of a custom module containing
  your hook implementation, and "YOUR_FACET_NAME" with the
  machine name of the specific facet whose items you want to
  rewrite.

  $build is an array of facet items you
  can rewrite, $settings contains the facet filter settings
  as context to determine the facet and search context.

* Filter "Do not display items that do not narrow results"

  This filter checks the number of items that will be displayed after activating
  facet link and removes the link if the number is the same as currently
  displayed. If link has children in hierarchical structure, it won't be removed.

* Filter "Do not show facet with only X items"

  This filter checks total number of links and if number is less than X, we
  remove all items and hide block completely. Block will not be hidden if there
  any active items in it.

* Filter "Show only deepest level items"

  Removes all items that have children.


* Integration with Page Title module

  Now you can set search (views) page titles using Page Title module. Module
  provides possibility to set tokens 'facetapi_results' and 'facetapi_active'
  groups. So in title we can display number of results on the page or values of
  active facets. As there can be multiple active facet values please use following
  pattern to use facetapi_active tokens:

  list<[facetapi_active:facet-label]: [facetapi_active:active-value]>

  This will make coma separated list of active facet labels and their values.


* Current search block Reset Filters link

  Gives possibility to add link to current block that resets all applied facets.
  Text is customizable.

===> Further additions are very welcome! <===

Facet API Bonus is written for Drupal 7, and is stable, tested,
and ready to be used in production environments.

Requirements:

* Facet API is obviously required, as well as
  a compatible search module (e.g. apachesolr, search_api).

Similar projects:

* http://drupal.org/project/facetapi_extra Module has been deprecated in favour
  of facetapi_bonus module. All features have been merged.


MODULE URL


More information and issues, see the module page, currently at:

  http://drupal.org/project/facetapi_bonus

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

[![Build Status](https://travis-ci.org/RESTful-Drupal/restful.svg?branch=7.x-2.x)](https://travis-ci.org/RESTful-Drupal/restful)

# RESTful best practices for Drupal

This module allows Drupal to be operated via RESTful HTTP requests, using best
practices for security, performance, and usability.

## Concept
Here are the differences between RESTful and other modules, such as RestWs and
Services Entity:

* RESTful requires explicitly declaring the exposed API. When enabling
the module, nothing happens until a plugin declares it.
* Resources are exposed by bundle, rather than by entity.  This would allow a
developer to expose only nodes of a certain type, for example.
* The exposed properties need to be explicitly declared. This allows a _clean_
output without Drupal's internal implementation leaking out. This means the
consuming client doesn't need to know if an entity is a node or a term, nor will
 they be presented with the ``field_`` prefix.
* Resource versioning is built-in, so that resources can be reused with multiple
consumers.  The versions are at the resource level, for more flexibility and
control.
* It has configurable output formats. It ships with JSON (the default one), JSON+HAL and as an example also XML.
* Audience is developers and not site builders.
* Provide a key tool for a headless Drupal. See the [AngularJs form](https://github.com/Gizra/restful/blob/7.x-1.x/modules/restful_angular_example/README.md) example module.


## Module dependencies

  * [Entity API](https://drupal.org/project/entity), with the following patches:
  * [Prevent notice in entity_metadata_no_hook_node_access() when node is not saved](https://drupal.org/node/2086225#comment-8768373)

## Recipes
Read even more examples on how to use the RESTful module in the [module documentation
node](https://www.drupal.org/node/2380679) in Drupal.org. Make sure you read the _Recipes_
section. If you have any to share, feel free to add your own recipes.

## Declaring a REST Endpoint

A RESTful endpoint is declared via a custom module that includes a plugin which
describes the resource you want to make available.  Here are the bare
essentials from one of the multiple examples in
[the example module](./modules/restful_example):

####restful\_custom/restful\_custom.info
```ini
name = RESTful custom
description = Custom RESTful resource.
core = 7.x
dependencies[] = restful

registry_autoload[] = PSR-4
```

####restful\_custom/src/Plugin/resource/Custom__1_0.php
```php

namespace Drupal\restful_custom\Plugin\resource;

/**
 * Class Custom__1_0
 * @package Drupal\restful_custom\Plugin\resource
 *
 * @Resource(
 *   name = "custom:1.0",
 *   resource = "custom",
 *   label = "Custom",
 *   description = "My custom resource!",
 *   authenticationTypes = TRUE,
 *   authenticationOptional = TRUE,
 *   dataProvider = {
 *     "entityType": "node",
 *     "bundles": {
 *       "article"
 *     },
 *   },
 *   majorVersion = 1,
 *   minorVersion = 0
 * )
 */
class Custom__1_0 extends ResourceEntity implements ResourceInterface {

  /**
   * Overrides EntityNode::publicFields().
   */
  public function publicFields() {
    $public_fields = parent::publicFields();

    $public_fields['body'] = array(
      'property' => 'body',
      'sub_property' => 'value',
    );

    return $public_fields;
  }
}
```

After declaring this plugin, the resource could be accessed at its root URL,
which would be `http://example.com/api/v1.0/custom`.

### Security, caching, output, and customization

See the [Defining a RESTful Plugin](./docs/plugin.md) document for more details.


## Using your API from within Drupal

The following examples use the _articles_ resource from the _restful\_example_
module.

#### Getting a specific version of a RESTful handler for a resource

```php
// Get handler v1.1
$handler = restful()->getResourceManager()->getPlugin('articles:1.1');
```

#### Create and update an entity
```php
$handler = restful()
  ->getResourceManager()
  ->getPlugin('articles:1.0');
// POST method, to create.
$result = restful()
  ->getFormatterManager()
  ->format($handler->doPost(array('label' => 'example title')));
$id = $result['id'];

// PATCH method to update only the title.
$request['label'] = 'new title';
restful()
  ->getFormatterManager()
  ->format($handler->doPatch($id, $request));
```

#### List entities
```php
$handler = restful()->getResourceManager()->getPlugin('articles:1.0');
$handler->setRequest(Request::create(''));
$result = restful()->getFormatterManager()->format($handler->process(), 'json');

// Output:
array(
  'data' => array(
    array(
      'id' => 1,
      'label' => 'example title',
      'self' => 'https://example.com/node/1',
    );
    array(
      'id' => 2,
      'label' => 'another title',
      'self' => 'https://example.com/node/2',
    );
  ),
);
```

### Sort, Filter, Range, and Sub Requests
See the [Using your API within drupal](./docs/api_drupal.md) documentation for
more details.

## Consuming your API
The following examples use the _articles_ resource from the _restful\_example_
module.

#### Consuming specific versions of your API
```shell
# Handler v1.0
curl https://example.com/api/articles/1 \
  -H "X-API-Version: v1.0"
# or
curl https://example.com/api/v1.0/articles/1

# Handler v1.1
curl https://example.com/api/articles/1 \
  -H "X-API-Version: v1.1"
# or
curl https://example.com/api/v1.1/articles/1
```


#### View multiple articles at once
```shell
# Handler v1.1
curl https://example.com/api/articles/1,2 \
  -H "X-API-Version: v1.1"
```


#### Returning autocomplete results
```shell
curl https://example.com/api/articles?autocomplete[string]=mystring
```


#### URL Query strings, HTTP headers, and HTTP requests
See the [Consuming Your API](./docs/api_url.md) document for more details.

## CORS
RESTful provides support for preflight requests (see the
[Wikipedia example](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing#Preflight_example)
for more details).

To configure the allowed domains, you can:

  - Go to `admin/config/services/restful` and set _CORS Preflight_ to the
allowed domain. This will apply globally unless overridden with the method
below.
  - Set the `allowOrigin` key in your resource definition (in the annotation)
to the allowed domain. This setting will only apply to this resource.

Bear in mind that this check is only performed to the top-level resource.
If you are composing resources with competing `allowOrigin` settings, the
top-level resource will be applied.

## Documenting your API
Clients can access documentation about a resource by making an `OPTIONS` HTTP
request to its root URL. The resource will respond with the field information
in the body, and the information about the available output formats and the
permitted HTTP methods will be contained in the headers.


### Automatic documentation
If your resource is an entity, then it will be partially self-documented,
without you needing to do anything else. This information is automatically
derived from the Entity API and Field API.

Here is a snippet from a typical JSON response using only the automatic
documentation:

```json
{
  "myfield": {
    "info": {
      "label": "My Field",
      "description": "A field within my resource."
    },
    "data": {
      "type": "string",
      "read_only": false,
      "cardinality": 1,
      "required": false
    },
    "form_element": {
      "type": "textfield",
      "default_value": "",
      "placeholder": "",
      "size": 255,
      "allowed_values": null
    }
  }
  // { ... other fields would follow ... }
}
```

Each field you've defined in `publicFields` will output an object similar
to the one listed above.


### Manual documentation
In addition to the automatic documentation provided to you out of the box, you
have the ability to manually document your resources.  See the [Documenting your API](./docs/documentation.md)
documentation for more details.


## Modules integration
* [Entity validator 2.x](https://www.drupal.org/project/entity_validator): Integrate
with a robust entity validation (RESTful 1.x requires Entity Validator 1.x).


## Credits
* [Gizra](http://gizra.com)
* [Mateu Aguiló Bosch](https://github.com/e0ipso)
About CKEditor for Drupal
-------------------------
This module allows Drupal to replace textarea fields with CKEditor.
CKEditor is an online rich text editor that can be embedded inside web pages.
It is a WYSIWYG (What You See Is What You Get) editor which means that the
text edited in it looks as similar as possible to the results end users will
see after the document gets published. It brings to the Web popular editing
features found in desktop word processors such as Microsoft Word and
OpenOffice.org Writer. CKEditor is truly lightweight and does not require any
kind of installation on the client computer.

Help & Documentation
--------------------
If you are looking for more information, have any trouble with the configuration of the module
or found an issue, please visit the official project page:
  http://drupal.org/project/ckeditor

Extensive CKEditor for Drupal documentation is available at:
  http://docs.cksource.com/CKEditor_for_Drupal/Open_Source/Drupal_7

Contribution
------------
If you would like to help in the development of the module, we encourage you to join our team.
Any help will be greatly appreciated!

Module Information and License
----------------------------
CKEditor - The text editor for the Internet
Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
http://cksource.com/

Licensed under the terms of the GNU Lesser General Public License:
    http://www.opensource.org/licenses/lgpl-license.php

For further information visit:
    http://ckeditor.com/RDF is a W3C standard for modeling and sharing distributed knowledge based on a
decentralized open-world assumption. This RDF Extensions (RDFx) package for
Drupal 7 includes several modules to enhance the RDF and RDFa functionality
which are part of Drupal 7 core.

This project includes the following modules:

* RDFx: extends core RDF support by providing extra APIs and additional
  serialization formats such as RDF/XML, NTriples, Turtle... (requires the
  RESTful Web Services module). Browse to node/1.rdf or node/1.nt to export RDF.
* RDF UI: allows site administrators to manage the RDF mappings of their site:
  alter default core mappings or specify mappings for the new content types and
  fields they create.
* Evoc: enables the import of RDF vocabularies (such as FOAF, SIOC, etc.) which
  the site administrator can use to map Drupal data to RDF.


== Dependencies ==

This project requires the Entity API module:
http://drupal.org/project/entity


== Related projects ==

Download the following modules to avail more RDF features:

* RESTful Web Services module for RDF serializations
  http://drupal.org/project/restws

* The site RDF data can be made available in a SPARQL endpoint with the
  SPARQL module.
  http://drupal.org/project/sparql


== Install the RDF Extensions (RDFx) module ==

  1. Copy all the module files into a subdirectory called
     sites/all/modules/rdfx/ under your Drupal installation directory.

  2. Go to Administer >> Site building >> Modules and enable the RDFx module and
     any other module you would like. You will find them in the "RDF" section.

  3. Install the ARC2 library following one of these 2 options:
       - run "drush rdf-download" (recommended, it will download the right
         package and extract it at the right place for you.)
       - manual install: requires the libraries API module:
         http://drupal.org/project/libraries
         Download the ARC2 library from
         http://github.com/semsol/arc2/tarball/master and extract it in the
         libraries directory such that you end up with the following file
         structure: sites/all/libraries/ARC2/arc/ARC2.php

== Bug reports ==

Post bug reports and feature requests to the issue tracking system at:
<http://drupal.org/node/add/project_issue/rdf>


== Credits ==
The original RDF module was written for Drupal 6 by Arto Bendiken. It has been
refactored for Drupal 7 by Stéphane Corlosquet, Lin Clark and Richard Cyganiak,
based on the RDF CCK and Evoc modules, which are now part of the main RDF
package for Drupal 7.


== Current maintainers ==
  Stéphane "scor" Corlosquet - <http://openspring.net/>
  Lin Clark - <http://lin-clark.com/>

Current state of Context for Drupal 7
-------------------------------------
Context for D7 is a straight port of Context 3.x from D6. There are no major
API changes and any exported contexts from D6 should be compatible with the D7
version. You will need the latest CTools (as of Sept. 16 2010) from here:

- http://github.com/sdboyer/ctools

### Working

- all conditions except node taxonomy condition
- all reactions
- context UI
- context layouts
- inline editor (see the context_ui README file for info on enabling)

### Expect API changes

- node taxonomy condition to generic field condition for entities


Context 3.x for Drupal 7.x
--------------------------
Context allows you to manage contextual conditions and reactions for
different portions of your site. You can think of each context as
representing a "section" of your site. For each context, you can choose
the conditions that trigger this context to be active and choose different
aspects of Drupal that should react to this active context.

Think of conditions as a set of rules that are checked during page load
to see what context is active. Any reactions that are associated with
active contexts are then fired.


Installation
------------
Context can be installed like any other Drupal module -- place it in
the modules directory for your site and enable it (and its requirement,
CTools) on the `admin/modules` page.

You will probably also want to install Context UI which provides a way for
you to edit contexts through the Drupal admin interface.


Example
-------
You want to create a "pressroom" section of your site. You have a press
room view that displays press release nodes, but you also want to tie
a book with media resources tightly to this section. You would also
like a contact block you've made to appear whenever a user is in the
pressroom section.

1. Add a new context on admin/structure/context
2. Under "Conditions", associate the pressroom nodetype, the pressroom view,
   and the media kit book with the context.
3. Under "Reactions > Menu", choose the pressroom menu item to be set active.
4. Under "Reactions > Blocks", add the contact block to a region.
5. Save the context.

For a more in-depth overview of the UI components, see the Context UI
`README.txt`.


Hooks
-----
See `context.api.php` for the hooks made available by context and `API.txt` for
usage examples.


Maintainers
-----------

- yhahn (Young Hahn)
- jmiccolis (Jeff Miccolis)
- Steven Jones


Contributors
------------

- alex_b (Alex Barth)
- dmitrig01 (Dmitri Gaskin)
- Pasqualle (Csuthy Bálint)

Context layouts
---------------
Context layouts provides a formalized way for themes to declare and switch
between page templates using Context. It is a continuation of an old Drupal
themer's trick to switch to something besides the standard `page.tpl.php` file
for a variety of special-case pages like the site frontpage, login page, admin
section, etc.


Requirements
------------
In order to use context layouts, your site must meet a few conditions:

- Context and Context layouts modules are enabled (`admin/modules`).
- You are using a theme which provides and has declared multiple layouts. (See
  "Example themes" for themes you can try.)


Basic usage
-----------
Once you have layouts enabled, you can have a context trigger the usage of a
particular layout in either the admin interface (`admin/structure/context`) or
inline context editor. Different layouts may have fewer or greater regions than
the default page template, so adjust your blocks accordingly.


Supporting context layouts in your theme
----------------------------------------
You can add layouts support to your theme by declaring additional layouts in
your theme's info file. Here is an example:

`example.info`

    name = "Example"
    description = "Example theme"
    core = "6.x"
    engine = "phptemplate"

    regions[left] = "Left sidebar"
    regions[right] = "Right sidebar"
    regions[content] = "Content"
    regions[footer] = "Footer"

    ; Layout: Default
    layouts[default][name] = "Default"
    layouts[default][description] = "Simple two column page."
    layouts[default][template] = "page"
    layouts[default][regions][] = "content"
    layouts[default][regions][] = "right"

    ; Layout: Columns
    layouts[columns][name] = "3 columns"
    layouts[columns][description] = "Three column page."
    layouts[columns][stylesheet] = "layout-columns.css"
    layouts[columns][template] = "layout-columns"
    layouts[columns][regions][] = "left"
    layouts[columns][regions][] = "content"
    layouts[columns][regions][] = "right"
    layouts[columns][regions][] = "footer"

Each layout is declared under `layouts` with the key as the identifier that will
be used by context for this layout. You may use any reasonable machine name for
each layout, but note that `default` is special -- it will be the default layout
for your theme if no other layout is specified.

The following keys can be declared for each layout:

- `name`: The human readable name for this layout, shown in the admin UI.
- `description`: A short description of your layout, same as above.
- `stylesheet`: A stylesheet to be included with the layout. Optional.
- `template`: The name of the template file for this layout, without the
  `.tpl.php` extension.
- `region`: An array of regions supported by this layout. Note that any of the
  regions listed here **must also be declared** in the standard theme `regions`
  array.


Example themes
--------------
- Cube, a subtheme included with [Rubik][1] provides a variety of layouts.
- [Ginkgo][2] the default theme included with Open Atrium.

[1]: http://github.com/developmentseed/rubik/downloads
[2]: http://github.com/developmentseed/ginkgo/downloads

Context UI
----------
Context UI provides an administrative interface for managing and editing
Contexts. It is not necessary for the proper functioning of contexts once they
are built and can be turned off on most production sites.


Requirements
------------
- Context, Context UI modules enabled (`admin/modules`)


Basic usage
-----------
As a site administrator you can manage your site's contexts at
`admin/structure/context`. The main page will show you a list of the contexts
on the site and give you some options for managing each context.

When editing or adding a new context, you will be presented with a form to
manage some basic information about the context and then alter its conditions
and reactions.

- `name`: The name of your context. This is the main identifier for your context
  and cannot be changed after you've created it.
- `description`: A description or human-readable name for your context. This is
  displayed in the inline editor if available instead of the name.
- `tag`: A category for organizing contexts in the administrative context
  listing. Optional.

**Conditions**

When certain conditions are true, your context will be made active. You can
customize the conditions that trigger the activation of your context.

- **Condition mode**: you can choose to have your context triggered if **ANY**
  conditions are met or only active when **ALL** conditions are met.
- **Adding/removing conditions**: you can add or remove to the conditions on
  your context using the conditions dropdown.
- **Individual settings**: most conditions provide a simple form for selecting
  individual settings for that condition. For example, the node type condition
  allows you to choose which node types activate the context.

**Reactions**

Whenever a particular context is active, all of its reactions will be run.
Like conditions, reactions can be added or removed and have settings that can
be configured.

- **Reaction Block Groupings**: You can influence what "group" a block appears
  in when listing all blocks available to be added to a region.  This is done
  by specifying $block->context_group via hook_block_info.  If no group is
  specified it will default to the module name, but if a group is specified
  it will be grouped under that group name.



Using the inline editor
-----------------------
The inline editor allows you to manage the block reaction for active
contexts within the context of a page rather than through the admin
interface. This can also be helpful when managing block ordering among
multiple contexts.

1. As an administrative user go to `admin/structure/context/settings`.
2. Check the 'Use Context Editor Dialog' block and save. You should also
   check the show all regions box.
3. When viewing a page with one or more active contexts, you will see
   the option to configure layout in the contextual links on all blocks
   on the page. This will allow you to manage the blocks placed by the
   block reaction for contexts.
4. You can use the context editor to adjust the conditions under which each
   context is active and alter its reactions.

You may want to visit the handbook of this module, at:

  http://drupal.org/handbook/modules/flag

The Flag module is a flexible flagging system whose primary goal is
to give all the control to the administrator. Using this module, the
site administrator can provide an arbitrary number of 'flags'.

A flag is really just a boolean toggle that is set on an entity such as a node,
comment, or user. Flags may be per-user, meaning that each user can flag an item
individually, or global, meaning that the item is either flagged or it
is not flagged, and any user who changes that changes it for everyone.

In this way, additional flags (similar to 'published' and 'sticky') can
be put on nodes, or other items, and dealt with by the system however
the administration likes.

Each flag allows the administrator to choose the 'flag this' text, and
the place where the user interface for flagging the item will appear
(For example: for nodes, whether a flagging link appears on the node
teaser as well on the full node view).

Each flag can be restricted to use only by certain roles. Each
flag provides data to the Views module, and provides a default
view to list 'My bookmarks'. These default views are somewhat crude,
but are easily tailored to whatever the system administrator would like
it to do.

Each flag also provides an 'argument' to the Views module that can be
used to allow a user to view other people's flagged content. This isn't
turned on by default anywhere, though, and the administrator will need
to construct a view in order to take advantage of it.

The Flag Bookmark module provides a simple flag called "bookmarks" and
a simple view for 'My bookmarks'. This is a default view provided by the
Flag module, but can be customized to fit the needs of your site. To
customize this view, go to admin/structure/views and find the
'flags_bookmarks' view. Click the 'Add' action to customize the view.
Once saved, the new version of the view will be used rather than the one
provided by Flag.

Besides editing the default view that comes with the module, Flag
provides many views filters, fields, and sort criteria to make all sorts of
displays possible relating to the number of times an item has been flagged.

This module was formerly known as Views Bookmark, which was originally was
written by Earl Miles. Flag was written by Nathan Haug and mystery man Mooffie.

This module built by robots: http://www.lullabot.com

Recommended Modules
-------------------
- Views
- Session API
- Token, which is required for Flag to provide tokens on flagged entities.

Installation
------------
1) Copy the flag directory to the modules folder in your installation.

2) Enable the module using Administer -> Modules (/admin/modules)

Optional Installation
---------------------
1) The ability for anonymous users to flag content is provided by the Session
   API module, available at http://drupal.org/project/session_api.

Configuration
-------------
The configuration for Flag is spread between Views configuration
and the Flag site building page. To configure:

1) Configure the flags for your site at
   Administer -> Structure -> Flags (/admin/structure/flags)

   You can create and edit flags on this page. Descriptions for the various
   options are provided below each field on the flag edit form.

2) Go to the Views building pages at
   Administer -> Site Building -> Views (/admin/structure/views)

   A default view is provided to get you started organizing your flags. You
   can override the view or use it as a template to control the display of your
   flags.

Support
-------
If you experience a problem with flag or have a problem, file a
request or issue on the flag queue at
http://drupal.org/project/issues/flag. DO NOT POST IN THE FORUMS.
Posting in the issue queues is a direct line of communication with the module
authors.

No guarantee is provided with this software, no matter how critical your
information, module authors are not responsible for damage caused by this
software or obligated in any way to correct problems you may experience.

Licensed under the GPL 2.0.
http://www.gnu.org/licenses/gpl-2.0.txt


Theming instructions
====================

You may want to visit the Theming Guide of this module, at:

  http://drupal.org/node/295346

Template file
-------------
In order to customize flag theming:

- Copy the 'flag.tpl.php' template file into your theme's folder.[1]

- Clear your theme registry.[2]

- Edit that copy to your liking.


Template variants
-----------------
The theme layer will first look for the following templates in this order:
  - flag--<FLAG_NAME>.tpl.php
  - flag--<FLAG_LINK_TYPE>.tpl.php
  - flag.tpl.php
These should also be placed in your theme's folder.[2][1]


Footnotes
---------
[1] Or to a sub-folder in your theme's folder.

[2] Clearing the theme registry makes Drupal aware of your new template
file. This step is needed if you create or rename template files. This
step *isn't* needed if you merely modify the contents of a file. Instructions
on how to clear you theme registry are at http://drupal.org/node/173880#theme-registry

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
Jose A. Reyero, http://reyero.net[![Build Status](https://travis-ci.org/Gizra/og.svg?branch=7.x-2.x)](https://travis-ci.org/Gizra/og)

DESCRIPTION
--------------------------
The Organic Groups module (also referred to as the 'og' module), provides users
the ability to create, manage, and delete their own 'groups' on a site.
Each group can have members, and maintains a group home page which individual
group members may post into. Posts can be sent to multiple groups (i.e. cross-
posted), and individual posts (referred as 'group content') may be shared with
members, or non-members where necessary.
Group membership can be open, closed or moderated.

TERMS AND DEFINITIONS
------------------------------------
- GROUP: A single node which can have different content types and users
  associated with it.
- GROUP CONTENT: Content such as nodes or users, which are associated with a
  group.
- GROUP ADMIN: Is a privileged user with permission to administer particular
  activities within a group.
- SITE ADMIN: Compared to group admin, a site admin is granted access to all
  groups operating within a site. The site admin can specify the permissions
  group admins are granted in order to control their group related activities,
  while keeping other permissions out of their reach.
- GROUP CONTEXT: Whenever an individual piece of content such as a node or a
  user is viewed, the module attempts to determine if the content is associated
  with a particular group.
  The group context is later on used to determine which access rights the user
  is granted. For example, in a particular group context the user can edit
  nodes, but is only allowed to view the nodes in a different group context.
  The group context can also be used by custom modules to determine different
  behaviors. For example, displaying different blocks on different groups,
  switching to a different theme, etc.
- ENTITY: Nodes, users, and taxonomy terms, are examples of Drupal entities.
  Organic Groups allows each individual Drupal entity type to be associated with
  a group or with a group content. This means that you can associate different
  users (as group content) to a certain user (as a group).

GROUP ARCHITECTURE
--------------------------
At the lowest level the module associates content types with groups. Above this
level is the role and permissions layer, which operates at the group level.
The Organic Groups module leverages Drupal's core functionality, especially the
field API. This means that a content type is associated with a group, by setting
the correct field value.
Users are also allowed to select the groups that will be associated with the
content from a list of groups, which they have authorization to view.
As is the case with Drupal itself, in Organic Groups different permissions can
be assigned to different user roles. This allows group members to perform a
different set of actions, in different group contexts.

INSTALLATION DRUPAL 7.x
--------------------------------------------
Note that the following guide is here to get you started. Names for content
types, groups and group content given here are suggestions and are given to
provide a quick way to get started with Organic groups.

1. Enable the Group and the Group UI modules.
2. Create a new content type via admin/structure/types/add. Call it "Group", and
   define it to be of Group type.
3. Create a second content type. Call it "Group content", and set it to be of
   Group content type.
4. Add a Group by going to node/add/group. Call it First group, and enable the
   Group through the "Group type" field.
5. Add a Group Content by going to node/add/group-content. In the Groups
   audience field, select First group. In the group content view a link was
   added to the group.
6. Click on the Group link. In the group view, a new tab was added labeled
   Group.
7. Click on the Group tab. You will be redirected to the group administration
   area. Note that this is the administration of First group only. It will not
   affect existing or new groups which will be created on the site.
8. You are now presented with different actions you can perform within the
   group. Such as add group members, add roles, and set member permissions. You
   will notice that these options have the same look and feel as Drupal core in
   matters relating to management of roles and permissions.
9. You can enable your privileged users to subscribe to a group by providing a
   'Subscribe' link. (Subscribing is the act of associating a user with a group.)
   To show this subscribe link:
   9.1 Make sure you have the Group UI module enabled
   9.2 Go to admin/config/group/permissions and make sure that the "Subscribe user to group"
       permission is given to the appropriate user-roles.
   9.3 Navigate to the "manage display" tab of your content type
      (admin/structure/types/manage/group/display)
       and choose the Group subscription format for the Group type field.
   9.4 Back in the group view you will now notice a 'Subscribe' link (If you are the
       group administrator it will say "You are the group manager").
10. In order to associate other entities with group or group content, navigate
    to Organic Groups field settings", in admin/config/group/fields.
11. In order to define default permissions for groups that are newly created or
    to edit permissions on all existing groups, navigate to the Group
    default permissions page. Important permissions in this page are the ones
    under the administer section. These permissions are what enable group admins
    to have granular control over their own group. This means, that if you as
    the site admin, don't want to allow group admins to control who can edit
    nodes in their own group, you need to uncheck those permissions.

DEVELOPERS & SITE BUILDERS
----------------------------------------------
- Views integration: There are some default views that ship with the module.
  Follow those views configuration in terms of best practice (e.g. adding a
  relationship to the group-membership entity instead of querying directly the
  group-audience field).
- Token integration: Enable the entity-tokens module that ships with Entity API
  module.
- Rules integration: Organic groups is shipped with a Rules configuration that
  allows simple notification. You can disable it or clone and change its
  behaviour.
- Devel generate integration: Enable devel-generate module to create dummy
  groups and groups content.
- You may craft your own URLs to prepopulate the group-audience fields
  (e.g. node/add/post?field_group_audience=1 to prepopulate reference to
  node ID 1), using the "Entity reference prepopulate" module
  http://drupal.org/project/entityreference_prepopulate
  and configuring the correct settings in the field UI. Read more about
  it in Entity reference prepopulate's README file.
  Further more, when Entity reference prepopulate module is enabled the node
  "create" permissions will be enabled even for non-members. In order to allow
  a non member to create a node to a group they don't belong to, you should
  craft the URL in the same way. OG will recognize this situation and add the
  group as a valid option under the "My groups" widget.
- When deleting groups, it is possible to delete orphan group-content, or move
  it under another group. In order to do it in a scalable way, enable the
  "Use queue" option, and process it using for example:
  drush queue-run og_membership_orphans

FAQ
----
Q: How should I update from Drupal 6?
A: Run update.php; Enable the og-migrate module and execute all the migration
   plugins.

Q: How should I update from a previous Drupal 7 release (e.g. 7.x-1.0 to
   7.x-1.1)?
A: Same as updating from Drupal 6 -- Run update.php; If requested enable the
    og-migrate module and execute all the migration plugins.

Q: How do I use OG tokens with pathauto module to craft the url alias.
A: After enabling entity-tokens module you will have some tokens exposes by
   Organic groups. However you are not able to do something like
   [node:og_membership(1):group:label].
   See http://drupal.org/node/1088538#comment-4376910

Q: Must I use Panels module along with Organic groups?
A: No. However note that the maintainer of the module highly recommends using
   it, and considers it as good practice.

CREDITS
----------------------------
- Organic groups for Drupal 5 and 6 authored by Moshe Weitzman -
  <weitzman AT tejasa DOT com>
- Current project maintainer and Drupal 7 author is Amitai Burstein (Amitaibu) -
  gizra.com
DESCRIPTION
-----------
The "Organic groups field access" module lets you define which fields are
accessible by group members and non-members. For each field that is in a group
or a group content you can decide who can view the field and who can edit it.

USAGE
-----
1. Enable Organic Groups Field Access at admin/modules
2. Go to admin/config/group/permissions and define the access permissions


INSTALLATION
------------
1) Enable module and all the dependencies.
2) In /admin/structure/pages enable the pre-configured "node_view" 
   (path is /node/%node).
Views Data Export
=================

Introduction
------------

This module is designed to provide a way to export large amounts of data from
views. It provides a display plugin that can rendered progressively in a batch.
Style plugins are include that support exporting in the following types:

* CSV
* Microsoft XLS
* Microsoft Doc
* Basic txt
* Simple xml.

Using the "Views Data Export" module
------------------------------------

1. Add a new "Data export" display to your view.
2. Change its "Style" to the desired export type. e.g. "CSV file".
3. Configure the options (such as name, quote, etc.). You can go back and do
   this at any time by clicking the gear icon next to the style plugin you just
   selected.
4. Give it a path in the Feed settings such as "path/to/view/csv".
5. Optionally, you can choose to attach this to another of your displays by
   updating the "Attach to:" option in feed settings.

Advanced usage
--------------

This module also exposes a drush command that can execute the view and save its
results to a file.

drush views-data-export [view-name] [display-id] [output-file]


History
-------

This module has its roots in the export module that was part of the views bonus
pack (http://drupal.org/project/views_bonus). However, massive changes were
needed to make the batch export functionality work, and so this fork was 
created. See: http://drupal.org/node/805960

Language icons
http://drupal.org/project/languageicons
=======================================


DESCRIPTION
-----------
This module provides icons for language links, both for the Language switcher
block and (optionally) for node links.
It is a spin-off from Internationalization (i18n) package.


REQUIREMENTS
------------
Drupal 7.x

For a fully enabled multilingual site, the Internationalization (i18n) package
is recommended. See http://drupal.org/project/i18n 


INSTALLING
----------
1. To install the module copy the 'languageicons' folder to your
   sites/all/modules directory.

2. Go to admin/build/modules. Enable the module.
Read more about installing modules at http://drupal.org/node/70151


CONFIGURING AND USING
---------------------
1. Go to admin/structure/block

2. Ensure that 'Language switcher' block is associated with a visible region. If
   unsure, move the 'Language switcher' block to 'Sidebar first' region.

3. Click on 'Save blocks' button.

4. To preview simply view any appropriate page. If successful you will see a
   flag on the left side of each language link.

There are some configuration options at admin/config/regional/language/icons.
You can place flags before or after the language link or choose to only display
the language flag without the language name (pick "Replace link" under icon
placement to do so). There are some other options so make sure to check it out.


CONTRIBUTING. REPORTING ISSUE. REQUESTING SUPPORT. REQUESTING NEW FEATURE.
--------------------------------------------------------------------------
1. Go to the module issue queue at
   http://drupal.org/project/issues/languageicons?status=All&categories=All
2. Click on CREATE A NEW ISSUE link.
3. Fill out the form.
4. To get a status report on your request go to
   http://drupal.org/project/issues/user


UPGRADING
---------
Read more at http://drupal.org/node/250790

ABOUT

"Eva" is short for "Entity Views Attachment;" it provides a Views display
plugin that allows the output of a View to be attached to the content of any
Drupal entity. The body of a node or comment, the profile of a user account,
or the listing page for a Taxonomy term are all examples of entity content.

The placement of the view in the entity's content can be reordered on the
"Field Display" administration page for that entity, like other fields added
using the Field UI module.

In addition, the unique ID of the entity the view is attached to -- as well as
any tokens generated from that entity -- can be passed in as arguments to the
view. For example, you might make a View that displays posts with an 'Author
ID' argument, then use Eva to attach the view to the User entity type. When a
user profile is displayed, the User's ID will be passed in as the argument to
the view magically.

That's right: magically.

Eva is powered by witchcraft.

HISTORY

Eva was originally developed by Jeff Eaton but never released. Larry Garfield
later cleaned it up and added the CCK integration, then released it under the
name 'Views Attach.' Endless confusion followed, as everyone thought it would
allow them to attach things to Views. Then Jeff Eaton refactored it for Drupal
7. Then they renamed it again, because they didn't want to write an upgrade
path.

Why *isn't* there an upgrade path? This version is built on top of Drupal 7's
Entity API as a single unified Views Display, while the D6 version juggled
NodeAPI and hook_user. While there's definitely feature parity, enough has
changed that cleanly upgrading a view from Views Attach 6.x-2.0 is essentially
impossible. They feel bad about it, and would accept patches that implemented
a well-tested upgrade path, but don't have the bandwidth to implement it
ourselves.

REQUIREMENTS

- Drupal 7
- Views 3

AUTHOR AND CREDIT

Original development: Jeff Eaton "eaton" (http://drupal.org/user/16496)

Actual D6 release, and version 2.0: Larry Garfield "Crell"
(http://drupal.org/user/26398)

D7 port and tomfoolery: Jeff Eaton "eaton" (http://drupal.org/user/16496)
Select (or other) README

CONTENTS OF THIS FILE
----------------------

  * Introduction
  * Installation
  * Usage
  * Example


INTRODUCTION
------------
Maintainer: Daniel Braksator (http://drupal.org/user/134005)

Project page: http://drupal.org/project/select_or_other.


INSTALLATION
------------
1. Copy select_or_other folder to modules directory.
   Usually sites/all/modules
2. At admin/build/modules enable the Select (or other) module.


USAGE
------------
Field API integration is available for Boolean, Decimal, Float, and Text field
types.

Webform integration is built into Webform 3.

Custom Forms API usage instructions available on project page.


EXAMPLE
-------
Visit path 'select-or-other-test-form' on your site.
For example: http://www.example.com/select-or-other-test-form
NOTE: You must have the permission to 'access administration pages'.
Conditional Fields:
--------------------
A Drupal module


Author:
--------------------
Gregorio Magini (peterpoe) <gmagini@gmail.com> - http://www.twitter.com/peterpoe


Short Description:
--------------------
Define dependencies between fields based on their states and values. Conditional Fields for Drupal 7 is basically an user interface for the States API, plus the ability to hide fields on certain conditions when viewing content.


Description:
--------------------
The Conditional Fields module allows you to manage sets of dependencies between fields. When a field is "dependent", it will only be available for editing and displayed if the state of the "dependee" field matches the right condition.
When editing a node (or any other entity type that supports fields, like users and categories), the dependent fields are dynamically modified with the States API.
You can, for example, define a custom “Article teaser" field that is shown only if a "Has teaser" checkbox is checked.


Dependencies:
--------------------
- Drupal core: version 7.14 or higher.


Installation:
--------------------
- Install as usual, see http://drupal.org/documentation/install/modules-themes/modules-7 for further information.


Usage:
--------------------
Users with the "administer dependencies" permission can administer dependencies at admin/structure/dependencies.

For more information, read the Conditional Fields documentation:
http://drupal.org/node/1704126


Upgrading from Drupal 6 to Drupal 7
--------------------
Read carefully these instructions since taking the wrong steps could lead to loss of dependencies data!

- Before upgrading, ensure that you have the latest stable version of Conditional Fields for Drupal 6 installed and working.
- Follow the instructions on the D6 to D7 upgrade process here: http://drupal.org/node/570162.
- Most importantly, you have to migrate your old CCK fields to the new format BEFORE updating Conditional Fields, so do not omit step 14: "Upgrade fields"! Failing to do so will give an error when trying to run the subsequent update on step 15: "Update contrib modules and themes" and could lead to loss of dependencies data.
- After step 14, leave the Content Migrate module activated. You can safely disable it after step 15.
- Note that Content Migrate in certain cases changes the allowed values of fields: you will have to manually edit the dependencies to match the new allowed values if this happens.


Limitations:
--------------------
- Conditional Fields, for now, supports only core fields and widgets as dependee fields. Fields from other modules might work, but probably won't. Dependent fields, though, can be of any type.


Any help is welcome!
--------------------
Check the issue queue of this module for more information:
http://drupal.org/project/issues/conditional_fields

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

An example of a module using this API is Internationalization's i18n_variable module.Defines a formatter that renders a link like an iframe

This module has been sponsored by [Atenea tech](http://ateneatech.com

Requires:
---------

* [Link](http://drupal.org/project/link)

Installation:
-------------

Just drop this module folder into your modules folder, as usual, and enable it.

Usage:
------

Once enabled, you can select "Iframe" as the display formatter of a "Link" 
field in the "Manage display" page of the desired content type. You can set the 
width and the height of the generated iframe tag.

Drupal module implementing the oEmbed standard: http://oembed.com/

* Supplies an input filter that replaces URL:s from oEmbed enabled sites with the embeddable data fetched from it
* Contains a CCK field for exposing oEmbed content
* Makes it possible for a Drupal site to become an oEmbed provider itself
* Creates a oEmbed PHP Stream Wrapper for Resource and implements the various
  formatter and file listing hooks in the File Entity and Media module.
/* $Id: README.txt,v 1.4 2011/01/09 06:22:40 sun Exp $ */

-- SUMMARY --

Compact Forms presents text fields for selected forms in a more compact fashion
using jQuery.

The form item/element fields are overlaid with their respective labels.  When
the user focuses a field the label fades away nicely, and if the field is left
empty the label fades back in again.

By default, only the user login block is switched to compact style, but the
behavior can be added to any form by adding the corresponding CSS ids to the
Compact Forms configuration.

For a full description of the module, visit the project page:
  http://drupal.org/project/compact_forms

To submit bug reports and feature suggestions, or to track changes:
  http://drupal.org/project/issues/compact_forms


-- REQUIREMENTS --

* None.


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.


-- CONFIGURATION --

* Configure forms to display compact in Administration » Configuration »
  User interface » Compact Forms.


-- CUSTOMIZATION --

* To programmatically disable the compact forms behavior on a particular form,
  set the following property on the $form element in your form constructor
  function or via hook_form_alter():

    $form['#compact_forms'] = FALSE;


-- CONTACT --

Current maintainers:
* Daniel F. Kudwien (sun) - http://drupal.org/user/54136

Previous maintainers:
* Tom Sundström (tomsun) - http://drupal.org/user/63478

This project has been sponsored by:
* UNLEASHED MIND
  Specialized in consulting and planning of Drupal powered sites, UNLEASHED
  MIND offers installation, development, theming, customization, and hosting
  to get you started. Visit http://www.unleashedmind.com for more information.

INTRODUCTION
------------

This module provides a multiselect widget plugin for the Facet API module
(http://drupal.org/project/facetapi).

It allows faceted searches (for example, those performed with Apache Solr) to
use a multiple select dropdown for drilling down into the search results.  It
automatically supports optgroups (for data with a hierarchy) as well.

JAVASCRIPT PLUGIN INTEGRATION
-----------------------------

Although this module can be used on its own, the standard HTML multiple select
element which it outputs is generally considered to have poor usability. Thus,
this module's primary use case is to allow easy integration of faceted search
with JavaScript plugins that provided an enhanced experience for multiple
select dropdowns. For example:
- jQuery UI MultiSelect Widget (http://www.erichynds.com/jquery/jquery-ui-multiselect-widget/)
- jQuery UI Multiselect (http://quasipartikel.at/multiselect/)
- Chosen (http://harvesthq.github.com/chosen/)

Integration can be accomplished relatively easily using hook_form_alter(). A
basic example is shown below, specifically targeted to the jQuery UI
MultiSelect Widget although similar code will likely work for other JavaScript
plugins too.

<?php
/**
 * Implements hook_form_BASE_FORM_ID_alter().
 */
function MYMODULE_form_facetapi_multiselect_form_alter(&$form, &$form_state) {
  // Add the JavaScript and CSS for the library itself. This assumes you are
  // using the Libraries module (http://drupal.org/project/libraries) and that
  // you've put the external library in sites/all/libraries/jquery.multiselect.
  // Note: Rather than adding each JS and CSS file individually as is done
  // below, hook_library() and $form['#attached']['library'][] could be used
  // instead.
  $path = libraries_get_path('jquery.multiselect');
  $form['#attached']['js'][] = $path . '/jquery.multiselect.min.js';
  $form['#attached']['css'][] = $path . '/jquery.multiselect.css';

  // Add a custom JavaScript file which will trigger the jQuery MultiSelect
  // widget on the correct form elements.
  $form['#attached']['js'][] = drupal_get_path('module', 'MYMODULE') . '/MYMODULE.facetapi.multiselect.js';
}
?>

The content of the above custom JavaScript file could be as simple as:

Drupal.behaviors.MYMODULEFacetApiMultiselectWidget = {
  attach: function (context, settings) {
    // Go through each facet API multiselect element that is being displayed.
    jQuery('.facetapi-multiselect', context).each(function () {
      // Attach the behavior to it.
      jQuery(this).multiselect({
        // Pass in whatever array of options you need here.
      });
    });
  }
};

Obviously, the exact content will depend on which JavaScript plugin you are
using and which options it requires.

If you need more complex functionality, note that when altering this form you
have access to a $form_state['facetapi_multiselect'] array with information
about the facet and widget (this information is also available in
$form['#facetapi_multiselect'] if for some reason you don't have access to
$form_state). This array contains the following keys:
- widget: The object used to build the multiselect Facet API widget. Any of its
  public methods are available to call.
- facet_name: The machine-readable name of the facet this widget was built for.
- facet_class: An HTML class based on facet name. All widgets will have the
  shared "facetapi-multiselect" class applied to them (used in the custom
  JavaScript example above), but this additional class allows you to uniquely
  target the widget for this particular facet; for example, you can pass it as
  a JavaScript setting and use it in order to have your custom JavaScript code
  make specific changes to this particular facet.

RELATED PROJECTS
----------------

If you are interested in this module, you might also want to take a look at the
following sandbox projects (this module also owes a debt to them for
inspiration for some of the code):
- Facetapi Select (http://drupal.org/sandbox/lynn/1311040), which provides a
  widget plugin for single selects, rather than multiselects
- Facet API Chosen (http://drupal.org/sandbox/sammyd56/1353462), which
  integrates directly with the Chosen JavaScript plugin, but currently only
  supports single selects, not multiselects.

CREDITS
-------

This project was sponsored by Advomatic (http://advomatic.com).
  ------------------------------------------------------------------------------------
                                      INSTALLATION
  ------------------------------------------------------------------------------------

  This module requires optional core modules: "Locale" and "Content translation".
  The module will populate a new block named "Language switcher dropdown" under "{host}/admin/structure/block".
  
  Please see the below instructions to configure the block.

  ------------------------------------------------------------------------------------
                                      CONFIGURATION
  ------------------------------------------------------------------------------------

  1) Configure the "Language negotiation" at "{host}/admin/config/regional/language/configure".
     
  2) Enable the "Language switcher dropdown" block at "{host}/admin/structure/block".
  
  3) Configure the "Language switcher dropdown" block settings as follows:
     - "Output as HTML and JavaScript widget instead of HTML select element"
        The option will allow you to display the widget using themable HTML and JavaScript widget instead of the default select element.
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
  * Stem words
    Uses the PorterStemmer method to reduce words to stems. A search for
    "garden" will return results for "gardening" and "garden," as will a search
    for "gardening."

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

"Random sort" feature
---------------------
This module defines the "Random sort" feature (feature key:
"search_api_random_sort") that allows to randomly sort the results returned by a
search. With a server supporting this, you can use the "Global: Random" sort to
sort the view's results randomly. Every time the query is run a different
sorting will be provided.

For developers:
A service class that wants to support this feature has to check for a
"search_api_random" field in the search query's sorts and insert a random sort
in that position. If the query is sorted in this way, then the
"search_api_random_sort" query option can contain additional options for the
random sort, as an associative array with any of the following keys:
- seed: A numeric seed value to use for the random sort.

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
Entity RDF module
-----------------

The Entity RDF module is a replacement for the Drupal 7 core RDF module offering a tight integration between the RDF mappings and Entity API. Each RDF mapping is attached to its appropriate property definition in the the Entity API property info.

The Entity RDF module attempts to solve some of the issues and shortcomings of the Drupal 7 core RDF module:
- RDF mappings can not only be assigned to entity properties and fields but also to field internal values, which is useful for compound fields such as addressfield for example
- References to classes and properties are stored as full URIs to avoid depending on prefix bindings (the use of CURIEs is left up to the administration UI and/or the serialization)
- RDF mappings are no longer carried around in the entity object (the stucture info is separate from the data)
- RDF mappings are available in the entity metadata wrapper
- Default RDF mappings are no longer automatically set for common properties, but instead they need to be enabled. Suggestions for mappings can be provided to the administrator setting the mappings.



Mappings are visible Entity API's property info, for example:
entity_metadata_wrapper('node', 1)->getPropertyInfo();
entity_get_property_info('node');
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
the Field API./**
 * @file
 * README file for Workbench Media.
 */

Workbench Media
Workbench integration for the File, File Entity, and Media modules.

CONTENTS
--------

1.  Introduction
1.1   Use-case
1.2   Examples
2.  Installation
3.  Permissions
4.  Configuration
5.  Using the module
6.  Troubleshooting
7.  Developer notes
7.1   API documentation
7.2   Database schema
8.  Feature roadmap


----
1.  Introduction

Workbench Media provides integration with the File, File Entity, and Media
modules for Workbench and its suite of modules.

Workbench Media provides some basic file management within the Workbench
framework; essentially, it allows users to see all files that have been
uploaded to the site.

----
1.1  Use-case

Media module is a solution for managing various media files including
images, video, and audio.  The Media Workbench module allows a user to add
media items without having to leave the Workbench.

A typical request from clients is to re-use files that have already been
uploaded to a site.  Any type of file might be re-used: PDF, PNG, ZIP.

----
1.2  Examples

To support large numbers of photo galleries or slideshows it's nice to provide
a reverse lookup.  Create your photo gallery, then create media items and
use a node reference field to choose which gallery will display the media item.

Adding a media item on its own requires having access to Find Content -> Media
tab.  We wanted to simplify where content administrators need to go to add
any content.


----
2.  Installation

Workbench and Media are required in order to install Workbench Media.


----
3.  Permissions

Permissions need to be set for Media and Workbench Media modules in order to
make use of Workbench Media.

Workbench Media has one permission:

 -- Use the media add form
 Allows the user to add media directly from the Create Content tab.

A typical permission setup so that a user can take advangate of Workbench Media
looks like:

  Media Permissions
   -- View media
   -- Edit media

  Workbench
   -- Access My Workbench

  Workbench Media
   -- Use the media add form

A user needs the "Access My Workbench" permission which is a general
Workbench permission setting.  If a user has Access My Workbench permission,
then she can access Workbench Files.


----
4.  Configuration

There is no specific configuration for Workbench Media.


----
5.  Using the module

When viewing the Workbench, you can access media items in two ways.

Click the Create Content tab.  The Create Media list is at the top.  Click
Upload Media.  From there you select a file to upload.  Click Save, and it is
saved as a media item.

Media items are entities.  You can easily expand a media item to contain any
important meta data you want to store with the uploaded file.  Learn more at
http://drupal.org/project/media

Back in My Workbench, you can see media you have uploaded in the File List tab.

When viewing My Workbench, you will see that Workbench Media adds a tab
called "File List".  Click this tab.

The File List tab provides a list of all files that have been uploaded to the
site.  Typical web image file formats (like jpg, png, gif) will include a
thumbnail of the image in the Type column.  Other file types like PDF display a
icon representing the file type.

The list includes which nodes use the file, the URL as well as the filepath
(e.g. public://filename.pdf).


----
6.  Troubleshooting

When I add media, I get a Permission Denied error when I click save.
  -- Fix this by setting the "View media" and "Edit media" permissions for your
  user role.


----
7.  Developer notes

The following section documents technical details of interest to developers.

----
7.1   API documentation

Workbench Media does not offer an API.

----
7.2   Database schema

Workbench Media does not create any tables during installation.

----
8.  Feature roadmap

We think some of the changes made for Workbench Media may roll back into Media.
Workbench Media has been merged with Workbench Files. Please see "tasks" in the
Workbench Media issue queue for information on the current direction:
http://drupal.org/project/issues/workbench_media?status=Open&categories=task
OAuth implements the OAuth classes for use with Drupal and acts as a support
module for other modules that wish to use OAuth.

OAuth Client flow:

The callback to be used is /oauth/authorized/% where % is the id of the consumer
used by the client. We need the id of the consumer to be able to find the token
correctly.

CONTENTS
--------

 * About
 * Installation
 * On-page translation
 * Sharing translations
 * Re-importing translation packages
 * Contributors & sponsors

ABOUT
-----

The main goal of the Localization client module (l10n_client) is to provide you
with an easy way to translate your website's interface. The module includes an
AJAX on-page editor that allows you to translate right on the actual web page
that you are viewing. The Localization client module also offers an overview
of all interface strings of your website. This module only lets you translate
the website's interface, for information on translating your site's content
please check the Drupal handbook page about the Translation module
(http://drupal.org/handbook/modules/translation).

The module can instantly share your translations by sending them to
localization servers such as localize.drupal.org. See also the Localization
server project  (http://drupal.org/project/l10n_server).

Finally the module includes a translation package re-import tool, which
simplifies importing new and changed translations, especially when upgrading
or developing modules. This functionality is similar to the Drupal 5.x
Autolocale module (http://drupal.org/project/autolocale).

The translation sharing and re-import tools are only available in the 6.x
version of the module because these functionalities are based on features only
available in Drupal 6.x. Therefore it is impossible to backport these
functionalities to the 5.x version without modifying Drupal itself.

 * Project page: http://drupal.org/project/l10n_client
 * Support queue: http://drupal.org/project/issues/l10n_client

INSTALLATION
------------

 1. Enable the Localization client module at Administer > Modules
 2. Enable two or more languages at Administer > Configuration > Regional and
    Language > Languages. For help with building a multilingual website please
    check the Drupal handbook page about the Locale module at
    http://drupal.org/handbook/modules/locale
 3. Join a language team on localize.drupal.org (required to be able to submit
    translation updates)
 4. Assign the appropriate permissions to the user roles under the section
    "Localization client module" at Administer > People > Permissions

ON-PAGE TRANSLATION
-------------------

Users with the permission "Use on-page translation" can translate interface
strings right on the page that they are viewing.

 1. Switch the website's language to one that is not English.
 2. Browse to the webpage that contains the interface string you want to translate
 3. Click the "TRANSLATE TEXT" button in the right bottom corner of the webpage
    The on-page translation pane appears, showing all strings available on the
    current webpage in the left column. Already translated strings are marked
    green, yet untranslated strings are shown in white. You can filter the list
    using the input field in the left bottom corner of the page.
 4. Select a string in the left column to see the source text and the
    translation (if available). You can add your own translation or edit the
    existing translation in the column at the right. Your changes will be saved
    to your local database. The translations can be shared (see below).

Open the list of all the website's interface strings by selecting Translate
Strings from the menu (http://www.example.com/locale). Click "TRANSLATE TEXT"
to start translating.

SHARING TRANSLATIONS
--------------------

Localization client can instantly share your translations by sending them to a
localization server. For this a user needs the "Submit translations to
localization server" permission. To be able to share translations a user needs
an API key from the localization server.

 1. Enable translation sharing at Administer > Configuration > Regional and
    Language > Languages > Sharing
 2. Enter a localization server, e.g. "http://localize.drupal.org"
 3. Join a language team on localize.drupal.org (required to be able to submit
    translation updates)
 3. Enter your localization server API key at My account > Edit
    (The form field has a link to obtain the key from the set localization server)
 4. Start translating interface strings.

RE-IMPORTING TRANSLATION PACKAGES
-----------------------------------------------------------------

To re-import translation all files should be already uncompressed to the
Drupal directories.

Choose the languages for which you want to re-import translations at
Administer > Configuration > Regional and language > Translate interface >
Import > Reimport packages.

See also http://drupal.org/project/l10n_update.

CONTRIBUTORS & SPONSORS
--------------------------------------------------------------------------------

 * Gábor Hojtsy http://drupal.org/user/4166 (original author)
 * Young Hahn / Development Seed - http://developmentseed.org/ (friendly user interface)

Initial development was sponsored by Google Summer of Code 2007,
user interface sponsored by Development Seed / Young Hahn.
Superfish module

About
-----
This module allows for integration of jQuery Superfish plug-in with Drupal CMS.


Requirement
-----------
- Superfish library.
  Link: http://drupal.org/project/superfish


Installation instructions
-------------------------
1. Download and extract the Superfish library into the libraries directory (usually
   "sites/all/libraries").
   Link: https://github.com/mehrpadin/Superfish-for-Drupal/zipball/master

2. Download and extract the Superfish module into the modules directory (usually
   "sites/all/modules").
   Link: http://drupal.org/project/superfish
   Drush users can use the command "drush superfish-plugin".

3. Go to "Administer" -> "Modules" and enable the module.

Note: Though no longer required, using Libraries API is still recommended.
      Link: http://drupal.org/project/libraries


Upgrade instructions
--------------------
Did you change any part of the module or the library?

- If you did not change the module or the library; download the latest versions of the module and
  the library and upload them (replacing the old files).

- If you did change the module or the library; use a visual comparison tool (such as Winmerge 
  or Kompare, so on) in order to compare your current copy with its original one (you can find it at
  http://drupal.org/node/711944/release) find out what was changed and do the same to the version
  you are upgrading to.
  WARNING: This is for experts only!
  
- Please note that if you are upgrading from version 1.6 running update.php will cause error
  messages to appear. To resolve this go to "Administer" -> "Structure" -> "Blocks", click the
  "Configure" link for each Superfish block and click "Save block" button.
  

Configuring the module
----------------------
- For block-specific settings go to "Administer" -> "Structure" -> "Blocks" and click the
  "Configure" link of the Superfish block.

- For module settings go to "Administer" -> "Configuration" -> "User Interface" -> "Superfish".

- Detailed configuration instructions can be found at http://drupal.org/node/1125896


How to style
------------
If you know CSS, even basics of it, designing won't be a big challenge.

Here are some tips and tricks:

A) Always use a DOM inspector utility (such as Firebug).

B) Set the "Menu delay" option to a very high number such as 99999999. This will give you enough
   time to work with sub-menus.

C) If you are not using the built-in styles, set the "Style" option to "None".

D) Utilise the "Simple" style as reference; add the newly-created CSS file either to your theme CSS
   or as a new CSS file under the styles directory in the Superfish library (probably
   "sites/all/libraries/superfish/style"); putting it in the styles folder will automatically add it
   to the styles list in the block configuration.
   
- More information can be found in the Superfish documentation at http://drupal.org/node/1125896


Support requests
----------------
You can request support here: http://drupal.org/project/issues/superfish


How to help?
------------
Glad you asked that :)

- Help find bugs!
- Suggest new features!
- Test the beta versions!
- Translate the UI into your language!
Enhanced autocomplete widget for drupal 7.xDraggableViews
==============

This module provides dragging entities and saving their order.

Quick install:
 1) Activate Draggableviews module at admin/modules.
 2) Navigate to view edit-page, click on the first link at the Format section and then choose style "table".
 3) Click Add button at the "Fields" section and choose field "Content:title", add and apply.
 4) Click Add button at the "Fields" section and choose field "Draggableviews: Content", add apply.
 5) Click Add button at the "Sort criteria" section and choose field "Draggableviews: Weight", add and choose sort asc, then apply.
 6) Save the view and you're done.

In the case of table standard drupal tabledrag.js JavaScript is used.

We also support jQuery UI Sortable JavaScript. In order to use it please set display style HTML List.
By default HTML list is displayed like grid. If you would like it to be displayed as list override
CSS styles for example in following way:
  .draggableviews-processed li.views-row { float: none; width: 100%; margin-left: 0; }

One view/display to set order another to display
================================================

You can create one view to set the order and another view to display the order. Or even
create one view with two separate displays. In a view that displays the order there
should be no draggableviews field (that makes view sortable), then in the settings of
the "draggableviews weight" sorting criteria there will be selectbox "Display sort as"
where you can choose the source view of your weights. This is applicable when you use
 Native handler.

Step by Step Guide for Creating a New View with 2 Displays:
===========================================================
Requirements: Draggableviews 7.x-2.x, Views 7.x-3.x, Views UI module enabled.

 1) Activate Draggableviews module at admin/modules.
 2) Create a new view
    - Goto '/admin/structure/views/add' on your site.
    - Check off 'Create a page'.
    - Check off 'Create a block'.
    - Set the 'Display format' for the page to what you desire.
    - Set the "'Display format' of" to fields.
    - Set the 'Display format' for the block to table.
    - Fill in the rest of the views information.
    - Click Continue & edit button.
 3) Under the "FIELDS" section, do you see "Content: Title (Title)"?  If you do not:
    - Click 'add' button at the "Fields" section and choose field "Content:title", add and apply.
 4) Click on 'Block' under the 'Display', to change the view display to the block display.
 5) Add the Draggableviews Field:
    - Click Add button at the "FIELDS" section.
    - At the top of the overlay, Change "For: 'All displays'" to 'This block (override)'.
      - If you do not do this then the field will be add to all displays and will prevent your
        page display from using the block display to sort the order.
 5) Click Add button at the "SORT CRITERIA" section choose field "Draggableviews: Weight", add and choose sort asc, then apply.
 6) Under the "SORT CRITERIA" section, do you see "Content: Post date (asc)"?  If you do:
    - Click on it.  At the bottom, click the 'Remove' button.
      - An alternative is to rearrange the "SORT CRITERIA" order, making sure 'Draggableviews: Weight (asc)
        appears first (or on top).
 7) Save the view and you're done.*
*Things to confirm after you saved your new view.
- In the Administrative Views UI, Go back to your View's 'page' display.
  -> Click 'Draggableviews: Weight (asc)' under 'SORT CRITERIA'
  -> You should see:

  Display sort as:
  <title of view> (<display title>)

  This should the view and block display you just create.

  FYI - This is also where you can change it to another view.

Permissions
===========

Add "Access draggable views" permission to users who should be able to reorder views.  If a user does not have this
permission they can still see the view, however they will not be able to reorder it.

If you want only want the order view visible to users with "Access draggable views" then set the Access to
"Permission: Access draggable views".

When users have the "Access draggable views" and "Use contextual links" permission, they will see
a contextual link from the non-reordering view to the ordering view.

Arguments handling
==================

Every time we save the order of a view, current set of arguments are saved with order.
You can see this in draggableviews_structure table "args" column. By default when we display order we use all
currently passed arguments to a view to "match" arguments in "args" column. This means that we can create
a view with contextual filter or exposed filter criteria and save different orders for different sets of arguments.

Using the "Do not use any arguments (use empty arguments)" option will completely ignore passed arguments used
in the Arguments handling of Sort criteria Draggable views weight. Be aware that in this case empty arguments set
will be used. So you can set order for a view when no arguments passed and then whatever arguments passed,
empty set will be used.

Using the "Prepare arguments with PHP code" option will let you alter arguments before they passed to
"matching" with "args" column. For us this means that we can create, for example, several exposed filters,
but pass values of only one of values of exposed filters instead of all of them (like we create two exposed
filters: author and node type, but take into account for ordering only node type).
Please be aware that in PHP code arguments are passed as $arguments variable and you should return an array.
IE return array('status' => 1, 'user' => 2);  or return $arguments; // $arguments is already an array

When using arguments,  make sure your ordering view display has the same arguments as the display you want to show
the end user.  If they do not match, then your ordering will not match.

Using hook_draggableviews_handler_native_arguments_alter(&$arguments, $view, &$form_values) {} You may remove or change
the arguments save to the database, just as the "Prepare arguments with PHP code" option. See draggavleviews.api.php
for more details.

In the $arguments array, Contextual filters are number keyed and exposed filters are name keyed.

Removed Arguments:
- The pager 'item_per_page' exposed filter will never be saved.


Contextual link "Order view"
============================

If there is view with sort order draggableviews weight and the order is set by another view we show "Order view"
contextual link for opening a view that sets the order.


Troubleshooting Drag n' drop Not Showing
========================================
1. Make sure JavaScript is turned on and loading property.  Double check your source code.  For tables (D7) its <root>/misc/tabledrag.js.
2. Make sure you have draggableviews permission for the correct role.
3. Select 'show row weights'.  By default, this is located at the top right of the table. See http://drupal.org/files/draggableviews-1978526-hode-row-weights.png" for a visual image.
4. 'Show row weights' is a global variable/setting.  If you turn it off for 1 table, then all tables, across all pages, across all users, will not see it.  To fix this in the UI, you have to 'hide row weights' on another page/table, such as admin/structure/block (D7) or admin/build/block (D6), or go into the variables table in the database.
-- SUMMARY --

As the name implies, Block Refresh is a module that lets administrators configure all
or some of their blocks to be refresh, either by an defined number of seconds or by providing
a link for the website user to click on to refresh content, or both options on the same block.

To submit bug reports and feature suggestions, or to track changes:
  http://drupal.org/project/issues/block_refresh


-- REQUIREMENTS --

None.


-- INSTALLATION --

* Install as usual, see http://drupal.org/node/70151 for further information.


-- CONFIGURATION --

* Once installed, go to admin/structure/block
* Select 'configure' next to the block you want to setup with Block Refresh
* In the configuration window there will be a section for Block Refresh settings.
* Set the settings that you want to apply to the block (Block Refresh settings
  and any others) and click "Save Block"

** NOTE: Make sure and set the 'access block refresh content' permission for the roles
         you want to be able to see the block refresh. If the user does not have the
         permission required, the block will appear as though it was not configured with
         Block Refresh.


--  TROUBLESHOOTING --

* Use the included 'Block Refresh Demo' module to test functionality.
* If block are refreshing strangely on taxonomy/term/xx pages and you are
running the Global Redirect module, disable the 'taxonomy term path handler'
feature on that module's configuration page.

-- CONTACT --

Current maintainers:
* Phil Dodd (tripper54) - http://drupal.org/user/452964# Media Filepicker.io - Integrate the Filepicker.io file selector into your site

## Description

Ever wanted to let users easily import picture from Facebook, or files from Dropbox, without having to deal with 10 different REST APIs and oAuth implementations?  Filepicker.io (https://www.filepicker.io/) lets you connect your site from everything from Dropbox to Gmail.  

This module lets you Adds a Filepicker.io tab to the media dialog so that you can easily browse images from  the Media Selector widget or your WYSIWYG editor.  After you have selected your image, you it is copied over to your Files directory so you can still apply Drupal file styles and access control.

The following services are currently supported by Filepicker.io (https://developers.filepicker.io/docs/web/#pick):
  - Box
  - Upload from Computer (via drag-and-drop)
  - Dropbox
  - Evernote
  - Facebook
  - Flickr
  - FTP
  - Github
  - Google Drive
  - SkyDrive
  - Picasa
  - Webdav
  - Gmail
  - Image Search
  - Instagram
  - URL
  - Video
  - Webcam


## Installation

Install as you would any other Drupal module:

1. Download the module and put it in sites/all/modules or sites/SITENAME/modules
2. Create an account on https://www.filepicker.io/
3. Go to admin/config/media/filepickerio and enter your Filepicker.io key and other customize the other settings
4. Enable Filepicker.io in your media field settings under "Enabled browser plugins"


## Who

Developed and maintained by Albatross Digital, http://www.albatrossdigital.com.  This module is currently not affiliated with Filepicker.io

Solr search
-----------

This module provides an implementation of the Search API which uses an Apache
Solr search server for indexing and searching. You can find detailed
instructions for setting up Solr in the module's handbook [1].

[1] https://www.drupal.org/node/1999280

Supported optional features
---------------------------

All Search API datatypes are supported by using appropriate Solr datatypes for
indexing them. By default, "String"/"URI" and "Integer"/"Duration" are defined
equivalently. However, through manual configuration of the used schema.xml this
can be changed arbitrarily. Using your own Solr extensions is thereby also
possible.

The "direct" parse mode for queries will result in the keys being directly used
as the query to Solr. For details about Lucene's query syntax, see [2]. There
are also some Solr additions to this, listed at [3]. Note however that, by
default, this module uses the dismax query handler, so searches like
"field:value" won't work with the "direct" mode.

[2] http://lucene.apache.org/java/2_9_1/queryparsersyntax.html
[3] http://wiki.apache.org/solr/SolrQuerySyntax

Regarding third-party features, the following are supported:

- search_api_autocomplete
  Introduced by module: search_api_autocomplete
  Lets you add autocompletion capabilities to search forms on the site. (See
  also "Hidden variables" below for Solr-specific customization.)
- search_api_facets
  Introduced by module: search_api_facetapi
  Allows you to create facetted searches for dynamically filtering search
  results.
- search_api_facets_operator_or
  Introduced by module: search_api_facetapi
  Allows the creation of OR facets.
- search_api_mlt
  Introduced by module: search_api_views
  Lets you display items that are similar to a given one. Use, e.g., to create
  a "More like this" block for node pages.
  NOTE: Due to a regression in Solr itself, "More like this" doesn't work with
  integer and float fields in Solr 4. As a work-around, you can index the fields
  (or copies of them) as string values. See [4] for details.
  Also, MLT with date fields isn't currently supported at all for any version.
- search_api_multi
  Introduced by module: search_api_multi
  Allows you to search multiple indexes at once, as long as they are on the same
  server. You can use this to let users simultaneously search all content on the
  site – nodes, comments, user profiles, etc.
- search_api_spellcheck
  Introduced by module: search_api_spellcheck
  Gives the option to display automatic spellchecking for searches.
- search_api_data_type_location
  Introduced by module: search_api_location
  Lets you index, filter and sort on location fields. Note, however, that only
  single-valued fields are currently supported for Solr 3.x.
- search_api_grouping
  Introduced by module: search_api_grouping [5]
  Lets you group search results based on indexed fields. For further information
  see the FieldCollapsing documentation in the solr wiki [6].

If you feel some service option is missing, or have other ideas for improving
this implementation, please file a feature request in the project's issue queue,
at [7].

[4] https://drupal.org/node/2004596
[5] https://drupal.org/sandbox/daspeter/1783280
[6] http://wiki.apache.org/solr/FieldCollapsing
[7] https://drupal.org/project/issues/search_api_solr

Specifics
---------

Please consider that, since Solr handles tokenizing, stemming and other
preprocessing tasks, activating any preprocessors in a search index' settings is
usually not needed or even cumbersome. If you are adding an index to a Solr
server you should therefore then disable all processors which handle such
classic preprocessing tasks. Enabling the HTML filter can be useful, though, as
the default config files included in this module don't handle stripping out HTML
tags.

Clean field identifiers:
  If your Solr server was created in a module version prior to 1.2, you will get
  the option to switch the server to "Clean field identifiers" (which is default
  for all new servers). This will change the Solr field names used for all
  fields whose Search API identifiers contain a colon (i.e., all nested fields)
  to support some advanced functionality, like sorting by distance, for which
  Solr is buggy when using field names with colons.
  The only downside of this change is that the data in Solr for these fields
  will become invalid, so all indexes on the server which contain such fields
  will be scheduled for re-indexing. (If you don't want to search on incomplete
  data until the re-indexing is finished, you can additionally manually clear
  the indexes, on their Status tabs, to prevent this.)

Hidden variables
----------------

- search_api_solr_autocomplete_max_occurrences (default: 0.9)
  By default, keywords that occur in more than 90% of results are ignored for
  autocomplete suggestions. This setting lets you modify that behaviour by
  providing your own ratio. Use 1 or greater to use all suggestions.
- search_api_solr_index_prefix (default: '')
  By default, the index ID in the Solr server is the same as the index's machine
  name in Drupal. This setting will let you specify a prefix for the index IDs
  on this Drupal installation. Only use alphanumeric characters and underscores.
  Since changing the prefix makes the currently indexed data inaccessible, you
  should change this vairable only when no indexes are currently on any Solr
  servers.
- search_api_solr_index_prefix_INDEX_ID (default: '')
  Same as above, but a per-index prefix. Use the index's machine name as
  INDEX_ID in the variable name. Per-index prefixing is done before the global
  prefix is added, so the global prefix will come first in the final name:
  (GLOBAL_PREFIX)(INDEX_PREFIX)(INDEX_ID)
  The same rules as above apply for setting the prefix.
- search_api_solr_http_get_max_length (default: 4000)
  The maximum number of bytes that can be handled as an HTTP GET query when
  HTTP method is AUTO. Typically Solr can handle up to 65355 bytes, but Tomcat
  and Jetty will error at slightly less than 4096 bytes.
- search_api_solr_cron_action (default: "spellcheck")
  The Search API Solr Search module can automatically execute some upkeep
  operations daily during cron runs. This variable determines what particular
  operation is carried out.
  - spellcheck: The "default" spellcheck dictionary used by Solr will be rebuilt
  so that spellchecking reflects the latest index state.
  - optimize: An "optimize" operation [8] is executed on the Solr server. As a
  result of this, all spellcheck dictionaries (that have "buildOnOptimize" set
  to "true") will be rebuilt, too.
  - none: No action is executed.
  If an unknown setting is encountered, it is interpreted as "none".
- search_api_solr_site_hash (default: random)
  A unique hash specific to the local site, created the first time it is needed.
  Only change this if you want to display another server's results and you know
  what you are doing. Old indexed items will be lost when the hash is changed
  and all items will have to be reindexed. Can only contain alphanumeric
  characters.
- search_api_solr_highlight_prefix (default: "tm_")
  The prefix of Solr fields for which field-level highlighting will be enabled.
  Since the prefix of fields is used to determine the field type (by default),
  this lets you enable highlighting for other field types. By default,
  highlighting will be possible for all fulltext fields.

[8] http://wiki.apache.org/solr/UpdateXmlMessages#A.22commit.22_and_.22optimize.22

Customizing your Solr server
----------------------------

The schema.xml and solrconfig.xml files contain extensive comments on how to
add additional features or modify behaviour, e.g., for adding a language-
specific stemmer or a stopword list.
If you are interested in further customizing your Solr server to your needs,
see the Solr wiki at [9] for documentation. When editing the schema.xml and
solrconfig.xml files, please only edit the copies in the Solr configuration
directory, not directly the ones provided with this module.

[9] http://wiki.apache.org/solr/

You'll have to restart your Solr server after making such changes, for them to
take effect.

Developers
----------

The SearchApiSolrService class has a few custom extensions, documented with its
code. Methods of note are deleteItems(), which treats the first argument
differently in certain cases, and the methods at the end of service.inc.

Job Scheduler
=============

Simple API for scheduling tasks once at a predetermined time or periodically at
a fixed interval.


Usage
=====

Declare scheduler.

  function example_cron_job_scheduler_info() {
    $schedulers = array();
    $schedulers['example_unpublish'] = array(
      'worker callback' => 'example_unpublish_nodes',
    );
    return $schedulers;
  }

Add a job.

  $job = array(
    'type' => 'story',
    'id' => 12,
    'period' => 3600,
    'periodic' => TRUE,
  );
  JobScheduler::get('example_unpublish')->set($job);

Work off a job.

  function example_unpublish_nodes($job) {
    // Do stuff.
  }

Remove a job.

  $job = array(
    'type' => 'story',
    'id' => 12,
  );
  JobScheduler::get('example_unpublish')->remove($job);

Optionally jobs can declared together with a schedule in a hook_cron_job_scheduler_info().

  function example_cron_job_scheduler_info() {
    $schedulers = array();
    $schedulers['example_unpublish'] = array(
      'worker callback' => 'example_unpublish_nodes',
      'jobs' => array(
         array('type' => 'story', 'id' => 12, 'period' => 3600, 'periodic' => TRUE),
      )
    );
    return $schedulers;
  }

Jobs can have a 'crontab' instead of a period. Crontab syntax are Unix-like formatted crontab lines.
Example of job with crontab.

  // This will create a job that will be triggered from monday to friday, from january to july, every two hours
  function example_cron_job_scheduler_info() {
    $schedulers = array();
    $schedulers['example_unpublish'] = array(
      'worker callback' => 'example_unpublish_nodes',
      'jobs' => array(
         array('type' => 'story', 'id' => 12, 'crontab' => '0 */2 * january-july mon-fri', 'periodic' => TRUE),
      )
    );
    return $schedulers;
  }

Read more about crontab syntax, http://linux.die.net/man/5/crontab

Drupal Queue integration
========================

Optionally, at the scheduled time Job Scheduler can queue a job for execution,
rather than executing the job directly. This is useful when many jobs need to
be executed or when the job's expected execution time is very long.

More information on Drupal Queue: http://api.drupal.org/api/group/queue/7

Instead of declaring a worker callback, declare a queue name.

  function example_cron_job_scheduler_info() {
    $schedulers = array();
    $schedulers['example_unpublish'] = array(
      'queue name' => 'example_unpublish_queue',
    );
    return $schedulers;
  }

This of course assumes that you have declared a queue. Notice how in this
pattern the queue callback contains the actual worker callback.

  function example_cron_queue_info() {
    $schedulers = array();
    $schedulers['example_unpublish_queue'] = array(
      'worker callback' => 'example_unpublish_nodes',
    );
    return $schedulers;
  }


Work off a job: when using a queue, Job Scheduler reserves a job for one hour
giving the queue time to work off a job before it reschedules it. This means
that the worker callback needs to reset the job's schedule flag in order to
allow renewed scheduling.

  function example_unpublish_nodes($job) {
    // Do stuff.
    // Set the job again so that its reserved flag is reset.
    JobScheduler::get('example_unpublish')->set($job);
  }

Example
=======

See Feeds module.


Hidden settings
===============

Hidden settings are variables that you can define by adding them to the $conf
array in your settings.php file.

Name:        'job_scheduler_class_' . $name
Default:     'JobScheduler'
Description: The class to use for managing a particular schedule.
Drupal Module: Job Scheduler Trigger
====================================
Extension for Job Scheduler to create timed periodic triggers.

This module provides a simple UI to configure trigger name and crontab. We provide no actions, though actions created
by other modules can be set to be triggered with these timers.

Trigger type: job_scheduler
Hook names will be created on the fly for configured triggers as: job_scheduler_1, job_scheduler_2, etc...

Jose A. Reyero, http://www.developmentseed.org

This filter makes it easy to resize images, especially when combined with a
WYSIWYG editor such as tinyMCE or FCKeditor. Users never have to worry about
scaling image sizes again, just insert an image and set it's height and width
properties in HTML and the image is resized on output.

Author: Nathan Haug (quicksketch)

This module Built By Robots: http://www.lullabot.com.

Dependencies
------------
 * Drupal 6 or 7

Install
-------
1) Place the entire image_resize_filter directory in sites/all/modules. Then
   enable the module in Drupal.

2) Visit the Adminsiter->Configuration->Content authoring->text formats
   (admin/config/content/formats). Click "configure" next to the text format you
   want to enable the image resize filter on.

3) Check the box for "Image resize filter" under the list of filters.

4) IMPORTANT: Re-order your enabled filters under "Filter processing order".

   If using the Image Resize Filter on the "Filtered HTML" text format, you
   MUST ensure A) that the <img> tag is in the list of allowed tags and B) The
   "Image resize filter" is run BEFORE the "HTML filter".

   If using the Image Resize Filter with BBCode or some other non-HTML filter,
   the "Image resize filter" must be run AFTER the BBCode filter. If using
   Pathologic (http://drupal.org/project/pathologic), Image Resize Filter must
   be run AFTER the Pathologic filter too, since Pathologic must correct image
   path locations for Image Resize Filter to find the images.

5) Optional. Click the Image resize filter tab underneath "Filter settings" to
   set additional configuration for the the image resize filter.

Identifying problems
--------------------
It is important to understand that Image Resize Filter has absolutely no effect
on the content creation form. If you are having trouble resizing an image in a
WYSIWYG or editing a piece of content, DO NOT file an issue with Image Resize
Filter. This module is only responsible for the display of output and has
absolutely no effect on editing or creating new content.

Support
-------
If you experience a problem with Image Resize Filter, file a request or issue in
the Image Resize Filter queue at
http://drupal.org/project/issues/image_resize_filter.
DO NOT POST IN THE FORUMS. Posting in the issue queues is a direct line of
communication with the module authors.
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
    ____  _            __               _____       _ __     
   / __ \(_)________  / /___ ___  __   / ___/__  __(_) /____ 
  / / / / / ___/ __ \/ / __ `/ / / /   \__ \/ / / / / __/ _ \
 / /_/ / (__  ) /_/ / / /_/ / /_/ /   ___/ / /_/ / / /_/  __/
/_____/_/____/ .___/_/\__,_/\__, /   /____/\__,_/_/\__/\___/ 
            /_/            /____/                            

Display Suite gives you full control over the way content is displayed without
having to maintain dozens of PHP template files.
Read more: http://drupal.org/node/644662

-- GETTING STARTED --

1. Install Display Suite in the usual way (http://drupal.org/node/895232)
2. Go to Administration > Structure > Display Suite > Layout
   (admin/structure/ds/layout)
3. Click "Manage display" for the entity (e.g., "User") whose display you like
   to change
4. In the vertical tab "Layout for ... in default" choose the desired layout
   template (e.g. "Two column stacked") and click "Apply"
5. Start managing the display by dragging fields to regions
6. Click "Save"
Read more: http://drupal.org/node/1795282

-- CHANGES IN DISPLAY SUITE 7.x-2.x ---

Display Suite 7.x-2.x introduces many changes in comparison to 7.x-1.x. Among
them are:
* Improved UI
* HTML5 support
* Panel views mode removed from Display Suite
* Manage display of forms

Do not upgrade an existing site from 7.x-1.x to 7.x-2.x. Some functionality has
been changed, especially on the template level.

Read more: http://drupal.org/node/1524800

-- LINKS --

Project page: http://drupal.org/project/ds
Documentation: http://drupal.org/node/644662
Screencastst & articles: http://drupal.org/node/644706
Submit bug reports, feature suggestions: http://drupal.org/project/issues/ds

-- MAINTAINERS --

swentel - http://drupal.org/user/107403
stalski - http://drupal.org/user/322618
zuuperman - http://drupal.org/user/361625
jyve - http://drupal.org/user/591438
aspilicious - http://drupal.org/user/172527

-- INSPIRATORS --

mzenner - http://drupal.org/user/35077
Wimmmmm - http://drupal.org/user/34940
Use this example layout template and configuration as a starting point for your
own, custom Display Suite layouts.

The extras module contains functionality that is not often used. It holds
following functionality:

 - switch view modes: switch view mode on a per node basis.
 - block region: add regions which will be exposed as blocks.
 - extra fields: expose extra fields defined by other modules.
 - field permissions: add view permissions on DS fields.
 - Flag: expose flags as fields
 - Hidden region: region which in case it has fields will not be printed.
 - field templates: overwrite any field with custom markup.
 - switch view mode field: switch from one view mode to another inline.
 - page title options: hide the page title or manually set (with substitutions).
 - contextual links: add the 'manage display' link to contextual links 
   and on the full page view of nodes, users and terms.
 - Views displays: render views (row fields) into a different layout.
     Important: If you are creating new ds fields for vd,
     check ds_vd_render_title_field() how to return the content.
 
Any other functionality will be included in this module.Views Bulk Operations augments Views by allowing bulk operations
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
This simple module makes it easy to include the Typekit library on your site. You will have to have an account at Typekit (http://typekit.com/).


Installation
==================
* Regular module installation process.
* Go to admin/config/user-interface/typekit to put in your "key"
  and determine how you want Typekit to show up.



Author(s)
==================
zzolo (http://drupal.org/user/147331)
jpamental (http://drupal.org/user/174960)ABOUT
================================================================================

The goal of the Translation Template Extractor project is to provide 
command line and web based Gettext translation template extractor 
functionality for Drupal. These translation templates are used by 
teams to translate Drupal to their language of choice. There are 
basically two ways to use the contents of this project:

 * Copy potx.inc and potx-cli.php to the directory you would like to 
   generate translation templates for and run php potx-cli.php. 
   The translation templates will get generated in the current 
   directory.

 * Install the module on a Drupal site as you would with any other 
   module. Once potx module is turned on, you can go to the 
   "Extract" tab on the "Translate interface" administration interface, select 
   the module or modules or theme or themes you want to have a translation
   template for, and submit the form. You will get one single template file
   generated.

   Note: If you only get a white browser screen as response to the 
   extraction request, the memory limit for PHP on the server is probably 
   too low, try to set that higher.

The module also includes optional Coder (http://drupal.org/project/coder)
integration, allowing you to spot translatability errors in modules while
doing your regular code review.

USING potx-cli.php ON THE COMMAND LINE
================================================================================

Translation templates can easily be created by running the potx-cli.php
script on all source files that contain translatable strings.

  1. Copy the potx-cli.php and potx.inc to whatever folder you
     would like to generate template files in.
  2. Run 'php potx-cli.php' and the script will autodiscover
     all possible files to generate templates for.
  3. Translation templates are generated in this folder, if you
     have the proper rights to create files here.
     
You can try 'php potx-cli.php --help' to get a list of more options.
  
The contents of files depend on the mode you use. By default, one
single general.pot file will be generated. You can use the "core"
mode to generate Drupal core templates (one file per directory, repeated
usage of the same string in multiple directories folded into general.pot,
.info files folded into general.pot). Or you can use the "multiple" mode
which is similar to the "core" mode, but .info files are folded into
their module template files.

In case of "core" and "multiple" mode, the generated general.pot will
contain strings that occur more than once in the source files. This will help 
translators to maintain a single translation for them. 

CREDITS
================================================================================

Command line extractor functionality orignally by 
  Jacobo Tarrio <jtarrio [at] alfa21.com> (2003, 2004 Alfa21 Outsourcing)

Greatly optimized by 
  Brandon Bergren (2007)

Currently maintained by 
  Gabor Hojtsy <gabor [at] hojtsy.hu>

The Migrate module provides a flexible framework for migrating content into Drupal 
from other sources (e.g., when converting a web site from another CMS to Drupal). 
Out-of-the-box, support for creating Drupal nodes, taxonomy terms, comments, and 
users are included. Plugins permit migration of other types of content.

Usage
-----
Documentation is at http://drupal.org/migrate. To get started, enable the
migrate_example module and browse to admin/content/migrate to see its dashboard.
The code for this migration is in migrate_example/beer.inc (advanced examples are
in wine.inc). Mimic that file in order to specify your own migrations. 

The Migrate module itself has support for migration into core objects. Support
for migration involving contrib modules is in the migrate_extras module. 

Known issues
------------
A user migration with systemOfRecord == DESTINATION will drop pictures from user
records due to core bug http://drupal.org/node/935592 - the simpletests report an
error reflecting this. We have not developed a work-around.

Upgrading
---------
Do not attempt to upgrade directly from Migrate 1 to Migrate 2! There is no
automated path to upgrade - your migrations (formerly known as "content sets")
must be reimplemented from scratch. It is recommended that projects using
Migrate 1 stay with Migrate 1, and that Migrate 2 be used for any new migration
projects.

Acknowledgements 
----------------
Much of the Migrate module functionality was sponsored by Cyrve, for its clients GenomeWeb 
(http://www.genomeweb.com), The Economist (http://www.economist.com), and Examiner.com 
(http://www.examiner.com). 

Authors
-------
Mike Ryan - http://drupal.org/user/4420
Moshe Weitzman - http://drupal.org/user/23
An example migration from comma separated value files into Drupal nodes. Also a
good example of a DynamicMigration (i.e. the same migration class handles
multiple migrations).

We currently depend on Features module just for easy export of a content type.

The data comes from http://www.retrosheet.org/gamelogs/index.html:

The information used here was obtained free of charge from and is copyrighted by
Retrosheet.  Interested parties may contact Retrosheet at "www.retrosheet.org".

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
About
=====
Integrates the FlexSlider library into Drupal.

Known Issues
------------

- IE10 requires an updated version of jQuery to work properly with FlexSlider. Please see http://drupal.org/project/jquery_update

Current Options
---------------
Allows you to use FlexSlider in a few different ways

- As a library to be used with any other theme or module by calling flexslider_add() (N.B. You may also use libraries_load('flexslider') or drupal_add_library('flexslider', 'flexslider'), but only if you want to control everything manually).
- Integrates with Fields (flexslider_fields)
- Adds a Views display mode (flexslider_views)

About FlexSlider
----------------

Library available at https://github.com/woothemes/FlexSlider

- Simple, semantic markup
- Supported in all major browsers
- Horizontal/vertical slide and fade animations
- Multiple slider support, Callback API, and more
- Hardware accelerated touch swipe support
- Custom navigation options
- Use any html elements in the slides
- Built for beginners and pros, alike
- Free to use under the MIT license

Installation
============

Dependencies
------------

- [Libraries API 2.x](http://drupal.org/project/libraries)
- [FlexSlider Library](https://github.com/woothemes/FlexSlider)

Tasks
-----

1. Download the FlexSlider library from https://github.com/woothemes/FlexSlider
2. Unzip the file and rename the folder to "flexslider" (pay attention to the case of the letters)
3. Put the folder in a libraries directory
    - Ex: sites/all/libraries
4. The following files are required (last file is required for javascript debugging)
    - jquery.flexslider-min.js
    - flexslider.css
    - jquery.flexslider.js
5. Ensure you have a valid path similar to this one for all files
    - Ex: sites/all/libraries/flexslider/jquery.flexslider-min.js

That's it!

Drush Make
----------

You can also use Drush Make to download the library automatically. Simply copy/paste the 'flexslider.make.example' to 'flexslider.make' or copy the contents of the make file into your own make file.

Usage
======

Option Sets
-----------

No matter how you want to use FlexSlider (with fields or views) you need to define "option sets" to tell FlexSlider how you want it to display. An option set defines all the settings for displaying the slider. Things like slide direction, speed, starting slide, etc... You can define as many option sets as you like and on top of that they're all exportable! Which means you can carry configuration of your Flex Slider instances from one site to the next or create features.

Go to admin/config/media/flexslider

From there you can edit the default option set and define new ones. These will be listed as options in the various forms where you setup FlexSlider to display.  NOTE: under advanced options, you can set a namespace prefix for the optionset.  This will allow you to build custom CSS for each optionset.  Start by copying the flexslider_img.css from the assets subfolder to your theme.  Build new custom CSS for each prefix in your optionsets.

Carousels
---------

Carousels can be created with Flexslider2 by setting an Item Width for images and a Margin Width in the optionset.  Use the flexslider_thumbnail image style and set your item width to fit the desired number of images into the div space available.  NOTE: the margin width setting should correspond IN PIXELS to the margin widths set by your img CSS in your theme.  This will allow Flexslider to properly calculate the "total width" of the image+margins so that horizontal scrolling behaves properly.

Flexslider Views
----------------

Flex Slider Views allows you to build views which display their results in Flex Slider. Similarly to how you can output fields as an "HTML List" or "Table", you can now select "Flex Slider" as an option.

Create or edit a view and ensure it can load a content type which contain image fields. Set your display fields to include an image field. In the field settings, DO NOT SET THE FORMATTER TO FLEXSLIDER. This will attempt to put Flex Sliders inside other Flex Sliders and will just get messy. Ensure you don't include any wrapper markup, labels or container markup for the field value itself. Save your field.

Next, go to "Format" in the main Views windows. Click and select "Flex Slider", then select your option set. Save your view and you should see your results displayed in Flex Slider.

Debugging
---------

You can toggle the development version of the library in the administrative settings page. This will load the unminified version of the library.  Uncheck this when moving to a production site to load the smaller minified version.

### Image Width/Height Attributes

If your images aren't resizing, ensure the width and height attributes are removed. The module will attempt to remove them automatically on any image matching the pattern 

    ul.slides > li > img
    


Export API
==========

You can export your FlexSlider option presets using CTools exportables. So either using the Bulk Export module or Features.

External Links
==============

- [Wiki Documentation for FlexSlider 2](https://github.com/woothemes/FlexSlider/wiki/FlexSlider-Properties)FlexSlider Example
==================

Contains sample configurations for FlexSlider. You can use these as a starting point for creating your own FlexSlider configurations.

Dependencies
------------

- FlexSlider Views
- FlexSlider Fields
- FlexSlider
- ContextAbout
=====

Adds a field display formatter to allow you to display field content using FlexSlider. The module doesn't require Field UI to be enabled by default (so you can leave it off once everything is configured) but it is recommended to use to setup your display settings.

Usage
=====

Manage the fields on any entity (ex: node of type Article)

Ex: admin/structure/types/manage/article

Select any field of type "image" or "media" and set the display options to "FlexSlider". Then select your option set in the display formatter settings. That's it!

About
=====

This adds a new display style to views called "FlexSlider". Similar to how you select "HTML List" or "Unformatted List" as display styles.

This module doesn't require Views UI to be enabled but it is required if you want to configure your Views display using FlexSlider through the web interface. This ensures you can leave Views UI off once everything is setup.

Usage
=====

Go to Views andUse the display mode "FlexSlider"
Summary
=======
Multistep adds multiple-step functionality to node type editing forms. It does
so by assigning a step number to each field or field group within the node type
and hiding all the fields or groups that do not belong to the current step. The
user can then use different submitting buttons that will redirect to the
previous, next, or current step.

The module also provides a block for each node type with a menu of the
different groups within that form and a progress bar. This provides an easy way
to jump to different steps throughout the form without having to go one by one
as well as keeping track of the progress of the form.

For a full description visit the project page:
  http://drupal.org/project/multistep
  
Bug reports, feature suggestions and latest developments:
  http://drupal.org/project/issues/multistep

Requirements
============
This module requires Fields, which is part of Drupal core. It also benefits
strongly from Field group, which can be found here:
  http://drupal.org/project/field_group

To Use
======
To use this module, go into the node type editing form in Structure >> Content
types and select the content type you want to enable Multistep for.
  
There will be a collapsed Multistep Form section below, mark it as Enabled and
enter the amount of steps that you want this form to span.
  
Now, whenever you add or edit a group (or a field that does not belong to any
group), you will be able to select which step that group belongs to. The group
will only be shown when in that step, or in all of them if All is selected as
an option.

If you are configuring multistep for a content type that already had data
previously, you should go to Configuration >> Multistep and reset the table for
that node type. This will create step data for all nodes that were previously
created.

If you have a Taxonomy vocabulary set for the content type, you will see an
option to set which step it should belong to in the content type editing form
after you save the number of steps.

Configuration
=============
To configure the multistep menu and the progress bar, go to Administer >> Site
building >> Blocks and configure the corresponding block that will appear on
the list. You can select whether to enable or disable the menu and the progress
bar.

To remove/show the Preview button on the node editing form, go to the content
type editing form in Administer >> Content management >> Content types and
check/uncheck the box that says "Hide Preview button".

To change the text that appears on the different buttons of the form (Previous,
Next, Save, Done), go to the admin settings page in Administer >> Site
configuration >> Multistep and modify the values shown in the Navigation button
labels section.

Users with "toggle multistep" permission can select whether to view the entire
form in a single page or the multistep form split over multiple pages. This is
useful for vieweing a whole form at a glance before starting to enter the data.

You can also set whether the default display of the form is the multistep form
or the entire form. Only users with "toggle multistep" permissions will be able
to switch displays.

Development
===========
For hooks provided by Multistep, read multistep.api.php

If you create a module that defines fieldsets for CCK, you have to implement
hook_content_extra_fields(). See http://drupal.org/node/901420 for information
on how to implement this specific hook.

Credits
=======
Author: Victor Kareh (vkareh) - http://www.vkareh.net
ADDING MENU BLOCKS
------------------

To add new menu blocks, use the "Add menu block" link on the administer blocks
page, admin/structure/block. You will then be able to configure your menu block
before adding it.


CONFIGURING MENU BLOCKS
-----------------------

When adding or configuring a menu block, several configuration options are
available:

Basic Options:

Block title
  For menu trees that start with the 1st level, the default block title will be
  the menu name. For menu trees that start with the 2nd level or deeper, the
  default block title will be the title for the parent menu item of the
  specified level.

  For example, if the active menu trail for the Management menu is: Administer >
  Structure > Menus > Main menu, then a menu block configured to start with the
  1st level of the Management menu will display a block title of "Management".
  And a menu block configured to start with the 3rd level of the Management menu
  will display a block title of "Structure".

Block title as link
  For menu trees that start with the 2nd level or deeper, the default block
  title will be the title for the parent menu item of the specified level. If
  this option is checked, the block title will be a link to that menu item.

Administrative title
  To help identify the block on the administer blocks page, you can specify a
  unique title to be used on that page. If blank, the regular title will be
  used.

Menu name
  Select the menu to use for the tree of links.

Starting level
  Blocks that start with the 1st level will always be visible. Blocks that start
  with the 2nd level or deeper will only be visible when the trail to the active
  menu item is in the block's tree.

Maximum depth
  From the starting level, specify the maximum depth of the tree. Blocks with a
  maximum depth of 1 will just be a single un-nested list of links with none of
  those links' children displayed.

Advanced options:

Make the starting level follow the active menu item
  If the active menu item is deeper than the level specified above, the starting
  level will follow the active menu item. Otherwise, the starting level of the
  tree will remain fixed.

Expand
  All children of this menu will be expanded.

Sort
  Sort each item in the active trail to the top of its level. When used on a
  deep or wide menu tree, the active menu item's children will be easier to see
  when the page is reloaded.

Fixed parent item
  If you select a specific menu item, you alter the "starting level" and
  "maximum depth" options to be relative to the fixed parent item. The tree of
  links will only contain children of the selected parent item.


STYLING MENU BLOCKS
-------------------

Classes:

Themers should look at the myriad of classes added to the <div>, <li> and <a>
elements.

<div>
  The <div> wrapped around the menu tree has a class for several of the
  configurable options of the block: menu-block-[block id number]
  menu-name-[menu name] parent-mlid-[menu link ID] menu-level-[level number]

<li>
  The <li> elements of the menu tree can have an extended list of classes
  (compared to standard menu trees): first last menu-mlid-[menu link ID]
  has-children active active-trail

<a>
  The <a> elements of the menu tree can have: active active-trail

Templates:

In addition, the wrapper <div> for the block is generated using the
menu-block-wrapper.tpl.php template. And Menu block provides several theme hook
suggestions for that template:
- menu-block-wrapper--[block id number].tpl.php
- menu-block-wrapper--[menu name].tpl.php

For example, a file in your theme called
menu-block-wrapper--main-menu.tpl.php can be used to override the <div> for
just the "Primary links" menu blocks.

Theme functions:

Menu block uses Drupal core's menu theme functions. However, it also provides
theme hook suggestions that can be used to override any of the theme functions
called by it.

- theme_menu_tree() can be overridden by creating one of:
  - [theme]_menu_tree__[menu name]()
  - [theme]_menu_tree__menu_block()
  - [theme]_menu_tree__menu_block__[menu name]()
  - [theme]_menu_tree__menu_block__[block id number]()

- theme_menu_link() can be overridden by creating one of:
  - [theme]_menu_link__[menu name]()
  - [theme]_menu_link__menu_block()
  - [theme]_menu_link__menu_block__[menu name]()
  - [theme]_menu_link__menu_block__[block id number]()

For example, if you created a bartik_menu_tree__menu_block() function, it would
override theme_menu_tree() any time it was used by this module, but not when
used by any other module. Similarly, a bartik_menu_link__menu_block__1()
function would override theme_menu_link(), but only for the first menu block in
your system (the menu block with an ID of 1).


MENU BLOCK API
--------------

Developers can use the API of this module to create their own menu trees outside
the confines of blocks. All of the publicly available API functions are
documented in the menu_block.module file.

In addition, Menu block implements HOOK_menu_block_get_menus(),
HOOK_menu_block_get_sort_menus() and HOOK_menu_block_tree_alter(). See
menu_block.api.php for documentation.

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

  * As of now, the field collection field does not properly respect different
    languages of the host entity. Thus, for now it is suggested to only use the
    field for entities that are not translatable.[![Build Status](https://travis-ci.org/NuCivic/open_data_schema_map.svg?branch=master)](https://travis-ci.org/NuCivic/open_data_schema_map)

Open Data Schema Map
====================

This module provides a flexible way to expose your Drupal content via APIs following specific Open Data schemas. Currently, the [CKAN](http://docs.ckan.org/en/ckan-1.8/domain-model-dataset.html) and [Project Open Data schemas](http://project-open-data.github.io/schema/) are provided, but new schemas can be easily added through your own modules. A user interface is in place to create endpoints and map fields from the chosen schema to Drupal content using tokens.

DKAN-specific implementation: https://github.com/NuCivic/open_data_schema_map_dkan

## Basic concepts

### Schema
A schema is a list of field definitions, usually representing a community specification for presenting machine-readable data. The core Open Data Schema Map module does not include any schemas; they are provided by additional modules. A schema module includes:

* a standard Drupal .module file -- with an implementation of ```hook_open_data_schema()``` to expose the schema to the core Open Data Schema Map module, plus _alter functions for any needed modifications of the UI form or the data output itself.
* the schema itself, expressed as a .json file. For instance, see the [Project Open Data schema file](https://github.com/NuCivic/open_data_schema_map/blob/master/modules/open_data_schema_pod/data/single_entry.json) to see how these schema are defined in JSON


### API
An API in this module is a configuration set that exposes a specific set of machine-readable data at a specific URL (known as the API's endpoint). This module allows you to create multiple APIs that you save as database records and/or export using [Features](http://drupal.org/project/features). An API record will contain:

* an endpoint URL
* a schema (chosen from the available schemas provided by the additional modules as described above)
* a mapping of fields defined in that schema to Drupal tokens (usually referencing fields from a node)
* optionally, one or more arguments passed through the URL to filter the result set

## Usage

### Installation

Enable the main _Open Data Schema Map_ module as usual, and additionally enable any schema modules you will need to create your API.

### Creating APIs

Navigate to admin/config/services/odsm and click "Add API."

![screen shot 2014-07-14 at 3 24 03 pm](https://cloud.githubusercontent.com/assets/309671/3575902/c7ff24e6-0b8c-11e4-92c3-9ba2e163bf56.png)

Give the API a title, machine name, choose which entity type (usually _node_) and bundle (in [DKAN](https://github.com/NuCivic/dkan), this is usually _Dataset_).

![screen shot 2014-07-14 at 3 46 39 pm](https://cloud.githubusercontent.com/assets/309671/3576163/b3e6ea90-0b8f-11e4-9d9e-33b4515310f0.png)

You will need to create the API record before adding arguments and mappings.

### Arguments

The results of the API call can be filtered by a particular field via arguments in the URL. To add an argument, first choose the schema field then, if you are filtering by a custom field API field (ie, a field whose machine name begins with "field\_"), identify the database column that would contain the actual argument value. Leave off the field name prefix; for instance, if filtering by a DKAN tag (a term reference field), the correct column is field_tags_tid, so you would enter "tid". Which Drupal field to use will be extrapolated from the token you map to that schema field.

![Screen Shot 2014-07-14 at 3.55.49 PM.png | uploaded via ZenHub](https://cloud.githubusercontent.com/assets/512243/5281816/992d1138-7ac6-11e4-8e7b-bcaefa733648.png)

### Field Mapping

The API form presents you with a field for each field in your schema. Map the fields using Drupal's token system. Note: using more than one token in a single field may produce unexpected results and is not recommended. 

#### Multi-value fields

For Drupal multi-value entity reference fields, the schema can use an array to instruct the API to iterate over each value and map the referenced data to multiple schema fields. For instance, in the CKAN schema, tags are described like this in schema_ckan.json:

```    
      "tags": {
      "title":"Tags",
      "description":"",
      "anyOf": [
        {
          "type": "array",                    
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "title": "UUID",
                "type": "string"
              },
              "vocabulary_id": {
                "title": "Vocaulary ID",
                "type": "string"
              },
              "name": {
                "title": "Name",
                "type": "string"
              },
              "revision_timestamp": {
                "title": "Revision Timestamp",
                "type": "string"
              },
              "state": {
                "title": "state",
                "description": "",
                "type": "string",
                "enum": ["uncomplete", "complete", "active"]
              }
            }
          }
        }
      ]
    },
```

You can choose which of the available multivalue fields on your selected bundle to map to the "tags" array, exposing all of the referenced "tag" entities (taxonomy terms in this example) to use as the context for your token mappings on the schema fields within that array. First, simply choose the multivalue field, leaving the individual field mappings blank, and save the form.

![screen shot 2014-07-16 at 12 14 29 am](https://cloud.githubusercontent.com/assets/309671/3594511/c3ca9cd4-0c9f-11e4-8fd0-1ea7c3c8b2b3.png)

When you return to the tags section of the form after saving, you will now see a special token navigator you can use to find tokens that will work with this iterative approach (using "Nth" in place of the standard delta value in the token):

![screen shot 2014-07-16 at 12 22 00 am](https://cloud.githubusercontent.com/assets/512243/5281826/ad5e3eac-7ac6-11e4-8c7d-91076527c84d.png)

## Customizing

### Adding new schemas

You are not limited by the schemas included with this module; any Open Data schema may be defined in a custom module. Use the open_data_schema_ckan module as a model to get started.

### Using the xml output module

We've isolated xml output into its own module. A few reasons why:

+ It relies on a composer dependency
+ This module is distributed with dkan, a drupal installation profile, and we don't have a way of installing composer dependencies while building the distro with ```drush make```
+ We don't want to force all this trouble on users that just want ***json output*** 

Because of all this, if you still want to use xml output for your odsm endpoints (we don't judge), you need to:


+ Install composer dependencies:

```
$ cd modules/open_data_schema_map_xml_output
$ composer install
```

+ Enable module

```
$ drush -y en open_data_schema_map_xml_output
```

If you need instructions to install composer globally in your system please refer to https://getcomposer.org/doc/00-intro.md#globally.

### Date format
Date formats can be chanaged manually by changing the "Medium" date time format in "admin/config/regional/date-time" or in code by using one of the alter hooks:
![screen shot 2014-09-04 at 11 15 01 am](https://cloud.githubusercontent.com/assets/512243/4152408/a9cb06b2-344e-11e4-84c8-c2174b5fc566.png)

## Contributing

We are accepting issues in the dkan issue thread only -> https://github.com/NuCivic/dkan/issues -> Please label your issue as **"component: open_data_schema_map"** after submitting so we can identify problems and feature requests faster.

If you can, please cross-reference commits in this repo to the corresponding issue in the dkan issue thread. You can do that easily adding this text:

```
NuCivic/dkan#issue_id
``` 

to any commit message or comment replacing **issue_id** with the corresponding issue id.

# JSON Schema for PHP

[![Build Status](https://travis-ci.org/justinrainbow/json-schema.svg?branch=master)](https://travis-ci.org/justinrainbow/json-schema)
[![Latest Stable Version](https://poser.pugx.org/justinrainbow/json-schema/v/stable.png)](https://packagist.org/packages/justinrainbow/json-schema)
[![Total Downloads](https://poser.pugx.org/justinrainbow/json-schema/downloads.png)](https://packagist.org/packages/justinrainbow/json-schema)

A PHP Implementation for validating `JSON` Structures against a given `Schema`.

See [json-schema](http://json-schema.org/) for more details.

## Installation

### Library

    $ git clone https://github.com/justinrainbow/json-schema.git

### Dependencies

#### [`Composer`](https://github.com/composer/composer) (*will use the Composer ClassLoader*)

    $ wget http://getcomposer.org/composer.phar
    $ php composer.phar require justinrainbow/json-schema:~1.3

## Usage

```php
<?php

// Get the schema and data as objects
$retriever = new JsonSchema\Uri\UriRetriever;
$schema = $retriever->retrieve('file://' . realpath('schema.json'));
$data = json_decode(file_get_contents('data.json'));

// If you use $ref or if you are unsure, resolve those references here
// This modifies the $schema object
$refResolver = new JsonSchema\RefResolver($retriever);
$refResolver->resolve($schema, 'file://' . __DIR__);

// Validate
$validator = new JsonSchema\Validator();
$validator->check($data, $schema);

if ($validator->isValid()) {
    echo "The supplied JSON validates against the schema.\n";
} else {
    echo "JSON does not validate. Violations:\n";
    foreach ($validator->getErrors() as $error) {
        echo sprintf("[%s] %s\n", $error['property'], $error['message']);
    }
}
```

## Running the tests

    $ vendor/bin/phpunit
## POD Schema

Comes from https://github.com/GSA/project-open-data-dashboard/tree/master/schema
DESCRIPTION
-----------

This module uses the FitVids.js library for fluid width video embeds (e.g. flash video in <iframe>s). You don't need it for pure HTML5 videos.

It supports YouTube, Vimeo, Blip.tv and Kickstarter by default, and you should be able to use it with other video providers.

It's useful if you are using a responsive theme (such as Omega), and want the videos to scale.


CONFIGURATION
-------------

# jQuery selectors

You can usually use the defaults. It assumes that you'll want to apply it to all videos on the page. 

If your theme uses a different class or id, or you only want to target certain videos, you can specify that class/id in the video containers field. You can use any valid jQuery selector, e.g.,

~~~
#my-video-container
.content
body
~~~

You can specify as many containers as you want.


# Video providers

Not all players will work with FitVids, but you can try it out by adding the domain (in the Custom iframe URLs field).


REQUIREMENTS & INSTALLATION
---------------------------

Uses the Libraries API. 

You'll also need to download the jQuery plugin from https://raw.github.com/davatron5000/FitVids.js/master/jquery.fitvids.js before you can enable the module. 

Place it in the /sites/all/libraries/fitvids folder. 

Works best with jQuery 1.7 or above (use jquery_update or add a newer version to your theme manually), but you should be OK with the version that ships with Drupal.

/**
 *  @file
 *  README for the Media Module.
 */

See -https://www.drupal.org/documentation/modules/media

Site Building Guide ->
 \/ Media and files
    \/ Media 
- https://www.drupal.org/documentation/modules/media
     > Media Internet Sources
     . Media and file cleanup
     . Media: YouTube upload
     > Upgrading Media 7.x-1.x to 7.x-2.x
     . Using existing files (FTP uploads etc)
     . Media Installation and distributions
     . Media 2.x Quick Start Guide
     . Displaying Media
     . Media Library
     . Media Roadmap
     > Media Recipes (custom FORM, developer recipes)
     > Media Developer Documentation (Outdated)
     > Media FAQ (Outdated)
     . Media Vimeo Uploader  

items preceded with a '>' indicate more available media module documentation sub categories
Open Data Schema Map DKAN
=========================

Default Open Data Schema Map endpoints for DKAN. Includes CKAN and Project Open Data endpoints.

Includes the following endpoints:

#### Project Open Data
* data.json

#### CKAN
* ckan_package_show
* ckan_current_package_list_with_resources
* ckan_group_list
* ckan_group_package_show
* ckan_package_list
* ckan_package_show
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

        FORWARD MODULE - README
______________________________________________________________________________

NAME:       Forward
AUTHORS:    Drupal 7 version:
            John Oltman <john.oltman@sitebasin.com>

            Drupal 6 version:
            Sean Robertson <seanr@ngpsoftware.com>
            Peter Feddo
______________________________________________________________________________


DESCRIPTION

Adds a "forward this page" link to each node. This module allows users to
forward a link to a specific node on your site to a friend.  You can customize
the default form field values and even view a running count of the emails sent
so far using the forward module.


INSTALLATION

Step 1) Download latest release from http://drupal.org/project/forward

Step 2)
  Extract the package into your 'modules' directory.


Step 3)
  Enable the forward module.

  Go to "/admin/modules" and put a checkmark in the 'Enabled' column next to
  'Forward'.


Step 4)
  Go to "/admin/config/user-interface/forward" to configure the module.
  This path is also linked from the Configuration page and the Modules list
  page within site administration.

  If you wish to customize the emails, copy 'forward.tpl.php' into your theme
  directory. Then you can customize the function as needed and those changes
  will only appear when sent by a user using that theme.

  If you check the 'custom display' box on the configuration page, the Forward
  view mode which defines the fields that will be sent in Forward emails can
  be configured here:

  "/admin/structure/types/manage/[machine-name]/display/forward"

  where [machine-name] is replaced by the machine name of the content type
  being configured.

  For example, for articles, the full path to the link is:
  "/admin/structure/types/manage/article/display/forward"


Step 5)
  Enable permissions appropriate to your site.

  Go to "/admin/people/permissions#module-forward" to configure permissions.
  This path is also linked from the Modules list page, click on the 
  Permissions link next to Forward.

  The forward module provides several permissions:
   - 'access forward': allow user to forward pages.
   - 'access epostcard': allow user to send an epostcard.
   - 'override email address': allow logged in user to change sender address.
   - 'administer forward': allow user to configure forward.
   - 'override flood control': allow user to bypass flood control on send.

  Note that you need to enable 'access forward' for users who should be able
  to send emails using the forward module.


Step 6)
  Go to "/admin/reports/forward" to view forward usage statistics.
  There is also a link on the Reports page within site administration.

  Statistics are captured when emails are sent and when recipients click on
  links within the sent emails.

Step 7)
  If the Views module is enabled for your site, go to "admin/structure/views"
  to optionally enable and configure Forward related views:
  
  Most forwarded
  Most recently forwarded
  Most clickthroughs

Step 8)
  Go to "admin/structure/block" to optionally enable and configure Forward
  blocks for your theme.  Several blocks are available:

  Forward: Interface - places the forward link or forward form in a block
  Forward: Statistics - most recently emailed or most emailed of all time

  If you enabled views in step 7, these blocks are also available:

  View: Most forwarded
  View: Most recently forwarded
  View: Most clickthroughs


SENDING FORWARD EMAILS AS HTML

  By default, Forward will install a new mail system named ForwardMailSystem
  that is configured to send email as HTML. If you installed a different
  mail system module for sending emails, you should visit the Mail System
  configuration page at "admin/config/system/mailsystem" to change the mail
  system setup.  For example, if you installed the HTMLMail module, you could
  change the default site wide mail system to HTMLMailSystem. The Mail System
  module also allows you to use one mail system as a default but a different
  mail system on a module by module basis.  This would allow you to use a
  special mail handler for Forward emails while not affecting emails sent
  from the rest of your site.

 
THEMEING

Sent email   - copy forward.tpl.php into your theme and modify
Forward page - add yourtheme_forward_page($variables) to template.php
Forward link - add yourtheme_forward_link($variables) to template.php

Forward links generated using Panels, Display Suite or Views integration
are fully themeable. Forward links generated into the node inline links
render array are not directly themeable; to override these links you
can write a preprocess_node function. However, the ability to provide
a custom icon and any text for the links via the Forward configuration
page should make this unnecessary for most use cases.


TEMPLATES

Forward links can be hardcoded into your theme templates as needed:

print theme('forward_link', array('node' => $node)); // for nodes
print theme('forward_link', array('path' => $path)); // for non-nodes

However, the use of Display Suite or Panels is recommended instead of
writing PHP code.

  
VIEWS INTEGRATION

The Forward Log is now integrated with Views 3 for Drupal 7. You can create
a view with log data including users who forwarded, the forwarded path, the
data and time the forwarding occurred, and other information.

You can also add a Forward link if you are using fields as the row style.


DISPLAY SUITE INTEGRATION

Forward link is now a field that is available within DS layouts.


PANELS INTEGRATION

Forward link is now available when adding content to a panel, both as a
node field and also a widget. If your panel is working within a node context,
such as when overriding a standard node view with a panel, use the node
field instead of the widget.


DYNAMIC BLOCK ACCESS CONTROL

The 7.x-1.3 release of the Forward module added a new security field
for administators on the Forward configuration page named Dynamic Block
Access Control.  This field allows the administrator to control which
permissions are used when Drupal applies access control checks to the nodes,
comments or users listed in the Dynamic Block.  Several access control
options are available, including a bypass option.  The bypass option allows
the email recipient to possibly view node titles, comment titles, or user
names that only privileged users should see. The bypass option should not
normally be selected, but is provided for sites that used prior versions
of Forward and rely on the access bypass to operate correctly.

IMPORTANT: Because the default for the new field is to apply access control,
administrators of sites that rely on the access bypass to operate correctly
need to visit the Forward configuration page and explicitly select the bypass
option after upgrading from versions of Forward prior to 7.x-1.3.


CLICKTHROUGH COUNTER FLOOD CONTROL

The Forward module tracks clicks from links in sent emails to determine which
nodes get the most clickthroughs.  The method used could allow someone to
manipulate clickthrough counts via CSRF - for example, placing an image on
a website with a src tag that points to the clickthrough counter link.  The
module uses flood control to limit the number of clickthroughs from a given
IP address in a given time period to migitate this possibility.


CREDITS & SUPPORT

Special thanks to Jeff Miccolis of developmentseed.org for supplying the
tracking features and various other edits.  Thanks also to Nick White for his
EmailPage module, some code from which was used in this module, as well as the
numerous other users who have submitted issues and patches for forward.

All issues with this module should be reported via the following form:
http://drupal.org/node/add/project_issue/forward
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
TTR Configurable Widget
Author: Saemie Chouchane (saemchou on Drupal.org)
Sponsor: Microserve LTD (microserveltd.co.uk)

Overview:
-------------------

TTR Configurable Widget is a flexible, configurable widget 
for use with taxonomy term reference fields. 
By default users can choose between 'Select List' and 'Checkboxes' 
as the available widgets, whereas with with TTR Configurable Widget 
users are now able to choose additional, more advanced options.

Due to it's extensibility it is very easy for other developers to add 
further options. The module provides additional back-end options which 
allows users to filter and order taxonomy term options within a field 
and gives the admin control over how taxonomy term fields are listed 
in a form. Developers can then extend the widget by creating their own 
front-end variations which utilise this functionality.

Instructions:
-------------------
When creating or editing a taxonomy term field select 
the TTR Configurable Widget as the widget option.
You can then edit the widget settings that are located in the 
`TTR CONFIGURATION SETTINGS` fieldset.

You can choose to display a number of options or all options.

Option ordering will decide how options are listed on the node form.

Choose the `view type` depending on how you would like the options to
be displayed on the form. More view types can be added. By default there
are a `select list` choce and a `checkboxes/radio` one.
Try the Wordwall view type that is included in this module. This must be
enabled separately.
Word Wall module.
Author: Saemie Chouchane (saemchou on Drupal.org)
Sponsor: Microserve LTD (microserveltd.co.uk)

Overview:
-------------------
This module extends the TTR Configurable Widget module to add a `view type`.

How it works:
-------------------
Word Wall is simple to use. Simply click on the options you want to select. 
These will be highlighted. If there is a limit set of the number of chooseable 
values, the list will be frozen. To unselect an item simply click it again, 
if the list was frozen it will become unfrozen and the other options will 
become selectable again.

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
CONTENTS OF THIS FILE
---------------------

 * Description
 * Installation


Description
------------

The Range module defines various numeric range field types for the Field module.
Ranges can be in integer, decimal, or floating-point form, and they can be
formatted when displayed. Range fields can be limited to a specific set of input
values or to a range of values.


INSTALLATION
------------

Install as usual, see http://drupal.org/node/70151 for further information.
This module integrates the Plupload library (available from http://plupload.com)
with Drupal forms. To install the Plupload library:

1. Download it (version 1.5.1.1 or later) from http://plupload.com.
2. Unzip it into sites/all/libraries, so that there's a
   sites/all/libraries/plupload/js/plupload.full.js file, in addition to the
   other files included in the library.
3. Remove "examples" folder from libraries folder as it could constitute a
   security risk to your site. See http://drupal.org/node/1895328 and
   http://drupal.org/node/1189632 for more info.

If you would like to use an alternate library location, you can install the
http://drupal.org/project/libraries module and/or add

  $conf['plupload_library_path'] = PATH/TO/PLUPLOAD;

to your settings.php file.

At this time, this module only provides a 'plupload' form element type that
other modules can use for providing multiple file upload capability to their
forms. It does not provide any end-user functionality on its own. This may
change, however, as this module evolves. See http://drupal.org/node/880300.

---=== For developers ===---

Plupload from element can be used like this:

$form['my_element'] = array(
  '#type' => 'plupload',
  '#title' => t('Upload files'),
  '#description' => t('This multi-upload widget uses Plupload library.'),
  '#submit_element' => '#id-of-your-submit-element',
  '#upload_validators' => array(
    'file_validate_extensions' => array('jpg jpeg gif png txt doc xls pdf ppt pps odt ods odp'),
    'my_custom_file_validator' => array('some validation criteria'),
  );
  '#plupload_settings' => array(
    'runtimes' => 'html5',
    'chunk_size' => '1mb',
  ),
);

- #submit_element - optionally specify which submit element plupload shall use
  to submit the form. See: http://drupal.org/node/1935256

- #upload_validators - an array of validation function/validation criteria pairs, that
  will be passed to file_validate().

  Defaults to:
  '#upload_validators' => array(
    'file_validate_extensions' => array('jpg jpeg gif png txt doc xls pdf ppt pps odt ods odp'),
  );


- #plupload_settings - array of settings, that will be passed to Plupload library.
  See: http://www.plupload.com/documentation.php

  Defaults to:
  '#plupload_settings' => array(
    'runtimes' => 'html5,flash,html4',
    'url' => url('plupload-handle-uploads', array('query' => array('plupload_token' => drupal_get_token('plupload-handle-uploads')))),
    'max_file_size' => file_upload_max_size() . 'b',
    'chunk_size' => '1mb',
    'unique_names' => TRUE,
    'flash_swf_url' => file_create_url($library_path . '/js/plupload.flash.swf'),
    'silverlight_xap_url' => file_create_url($library_path . '/js/plupload.silverlight.xap'),
  ),
Database search
---------------

This module provides a database based implementation of the Search API. The
database and target to use for storing and accessing the indexes can be selected
when creating a new server.

All Search API datatypes are supported by using appropriate SQL datatypes for
their respective columns (with "String"/"URI", and "Integer"/"Duration" being
equivalent).

The "direct" parse mode for queries will result in a simple splitting of the
query string into keys. Additionally, search keys containing whitespace will be
split, as searching for phrases is currently not supported.

Supported optional features
---------------------------

- search_api_autocomplete
  Introduced by module: search_api_autocomplete
  Lets you add autocompletion capabilities to search forms on the site. (See
  also "Hidden variables" below for backend-specific customization.)
  NOTE: Due to internal database restrictions, this will perform significantly
  better if only a single field is used for autocompletion.
- search_api_facets
  Introduced by module: search_api_facetapi
  Allows you to create facetted searches for dynamically filtering search
  results.

If you feel some service option is missing, or have other ideas for improving
this implementation, please file a feature request in the project's issue queue,
at [http://drupal.org/project/issues/search_api], using the "Database search"
component.

Known problems
--------------

Currently, Drupal doesn't support setting the table collation when creating
tables. This might cause problems when you want to index data which can contain
accented characters, umlauts and other non-ASCII characters (à, á, ä, …).
To resolve the issue, please set "utf8_bin" as the collation for all tables
starting with "search_api_db_". This has already been automated for MySQL
databases in newer releases but must be done manually for other databases.
See [1] for details.

[1] http://drupal.org/node/1144620

Also, using facets with a database server will only work if the database user
Drupal is using has the "CREATE TEMPORARY TABLES" permission (or similar, in
DBMSs other than MySQL).

Developer information
---------------------

Database queries for searches with this module are tagged with
"search_api_db_search" to allow easy altering. As metadata, such database
queries will have the Search API query object set as "search_api_query", and the
field settings of the server for the corresponding search index as
"search_api_db_fields".

Hidden variables
----------------

- search_api_db_autocomplete_max_occurrences (default: 0.9)
  By default, keywords that occur in more than 90% of results are ignored for
  autocomplete suggestions. This setting lets you modify that behaviour by
  providing your own ratio. Use 1 or greater to use all suggestions.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Field Permissions module
;;
;; Original author: markus_petrux (http://drupal.org/user/39593)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

CONTENTS OF THIS FILE
=====================
* OVERVIEW
* USAGE
* REQUIREMENTS
* INSTALLATION


OVERVIEW
========

The Field Permissions module allows site administrators to set field-level
permissions for fields that are attached to any kind of entity (such as nodes
or users).

Permissions can be set for editing or viewing the field (either in all
contexts, or only when it is attached to an entity owned by the current user).
Permissions can also be set for editing the field while creating a new entity.

Permissions for each field are not created by default. Instead, administrators
can enable these permissions explicitly for the fields where this feature is
needed.


USAGE
=====

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


INSTALLATION
============

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

*******************************************************************************

Quicktabs

Description:
-------------------------------------------------------------------------------

This module provides a form for admins to create a block of tabbed content by
selecting a view, a node, a block or an existing Quicktabs instance as the content
of each tab.
The module can be extended to display other types of content.


Installation & Use:
-------------------------------------------------------------------------------

1.  Enable module in module list located at administer > structure > modules.
2.  Go to admin/structure/quicktabs and click on "Add Quicktabs Instance".
3.  Add a title (this will be the block title) and start entering information for your tabs
4.  Use the Add another tab button to add more tabs.
5.  Use the drag handles on the left to re-arrange tabs.
6.  Once you have defined all the tabs, click 'Save'.
7.  You new block will be available at admin/structure/blocks.
8.  Configure & enable it as required.
9.  To add tab styles to your Quicktabs instances, enable the quicktabs_tabstyles module
10. Edit the default style at admin/structure/quicktabs/styles
11. Control the style of individual Quicktabs instances by editing the instance in
question and selecting from the style dropdown.

Note:
-------------------------------------------------------------------------------
Because Quicktabs allows your tabbed content to be pulled via ajax, it has its
own menu callback for getting this content and returning it in JSON format. For
node content, it uses the standard node_access check to make sure the user has
access to this content. It is important to note that ANY node can be viewed
from this menu callback; if you go to it directly at quicktabs/ajax/node/[nid]
it will return a JSON text string of the node information. If there are certain 
fields in ANY of your nodes that are supposed to be private, these MUST be 
controlled at admin/content/node-type/MY_NODE_TYPE/display by setting them to 
be excluded on teaser and node view. Setting them as private through some other 
mechanism, e.g. Panels, will not affect their being displayed in an ajax Quicktab.

For Developers:
-------------------------------------------------------------------------------
The basic Quicktabs functionality can be extended in several ways. The most basic is
to use the quicktabs_build_quicktabs() function to create Quicktabs instances 
programmatically, putting whatever you want into the Quicktabs instance. This function
takes 3 parameters:
$name - the name of an existing Quicktabs instance (i.e. existing in the database or
in code), or a new name if creating an instance from scratch
$overrides - an array of options to override the settings for the existing instance, or
to override the default settings if creating an instance from scratch
$custom_tabs - an array of tab content arrays. A very basic tab content array would be
array('title' => 'My Custom Tab', 'contents' => 'Some text').
One example of where this might prove useful is in a hook_page_alter implementation,
where you could essentially put any render array that's part of the page into a
Quicktabs instance. The contents property of a cusom tab can be a render array or
a string of html.

Another way to extend Quicktabs is to add a renderer plugin. Quicktabs comes with
3 renderer plugins: jQuery UI Tabs, jQuery UI Accordion, and classic Quicktabs. A
renderer plugin is a class that extends the QuickRenderer class and implements the 
render() method, returning a render array that can be passed to drupal_render().
See any of the existing renderer plugins for examples. Also see Quicktabs' implement-
ation of hook_quicktabs_renderers().

Lastly, Quicktabs can be extended by adding new types of entities that can be loaded
as tab content. Quicktabs itself provides the node, block, view, qtabs and callback
tab content types. Your contents plugins should extend the QuickContent class. See
the existing plugins and the hook_quicktabs_contents implementation for guidance.



Author:
-------------------------------------------------------------------------------
Katherine Bailey <katherine@katbailey.net>
http://drupal.org/user/172987

# Video.js support module 2 for Drupal 7

## Required dependencies

- Drupal core File module

## Optional dependencies

- [Libraries API 2](http://drupal.org/project/libraries)

## Installation

1. Install the Video.js module by copying the sources to a modules directory, 
   such as `sites/all/modules` or `sites/[yoursite]/modules`.
2. Download the Video.js library from http://videojs.com. Extract the module to
   `sites/all/libraries/video-js` and make sure that
   `sites/all/libraries/video-js/video.min.js` exists.
3. In your Drupal site, enable the module.
4. If not yet created, create a File field for one of your content types at
   Structure -> Content types -> [type] -> Manage fields. Make sure
   the allowed extensions contain only HTML5 video extensions, such as mp4,
   webm, mov and ogv. Use the `Number of values` setting to allow users to
   upload alternative versions of the same video, for instance MP4 and Ogg.
   To allow users to upload a poster image, also allow png, gif or jpg.
5. At the Manage display tab, select `Video.js` for your File field.
6. Create a piece of content with the configured field.
7. Create a poster image and upload the image in the FileField field created in
   step #4.

## Poster images from a separate field

It is possible to display images uploaded to an image field as the video
poster image. After you added an image field to your content type, edit the
display settings of the Video.js field and specify the image field in the
"Poster image field" setting.

## Installation with the Video module

If you are using the Video module, you can't configure the player at the
`Manage display` tab. Instead, select Video.js at the Players tab of the
Video settings page (admin/config/media/video/players).

## Support

Report bugs at http://drupal.org/project/issues/videojs
Video.js HTTP Live Streaming
============================

HTTP Live Streaming is developer by Apply to allow iOS devices like the iPad,
iPod Touch or iPhone to select a video stream that suits the device capabilities
and available bandwidth. Each stream is segmented in multiple MPEG stream files
and has an m3u8 index files. Another m3u8 file lists these m3u8 files together
with the bitrate of these alternatives. This m3u8 master index file is used
by the iOS video player to select the right m3u8 file. When the available
bandwidth changes during playback, the device may switch to another stream.

This module intercepts m3u8 files supplied to the Video.js module.
It replaces these files with one new dynamically generated file file that makes
bandwidth switching available to iOS devices.

Requirements
------------

1. Multiple m3u8 files need to be supplied to Video.js. When just one m3u8 file
   is supplied there is no choice for the iOS player, so no master index is
   needed.
2. The files need to have the filemime application/vnd.apple.mpegurl.
3. The filenames need to contain `<number>k` in the file name, such as
   `sample-640k.m3u8`. This number is used to indicate the bandwidth
   to the client.

You can use the Video module with the Zencoder transcoder to create files
that are compatible with the Video.js module.

Configuration
-------------

The module works out of the box without configuration, provided you meet the
requirements and Video.js is working correctly.
By default, the m3u8 master index files are created dynamically: the paths
to the individual files are embedded in the path of the index file. This works
in most of the times and only breaks if the paths to the m3u8 files are very
long.
In those cases, you can change the `Delivery mode` to `Static files` in
the Video.js settings page. Now, the m3u8 master index file will be stored on
a configurable location. The filename will be formed by the MD5 hash of the
file contents, so a new file will only be written if the source file names
change. The master index file will never be deleted, so it is advisable to
write the master index files to a dedicated directoryso they can be removed
occasionally. It is no problem to remove a m3u8 master index file because they
will be recreated when needed.


Also see
--------

- https://app.zencoder.com/docs/guides/encoding-settings/http-live-streaming
- https://developer.apple.com/resources/http-streaming/
- http://drupal.org/project/video
This is a temporary fork of http://drupal.org/project/leaflet_widget. Hoping to merge.
-- SUMMARY --

Chosen uses the Chosen jQuery plugin to make your <select>
elements more user-friendly.


-- INSTALLATION --

  1. Download the Chosen jQuery plugin
  (http://harvesthq.github.io/chosen/ version 1.1.0 is recommended)
  and extract the file under sites/all/libraries.
  2. Download and enable the module.
  3. Configure at Administer > Configuration >
  User interface > Chosen (requires administer site configuration permission)

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
      For date fields this could look like:
      select:not([name*='day'],[name*='year'],[name*='month'])
efb
==============

A Drupal module to support rapid creation of entity fields based on schema.org templates
Views Slideshow
===============

The Views Slideshow module is a Views Style Plugin that can be used to output
Views in a jQuery slideshow.

There are currently 2 modes:

SingleFrame

In SingleFrame mode slideshows are output as single elements and controls can be
displayed as numbered links or thumbnails of individual fields.

ThumbnailHover

In ThumbnailHover mode slideshows are output as node teasers or full nodes. The
controls for advancing the slideshow are nodes too.

Further details about each can be found within their respective directories.


Requirements
============

Views 3 is required for this module to be of any use.


Description
===========

This module will create a View type of Slideshow that will display nodes in a
jQuery slideshow.

Settings are available for fade, timing, mode, and more.


Authors/maintainers
===================

Original Author:

Aaron Winborn (winborn at advomatic dot com)
http://drupal.org/user/33420

Co-maintainers:

redndahead
http://drupal.org/user/160320

psynaptic
http://drupal.org/user/93429


Support
=======

Issues should be posted in the issue queue on drupal.org:

http://drupal.org/project/issues/views_slideshow

Views Slideshow: Cycle
============================

The original default slideshow mode for Views Slideshow.


Description
===========

The Views Slideshow: Cycle module adds a Views display for showing rows as items
in a jQuery slideshow. Rows could be single images, full nodes, fields, or
whatever else that Views can display.

Controls can be added to control the slideshow. And it also has the ability to
allow modules to create different pagers for it.


"It feeds"


FEEDS
=====

An import and aggregation framework for Drupal.
http://drupal.org/project/feeds

Features
========

- Pluggable import configurations consisting of fetchers (get data) parsers
  (read and transform data) and processors (create content on Drupal).
-- HTTP upload (with optional PubSubHubbub support).
-- File upload.
-- CSV, RSS, Atom parsing.
-- Creates nodes or terms.
-- Creates lightweight database records if Data module is installed.
   http://drupal.org/project/data
-- Additional fetchers/parsers or processors can be added by an object oriented
   plugin system.
-- Granular mapping of parsed data to content elements.
- Import configurations can be piggy backed on nodes (thus using nodes to track
  subscriptions to feeds) or they can be used on a standalone form.
- Unlimited number of import configurations.
- Export import configurations to code.
- Optional libraries module support.

Requirements
============

- CTools 7.x-1.x
  http://drupal.org/project/ctools
- Job Scheduler
  http://drupal.org/project/job_scheduler
- Drupal 7.x
  http://drupal.org/project/drupal
- PHP safe mode is not supported, depending on your Feeds Importer configuration
  safe mode may cause no problems though.

Installation
============

- Install Feeds, Feeds Admin UI.
- To get started quick, install one or all of the following Feature modules:
  Feeds News, Feeds Import, Feeds Fast News (more info below).
- Make sure cron is correctly configured http://drupal.org/cron
- Go to import/ to import data.

SimplePie Installation
======================

- To install the SimplePie parser plugin, complete the following steps:
  1. Download SimplePie from http://simplepie.org/downloads. The recommended
     version is: 1.3.
  2. Decompress the downloaded zip file.
  3. Rename the uncompressed folder to 'simplepie'.
     For example rename 'simplepie-simplepie-e9472a1' to 'simplepie'.
  4. Move the folder to sites/all/libraries. The final directory structure
     should be sites/all/libraries/simplepie.
  5. Flush the Drupal cache.
  6. The SimplePie parser should be available now in the list of parsers.

Feature modules
===============

Feeds ships with three feature modules that can be enabled on
admin/build/modules or - if you are using Features - on admin/build/features.
http://drupal.org/project/features

The purpose of these modules is to provide a quick start for using Feeds. You
can either use them out of the box as they come or you can take them as samples
to learn how to build import or aggregation functionality with Feeds.

The feature modules merely contain sets of configurations using Feeds and in
some cases the modules Node, Views or Data. If the default configurations do not
fit your use case you can change them on the respective configuration pages for
Feeds, Node, Views or Data.

Here is a description of the provided feature modules:

- Feeds News -

This feature is a news aggregator. It provides a content type "Feed" that can
be used to subscribe to RSS or Atom feeds. Every item on such a feed is
aggregated as a node of the type "Feed item", also provided by the module.

What's neat about Feeds News is that it comes with a configured View that shows
a list of news items with every feed on the feed node's "View items" tab. It
also comes with an OPML importer filter that can be accessed under /import.

- Feeds Import -

This feature is an example illustrating Feeds' import capabilities. It contains
a node importer and a user importer that can be accessed under /import. Both
accept CSV or TSV files as imports.

PubSubHubbub support
====================

Feeds supports the PubSubHubbub publish/subscribe protocol. Follow these steps
to set it up for your site.
https://github.com/pubsubhubbub/

- Go to admin/build/feeds and edit (override) the importer configuration you
  would like to use for PubSubHubbub.
- Choose the HTTP Fetcher if it is not already selected.
- On the HTTP Fetcher, click on 'settings' and check "Use PubSubHubbub".
- Optionally you can use a designated hub such as http://superfeedr.com/ or your
  own. If a designated hub is specified, every feed on this importer
  configuration will be subscribed to this hub, no matter what the feed itself
  specifies.

Libraries support
=================

If you are using Libraries module, you can place external libraries in the
Libraries module's search path (for instance sites/all/libraries. The only
external library used at the moment is SimplePie.

Libraries found in the libraries search path are preferred over libraries in
feeds/libraries/.

Transliteration support
=======================

If you plan to store files with Feeds - for instance when storing podcasts
or images from syndication feeds - it is recommended to enable the
Transliteration module to avoid issues with non-ASCII characters in file names.
http://drupal.org/project/transliteration

API Overview
============

See "The developer's guide to Feeds":
http://drupal.org/node/622700

Debugging
=========

Set the Drupal variable 'feeds_debug' to TRUE (i. e. using drush). This will
create a file /tmp/feeds_[my_site_location].log. Use "tail -f" on the command
line to get a live view of debug output.

Note: at the moment, only PubSubHubbub related actions are logged.

Performance
===========

See "The site builder's guide to Feeds":
http://drupal.org/node/622698

Hidden settings
===============

Hidden settings are variables that you can define by adding them to the $conf
array in your settings.php file.

Name:        feeds_debug
Default:     FALSE
Description: Set to TRUE for enabling debug output to
             /DRUPALTMPDIR/feeds_[sitename].log

Name:        feeds_library_dir
Default:     FALSE
Description: The location where Feeds should look for libraries that it uses.
             You can use this variable to override the libraries that are in
             the Feeds libraries folder, for example "http_request.inc".

Name:        feeds_importer_class
Default:     'FeedsImporter'
Description: The class to use for importing feeds.

Name:        feeds_source_class
Default:     'FeedsSource'
Description: The class to use for handling feed sources.

Name:        feeds_process_limit
Default:     50
             The number of nodes feed node processor creates or deletes in one
             page load.

Name:        http_request_timeout
Default:     15
Description: Timeout in seconds to wait for an HTTP get request to finish.
Note:        This setting could be overridden per importer in admin UI :
             admin/structure/feeds/<your_importer>/settings/<your_fetcher> page.

Name:        feeds_never_use_curl
Default:     FALSE
Description: Flag to stop feeds from using its cURL for http requests. See
             http_request_use_curl().

Name:        feeds_use_mbstring
Default:     TRUE
Description: The extension mbstring is used to convert encodings during parsing.
             The reason that this can be turned off is to be able to test Feeds
             behavior when the extension is not available.

Glossary
========

See "Feeds glossary":
http://drupal.org/node/622710
This module allows you to embed a View as a field in another View.

The View in the view-field can accept argument values from other fields of the parent View, using tokens.

Here's how:

1. Before you can add a view-field to a "parent" view, you must create a "child" view.
2. Add arguments to that child view. The parent view will be passing argument values to
   the child so that the child knows what to display. No other settings are necessary,
   but validators and "argument not present" could be set.
3. Create a "parent" view, if not already existing.
4. Add child view (Global:View field). The field must be toward the bottom of the field list,
   or at least underneath the fields that are going to be used as arguments.
   (E.g., "node id" might be used as an match between the parent and child views,
   so put the "node id" field before your Global:View field in the list.)
5. Select which View and Display to use for the child data (will require doing this in 2 steps
   - the field must be saved before the display selection is available).
6. Find which tokens are available by looking at the "Replacement patterns" list right below the Arguments setting.
   Type the token replacements, in order, separated by a comma, as the arguments for that view field.
   These values will be passed to the child. Make sure each field you are passing as an argument is completely clean,
   as in: no label, no formatting, nothing that would pass into the argument other than the desired text or number.
Welcome to Remote File Source.

-- SUMMARY --

Remote File Source allows you to add a file from a remote server to a filefield
without transferring it locally.

-- REQUIREMENTS --

- FileField Sources
- Remote stream wrapper


-- INSTALLATION --

1) Install as usual, see http://drupal.org/node/70151 for further information.

2) You are done.
   Token Filter
-----------

This is a very simple module to make token values available as an input filter.

This initial development version only works for global and user token types.

Installation:

1) Enable the module
2) Go to /admin/settings/filters and enable the token_filter for any of your existing filter type or if you wish, create a new one.

Then in the text where you use that input filter you can use substitution tokens with

[token global site-name] etc.

Tokens typically available are:

global:
-------
user-name
user-id
user-mail
site-url
site-name
site-slogan
site-mail
site-date

user:
-----
user
user-raw
uid
mail
reg-date
reg-since
log-date
log-since
date-in-tz
account-url
account-edit
/**
 * @file
 * README file for Workbench.
 */

Workbench
A framework for simplified content management.

CONTENTS
--------

1.  Introduction
1.1   Use-case
1.2   Examples
1.3   Terminology
2.  Installation
3.  Permissions
4.  Configuration
5.  Using the module
5.1  My Content
5.2  Create Content
6.  Troubleshooting
7.  Developer notes
7.1   API documentation
7.2   Database schema
7.3   Views integration
8.  Feature roadmap


----
1.  Introduction

Workbench provides a simplified user interface and an API to integrate other
Drupal modules.  Workbench on its own provides Content contributors a way to
easily access their own content.

Workbench gains more features when you install and enable these modules:

Workbench Access - http://drupal.org/project/workbench_access
Workbench Moderation - http://drupal.org/project/workbench_moderation
Workbench Media - http://drupal.org/project/workbench_media
Workbench Files - http://drupal.org/project/workbench_files

One way to think about Workbench is that it becomes the Dashboard for Content
Contributors.  Basically, putting all of the content needs of a user in one
place.

----
1.1  Use Case

Drupal provides a great framework for building functionality.  Workbench helps
harness content-focused features in one unified user interface.  The goal
is that a user does not need to learn Drupal in order to add content to the
site.

Users need access to their account, their content, and to add new content.
Instead of having to know how to navigate to My Account (/user/[uid]),
Add content (node/add), and Find Content (admin/content), the user goes to
My Workbench instead.

Simple changes like this help ease the learning curve for new users.

With additional Workbench modules like Workbench Access and Workbench
Moderation, Workbench becomes a full system which controls who can access
content and provide editorial workflow so that only the correct content is
published.

----
2.  Installation

Views is required in order to install Workbench.

Install the module and enable it according to Drupal standards.


----
3.  Permissions

Once a user role has access to create content, Workbench becomes
immediately useful.

 Workbench Permissions

 -- Administer Workbench settings
 Only Administrators should have access to this.  Workbench without its other
 modules does not have any configuration settings.  It becomes more useful
 when additional workbench modules are enabled.

 -- Access My Workbench
 For any user role who may access their own workbench a.k.a My Workbench

 -- View all unpublished content
 Allows a user to see content that is not Published on the site.  This
 becomes even more useful when Workbench Moderation is enabled.

A typical permission setup so that a user can take advantage of Workbench
looks like:

Node Permissions
 -- Article: Create new content
 -- Article: Edit own content
 -- Article: Delete own content
 -- Basic page: Create new content
 -- Basic page: Edit own content
 -- Basic page: Delete own content

System Permissions
 -- View the administration theme

Toolbar Permissions
 -- Use the administration toolbar

Workbench Permissions
 -- Access My Workbench

----
4.  Configuration

Workbench does not have any Configuration settings.  Additional Workbench
modules have their own configuration.

----
5.  Using the module

As an Administrator or a user with Access My Workbench permissions, you will
see My Workbench in the toolbar to the right of the Home icon.

----
5.1  My Content
On the My Content tab, you can see three areas:

 - My Profile
 - Content I've Edited
 - All Recent Content

This is your content dashboard.  As soon as you Add or edit content, it will
be displayed in the Content I've Edited block.

Notice the sub tabs:

 - Content I've Edited
 - All Recent Content

These go to full page lists with filters available to shorten the list of
content.  You can filter the list by:

 - Title (keywords)
 - Type (Content type)
 - Published (status of the content)
 - Items per page (defaults to 25)

Any lists of content include columns labels which can sort the current list.
Each item in the list links to the full content or you can click edit to
start editing.

----
5.2  Create Content

Click the Create Content tab to view a list of types of content that you can
create.  Remember, we're dealing with Entities now.  Initially, Workbench
shows various Node Types that you have permission to create.  When
Workbench Media is enabled, the Media item is added to this list as well.

Click the type of content you want to add, then follow the usual procedure for
adding content.

----
6.  Troubleshooting

Some helpful tips.

For automatic navigation to Workbench, be sure to give your user role
access to the Administration Toolbar; otherwise you need to add access to
one of the menus.

Be sure your user role has permission to create content.  Without those
permissions, Workbench will only give you access to your user account.

----
7.  Developer notes

The following section documents technical details of interest to developers.

----
7.1   API documentation

Workbench does not offer a generic API.  Please check the other
Workbench modules like Workbench Access for descriptions of their APIs.

----
7.2   Database schema

Workbench does not create any tables during installation.  Other Workbench
modules like Workbench Access and Workbench Moderation create tables.
Please review each module's README.txt file to learn more about schema
changes.

----
7.3   Views integration

Workbench creates several base views for the My Content tab.  Other
Workbench modules further alter these views.  You can alter the views
via Views UI as well.

----
8.  Feature roadmap

 -- integrate workflow module as an alternative to workbench_moderation
 -- publish permissions per content type
 -- email notifications
 -- integrate scheduler module for scheduled start/end publish dates
 -- general UX improvements

DESCRIPTION
-----------
Enable users to manage menus inside Organic Groups.

REQUIREMENTS
------------
- Organic Groups module (http://drupal.org/project/og).
- Menu module.

INSTALLATION
------------
- Enable the module.
- Give "administer og menu" permission to the desired roles.
- Visit the og menu configuration page to configure at will.
- Enable group content types for use with OG Menu.

USAGE
-----
- Administrators can create OG menus through the regular menu interface at
  admin/structure/menu/add. Choose a group to associate with the menu.
- Organic group members with the "administer og menu" permission can also manage
  menus at node/[nid]/og_menu.
- "administer og menu" permission can be granted on global or group level.
- Group content types can be enabled for use with OG Menu. Once enabled, users
  can add a menu link directly from the node creation form to any of the menu's
  they have access to.
- For group types, users can create an associated menu by checking
  "Enable menu for this group" on the node edit/creation form.
- You can enable the "OG Menu : single" and the "OG Menu : multiple" blocks at
  admin/build/block.
  - "OG Menu : single" will display the first available menu for the first
    available group in the context.
  - "OG Menu : multiple" will display all available menus for all available
    groups in the context.
- OG menus won't show on the regular menu interface. They show up on
  admin/structure/og_menu.
- Ability to hide OG Menu's from the block admin interface and on other places
  for some contrib modules.

NOTES
-----
Be aware that since menu administration forms are mostly duplicated, if a
contrib module adds functionality to menu administration forms without
additional permissions, these additions may be available for OG menu users with
'administer og menu' permission. This could allow these users to be able to do
things you don't want them to. Please report these modules if you catch one.

TODO/BUGS/FEATURE REQUESTS
--------------------------
- See http://drupal.org/project/issues/og_menu. Please search before filing
  issues in order to prevent duplicates.
- Please test the D7 release and report any bugs or suggestions you might find.

UPGRADING FROM 6.x TO 7.x
---------------------------
- There currently is no upgrade path! If you need an upgrade path, please file
  an issue
UPGRADING FROM 7.x-2.x TO 7.x-3.x
---------------------------------
- Update OG first!

CREDITS
-------
Originally authored and maintained by Scott Ash (ashsc).

7.x-3.x port contributors (sorry if anyone was forgotten):
  - bulldozer2003
  - zipymonkey
  - jgraham
  - Jackinloadup
  - Wim Vanheste (rv0) (http://www.coworks.net)

7.x initial port contributors:
  - Stefan Vaduva (http://vamist.ro)
  - Nick Santamaria (http://www.itomic.com.au)
  - Frederik Grunta (Aeternum)
  - Wim Vanheste (rv0) (http://www.coworks.net)

7.x maintainers
  - Wim Vanheste (rv0) (http://www.coworks.net)

6.x-2.x maintainer
  - Julien De Luca (jide)/**
 * Unique Field module for Drupal (unique_field)
 * Compatible with Drupal 7.x
 *
 * By Joe Turgeon [http://arithmetric.com]
 */

The Unique Field module provides a way to require that specified fields
or characteristics of a node are unique. This includes the node's title,
author, language, taxonomy terms, and other fields.

Without this module, Drupal and CCK do not prevent multiple nodes from
having the same title or the same value in a given field.

For example, if you have a content type with a Date field and there
should only be one node per date, you could use this module to prevent a
node from being saved with a date already used in another node.

This module adds additional options to the administration page for each
content type (i.e. admin/structure/types/manage/<content type>) for
specifying which fields must be unique. The administrator may specify
whether each field must be unique or whether the fields in combination must
be unique. Also, the administrator can choose whether the fields must be
unique among all other nodes or only among nodes from the given node's
content type.

Alternatively, you can select the 'single node' scope, which allows you
to require that the specified fields are each unique on that node. For
example, if a node has multiple, separate user reference fields, this
setting will require that no user is selected more than once on one node.

For more information, see this module's page at:
http://drupal.org/project/unique_field
-----------------
FileField Sources
-----------------

Description
-----------
FileField Sources is a module that enhances the generic and image upload fields
in Drupal. Typically such fields only allow you to upload a file from your
desktop. FileField Sources makes it so that you can populate any file field
from a variety of sources, such as entering remote URLs directly, re-use
existing uploaded files, pull from a server directory, or a variety of other
possibilities.

This module built by Robots: http://www.lullabot.com
Author: Nathan Haug (quicksketch)

Installation
------------
1) Place this module directory in your modules folder (this will usually be
   "sites/all/modules/").

2) Enable the module within your Drupal site.

3) Add or configure an existing file or image field. To configure a typical node
   field, visit Admin -> Structure -> Content types and click "manage fields"
   on a type you'd like to modify. Add a new file field or edit an existing one.

   While editing the file or image field, you'll have new options available
   under a "File sources" fieldset. You can enable the desired sources for that
   particular field.

4) Create a piece of content that uses your file file and try it out.

Support
-------
Please file bug reports in the FileField Sources issue queue. Do not use the
Drupal.org forums or send bug reports via e-mail.
http://drupal.org/project/issues/filefield_sources?categories=All
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

DOUBLE FIELD DRUPAL MODULE
---------------------------

SUMMARY:

  This is a small module written to provide extensions to Drupal's core fields.
  By this module you can split your fields up into two separate parts.
  Example: key/value, name/email etc.

INSTALLATION:

  1. Copy the module folder to your server.
  2. Enable the module via the modules page.
  See http://drupal.org/node/895232 for further information

CONFIGURATION:

  * There are lots of configurable options.
  * Go to admin/structure/types to add or edit double fields for
    your content types.
  
                        IMPORTANT INSTALLATION INSTRUCTIONS
  ------------------------------------------------------------------------------------
  In order for this module to work properly with IE, you will need to download the 
  ExplorerCanvas library, which can be found here - http://excanvas.sourceforge.net/.
  Place the downloaded directory 'excanvas' inside the 'sites/all/libraries' directory.
  Also, make sure that this file is accessable (readable).  A standard permission setting 
  of 755 should work for the excanvas folder (755 means permission settings - rwxr-xr-x)
  On Linux or Mac, you can do this with the command 'sudo chmod -R 755 excanvas'

  Other than that, you just need to turn the module on in the usual Drupal way.

  --------------------------------------------------------------------------------------
                                   ABOUT THE MODULE
    
  The Beautytips module provides ballon-help style tooltip for any page element. 
  It integrates BeautyTips jQuery plugin by Jeff Robbins with Drupal.  Currently, this 
  module allows tooltips to appear with textfields and textareas.  It also supplies hover
  tips for Drupal help links and advanced help links.  Most importantly, it allows developers
  to add their own beautytips popups to their site without having to delve into jQuery.
  
  For information about the Beauty Tips jQuery plugin:
    http://www.lullabot.com/articles/announcing-beautytips-jquery-tooltip-plugin
    http://www.lullabot.com/articles/beautytips-09-release
  
  To see a demonstration:
    http://www.lullabot.com/files/bt/bt-latest/DEMO/index.html

  ------------------------------------------------------------------------------------
                         Add beautytips js to every page
  ------------------------------------------------------------------------------------
  
  If you enable the option 'Add beautytips js to every page', then, anything with the 
  class 'beautytips' will automatically have a popup which displays the 'title' attribute 
  of the element.  If there is nothing in the title attribute, then there will be no popup.
  
  With this enabled, you can also define custom elements which will be given a beautytip.
  For example, you can set it up so that anything on any page with the id 'example'
  will have a popup.  Again, the content of the beauty will be pulled from the
  element's title attribute.

  --------------------------------------------------------------------------------------
                                 Custom Beautytips
  --------------------------------------------------------------------------------------
    Beautytips has an API so that you can create your own beautytips and add them into 
  any place on your site.  To do this, you will need to set up an array of options and 
  then pass them along to the beautytips_add_beautytips function.  All of the options are 
  outlined below.  This array will need to have a couple of important pieces of 
  information, and can accept a plethora of other optional info.

    1.  Each beautytip will need a name - distinct from other beautytips added on the 
        web page.
      ex. options['bt_drupal_help_page'] = array( . . .

    2.  Each beautytip will need a css(or jQuery) selector.  This is how the bt plugin 
        knows where to place the tooltip.
      ex. 'cssSelect' => '.help-items li a'

    3.  Each beautytip will need some text to display.  You can define what to display 
        in 3 different ways.
  
      a.  Use 'text' to directly add supply the text.  It can accept html.
        ex 1.  'text' => t('Here's some beautytips text to display on this page.'),
  
      b.  Use 'contentSelector' to use jQuery to tell beautytips where to find the text 
          on a page.
        ex 2.  'contentSelector' => '$(this).next(".description").html()',
        This tells beautytips to find the next item after the css selector with class 
        'description' and use display it's html
  
      c.  Use 'ajaxPath' to provide a place on another webpage that should be displayed.
    
        ex 3. 'ajaxPath' => 'demo.html',
        This will display that particular webpage within the tooltip balloon.
    
        ex 4.  'ajaxPath' => '$(this).attr("href")',
        This uses jQuery to find the url associated with the link that was selected with 
        the css selector and displays it.
    
        ex 5. 'ajaxPath' => array('$(this).attr("href"), '#squeeze.clear-block p'),
        This does the same thing as ex. 4, except it only displays the css-selected section of 
        the page.
  
      d.  If none of the above 3 options are given, the beautytips plugin will by default set 
      'contentSelector' to be '$(this).attr('title')'.

    4.  All other options are optional.  See the list below.
      ex.  'fill' => "rgb(255, 155, 55)" - sets the background color of the balloon.

  ------------------------------------------------------------------------------------
    ex. Full options array and function call to add beautytips

    $options['bt_drupal_help_page'] = array(
      'cssSelect' => '.help-items li a',
      'ajaxPath' => array("$(this).attr('href')", '.clear-block p'),
      'trigger' => array('mouseover', 'click'),
      'width' => 350,
    );
    beautytips_add_beautytips($options);
    
  ------------------------------------------------------------------------------------
                                     HOOK
  ------------------------------------------------------------------------------------
  
  hook_define_beautytips_styles() - allows a module to define its own base beautytips
  styles.  (See beautytips_api.module for an example). This allows easier use of 
  beautytips_add_beautytips by allowing a style to be indicated instead of having to 
  define all of the same options everytime.
  example of adding beautytips with the style option:
    $options['bt_drupal_help_page'] = array(
      'cssSelect' => '.help-items li a',
      'ajaxPath' => array("$(this).attr('href')", '.clear-block p'),
      'trigger' => array('mouseover', 'click'),
      'width' => 350,
      'style' => 'hulu',
    );
    beautytips_add_beautytips($options);
    
  This example will add beautytips to the help page using the 'hulu' style
  as defined in the implementation of this hook in beautytips_api.module.
  
  Any defined style will also show up on the beautytips settings page and
  can be set as the default style.

  ------------------------------------------------------------------------------------
                               Beautytips Manager
  ------------------------------------------------------------------------------------
  You can setup custom styles and custom tooltips using the beautytips_manage module.
  **TODO: The Rest**

  All styles are added into javascript settings in Drupal.settings.beautytipStyles
  in case you want to use the setup styles, but want to add you tooltips through
  javascript.
  **TODO: The Rest**
  
******************************************************************************
Beautytips options and defaults (Copied and pasted from the jQuery.bt.js file)
******************************************************************************
/**
 * Defaults for the beauty tips
 *
 * Note this is a variable definition and not a function. So defaults can be
 * written for an entire page by simply redefining attributes like so:
 *
 *   jQuery.bt.options.width = 400;
 *
 * Be sure to use *jQuery.bt.options* and not jQuery.bt.defaults when overriding
 *
 * This would make all Beauty Tips boxes 400px wide.
 *
 * Each of these options may also be overridden during
 *
 * Can be overriden globally or at time of call.
 *
 */
jQuery.bt.defaults = {
  trigger:         'hover',                // trigger to show/hide tip
                                           // use [on, off] to define separate on/off triggers
                                           // also use space character to allow multiple  to trigger
                                           // examples:
                                           //   ['focus', 'blur'] // focus displays, blur hides
                                           //   'dblclick'        // dblclick toggles on/off
                                           //   ['focus mouseover', 'blur mouseout'] // multiple triggers
                                           //   'now'             // shows/hides tip without event
                                           //   'none'            // use $('#selector').btOn(); and ...btOff();
                                           //   'hoverIntent'     // hover using hoverIntent plugin (settings below)
                                           // note:
                                           //   hoverIntent becomes default if available
                                           
  clickAnywhereToClose: true,              // clicking anywhere outside of the tip will close it 
  closeWhenOthersOpen: false,              // tip will be closed before another opens - stop >= 2 tips being on
                                           
  shrinkToFit:      false,                 // should short single-line content get a narrower balloon?
  width:            '200px',               // width of tooltip box
  
  padding:          '10px',                // padding for content (get more fine grained with cssStyles)
  spikeGirth:       10,                    // width of spike
  spikeLength:      15,                    // length of spike
  overlap:          0,                     // spike overlap (px) onto target (can cause problems with 'hover' trigger)
  overlay:          false,                 // display overlay on target (use CSS to style) -- BUGGY!
  killTitle:        true,                  // kill title tags to avoid double tooltips

  textzIndex:       9999,                  // z-index for the text
  boxzIndex:        9998,                  // z-index for the "talk" box (should always be less than textzIndex)
  wrapperzIndex:    9997,
  offsetParent:     null,                  // DOM node to append the tooltip into.
                                           // Must be positioned relative or absolute. Can be selector or object
  positions:        ['most'],              // preference of positions for tip (will use first with available space)
                                           // possible values 'top', 'bottom', 'left', 'right' as an array in order of
                                           // preference. Last value will be used if others don't have enough space.
                                           // or use 'most' to use the area with the most space
  fill:             "rgb(255, 255, 102)",  // fill color for the tooltip box, you can use any CSS-style color definition method
                                           // http://www.w3.org/TR/css3-color/#numerical - not all methods have been tested
  
  windowMargin:     10,                    // space (px) to leave between text box and browser edge

  strokeWidth:      1,                     // width of stroke around box, **set to 0 for no stroke**
  strokeStyle:      "#000",                // color/alpha of stroke

  cornerRadius:     5,                     // radius of corners (px), set to 0 for square corners
  
                    // following values are on a scale of 0 to 1 with .5 being centered
  
  centerPointX:     .5,                    // the spike extends from center of the target edge to this point
  centerPointY:     .5,                    // defined by percentage horizontal (x) and vertical (y)
    
  shadow:           false,                 // use drop shadow? (only displays in Safari and FF 3.1) - experimental
  shadowOffsetX:    2,                     // shadow offset x (px)
  shadowOffsetY:    2,                     // shadow offset y (px)
  shadowBlur:       3,                     // shadow blur (px)
  shadowColor:      "#000",                // shadow color/alpha
  shadowOverlap:   false,                  // when shadows overlap the target element it can cause problem with hovering
                                           // set this to true to overlap or set to a numeric value to define the amount of overlap
  noShadowOpts:     {strokeStyle: '#999'},  // use this to define 'fall-back' options for browsers which don't support drop shadows
  
  cssClass:         '',                    // CSS class to add to the box wrapper div (of the TIP)
  cssStyles:        {},                    // styles to add the text box
                                           //   example: {fontFamily: 'Georgia, Times, serif', fontWeight: 'bold'}
                                               
  activeClass:      'bt-active',           // class added to TARGET element when its BeautyTip is active

  contentSelector:  "$(this).attr('title')", // if there is no content argument, use this selector to retrieve the title
                                           // a function which returns the content may also be passed here

  ajaxPath:         null,                  // if using ajax request for content, this contains url and (opt) selector
                                           // this will override content and contentSelector
                                           // examples (see jQuery load() function):
                                           //   '/demo.html'
                                           //   '/help/ajax/snip'
                                           //   '/help/existing/full div#content'
                                           
                                           // ajaxPath can also be defined as an array
                                           // in which case, the first value will be parsed as a jQuery selector
                                           // the result of which will be used as the ajaxPath
                                           // the second (optional) value is the content selector as above
                                           // examples:
                                           //    ["$(this).attr('href')", 'div#content']
                                           //    ["$(this).parents('.wrapper').find('.title').attr('href')"]
                                           //    ["$('#some-element').val()"]
                                           
  ajaxError:        '<strong>ERROR:</strong> <em>%error</em>',
                                           // error text, use "%error" to insert error from server
  ajaxLoading:     '<blink>Loading...</blink>',  // yes folks, it's the blink tag!
  ajaxData:         {},                    // key/value pairs
  ajaxType:         'GET',                 // 'GET' or 'POST'
  ajaxCache:        true,                  // cache ajax results and do not send request to same url multiple times
  ajaxOpts:         {},                    // any other ajax options - timeout, passwords, processing functions, etc...
                                           // see http://docs.jquery.com/Ajax/jQuery.ajax#options
                                    
  preBuild:         function(){},          // function to run before popup is built
  preShow:          function(box){},       // function to run before popup is displayed
  showTip:          function(box){
                      $(box).show();
                    },
  postShow:         function(box){},       // function to run after popup is built and displayed
  
  preHide:          function(box){},       // function to run before popup is removed
  hideTip:          function(box, callback) {
                      $(box).hide();
                      callback();   // you MUST call "callback" at the end of your animations
                    },
  postHide:         function(){},          // function to run after popup is removed
  
  hoverIntentOpts:  {                          // options for hoverIntent (if installed)
                      interval: 300,           // http://cherne.net/brian/resources/jquery.hoverIntent.html
                      timeout: 500
                    }
                                               
}; // </ jQuery.bt.defaults >

  **Note: If you need to use 'preBuild', 'preShow', 'showTip', 'postShow', 'preHide', 'hideTip', or 'postHide', 
  then it's recommended that you add your beautytips in javascript instead of in using this module's api.
  

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

Spaces 3.x
----------
Spaces is an API module intended to make configuration options generally
avaliable only at the sitewide level to be configurable and overridden by
individual "spaces" on a Drupal site. It has been described as:

- A way to make one Drupal site act like several sites
- A way to provide much more configurable, full-feature Organic Groups or user
  homepages
- A generalized API for contextual configuration


Requirements & compatibility
---------------------------
Use of spaces requires

- CTools: http://drupal.org/project/ctools
- Features: http://drupal.org/project/features

However, you will want the following modules in order to build or use reasonably
cool features with Spaces and take advantage of most space types:

- PURL: http://drupal.org/project/purl
- Context 3.x: http://drupal.org/project/context
- Strongarm 2.x: http://drupal.org/project/strongarm
- Views 2.x: http://drupal.org/project/views

Out of the box, Spaces provides integration modules for:

- User: `spaces_user`
- Taxonomy: `spaces_taxonomy`
- OG: `spaces_og`


Coming from Spaces 2.x?
-----------------------
The Spaces 3.x branch makes significant departures from many of the concepts
in the 2.x branch. Here is a non-exhaustive list of important changes:

- Removed strict PURL dependency. Spaces can now be made active through means
  other than a PURL provider (see `spaces_user_init()`).
- Usage of CTools plugins API and export API.
- `spaces_customizers()` and `spaces_settings()` have been replaced with a
  general configuration override system using object controllers (more on this
  below).

If you are upgrading from Spaces 2.x, prepare for a rocky ride. Update scripts
are included to migrate as cleanly as possible from 2.x to 3.x but any custom
settings you have created will need to be managed manually. The update scripts
leave the `spaces_settings` table intact for this reason.

Here is a rough list of steps to consider when upgrading from 2.x to 3.x:

1. Backup everything.
2. Run `update.php`.
3. Upgrade your features to Context 3, Strongarm 2, etc.
4. Have you implemented any custom 2.x space types? You need to migrate them,
   see `API.txt` and `spaces.api.php`.
5. Have you implemented any custom 2.x spaces settings? You need to migrate
   them to use standard Drupal variables and `system_settings_form()` (see
   the `features_test` module for an example).
6. Have you implemented any custom 2.x spaces customizers? The concept may not
   transfer cleanly to Spaces 3, or if it does, it will probably make the most
   sense as a custom controller.


Core concept behind Spaces 3
----------------------------
Spaces 3 has been built outwards from the basic idea that it should be possible
for a "space" to override the values of a Drupal object that would otherwise
have a single, sitewide value. For our purposes

  A space is a configuration environment that is triggered or made active by
    some condition. For example, a "user space" might be made active when
    viewing a user's profile. Once that user space is active, any customization
    that user has made override sitewide values.

  An object is a Drupal site building or configuration structure. Examples
    include variables, contexts and views. Not included: nodes, users, taxonomy
    terms, other "content".

Let's first look at storage of overridden values. Spaces stores all of its
overrides in the `spaces_overrides` table. Here is a sample row:

    +------+----+-------------+------------------+------------------------+
    | type | id | object_type | object_id        | value                  |
    +------+----+-------------+------------------+------------------------+
    | og   | 14 | variable    | spaces_preset_og | s:13:"private_group";  |
    +------+----+-------------+------------------+------------------------+

This row describes an overridde when a certain Organic Group (node 14) is
active. In particular, the variable `spaces_preset_og` has the value
`private_group` when this space is active. More generally, `spaces_overrides`
can store any value to override the default of an object, described by
(`object_type`, `object_id`), for any space, described by (`type`, `id`).

In practice, this means that when node 14 is active

    variable_get('spaces_preset_og', NULL);
    // returns "private_group"

While when node 14 is not active

    variable_get('spaces_preset_og', NULL);
    // returns NULL or sitewide value


Controllers & contextuality
---------------------------
The example above shows that when a space is active you need to change some
basic assumptions about how Drupal works. In particular, spaces introduces
contextuality to settings and configuration.

Per-space overrides are handled by controllers. Controllers are CTools plugins
that manage retrieval and storage of overrides for a given object type. For
example, spaces comes with a variable controller and context controller. Each
controller should interface with its object's API at a retrieval point and at
a storage or save point.

    +-------------------------------------+-----------------------------------+
    |Drupal integration point             |Controller method                  |
    +-------------------------------------+-----------------------------------+
    |hook_context_reaction_fetch_alter()  |$space->controllers->context->get()|
    |spaces_form_context_ui_editor_alter()|$space->controllers->context->set()|
    +-------------------------------------+-----------------------------------+

Whenever a context's reaction value is fetched, the context controller's `get()`
method is invoked retrieving a value specific to the active space.

The controller's save integration point is triggered through a custom submit
handler to the context editor form through a `hook_form_alter()`.

Currently, our rule of thumb is that while retrieval may be contextual, actual
save API functions should not be overridden. In general, you should always be
able to retrieve and save the original values of an object in addition to
manipulating space overrides from the API.


Presets, levels of configuration
--------------------------------
Spaces presets are sets of configuration that apply to whole sets of spaces. For
example you may not want to make the same set of customizations for every new
user you add to the site. You can use a preset like "member" or "guest" to
capture a variety of settings and have new users use one of the presets.

With presets in the picture, `variable_get('foo', NULL)` can actually return one
of three possible values when a space is active:

1. `space`: is the override value for the active space. If the active space has
    saved an override for `foo`, this is what you will get.
2. `preset` is the override value for the preset. If the active space has not
    saved a value for `foo` the variable controller will fall back to the preset
    if it has a value for `foo`.
3. `original` is the sitewide, canonical value for `foo`. If neither the space
    nor the preset have an override for `foo`, you will get the sitewide value
    like a call to `variable_get()` when no spaces are active.

This cascading of values applies to all object types with a spaces controller.

**Aside**

This architecture *strongly* implies that it could or should be possible to
stack configuration overrides n levels rather than the current fixed number. In
such a scenario, presets would themselves become stacked spaces, and the picture
would become even simpler:

- Fixed stacking model (where > can be read as "inherits from"):

        space > preset > original

- Arbitrary stacking model (where space 0 is the preset space)

        space n > space n-1 > ... > space 1 > space 0 > original

This model is very attractive but requires some serious study before it can be
realized. Spaces 3 currently implements the fixed stacking model.


Managing and editing presets
----------------------------
The Spaces UI module allow provides the facility to manage presets. This
includes creating new presets, reverting overrides and editing preset metadata.
There is not a single UI for creating and editing all the elements of a
spaces preset. Presets can contain many settings about which the spaces module
actually knows nearly nothing, making it impossible to provide a useful
interface. Presets are meant to be edited through actual instance of a space.

For example, to change the features a preset has enabled you would:

1. Goto, or create, a space which uses the preset you wish to change.
2. Set the space to have the desired set of enabled feature.
3. Goto the "overrides" page (generally rendered as a tab) for the space.
4. Click the checkbox for the `space_menu_items` variable.
5. Click "Save to preset".

At this point any new groups created with this same preset will have the
configuration you've just specified. If the preset you've edited is provided
in code the interface at "admin > site building > spaces" (`admin/build/space`)
will show them as overriden.


Other functionality
-------------------
There is quite a bit of functionality in Spaces that does not fit neatly into
the picture of each space as a "configuration override environemnt." This
functionality has survived to support the users and code implemented around
existing user stories that spaces currently serves. In the future the
functionality may be further abstracted out so that Spaces can play a much more
minimal and possibly flexible role.

1. Features can be set to a state per space (defaults to enabled/disabled, but
overridable by extending classes) that determine their behavior within a space.
In particular, features tend to hide or show menu items, alter access to parts
of the menu tree, etc.
2. Access to a space has several levels - space types can control degrees of
admin access, feature access and basic access to a space.
3. Spaces can determine routing of certain pages - for example, some nodes may
only be viewed when a certain space is active or a certain administrative page
may drop all active spaces.

Note that none of these user stories are necessarily implied by the
configuration override framework introduced above.


Features
--------
Spaces integrates with the Features built using the Features module. Features
that are compatible with spaces must declare themselves as such by including the
`spaces[types]` key in their `.info` file.

For example a "MyBlog" module may include the following snippet in
`myblog.info` to declare that is is spaces-enabled;

    name = "MyBlog"
    package = "Features"
    ...
    spaces[types] = "all"

`spaces[types]` may be declared to be one of the following values:

- `all` indicates that this feature is compatible with all space types.
- an array of space types where this feature may be enabled. Note that you may
  also include the faux space type `site` in this array, indicating that this
  feature may be enabled even and/or possibly only when no spaces are active.

For example, if my feature `my_cool_gallery` should only be available when
outside of any spaces, I would use the following entry:

    spaces[types][] = "site"

If it can be enabled both outside of any spaces and inside of user spaces, but
not group spaces, I could use:

    spaces[types][] = "site"
    spaces[types][] = "user"


Settings
--------
Settings can be defined for spaces features simply as Drupal variables by
implementing a `system_settings_form()` at `features/[my-feature]`. If spaces
finds such a page defined by your feature, it will expose it as a link in
the features form for any of the space types where the feature is enabled.


Creating your own space types or extending existing ones
--------------------------------------------------------
Please see `API.txt` for instructions on how you can create your own space types
or use your own class to extend or replace one of the existing classes.


Maintainers
-----------
- alex_b (Alex Barth)
- jmiccolis (Jeff Miccolis)
- yhahn (Young Hahn)
- Ian Ward
About Spaces Taxonomy
=====================

A vocabulary is selected that will represent the Space realm and any
node tagged with a term from that Vocabulary will belong to that term
space. A node can only belong to one term space and you can't move it
between term spaces.

It would obviously be a nice to have to support multiple spaces and
moving between spaces but the implementation of both of these is
tricky, in particular questions like:

 1. If you land in node/5 without a PURL modifier which of its multiple
    spaces should spaces push you to? Should it just show it to you out of
    any space context? (often a bad idea)

 2. If you want to move foo/node/5 to bar/node/5, how do you handle any
    associations that may/may not be relevant in the new space? For
    example, imagine moving a casetracker case from a client group to a
    private group -- what should happen to its parent project and any
    email subscriptions for users that aren't in the target space?

These are reasons that term spaces are single selects.

Spaces Custom Text
------------------

This module allows space administrators to customize a limited number of
strings for a given space through the use of the global $conf
locale_custom_text_[langcode] variable. It is heavily inspired by the
stringoverrides modules.

 
Known Incompatibilities
-----------------------

Because it uses the core localization system to customize strings, this module
is incompatible with any normal usage of the localization system. This includes
core locale module.

See spaces_customtext.module for more details.

Spaces Dashboard 3.x
--------------------

The Spaces Dashboard module provides a "Dashboard" feature that can be used in
space type. The "Dashboard" is intended to be a page, or set of pages, where
space administrator have the ability to modify the content and arrangement.

Content is made available to the Dashboard using the core blocks system. Not all
block will show up as options for users, the dashboard must be told what blocks
it should offer. The dashboard feature offers a settings page in each space
where block availability can be configured. 

By default all dashboards will inherit the dashboard settings of the dashboard
in the so-called 'site' space. To target block availability settings at the
correct space type its important to understand how a particular spaces inherits
it's settings. A particular spaces has three source of a individual settings,
what has been set for the particular space, the setting of that space's preset,
the site wide setting. To make certain blocks available to spaces of a certain
type you must add this setting to a spaces preset. If neither the space itself
nor the preset includes a setting for which dashboard blocks are available the
site setting will be used.

Note: Spaces settings inheritance & spaces presets are covered in detail in the
main spaces module README.txt

Spaces OG
---------

Spaces integration of Organic Groups. Offers simplified Organic Groups privacy
presets and overrides on a per group level.


Installation
------------

- Install module and its dependencies.
- Go to admin/build/spaces and pick the default preset. Disable presets that
  users that can edit a group content type should not be able to pick.
- Go to admin/settings/purl and review settings. Per default Spaces OG assumes
  that a group should be identified by a unique path prefix (Types 'path' is
  enabled and the Modifier type 'path' is selected for Group spaces. If these
  settings do not fit your purposes, please refer to the Purl documentation for
  further information.
- Go to admin/content/node-settings/rebuild and rebuild your node access table
  if you have not rebuilt it after installing OG Access in a previous step.
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
https://drupal.org/documentation/install/modules-themes/modules-7 for further
information.


TROUBLESHOOTING
---------------

Token module doesn't provide any visible functions to the user on its own, it
just provides token handling services for other modules.


MAINTAINERS
-----------

Current maintainers:

 * Dave Reid (https://drupal.org/user/53892)= Masquerade =

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
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; WYSIWYG Filter module for Drupal
;;
;; Original author: markus_petrux at drupal.org (October 2008)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

OVERVIEW
========

The WYSIWYG Filter module provides an input filter that allows site
administrators configure which HTML elements, attributes and style properties
are allowed. It also may add rel="nofollow" to posted links based on filter
options. It can do so with no additional parsing on user input. That is, it may
apply nofollow rules while parsing HTML elements and attributes.

The filter is based on whitelists that can be defined from the filter settings
panel. Rules for HTML element and attributes are defined using the same syntax
of the TinyMCE valid_elements option.

The following elements cannot be whitelisted due to security reasons, to
prevent users from breaking site layout and/or to avoid posting invalid HTML.
Forbidden elements: applet, area, base, basefont, body, button, embed, form,
frame, frameset, head, html, iframe, input, isindex, label, link, map, meta,
noframes, noscript, object, optgroup, option, param, script, select, style,
textarea, title.

The section used to whitelist style properties is pretty simple. You just check
the properties you need from a list where almost all style properties are
organized into logical groups (Color and Background properties, Font, Text,
Box, Table, List, ...). The WYSIWYG Filter will strip out style properties not
explicitly enabled. On the other hand, for allowed style properties the WYSIWYG
Filter will check their values for strict CSS syntax (based on regular
expressions) and strip out those that do not match. Additional matching rules
are explicitly required for properties that may contain URLs in their values
("background", "background-image", "list-style" and "list-style-image"). If
rules don't match, these style properties will be ignored from user input.

When the "id" and "class" attributes have been whitelisted, it is also required
to specify explicit rules that will be used to validate user input, and again,
those that don't match will be stripped out.

As a measure to reduce the effectiveness of spam links, it is often recommended
to add rel="nofollow" to posted links leading to external sites. The WYSIWYG
Filter can easily do this for you while HTML is being processed with almost no
additional performance impact. There is a section in the filter settings panel
where a white/back list policy can be defined per domain name (the host part in
the URLs).


INSTALLATION
============

- Copy all contents of this package to your modules directory preserving
  subdirectory structure.

- Goto admin/build/modules to install the module.

- Goto admin/settings/filters and create a new input format as follows:

  - Input format name: WYSIWYG Filter (or something similar of your choice).
  - Check the filters: WYSIWYG Filter and HTML Corrector. Save.
  - Goto Rearrange tab.
  - Drag the WYSIWYG Filter on top of the HTML Corrector. Save.
  - Goto the Configure tab of your newly created WYSIWYG Filter and setup the
    available options to suit your needs.


SECURITY ISSUES
===============

- To report security issues, do not use the issue tracker of the module.
  Instead, please contact the Drupal Security Team or the WYSIWYG Filter
  module developer (preferred).

- To contact the WYSIWYG Filter module developer:
  http://drupal.org/user/39593
  http://drupal.org/user/39593/contact

- To contact the Drupal Security Team:
  http://drupal.org/security-team

- For any other kind of issue (support or feature requests, bug reports,
  translations, etc.), please, use the issue tracker of the module:
  http://drupal.org/project/issues/wysiwyg_filter

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Installation
 * Frequently Asked Questions (FAQ)
 * Known Issues
 * How Can You Contribute?


INTRODUCTION
------------

Maintainer: Narno <http://drupal.org/user/141690>
Maintainer: Dave Reid <http://drupal.org/user/53892>
Contributer: madler <http://drupal.org/user/123779>
Project Page: http://drupal.org/project/gravatar

This module integrates the Gravatar service with Drupal user pictures.


INSTALLATION
------------

See http://drupal.org/getting-started/install-contrib for instructions on
how to install or update Drupal modules.

User picture support (admin/config/people/settings) must be enabled for Gravatar
to work. Once Gravatar is installed and enabled, you can configure the module
at admin/config/people/gravatar.

You will also want to make sure user pictures are enabled for your theme at
admin/appearance/settings and the approprate user roles have the 'use gravatar'
permission assigned to them at admin/people/permissions.


FREQUENTLY ASKED QUESTIONS
--------------------------

Q: Is Gravatar support enabled by default for my users?
A: If their user role has the 'use gravatar' permission, yes Gravatar is enabled
   by default.


KNOWN ISSUES
------------

There are no known issues at this time.

To report new bug reports, feature requests, and support requests, visit
http://drupal.org/project/issues/gravatar.


HOW CAN YOU CONTRIBUTE?
---------------------

- Write a review for this module at drupalmodules.com.
  http://drupalmodules.com/module/gravatar

- Help translate this module on launchpad.net.
  http://localize.drupal.org/translate/projects/gravatar

- Report any bugs, feature requests, etc. in the issue tracker.
  http://drupal.org/project/issues/gravatar
# Media Filepicker.io - Integrate the Filepicker.io file selector into your site

## Description

Ever wanted to let users easily import picture from Facebook, or files from Dropbox, without having to deal with 10 different REST APIs and oAuth implementations?  Filepicker.io (https://www.filepicker.io/) lets you connect your site from everything from Dropbox to Gmail.  

This module lets you Adds a Filepicker.io tab to the media dialog so that you can easily browse images from  the Media Selector widget or your WYSIWYG editor.  After you have selected your image, you it is copied over to your Files directory so you can still apply Drupal file styles and access control.

The following services are currently supported by Filepicker.io (https://developers.filepicker.io/docs/web/#pick):
  - Box
  - Upload from Computer (via drag-and-drop)
  - Dropbox
  - Evernote
  - Facebook
  - Flickr
  - FTP
  - Github
  - Google Drive
  - SkyDrive
  - Picasa
  - Webdav
  - Gmail
  - Image Search
  - Instagram
  - URL
  - Video
  - Webcam


## Installation

Install as you would any other Drupal module:

1. Download the module and put it in sites/all/modules or sites/SITENAME/modules
2. Create an account on https://www.filepicker.io/
3. Go to admin/config/media/filepickerio and enter your Filepicker.io key and other customize the other settings
4. Enable Filepicker.io in your media field settings under "Enabled browser plugins"


## Who

Developed and maintained by Albatross Digital, http://www.albatrossdigital.com.  This module is currently not affiliated with Filepicker.io


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
Login integration for your site and the Pantheon control panel
---------------------------------------
PANTHEON MIGRATE MODULE README.TXT FILE
---------------------------------------

Table of Contents:
1.) Migrating to Pantheon
2.) Installing PEAR
3.) Installing Archive_Tar
4.) Troubleshooting Errors
=======================================

1.) Migrating to Pantheon

In order to migrate your site to Pantheon, you need to install and enable both the Backup and Migrate Module (http://drupal.org/project/backup_migrate) and the Pantheon Migrate module. Afterwards, using a user with the appropriate permissions you can initiate a migration on your local Drupal site here (admin/config/system/backup_migrate/export/pantheon) by creating a Pantheon Archive file. To complete the migration you need to copy the URL of the backup and paste it in the Pantheon Import area.

2.) Installing PEAR

The Pantheon Migration module requires the use of PEAR to load the Archive_Tar library which is necessary for the migration. Most systems already have PEAR installed, but if you need to install it you can do so by following these directions - http://pear.php.net/manual/en/installation.php.

3.) Installing Archive_Tar

The Pantheon Migration module requires the Archive_Tar PEAR extension to package your site for migration. You can download the Archive_Tar extension by following these instructions (http://pear.php.net/package/Archive_Tar/download) or by manually downloading the package (http://download.pear.php.net/package/Archive_Tar-1.3.7.tgz) and placing the Tar.php file in the pantheon_migrate folder.

4.) Troubleshooting Errors

The process of migrating a Drupal site can be complex and there are a number of errors that you might run into during that process. Please consult these common problems and the contact Pantheon Support (https://getpantheon.com/support/contacting-pantheon-support) if you have further questions.

Memory Problems Creating a Pantheon Archive - The archive process often takes more memory than is normally available to PHP. If you need more memory, read this documentation (http://drupal.org/node/207036) on how to increase the amount of available memory.

Problems with Symbolic Links - If your site makes use of symbolic links, they have been known to confuse the Pantheon Archive functionality. If you see problems with symbolic links, we recommend you review your symbolic links before attempting to migrate again.

Problems with Firewalls or Localhost Migrations - The Pantheon Migration process requires that the Pantheon servers are able to access your Pantheon Archive file directly. If your site is behind a firewall or if your site is on localhost, the automatic migration will not work. Instead, download the archive file and upload it manually to Pantheon.

Reverse Proxy - If your existing drupal site is behind a reverse-proxy cache (e.g. Varnish) and your archive is very large in size, you may need to go around the proxy to successfully transfer the file. Often this is done using an alternat port (e.g. :8080). Contact your local system administrator if you need help with this.

Pantheon Error: "Not a valid tar/zip archive" - There are a number of things that can cause this error, but the most common one is that Pantheon cannot read the file correctly do to one of the above problems. Make sure the import URL is accessable and the archive is valid. In most cases, you should be able to download and extract the archive on your desktop using the same URL as you supply to Pantheon.
The Migrate Extras module provides extensions to Migrate (http://drupal.org/project/migrate)
to support various contributed modules. The ideal place to implement migration support
for a contributed module is in that module. That way, the migration support is always
self-consistent with the current module implementation - it's not practical for the
migrate_extras module to keep up with changes to all other contrib modules. Support
for contributed modules may be added to migrate_extras for two reasons - if the module's
maintainer does not accept a patch providing migration support, or as an intermediate
step before submitting such a patch to the other module.

In cases where modules supported by migrate_extras end up implementing the support
themselves, you could at least temporarily end up with redundant implementations.
The extra implementation may be disabled at admin/content/migrate/configure.

The following modules are currently supported in Migrate Extras on Drupal 7 (note
that Date module support has moved into the Date module itself):

Address Field
Entity API
Flag
Geofield
Interval
Media
Name Field
Pathauto
Phone Number (cck_phone)
Private Messages
Profile2
Rules
User Relationships
Voting API
Webform

Compatibility
-------------
This release of Migrate Extras requires Migrate V2.4-beta1 or later.

Migrate_Extras_Examples
----------------
See the Examples folder for a few implemented Migrations that you can run and
inspect.

Maintainers
-----------
Frank Carey http://drupal.org/user/112063
Mike Ryan - http://drupal.org/user/4420
Moshe Weitzman - http://drupal.org/user/23

r4032login
--------------------------------------------------------------------------------
Redirect the HTTP 403 error page to the Drupal /user/login page with a message
that reads, "Access denied. You must login to view this page." Also, a redirect
to the desired page is appended in the url query string so that, once login is
successful, the user is taken directly where they were originally trying to go.

Makes for a much more user-friendly Drupal.

Installation
--------------------------------------------------------------------------------

Extract and enable r4032login.
Configure at admin/config/system/site-information .

Support
--------------------------------------------------------------------------------
This open source project is supported by the Drupal.org community. To report a
bug, request a feature, or upgrade to the latest version, please visit the
project page:

  http://drupal.org/project/r4032login

README.txt
==========

********************************************************************
This is i18nviews package 7.x, and will work with Drupal 7.x
********************************************************************

This module extends i18n with multilingual support for views.
These modules will build onto Drupal 7 core features enabling a full multilingual site


Up to date documentation will be kept on-line at http://drupal.org/node/133977

Additional Support
=================
For support, please create a support request for this module's project:
  http://drupal.org/project/i18nviews

Support questions by email to the module maintainer will be simply ignored. Use the issue tracker.

Now if you want professional (paid) support the module maintainer may be available occassionally.
Drop me a message to check availability and hourly rates, http://md-systems.ch/contact

====================================================================
Miro Dietiker, miro dot dietiker at md-systems dot ch, http://www.md-systems.ch
Jose A. Reyero, drupal at reyero dot net, http://reyero.net
Description
===========
Allows the contents of an "Entity Reference" field to be pre-populated by
taking a parameter from the URL path.

Install
=======
1. Download and enable the module.
2. Visit admin/structure/types/manage/[ENTITY-TYPE]/fields/[FIELD-NAME]
3. Enable "Entity reference prepopulate" under the instance settings.


Configuration
=============
Enable Entity reference prepopulate:
  Check this to enable Entity reference prepopulate on this field.
Action
  Using the select box choose the action to take if the entity reference
  field is pre-populated.
Fallback behaviour
  Select what to do if the URL path does NOT contain a parameter to
  pre-populate the field.
Skip access permission
  This is a fallback override, the fallback behaviour will not be followed
  for users with the specified permission.

Usage
=====
In order to pre-populate an entity reference field you have to supply the
parameter in the URL.

The structure is
node/add/article?[field_ref]=[id]

Where [field_ref] is the name of the entity reference field and [id] is
the id of the entity being referenced.

Examples:
node/add/article?field_foo=1
node/add/page?field_bar=1,2,3



README - TAXONOMY MANAGER 
**************************


SHORT PROJECT DESCRIPTION
--------------------------
This module provides a powerful interface for managing vocabularies of the taxonomy module.
It's especially very useful for long sets of vocabularies.

Features:
  * dynamic tree view
  * mass deleting
  * mass adding of new terms
  * moving of terms in hierarchies
  * merging of terms (Term merge module)
  * fast weight changing with up and down arrows (and AJAX saving)
  * AJAX powered term editing form
  * simple search interface


REQUIREMENTS
------------
  - Taxonomy module enabled
  - JavaScript enabled in your browser
  - a user with 'administer taxonomy' permission


INSTALLATION
------------
1. Place the entire taxonomy_manager directory into your Drupal sites/all/modules/ directory.

2. Enable the taxonomy manager module by navigating to:

     administer > site building > modules


UPGRAGE to 7.x
---------------
The table 'taxonomy_manager_merge' is deprecated and won't be used by now. This table stores
which terms were merged into which destination term. If you do not need this information, you
can manually remove this table.


USING THE TAXONOMY MANAGER
--------------------------
To use the Taxonomy Manager go to administer > content management > taxonomy manager. This page
contains a list of all available vocabularies. By clicking at one of the vocabularies, you get 
redirected to the Taxonomy Manager interface, where you can edit the whole tree structure and
terms. 
If you want to edit any general vocabulary settings or if you want to create a new one, go to 
the categories (administer > content management > categories) page.

The interface contains a search bar, a toolbar with some operations, a tree view and if a term
gets selected a form for editing the term data.
The following lines describe all operations and some terminology.

 - Tree View
     The tree view shows all terms of the vocabulary with their hierarchical relations. If your
     list of terms gets very long, there is a paging mechanism included with a page size of 50 terms. 
     If you are having hierarchical vocabularies, all parent terms have a plus symbol, which 
     means you can expand them to show their child terms. Use the minus symbol to collapse
     them again.
     In multiple hierarchies, if one term has more parents, the term gets shown under 
     each of its parents. 
     
 - Adding of terms
     For adding new term, click on the 'Add' Button. A fieldset containing some textfields expands.
     If you want to close this fieldset, click 'Cancel'.
     To insert a new term, fill in any textfield. Each textfield can only contain one term. 
     You don't have to fill in all textfields, they can be left empty. 
     Depending on your hierarchy settings, it's possible to insert terms and to directly assign 
     a parent to them. If you want to do this, select a parent term in the tree view by marking 
     the checkbox. If you have multiple hierarchies enabled, it's even possible to assign the 
     new inserted terms to more parents at once by selecting more terms in the tree view.
     
 - Weight Editing
     Every term has a weight. This weight determines the position the terms get listed. If terms
     have the same weight, they are ordered alphabetically. 
     If you want to change the weight, you have 3 ways to do that.
       1st way: select the terms you want to move by one position (can be more terms at once) and press
                either the up or the down button in the toolbar. All saving is done automatically through 
                AJAX.
       2nd way: every term in tree view has a mouseover effect. When you move your mouse over a term, two
                small up and down arrows will appear. Click them to move this term by one
                position.
       3rd way: click on the term, where you want to change the weight. A form for editing the 
                term data appears on the right side of the tree view. At the bottom of this 
                form, there is a select field, which shows the current weight. By changing the
                value, the tree view gets automatically reordered and the values are saved to the
                database through AJAX.
 
 - Deleting
     If you want to delete terms from the vocabulary, select them by marking the checkbox and click
     the 'Delete' button. A fieldset, where you have to confirm the deletion, expands. 
     For hierarchical vocabularies (single or multi), the fieldset contains an option, which says:
     'Delete children of selected, if there are any'. Check this if you want to delete all children 
     of a selected parent term. Otherwise, if you are deleting the last parent of terms, the terms
     get added to root level.

 - Moving
     This operation is only available in hierarchical (single or multiple) vocabularies. It allows
     you to change hierarchies by moving terms from one parent to one other.
     Select all terms you want to move by marking the checkbox. Click the 'Move' button. A fieldset with
     some options expands.
     This fielset contains a autocomplete field, where you have to determine the parent term (under which
     the terms should be moved). If you want to move terms to the root level, leave this field empty. 
     This autocomplete form allows you to either choose a parent term from the list of exisitng terms
     or to insert a new terms, which will be used as parent (this parent term will be added to the root 
     level). 
     In multiple hierarchical vocabularies, it's possible to move terms to more parents in one step by
     inserting more terms into the autocomplete field and separating them by commas. Additional, there
     appears an option ('Keep old parents and add new one'), which prevents the replacing of old parents.
 
 - Merging
     With the merging action, you can put terms with the same meaning together (e.g. your vocabulary
     contains: SoC, Summer of Code, GSoC, Google Summer of Code). All terms, that get merged into 
     one other, get synonyms of resulting term (here called merged or main term). Additional
     all term-node association gets automatically updated (this means nodes, that had a merging term
     assigned, now get the resulting merged term instead). All merging terms are deleted afterwards. 
     In the Taxonomy Manager, you can do that by selecting all terms you want to merge and to click
     the 'Merge' button. A fieldset with an autocomplete field an some options expands. In the 
     autocomplete field you have to specify the resulting merged term (into which the selected get merged). 
     The merged term can be either chosen from the list of existing terms or can be inserted automatically
     and used as merged term.
     Additional, there are some options available (they depend on the vocabulary settings). If you want
     to add any kind of relations (parents, children, related terms) from the merging terms to the
     resulting merged term, select one (or more) of them.
     
     The default taxonomy term page, which shows all assigned nodes, is overriden by the Taxonomy
     Manager, so that former merged terms can be considered (if someone calls a term, that was merged, 
     it redirects to the resulting merged term).
     
     NOTE: At the moment, the Taxonomy Manager only cares about the term-node association inserted
           into the term_node table (by the taxonomy module). If you are using any CCK modules, like 
           CCK Taxonomy or Content Taxonomy, which (can) save the term - node association in cck tables, 
           don't use the Merging action, because changes are not handled.
           If you are using Views filters instead of the default taxonomy term page, merged terms are 
           either respected.
           If you want to customize this by yourself or have some other module, you can use following 
           function taxonomy_manager_merge_get_main_term($tid) for getting the main term id (if there 
           is any main term, else return 0). The term merge history gets saved in the 
           taxonomy_manager_merge table (main_tid, merged_tid) and gets additional cached, so that 
           checking for a merged terms causes nearly no performance loss.
 
 - Editing term data
     If you want to edit or read some term properties, click on the term. A fieldset on the right side
     of the tree view gets loaded. This contains all term related information and can be edited. If you
     want to change the term name or the description, fill in any changes you want and click the saving 
     symbol. All saving is done through AJAX, so no reload is necessary.
     Additional, this page contains listing of synonyms, related terms and parents (depends on your 
     vocabulary settings). 
     Every listed entry has an delete operation. By clicking the delete symbol, the relation gets deleted.
     In case of synonyms, the names get deleted from the database. If you are deleting a related term or a 
     parent, this doesn't delete the term itself, only the relation. 
     For adding new synonyms, the listing has a textfield below. Insert there any new synonym and click the 
     plus symbol.
     For adding a new related term or a new parent (if multi hierarchy), there is a autocomplete field below
     the listing. Use this to insert new terms or to choose existing ones and assign them to the current term. 
 
 - Using the search
     At the top of the page, there is a collapsed fieldset, called 'Search'. This search allows you to 
     directly select an existing term for editing. Else, if your input doesn't match an existing term, 
     the value will be used for filtering root level terms (this doesn't affect any child term).



AUTHOR
------
Matthias Hutterer 
User: mh86@drupal.org
Email: m_hutterer@hotmail.com

Context OG for Context 3.x for Drupal 6.x
-----------------------------------------
Context OG provides some Organic Groups related conditions and reactions
for Context.  If you are already familiar with the Context module and its
conditions and reactions then this module should help you fill in the missing
pieces in regards to Organic Groups.

Installation
------------
1. Context can be installed like any other Drupal module -- place it in
the modules directory for your site and enable it.

2. Currently you must clear all caches (the button on the
admin/settings/performance screen is one way to do it) in order to
see the new conditions and reactions that are provided by this module.

Maintainers
-----------
This module was developed by the friendly primates at FunnyMonkey.com.

INTRODUCTION
------------

This module provides an API for adding universally unique identifiers (UUID) to
Drupal objects, most notably entities.

FEATURES
--------

 * Automatic UUID generation:
   UUIDs will be generated for all core entities. An API is provided for other
   modules to enable support for custom entities.
   See https://www.drupal.org/node/2387671
 * UUID API for entities, properties and fields:
   With this unified API you can load entities with entity_uuid_load() so that
   all supported properties and fields are made with UUID references. You can
   also save entities formatted this way with entity_uuid_save() (depends on
   Entity API).
 * Export entities to use as default/demo content:
   The integration with Features module provides the ability to export UUID
   enabled entities with intact dependencies and references to other entities.
   This functionality depends on Deploy module 7.x-2.0-alpha1 (soon to be
   released) and is probably the most robust way for installation profiles and
   distributions to provide demo content!
 * Services integration:
   The integration with Services module alters all UUID enabled entity resources
   (nodes, users, taxonomies etc) to be based on UUIDs instead. This way it
   becomes easier to share and integrate content between sites. This
   functionality is used by Deploy module.
 * More integrations:
   UUID module integrates with Views, Token, Rules and provides some CTools
   plugins.
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
Twitter
-------
The Twitter module allows listing tweets in blocks or pages. Its integration
with Views opens the door to all sorts of formatting (ie. as an automatic
slideshow with views_slideshow). It also provides useful input filters to easily
link Twitter accounts and searches within text.

Twitter's submodules allow posting to twitter, executing actions/rules when
tweeting, login with a Twitter account, or listing the most recent tweet from a
specific account.


Installation
--------------------------------------------------------------------------------
The OAuth module is required:
  https://www.drupal.org/project/oauth

When installing the Twitter module without the above being available, Drupal
will complain about a missing "oauth_common" module. This module is actually
provided by the OAuth project - the module name and project name are not the
same, hence this error.

Once OAuth and Twitter have been enabled, go to admin/config/services/twitter
and follow the instructions in order to provide the Twitter Application keys.

Further installation instructions can be found at:
  https://www.drupal.org/node/1346824


How to use the username, hashtag and embedded tweet input filters
--------------------------------------------------------------------------------
1. Go to admin/settings/filters.
2. Select the text format where the filters are to be added to.
3. At "Enabled filters" check the Twitter filters.

After that, clear cache and try to create a page with the following body:

#drupal @drupal

This will link to a search in Twitter for the #drupal hashtag, and to the
@drupal account profile page.

To display a single tweet in a page, insert a full URL to a tweet in a node's
body field, e.g.:

https://twitter.com/drupal/status/580521032664145920

These filters are avilable when configuring list of tweets in Views.

Note: These filters may be used without OAuth being configured.



How to post to Twitter
--------------------------------------------------------------------------------
 1. Install and configure OAuth, as described above.

 2. Verify permissions at admin/people/permissions:
    - Post a message to Twitter
      Users with this permission will be able to post to Twitter using an
      authenticated account that they have added to the site.
    - Post a message to Twitter using a global account
      Users with this permission will be able to post to Twitter using an
      account that is set up with the "is global" option.

 3. Go to the "Manage fields" page for a content type, or other entity (taxonomy
    terms, etc), that is to be used to notify Twitter. Add a new field by
    filling in a field name, selecting "Twitter" as the field type and "Post to
    Twitter" as the field widget, and clicking "Save". Fill in the default
    string to be used when posting new tweets and click "Save".

 4. Add a Twitter account and try to edit or post content.

Further information can be found at https://www.drupal.org/node/1016584.


How to sign in with Twitter
--------------------------------------------------------------------------------
Existing and new users can sign in with Twitter by enabling the twitter_signin
module. The following scenarios are being supported so far:

* A visitor logs in with their Twitter account and, once authenticated at
  Twitter.com, fills in their email in the Drupal registration form and receives
  an email to log in and their account password.

* An existing user signs in with Twitter and then logs in into their Drupal user
  account. This results in the Twitter account mecoming related to the user
  account so next time Twitter sign-in will work.

* An existing user with an already configured Twitter account can log in
  automatically by clicking on the "Sign in with Twitter" button.


Credits / Contact
--------------------------------------------------------------------------------
Currently maintained by Damien McKenna [1]. Originally written by James Walker
[2] with many contributions by Michael Hellein [3], Juampy Novillo Requena [4],
Chris Burgess [5], Jeff Eaton [6] and others in the community.

Ongoing development is sponsored by Mediacurrent [7].

The best way to contact the authors is to submit an issue, be it a support
request, a feature request or a bug report, in the project issue queue:
  https://www.drupal.org/project/issues/twitter


References
--------------------------------------------------------------------------------
1: https://www.drupal.org/u/damienmckenna
2: https://www.drupal.org/u/walkah
3: https://www.drupal.org/u/michaek
4: https://www.drupal.org/u/juampynr
5: https://www.drupal.org/u/xurizaemon
6: https://www.drupal.org/u/eaton
7: http://www.mediacurrent.com/

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
LLC (midwesternmac.com), and sponsored by flockNote (flocknote.com).********************************************************************
                COUNTDOWN TIMER FIELD M O D U L E
********************************************************************
Original Author: Varun Mishra
Current Maintainers: Varun Mishra
Email: varunmishra2006@gmail.com

********************************************************************
DESCRIPTION:

   Countdown timer field module allows you to create countdown timer
   field to count the days, hours, minutes, and seconds until a specified
   event. The module uses jQuery Countdown Timer to display the countdown
   timer in a nice graphical way.


********************************************************************

INSTALLATION:

1. Place the entire field_countdown directory into sites modules directory
  (eg sites/all/modules).

2. Enable this module by navigating to:

     Administration > Modules

3) This module have dependency on date_popup and libraries module.

4) Download jQuery Countdown Timer Library from
   http://tutorialzine.com/2011/12/countdown-jquery/ . Install it in
   sites/all/libraries directory, and rename the directory to jquery-countdown.
   The library should be available at a path like 
   sites/all/libraries/jquery-countdown/assets/countdown/jquery.countdown.js

5) Please read the step by step instructions as an example to use this
   module below:-

a) Install the module. 

b) Go to admin/structure page. Click on manage fields of any content type.

c) Add new field and select "Countdown Timer Field" From Field type. 

d) Now you timer field is ready to use. 

e) Click on Manage Display link to select how do you want to display this field.

f) There are 4 display formats available:-
    I)   jQuery Countdown Timer without text timer.
    II)  jQuery Countdown Timer with text timer.
    III) Date and time as string.
    IV)  Unix time stamp.
ABOUT MENU POSITION
-------------------

Often times site builders want certain types of content to appear in a specific
position in the navigational menu. The simplest solution, adding all of that
content individually to the menu system, has performance and usability issues.
(Imagine hundreds of menu items added to one spot in the menu.)

This module allows for the creation of rules that will dynamically add the
current page into the menu system at the requested spots.

This includes affecting:
* The main links of the theme
* The secondary links of the theme
* The breadcrumb trail
* Menu blocks provided by core's Menu module
* Menu blocks provided by the Menu Block module


RULE CHECKING
-------------

Rules can be added, modified, re-ordered, disabled and deleted from the admin
page available at: Structure > Menu position rules

When multiple rules are enabled, the rules are checked as followed:
* Disabled rules are not evaluated.
* Enabled rules are evaluated in the order they appear on the "Menu position
  rules" administration form.
* The menu name used by the rule is checked to see:
  * if a menu item for the current page's path is already included in the
    specified menu, the rule is skipped.
  * if this rule's menu was used in a previously-matched rule, the rule is
    skipped.
* For each condition in the rule, the condition is evaluated. If all of the
  conditions are determined to be TRUE, the rule is "matched".
* If the rule contains no conditions, the rule is "matched".

Once a rule is "matched", the following things happen:
* If the rule's chosen menu is the "Source for the Main links" (as defined by
  the Menu Settings form at Structure > Menus > Settings), the theme's main
  links will be affected by the active trail specified in the rule.
* If the rule's chosen menu is the "Source for the Secondary links" (as defined
  by the Menu Settings form at Structure > Menus > Settings), the theme's
  secondary links will be affected by the active trail specified in the rule.
* Any menu trees generated by blocks or page content will be affected by the
  active trail specified in the rule.
* If this is the first matched rule and no rules were skipped because their
  menu already contained a menu item for the current page, the theme's
  breadcrumbs will be affected by the active trail specified in the rule.


PLUG-INS
--------

Currently, the Menu position module only provides "content type" and "pages"
plug-ins that allow conditions to be added to rules based on the type of content
being displayed or on the path of the page. However, this module also provides a
simple API for "rule conditions" plug-ins so module developers can develop their
own logic for adding dynamic menu positioning.

See the following files for more information:
- menu_position.api.php
- menu_position.example_plugin.inc
- menu_position.node_type.inc

The External Links module is a very simple approach to adding icons to links
to external websites or e-mail addresses. It is a purely JavaScript
implementation, so the icons are only shown to users that have JavaScript
enabled.

External Links was written by Nathan Haug.
Built by Robots: http://www.lullabot.com

Install
-------
Simply install External Links like you would any other module.

1) Copy the extlink folder to the modules folder in your installation.

2) Enable the module using Administer -> Modules (/admin/build/modules).

3) No additional configuration is necessary though you may fine-tune settings at
   Administer -> Site configuration -> External Links (/admin/settings/extlink).

A note about the CSS
--------------------
This module adds a CSS file that is only a few lines in length. You may choose
to move this CSS to your theme to prevent the file from needing to be loaded
separately. To do this:

1) Open the .info file for your theme, add this line of code to prevent
   the extlink.css file from loading:
   stylesheets[all][] = extlink.css
2) Open the extlink.css file within the extlink directory and copy all the code
   from the file into your theme's style.css file.
3) Copy the extlink.png and mailto.png files to your theme's directory.

Note that you DO NOT need to make a extlink.css file. Specifying the file in the
info file is enough to tell Drupal not to load the original file.

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
Copy the 'googleanalytics' module directory in to your Drupal
sites/all/modules directory as usual.

Upgrading from 6.x-3.x and 7.x-1.x
==================================
If you upgrade from 6.x-3.x and 7.x-1.x (ga.js) to 7.x-2.x (analytics.js) you
should verify if you used custom variables. Write down your settings or make a 
screenshot. You need to re-configure the settings to use custom dimensions or
metrics. There is no automatic upgrade path for custom variables feature. All
other module settings are upgraded automatically.

See https://support.google.com/analytics/answer/2795983?hl=en for more details.

Usage
=====
In the settings page enter your Google Analytics account number.

All pages will now have the required JavaScript added to the
HTML footer can confirm this by viewing the page source from
your browser.

Page specific tracking
======================
The default is set to "Add to every page except the listed pages". By
default the following pages are listed for exclusion:

admin
admin/*
batch
node/add*
node/*/*
user/*/*

These defaults are changeable by the website administrator or any other
user with 'Administer Google Analytics' permission.

Like the blocks visibility settings in Drupal core, there is a choice for
"Add if the following PHP code returns TRUE." Sample PHP snippets that can be
used in this textarea can be found on the handbook page "Overview-approach to
block visibility" at http://drupal.org/node/64135.

Custom dimensions and metrics
=============================
One example for custom dimensions tracking is the "User roles" tracking.

1. In the Google Analytics Management Interface (http://www.google.com/analytics/)
   you need to setup Dimension #1 with name e.g. "User roles". This step is
   required. Do not miss it, please.

2. Enter the below configuration data into the Drupal custom dimensions settings
   form under admin/config/system/googleanalytics. You can also choose another
   index, but keep it always in sync with the index used in step #1.

   Index: 1
   Value: [current-user:role-names]

More details about custom dimensions and metrics can be found in the Google API
documentation at https://developers.google.com/analytics/devguides/collection/analyticsjs/custom-dims-mets

Advanced Settings
=================
You can include additional JavaScript snippets in the custom javascript
code textarea. These can be found on the official Google Analytics pages
and a few examples at http://drupal.org/node/248699. Support is not
provided for any customisations you include.

To speed up page loading you may also cache the Google Analytics "analytics.js"
file locally.

Manual JS debugging
===================
For manual debugging of the JS code you are able to create a test node. This
is the example HTML code for this test node. You need to enable debugging mode
in your Drupal configuration of Google Analytics settings to see verbose
messages in your browsers JS console.

Title: Google Analytics test page

Body:
<ul>
  <li><a href="mailto:foo@example.com">Mailto</a></li>
  <li><a href="/files/test.txt">Download file</a></li>
  <li><a class="colorbox" href="#">Open colorbox</a></li>
  <li><a href="http://example.com/">External link</a></li>
  <li><a href="/go/test">Go link</a></li>
</ul>

Text format: Full HTML
Readme
------
Tagclouds is a small module forked from Tagadelic, without any databases, or configuration, that generates pages with weighted tags.
Tagclouds is an out of the box, ready to use module, if you want simple weighted tag clouds. With, or without some small CSS moderations this will probably suit most cases.
Unlike Tagadelic, Tagclouds does not claim to be an API.
Tagclouds supports the module i18n, if available see notes below for entity translation configuration and testing.

HOWTO - tags per entity with entity translation enabled
To test this patch:

 1    enable entity translation if it isn't already (or use a distro like this)
 2    create taxonomy vocabulary with translation mode "Translate." enabled (Different terms will be allowed for each language and they can be translated.)
 3    add taxonomy term reference field to basic page content type
 4    (options: use autocomplete widget)
 5    (more options: enable translation on taxonomy term reference field)
 6    install and enable tagclouds
 7    enable "Separation of Tags per language using entity translation" in eng/admin/config/content/tagclouds
 8    add tagclouds block to a panel or page
 9    add new basic page , add two taxonomy terms to your autocomplete taxonomy term reference field "taxonomy1-eng, taxonomy2-eng"
10   translate the same basic page (entity translation so the same "entity id /node id") , add terms "taxonomy1-lang2, taxonomy2-lang2"
11   add a second basic page, and translate it as done in step 7 and step 8, (use same taxonomy (tag) names "taxonomy1-eng, taxonomy2-eng" for english and "taxonomy1-lang2, taxonomy2-lang2" for the "other " language
12   compare results, you should see tag clouds for both english and lang2

KNOWN ISSUES: when your tag is common to both languages it will only show up in the language it was first saved to.  
For example the word "corruption" is spelled exactly the same in English as well as French and possibly other languages.
Until an enhancement to this module is created you can workaround this by naming the tag "le corruption" .
README for the Imagecache Actions Drupal module
-----------------------------------------------

Project page: https://drupal.org/project/imagecache_actions

Current and past maintainers for Imagecache Actions:
- dman (https://drupal.org/user/33240)
- sidneyshan (https://drupal.org/user/652426)
- fietserwin (https://drupal.org/user/750928)


Release notes for 7.x-1.x-dev
-----------------------------
- Clear all caches after updating.


Release notes for 7.x-1.4
-------------------------
- This release supports image labels as introduced by Drupal 7.23.
- See CHANGELOG.txt for a full overview of changes.


Release notes for 7.x-1.1
-------------------------
- If you use the module:// notation anywhere in an image effect, you must now
  install the System Stream Wrapper module
  (https://drupal.org/project/system_stream_wrapper).
- Clear the cache after updating.


Release notes for 7.x-1.0
-------------------------
- Clear the (registry) cache after installing or updating to 7.x-1.0.
- If you use custom actions, run update.php.
- If you use custom actions, be sure to enable the 'PHP filter' module and give
  image style editors that may create custom actions the 'use PHP for settings'
  permission. The module must also be enabled on image creation.
- If you use custom actions, please read the README.txt from that sub-module to
  find out about how information and resources are available to you. You will
  probably have to change your code snippets.
- If you use effects that use files (mask, overlays, underlays, text fonts),
  check the way they are specified. From 7.x-1.0 on, you have to specify the
  location using one of the schemes private://, public://, module:// or
  temporary://. If no scheme is specified, the file is searched for as is, thus
  relative to the current directory or as an absolute path.
- Effects that use the transparency layer (e.g. mask, rounded corners) do not
  automatically convert to PNG anymore. Use the "Change file format" for that.
- There's no upgrade from D6. You will have to recreate your styles manually.

Warning:
  Ongoing development in the area of e.g. making the effects more consistent,
  adding and/or removing parameters or redefining their meaning, might cause
  backward incompatibilities between future versions and the current version.
  Thus, we cannot and do not guarantee backwards compatibility or automatic
  upgrade paths for future versions.


Introduction
------------
The Imagecache Actions module provides a suite of additional image effects that
can be added to image styles. Image styles let you create derivations of images
by applying (a series of) effect(s) to it. Think of resizing, desaturating,
masking, etc.

Furthermore, imagecache_actions extends the administrative interface for image
styles by providing additional features. It does so in the "Image styles admin"
sub module.

The additional effects that Imagecache Actions provides include:
- Watermark: place a image with transparency anywhere over a source picture.
- Overlay: add photo-corners etc to the image
- Text overlay: add e.g. a copyright notice to your image.
- Color-shifting: colorize images.
- Brighten/Darken.
- Alpha blending: use a gray scale image to define the transparency layer of an
  image.
- Canvas manipulation: resize the canvas and add a background color or image.
- File Format switcher: if you need transparency in JPGs, make them PNG. If your
  PNG thumbnails are 30K each, save them as JPGs.
- Rounded corners.
- TODO: complete list, check short descriptions

These effects are grouped in sub-modules. Just enable the ones you want to use.
TODO: list sub-modules and their sets of effects.

Imagecache Actions supports both the GD toolkit from Drupal core and the
Imagemagick toolkit. However, please note that Imagemagick support is not yet
complete. Please file an issue if you encounter problems in using Imagemagick.


What is imagecache_action not?
------------------------------
Imagecache Actions does not provide a new UI or new menu items. It hooks into
the already existing image styles system (from Drupal core). See
https://drupal.org/documentation/modules/image for more information about
working with images.


A note about the name of this module
------------------------------------
Image styles are part of Drupal 7 core and are the successor of the Drupal 6
imagecache module. In Drupal 6 image styles were called (imagecache) presets and
the separate effects that made up a style were called (imagecache) actions. In
porting to D7, that name has not been changed (yet).


Which toolkit to use?
---------------------
Personally, I (fietserwin) prefer the imagemagick toolkit:
- It is better in anti-aliasing. Try to rotate an image using both toolkits and
  you will see what I mean.
- It does not execute in the PHP memory space, so is not restricted by the
  memory_limit PHP setting.
- The GD toolkit will, at least on my Windows configuration, keep the font file
  open after a text operation, so you cannot delete, move or rename it anymore.

On the other hand: the GD toolkit is always available (in the correct version),
whereas imagemagick is not always present on shared hosting or may be present in
an antique version that might give problems.

Please also note that effects may give different results depending on the
toolkit used.


Hard Dependencies
-----------------
- Image module from Drupal core

At least 1 of the available image toolkits:
- GD toolkit from Drupal core.
- Imagemagick toolkit: https://drupal.org/project/imagemagick.


Soft Dependencies
-----------------
- System stream wrapper (https://drupal.org/project/system_stream_wrapper)
- Remote stream wrapper (https://drupal.org/project/remote_stream_wrapper)
These modules provide additional stream wrappers. Especially the system stream
wrapper is very handy as it provides, among others, a module:// and theme://
wrapper.


Installing
----------
As usual.


Usage
-----
After enabling the module:
- Assure that the Image module from core is enabled.
- Configure your toolkit and its settings at admin/config/media/image-toolkit.
- Define image styles at admin/config/media/image-styles and add 1 or more
  effects as defined by this module
- Use the image styles via e.g. the formatters of image fields.


Upgrading from D6
-----------------
There's no upgrade path defined for sites upgrading from D6 to D7. This means
that you will have to manually redefine your D6 imagecache presets as D7 image
styles. Note that actually an upgrade path would have to be defined by the
imagecache module, not this imagecache actions module. However, as there is no
D7 version of imagecache that provides an upgrade, users may post an upgrade
function to the issue queue and we will incorporate it.


Backwards compatibility
-----------------------
Future releases will not be guaranteed to be backwards compatible. Implementing
Imagemagick support e.g. might give unforeseen problems that can only be solved
by changing the details of what an effect does. We will document these kind of
incompatibilities in the changelog and the release notes.


File form fields
----------------
A number of effects have a file form field where the editor can define a file
name to use. This can be e.g. for overlays, masks or fonts. The file name should
be defined using either:
- 1 of the (enabled) scheme's:
  * public://
  * private:// Preferred for site specific masks, overlays, etc, that do not
    need to be shared publicly.
  * temporary:// Unlikely to be useful, but supported anyway as all schemes are
    supported.
  * module:// Introduced by the system stream wrapper module and preferred for
    module provided resources.
  * theme:// idem.
  * profile:// idem.
  * library:// idem.
- A relative (to the current directory, probably Drupal root) or absolute path.


Support
-------
Via the issue queue of this project at Drupal.org.


Known problems
--------------
These are better documented in the issue queue, but might be listed here (as
well).

- Underlay does not work in imagemagick if the dimensions of both images are not
  equal. As a workaround first add a canvas effect with a fully transparent
  background.
- Underlay/overlay: keywords in the x and y offset fields do not work.
- Underlay does still display a message about Imagemagick not being supported.
- Brightness values outside the -250 .. 250 range are accepted.
- Check color fields that allow a transparency component or allow to be empty to
  specify fully transparent.

Known problems: Imagemagick
---------------------------
- Define canvas using offsets may bot work on older versions. We have an error
  report for version 6.5.4.7 (2009-07) (https://drupal.org/node/888644).
README
------
README for the custom actions effect module.


Dependencies
------------
Hard dependencies:
- Imagecache actions.
- Image (Drupal core).

Soft dependencies/recommended modules:
- Imagemagick (preferred toolkit).
- PHP filter (Drupal core).


Which toolkit?
--------------
Personally, I prefer the imagemagick toolkit:
- It is better in anti-aliasing, try to rotate an image using both toolkits and
  you will see what I mean.
- It does not execute in the PHP memory space, so is not restricted by the
  memory_limit PHP setting.
- The GD toolkit will, at least on my Windows configuration, keep font files
  open after a text operation, so you cannot delete, move or rename it anymore.


Installing
----------
As usual. After enabling the module you can add custom actions to images.


Custom action PHP snippets
--------------------------
Given the correct permission, the custom action effect allows you to write your
own PHP snippet that does the requested processing on the image. How it can do
so, depends on the toolkit.

For all toolkits, the snippet should return true to indicate success and false
to indicate failure.

GD
--
The GD image resource is available in $image->resource. You can call the GD
functions on this resource. This effect will query the width and height after
your processing, so you don't have to change that yourself.

Imagemagick
-----------
All real image processing is done at the end, if all effects have added their
command line arguments to the $image->ops array. So your custom action should
add the imagemagick commands and its parameters by adding new string entries to
the end of that array.

If your commands change the width or height of the resulting image, you should
record so by changing $image->info['width'] and/or $image->info['height'].

General
-------
To ease your task, this effect makes some information regarding the image being
processed available in 2 variables: $image and $image_context. These variables
are readily available in your snippet.

$image is an object containing the following properties:
- source: string, the source of the image, e.g. public://photo.jpg
- info: array, example data:
   - width (int) 180
   - height  (int) 180
   - extension (string) png
   - mime_type (string) image/png
   - file_size (int) 4417
- toolkit: string, imagemagick or GD
- resource: resource. The GD image resource.
- ops: array. An array of strings with the ImageMagick commands.

$image_context is an associative array containing:
- effect_data: array, the data of this image effect, example data for the custom
  action effect:
   - php  (string)
- managed_file: object|null. A managed file object containing these properties:
   - fid (string) 2
   - uid (string) 1
   - filename  (string) photo.jpg
   - uri (string) public://photo.jpg
   - filemime  (string) image/jpeg
   - filesize  (string) 445751
   - status  (string) 1
   - timestamp (string) 1327525851
   - metatags  Array [0]
   - rdf_mapping Array [0]
- referring_entities: array|null. A nested array with (fully loaded) entities
  referring to the current image. The 1st level of entries is keyed by the field
  name, the 2nd by entity type, and the 3rd by entity id. Example data:
   - field_photo Array [1]
      - node  Array [1]
         - 12  Object of: stdClass
            - nid (string) 12
            - vid (string) 12
            - type  (string) page
            - author ...
            - timestamp ...
            - ...
- entity: object|null, the 1st entity in referring_entities. This is for easy
  access to the referring entity if it may be assumed that only 1 entity is
  referring to the current image.
- image_field: array|null, the 1st image field in entity that is referring to
  the current image. This is for easy access to the image field data if it may
  be assumed that only 1 image field is referring to the current image. Example
  data:
   - fid (int) 2
   - alt (string) ...
   - title (string) ...
   - ...

Of course there are many other possible useful globals. Think of:
- base_url
- base_path
- base_root
- is_https
- user
- language
and of course $_SERVER and $_GET.

Using these information you can access entity data as follows:

Specific case (1 entity, of known entity_type, referring to the image):
<?php
$entity_type = 'node';
$field_name = 'my_field';
$entity = $image_context['entity'];
$field = field_get_items($entity_type, $entity, $field_name);
?>

Or the more general case (not knowing the referring type, or multiple entities
that may be referring to the image):
<?php
$referring_entities = $image_context['referring_entities'];
foreach ($referring_entities as $field_name => $field_referring_entities) {
  foreach ($field_referring_entities as $entity_type => $entities) {
    foreach ($entities as $entity_id => $entity) {
      $field = field_get_items($entity_type, $entity, $field_name);
    }
  }
}
?>
README for the Image styleds admin Drupal module
------------------------------------------------

Project page: https://drupal.org/project/imagecache_actions

Current and past maintainers for Image styles admin:
- fietserwin (https://drupal.org/user/750928)


Release notes for 7.x-1.x-dev
-----------------------------
- Clear the (menu) cache after installing or updating.


Introduction
------------
The Image style admin module extends the administrative interface for image
styles by providing additional features.

Currently a duplicate, import and export image style feature are implemented.
More features may be added in the future. These features typically allow you to
more easily handle image styles. It allows us to more easily set up
a test/showcase sute of styles. Finally, it allows everybody to test D8 image
module features in real life.

This module is not a replacement for the features module
(https://drupal.org/project/features). If you are serious about configuration
management and want to distribute styles to other systems, use features.

Use this module for 1 time export/imports between different sites, "copy &
paste" reuse within a site, and when reporting issues to the imagecache_actions
issue queue.


TODO
----
Solving errors in the core image handling?
- [#1554074]: scale does not work with imagemagick when dimensions are unknown?
This module provides an overview of all the imagecache presets in use on this 
site, as well as a number of samples used to test if everything is working as 
expected.

Sample images are provided to illustrate a number of the sample presets.
Each image shown should match the one next to it. 
Where they don't match illustrates a current weakness in the system or the code 
coverage.

README
------
README for the Image effect text module.

Author Erwin Derksen (fietserwin: https://drupal.org/user/750928)


Dependencies
------------
Hard dependencies:
- Imagecache actions.
- Image (Drupal core).

Soft dependencies/recommended modules:
- Imagemagick (preferred toolkit, https://drupal.org/project/imagemagick).
- PHP filter (Drupal core, if yuo want to use PHP to create the text to render).
- System stream wrapper (https://drupal.org/project/system_stream_wrapper)
- Remote stream wrapper (https://drupal.org/project/remote_stream_wrapper)
The latter 2 provide additional stream wrappers. Especially the system stream
wrapper is very handy as it provides, among others, a module:// and theme://
wrapper.


Toolkit
-------
Personally, I prefer the imagemagick toolkit:
- It is better in anti-aliasing, try to rotate an image using both toolkits and
  you will see what I mean.
- It does not execute in the PHP memory space, so is not restricted by the
  memory_limit PHP setting.
- The GD toolkit will, at least on my Windows configuration, keep the font file
  open after a text operation, so you cannot delete, move or rename it anymore.
- This module does a better job with Imagemagick (see below).


Installing
----------
As usual. After enabling the module you can add texts to images. This image
effect works with both the GD and imagemagick toolkit, though results differ
depending on the toolkit you use.


More information about the effect data options
----------------------------------------------

Font
----
This module comes with some free fonts so you can easily test this effect.
Please read their respective licences.

For real use, you normally want to use your own font as dictated by the website
design. The font types supported depend on the toolkit in use, but at least ttf
files will always work. This option accepts either:
- 1 of the (enabled) scheme's:
  * public://
  * private:// Preferred for site specific masks, overlays, etc, that do not
    need to be shared publicly.
  * temporary:// Unlikely to be useful, but supported anyway as all schemes are
    supported.
  * module:// Introduced by the system stream wrapper module and preferred for
    module provided resources.
  * theme:// idem.
  * profile:// idem.
  * library:// idem.
- A relative path (relative to the current directory, probably Drupal root).
- An absolute path.
- A system or toolkit font specification. E.g. on my Windows system 'arial.ttf'
  worked with both GD and Imagemagick. A warning will be issued but that may be
  ignored when it works as expected.


Text position
-------------
The text position defines the point in the image where you want to place (align)
your text. It starts at the top left corner of the image with position 0,0 and
the positive directions are to the right and down.

The definition of the vertical position differs per toolkit. For GD it is the
position of the font baseline, while for Imagemagick it is the bottom of the
bounding box, i.e the descender or beard line in typography terminology.


Text alignment
--------------
You can align your text with regard to the text position. Possible horizontal
alignments are left (default), center and right. Vertical alignments are top,
center and bottom (default).

Note: Given
- the way that GD uses the vertical text position (as baseline),
- and the way this module implements (vertical) alignment (translating the
  (vertical) position using the calculated bounding box),
vertical alignment with the GD toolkit is a bit off. You will have to compensate
for this yourself.


Rotation
--------
The text can be rotated before being overlaid on the image. The value is in
degrees. Positive values are rotated clockwise, So 90 degrees is straight down.
negative values counter clockwise.

In Imagemagick the text is rotated around the text position. Thus centered text
is rotated around its own center. GD, on the other hand, always rotates around
the left bottom (baseline) position, regardless the text alignment. So using
rotation with a non default alignment (left bottom) will give surprising
results.


Text source
-----------
The text to place on the image may come from different sources:
- Text (with token replacement): the text to place on the image has to be
  entered on the image effect form. Use this e.g. for a copyright notice.
  notes:
  * Token replacement: you can use all global tokens, the file tokens, and
    tokens from entities referring to the image via an image field. Example: if
    you know that the image style is only used for article nodes, you can use
    [node:field-image:alt] to get the alt text of the image. Note: this specific
    example requires the entity_token module.
  * New lines: you can add a new line by adding \n to your text. To get a
    literal \n, use \\n.
- PHP: the text to place on the image comes from a piece of PHP code that should
  return the text to place on the image. Only users with the 'use PHP for
  settings' permission are allowed to use this source. This permission and the
  evaluation of the PHP code come from the PHP filter module which is part of
  Drupal core and thus needs to be enabled, also during image generation.
  To add new lines to your text add them literally to the string you return,
  normally by using "\n" in your PHP code.
- Image Alt or Title: to alleviate the need to enable the PHP filter module, 2
  commonly used sources for dynamic texts are directly available without any
  coding: the alt and title properties of an image field linked to the image at
  hand.

Notes:
- When using token replacement or the image alt or title, multiple image fields,
  possibly in different languages, may be referring to the image that is being
  processed. This module will take the first image field it finds to extract the
  alt and title. If the field in itself is multi-lingual, thus not a synced
  field, the current language will be taken, which is the language of the user
  that happens to request this image derivative first.
- This module will not automatically break text based on available space.
- Due to the way that GD text box positioning works it is quite difficult to
  correctly position multiple lines of text with GD. If you have a working
  solution please post a patch. (Probably involves exploding the text in
  separate lines and then positioning each line separately.)


PHP snippets to determine the text
----------------------------------
Given the correct permission, you can write your own PHP snippet to compute the
text to display. To ease this task, this module makes some information regarding
the image being processed available in 2 variables: $image and $image_context.
These variables are readily available in your snippet.

$image is an object containing the following properties:
- source: string, the source of the image, e.g. public://photo.jpg
- info: array, example data:
   - width (int) 180
   - height  (int) 180
   - extension (string) png
   - mime_type (string) image/png
   - file_size (int) 4417
- toolkit: string, imagemagick or GD

$image_context is an associative array containing:
- effect_data: array, the data of this image effect, example data for the text
  effect:
   - size  (string) 12
   - xpos  (string) center
   - ypos  (string) center
   - halign  (string) left
   - valign  (string) bottom
   - RGB Array [1]
      - HEX (string) 000000
      - alpha (string) 100
   - angle (string) 0
   - fontfile  (string:46) module://image_effects_text/Komika_display.ttf
   - text_source   (string) text
   - text  (string) Hello World!
   - php  (string) return 'Hello World!'
- managed_file: object|null. A managed file object containing these properties:
   - fid (string) 2
   - uid (string) 1
   - filename  (string) photo.jpg
   - uri (string) public://photo.jpg
   - filemime  (string) image/jpeg
   - filesize  (string) 445751
   - status  (string) 1
   - timestamp (string) 1327525851
   - metatags  Array [0]
   - rdf_mapping Array [0]
- referring_entities: array|null. A nested array with (fully loaded) entities
  referring to the current image. The 1st level of entries is keyed by the field
  name, the 2nd by entity type, and the 3rd by entity id. Example data:
   - field_photo Array [1]
      - node  Array [1]
         - 12  Object of: stdClass
            - nid (string) 12
            - vid (string) 12
            - type  (string) page
            - author ...
            - timestamp ...
            - ...
- entity: object|null, the 1st entity in referring_entities. This is for easy
  access to the referring entity if it may be assumed that only 1 entity is
  referring to the current image.
- image_field: array|null, the 1st image field in entity that is referring to
  the current image. This is for easy access to the image field data if it may
  be assumed that only 1 image field is referring to the current image. Example
  data:
   - fid (int) 2
   - alt (string) ...
   - title (string) ...
   - ...

Of course there are many other possible useful globals. Think of:
- base_url
- base_path
- base_root
- is_https
- user
- language
and of course $_SERVER and $_GET.

Using these information you can access entity data as follows:

Specific case (1 entity, of known entity_type, referring to the image):
<?php
if (!$image_context['entity']) {
  return 'No referring entity';
}
$entity_type = 'node';
$field_name = 'my_field';
$entity = $image_context['entity'];
$field = field_get_items($entity_type, $entity, $field_name);
if ($field) {
  return isset($field[0]['value']) ? $field[0]['value'] : 'No field value';
}
?>

Or the more general case (not knowing the referring type, or multiple entities
that may be referring to the image):
<?php
if (!$image_context['referring_entities']) {
  return 'No referring entities';
}
$referring_entities = $image_context['referring_entities'];
foreach ($referring_entities as $field_name => $field_referring_entities) {
  foreach ($field_referring_entities as $entity_type => $entities) {
    foreach ($entities as $entity_id => $entity) {
      $field = field_get_items($entity_type, $entity, $field_name);
      // ...
    }
  }
}
?>

TODO
----
- Vertical alignment: add baseline as vertical alignment and make both toolkits
  behave the same for any given vertical alignment.
- Rotation and alignment. Imagemagick seems to be more correct. Can GD made to
  do the same?
- Language and alt/title: what if the first user to pass by and that generates
  the image is in a language that has no alt/title?
- Check for existence of imagettftext() and fail properly.

To quote http://www.imagemagick.org/Usage/text/#draw:
As of IM version 6.2.4, the "-draw text" operation no longer understands the use
of '\n' as meaning newline, or the use of percent '%' image information escapes.
(See Drawing a Percent Bug). These abilities, and problems, however remain
available in the new IM v6 operator "-annotate". See the Annotate Text Drawing
Operator below.
README
------
README for the Image effect text test module.

This module contains several image styles to test text effects. It uses an image
containing a grid and a font which are included in the install package as well.
The image styles defined by this module start with 'text-test-'.

Hard Dependencies
-----------------
Hard dependencies:
- Imagecache actions (canvas_actions and image_effects_text).
- Image (Drupal core).
- System stream wrapper (https://drupal.org/project/system_stream_wrapper)

Soft Dependencies
-----------------
- Imagemagick (preferred toolkit, https://drupal.org/project/imagemagick).
- GD
Bean (Bean Entities Aren't Nodes)
==================================

The bean module was created to have the flexibility of
Block Nodes without adding to the node space.

Bean Types
----------

A Bean Type (or Block Type) is a bundle of beans (blocks).
Each Bean type is defined by a ctools plugin and are fieldable.
Currently Bean Types are only defined in hook_bean_plugins().

If you enable bean_admin_ui you can add/edit bean types at
admin/structure/block-types

Beans
-----
An overview of all beans created is at: admin/content/blocks

If views is installed and enabled, a default called 'Bean Block List' is available to replace the default block list at: admin/content/blocks

Beans can be added at: block/add

Example Bean Type Plugins
-------------------------
indytechcook's original bean plugin gist: https://gist.github.com/1460818
Context Bean: Context Bean block types display other beans (block entities). http://drupal.org/project/context_bean
Examples: http://drupal.org/project/bean_examples
Flickr Integration: http://drupal.org/project/bean_flickr
Leafbean - Leaflet + Bean for a simple map block: http://drupal.org/sandbox/rerooting/1787416
Leaflet GeoJSON Bean: http://drupal.org/project/leaflet_geojson
Openlayers Blocks: http://drupal.org/project/openlayers_blocks
Bean Panels - provides loose bean placement in panels, content need not exist: http://drupal.org/project/bean_panels
Relevant Content: http://drupal.org/project/bean_relevant
Service Links: http://drupal.org/project/bean_service_links (Integration with the Service Links module)
Slideshow: http://drupal.org/project/beanslide
Slideshow: https://github.com/opensourcery/os_slideshow
Taxonomy plugins: http://drupal.org/project/bean_tax
Twitter Pull integration: http://drupal.org/project/bean_twitter_pull (Integration with the Twitter Pull module)
Flickr Integration: http://drupal.org/project/bean_flickr
MapBox.js Integration: http://drupal.org/project/mapboxjs
(Latest list of plugins: http://drupal.org/node/1475632)

Articles and Videos
-------------------
Bean Tutorial: http://treehouseagency.com/blog/neil-hastings/2011/09/21/building-custom-block-entities-beans
Bean Presentation: http://www.archive.org/details/DrupalBeanModuleTutorial-UsingBeanAdminUiAndWritingBeanPlugins-
Admin UI tutorial: http://youtu.be/Eu1YNy-BNG8
Easily convert Boxes to Beans: https://github.com/skwashd/bean_boxes
Views without Views: http://thinkshout.com/blog/2012/06/sean/introducing-relevant-content-bean
Bean Intro: http://previousnext.com.au/blog/introduction-bean-module
Extending An Already Defined Bean: http://drupal.org/node/1826204
Empty Front Page
----------------

This is an ultra lightweight module that remove default content from 
the frontpage.


Installation
------------
Place empty_front_page in the modules directory for your site and enable it.

Make sure your 'Default front page' setting is empty. 
See admin/config/system/site-information.
Description
-----------
This module makes it possible to edit fields in-place.


Installation
------------
1. Install like any other Drupal module.
2. Grant the 'Access in-place editing' permission to relevant roles.
3. A new "In-place edit operations" block displaying the "Quick edit" link is
   now available and placed in the first sidebar by default.


In-place WYSIWYG editing using CKEditor
---------------------------------------
1. Download and install the latest stable release (version 1.13 or newer) of the
   CKEditor module from http://drupal.org/project/ckeditor.
   Note that *only* the CKEditor module is supported, not any other module, like
   the "Wysiwyg" module (http://drupal.org/project/wysiwyg).
2. Go to http://ckeditor.com/download and download the Standard or Full package.
3. Extract the dowwnloaded package to sites/all/libraries/ckeditor. For maximum
   security, it is recommended to delete the included "samples" directory at
   sites/all/libraries/ckeditor/samples.
4. Go to admin/config/content/ckeditor/, enable one of the CKEditor profiles for
   each text format where you want to use CKEditor. Or create a new CKEditor
   profile.
   e.g. Enable the default "Advanced" profile for Drupal's "Filtered HTML" text
   format.
5. Find a node that uses e.g. the "Filtered HTML" text format for its body,
   click the "Quick edit" link, then click the node's body, and you should see
   CKEditor's in-place editing!

FAQ
---
Q: I want to make the "Quick edit" link look different.
A: No problem! Disable the block, and output edit_trigger_link()'s render array
   somewhere else on the page.
Q: Edit breaks my node titles!
A: This probably means you're using a theme that inappropriately uses the node
   title as a "title" attribute as well, without stripping any HTML used in the
   title. Within an attribute, HTML is pointless and potentially harmful.
   So if your theme's node.tpl.php does something like this:
     title="<?php print $title ?>"
   then please replace it with this:
     title="<?php print filter_xss($title, array()) ?>"
   This ensures that any HTML tags are stripped from the title.
   See http://drupal.org/node/1913964#comment-7231462 for details.
Q: Why does Edit add attributes to my HTML even for users that don't have the
   permission to use in-place editing?
A: First: precisely because these are just small bits of metadata, there is no
   harm; there is no security risk involved.
   Second: it is by design, this metadata is always added, to not break Drupal's
   render cache.
Q: Why do I get a 'The filter "<filter name>" has no type specified!'' error?
A: For Edit module to allow for in-place editing of "processed text" fields
   (i.e. text passed through Drupal's filter system, via check_markup()), it
   needs to know about each filter what type of filter it is. For simpler text
   formats (i.e. with simpler filters), the unfiltered original may not have to
   be retrieved from the server. See http://drupal.org/node/1817474 for details.
/**
 * @file
 * README file for Workbench Email.
 */

Workbench Email

CONTENTS
--------

1.  Introduction
2.  Installation
2.1  Requirements
3.  Configuration
4.  Using the module
5.  Troubleshooting
6.  Developer notes
6.1  Database schema
7.  Feature roadmap

----
1.  Introduction

Workbench Email

----
1.1  Concepts

Extends Workbench Moderation by adding the ability to add emails to specific
transitions. Based on those email transitions, the admin can configure
each email's subject / message. Then when the content moves through the
specific transition, if an email transition is already set, the current
content editor has the ability to send email to those specific role based
user(s).

----
2.  Installation

Install the module and enable it according to Drupal standards.

The module's configuration pages reside at:
- admin/config/workbench/moderation/email-transitions
- admin/config/workbench/moderation/emails

The module depends on workbench moderation and will display help messages if
that module has not been setup correctly.

----
2.1  Requirements

Workbench Email requires:
- Workbench Moderation (and dependencies)
- Token

----
3.  Configuration

Workbench Moderation's configuration section is located at:

- Admin > Configuration > Workbench > Workbench Moderation -> Email Transitions

This section allows the admin to configure email transitions based on
transition states and user roles.

- Admin > Configuration > Workbench > Workbench Moderation -> Emails

Depending on what email transtions have been set, the admin can configure each
transitions subject / message.


----
3.3  Checking permissions

In order to use moderate the emails and email transitions, the user must be
given the appropriate role. Navigate to admin/people/permissions and
select Administer Workbench Moderation Emails under Workbench Email for the
appropriate role.

----
4.  Using the module

Once the module is installed and moderation is enabled for one or more node
types, users with permission may:

* Select the appropriate users that you wish to send an email to when moderated
content is moving through configured email transition.

----
5.  Troubleshooting

* If users do not see the node form select list that allows them to select the
user(s) they wish to send an email to, check the email transitions and emails
administration pages. If no email transition is defined, no form option will
display. If no email subject / message is defined, the system will display the
following message:
- No email template is set, so no email was sent. Contact your system admin
to resolve this issue.
* If no email templates are available within the administration area
(admin/config/workbench/moderation/emails), then check that you have email
transitions set (admin/config/workbench/moderation/email-transitions).
* If no email transitions are available (transitions show up but no roles
can be selected), then no roles have been associated to the moderation of
content. Check Workbench Moderation readme.txt to figure out the correct
permissions for this.

----
6.  Developer notes

This is my first drupal contributed module, so I know there is room for
improvements. Emails being sent when content moves through a transition is
something that clients always seem to request but no system has existed that
is easy to configure and can be exported (featured). I know rules, actions,
triggers etc exist but they are cumbersome to configure and export (IMO).
So, I'm curious to see what other people think about this, feel free to
comment :)

----
6.1  Database schema

Workbench Email uses two tables to store emails and email transitions.

* workbench_email_transitions
  Stores administrator-configured email transitions.

* workbench_emails
  Stores administrator-configured subject / message for each email transition

----
7.  Feature roadmap
Views Datasource README
-------------------------------------------------------------------------------

About
-----
Views Datasource is a set of plugins for Views for rendering node content in a
set of shareable, reusable data formats based on XML, JSON, and XHTML. These
formats allow content in a Drupal site to be easily used as data sources for
Semantic Web clients and web mash-ups. Views Datasource plugins output content
from node lists created in Drupal Views as:
  1)XML data documents using schemas like OPML and Atom;
  2)RDF/XML data documents using vocabularies like FOAF, SIOC and DOAP;
  3)JSON data documents in plain JSON or in a format like MIT Simile/Exhibit;
  4)XHTML data documents using microformat like hCard and hCalendar

The project consists of 4 Views style plugins:
  1)views_xml - Output as raw XML, OPML, and Atom;
  2)views_json - Output as simple JSON, Simile/Exhibit JSON and JqGrid;
  3)views_rdf - Output as FOAF, SIOC and DOAP;
  4)views_xhtml - Output as hCard and hCalendar.

In Drupal 7.x, to use these plugins you should:
1) Enable the module containing the format you want to render your views as.
2) In the Views UI set the view style (in Basic Settings) to one of:
   i)  JSON data document (render as Simple JSON or Simile/Exhibit JSON)
   ii) XML data document (render as raw XML, OPML, or Atom)
   iii) RDF data document (render as a FOAF or SIOC or DOAP RDF/XML document)
   iv) XHTML data document (render as hCard or hCalendar XHTML)
3) In the view style options choose the options or vocabulary for your format
   (like raw or the OPML or Atom vocabulary for XML rendering.)
4) Add the fields to your view that contain the information you want to be
   pulled into the format renderer. All formats will output the fields
   recognized as belonging to that format, and certain formats like Atom and
   SIOC require certain fields to be present (see below.)
   The SIOC format requires the fields: node nid, type, title, body, posted date
5) That's it! The rendered view will be visible in the preview and at your
   view's page displaypath. When you create a page display for your view with a unique URL,
   no Drupal markup is emitted from this page, just the data for the particular
   content type with the proper Content-Type HTTP header (like text/xml or
   application/rdf+xml.)

A JSON data document will render the nodes generated by a view as a
serialization of an array of Javascript objects with each object's properties
corresponding to a view field. Simple JSON is just plain-vanilla JSON
serialization usable in most apps while Simile/Exhibit JSON is the serialization
format used by the Exhibit web app - http://simile.mit.edu/exhibit/

An XML data document with render the nodes generated by a view as XML. The raw
XML format creates a root element called 'nodes' and then a 'node' child element
for each node in the view, with each node's child elements corresponding to a
view field. OPML is a very simple XML schema useful for generating simple lists
(like lists of tracks in an music playlist.) Atom is a syndication schema with
similar intents as RSS. The following fields will bviews_rdf will render
the nodes generated by a view as an RDF/XML FOAF document with each
<foaf:Person> element corresponding to a node in the view. To use just have
fields in the view named as their equivalent FOAF properties - for example to
have a <foaf:name> or <foaf:nick> element, have a field named 'name' and 'nick'
in your view. Similarly views_xhtml provides the hCard plugin which will render
each node in the XHTML hCard format - just have fields corresponding to hCard
properties defined in the view. For example to create an <email> element inside
the <div class="hcard"> root element, just have one or more fields in the view
containing the text 'email'.

The FOAF and hCard renderers are most useful with view based on user profiles
where you can create profile fields corresponding to properties defined in the
FOAF (http://xmlns.com/foaf/spec/) or hCard
(http://microformats.org/wiki/hcard-cheatsheet) spec. However any node type
(like those created with nodeprofile or Bio or Advanced Profile or Content
Profile) can be used in the view. It doesn't matter what data table the view
is based on, only what fields are present in the view.

OPTIONS
------
Each style has a range of options you can use to customize the output:

 The following options are common to all plugins:
  1. Field output: Normal or Raw
      This determines if each object in the view is displayed as normally
      rendered by Drupal, or as the raw result object. Raw is useful if
      you don't want any Drupal formatting applied to the view result, for
      example, if you have a field with a date and you just want the timestamp
      value from the database. Note that both a field's label and content are
      rendered as raw so XML element or attribute labels will have the internal
      field name - for example instead of 'Body' a raw field will have the
      label 'node_revisions_body'.
  2. Plaintext output
      Selecting this neans that all HTML markup will be stripped from the
      view result. This is useful, for example, if you are generating an
      XML document from nodes and you just want the plain text content
      of a node without markup tags mixing with the other XML elements.
     (Note that you can also escape XML content using CDATA sections,
     see below.)
  3. Content-Type
      This determine the Content-Type header sent in a page display of
      a view. This header is necessary for most clients consuming data
      from the view. You can use the default Content-Type for the
      particular plugin or choose from alternate types.
  4. Use Views API mode - by default the plugins stop Drupal from
      doing any additional processing when a view is rendered - allowing
      the content to be output without any additional Drupal markup.
      However if you are calling a view programatically then this will
      hlar your code prematurely. The solution (contributed by icylake)
      is to use the Use Views API mode option if you are going to call
      the view from code. This option causes the plugin to not terminate
      Drupal execution.

 The following options are common to the views_xml, and views_xhtml plugins:
  1. Escape row content as CDATA
      This option escapes all content from the result row using the ![CDATA[
      XML directive. This is useful if you want all content markup preserved,
      but kept separate from the other XML tags in the document. You will
      have to instruct your client that the data you are processing is
      in CDATA blocks, and different XML processors may handle these blocks
      differently.
  2. XML document header
      This option lets you specify the XML document header which precedes the
      root XML element. If you specify a header here it will override any
      header generated automatically by the plugin.

 The views_json plugin has the following options:
  1. Root object name
      This specifies the name of the top-level object in the JSON object. The
      default is the name of the view base table (nodes, users, etc.)
  2. JSON data format
      This specifies the format of the JSON output - either simple, plain-
      vanilla JSON, or the JSON format compatible with the Simile/Exhibit
      application.

 The views_xml plugin has the following options:
  1. XML schema:
      This specifies the XML schema the view will render.
      Raw simply renders each view field using the field name as
      a element/attribute label and the field content as the element/attribute
      value.

      OPML renders each field as an attribute-value pair in an <outline>
      element. The OPML schema requires at least one field labelled 'text' - or
      if this is not found it falls back to 'body' or 'node_revisions_body'.
      The following fields are recommended (fallback in brackets):
      type (node_type), created(published, node_created, Post date).

      Atom renderes a view using the Atom syndication schema. You can use this
      format to create an Atom syndication of the content in your view. Atom
      requires the following fields to be present (fields in bracket indicate
      what the plugin will fall back to if it can find the explicitly named
      Atom field):
      id (nid), title(node_title) updated(last_updated, Updated date, changed,
      Last updated/commented, Last comment time)
      The following fields are recommended: content(Body, node_body,
      node_revisions_body), link (nid {a link will be constructed from the
      Drupal path and the nid), summary author(uid).

  2. Root element name:
      Only applies to the Raw XML schema. This specifies the root XML element
      in the document. All other elements will be children of this element.
      The default is the name of the view base table.

  3. Element output:
      Only applies to the Raw XML schema. This specifies whether the view
      fields will be output as nested child elements or attributes. For example
      if Element output is set to Nested then a field labelled 'title' with
      content 'foo' will be output as <title>foo</title> If Element output
      is set to Attributes then this field will be output as title = "foo"
      for each row element. Note that the plugin automatically strips invalid
      XML element and attribute label characters (like spaces), so a field like
      'Post date' will become 'postdate'.

  4. View author:
      This is used by the Atom and OPML plugins to provide the author
      of the Atom or OPML document. It can be a valid Drupal user name,
      a Drupal user uid, or any name otherwise.

 The views_rdf plugin has the following options:
  1. RDF vocabulary:
     This indicates what RDF vocabulary to use in the document: either
     FOAF or SIOC or DOAP . FOAF (Friend of a Friend) is useful for sharing a
     list of  users or people, while SIOC
     (Semantically-Interlinked Online Communities Project) is most useful for
     describing a set of pages, stories, blogs,
     or forum posts with comments from different people. SIOC itself uses
     FOAF to describe the posts and comments from different people. DOAP
     (Description of a Project) is useful for - as the name suggests - projects.
     See these links for more info:
      http://www.foaf-project.org/
      http://sioc-project.org/
      http://trac.usefulinc.com/doap

     The following fields are recognized when using the FOAF vocabulary
     (fallbacks in brackets):
     name, firstname, surname, title, nick, mbox (mail, email), mbox_sha1sum,
     openid, workplacehomepage, homepage, weblog, img, depiction, member,
     phone, jabberID, msnChatID, aimChatID, yahooChatID.

     The following fields are required when using the SIOC vocabulary:
     id (nid), created(node_created, Post date, title, type (node_type),
     changed (node_changed, updated/commented date) last_updated(updated date),
     body(node_body, node_revisions_body), uid (users_uid).

     The following fields are recognized when using the DOAP vocabulary:
     (optional fields in square brackets)
     nid, name, homepage, [license], [shortdesc], [language], [repositories],
     [developers]

 The views_xhtml plugin has the following options:
  1. Microformat
     This specifies the microformat to be rendered: hCard is most useful for a
     list of users or people. hCalendar can be used to describe a list of
     events.
     The following fields are recognized by hCard:
     Address Type, Post office box, Street Address, Extended Address, region,
     Locality. Postal Code, Country name, agent, bday, class, category, email,
     honorific prefix, Given name, Additional name, Family name, Honoric suffix,
     Nickname, Organization name, Organization unit, photo, tel.

     The following fields are recognized by hCalendar:
     class, category, description, summary, dtstart(Event start, event_start)
     dtend(Event end, event_end).


TODO
----
 Proper date handling for each format
 Check for separator in profile fields
 Properly handle grouped multiple values in views_xhtml et. al
 Strict conformance with Atom spec
 Recognize when field rewriting rules are used
 Represent multiple-valued fields using nested child elements
Term Merge
------------------------
by:
 * Max Nylin <max@articstudios.se>
 * Oleksandr Trotsenko

Description
-----------
When using taxonomy for free tagging purposes, it's easy to end up with
several terms having the same meaning. This may be due to spelling errors,
or different users simply making up synonymous terms as they go.

You, as an administrator, may then want to correct such errors or unify
synonymous terms, thereby pruning the taxonomy to a more manageable set.
This module allows you to merge multiple terms into one, while updating
all fields referring to those terms to refer to the replacement term instead.

Currently, the module only acts on:
 * fields of 'taxonomy term reference' type
 * Views Taxonomy Term filter handlers
 * Redirects

It would be desirable to update other possible
places where deleted terms are used.

Integration
-------------
Currently module integrates with the following core and contributed modules:
 * Redirect module (http://drupal.org/project/redirect). During term merging
 you may set up SEO friendly redirects from the branch terms to point to the
 trunk term
 * Synonyms module (http://drupal.org/project/synonyms). During term merging
 you will be able to choose a trunk term's field into which all the branch terms
 will be added as synonyms (until cardinality limit for that field is reached).
 * Hierarchical Select (http://drupal.org/project/hierarchical_select). If
 Hierarchical Select module is configured to be used for working with Taxonomy,
 its widget will be shown on the form, where you choose what terms to merge into
 what term.
 * Views (http://drupal.org/project/views). If the branch terms are to be
 deleted after the merging process, you could end up having some Views filters
 to filter on no longer existing terms. Term Merge module, while merging terms,
 will update those filters to filter not on the branch term, but on the trunk
 term. This way you will not have senseless filters and will not have to update
 them manually.

Requirements
-------------
The modules requires enabled the following modules:
 * Taxonomy module (ships with Drupal core)
 * Entity API (http://drupal.org/project/entity)

Installation
------------
 * Copy the module's directory to your modules directory and activate the
 module.
=====
Block Class
http://drupal.org/project/block_class
-----
Block Class was developed and is maintained by Four Kitchens
<http://fourkitchens.com>.


=====
Installation
-----

1. Enable the module
2. To add a class to a block, simply visit that block's configuration page at
Administration > Structure > Blocks
-- SUMMARY --

The JW Player module adds a new field for displaying video files in a JW Player.

For a full description visit the project page:
  http://drupal.org/project/jw_player
Bug reports, feature suggestions and latest developments:
  http://drupal.org/project/issues/jw_player


-- REQUIREMENTS --

* This module depends on the File module, which is part of Drupal core, Chaos
  Tools (http://drupal.org/project/ctools) and the Libraries module
  (http://drupal.org/project/libraries).


-- INSTALLATION --

* Download either the latest commercial or the latest non-commercial JW
  Player at http://www.longtailvideo.com/players/jw-flv-player/.

* Extract the zip file and put the contents of the extracted folder in
  libraries/jwplayer. 
  E.g.: sites/all/libraries/jwplayer or sites/<sitename>/libraries/jwplayer
	
* Install this module as described at http://drupal.org/node/895232.

* Go to Administration > Reports > Status reports (admin/reports/status) to
  check your configuration.


-- BASIC USAGE --

In that majority of cases JW Player is used as a field formatter on a file
field. Before enabling JW Player on a field visit /admin/config/media/jw_player
to configure one or more presets. A preset is a group of JW Player settings,
such as dimentions and skin, that can be re-used multiple times.

Once a preset has been defined visit /admin/structure/types and select "manage
display" for the content type you'd like to configure and select "JW player" as
the formatter on the relevant file field. At this point you will also need to
click on the cog beside the field to select the preset you'd like to apply to
the file. That's it - vidoes uploaded to this field should now be displayed
using JW Player!
-- SUMMARY --

Wysiwyg API allows users of your site to use WYSIWYG/rich-text, and other
client-side editors for editing contents. This module depends on third-party
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
    disable "Limit allowed HTML tags", "Convert line breaks...", and
    (optionally) "Convert URLs into links".
    Note that disabling "Limit allowed HTML tags" will allow users to post
    anything, including potentially malicious content. For a more configurable
    alternative to "Limit allowed HTML tags" try
    http://drupal.org/project/wysiwyg_filter.

  - or add a new text format, assign it to trusted roles, and ensure that above
    mentioned input filters are configured as detailed.

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


This is the new module home for a unified redirection API (also replaces
path_redirect and globalredirect).

Entity API module
-----------------
by Wolfgang Ziegler, nuppla@zites.net

This module extends the entity API of Drupal core in order to provide a unified
way to deal with entities and their properties. Additionally, it provides an
entity CRUD controller, which helps simplifying the creation of new entity types.


This is an API module. You only need to enable it if a module depends on it or
you are interested in using it for development.

Advanced usage:
---------------
You can optimize cache clearing performance by setting the variable
'entity_rebuild_on_flush' to FALSE. This skips rebuilding of feature
components and exported entities during cache flushing. Instead, it is triggered
by the features module only; e.g., when features are reverted.


The README below is for interested developers. If you are not interested in
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
README for Disqus for Drupal 7

Disqus 7.x-1.x
=================================

Disqus Official PHP API Support
=================================

INSTALL
=============
You will need to install the Libraries API module (7.x-2.x branch).

https://drupal.org/project/libraries

The Disqus Official PHP API can be downloaded at:

https://github.com/disqus/disqus-php

Copy the contents of the disqusapi folder to sites/all/libraries/disqusapi.
You will need to obtain your user access key from the application specific
page found here:

http://disqus.com/api/applications/

BUILT-IN FEATURES
=============
This module can automatically update and/or delete your Disqus threads when you
delete/update your nodes. 

Visit Disqus configuration page after you installed Disqus API to configure it's
behaviour. 

EXAMPLES
=============
You can find the API reference here:

http://disqus.com/api/docs/

Any of these methods can be called by creating an instance of the Disqus API
through disqus_api(). You must use try/catch to avoid php throwing a general
exception and stopping script execution.

For a full explanation of the official API you can view the readme located here:

https://github.com/disqus/disqus-php/blob/master/README.rst

Example: Calling threads/details and threads/update

  $disqus = disqus_api();
  if ($disqus) {
    try {
      // Load the thread data from disqus. Passing thread is required to allow the thread:ident call to work correctly. There is a pull request to fix this issue.
      $thread = $disqus->threads->details(array('forum' => $node->disqus['domain'], 'thread:ident' => $node->disqus['identifier'], 'thread' => '1', 'version' => '3.0'));
    }
    catch (Exception $exception) {
      drupal_set_message(t('There was an error loading the thread details from Disqus.'), 'error');
      watchdog('disqus', 'Error loading thread details for node @nid. Check your API keys.', array('@nid' => $node->nid), WATCHDOG_ERROR, 'admin/config/services/disqus');
    }
    if (isset($thread->id)) {
      try {
        $disqus->threads->update(array('access_token' => variable_get('disqus_useraccesstoken', ''), 'thread' => $thread->id, 'forum' => $node->disqus['domain'], 'title' => $node->disqus['title'], 'url' => $node->disqus['url'], 'version' => '3.0'));
      }
      catch (Exception $exception) {
        drupal_set_message(t('There was an error updating the thread details on Disqus.'), 'error');
        watchdog('disqus', 'Error updating thread details for node @nid. Check your user access token.', array('@nid' => $node->nid), WATCHDOG_ERROR, 'admin/config/services/disqus');
      }
    }
  }

# About this module

This module provides a file field which accepts csv file uploads and visualizes their
contents using Recline.js

## INSTALLATION


+ Download the Reline.js library from https://github.com/okfn/recline 
(zip file) and install in 'sites/all/libraries/'.
+ Enable recline module.

## Supported Backends and File Types

This creates grid, graph, and map data previews for CSV and XLS files based off of the following mechanisms.

It first checks to see if the DKAN Datastore module is installed, and if a datastore has been created for the file. If the datastore is available it uses that to visualize the data. This is extremely scalable since it only queries the first 50 rows of the table in the database. It has been tested with files up to 500 GB and a million+ rows.

If the datastore is not available it checks if the file is a CSV. If it is a CSV it tries to load the file into memory. If it takes longer than a second to load the file it instructs the user that the file is too large to preview. This keeps the page from freezing for larger files.

If the file is a XLS it uses the DataProxy services to preview the file since there is currently not a CSV backend for Recline. DataProxy parses the file and returns it as a data object which is previewed.

## Contributing

We are accepting issues in the dkan issue thread only -> https://github.com/NuCivic/dkan/issues -> Please label your issue as **"component: recline"** after submitting so we can identify problems and feature requests faster.

If you can, please cross reference commits in this repo to the corresponding issue in the dkan issue thread. You can do that easily adding this text:

```
NuCivic/dkan#issue_id
``` 

to any commit message or comment replacing **issue_id** with the corresponding issue id.
/**
 * @file
 * README file for Workbench Moderation.
 */

Workbench Moderation
Arbitrary moderation states and unpublished drafts for nodes

CONTENTS
--------

1.  Introduction
1.1  Concepts
1.1.1  Arbitrary publishing states
1.1.2  Node revision behavior
1.1.3  Moderation states and revisions
2.  Installation
2.1  Requirements
3.  Configuration
3.1  Configuring states
3.2  Configuring transitions
3.3  Checking permissions
3.3.1  Recommended permissions
4.  Using the module
5.  Troubleshooting
6.  Developer notes
6.1  Database schema
6.2  Views integration
7.  Feature roadmap

----
1.  Introduction

Workbench Moderation 

----
1.1  Concepts

Workbench Moderation adds arbitrary moderation states to Drupal core's
"unpublished" and "published" node states, and affects the behavior of node
revisions when nodes are published. Moderation states are tracked per-revision;
rather than moderating nodes, Workbench Moderation moderates revisions.

----
1.1.1  Arbitrary publishing states

In Drupal, nodes may be either unpublished or published. In typical
configurations, unpublished nodes are accessible only to the user who created
the node and to users with administrative privileges; published nodes are
visible to any visitor. For simple workflows, this allows authors and editors to
maintain drafts of content. However, when content needs to be seen by multiple
people before it is published--for example, when a site has an editorial or
moderation workflow--there are limited ways to keep track of nodes' status.
Workbench Moderation provides moderation states, so that unpublished content may
be reviewed and approved before it gets published.

----
1.1.2  Node revision behavior

Workbench Moderation affects the behavior of Drupal’s node revisions. When
revisions are enabled for a particular node type, editing a node creates a new
revision. This lets users see how a node has changed over time and revert
unwanted or accidental edits. Workbench Moderation maintains this revision
behavior: any time a node is edited, a new version is created.

When there are multiple versions of a node--it has been edited multiple times,
and each round of editing has been saved in a revision--there is one "current"
revision. The current revision will always be the revision displayed in the node
editing form when a user goes to edit a piece of content.

In Drupal core, publishing a node makes the current revision visible to site
visitors (in a typical configuration). Once a node is published, its current
revision is always the published version. Workbench Moderation changes this; it
allows you to use an older revision of a node as the published version, while
continuing to edit a newer draft.

@see workbench_moderation-core_revisions.png
@see workbench_moderation-wm_revisions.png

Internally, Workbench Moderation does this by managing the version of the node
stored in the {node} table. Drupal core looks in this table for the "current
revision" of a node. Drupal core equates the "current revision" of a node with
both the editable revision and, if the node is published, the published
revision. Workbench Moderation separates these two concepts; it stores the
published revision of a node in the {node} table, but uses the latest revision
in the {node_revision} table when the node is edited. Workbench Moderation's
treatment of revisions is identical to that of Drupal core until a node is
published.

----
1.1.3  Moderation states and revisions

Workbench Moderation maintains moderation states for revisions, rather than for
nodes. Since each revision may reflect a unique version of a node, the state may
need to be revisited when a new revision is created. This also allows users to
track the moderation history of a particular revision, right up through the
point where it is published.

Revisions are a linear; revision history may not fork. This means that only the
latest revision--Workbench Moderation calls this the "current draft"--may be
edited or moderated.

----
2.  Installation

Install the module and enable it according to Drupal standards.

After installation, enable moderation on a content type by visiting its
configuration page:

    Admin > Structure > Content Types > [edit Article]

In the tab block at the bottom of the form, select the "Publishing options" tab.
In this tab under "Default Options", Workbench Moderation has added a checkbox,
"Enable moderation of revisions". To enable moderation on this node type, check
the boxes labeled "create new revision" (required) and "enable moderation of
revisions", and then save the node type.

----
2.1  Requirements

Workbench Moderation may be used independently of other modules in the Workbench
suite, including the "Workbench" module. Unlike the "Workbench" module,
Workbench Moderation does not depend on Views. However, Workbench Moderation
does have Views integration, and it provides two useful views ("My Drafts" and
"Needs Review") that appear in the Workbench. If you wish to use Workbench
Moderation without Workbench, you may override or clone these views and place
them where your users can find them.

Using the "Workbench" module with Workbench Moderation enables the display of
moderation status information and a mini moderation form on node viewing pages.

----
3.  Configuration

Workbench Moderation's configuration section is located at:

    Admin > Configuration > Workbench > Workbench Moderation

This administration section provides tabs to configure states, transitions, and
to check whether your permissions are configured to enable full use of
moderation features.

----
3.1  Configuring states

Workbench Moderation provides three default moderation states: "Draft", "Needs
Review", and "Published". The Draft and Published states are required. You can
edit, add, and remove states at:

    Admin > Configuration > Workbench > Workbench Moderation > States

----
3.2  Configuring transitions

Workbench Moderation also provides transitions between these three states. You
can add and remove transitions at:

    Admin > Configuration > Workbench > Workbench Moderation > Transitions

----
3.3  Checking permissions

In order to use moderation effectively, users need a complex set of permissions.
If non-administrative users encounter access denied (403) errors or fail to see
notifications about moderation states, the "Check permissions" tab can help you
determine what permissions are missing. Visit:

    Admin > Configuration > Workbench > Workbench Moderation > Check Permissions

Select a Drupal role, an intended moderation task, and the relevant node types,
and Workbench Moderation will give you a report of possible missing permissions.
Permissions configuration depends heavily on your configuration, so the report
may flag permissions as missing even when a particular role has enough access to
perform a particular moderation task.

----
3.3.1  Recommended permissions

For reference, these are the permission sets recommended by the "Check 
Permissions" tab:

    Author:
      Node:
        access content
        view own unpublished content
        view revisions
        create [content type] content
        edit own [content type] content
      Workbench Moderation:
        view moderation messages
        use workbench_moderation my drafts tab
    
    Editor:
      Node:
        access content
        view revisions
        revert revisions
        edit any [content type] content
      Workbench:
        view all unpublished content
      Workbench Moderation:
        view moderation messages
        view moderation history
        use workbench_moderation my drafts tab
        use workbench_moderation needs review tab
    
    Moderator:
      Node:
        access content
        view revisions
        edit any [content type] content
      Workbench:
        view all unpublished content
      Workbench Moderation:
        view moderation messages
        view moderation history
        use workbench_moderation needs review tab
    Publisher
      Node:
        access content
        view revisions
        revert revisions
        edit any [content type] content
      Workbench:
        view all unpublished content
      Workbench Moderation:
        view moderation messages
        view moderation history
        use workbench_moderation needs review tab
        unpublish live revision

----
4.  Using the module

Once the module is installed and moderation is enabled for one or more node
types, users with permission may:

* Use the "Moderate" node tab to view moderation history and navigate versions.

When the Workbench module is enabled, users with permission may also:

* See messages about moderation state when visiting a moderated node.
* Moderate content from the "View Draft" page.

----
5.  Troubleshooting

* If users get access denied (403) errors when creating, editing, moderating, or
  reverting moderated content, the "Check Permissions" tab in Workbench
  Moderation's administration section can help diagnose what access is missing.
  See heading 3.3 in this README.

* If you're building Views of moderation records, keep in mind that for a single
  node, there will be multiple revisions, and for each revision, there may be
  multiple moderation records. This means it will be very easy to end up with a
  View that shows particular nodes or revisions more than once. Try adding the
  "Workbench Moderation: Current" filter, or using Views' "Use grouping" option
  (under the "Advanced settings" heading on the view editing page).

----
6.  Developer notes

Workbench Moderation does not have a mature API.

----
6.1  Database schema

Workbench Moderation uses three tables to track content moderation states.

* workbench_moderation_states
  Stores administrator-configured moderation states.

* workbench_moderation_transitions
  Stores administrator-configured transitions between moderation states. These
  are simply pairs of moderation states: a "from" state and a "to" state.

* workbench_moderation_node_history
  Stores individual moderation records related to each node revision. Each
  record stores the nid and vid of a node, the original moderation state and the
  new moderation state, the uid of the user who did the moderation, and a
  timestamp.

----
6.2  Views integration

Workbench Moderation provides Views integration so that site builders may
include moderation information in node and node revision views.

* Filters, fields, sorts, and arguments are provided for moderation record data.

* A relationship is provided from moderation records to the user who made the
  moderation change.

* A "content type is moderated" filter is provided on for nodes to help in
  creating lists of only moderated content.

----
7.  Feature roadmap

* Allow configuration of 'Draft' and 'Published' states.
Module:  Janrain Engage (formerly RPX)

Authors: Peat Bakke <peat@janrain.com>
         George Katsitadze <george@janrain.com>
         Nathan Rambeck <http://nathan.rambeck.org>
         Rendahl Weishar <ren@janrain.com>

         Many thanks to Ben Kaplan (BenK) for his great ideas and
         feedback. He is the driving force behind the new features in
         2.x

Description
===========

The Janrain Engage module (formerly RPX) integrates Drupal sites with
the powerful Janrain Engage service (www.janrain.com/products/engage).
Using Janrain Engage, Drupal sites can authenticate new and existing
users with popular third-party websites, map user profile data from
these websites to Drupal fields, and share Drupal content with a
user's existing social network on multiple third-party sites. The
result is an accelerated user registration process, an enhanced
ability to gather user data, and increased site traffic from the viral
promotion of website content.

In particular, the module helps Drupal websites quickly and seamlessly
integrate with 18 social networks and service providers, including
Facebook, Twitter, Google, Yahoo!, LinkedIn, Myspace, AOL, PayPal, and
Windows Live. Instead of having to integrate with each of these
websites on your own, the Janrain Engage module (and the underlying
Janrain Engage service) do the heavy lifting for you.


Features
===========

Some notable features of the module include:

* AUTHENTICATION:  Allow site visitors to register and login with one
  of their existing accounts at popular third-party websites. Support
  is included for both the Drupal user login block and the user login
  page. Quickly and easily converting anonymous site visitors into
  active registered users.

* LINKED ACCOUNT MANAGEMENT: A "Linked accounts" tab is provided to
  the end user (who has the appropriate module permission). Using this
  tab, a user can add, remove, or otherwise manage the third-party
  accounts connected to his/her Drupal site account.

* DATA MAPPING:  With permission of the user, you can map third-party
  user profile data to specific Drupal fields. A variety of fields
  are supported, including User fields, old-style Profile fields, and
  Profile2 contributed module fields.

* SOCIAL SHARING:  Make it easy for users to share their Drupal
  content and comments with friends and followers on other social
  networks. A "Share" button or link may be included on specific
  content types, which triggers the Janrain Engage social sharing
  widget.

* RULES INTEGRATION: For those using the popular Rules module
  (http://drupal.org/project/rules), you can configure the full range
  of Rules-based actions to occur (change a role, send an e-mail,
  etc.) whenever a user triggers certain events via Janrain
  Engage. The module currently provides the following Rules events:

     Linked account was added
     Linked account was deleted
     Social sharing cookie was set for shared content
     Social sharing cookie was set for shared comments
     Social sharing cookie was set for other information

  Additionally, the module provides a "Launch social sharing widget"
  action that enables a user to share with their third-party social
  network any other events provided by the Rules module or other
  contributed modules.

* VIEWS INTEGRATION: You can easily create views of your users that
  include data such as linked account type (i.e. Facebook), linked
  account ID, linked account icon, as well as an operation link to
  delete the linked account. These views can be used by site
  administrators, for example, to manage all of the linked third-party
  accounts on the site. Or you can use these views to create an
  alternate linked account management UI for end users. You can also
  configure a view to display reporting and analytics about the number
  of linked accounts of a given type that have been created on the
  site.


Supported Third-Party Websites
===========

The Janrain Engage service currently supports the following social
networks and service providers:

Facebook
Google
LinkedIn
Myspace
Twitter
Windows Live
Yahoo!
AOL
Blogger
Flickr
Hyves
Livejournal
OpenID
MyOpenID
Netlog
PayPal
Verisign
Wordpress

Because new providers are added on a regular basis, you can view the
most current list of providers at: https://rpxnow.com/docs/providers


Installation and Configuration
============

To install and configure this module, do the following:

1. Download the module's tarball, extract its contents, and move the
   resulting "rpx" directory into your site's "modules" directory.

2. Visit admin/modules and enable the "Janrain Engage Core," "Janrain
   Engage UI," and "Janrain Engage Widgets" modules. The "Janrain
   Engage Rules integration" module is optional if you would like
   those features. All of these modules can be found within the
   "Janrain Engage" fieldset.

3. Visit admin/people/permissions and configure available module
   permissions. This includes the "Administer Janrain Engage
   settings" permission and the "Manage own 3rd party identities"
   permission.

4. If you want users to be able to create their own accounts using
   Janrain Engage, you should visit admin/config/people/accounts and
   choose "Visitors" under the "Who can register accounts?" setting.

5. Visit admin/config/people/rpx and enter your Janrain Engage API
   key. This API key must be entered for the module to function. Once
   this API key is entered, the module will automatically populate
   your "Engage Realm" and "Engage Admin URL".

6. Also at admin/config/people/rpx, configure other module settings
   related to the user interface, authentication, social sharing, and
   verification e-mails.

7. Visit admin/config/people/rpx/profile and configure Field Mapping
   if you would like third-party profile data to be mapped to Drupal
   fields. You can map data to User fields
   (admin/config/people/accounts/fields), legacy Profile fields (for
   sites that have been upgraded from Drupal 6), or Profile2
   contributed module fields (http://drupal.org/project/profile2).

8. Login as a user with the "Manage own 3rd party identities"
   permission. Each user with this permission will have a "Linked
   accounts" tab by default on their account page.

NOTE: If you don't yet have a Janrain Engage API Key, please visit
the following link to create a Janrain Engage account:

http://www.janrain.com/products/engage/get-janrain-engage

You will be able to choose from a Basic (free), Plus, Pro, or
Enterprise level account. All account types are supported by this
module.

Additionally, in order to enable sign-in with Facebook, Linkedin,
Twitter, MySpace, Paypal, and Windows Live accounts (as well as social
publishing to Facebook, Twitter, Myspace, Linkedin and Yahoo!), you
must first create a free developer account with each respective
service. Easy-to-follow links and step-by-step instructions are
provided from your account control panel on the Janrain Engage
website.


RECOMMENDED MODULES
===============

* Rules (http://drupal.org/project/rules):  Allows you to configure
  actions that occur when a linked third-party account is added or
  removed. The Janrain Engage module also provides a social sharing
  action that allows you to post to third-party websites on other
  Drupal events.

* Profile2 (http://drupal.org/project/profile2):  Designed to be the
  successor of the core Profile module (which is deprecated for Drupal
  7), this module provides a new, fieldable "profile" entity.
  Third-party user data may be mapped directly to fields attached to
  these profile entities.

* Token (http://drupal.org/project/token): Tokens are small bits of
  text that can be placed into larger documents via simple
  placeholders. Although Drupal core supports tokens, this module adds
  some additional features. By enabling this module, you will see a
  browsable interface of available tokens in several administrative
  areas of the Janrain Engage module (where tokens are supported). You
  will be able to include a token (for instance, when defining your
  social sharing message text) simply by clicking on it).

* Views (http://drupal.org/project/views): Views provides a powerful
  and flexible way to display lists of content, users, and more. By
  enabling this module, you will be able to create user views that
  include field-level information about a user's linked accounts (via
  Janrain Engage). Views fields including linked account type, linked
  account ID, and linked account icon are supported.


DEMO SITE
===============

You can test the latest functionality and features at:
http://drupal7.janraindemo.com


DOCUMENTATION
===============

For detailed technical documentation, please visit:

* http://rpxnow.com/docs/
* http://api.drupal.org/


FAQ
===============

Q: My users get an error during registration that says "The configured
   token URL has not been whitelisted."  What should I do?

A: This is probably not a problem with the module itself. Try editing
   the app settings in your Janrain Engage account to use a wildcard
   for subdomains. So your domains would include mysite.com and also
   *.mysite.com.

Q: I want to set-up a Rules action that only happens when a user adds
   his Facebook account. How do it do this?

A: First, create a rule on the "Linked account was added" event.
   Then, create a "data comparison" condition and choose
   "rpx:provider-title" as the data to compare. Select "equals" as
   your comparison operator and enter "Facebook" as the data value.
   Any action that you now configure will only occur if the user adds
   a Facebook account. You can follow the same procedure for any
   other supported third-party website. Note that to get the same
   result you could also use "rpx:provider-machinename" as the data to
   compare and "facebook" (not capitalized) as the data value.
Service Links 2.x:
------------------
Author and mantainer: Fabio Mucciante aka TheCrow (since the 2.x branch)
Current co-mantainer: Simon Georges
Requirements:         Drupal 7
License:              GPL (see LICENSE.txt)

Introduction
------------
This module is the enhanced version of Service Links 1.x developed
by Fredrik Jonsson, rewritten and improved to fit the new purposes:
extend easily the number of services supported and provide APIs to
print links everywhere within any content.
At the address http://servicelinks.altervista.org/?q=service
a web interface helps to create a module including the services
not availables in the standard package.

Overview
---------
Service Links provide an amount of 70+ social networks
from around the World where submit the link of a given content,
below a short list:

* del.icio.us
* Digg
* Facebook
* Furl
* Google
* IceRocket
* LinkedIn
* MySpace
* Newsvine
* Reddit
* StumbleUpon
* Technorati
* Twitter
* Yahoo
* ...

The admin decides:
- the style to render the links: text, image, text + image
- to show links only for certain node types or some categories
- to add links within the content body, among the other links, or in a block
- what roles are allowed to see the selected links.

Within the 2.x branch has been introduced:
- modular management of services, grouped by different language area,
  through external modules implementing the hook_service_links()
- sorting of services through drag'n drop
- support for buttons which make use of Javascript without break the
  XHTML specifies to keep the module more 'accessible' as possible
- improved the use with not node pages
- support for other Drupal modules: Display Suite, Forward, Views, Short Url
- support for sprites to render the service images
- support for browser bookmarking (Chrome, Firefox, IE, Opera)
- two APIs to print easily the whole set of services or a customs subset of them
- configurable list of pages to show/hide on also through PHP code

A more detailed list of options and related explaining is available at the page:
http://servicelinks.altervista.org/?q=about

Installation and configuration
-------------------------------
1) Copy the whole 'service_links' folder under your 'modules' directory and then
   
2) Point your browser to administer >> modules', enable 'Service Links' and one
   of the 'XXX Services' provided, 'General Services' contain the most know social
   networks, and 'Widgets Services' the most used buttons

3) Go to 'administer >> access control' for allow users to watch the links.

4) At 'administer >> settings >> service links' select for what type of content
   enable Service Links and in 'Services' tab select the services to show.

More information
----------------

The file 'template.php' contains some examples about phptemplate variables

The file 'service_links.api.php' contains info about the hooks implemented

More info regarding installation and first configuration, set up of the available
options, either extension of the number of services and theming output are available
on the online documentation at the address:
http://servicelinks.altervista.org/?q=about

More services can be included and packed within an external module customizable
through a web interface available at the address:
http://servicelinks.altervista.org/?q=service

Link Checker
------------

Installation:

1. Install linkchecker via Modules page.
2. Go to Modules and enable the "Link checker" module.
3. Go to Configuration -> Content authoring -> Link checker and enable the node types to scan.
4. Under "Link extraction" check all HTML tags that should be scanned.
5. Adjust the other settings if the defaults don't suit your needs.
6. Save configuration
7. Wait for cron to check all your links... this may take some time! :-)

If links are broken they appear under Reports -> Broken links.

If not, make sure cron is configured and running properly on your Drupal
installation. The Link checker module also logs somewhat useful info about it's
activity under Reports -> Recent log messages.


Required:

1. For internal URL extraction you need to make sure that Cron always get called
   with your real public site URL (for e.g. http://example.com/cron.php). Make
   sure it's never executed with http://localhost/cron.php or any other
   hostnames or ports, not available from public. Otherwise all links may be
   reported as broken and cannot verified as they should be.

   To make sure it always works - it's required to configure the $base_url in
   the sites settings.php with your public sites URL. Better safe than sorry!


Known issues:

There are a lot of known issues in drupal_http_request(). These have been solved
in HTTPRL. As a workaround it's recommended to use HTTPRL in linkchecker.

Issues list:
 
* #997648: drupal_http_request() always calls fread() one more time than necessary
* #164365-12: drupal_http_request() does handle (invalid) non-absolute redirects
* #205969-11: drupal_http_request() assumes presence of Reason-Phrase in response Status-Line
* #371495: Error message from drupal_http_request() not UTF8 encoded
* #193073-11: drupal_http_request - socket not initialized
* #106506-8: drupal_http_request() does not handle 'chunked' responses - Make it support HTTP 1.1
* #1096890-15: drupal_http_request should return error if reaches max allowed redirects
* #875342-21: drupal_http_request() should pick up X-Drupal-Assertion-* HTTP headers
* #965078-31: HTTP request checking is unreliable and should be removed in favor of watchdog() calls
* #336367: HTTP client should protect commas when folding (compatibility with legacy HTTP/1.0)
* #45338: log fsockopen errors to watchdog
Metatag
-------
This module allows you to automatically provide structured metadata, aka "meta
tags", about your website and web pages.

In the context of search engine optimization, providing an extensive set of
meta tags may help improve your site's & pages' ranking, thus may aid with
achieving a more prominent display of your content within search engine
results. Additionally, using meta tags can help control the summary content
that is used within social networks when visitors link to your site,
particularly the Open Graph submodule for use with Facebook (see below).

This version of the module only works with Drupal 7.15 and newer.


Features
------------------------------------------------------------------------------
The primary features include:

* The current supported basic meta tags are ABSTRACT, DESCRIPTION, CANONICAL,
  COPYRIGHT, GENERATOR, IMAGE_SRC, KEYWORDS, PUBLISHER, ROBOTS, SHORTLINK and
  the page's TITLE tag.

* Multi-lingual support using the Entity Translation module.

* Translation support using the Internationalization (i18n) module.

* Per-path control over meta tags using the "Metatag: Context" submodule
  (requires the Context module).

* Integration with the Views module allowing meta tags to be controlled for
  individual Views pages, with each display in the view able to have different
  meta tags, by using the "Metatag: Views" submodule.

* Integration with the Panels module allowing meta tags to be controlled for
  individual Panels pages, by using the "Metatag: Panels" submodule.

* The fifteen Dublin Core Basic Element Set 1.1 meta tags may be added by
  enabling the "Metatag: Dublin Core" submodule.

* The Open Graph Protocol meta tags, as used by Facebook, may be added by
  enabling the "Metatag: Open Graph" submodule.

* The Twitter Cards meta tags may be added by enabling the "Metatag: Twitter
  Cards" submodule.

* An API allowing for additional meta tags to be added, beyond what is provided
  by this module - see metatag.api.php for full details.

* Support for the Migrate module for migrating data from another system - see
  metatag.migrate.inc for full details.

* Support for the Feeds module for importing data from external data sources or
  file uploads.


Configuration
------------------------------------------------------------------------------
 1. On the People Permissions administration page ("Administer >> People
    >> Permissions") you need to assign:

    - The "Administer meta tags" permission to the roles that are allowed to
      access the meta tags admin pages to control the site defaults.

    - The "Edit meta tags" permission to the roles that are allowed to change
      meta tags on each individual page (node, term, etc).

 2. The main admininistrative page controls the site-wide defaults, both global
    settings and defaults per entity (node, term, etc), in addition to those
    assigned specifically for the front page:
      admin/config/search/metatags

 3. Each supported entity object (nodes, terms, users) will have a set of meta
    tag fields available for customization on their respective edit page, these
    will inherit their values from the defaults assigned in #2 above. Any
    values that are not overridden per object will automatically update should
    the defaults be updated.

 4. As the meta tags are output using Tokens, it may be necessary to customize
    the token display for the site's entities (content types, vocabularies,
    etc). To do this go to e.g. admin/structure/types/manage/article/display, in
    the "Custom Display Settings" section ensure that "Tokens" is checked (save
    the form if necessary), then to customize the tokens go to:
    admin/structure/types/manage/article/display/token


Internationalization: i18n.module
------------------------------------------------------------------------------
All default configurations may be translated using the Internationalization
(i18n) module. The custom strings that are assigned to e.g. the "Global: Front
page" configuration will show up in the Translate Interface admin page
(admin/config/regional/translate/translate) and may be customized per language.


Fine Tuning
------------------------------------------------------------------------------
* By default Metatag will load the global default values for all pages that do
  not have meta tags assigned via the normal entity display or via Metatag
  Context. This may be disabled by setting the variable 'metatag_load_all_pages'
  to FALSE through one of the following methods:
  * Use Drush to set the value:
    drush vset metatag_load_all_pages FALSE
  * Hardcode the value in the site's settings.php file:
    $conf['metatag_load_all_pages'] = FALSE;
  To re-enable this option simply set the value to TRUE.


Developers
------------------------------------------------------------------------------
Full API documentation is available in metatag.api.php.

To enable Metatag support in custom entities, add 'metatag' => TRUE to either
the entity or bundle definition in hook_entity_info(); see metatag.api.php for
further details and example code.


Troubleshooting / Known Issues
------------------------------------------------------------------------------
* When using custom page template files, e.g. page--front.tpl.php, it is
  important to ensure that the following code is present in the template file:
    <?php render($page['content']); ?>
  or
    <?php render($page['content']['metatags']); ?>
  Without one of these being present the meta tags will not be displayed.
* Versions of Drupal older than v7.17 were missing necessary functionality for
  taxonomy term pages to work correctly.
* Using Metatag with values assigned for the page title and the Page Title
  module simultaneously can cause conflicts and unexpected results.
* Using the Exclude Node Title module will cause the [node:title] token to be
  empty on node pages, so using [current-page:title] will work around the
  issue. Note: it isn't possible to "fix" this as it's a by-product of what
  Exclude Node Title does - it removes the node title from display.
* When customizing the meta tags for user pages, it is strongly recommended to
  not use the [current-user] tokens, these pertain to the person *viewing* the
  page and not e.g. the person who authored a page.
* If images being displayed in image tags need to be resized to fit a specific
  requirements, use the Imagecache Token module to customize the value.
* Certain browser plugins, e.g. on Chrome, can cause the page title so be
  displayed with additional doublequotes, e.g. instead of:
    <title>The page title | My cool site</title>
  it will show:
    <title>"The page title | My cool site"</title>
  The solution is to remove the browser plugin - the page's actual output is not
  affected, it is just a problem in the browser.


Related modules
------------------------------------------------------------------------------
Some modules are available that extend Metatag with additional functionality:

* Domain Meta Tags
  http://drupal.org/project/domain_meta
  Integrates with the Domain Access module, so each site of a multi-domain
  install can separately control their meta tags.

* Select or Other
  http://drupal.org/project/select_or_other
  Enhances the user experience of the metatag_opengraph submodule by allowing
  the creation of custom Open Graph types.

* Imagecache Token
  http://drupal.org/project/imagecache_token
  Provide tokens to load fields using an image style preset, for when meta tags
  need to fix exact requirements.


Credits / Contact
------------------------------------------------------------------------------
Currently maintained by Dave Reid [1] and Damien McKenna [2].

All initial development was sponsored by Acquia [3] and Palantir [4];
continued development sponsored by Palantir and Mediacurrent [5].

The best way to contact the authors is to submit an issue, be it a support
request, a feature request or a bug report, in the project issue queue:
  http://drupal.org/project/issues/metatag


References
------------------------------------------------------------------------------
1: http://drupal.org/user/53892
2: http://drupal.org/user/108450
3: http://www.acquia.com/
4: http://www.palantir.net/
5: http://www.mediacurrent.com/
Metatag: Dublin Core
--------------------
This module adds the fifteen Dublin Core Metadata Element Set [1] to the
available meta tags, as defined by the Dublin Core Metadata Institute [2].

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
1: http://dublincore.org/documents/dces/
2: http://www.dublincore.org/
3: http://drupal.org/user/960720
4: http://www.gemeentemuseum.nl/
5: http://drupal.org/node/1491616
Metatag: Panels
-----------------
This module adds support for meta tag configuration for Panels pages.

Configuration is done within the "Metatag" tab existant in the Page Manager
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
1: http://drupal.org/user/887060
2: http://dri-global.com
3: http://drupal.org/project/panels_breadcrumbs
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
* twitter:image
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
3: http://drupal.org/user/960720
4: http://www.gemeentemuseum.nl/
5: http://drupal.org/node/1664322
Metatag Context
---------------
This module is provides a Metatag reaction for Context [1], thus allowing meta
tags to be assigned to specific paths and other conditions.

Configuration can controlled via the normal Context UI module or the new admin
page available at: admin/config/search/metatags/context


Credits
------------------------------------------------------------------------------
This module is based on the Context Metadata [2] module. The initial
development was by Marcin Pajdzik [3] (sponsored by Dennis Publishing [4]).


References
------------------------------------------------------------------------------
1: http://drupal.org/project/context
2: http://drupal.org/project/context_metadata
3: http://drupal.org/user/160555
4: http://www.dennis.co.uk/
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
1: http://drupal.org/user/53892
                  __ _      _     _
                 / _(_)    | |   | |
 __ _  ___  ___ | |_ _  ___| | __| |
/ _` |/ _ \/ _ \|  _| |/ _ \ |/ _` |
| (_| | __/ (_) | | | |  __/ | (_| |
\__, |\___|\___/|_| |_|\___|_|\__,_|
 __/ |
|___/

CONTENTS OF THIS FILE
---------------------

 * About Geofield
 * Install
 * Configure
 * Credits
 * API notes

ABOUT GEOFIELD
--------------
Geofield (http://drupal.org/project/geofield) is a Drupal 7 module that
provides a field types for storing geographic data. This data can be attached
to any entity, e.g., nodes, users and taxonomy terms. Geofield provides
different widgets for data input and formatters for data output. The Geofield
module can can store data as Latitude and Longitude, Bounding Box and Well
Known Text (WKT) and it supports all types of geographical data: points,
lines, polygons, multitypes et cetera.

Great documentation on Geofield can be found at http://drupal.org/node/1089574

INSTALL
-------

Install the modules Geofield and geoPHP in the usual way. General information
on installing Drupal modules can be found here: http://drupal.
org/documentation/install/modules-themes/modules-7

Optionally install Open Layers 2: http://drupal.org/project/openlayers

CONFIGURE
---------

To add a geofield to a content type go to /admin/structure/types/ and choose
"Manage fields" for the chosen content type. Add a new field of the field type
"Geofield", and choose the preferred widget, e.g., "OpenLayers Map". Configure
the field according ton the chosen options.

Geofield comes with the basic but easy-to-use submodule Geofield Map that
allows you to display geographical data in a Google map. Enable Geofield Map
at /admin/modules. Read more about Geofield Map at
http://drupal.org/node/1466490

For more advanced and flexible data display you need to configure or create a
map in OpenLayers at /admin/structure/openlayers/maps. You can easily create
your own map by cloning an existing one. An introduction to OpenLayers can be
found here: http://drupal.org/node/1481374.

When you have configured a map in OpenLayers you must define to use the map.
Go to  /admin/structure/types and choose "Manage display".

Note: you can also add a geofield to a user, a taxonomy term or a comment.

CREDITS
-------
Original author:  Tristan O'Neil
Contributors:     Alex Barth, Jeff Miccolis, Young Hahn, Tom MacWright,
                  Patrick Hayes, Dave Tarc, Nikhil Trivedi, Marek Sotak,
                  Khalid Jebbari, Brandon Morrison, David Peterson

API NOTES
---------
Geofield fields contain nine columns of information about the geographic data
that is stores. At its heart is the 'wkt' column where it stores the full
geometry in the 'Well Known Text' (WKT) format. All other columns are metadata
derived from the WKT column. Columns are as follows:

  'wkt'          WKT
  'geo_type'     Type of geometry (point, linestring, polygon etc.)
  'lat'          Centroid (Latitude or Y)
  'lon'          Centroid (Longitude or X)
  'top'          Bounding Box Top (Latitude or Max Y)
  'bottom'       Bounding Box Bottom (Latitude or Min Y)
  'left'         Bounding Box Left (Longitude or Min X)
  'right'        Bounding Box Right (Longitude or Max X)

When a geofield is saved using the provided widgets, these values are passed
through the geofield_compute_values function in order to compute dependent
values. By default dependent values are computed based on WKT, but this may be
overriden to compute values based on other columns. For example,
geofield_compute_values may be called like so:

  geofield_compute_values($values, 'latlon');

This will compute the wkt field (and all other fields) based on the lat/lon
columns, resulting in a point. As a developer this is important to remember if
you modify geofield information using node_load and node_save. Make sure to
run any modified geofield instances through geofield_compute_values in order
to make all columns consistent.

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
  The configuration page is at admin/config/people/captcha,
  where you can configure the CAPTCHA module
  and enable challenges for the desired forms.
  You can also tweak the image CAPTCHA to your liking.
It possible to put your own fonts for the Image CAPTCHA in this folder.
However, this is not the recommended way, as they can get lost easily during
a module update. The recommended way to provide your own fonts is putting them
in the files directory of your Drupal setup or, just like with contributed
modules and themes, in the "libraries" folders sites/all/libraries/fonts
or sites/<site>/libraries/fonts.

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
-- SUMMARY --
qTip is another tooltip module for Drupal. By using a simple input filter in your
code you can have a stylish tooltip in just seconds.


-- REQUIREMENTS --
You must download and install the qTip library from
http://craigsworks.com/projects/qtip/download/
This library is licensed under MIT and therefore is not allowed to be hosted on drupal.org

Make sure that you select the 'Production' option. You may download the development
option as well if you would like to check out the code and select to use it on the
admin settings page (under Advanced options), but it is recommended that you use the
compressed 'Production' version of the library on production (live) sites.

Place the extracted contents of the library into /sites/all/libraries/qtip
NOTE: You may have to create the libraries directory
  You should end up with something like this:
    /sites/all/libraries
      /qtip (You will need to create this directory)
        jquery.qtip-1.0.0-rc3.min.js
        REQUIREMENTS
        INSTALL
        LICENSE


-- INSTALLATION --
* Install as usual (see dependency above), see http://drupal.org/node/70151 for further information.


-- CONFIGURATION --
* Once installed, go to admin/config/content/qtip
    * Select how you would like your qTips to display. Save.
* If you want to use simple tooltips via a filter:
    * Go to admin/config/content/formats
        * Click 'configure' on the input filter that you would like to add qTip to
          NOTE: For input filters that have 'HTML filter' enabled (like Filtered HTML), qTip MUST be weighted heavier than HTML filter
            This should be default, but it would be a good idea to check.
    * Save and repeat for as many input filters as you would like.

-- USAGE --
* On a node page enter the filter with one of the following formats:
    Without heading text:
      [qtip:Name of link (target) text|Text to appear in tooltip]
    With heading text:
      [qtip:Name of link (target) text|Header to appear in tooltip|Text to appear in tooltip]
* To use more advanced (including HTML markup) tooltips:
  NOTE: For input filters that have 'HTML filter' enabled (like Filtered HTML), this option will not work!
    * Use the following structure on a node page
        * <span class="qtip-link">
            <span class="qtip-header">Tooltip Heading (optional)</span>
            <span class="qtip-tooltip">Tooltip content</span>
            Link text to tooltip
          </span>
        * You do not have to specify a heading.
        * The tooltip content area can contain any HTML markup.
* Below is an example template of how each tooltip HTML is structured. Use this for custom CSS styling
  NOTE: For performance, these are not created until the cooresponding link is hovered or clicked for the first time (per page load)
    <div id="ui-tooltip-0" role="tooltip" class="ui-tooltip qtip ui-helper-reset ui-tooltip-red ui-tooltip-focus ui-tooltip-pos-rc" aria-hidden="true">
      <div class="ui-tooltip-tip">
        <canvas width="12" height="12"></canvas>
      </div>
      <div class="ui-tooltip-wrapper">
        <div class="ui-tooltip-titlebar">
          <div id="ui-tooltip-0-title" class="ui-tooltip-title">Test Header</div>
        </div>
        <div class="ui-tooltip-content " id="ui-tooltip-0-content">Tooltip Text</div>
      </div>
    </div>
    NOTE: You may have to use !important with your CSS rules as some of the rules are set inline by the qTip library.


-- MAINTAINERS --
Current maintainers:
* Jacob Neher (bocaj) - http://drupal.org/user/582042


-- SPECIAL THANKS --
To Craig Thompson, creator of the qTip jQuery plugin!
http://craigsworks.com********************************************************************
                P A G E    T I T L E    M O D U L E
********************************************************************
Original Author: Robert Douglass
Current Maintainers: Nicholas Thompson and John Wilkins

********************************************************************
DESCRIPTION:

   This module gives you control over the page title. It gives you the chance
   to provide patterns for how the title should be structured, and on node
   pages, gives you the chance to specify the page title rather than defaulting
   to the node title.

********************************************************************
PERMISSIONS:

   This module defines the "set page title" and "administer page titles"
   permissions. The "set page title" permission determines whether a user will
   be able to edit the "Page title" field on node edit forms (if visible.) The
   "administer page titles" permission determines whether a user will be able to
   edit the "Page title" administration pages.

********************************************************************
INSTALLATION:

1. Place the entire page_title directory into your Drupal modules/
   directory or the sites modules directory (eg site/default/modules)


2. Enable this module by navigating to:

     Administration > Modules

   At this point the Drupal install system will attempt to create the database
   table page_title. You should see a message confirming success or
   proclaiming failure. If the database table creation did not succeed,
   you will need to manually add the following table definition to your
   database:

    CREATE TABLE `page_title` (
      `type` varchar(15) NOT NULL default 'node',
      `id` int(10) unsigned NOT NULL default '0',
      `page_title` varchar(255) NOT NULL default '',
      PRIMARY KEY  (`type`,`id`)
    );

3. Optionally configure the two variations of page title by visiting:

    Administration > Configuration > Search and metadata
/**
 * @file
 * README file for Workbench Access.
 */

Workbench Access
A pluggable, hierarchical editorial access control system

Please see https://drupal.org/documentation/modules/workbench_access for
documentation, including installation and configuration walkthroughs.


----------------
Version history
----------------

7.2-1.2 27-JAN-2013
7.x-1.1 18-JAN-2013
7.x-1.0 26-AUG-2011
[![Build Status](https://travis-ci.org/RESTful-Drupal/restful_search_api.svg?branch=7.x-2.x)](https://travis-ci.org/RESTful-Drupal/restful_search_api)

# RESTful Search API
Expose your Search API results with your RESTful API.

## Features
Building a search engine integration with faceted search in Drupal is really
easy with Search API and all the helper modules around it. With this module you
can expose your search to your decoupled consumer.

### Get the output that you want for your search
This falls in line with the philosophy of the RESTful module, where you get the
exact output that you need. To do so you need to be declarative about it by
implementing `publicFieldsInfo`.

First of all configure your search index in Drupal using Search API to index the
fields that you want to make searchable and you want to output. Once you have
Search API configured, implement `publicFieldsInfo` to control how you expose
each field that you need to expose with your HTTP API. 

#### How do I know the properties to map to?
You will notice in the examples that you have to indicate the name of the
property. Some times it is complicated to know what properties you have
available in the search results that Search API returns, to be mapped by
RESTful. In those situations it is helpful to use the `pass_through` option in
your resource definition. That will output every available property regardless
of the mappings that you have done in `publicFieldsInfo`. 

### Sort by any public property
You just need to provide the sort query string to sort your results:

```
curl https://www.example.org/api/search/lorem?sort=-created,id
```

Prepend a `-` in front of the sort key to sort in descending order.

You can use any property that supports sorting in your search index, that will
be passed to Search API.

Additionally you can use any public property in your final output to sort the
results. If the selected property does not support sorting in Search API the
sorting will be applied to the output generated after making the query to Search
API without sorting. Use this type of sorting only if you really need to, the
preferred method is to use the supported sort properties in Search API.

### Filter by your facets
Add some facets to the Search API configuration and use them in your search
queries. To do so use
[the same format used in RESTful](https://github.com/RESTful-Drupal/restful#filter-1).

If a search has relevant facet information attached, those will be sent along
with the search results.

```javascript
// https://www.example.org/api/basic_search/elit?filter[comment_count][value]=2&filter[comment_count][operator]=">="
{
    "count": 23,
    "facets": {
        "author": [
            { "filter": "\"0\"", "count": 12 },
            { "filter": "\"1\"", "count": 11 }
        ],
        "comment_count": [
            { "filter": "\"2\"", "count": 13 },
            { "filter": "\"3\"", "count": 10 }
        ]
    },
    "data": [
        { "entity_id": 704, "version_id": 704, "relevance": 0.013727446 },
        …
    ]
}
```
## Additional information
See [this post in Medium](https://medium.com/@e0ipso/restful-drupal-with-search-api-f370050a26bb) with some additional information.
Simple module to add PSR-0 and PSR-4 support to the Drupal 7 Core registry.

### INSTALL

- Enable the module
- Change your .info files and add ```registry_autoload[] = PSR-0|PSR-4``` key (choose one)
- Put your files in src/ for PSR-4 and lib/ for PSR-0.
- DONE

Alternatively to the registry\_autoload key use:

````
  registry_autoload_files[] = filename
````

to specify all your files manually and avoid the file system scan.

It is still advised to provide files in PSR-0 or PSR-4 format, so that you can
switch to another autoloader later.

### FORMAT

Add the following keys to your modules .info file to search the respective
subdir for .php files:

sample.info:

````
  registry_autoload[] = PSR-0
  registry_autoload[] = PSR-4
  registry_autoload[] = PHPUnit
````

PSR-0 will by default search the lib/ subdirectory of your module and the
convention is to repeat the full namespace, e.g.

lib/Drupal/Core/Cache/CacheableInterface.php

with:

````php
namespace Drupal\Core\Cache;
````

PSR-4 will by default search the src/ subdirectory of your module and the
convention is to only repeat the namespace after Drupal/your\_module:

src/Cache/CacheableInterface.php

with:

````php
namespace Drupal\your_module\Cache;
````

### AVOID FILE SYSTEM SCAN 

If you want to avoid the static file\_scan\_directory use:

````
  registry_autoload_files[] = filename
````

The PSR-0 and PSR-4 are just shortcuts if you want to register all your files
automatically.

### SEARCHING ARBITRARY PATHS

To support arbitrary libraries in e.g. sites/all/libraries use e.g:

````
  registry_autoload[DRUPAL_ROOT/sites/all/libraries/mylibrary/lib] = PSR-0
  registry_autoload[DRUPAL_ROOT/sites/all/libraries/mylibrary/src] = PSR-4
````

DRUPAL\_ROOT is the only supported constant here and will be replaced with the constant ```DRUPAL_ROOT```.

To add arbitrary paths relative to the module, use e.g.:

````
  registry_autoload[mylibrary/lib] = PSR-0
  registry_autoload[mylibrary/src] = PSR-4
````

Note that neither lib/ nor src/ are appended when specifying a path yourself.

### Traits

PHP 5.4 traits are supported. For PHP versions < 5.4, the files with trait declarations are simply ignored.

### RELATED MODULES

xautoload is a related module.

The difference is that this statically scans all files during the registry
rebuild to register the files, while xautoload does it dynamically during
runtime based on the class name.

However this does only need the D7 core registry and only changes the registry
in a way to add namespaced files, which core could support, too.

### STATUS

[![Build Status](https://travis-ci.org/LionsAd/registry_autoload.svg?branch=7.x-1.x)](https://travis-ci.org/LionsAd/registry_autoload)
SUMMARY - YouTube Field
========================
The YouTube field module provides a simple field that allows you to add a
YouTube video to a content type, user, or any entity.

Display types include:

 * YouTube videos of various sizes and options.
 * YouTube thumbnails with image styles.


REQUIREMENTS
-------------
All dependencies of this module are enabled by default in Drupal 7.x.


INSTALLATION
-------------
Install this module as usual. Please see
http://drupal.org/documentation/install/modules-themes/modules-7


USAGE
-------
To use this module create a new field of type 'YouTube video'. This field will
accept YouTube URLs of the following formats:

 * http://youtube.com/watch?v=[video_id]
 * http://youtu.be/[video_id]
 * http://youtube.com/v/[video_id]
 * http://youtube.com/embed/[video_id]
 * http://youtube.com/?v=[video_id]

All formats listed above can also be provided without 'http://', with 'www.',
or with 'https://' rather than 'http://'. The last format can be provided with
additional parameters (ignored) and v does not have to be the first parameter.

To enable Colorbox support, enable the YouTube Field Colorbox module included in
this directory and consult its README file.


CONFIGURATION
--------------
Global module settings can be found at admin/config/media/youtube.

The video output of a YouTube field can be manipulated in three ways:
 * global parameters found on the configuration page mentioned above
 * field-specific parameters found in that particular field's display settings
 * Views settings for the specific field

The thumbnail of the YouTube image can also be used and can link to either the
content, the video on YouTube, or nothing at all.

To configure the field settings:

 1. click 'manage display' on the listing of entity types
 2. click the configuration gear to the right of the YouTube field


SUPPORT
--------
Please use the issue queue to report bugs or request support:
http://drupal.org/project/issues/youtube
SUMMARY - YouTube Field Colorbox
=================================
Provides Colorbox support to the YouTube Field module.

Provides the ability to link YouTube thumbnails to be opened in a YouTube video
player within a Colorbox modal window. Display settings can alter the Colorbox
size and other parameter options.


REQUIREMENTS
-------------
 - YouTube Field
 - Colorbox


INSTALLATION
-------------
Install this module as usual. Please see
http://drupal.org/documentation/install/modules-themes/modules-7


USAGE
------
To use this module:
 1. The Colorbox plugin must be properly included. The status of this can be
    checked at admin/reports/status.
 2. 'Enable Colorbox load' must be enabled on the Colorbox module settings. This
    setting is found at admin/config/media/colorbox.


CONFIGURATION
--------------
There are no global module settings.

Once enabled, to use and configure this module:
 1. Create a YouTube field (see USAGE within YouTube Field's README).
 2. Alter the YouTube field's display settings.
 3. Select 'YouTube thumbnail' for the format option.
 4. Under format settings (click gear), select 'Colorbox' under 'Link image to'.
 5. Alter the parameters and other settings available when 'Colorbox' is chosen.


SUPPORT
--------
Please use the issue queue to report bugs or request support:
http://drupal.org/project/issues/youtube
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Configuration
 * Credits
 * Maintainers


INTRODUCTION
------------
Provides an ability to output Views exposed filters in layouts.

 * For a full description of the module, visit the project page:
   https://drupal.org/project/vefl

 * To submit bug reports and feature suggestions, or to track changes:
   https://drupal.org/project/issues/vefl


FEATURES
--------
 * Provides Default and supports Panels layouts.
 * You can define custom layouts with regions.
 * You can override exposed form template as usual.
 * Supports Better exposed filters module.


REQUIREMENTS
------------
This module requires the following modules:
 * Views (https://drupal.org/project/views)


INSTALLATION
------------
Install as you would normally install a contributed drupal module.
See: https://drupal.org/documentation/install/modules-themes/modules-7
for further information.


CONFIGURATION
-------------
* For site-builders:
  -On views edit page find Exposed form section.
  -Choose Basic (with layout) or Better Exposed Filters (with layout) Exposed form style.
  -Exposed form settings form find Layout settings fieldset.
  -Choose Layout and click Change. Do you need more default layouts?
  -Set in which region each exposed filter will be outputted.
  -Click Apply and have fun.
* For developers:
  -You can define custom layouts, see an example in vefl.api.php.
  -You can override exposed form template as usual:
  -In your theme define views-exposed-form.tpl.php, use $region_widgets variable to output widgets by regions.
  -views-exposed-form--VIEWNAME.tpl.php or views-exposed-form--VIEWNAME--DISPLAYNAME.tpl.php also work.


CREDITS
-------
The project sponsored by
Bright Solutions GmbH (https://www.drupal.org/node/1469032).


MAINTAINERS
-----------
Current maintainers:
 * Sergey Korzh (korgik) - https://drupal.org/user/813560
OAuth implements the OAuth classes for use with Drupal and acts as a support
module for other modules that wish to use OAuth.

OAuth Client flow:

The callback to be used is /oauth/authorized/% where % is the id of the consumer
used by the client. We need the id of the consumer to be able to find the token
correctly.

# Boxes

Boxes module is a reimplementation of the custom blocks (boxes) that the core
block module provides. It is a proof of concept for what a re-worked block
module could do.

The module assumes that custom blocks are configuration, and not content. This
means that it is a reasonable action to ask for all blocks at one time, this is
in fact exactly what the core block module does.

## Features

**Inline editing.** Boxes provides an inline interface for editing blocks,
allowing you to change the contents of blocks without going to an admin page.

**Exportability.** Boxes provided blocks can be exported into code. Note; this
includes the settings for the boxes themselves and not visibility rules. For
exporting visibility settings the Context[1] module is recommended.

**Pluggable box types.** Boxes includes a basic "box type" that mimics how custom
blocks behave in core. Boxes is designed to allow for modules to provide
additional "box types" that have different configuration and rendering options.

## Chaos tools support

Boxes provides exportables for its blocks via the required Chaos tools[2]
module. This allows modules to provide blocks in code that can be overwritten
in the UI.

Chaos tools is required to use Boxes.

## Spaces support

Boxes provides a Spaces[3] controller class that allows individual spaces to
override a particular block, or even define a completely new block for a
specific space.

Spaces is not required by boxes.

## Todo

* Boxes need language awareness.
* The inline editing experience could be nicer.


[1] http://drupal.org/project/context
[2] http://drupal.org/project/ctools
[3] http://drupal.org/project/spaces
TAXONOMY MENU
=============
(README.txt: 13th of April 2009, Version 6.x-2.3, indytechcook + ksc)

-------------- Content ------------------
INTRO
INSTALLATION
- New
- Upgrade
CONFIGURATION
- Where to find the configuration screen?
- Adjustments and options
PATH TYPES and INTEGRATION WITH VIEWS MODULE
- Menu Path Type: Default
- Menu Path Type: Hierarchy
- Menu Path Type: Custom
INTEGRATION WITH OTHER MODULES
- TAXONOMY MANGAGER
- TAXONOMY REDIRECT
- CONTENT TAXONOMY
- TAXONOMY BREADCRUMBS
- HIERARCHICAL SELECT
- i18n
- DOMAIN ACCESS
- PATHAUTO
ADDITIONAL NOTES
PROSPECT TO PLANNED FUNCTIONS
------------- End Content -----------------


INTRO
=====
This module adds links (menu entries) to taxonomy terms to the global navigation menu.
With the current version users can create one group of menu entries and add specific options 
for each vocabulary. More functionality is beeing planned with further versions. 

INSTALLATION
============

NEW 

1) Place this module directory in your "modules" folder (this will usually be
   "sites/all/modules/"). Don't install your module in Drupal core's "modules"
   folder, since that will cause problems and is bad practice in general. If
   "sites/all/modules" doesn't exist yet, just create it.

2) Enable the Taxonomy Menu module in Drupal at:
   administration -> site configuration -> modules (admin/build/modules)
   The Drupal core taxonomy module is required.
   The modules Taxonomy Menu Custom Path and Taxonomy Menu Hierarchy provide
   additional path configuration types (see the "INTEGRATION WITH VIEWS MODULE" section below). 

3) Create a new vocabulary or edit an excisting one.
   
4) Choose which vocabularies to appear in the menu at:
   administration -> content management -> taxonomy
   (admin/content/taxonomy)

UPGRADE
Please read UPGRADE.txt


CONFIGURATION
=============

LOCATION OF CONFIGURATION SCREEN
 All configuration options are on the vocabulary's edit screen: 
  admin/content/taxonomy   (or)
  admin/content/taxonomy/edit/vocabulary/$vid

ADJUSTMENTS AND OPTIONS
 Menu: Select under which menu the vocabulary's terms should appear. 
  With the current version users can create one group of menu entries for each vocabulary.
 
 Menu Path Type: Select how the url for the term path should be created. 
  Included are Default, Hierarchy and Custom Path.
  To use Hierarchy and/or Custom Path you need to enable the related modules first.  
  Menu Path Type = Default: The path will be taxonomy/term/% while Term ID will be passed as argument.
  (multiple arguments possible). This path type uses standard taxonomy display - views is not needed.
  
  For other path types and their options see: INTEGRATION WITH VIEWS MODULE
  For developers: This is extendable using hook_taxonomy_menu_path().
  See developers documentation for more information. (http://drupal.org/node/380652)
  
 Syncronise changes to this vocabulary: If selected, the menu will auto update when you
  change a node or term. Recommened to always have this selected.
  When you change the generated menu with the core menu function, i.e. move it or change the structure, 
  these changes most probably get lost when adding a new taxonomy term because Taxonomy Menu rebuilds
  the menu without knowing about the changes made elsewhere.
 
 Display Number of Nodes: Displays the number of nodes next to the term in the menu.
  If option "Display Descendants" is enabled also descendents will be counted.
 
 Hide Empty Terms: Does not create menu links for terms with no nodes attached to them.
 
 Item for Vocabulary: Create a menu link for the vocabulary.  
  This will be the parent menu item.
 
 Auto Expand Menu Item: Enables the 'Expand' option when creating the menu links.  
  This is useful if using 'suckerfish' menus (pull down menus) in the primary links.
 
 Display Descendants:  Alters the URL to display all of child terms. 
 <base path>/$tid $tid $tid $tid
  When this is set, the Path Alias (module PATHAUTO) is not applied.
 
 Select to rebuild the menu on submit: Deletes all of menu items and relationships between 
  the menu and terms and recreates them from the vocabulary's terms.  
  This will create new mlid's for each item, so be careful if using other modules to extend 
  the menu functionality.

     
PATH TYPES and INTEGRATION WITH VIEWS MODULE
============================================

MENU PATH TYPE: DEFAULT
 The path will be taxonomy/term/% while Term ID will be passed as argument (multiple arguments possible).
 This path type can be used without having the VIEWS module installed.
 VIEWS provides a view named taxonomy_term (A view to emulate Drupal core's handling of taxonomy/term)
 The path of the view is 'taxonomy/term/%', the argument is 'Term ID (with depth)' and 'Depth Modifier' - 
 but only TERM ID will be passed as an argument.
 One can adjust this view to ones needs - but it might be a problem, to have only one view for all all 
 taxonomy menu links. So it is recommended to use the option MENU PATH TYPE: CUSTOM for individual 
 views per vocabulary.    

MENU PATH TYPE: CUSTOM
 With this path type, one can create individual views for each vocabulary.
 You need to have a view (page) with path 'custom path/%' and an argument 'Term ID' BEFORE you create 
 the taxonomy menu. Enable the option "Allow multiple terms per argument" while adding the argument 
 'Term ID' and choose a title like "Terms". Other options should be left by default unless really 
 needs to change sth..
 Fields and filters can be added and options can be set according to ones needs.
 Back to Taxonomy Menu:
 Enter your 'custom path' in the field "Base Path for Custom Path:" - leave out '/%'. 
 For example when your view path is 'interests/%' you enter only 'interests' here.   
 To use the 'Display Depth in Custom Path:' option, you need to have 'Taxonomy: Term ID depth modifier' 
 as second argument within your view.  

MENU PATH TYPE: HIERARCHY
 This path type is mainly beeing created for developers use.
 This should only be applied if you have custom code or a block that relies on the category/vid/tid/tid/tid.
 If you would like the url to be this path, the recomendation is to use PathAuto with 
 'category/[vocab-raw]/[copath-raw]'. Use the field "Base Path for Hierarchy Path" to see the base URL 
 that will match the veiw or page callback. The view or pagecall back MUST be created before the taxonomy menu.
 
 --- How to set up a view for MENU PATH TYPE: HIERARCHY (and only for this!)-----
 
 The vocabulary might be like:
 Vocabulary
 Term-1
 -- Term-1.1
 -- --Term-1.1.1
 -- --Term-1.1.2
 -- Term-1.2
 Term-2
 -- Term-2.1

 What is needed:
 Modules: TAXONOMY MENU with TAXONOMY MENU HIERARCHY and VIEWS

 Steps:
 * Create a view with a path: category/% (where the term "category" can be chosen)
 * Add fields and filters according your needs
 * Add the following arguments:
   - Vocabulary ID (Title: %1)
   - Term ID (Title: %2)
   - Term ID (Title: %3)
   - Term ID (Title: %4)
   - More arguments of this types might be needed, if the vocabulary has a greater depth than 3. 

 * Go to admin/content/taxonomy
   - Select the vocabulary you want to have a menu for.
   - Select "Menu:" (where the menu should show up)
   - Select "Menu Path Type: Hierarchy"
   - Enter "Base Path for Hierarchy Path: category" (or what you have chosen as path for view)
   - Optional: Display Number of Nodes / Auto Expand Menu Item
   - Check "Item for vocabulary"
   - Do NOT check "display descendants"  

 After saving the menu should appear.
 Now comes the BUT: most probably you don´t see any nodes when klicking the menu items.
 For Term-1 the path is: ..category/vid/tid, for Term-1.1.1 it is category/vid/tid/tid/tid
 Everything behind "category" will be taken as arguments in views.
 So only those nodes will be shown that are linked to the taxonomy terms Term-1 AND Term-1.1 
 AND Term1.1.1. within the vocabulary (it is a logical AND function, whereas multiple arguments 
 TermID TermID TermID is a logical OR function).
 Once you have linked your nodes to the taxonomy terms in the described way, they will be shown 
 when clicking on the menu items. It produces nice breadcrumbs and page titles (remember to set 
 the titles for the arguments in views as described) - and it always displays descendants.
 The only module that supports the saving of a whole term lineage when selecting a deep level 
 item seems to be HIERACHICAL SELECT. See chapter INTEGRATION WITH OTHER MODULES
 
INTEGRATION WITH OTHER MODULES
==============================

TAXONOMY MANGAGER
Helpful to organize taxonomy terms - Taxonomy Menu module does not interfere with it functions.
(http://drupal.org/project/taxonomy_manager)

TAXONOMY REDIRECT
Changes the taxonomy default URL to match the custom Taxonomy Menu Path can be controlled 
by Taxonomy Redirect. 
(http://drupal.org/project/taxonomy_redirect)
 
CONTENT TAXONOMY
It is a nice and very helpful module to link taxonomy terms to nodes. 
Taxonomy Menu does not interface with the content taxonomy tables, so be sure to enable the option 
"Save values additionally to the core taxonomy system (into the 'term_node' table)" 
otherwise the related taxonomy terms will not be accessable for Taxonomy Menu.
(http://drupal.org/project/content_taxonomy)
 
HIERARCHICAL SELECT with submodule HS_TAXONOMY
Supports the selection of terms in an hierarchical structured vocabulary. 
For using "MENU PATH TYPE: HIERARCHY" within Taxonomy Menu the HS options "Save term lineage" 
and "Force the user to choose a term from a deepest level" should be enabled.
(http://drupal.org/project/hierarchical_select) 
 
TAXONOMY BREADCRUMBS
Advanced breadcrumbs can be controlled by this module.
(http://drupal.org/project/taxonomy_breadcrumbs)

MENU BREADCRUMBS
Helpful to create menu breadcrumps outside the main navigation menu especially 
when using Custom or Hierarchical path. 
(http://drupal.org/project/menu_breadcrumbs)

i18n
At the momement the multiple language support seems to work only when the Taxonomy Menu option 
"item for vocabulary" is disabled. 

DOMAIN ACCESS
....

PATHAUTO
 Menu Items are Path Alias aware and compatible with PATHAUTO.
 Have a look at the various path types, which URL is passed to the code.
 Delault is taxonomy/term/$tid.
 (http://drupal.org/project/pathauto)
 
 
ADDITIONAL NOTES
================
 * Taxonomy Menu does not handle the menu call backs. It only creates the links to the menus.
   This means that everythign that is displayed on the page (including title, content, breadcrumbs, etc)
   are not controled by Taxonony Menu.
 * The router item must be created before Taxonomy Menu creates the links.  Failure to so so 
   will cause the menu items to not be created.
 * Router items can be created by either a view or another modules hook_menu.

 
PROSPECT TO PLANNED FUNCTIONS (6.x-3.0 version)
===============================================
- concept of "Menu Groups"
- any number of Menu Groups per vocabulary
- more than one vocabulary within one Menu Group
- more options to define the url path
- other options
CONTENTS OF THIS FILE
---------------------

  * Introduction
  * Examples
  * Installation
  * Known Issues/Shortcomings
  * Maintainers


INTRODUCTION
------------
Relationships or other joins in Views often create "duplicate" results. For
example, a node with a field that has multiple values may show up in the View
once per value in the multi-value field. It's frustrating, and the "DISTINCT"
option in the Views UI does not actually solve the problem because the result
row is technically distinct.

This module aims to give a simple GUI method to remove or aggregate these
"duplicate" rows. For any given field, including "Global: Text" fields, you can
optionally mark the field as filtered ("Filter Repeats") or aggregated
("Aggregate Repeats"). All rows with the same value in that field will either be
removed as duplicates (filtered), or aggregated in-line.

The "value" of the field as used for filtering or aggregation can be taken
pre-render (fastest and totally cacheable), or post-render (after any rewrite
rules or other transformations have occurred).  Post-render actions are a bit
slower (the View must be re-rendered, though the query is not re-run), but also
work with Global fields, like Global: Text w/rewrite rules.

EXAMPLES
--------
Consider a Course node with multiple Instructor fields:

    1) Course title: CHEM 101 - Introduction to Chemistry
       Instructor: Mr. Smith
    2) Course title: CHEM 101 - Introduction to Chemistry
       Instructor: Ms. Jones

when Aggregating on the Instructor field, and Filtering on the Course Title
field, the resulting view could like like:

    1) Course title: CHEM 101 - Introduction to Chemistry
       Instructor(s): Mr. Smith, Ms. Jones

Or, if there were multiple Course nodes (say, for multiple terms) the View may
by default be:

    1) Course title: CHEM 101 - Introduction to Chemistry
       Instructor: Mr. Smith
       Term: Fall 2013
    2) Course title: CHEM 101 - Introduction to Chemistry
       Instructor: Ms. Jones
       Term: Winter 2013

when Filtering on the Course Title field, the view could look like:

    1) Course title: CHEM 101 - Introduction to Chemistry

(note, you may want to remove the Term field, since it no longer applies once
we're purposely removing multiple term rows from the results)

Or, Aggregating on both Instructor and Term fields:

    1) Course title: CHEM 101 - Introduction to Chemistry
       Instructor(s): Mr. Smith, Ms. Jones
       Term(s): Fall 2013, Winter 2013


INSTALLATION
------------
Activate the Views Distinct module, then administer a desired View via Views UI.
Note: Although Views UI is not strictly a dependency of Views Distinct, Views UI
is required to initially configure Views Distinct options.

Under any field you want to affect, Edit the field and select the appropriate
Aggregate or Filter option under the "Views Distinct Settings" section of the
configuration form.

If you don't have have a good field to disambiguate "duplicate" rows, you can
add a Global: Text and rewrite it with some combination of existing fields,
like the rewrite values for a course title display:
"[class_subject] [class_number] [class_title]". Be sure to enable the
post-rendering option, or rewrites will not work!


KNOWN ISSUES/SHORTCOMINGS
-------------------------
These are on the To-Do list, but don't seem critical enough to prevent this
module from helping a lot of people. Still, they may cause odd behavior, so
it's best if folks know about them:

    1) Pager counts and the number of rows displayed are incorrect when
      filtering (removing) duplicates, and aggregation cannot aggregate fields
      from outside the scope of each page, since each page only has access to
      the rows on that page. This is a known issue without a fix for now.
      Results won't be scrambled, but fewer-than-expected results may show up on
      pagers; please test the outcome and choose if the pager is worth the
      oddness.
    2) Aggregating fields pre-render actually aggregates the base field in the
      query results, so any other display fields that in some way use those
      results will be using the aggregated versions. As far as I know there
      isn't another way to do this, because hook_views_post_execute() does not
      have access to the display fields, only the query result rows.
    3) Potential incompatibility with some style plugins: The "Use the rendered
      output of this field" option in Views Distinct may cause odd things to
      happen with some style plugins that change output when called twice (e.g.
      Views Slideshow - see #1956878: Interference with Views Slideshow). This
      is because Views Distinct needs to re-render the rows when it makes
      changes to the View output after the fields have been rendered. If you
      encounter this issue, uncheck the "Use the rendered output of this field"
      option.


MAINTAINERS
-----------
- jay.dansand (Jay Dansand)
# Facebook-Pull 7.x-3.x
Drupal Module: https://www.drupal.org/project/facebook_pull

<div class="field-item even"><p><em>Facebook Pull</em> is a fast and efficient module for displaying Facebook feeds on your site.</p>
<p>This module caches all queries to the graph, the time period default is 20 minutes.</p>
<h3>Usage</h3>
<p>Configure the module then add the block, or <a href="/project/boxes" rel="nofollow">box</a>, or use the API directly:<br></p><div class="codeblock"><pre><code>&lt;?php<br>echo facebook_pull_render($graph_id, $type, $app_id, $app_secret, $options);<br>?&gt;</code></pre></div>
<p>You must obtain an app_id and app_secret from Facebook before you can use this module. You can do this through the <a href="https://www.facebook.com/developers/createapp.php" rel="nofollow">Developer App</a> on Facebook.</p>
<p>You can configure this module at: "admin/config/services/facebook-pull"</p>

<p>More information about the facebook Graph API, the API which this module interfaces with, is available on the Facebook website:<br><a href="https://developers.facebook.com/docs/graph-api/reference/" rel="nofollow">https://developers.facebook.com/docs/graph-api/reference/</a></p>

<h3>Credits</h3>
<p>This module is currently maintained by @daveferrara1.</p>
</div>
Content Search provides a simple way for users to find site content.
Now you can quickly find content as an editor. Rather than scrolling through
pages of content, simply search by title.


HOW TO USE IT
======================
Simply enable the module and head to the Find Content screen.
You'll see the search box there, it's that easy!


AUTHOR/MAINTAINER
======================
Mike Spence (mikespence) - http://drupal.org/user/2007822
                         - http://twitter.com/mikespence
[![Build Status](https://travis-ci.org/Plug-Drupal/plug.svg?branch=7.x-1.x)](https://travis-ci.org/Plug-Drupal/plug) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/mateu-aguilo-bosch/plug/badges/quality-score.png?b=7.x-1.x)](https://scrutinizer-ci.com/g/mateu-aguilo-bosch/plug/?branch=7.x-1.x) [![Join the chat at https://gitter.im/Plug-Drupal/plug](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Plug-Drupal/plug?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
# Plug

Get the **plugin system** for Drupal 8 in your **Drupal 7 developments**.

The Plug module is a module for developers that can't wait until Drupal 8 comes out to use the plugin system that will ship with it. You can use this as an alternative to your custom CTools plugins.

## Do I need this module?
This is one of those modules that does nothing by itself, but provides tools for developers for a better developer experience. If you write custom PHP code for Drupal in a day to day basis, you can probably take advantage of this module and start writing plugins.

In Drupal 8 _everything_ is a plugin, by starting to write Drupal 8 style plugins today you accomplish two main objectives:

  - Your code is more capable to cope with change, is more maintainable and flexible.
  - You are already learning how you will program for Drupal 8 [when it comes out](http://drupalreleasedate.com/).

## Examples
Here you have a couple of examples. The best thing that you can do is read this [amazing post about plugins](https://drupalize.me/blog/201407/drupal-8-plugins-explained).

## Architecture
This module relies on some parts of the Drupal 8 code. Those parts have been encapsulated inside this module to simplify the installation process.

### Implementation examples
There is an [example module](modules/plug_example/plug_example.module) shipped with this module that will show you how to create your plugins and use them.

### Things that can be plugins.
Beep-boop-clink-clank, this section is not done just yet. Check back soon!

> Situations in which plugins are useful? Anytime you need to allow modules to provide additional "things" that implement the same interface but provide distinctly different functionality. Blocks are the classic example. In Drupal every block consists of essentially the same parts, a label, some content, and various settings related to visibility and cachability. How that label and content is generated is likely very different from one module to the next though. A custom block with static content vs. one provided by Views for example.

## Installing
Installation is straightforward. You only need to download and enable the module.

## Implementations
The following modules use the <strong>Plug</strong> module to declare their plugins. If you want your module to be in this list, [open an issue](https://github.com/mateu-aguilo-bosch/plug/issues/new).

  - [Plug Field](https://github.com/Plug-Drupal/plug_field)
  - [Plug Config](https://github.com/Plug-Drupal/plug_config)
Yaml Component
==============

YAML implements most of the YAML 1.2 specification.

```php
use Symfony\Component\Yaml\Yaml;

$array = Yaml::parse(file_get_contents(filename));

print Yaml::dump($array);
```

Resources
---------

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/Yaml/
    $ composer install
    $ phpunit
Translation Component
=====================

Translation provides tools for loading translation files and generating
translated strings from these including support for pluralization.

```php
use Symfony\Component\Translation\Translator;
use Symfony\Component\Translation\MessageSelector;
use Symfony\Component\Translation\Loader\ArrayLoader;

$translator = new Translator('fr_FR', new MessageSelector());
$translator->setFallbackLocales(array('fr'));
$translator->addLoader('array', new ArrayLoader());
$translator->addResource('array', array(
    'Hello World!' => 'Bonjour',
), 'fr');

echo $translator->trans('Hello World!')."\n";
```

Resources
---------

Silex integration:

https://github.com/fabpot/Silex/blob/master/src/Silex/Provider/TranslationServiceProvider.php

Documentation:

https://symfony.com/doc/2.8/book/translation.html

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/Translation/
    $ composer install
    $ phpunit
Validator Component
===================

This component is based on the JSR-303 Bean Validation specification and
enables specifying validation rules for classes using XML, YAML, PHP or
annotations, which can then be checked against instances of these classes.

Usage
-----

The component provides "validation constraints", which are simple objects
containing the rules for the validation. Let's validate a simple string
as an example:

```php
use Symfony\Component\Validator\Validation;
use Symfony\Component\Validator\Constraints\Length;

$validator = Validation::createValidator();

$violations = $validator->validateValue('Bernhard', new Length(array('min' => 10)));
```

This validation will fail because the given string is shorter than ten
characters. The precise errors, here called "constraint violations",  are
returned by the validator. You can analyze these or return them to the user.
If the violation list is empty, validation succeeded.

Validation of arrays is possible using the `Collection` constraint:

```php
use Symfony\Component\Validator\Validation;
use Symfony\Component\Validator\Constraints as Assert;

$validator = Validation::createValidator();

$constraint = new Assert\Collection(array(
    'name' => new Assert\Collection(array(
        'first_name' => new Assert\Length(array('min' => 101)),
        'last_name' => new Assert\Length(array('min' => 1)),
    )),
    'email' => new Assert\Email(),
    'simple' => new Assert\Length(array('min' => 102)),
    'gender' => new Assert\Choice(array(3, 4)),
    'file' => new Assert\File(),
    'password' => new Assert\Length(array('min' => 60)),
));

$violations = $validator->validateValue($input, $constraint);
```

Again, the validator returns the list of violations.

Validation of objects is possible using "constraint mapping". With such
a mapping you can put constraints onto properties and objects of classes.
Whenever an object of this class is validated, its properties and
method results are matched against the constraints.

```php
use Symfony\Component\Validator\Validation;
use Symfony\Component\Validator\Constraints as Assert;

class User
{
    /**
     * @Assert\Length(min = 3)
     * @Assert\NotBlank
     */
    private $name;

    /**
     * @Assert\Email
     * @Assert\NotBlank
     */
    private $email;

    public function __construct($name, $email)
    {
        $this->name = $name;
        $this->email = $email;
    }

    /**
     * @Assert\IsTrue(message = "The user should have a Google Mail account")
     */
    public function isGmailUser()
    {
        return false !== strpos($this->email, '@gmail.com');
    }
}

$validator = Validation::createValidatorBuilder()
    ->enableAnnotationMapping()
    ->getValidator();

$user = new User('John Doe', 'john@example.com');

$violations = $validator->validate($user);
```

This example uses the annotation support of Doctrine Common to
map constraints to properties and methods. You can also map constraints
using XML, YAML or plain PHP, if you dislike annotations or don't want
to include Doctrine. Check the documentation for more information about
these drivers.

Resources
---------

Silex integration:

https://github.com/fabpot/Silex/blob/master/src/Silex/Provider/ValidatorServiceProvider.php

Documentation:

https://symfony.com/doc/2.6/book/validation.html

JSR-303 Specification:

http://jcp.org/en/jsr/detail?id=303

You can run the unit tests with the following command:

    $ cd path/to/Symfony/Component/Validator/
    $ composer install
    $ phpunit
# Doctrine Inflector

Doctrine Inflector is a small library that can perform string manipulations
with regard to upper-/lowercase and singular/plural forms of words.

[![Build Status](https://travis-ci.org/doctrine/inflector.svg?branch=master)](https://travis-ci.org/doctrine/inflector)
# Doctrine Annotations

[![Build Status](https://travis-ci.org/doctrine/annotations.png?branch=master)](https://travis-ci.org/doctrine/annotations)

Docblock Annotations Parser library (extracted from [Doctrine Common](https://github.com/doctrine/common)).

## Changelog

### v1.2.0

 * HHVM support
 * Allowing dangling comma in annotations
 * Excluded annotations are no longer autoloaded
 * Importing namespaces also in traits
 * Added support for `::class` 5.5-style constant, works also in 5.3 and 5.4

### v1.1

 * Add Exception when ZendOptimizer+ or Opcache is configured to drop comments
# Doctrine Lexer

Base library for a lexer that can be used in Top-Down, Recursive Descent Parsers.

This lexer is used in Doctrine Annotations and in Doctrine ORM (DQL).
# Doctrine Cache

Master: [![Build Status](https://secure.travis-ci.org/doctrine/cache.png?branch=master)](http://travis-ci.org/doctrine/cache) [![Coverage Status](https://coveralls.io/repos/doctrine/cache/badge.png?branch=master)](https://coveralls.io/r/doctrine/cache?branch=master)

[![Latest Stable Version](https://poser.pugx.org/doctrine/cache/v/stable.png)](https://packagist.org/packages/doctrine/cache) [![Total Downloads](https://poser.pugx.org/doctrine/cache/downloads.png)](https://packagist.org/packages/doctrine/cache)

Cache component extracted from the Doctrine Common project.

## Changelog

### v1.2

* Added support for MongoDB as Cache Provider
* Fix namespace version reset
# Doctrine Collections

[![Build Status](https://travis-ci.org/doctrine/collections.svg?branch=master)](https://travis-ci.org/doctrine/collections)

Collections Abstraction library

## Changelog

### v1.3.0

* [Explicit casting of first and max results in criteria API](https://github.com/doctrine/collections/pull/26)
* [Keep keys when using `ArrayCollection#matching()` with sorting](https://github.com/doctrine/collections/pull/49)
* [Made `AbstractLazyCollection#$initialized` protected for extensibility](https://github.com/doctrine/collections/pull/52)

### v1.2.0

* Add a new ``AbstractLazyCollection``

### v1.1.0

* Deprecated ``Comparison::IS``, because it's only there for SQL semantics.
  These are fixed in the ORM instead.
* Add ``Comparison::CONTAINS`` to perform partial string matches:

        $criteria->andWhere($criteria->expr()->contains('property', 'Foo'));
# Doctrine Common

[![Build Status](https://secure.travis-ci.org/doctrine/common.png)](http://travis-ci.org/doctrine/common)

The Doctrine Common project is a library that provides extensions to core PHP functionality.

## More resources:

* [Website](http://www.doctrine-project.org)
* [Documentation](http://docs.doctrine-project.org/projects/doctrine-common/en/latest/)
* [Issue Tracker](http://www.doctrine-project.org/jira/browse/DCOM)
* [Downloads](http://github.com/doctrine/common/downloads)
# Running the Doctrine 2 Testsuite

## Running tests

Execute PHPUnit in the root folder of your doctrine-common clone.

    phpunit

## Testing Lock-Support

The Lock support in Doctrine 2 is tested using Gearman, which allows to run concurrent tasks in parallel.
Install Gearman with PHP as follows:

1. Go to http://www.gearman.org and download the latest Gearman Server
2. Compile it and then call ldconfig
3. Start it up "gearmand -vvvv"
4. Install pecl/gearman by calling "gearman-beta"

You can then go into tests/ and start up two workers:

    php Doctrine/Tests/ORM/Functional/Locking/LockAgentWorker.php

Then run the locking test-suite:

    phpunit --configuration <myconfig.xml> Doctrine/Tests/ORM/Functional/Locking/GearmanLockTest.php

This can run considerable time, because it is using sleep() to test for the timing ranges of locks.This module creates an input filter for Drupal that automatically transforms 
links to tweets such as 
https://twitter.com/lightsky_design/status/378242911420575744 into an Embedded 
Tweet.

Configuration

In order to configure this module, follow these steps:

Enable the Module
Go to Configuration -> Text Formats
Click Edit next to the text format you wish to enable embedded tweets for
Under "Enabled Filters" select "Twitter Embed Filter"
Change the order of the filter so that "Twitter Embed Filter" appears above 
"Convert URLs Into Links"
Embedding Tweets

Tweet Embed utilizes a BBCode style tag in order to embed tweets into your 
content. The default format is (on one line):

[tweet_embed]
https://twitter.com/lightsky_design/status/378242911420575744
[/tweet_embed]

You may also apply a variety of options to your tweets. A list of options that 
can be passed can be found here. 

Only the following options are currently supported.

maxwidth
hide_media
hide_thread
align
lang

In order to pass in the options add the option and the value within the 
"[tweet_embed]" block.  For example, to display a tweet in french, and align it 
in the center of the page, insert the following snippet into your content block 
(Note: This should be all on one line):

[tweet_embed lang="fr" align="center"]
https://twitter.com/lightsky_design/status/378242911420575744[/tweet_embed]

Getting Tweet Embed URL

In order to get the tweet URL, perform the following steps:

When viewing the tweet you wish to embed, click "Expand"
At the bottom of the tweet, click "Details" next to the timestamp.
Copy the URL in the address bar
Sponsorship

Development of this module is sponsored by LightSky (http://www.lightsky.com).
Reference options limit module
==============================

This module allows reference fields of several types to have their available
options limited by the values of other fields in the current entity.

Requirements
------------

- Drupal core 7.8 or higher, due to our use of hook_field_widget_form_alter().

Example
-------

Suppose you want news stories to be marked as being about a sport and a
particular team for that sport, perhaps using taxonomy terms for both.

To make editing easier, you would probably like want the 'team' dropdown to
be limited to just teams for the current news story's sport.

To achieve this with this module, add the 'sport' field to both news story 
nodes and team taxonomy terms. Hence the team 'Chudley Cannons' would have
as its team taxonomy term 'Quidditch'.

(This probably entails taxonomy term reference fields on terms
themselves... which was bound to happen with FieldAPI sooner or later.)

Thus, when editing a news story node, selecting 'Quidditch' as the sport
will cause the team reference field to update to show only teams which
also have Quidditch' as their* sport.

Setup
-----

Suppose:
- the option limited field (i.e. the field you want to limit) is on
  entity type A.
- this field points to (i.e., refers to) entities of type B.

1. Add your entity reference field on entity type A as normal. This will be the
  option limited field.
2. Add a field to entity type A whose values will be used to limit the option
  limited field.
3. Add the *same field* to entity type B.
4. Return to the option limited field settings and select field B as your
  matching field.

Terminology
-----------

- option limited field: a field whose type is some sort of reference, whose
   reference options we limit with this module.
- matching field: a field whose values we use to limit the options in an
   option limited field. We do this by requiring that the field be applied
   to both:
   - the entity bundle that bears the option limited field itself
   - the entity bundle(s) that the option limited field may refer to

-- SUMMARY --

The Better Exposed Filters module replaces the Views' default single-
or multi-select boxes with radio buttons or checkboxes, respectively.

Views Filters are a powerful tool to limit the results of a given view.
When you expose a filter, you allow the user to interact with the view
making it easy to build a customized advanced search.  For example,
exposing a taxonomy filter lets your site visitor search for articles
with specific tags.  Better Exposed Filters gives you greater control
over the rendering of exposed filters.

For a full description of the module, visit the project page:
  https://drupal.org/project/better_exposed_filters

To submit bug reports and feature suggestions, or to track changes:
  https://drupal.org/project/issues/better_exposed_filters

For more information on Views filters, see the Advanced Help documentation
that comes with Views or visit the online version:
  https://api.drupal.org/api/views/7


-- REQUIREMENTS --

This module requires the Views module:
  https://drupal.org/project/views


-- DOCUMENTATION --

See:
  https://drupal.org/node/766974


-- CONTACT --

The maintainer for this project is Mike Keran, known on drupal.org as mikeker
(https://drupal.org/user/192273). He can be contacted for work on this module or
other custom projects.
Views Dependent Filters
=======================

This module allows the presence of exposed filters on a view to be controlled by values in another exposed filter.

Dependent filters are hidden when not relevant, and their values are not considered when the exposed form is submitted.

The module is compatible with both the Views basic and the Better Exposed Filters form plugins.

Example
-------

Suppose you had a view showing several kinds of products, such as cake, bicycles, and books, and an exposed filter on product type that lets the user refine the listing to one or more types.

With this module you could add the following filters:
  - cake flavour, such as lemon, chocolate, coffee
  - bicycle size
  - book genre
and each filter will only show when the type it relates to is selected in the filter for product type.

The user experience is thus:

1. Load the page.
2. Select 'cake'. The cake flavour filter now appears in the exposed filter area.
3. Select 'chocolate'.
4. Submit the form to apply the filters.
5. In the refined view result, the user can unselect 'cake' and the cake flavour filter will disappear. Submitting the form at this point will take them back to the original, unfiltered view. Alternatively, selecting another type of product will let them select bicycle size or book genre accordingly.

Note that selecting *both* 'cake' and 'bicycle' will cause both the dependent filters to show, but due to the nature of Views queries, selecting values in both will not show any results! (Unless you stock a chocolate-flavoured bicycle with a 19" frame.)

Usage
----

1. Add a filter of type 'Global: Dependent filter' to your view. It should be positioned after the controlling filter and before the dependent filter(s).
2. In the first settings form, choose the controller filter. Only filters prior to this one in the filter order are available.
3. In the second settings form, choose the values on the controller filter that allow the dependent filters, and choose which filters are dependent.

Note that you can have multiple instances of the Dependent filter handler; indeed the above example would require one for each product type.
-------------------------------------------------------------------------------
Node Hierarchy 2 for Drupal 6.x
  by Ronan Dowling, Gorton Studios - ronan (at) gortonstudios (dot) com
-------------------------------------------------------------------------------

Node Hierarchy is a module which allows nodes to be children of other nodes
creating a tree-like hierarchy of content.

The module offers:
  * Automatic hierarchical urls using pathauto
    (eg: http://example.com/aboutus/history/beginning).
  * Automatic creation of hierarchical menus if desired.
  * Optional Views integration.
  * Optional Node Access integration (REMOVED UNTILL NODE ACCESS IS UPDATED)

-------------------------------------------------------------------------------
Installation
------------
Go to administer -> site building -> modules and enable the Node Hierarchy
module.

You must then tell the module which node types can be parents and which can be
children. To do this you can either:
1) Go to administer -> content administration -> content types. Click edit on
the types you want modify and check the "Can be parent" and "Can be child"
checkboxes
-- OR --
2) Go to administer -> settings -> Node Hierarchy and check the boxes in the for
the desired types.

You can also pick a default node for each given type. For example, you can
create a page called "Blogs" and have nodes of type "blog" be a child of that
page by default.

You will also need to assign the following permissions to the appropriate users:

1) create child nodes
   For users who are allowed to create children under existing nodes.
2) edit all node parents
   For users who are allowed to change the parent of any node, regardless of
   authorship.
3) edit own node parents
   For users who are allowed to change the parent of nodes which they have
   authored.
4) reorder children
   For users who are allowed to change the order of children on any node.
5) view site outline
   For users who are allowed to view the site outline
6) administer hierarchy
   For users who are allowed to edit the node hierarchy defaults.


-------------------------------------------------------------------------------
Using Node Hierarchy
--------------------
To assign a parent to a node, either:
1) Create a new node of a type that whose "Can be child" setting is true or edit
   an existing node. Expand the Node Hierarchy fieldset and chose a parent from
   the pulldown.
-- OR --
2) Navigate to the node you wish to make a parent. Click on the children tab,
   and click on one of the create links at the bottom of the tab.

To create a menu for a node:
Edit the node, expand the Node Hierarchy fieldset and check the "Create Menu"
box. Click Submit.
If the node's parent has a menu item, a new menu will be created for the node
under it's parent's menu item. The name of the menu item will be the title of
the node and it's weight will be the node's sort order.

If you edit the parent of a node or it's title, you can recreate an existing
menu item by checking "Recreate Menu". This will set the menu item's parent to
the new parent and the title to the new title. This is not done automatically
on edit, so that you can maintain menu hierarchy separately from node hierarchy
if desired.

If the node does not have a parent or it's parent does not have a menu item, the
new menu item will be a child of the default menu item set in the Node
Hierarchty settings.

Reordering Child Nodes:
Use the green arrow links on the Children tab of the parent node to rearrange
child nodes. This will also update the order of any generated menu items as long
as they have not been moved from their original location.

Token and Pathauto
----------------------
Node Hierarchy integrates with token (and therefore Pathauto 2.x and others).

For Pathauto, the recommended pattern to use is 
  [node:nodehierarchy:parent:url:alias]/[node:title] 
This will give you a hierarchical path which respects automatic and custom paths
for each ancestor up to the top level. 

For example a node with the hierarchical path:
  About us > History > Early Years > 1940s
will have the url:
  about-us/history/early-years/1940s

And if you change the About Us node's path to 'about' the descendant's path will
be 
  about/history/early-years/1940s
All descendant's url paths will need to be regenerated in order to reflect this 
change.

Views
-----
Node hierarchy integrates with Views providing the following:

Arguments:
  Parent Node Id - Takes a node id and returns only nodes which are children of
  that node. Used to provide lists of children for a give node.

Fields:
  Child Weight - The numerical sort order of a child node.

Sort Fields:
  Child Weight - Use this to sort child nodes by their Node Hierarchy sort order.

To enable views integration, turn on the Node Hierarchy Views module. With this
module turned on, you will also be able to embed a view of a node's children on
that node's page.

-------------------------------------------------------------------------------
Node Access
-----------
Node Access integration has been removed from Version 6, as the nodeaccess
module has not been updated to 6 at the time of this writing.

-------------------------------------------------------------------------------
Known Issues
------------
* Settings can break with long content type names.
* Does not respect revisions. Hierarchy settings are revision independant.
* Not tested with pgsql install

-------------------------------------------------------------------------------
TODO
----
* Improve "Can be child" setting to allow admins to specify which node types
  can be children of which node types. (e.g. 'chapter' nodes can only be
  children of 'book' nodes)
-------------------
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

Current Maintainer: Sami Radi a.k.a VirtuoWorks <http://drupal.org/user/656630>

Remove Duplicates removes duplicate nodes
according to any selected content field.

This can be very useful with Drupal feeds module :
- http://drupal.org/project/feeds

This module was inspired by these threads : 
- http://drupal.org/node/720190 : Remove Duplicate Nodes based on title
- http://drupal.org/node/1211922 : remove duplicated node base on title problem

THANKS
------

Thanks to dman <https://drupal.org/user/33240> for endorsing this project.

He wrote a sandbox module "Deduplicate Nodes" for D6 intended to deduplicate
nodes according to titles only : https://drupal.org/sandbox/dman/1422586

INSTALLING
----------

See http://drupal.org/getting-started/install-contrib
for instructions on how to install or update Drupal modules.

Once Remove Duplicates is installed and enabled,
you can use it at admin/config/content/remove_duplicates.

It is highly recommended that you backup your database before using this module.

UNINSTALLING
------------

Because Drupal does not uninstall modules in reverse 
order of their dependencies, if you want to uninstall
all the Remove Duplicates modules, be sure to disable 
and uninstall all the sub-modules before the base Remove 
Duplicates module.

To help fix this bug in Drupal core, visit http://drupal.org/node/151452.


FREQUENTLY ASKED QUESTIONS (FAQ)
--------------------------------

- There are no frequently asked questions at this time.


KNOWN ISSUES
------------

- See http://drupal.org/project/issues/2005296 
for a list of the current known issues.


MORE INFORMATION
----------------

- To issue any bug reports, feature or support requests
see the module issue queue at 
http://drupal.org/project/issues/2005296

- For additional documentation, see the online module handbook at
https://drupal.org/project/remove_duplicates


HOW CAN YOU CONTRIBUTE?
-----------------------

- Report any bugs, feature requests, etc. in the issue tracker.
http://drupal.org/node/add/project-issue/2005296

- Help translate this module.

- Write a review for this module at drupalmodules.com.
http://drupalmodules.com/

- Help keep development active by donating to the developers.
http://www.virtuoworks.com/
FEED IMPORT

Project page: https://drupal.org/project/feed_import

This module only provides an UI for Feed Import Base module.
Checkout the examples of how to use this UI https://drupal.org/node/2190315

Hooks
-----------

For examples, check feed_import.module file.

To register new settings:

function hook_feed_import_setting_types() {
  return array(
    'setting-name' => array(
      'hook' => 'hook_to_invoke',
      'base' => 'BaseClass',
    );
  );
}

To register a reader:

function hook_feed_import_reader_info() {
  return array(
    'my_reader' => array(
      // Reader name
      'name' => t('Reader name'),
      // Reader description
      'description' => t('Description'),
      // If you want to extend other reader and use its options you can specify
      // here the name of parent reader. You can reorder options using #wight,
      // you can remove options by setting it to false, you can change it by
      // adding properties to options or you can add new options.
      'inherit_options' => 'processor name or FALSE if no options are inherited',
      // The class that handles this reader (extending FeedImportReader)
      'class' => 'ReaderNameClass',
      // Options are form elements which must have a default value
      'options' => array(
        'option1' => array(
          '#type' => 'textfield',
          '#title' => t('Option1'),
          '#description' => t('Description 1'),
          '#default_value' => '1',
          '#required' => TRUE,
          '#maxlength' => 1024,
          // validate option by using #element_validate
          '#element_validate' => array('my_element_validate_function'),
        ),
        'optionx' => array(
          '#type' => 'textarea',
          '#title' => t('Option X)'),
          '#description' => t('Description of X'),
          '#default_value' => '',
        ),
        // Other options
      )
    ),
  );
}

To register a new processor:

function hook_feed_import_processor_info() {
  // similar to hook_feed_import_reader_info().
}

To register a new hash manager:

function hook_feed_import_hash_manager_info() {
  // similar to hook_feed_import_reader_info().
}

To register a new filter handler:

function hook_feed_import_filter_info() {
  // similar to hook_feed_import_reader_info().
}
FEED IMPORT BASE

Project page: https://drupal.org/project/feed_import
Developers info: https://drupal.org/node/2190383

------------------------------
About Feed Import Base
------------------------------

This module provides basic import functionality and abstractization supporting
all entity types.

The reader (source)
----------
Reader's job is to fetch content from a resource and map it to values by paths.
By default there are 6 provided readers:
  -XML files - XPATH mapped
  -XML Chunked for huge xml files - XPATH mapped
  -DomDocument XML/HTML - XPATH mapped
  -CSV fiels - Column name or index mapped
  -JSON files - Path to value mapped
  -SQL databases - Column name mapped


The Hash Manager
----------------
Used to monitor imported items for update/delete.
This module provides only an SQL based Hash Manager.


The filter
----------
Used to filter values. This module provides a powerful filter class.


The processor
-------------
The processor takes care of all import process.
This module provides just one processor compatibile with all readers.


Hooks
-------------
There are two hooks you could implement:

hook_feed_import_error($error_type, $feed, $report)

$error_type - an integer indicationg error type.
Can be one of the following constant from FeedImport class:
FEED_OVERLAP_ERR - overlap error
FEED_ITEMS_ERR   - few items error
FEED_SOURCE_ERR  - source error
FEED_CONFIG_ERR  - configuration error

$feed - feed configuration
$report - report info

hook_feed_import_success($feed, $report)
$feed - feed configuration
$report - report info

These hooks will not be called if variable feed_import_invoke_hooks
is set to false.
Place here your php files containig custom filters.
Drupal for Facebook
-------------------

Project Home:
http://www.drupalforfacebook.org, http://drupal.org/project/fb

Primary author and maintainer: Dave Cohen (http://www.dave-cohen.com/contact)
Do  NOT contact  the  maintainer  with a question  that  can be  easily
answered with a web search.  You may not receive a reply.

Branch: 7.x-3.x (version 3.x for Drupal 7.x)

This file is more current than online documentation.  When in doubt,
trust this file.  Online documentation: http://drupal.org/node/195035,
has more detail and you should read it next..

To upgrade from Drupal 6 to Drupal 7:
- Upgrade your D6 version to 3.3 or later.  Run update.php and make sure everything seems to work.  Then upgrade drupal and all modules to D7 branch.


To upgrade from D7 version to the next:
- Read the upgrade instructions: http://drupal.org/node/936958

To install:

- Make sure you have a PHP client from facebook (version >= 3.1.1).
  The 2.x.y versions are not supported by this version of Drupal for Facebook.
  Download from https://github.com/facebook/facebook-php-sdk.
  Extract the files, and place them in sites/all/libraries/facebook-php-sdk.

  If you have the Libraries API module installed, you may place the files in
  another recognised location (such as sites/all/libraries), providing that the
  directory is named 'facebook-php-sdk'.

  Or, to manually set the location of the php-sdk in any other
  directory, edit your settings.php to include a line similar to the
  one below. Add to the section where the $conf variable is defined,
  or the very end of settings.php. And customize the path as needed.

  $conf['fb_api_file'] = 'sites/all/libraries/facebook-php-sdk/src/facebook.php';

  See also http://drupal.org/node/923804

- Your theme needs the following attribute at the end of the <html> tag:

  xmlns:fb="http://www.facebook.com/2008/fbml"

  Drupal 7 should include this by default.  Use your browser's view source feature to confirm.
  If not, you may need to edit your theme's html.tpl.php file.  See
  http://www.drupalforfacebook.org/node/1106.  Note this applies to
  themes used for Facebook Connect, iframe Canvas Pages, and Social
  Plugins (i.e. like buttons).  Without this attribute, IE will fail.

  Note that some documention on facebook.com suggests
  xmlns:fb="http://ogp.me/ns/fb#" instead of the URL above.  Try that
  if the above is not working for you.


- To support canvas pages and/or page tabs, url rewriting and other
  settings must be initialized before modules are loaded, so you must
  add this code to your settings.php.  This is done by adding these
  two lines to the end of sites/default/settings.php (or
  sites/YOUR_DOMAIN/settings.php).

  include "sites/all/modules/fb/fb_url_rewrite.inc";
  include "sites/all/modules/fb/fb_settings.inc";

  (Change include paths if modules/fb is not in sites/all.)

- For canvas pages, add something like this to your settings.php:

  if (!headers_sent()) {
    header('P3P: CP="We do not have a P3P policy."');
  }

  See http://drupal.org/node/933994 and search for "P3P" for details.

- Go to Administer >> Site Building >> Modules and enable the Facebook
  modules that you need.

  Enable fb.module for Social Plugins.

  Enable fb_devel.module and keep it enabled until you have everything
  set up. You should disable this on your live server once you are
  certain facebook features are working. (Note this requires
  http://drupal.org/project/devel, which is well worth installing
  anyway.)

  Enable fb_app.module and fb_user.module if you plan to create
  facebook applications.

  Enable fb_connect.module for Facebook Connect and/or
  fb_canvas.module for Canvas Page apps.

  Create a new Text Format that does not restrict/clean HTML tags and use it
  in blocks and nodes. Other Text Formats (formerly called Input Formats in D6)
  like the built-in Full HTML Text Format actually mangle FB tags like <fb:like>.

  Pages at http://drupal.org/node/932690 will help you decide which
  other modules you need to enable for your particular needs.


To support Facebook Connect, Canvas Pages, and/or Social Plugins that
require an Application, read on...

- You must enable clean URLs. If you don't, some links that drupal
  creates will not work properly on canvas pages.

- Create an application on Facebook, currently at
  https://developers.facebook.com/apps (click "create new app").  Fill
  in the minimum required to get an apikey and secret.  If supporting
  canvas pages, specify a canvas name, too.  You may ignore other
  settings for now.

- Go to Administer >> Site Building >> Facebook Applications and click
  the Add Applicaiton tab.  Use the app id, apikey and secret that
  Facebook has shown you.  Hopefully other settings will be
  self-explanitory.  When you submit your changes, Drupal for Facebook
  will automatically set the callback URL and some other properties
  which help it work properly.


Troubleshooting:
---------------

Reread this file and follow instructions carefully.

Read http://drupal.org/node/933994, and all the module documentation
on http://drupal.org/node/912614.

Enable the fb_devel.module and add the block it provides (called
"Facebook Devel Page info") to the footer of your Facebook theme.
fb_devel.module will catch some errors and write useful information to
Drupal's log and status page.

Use your browser's view source feature, and search page source for any
<script> tag which includes facebook's javascript,
"http://connect.facebook.net/en_US/all.js".  fb.js will include this
for you.  Including it too soon will break many features.  So remove
it from any block, node, template or whatever that adds it to the
page.  Similarly, do not include any <div id="fb-root">.

Disable Global Redirect, if you have that module installed.  Users
have reported problems with it and Drupal for Facebook.  Any module
which implements custom url rewrites could interfere with canvas page
and profile tab support.

On the facebook side, make sure your application is not in "sandbox
mode".  This is known to have unwanted side effects.  Also, don't use
a test account. If you've used a test account, ever, even for another
application, clear all your browser's cookies.  Try to reproduce the
problem not in sandbox mode, and not using a test account.

Bug reports and feature requests may be submitted.
Here's an idea: check the issue queue before you submit
http://drupal.org/project/issues/fb

If you do submit an issue, start the description with "I read the
README.txt from start to finish," and you will get a faster, more
thoughtful response. Seriously, prove that you read this far.

Below are more options for your settings.php. Add the PHP shown below
to the very end of your settings.php, and modify the paths accordingly
(i.e. where this example has "sites/all/modules/fb", you might need
"profiles/custom/modules/fb").




//// Code to add to settings.php:
/////////////////////////////////

/**
 * Drupal for Facebook settings.
 */

if (!is_array($conf))
  $conf = array();

$conf['fb_verbose'] = TRUE; // debug output
//$conf['fb_verbose'] = 'extreme'; // for verbosity fetishists.

// More efficient connect session discovery.
// Required if supporting one connect app and different canvas apps.
//$conf['fb_id'] = '123.....XYZ'; // Your connect app's ID goes here.

// Enable URL rewriting (for canvas page apps).
include "sites/all/modules/fb/fb_url_rewrite.inc";
include "sites/all/modules/fb/fb_settings.inc";

// Header so that IE will accept cookies on canvas pages.
if (!headers_sent()) {
  header('P3P: CP="We do not have a P3P policy."');
}

// end of settings.php
modules/fb/contrib/README.txt

(Read modules/fb/README.txt for important information.)

In this directory you'll find modules that are either:

* experimental
* under development
* useful only with certain third-party modules

These are not part of the "officially supported" Drupal for Facebook.
If problems arise, we'll help if we can.  But hopefully you can
provide your own patches to the issue queue:
http://drupal.org/project/issues/fb

Do you feel one of these modules should be "promoted" to the
modules/fb/ directory?  Do you have a module you'd like to contribute
to this directory?  Please let us know by submitting an issue:
http://drupal.org/project/issues/fb
A simple empty page solution. Assists in creating empty menu callbacks, mostly used for pages that only consist of blocks.

Authors:
  Nick Robillard <http://drupal.org/user/176017>

Sponsors:
  80 Elements <http://80elements.com>


Requirements
------------

1. Menu - Drupal core optional


Installation
------------

1. Place this module directory in your modules folder (usually sites/all/modules/).

2. Go to "Administer" > "Modules" and enable the module.

3. Manage callbacks at "Structure" > "Empty Page callbacks" <admin/structure/empty-page>


Example: Create an empty front page
-------------------------------

1. Create an Empty Page callback. <admin/structure/empty-page/add>

2. Enter "node" in the Internal Path field (if that is what you have under Default Front Page on the Site Information page). <admin/config/system/site-information>

3. Add a Page Title (optional) and Save.


The standard list of the latest 10 nodes promoted to the front page is now gone.drupal for firebug 
----------------------
matt cheney (populist)
matt@chapterthree.com
----------------------

-- to use this module you must also download and install the drupal for firebug firefox extension. the extension is now public and available at https://addons.mozilla.org/en-US/firefox/addon/8370.

-- to see this module in action (after installing the firefox extension), check out the demonstration test site at http://drupalforfirebug.chapterthree.com/tests.

-- this module requires more memory than normal. a good rule of thumb is to set the memory at 96M. information on how to increase the memory is here: http://drupal.org/node/29268

more information about the module available at:
http://drupalforfirebug.chapterthree.com
http://www.drupal.org/project/drupalforfirebug
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

/* DESCRIPTION */

Views Accordion provides a display style plugin for the Views module.
It will take the results and display them as a jQuery UI accordion. It supports
grouping of fields and ajax pagination.


/* INSTALATION */

1. Place the views_accordion module in your modules directory (usually under
   /sites/all/modules/).
2. Go to /admin/modules, and activate the module (you will find it under the
   Views section).


/* USING VIEWS ACCORDION MODULE */

Your view must meet the following requirements:
  * Row style must be set to Fields
  * Provide at least two fields to show.

Choose Views Accordion in the Style dialog within your view, which will prompt
you to configure the accodion.

*        IMPORTANT       *
The first field WILL be used as the header for each accordion section, all
others will be displayed when the header is clicked. The module creates an
accordion section per row of results from the view. If the first field includes
a link, this link will not function, (the js returns false) Nothing will break
though.
**************************


/* THEMING INFORMATION */

Files included:
  * views-acordion.css - Just some styles to fix default styling problems in
    bartik.
  * views-view-accordion.tpl.php - copy/paste into your theme directory -
    please the comments in this file for requirements/instructions.

Both files are commented to explain how things work. Do read them to speed
things up.


/* ABOUT THE AUTHOR */

Views Accordion was created by Manuel Garcia
http://drupal.org/user/213194
Views Datasource README
-------------------------------------------------------------------------------

About
-----
Views Datasource is a set of plugins for Views for rendering node content in a
set of shareable, reusable data formats based on XML, JSON, and XHTML. These
formats allow content in a Drupal site to be easily used as data sources for
Semantic Web clients and web mash-ups. Views Datasource plugins output content
from node lists created in Drupal Views as:
  1)XML data documents using schemas like OPML and Atom;
  2)RDF/XML data documents using vocabularies like FOAF, SIOC and DOAP;
  3)JSON data documents in plain JSON or in a format like MIT Simile/Exhibit;
  4)XHTML data documents using microformat like hCard and hCalendar

The project consists of 4 Views style plugins:
  1)views_xml - Output as raw XML, OPML, and Atom;
  2)views_json - Output as simple JSON, Simile/Exhibit JSON and JqGrid;
  3)views_rdf - Output as FOAF, SIOC and DOAP;
  4)views_xhtml - Output as hCard and hCalendar.

In Drupal 7.x, to use these plugins you should:
1) Enable the module containing the format you want to render your views as.
2) In the Views UI set the view style (in Basic Settings) to one of:
   i)  JSON data document (render as Simple JSON or Simile/Exhibit JSON)
   ii) XML data document (render as raw XML, OPML, or Atom)
   iii) RDF data document (render as a FOAF or SIOC or DOAP RDF/XML document)
   iv) XHTML data document (render as hCard or hCalendar XHTML)
3) In the view style options choose the options or vocabulary for your format
   (like raw or the OPML or Atom vocabulary for XML rendering.)
4) Add the fields to your view that contain the information you want to be
   pulled into the format renderer. All formats will output the fields
   recognized as belonging to that format, and certain formats like Atom and
   SIOC require certain fields to be present (see below.)
   The SIOC format requires the fields: node nid, type, title, body, posted date
5) That's it! The rendered view will be visible in the preview and at your
   view's page displaypath. When you create a page display for your view with a unique URL,
   no Drupal markup is emitted from this page, just the data for the particular
   content type with the proper Content-Type HTTP header (like text/xml or
   application/rdf+xml.)

A JSON data document will render the nodes generated by a view as a
serialization of an array of Javascript objects with each object's properties
corresponding to a view field. Simple JSON is just plain-vanilla JSON
serialization usable in most apps while Simile/Exhibit JSON is the serialization
format used by the Exhibit web app - http://simile.mit.edu/exhibit/

An XML data document with render the nodes generated by a view as XML. The raw
XML format creates a root element called 'nodes' and then a 'node' child element
for each node in the view, with each node's child elements corresponding to a
view field. OPML is a very simple XML schema useful for generating simple lists
(like lists of tracks in an music playlist.) Atom is a syndication schema with
similar intents as RSS. The following fields will bviews_rdf will render
the nodes generated by a view as an RDF/XML FOAF document with each
<foaf:Person> element corresponding to a node in the view. To use just have
fields in the view named as their equivalent FOAF properties - for example to
have a <foaf:name> or <foaf:nick> element, have a field named 'name' and 'nick'
in your view. Similarly views_xhtml provides the hCard plugin which will render
each node in the XHTML hCard format - just have fields corresponding to hCard
properties defined in the view. For example to create an <email> element inside
the <div class="hcard"> root element, just have one or more fields in the view
containing the text 'email'.

The FOAF and hCard renderers are most useful with view based on user profiles
where you can create profile fields corresponding to properties defined in the
FOAF (http://xmlns.com/foaf/spec/) or hCard
(http://microformats.org/wiki/hcard-cheatsheet) spec. However any node type
(like those created with nodeprofile or Bio or Advanced Profile or Content
Profile) can be used in the view. It doesn't matter what data table the view
is based on, only what fields are present in the view.

OPTIONS
------
Each style has a range of options you can use to customize the output:

 The following options are common to all plugins:
  1. Field output: Normal or Raw
      This determines if each object in the view is displayed as normally
      rendered by Drupal, or as the raw result object. Raw is useful if
      you don't want any Drupal formatting applied to the view result, for
      example, if you have a field with a date and you just want the timestamp
      value from the database. Note that both a field's label and content are
      rendered as raw so XML element or attribute labels will have the internal
      field name - for example instead of 'Body' a raw field will have the
      label 'node_revisions_body'.
  2. Plaintext output
      Selecting this neans that all HTML markup will be stripped from the
      view result. This is useful, for example, if you are generating an
      XML document from nodes and you just want the plain text content
      of a node without markup tags mixing with the other XML elements.
     (Note that you can also escape XML content using CDATA sections,
     see below.)
  3. Content-Type
      This determine the Content-Type header sent in a page display of
      a view. This header is necessary for most clients consuming data
      from the view. You can use the default Content-Type for the
      particular plugin or choose from alternate types.
  4. Use Views API mode - by default the plugins stop Drupal from
      doing any additional processing when a view is rendered - allowing
      the content to be output without any additional Drupal markup.
      However if you are calling a view programatically then this will
      hlar your code prematurely. The solution (contributed by icylake)
      is to use the Use Views API mode option if you are going to call
      the view from code. This option causes the plugin to not terminate
      Drupal execution.

 The following options are common to the views_xml, and views_xhtml plugins:
  1. Escape row content as CDATA
      This option escapes all content from the result row using the ![CDATA[
      XML directive. This is useful if you want all content markup preserved,
      but kept separate from the other XML tags in the document. You will
      have to instruct your client that the data you are processing is
      in CDATA blocks, and different XML processors may handle these blocks
      differently.
  2. XML document header
      This option lets you specify the XML document header which precedes the
      root XML element. If you specify a header here it will override any
      header generated automatically by the plugin.

 The views_json plugin has the following options:
  1. Root object name
      This specifies the name of the top-level object in the JSON object. The
      default is the name of the view base table (nodes, users, etc.)
  2. JSON data format
      This specifies the format of the JSON output - either simple, plain-
      vanilla JSON, or the JSON format compatible with the Simile/Exhibit
      application.

 The views_xml plugin has the following options:
  1. XML schema:
      This specifies the XML schema the view will render.
      Raw simply renders each view field using the field name as
      a element/attribute label and the field content as the element/attribute
      value.

      OPML renders each field as an attribute-value pair in an <outline>
      element. The OPML schema requires at least one field labelled 'text' - or
      if this is not found it falls back to 'body' or 'node_revisions_body'.
      The following fields are recommended (fallback in brackets):
      type (node_type), created(published, node_created, Post date).

      Atom renderes a view using the Atom syndication schema. You can use this
      format to create an Atom syndication of the content in your view. Atom
      requires the following fields to be present (fields in bracket indicate
      what the plugin will fall back to if it can find the explicitly named
      Atom field):
      id (nid), title(node_title) updated(last_updated, Updated date, changed,
      Last updated/commented, Last comment time)
      The following fields are recommended: content(Body, node_body,
      node_revisions_body), link (nid {a link will be constructed from the
      Drupal path and the nid), summary author(uid).

  2. Root element name:
      Only applies to the Raw XML schema. This specifies the root XML element
      in the document. All other elements will be children of this element.
      The default is the name of the view base table.

  3. Element output:
      Only applies to the Raw XML schema. This specifies whether the view
      fields will be output as nested child elements or attributes. For example
      if Element output is set to Nested then a field labelled 'title' with
      content 'foo' will be output as <title>foo</title> If Element output
      is set to Attributes then this field will be output as title = "foo"
      for each row element. Note that the plugin automatically strips invalid
      XML element and attribute label characters (like spaces), so a field like
      'Post date' will become 'postdate'.

  4. View author:
      This is used by the Atom and OPML plugins to provide the author
      of the Atom or OPML document. It can be a valid Drupal user name,
      a Drupal user uid, or any name otherwise.

 The views_rdf plugin has the following options:
  1. RDF vocabulary:
     This indicates what RDF vocabulary to use in the document: either
     FOAF or SIOC or DOAP . FOAF (Friend of a Friend) is useful for sharing a
     list of  users or people, while SIOC
     (Semantically-Interlinked Online Communities Project) is most useful for
     describing a set of pages, stories, blogs,
     or forum posts with comments from different people. SIOC itself uses
     FOAF to describe the posts and comments from different people. DOAP
     (Description of a Project) is useful for - as the name suggests - projects.
     See these links for more info:
      http://www.foaf-project.org/
      http://sioc-project.org/
      http://trac.usefulinc.com/doap

     The following fields are recognized when using the FOAF vocabulary
     (fallbacks in brackets):
     name, firstname, surname, title, nick, mbox (mail, email), mbox_sha1sum,
     openid, workplacehomepage, homepage, weblog, img, depiction, member,
     phone, jabberID, msnChatID, aimChatID, yahooChatID.

     The following fields are required when using the SIOC vocabulary:
     id (nid), created(node_created, Post date, title, type (node_type),
     changed (node_changed, updated/commented date) last_updated(updated date),
     body(node_body, node_revisions_body), uid (users_uid).

     The following fields are recognized when using the DOAP vocabulary:
     (optional fields in square brackets)
     nid, name, homepage, [license], [shortdesc], [language], [repositories],
     [developers]

 The views_xhtml plugin has the following options:
  1. Microformat
     This specifies the microformat to be rendered: hCard is most useful for a
     list of users or people. hCalendar can be used to describe a list of
     events.
     The following fields are recognized by hCard:
     Address Type, Post office box, Street Address, Extended Address, region,
     Locality. Postal Code, Country name, agent, bday, class, category, email,
     honorific prefix, Given name, Additional name, Family name, Honoric suffix,
     Nickname, Organization name, Organization unit, photo, tel.

     The following fields are recognized by hCalendar:
     class, category, description, summary, dtstart(Event start, event_start)
     dtend(Event end, event_end).


TODO
----
 Proper date handling for each format
 Check for separator in profile fields
 Properly handle grouped multiple values in views_xhtml et. al
 Strict conformance with Atom spec
 Recognize when field rewriting rules are used
 Represent multiple-valued fields using nested child elements
PROBLEM:
Drupal's block module is limited by the fact that a block can
only have one instance. Each block has a 1:1 relationship with
its region, weight, visibility (and other) settings. This means 
that it is impossible to have blocks in multiple regions or to
have blocks that have different settings on different pages.

SOLUTION:
multiblock module will keep track of multiple instances of blocks
and dispatch to their appropriate block hooks. Using this stratgey,
you would not enable any blocks that are implemented by other
modules. Instead, you will go to admin/build/block/instances and create
an "instance" of a block. Multiblock module will then implement this
block in its own block hook which will forward any block API calls
to the original module's hook. Using this method we can maintain
multiple instances of blocks with different settings but the same
implementation. This should not affect block-level caching. One
catch here is that the configure and save hooks are usually implemented
to save only one set of data. This means that for blocks that are
unaware of multiblock you will only be able to save CUSTOM data (this
doesn't include visibility, weight, region, etc.) for one set of data.

HOW TO USE IT:
1. Go to admin/structure/block/instances
2. Select the type of block you want to create an instance of and
   type a unique title for that instance
3. Click "Add Instance"
4. Go to admin/structure/block
5. Enable the block instance you have just created.

DEVELOPING MULTIBLOCK-ENABLED BLOCKS:
Multiblock should successfully clone any regular block created with the
block API. However, if you clone a regular block that implements a
hook_block_save or hook_block_configure hook, the custom block settings of
one block instance will overwrite the settings of another. To get around
this, you can make a block "multiblock enabled." To do this, you should
add a 'mb_enabled' key with a value of true in hook_block_info to each
multiblock enabled block you are creating. Next, add an optional $edit
argument to your hook_block_view and hook_block_configure functions. Once
you do this, the instances you create will get the block instance ID
passed in the $edit variable for the view, configure, and save $ops. This
will let you save and load different data to different instances based on
this instance ID. It is passed in with the 'multiblock_delta' key with the
following format:
$edit['multiblock_delta'] = array(
          '#type' => 'value',
          '#value' => $block_id
      );

Example implementation of hook_block_info:
function hook_block_info() {
  $blocks['powered-by'] = array(
    'info' => t('Powered by Drupal'),
    'weight' => '10',
    'cache' => DRUPAL_NO_CACHE,
    'mb_enabled' => TRUE,
  );
  return $blocks;
}
[![Build Status](https://travis-ci.org/NuCivic/dkan_dataset.png?branch=7.x-1.x)](https://travis-ci.org/NuCivic/dkan_dataset)

# DKAN Dataset

This is a Drupal module containing the content types and other functionality to publish Open Data sets in Drupal.

DKAN Dataset is a standalone module that can be added to any existing Drupal 7 site.

DKAN Dataset is part of the [DKAN](https://drupal.org/project/dkan "DKAN homepage") project which includes the [DKAN profile](https://drupal.org/project/dkan "DKAN homepage") which creates a standalone Open Data portal, and [DKAN Datastore](https://drupal.org/project/dkan_datastore "DKAN Datastore homepage") which is a module that can be coupled with DKAN Dataset to offer a datastore and data previews.

DKAN Dataset is currently managed in code on Github but is mirrored on Drupal.org.

## INSTALLATION

This module REQUIRES implementers to use "drush make". If you only use "drush download" you will miss key dependencies for required modules and libraries.

See installation instructions here: http://docs.getdkan.com/dkan-documentation/dkan-developers/adding-dkan-features-existing-drupal-site#Installing_DKAN_Dataset

## Contributing

We are accepting issues in the dkan issue thread only -> https://github.com/NuCivic/dkan/issues -> Please label your issue as **"component: dkan_dataset"** after submitting so we can identify problems and feature requests faster.

If you can, please cross reference commits in this repo to the corresponding issue in the dkan issue thread. You can do that easily adding this text:

```
NuCivic/dkan#issue_id
``` 

to any commit message or comment replacing **issue_id** with the corresponding issue id.
FileSaver.js
============

FileSaver.js implements the HTML5 W3C `saveAs()` FileSaver interface in browsers that do
not natively support it. There is a [FileSaver.js demo][1] that demonstrates saving
various media types.

FileSaver.js is the solution to saving files on the client-side, and is perfect for
webapps that need to generate files, or for saving sensitive information that shouldn't be
sent to an external server.

Looking for `canvas.toBlob()` for saving canvases? Check out
[canvas-toBlob.js][2] for a cross-browser implementation.

Supported browsers
------------------

| Browser        | Constructs as | Filenames    | Max Blob Size | Dependencies |
| -------------- | ------------- | ------------ | ------------- | ------------ |
| Firefox 20+    | Blob          | Yes          | 800 MiB       | None         |
| Firefox < 20   | data: URI     | No           | n/a           | [Blob.js](https://github.com/eligrey/Blob.js) |
| Chrome         | Blob          | Yes          | [500 MiB][3]  | None         |
| Chrome for Android | Blob      | Yes          | [500 MiB][3]  | None         |
| IE 10+         | Blob          | Yes          | 600 MiB       | None         |
| Opera 15+      | Blob          | Yes          | 500 MiB       | None         |
| Opera < 15     | data: URI     | No           | n/a           | [Blob.js](https://github.com/eligrey/Blob.js) |
| Safari 6.1+*   | Blob          | No           | ?             | None         |
| Safari < 6     | data: URI     | No           | n/a           | [Blob.js](https://github.com/eligrey/Blob.js) |

Feature detection is possible:

```js
try {
    var isFileSaverSupported = !!new Blob;
} catch (e) {}
```

### IE < 10

It is possible to save text files in IE < 10 without Flash-based polyfills.
See [ChenWenBrian and koffsyrup's `saveTextAs()`](https://github.com/koffsyrup/FileSaver.js#examples) for more details.

### Safari 6.1+

Blobs may be opened instead of saved sometimes—you may have to direct your Safari users to manually
press <kbd>⌘</kbd>+<kbd>S</kbd> to save the file after it is opened. Using the `application/octet-stream` MIME type to force downloads [can cause issues in Safari](https://github.com/eligrey/FileSaver.js/issues/12#issuecomment-47247096).

### iOS

saveAs must be run within a user interaction event such as onTouchDown or onClick; setTimeout will prevent saveAs from triggering. Due to restrictions in iOS saveAs opens in a new window instead of downloading, if you want this fixed please [tell Apple](https://bugs.webkit.org/show_bug.cgi?id=102914) how this bug is affecting you.

Syntax
------

```js
FileSaver saveAs(in Blob data, in DOMString filename)
```

Examples
--------

### Saving text

```js
var blob = new Blob(["Hello, world!"], {type: "text/plain;charset=utf-8"});
saveAs(blob, "hello world.txt");
```

The standard W3C File API [`Blob`][4] interface is not available in all browsers.
[Blob.js][5] is a cross-browser `Blob` implementation that solves this.

### Saving a canvas

```js
var canvas = document.getElementById("my-canvas"), ctx = canvas.getContext("2d");
// draw to canvas...
canvas.toBlob(function(blob) {
    saveAs(blob, "pretty image.png");
});
```

Note: The standard HTML5 `canvas.toBlob()` method is not available in all browsers.
[canvas-toBlob.js][6] is a cross-browser `canvas.toBlob()` that polyfills this.


![Tracking image](https://in.getclicky.com/212712ns.gif)

  [1]: http://eligrey.com/demos/FileSaver.js/
  [2]: https://github.com/eligrey/canvas-toBlob.js
  [3]: https://code.google.com/p/chromium/codesearch#chromium/src/storage/browser/blob/blob_storage_context.cc&type=cs&sq=package:chromium&l=37&rcl=1418672972
  [4]: https://developer.mozilla.org/en-US/docs/DOM/Blob
  [5]: https://github.com/eligrey/Blob.js
  [6]: https://github.com/eligrey/canvas-toBlob.js

Contributing
------------

The `FileSaver.js` distribution file is compiled with Uglify.js like so:

```bash
uglifyjs FileSaver.js --comments /@source/ > FileSaver.min.js
```

Please make sure you build a production version before submitting a pull request.
Installation profiles define additional steps that run after the base
installation provided by Drupal core when Drupal is first installed.

WHAT TO PLACE IN THIS DIRECTORY?
--------------------------------

Place downloaded and custom installation profiles in this directory.
Installation profiles are generally provided as part of a Drupal distribution.
They only impact the installation of your site. They do not have any effect on
an already running site.

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
Login integration for your site and the Pantheon control panel
The cod_support features cod_base and cod_session have been updated to 
reflect changes on the site. Do NOT update and/or revert these features unless you know what you're doing!

/sites/all/modules/contrib/cod_support

Dan Feder Nov 8 2013 dan@nuams.com