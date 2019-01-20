# &log

Super simple, but solves these pain points:

- Lets you leave log statements in production, client-side code.
- It won't log anything unless `localStorage.debug` is set.
- Uses native `console` rather than trying to wrap it in something (which makes the output ugly).
- Works with CommonJS.
- It's just a selective alias for the `window.console` so the normal API applies.

## How to use it:


Step 1. include it:

```html
<script src="andlog.js"></script>
```

Step 2. Use the `console` in your code as usual:

```javascript
console.log("hello");
```

Step 3. If you want to see log output set a value called `debug` in `localStorage` by doing typing this in console:

```javascript
localStorage.debug = true
```

  If you'd like to use a custom debug key then set `localStorage.andlogKey = 'something-else'` and then set `localStorage['something-else'] = true` to enable logging.

Step 4. Refresh the page, you should now see logs.

Step 5. To turn off console, just delete the localStorage flag:

```javascript
delete localStorage.debug
```

Step 6. Feel free to deploy to production with console stuff in there.


## CommonJS Version

If you're using this on the client but your project is in node.js you can install this with: [browserify](https://github.com/substack/node-browserify/) and npm. 

```javascript
var logger = require('andlog');

logger.log('hello');
```

This is identical to:

```javascript
console.log('hello');
```

You *could* even get fancy and call it `console`. However by doing this you take the risk that you'll forget to `require` it and it'll still work and you'll ship it to production. However, obviously this would work as well:

```javascript
var console = require('andlog');

console.log('hello');
```

## License

MIT

If you like this, follow [@HenrikJoreteg](http://twitter.com/henrikjoreteg) on the twitterwebz.
Leaflet.markercluster
=====================

Provides Beautiful Animated Marker Clustering functionality for [Leaflet](http://leafletjs.com), a JS library for interactive maps.

*Requires Leaflet 0.7.0 or newer.*

For a Leaflet 0.5 compatible version, [Download b128e950](https://github.com/Leaflet/Leaflet.markercluster/archive/b128e950d8f5d7da5b60bd0aa9a88f6d3dd17c98.zip)<br>
For a Leaflet 0.4 compatible version, [Download the 0.2 release](https://github.com/Leaflet/Leaflet.markercluster/archive/0.2.zip)

## Using the plugin
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
* **spiderfyOnMaxZoom**: When you click a cluster at the bottom zoom level we spiderfy it so you can see all of its markers.
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
* **spiderfyOnMaxZoom**: When you click a cluster at the bottom zoom level we spiderfy it so you can see all of its markers.
* **removeOutsideVisibleBounds**: Clusters and markers too far from the viewport are removed from the map for performance.

Other options
* **animateAddingMarkers**: If set to true then adding individual markers to the MarkerClusterGroup after it has been added to the map will add the marker and animate it in to the cluster. Defaults to false as this gives better performance when bulk adding markers. addLayers does not support this, only addLayer with individual Markers.
* **disableClusteringAtZoom**: If set, at this zoom level and below markers will not be clustered. This defaults to disabled. [See Example](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-realworld-maxzoom.388.html)
* **maxClusterRadius**: The maximum radius that a cluster will cover from the central marker (in pixels). Default 80. Decreasing will make more smaller clusters.
* **polygonOptions**: Options to pass when creating the L.Polygon(points, options) to show the bounds of a cluster
* **singleMarkerMode**: If set to true, overrides the icon for all added markers to make them appear as a 1 size cluster
* **spiderfyDistanceMultiplier**: Increase from 1 to increase the distance away from the center that spiderfied markers are placed. Use if you are using big marker icons (Default:1)
* **iconCreateFunction**: Function used to create the cluster icon [See default as example](https://github.com/Leaflet/Leaflet.markercluster/blob/15ed12654acdc54a4521789c498e4603fe4bf781/src/MarkerClusterGroup.js#L542).

## Events
If you register for click, mouseover, etc events just related to Markers in the cluster.
To recieve events for clusters listen to 'cluster' + 'eventIWant', ex: 'clusterclick', 'clustermouseover'.

Set your callback up as follows to handle both cases:

```javascript
markers.on('click', function (a) {
	console.log('marker ' + a.layer);
});

markers.on('clusterclick', function (a) {
	console.log('cluster ' + a.layer.getAllChildMarkers().length);
});
```

## Methods

### Getting the bounds of a cluster
When you recieve an event from a cluster you can query it for the bounds.
See [example/marker-clustering-convexhull.html](http://leaflet.github.com/Leaflet.markercluster/example/marker-clustering-convexhull.html) for a working example.
```javascript
markers.on('clusterclick', function (a) {
	map.addLayer(new L.Polygon(a.layer.getConvexHull()));
});
```

### Zooming to the bounds of a cluster
When you recieve an event from a cluster you can zoom to its bounds in one easy step.
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

[![Build Status](https://travis-ci.org/Leaflet/Leaflet.markercluster.png?branch=master)](https://travis-ci.org/Leaflet/Leaflet.markercluster)Social Buttons for Bootstrap
============================

Social Buttons made in pure CSS based on
[Bootstrap](http://twbs.github.io/bootstrap/) and
[Font Awesome](http://fortawesome.github.io/Font-Awesome/)!

[Check the live demo!](http://lipis.github.io/bootstrap-social)

Installation
------------

Include the `bootstrap-social.css` or `bootstrap-social.less` in your project, or
install it through [Bower](http://bower.io/):

    bower install bootstrap-social

Available classes
-----------------
 - `btn-adn`
 - `btn-bitbucket`
 - `btn-dropbox`
 - `btn-facebook`
 - `btn-flickr`
 - `btn-foursquare`
 - `btn-github`
 - `btn-google-plus`
 - `btn-instagram`
 - `btn-linkedin`
 - `btn-microsoft`
 - `btn-openid`
 - `btn-reddit`
 - `btn-soundcloud`
 - `btn-tumblr`
 - `btn-twitter`
 - `btn-vimeo`
 - `btn-vk`
 - `btn-yahoo`

Examples
--------

```html
<a class="btn btn-block btn-social btn-twitter">
  <i class="fa fa-twitter"></i>
  Sign in with Twitter
</a>

<a class="btn btn-social-icon btn-twitter">
  <i class="fa fa-twitter"></i>
</a>
```

Pull Requests
-------------
If you are about to create a new **Pull Request** for adding a new button don't
update the minified `bootstrap-social.css` file. It will be generated
automatically after a successful merge.
# [Start Bootstrap](http://startbootstrap.com/) - [SB Admin 2](http://startbootstrap.com/template-overviews/sb-admin-2/)

[SB Admin 2](http://startbootstrap.com/template-overviews/sb-admin-2/) is an open source, admin dashboard template for [Bootstrap](http://getbootstrap.com/) created by [Start Bootstrap](http://startbootstrap.com/).

## Getting Started

To use this template, choose one of the following options to get started:
* Download the latest release on Start Bootstrap
* Fork this repository on GitHub
* Install via bower using `bower install startbootstrap-sb-admin-2`

## Bugs and Issues

Have a bug or an issue with this template? [Open a new issue](https://github.com/IronSummitMedia/startbootstrap-sb-admin-2/issues) here on GitHub or leave a comment on the [template overview page at Start Bootstrap](http://startbootstrap.com/template-overviews/sb-admin-2/).

## Creator

Start Bootstrap was created by and is maintained by **David Miller**, Managing Parter at [Iron Summit Media Strategies](http://www.ironsummitmedia.com/).

* https://twitter.com/davidmillerskt
* https://github.com/davidtmiller

Start Bootstrap is based on the [Bootstrap](http://getbootstrap.com/) framework created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thorton](https://twitter.com/fat).

## Copyright and License

Copyright 2013-2015 Iron Summit Media Strategies, LLC. Code released under the [Apache 2.0](https://github.com/IronSummitMedia/startbootstrap-sb-admin-2/blob/gh-pages/LICENSE) license.
# metisMenu [![Build Status](https://secure.travis-ci.org/onokumus/metisMenu.png?branch=master)](https://travis-ci.org/onokumus/metisMenu)

> Easy menu jQuery plugin for Twitter Bootstrap 3

> Now support cdnjs & jsdelivr


## Installation

* [npm](http://npmjs.org/)

```bash
npm install metismenu
```

* [Bower](http://bower.io)

```bash
bower install metisMenu
```

* [Download](https://github.com/onokumus/metisMenu/archive/master.zip)

## Usage

1. Include Twitter Bootstrap StyleSheet

    ```html
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.0/css/bootstrap.min.css">
    ```

2. Include metisMenu StyleSheet

    ```html
    <link rel="stylesheet" href="//cdn.jsdelivr.net/bootstrap.metismenu/1.1.2/css/metismenu.min.css">
    ```

3. Include jQuery

    ```html
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    ```

4. Include Twitter Bootstrap Script

    ```html
    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.0/js/bootstrap.min.js"></script>
    ```

5. Include metisMenu plugin's code

    ```html
    <script src="//cdn.jsdelivr.net/bootstrap.metismenu/1.1.2/js/metismenu.min.js"></script>
    ```

6. Call the plugin:

    ```javascript
    $("#menu").metisMenu();
    ```

### Options

#### toggle
Type: `Boolean`
Default: `true`

For auto collapse support.

```javascript
  $("#menu").metisMenu({
    toggle: false
  });
```

#### doubleTapToGo
Type: `Boolean`
Default: `false`

For double tap support.

```javascript
  $("#menu").metisMenu({
    doubleTapToGo: true
  });
```


### [DEMO](http://demo.onokumus.com/metisMenu/)

Contains a simple HTML file to demonstrate metisMenu plugin.

### Release History
**DATE**       **VERSION**   **CHANGES**
* 2014-11-01   v1.1.3        Bootstrap 3.3.0
* 2014-07-07   v1.1.0	       Add double tap functionality
* 2014-06-24   v1.0.3	       cdnjs support & rename plugin
* 2014-06-18   v1.0.3        Create grunt task
* 2014-06-10   v1.0.2        Fixed for IE8 & IE9


## Author

metisMenu was made with love by these guys and a bunch of awesome [contributors](https://github.com/onokumus/metisMenu/graphs/contributors).

[![Osman Nuri Okumuş](https://0.gravatar.com/avatar/4fa374411129d6f574c33e4753ec402e?s=70)](http://onokumus.com) |
--- | --- | --- | --- | --- | --- | ---
[Osman Nuri Okumuş](http://onokumus.com) |


## License

[MIT License](https://github.com/onokumus/metisMenu/blob/master/LICENSE)
# Bootstrap for Sass
[![Gem Version](https://badge.fury.io/rb/bootstrap-sass.svg)](http://badge.fury.io/rb/bootstrap-sass)
[![npm version](https://img.shields.io/npm/v/bootstrap-sass.svg?style=flat)](https://www.npmjs.com/package/bootstrap-sass)
[![Bower Version](https://badge.fury.io/bo/bootstrap-sass.svg)](http://badge.fury.io/bo/bootstrap-sass)
[![Build Status](http://img.shields.io/travis/twbs/bootstrap-sass.svg)](http://travis-ci.org/twbs/bootstrap-sass)

`bootstrap-sass` is a Sass-powered version of [Bootstrap](http://github.com/twbs/bootstrap), ready to drop right into your Sass powered applications.

## Installation

Please see the appropriate guide for your environment of choice:

* [Ruby on Rails](#a-ruby-on-rails).
* [Compass](#b-compass-without-rails) not on Rails.
* [Bower](#c-bower).

### a. Ruby on Rails

`bootstrap-sass` is easy to drop into Rails with the asset pipeline.

In your Gemfile you need to add the `bootstrap-sass` gem, and ensure that the `sass-rails` gem is present - it is added to new Rails applications by default.

```ruby
gem 'bootstrap-sass', '~> 3.3.5'
gem 'sass-rails', '>= 3.2'
```

`bundle install` and restart your server to make the files available through the pipeline.

Import Bootstrap styles in `app/assets/stylesheets/application.scss`:

```scss
// "bootstrap-sprockets" must be imported before "bootstrap" and "bootstrap/variables"
@import "bootstrap-sprockets";
@import "bootstrap";
```

`bootstrap-sprockets` must be imported before `bootstrap` for the icon fonts to work.

Make sure the file has `.scss` extension (or `.sass` for Sass syntax). If you have just generated a new Rails app,
it may come with a `.css` file instead. If this file exists, it will be served instead of Sass, so rename it:

```console
$ mv app/assets/stylesheets/application.css app/assets/stylesheets/application.scss
```

Then, remove all the `//= require` and `//= require_tree` statements from the file. Instead, use `@import` to import Sass files.

Do not use `//= require` in Sass or your other stylesheets will not be [able to access][antirequire] the Bootstrap mixins or variables.

Require Bootstrap Javascripts in `app/assets/javascripts/application.js`:

```js
//= require jquery
//= require bootstrap-sprockets
```

`bootstrap-sprockets` and `bootstrap` [should not both be included](https://github.com/twbs/bootstrap-sass/issues/829#issuecomment-75153827) in `application.js`.

`bootstrap-sprockets` provides individual Bootstrap Javascript files (`alert.js` or `dropdown.js`, for example), while
`bootstrap` provides a concatenated file containing all Bootstrap Javascripts.

#### Bower with Rails

When using [bootstrap-sass Bower package](#c-bower) instead of the gem in Rails, configure assets in `config/application.rb`:

```ruby
# Bower asset paths
root.join('vendor', 'assets', 'bower_components').to_s.tap do |bower_path|
  config.sass.load_paths << bower_path
  config.assets.paths << bower_path
end
# Precompile Bootstrap fonts
config.assets.precompile << %r(bootstrap-sass/assets/fonts/bootstrap/[\w-]+\.(?:eot|svg|ttf|woff2?)$)
# Minimum Sass number precision required by bootstrap-sass
::Sass::Script::Value::Number.precision = [8, ::Sass::Script::Value::Number.precision].max
```

Replace Bootstrap `@import` statements in `application.scss` with:

```scss
$icon-font-path: "bootstrap-sass/assets/fonts/bootstrap/";
@import "bootstrap-sass/assets/stylesheets/bootstrap-sprockets";
@import "bootstrap-sass/assets/stylesheets/bootstrap";
```

Replace Bootstrap `require` directive in `application.js` with:

```js
//= require bootstrap-sass/assets/javascripts/bootstrap-sprockets
```

#### Rails 4.x

Please make sure `sprockets-rails` is at least v2.1.4.

#### Rails 3.2.x

bootstrap-sass is no longer compatible with Rails 3. The latest version of bootstrap-sass compatible with Rails 3.2 is v3.1.1.0.

### b. Compass without Rails

Install the gem:

```console
$ gem install bootstrap-sass
```

If you have an existing Compass project:

1. Require `bootstrap-sass` in `config.rb`:

    ```ruby
    require 'bootstrap-sass'
    ```

2. Install Bootstrap with:

    ```console
    $ bundle exec compass install bootstrap -r bootstrap-sass
    ```

If you are creating a new Compass project, you can generate it with bootstrap-sass support:

```console
$ bundle exec compass create my-new-project -r bootstrap-sass --using bootstrap
```

or, alternatively, if you're not using a Gemfile for your dependencies:

```console
$ compass create my-new-project -r bootstrap-sass --using bootstrap
```

This will create a new Compass project with the following files in it:

* [styles.sass](/templates/project/styles.sass) - main project Sass file, imports Bootstrap and variables.
* [_bootstrap-variables.sass](/templates/project/_bootstrap-variables.sass) - all of Bootstrap variables, override them here.

Some bootstrap-sass mixins may conflict with the Compass ones.
If this happens, change the import order so that Compass mixins are loaded later.

### c. Bower

bootstrap-sass Bower package is compatible with node-sass 3.2.0+. You can install it with:

```console
$ bower install bootstrap-sass
```

Sass, JS, and all other assets are located at [assets](/assets).

By default, `bower.json` main field list only the main `_bootstrap.scss` and all the static assets (fonts and JS).
This is compatible by default with asset managers such as [wiredep](https://github.com/taptapship/wiredep).

#### Node.js Mincer

If you use [mincer][mincer] with node-sass, import bootstrap like so:

In `application.css.ejs.scss` (NB **.css.ejs.scss**):

```scss
// Import mincer asset paths helper integration
@import "bootstrap-mincer";
@import "bootstrap";
```

In `application.js`:

```js
//= require bootstrap-sprockets
```

See also this [example manifest.js](/test/dummy_node_mincer/manifest.js) for mincer.


### Configuration

#### Sass

By default all of Bootstrap is imported.

You can also import components explicitly. To start with a full list of modules copy
[`_bootstrap.scss`](assets/stylesheets/_bootstrap.scss) file into your assets as `_bootstrap-custom.scss`.
Then comment out components you do not want from `_bootstrap-custom`.
In the application Sass file, replace `@import 'bootstrap'` with:

```scss
@import 'bootstrap-custom';
```

#### Sass: Number Precision

bootstrap-sass [requires](https://github.com/twbs/bootstrap-sass/issues/409) minimum [Sass number precision][sass-precision] of 8 (default is 5).

Precision is set for Rails and Compass automatically.
When using ruby Sass compiler standalone or with the Bower version you can set it with:

```ruby
::Sass::Script::Value::Number.precision = [8, ::Sass::Script::Value::Number.precision].max
```

#### Sass: Autoprefixer

Bootstrap requires the use of [Autoprefixer][autoprefixer].
[Autoprefixer][autoprefixer] adds vendor prefixes to CSS rules using values from [Can I Use](http://caniuse.com/).

#### JavaScript

[`assets/javascripts/bootstrap.js`](/assets/javascripts/bootstrap.js) contains all of Bootstrap JavaScript,
concatenated in the [correct order](/assets/javascripts/bootstrap-sprockets.js).


#### JavaScript with Sprockets or Mincer

If you use Sprockets or Mincer, you can require `bootstrap-sprockets` instead to load the individual modules:

```js
// Load all Bootstrap JavaScript
//= require bootstrap-sprockets
```

You can also load individual modules, provided you also require any dependencies.
You can check dependencies in the [Bootstrap JS documentation][jsdocs].

```js
//= require bootstrap/scrollspy
//= require bootstrap/modal
//= require bootstrap/dropdown
```

#### Fonts

The fonts are referenced as:

```scss
"#{$icon-font-path}#{$icon-font-name}.eot"
```

`$icon-font-path` defaults to `bootstrap/` if asset path helpers are used, and `../fonts/bootstrap/` otherwise.

When using bootstrap-sass with Compass, Sprockets, or Mincer, you **must** import the relevant path helpers before Bootstrap itself, for example:

```scss
@import "bootstrap-compass";
@import "bootstrap";
```

## Usage

### Sass

Import Bootstrap into a Sass file (for example, application.scss) to get all of Bootstrap's styles, mixins and variables!

```scss
@import "bootstrap";
```

You can also include optional bootstrap theme:

```scss
@import "bootstrap/theme";
```

The full list of bootstrap variables can be found [here](http://getbootstrap.com/customize/#less-variables). You can override these by simply redefining the variable before the `@import` directive, e.g.:

```scss
$navbar-default-bg: #312312;
$light-orange: #ff8c00;
$navbar-default-color: $light-orange;

@import "bootstrap";
```

## Version

Bootstrap for Sass version may differ from the upstream version in the last number, known as
[PATCH](http://semver.org/spec/v2.0.0.html). The patch version may be ahead of the corresponding upstream minor.
This happens when we need to release Sass-specific changes.

Before v3.3.2, Bootstrap for Sass version used to reflect the upstream version, with an additional number for
Sass-specific changes. This was changed due to Bower and npm compatibility issues.

The upstream versions vs the Bootstrap for Sass versions are:

| Upstream |    Sass |
|---------:|--------:|
|    3.3.5 |   3.3.5 |
|    3.3.4 |   3.3.4 |
|    3.3.2 |   3.3.3 |
| <= 3.3.1 | 3.3.1.x |

Always refer to [CHANGELOG.md](/CHANGELOG.md) when upgrading.

---

## Development and Contributing

If you'd like to help with the development of bootstrap-sass itself, read this section.

### Upstream Converter

Keeping bootstrap-sass in sync with upstream changes from Bootstrap used to be an error prone and time consuming manual process. With Bootstrap 3 we have introduced a converter that automates this.

**Note: if you're just looking to *use* Bootstrap 3, see the [installation](#installation) section above.**

Upstream changes to the Bootstrap project can now be pulled in using the `convert` rake task.

Here's an example run that would pull down the master branch from the main [twbs/bootstrap](https://github.com/twbs/bootstrap) repo:

    rake convert

This will convert the latest LESS to Sass and update to the latest JS.
To convert a specific branch or version, pass the branch name or the commit hash as the first task argument:

    rake convert[e8a1df5f060bf7e6631554648e0abde150aedbe4]

The latest converter script is located [here][converter] and does the following:

* Converts upstream bootstrap LESS files to its matching SCSS file.
* Copies all upstream JavaScript into `assets/javascripts/bootstrap`, a Sprockets manifest at `assets/javascripts/bootstrap-sprockets.js`, and a concatenation at `assets/javascripts/bootstrap.js`.
* Copies all upstream font files into `assets/fonts/bootstrap`.
* Sets `Bootstrap::BOOTSTRAP_SHA` in [version.rb][version] to the branch sha.

This converter fully converts original LESS to SCSS. Conversion is automatic but requires instructions for certain transformations (see converter output).
Please submit GitHub issues tagged with `conversion`.

## Credits

bootstrap-sass has a number of major contributors:

<!-- feel free to make these link wherever you wish -->
* [Thomas McDonald](https://twitter.com/thomasmcdonald_)
* [Tristan Harward](http://www.trisweb.com)
* Peter Gumeson
* [Gleb Mazovetskiy](https://github.com/glebm)

and a [significant number of other contributors][contrib].

## You're in good company
bootstrap-sass is used to build some awesome projects all over the web, including
[Diaspora](https://diasporafoundation.org/), [rails_admin](https://github.com/sferik/rails_admin),
Michael Hartl's [Rails Tutorial](http://railstutorial.org/), [gitlabhq](http://gitlabhq.com/) and
[kandan](http://kandan.io/).

[converter]: https://github.com/twbs/bootstrap-sass/blob/master/tasks/converter/less_conversion.rb
[version]: https://github.com/twbs/bootstrap-sass/blob/master/lib/bootstrap-sass/version.rb
[contrib]: https://github.com/twbs/bootstrap-sass/graphs/contributors
[antirequire]: https://github.com/twbs/bootstrap-sass/issues/79#issuecomment-4428595
[jsdocs]: http://getbootstrap.com/javascript/#transitions
[sass-precision]: http://sass-lang.com/documentation/Sass/Script/Value/Number.html#precision%3D-class_method
[mincer]: https://github.com/nodeca/mincer
[autoprefixer]: https://github.com/ai/autoprefixer
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
[olson]: http://ftp.iana.org/time-zones
DataTables Plugins
==================

This repository contains a collection of plug-ins for the jQuery [DataTables](http://datatables.net) table enhancer. These plug-ins are feature enhancing for the DataTables library, adding extra options to core functionality such as additional sort algorithms, API methods and pagination controls. The plug-ins should not be confused with DataTables "extras" which are more significant software libraries which add additional features to DataTables.

This repository holds the following plug-in types for DataTables:

* Sorting
  * Type based
  * Custom data source based
* API 
* Filtering
  * Type based
  * Row based
* Internationalisation translations
* Type detection
* Pagination
* Integration scripts
  * Twitter Bootstrap

Each directory has an index.html file which is used to generate the plug-ins documentation on [DataTables.net](http://datatables.net/plug-ins) and describes how plug-ins can be used.Holder
======

![](http://imsky.github.io/holder/images/header.png)

Holder renders image placeholders on the client side using SVG.

Used by [Bootstrap](http://getbootstrap.com), thousands of [open source projects](https://github.com/search?q=holder.js+in%3Apath&type=Code&ref=searchresults), and [many other sites](https://search.nerdydata.com/search/#!/searchTerm=holder.js/searchPage=1/sort=pop).

Installing
----------

* [Bower](http://bower.io/): `bower install holderjs`
* [cdnjs](http://cdnjs.com/): <http://cdnjs.com/libraries/holder>
* [jsDelivr](http://www.jsdelivr.com): <http://www.jsdelivr.com/#!holder>
* [Rails Assets](https://rails-assets.org): `gem 'rails-assets-holderjs'`
* [Meteor](http://atmospherejs.com/): `mrt add holder`
* [Composer](https://packagist.org/): `php composer.phar update imsky/holder`
* [NuGet](http://www.nuget.org/): `Install-Package Holder.js`

Usage
-----

Include ``holder.js`` in your HTML:

```html
<script src="holder.js"></script>
```

Holder will then process all images with a specific ``src`` attribute, like this one:

```html
<img src="holder.js/200x300">
```

The above tag will render as a placeholder 200 pixels wide and 300 pixels tall.

To avoid console 404 errors, you can use ``data-src`` instead of ``src``.

Themes
------

![](http://imsky.github.io/holder/images/holder_sky.png)![](http://imsky.github.io/holder/images/holder_vine.png)![](http://imsky.github.io/holder/images/holder_lava.png)

Holder includes support for themes, to help placeholders blend in with your layout.

There are 6 default themes: ``sky``, ``vine``, ``lava``, ``gray``, ``industrial``, and ``social``. Use them like so:

```html
<img src="holder.js/200x300/sky">
```

Custom colors
-------------

Custom colors on a specific image can be specified in the ``background:foreground`` format using hex notation, like this:

```html
<img data-src="holder.js/100x200/#000:#fff">
```

The above will render a placeholder with a black background and white text.

Custom text
-----------

You can specify custom text using the ``text:`` operator:

```html
<img data-src="holder.js/200x200/text:hello world">
```

If you have a group of placeholders where you'd like to use particular text, you can do so by adding a ``text`` property to the theme:

```js
Holder.addTheme("thumbnail", { background: "#fff", text: "Thumbnail" });
```

Holder automatically adds line breaks to text that goes outside of the image boundaries. If the text is so long it goes out of both horizontal and vertical boundaries, the text is moved to the top. If you prefer to control the line breaks, you can add `\n` to the `text` property:

```html
<img data-src="holder.js/300x200/text:Add \n line breaks \n anywhere.">
```

Custom fonts, web fonts and icon fonts
--------------------------------------

You can set a placeholder's font either through a theme or through the `font` flag:

```html
<img data-src="holder.js/300x200/font:Helvetica">
```

Placeholders using a custom font are rendered using canvas by default, due to SVG's constraints on cross-domain resource linking. If you're using only locally available fonts, you can disable this behavior by setting `noFontFallback` to `true` in `Holder.run` options. However, if you need to render a SVG placeholder using an externally loaded font, you have to use the `object` tag instead of the `img` tag and add a `holderjs` class to the appropriate `link` tags. Here's an example:

```html
<head>
<link href="http://.../font-awesome.css" rel="stylesheet" class="holderjs">
</head>
<body>
<object data="holder.js/300x200/font:FontAwesome"></object>
```

**Important:** When testing locally, font URLs must have a `http` or `https` protocol defined.

`<object>` placeholders work like `<img>` placeholders, with the added benefit of their DOM being able to be inspected and modified.


Customizing themes
------------------

Themes have 5 properties: ``foreground``, ``background``, ``size``, ``font`` and ``fontweight``. The ``size`` property specifies the minimum font size for the theme. The ``fontweight`` default value is ``bold``. You can create a sample theme like this:

```js
Holder.addTheme("dark", {
  background: "#000",
  foreground: "#aaa",
  size: 11,
  font: "Monaco",
  fontweight: "normal"
});
```

Using custom themes
-------------------

There are two ways to use custom themes with Holder:

* Include theme at runtime to render placeholders already using the theme name
* Include theme at any point and re-render placeholders that are using the theme name

The first approach is the easiest. After you include ``holder.js``, add a ``script`` tag that adds the theme you want:

```html
<script src="holder.js"></script>
<script>
Holder.addTheme("bright", {
  background: "white", foreground: "gray", size: 12
});
</script>
```

The second approach requires that you call ``run`` after you add the theme, like this:

```js
Holder.addTheme("bright", {background: "white", foreground: "gray", size: 12}).run();
```

Using custom themes and domain on specific images
-------------------------------------------------

You can use Holder in different areas on different images with custom themes:

```html
<img data-src="example.com/100x100/simple" id="new">
```

```js
Holder.run({
  domain: "example.com",
  themes: {
    "simple": {
      background: "#fff",
      foreground: "#000",
      size: 12
    }
  },
  images: "#new"
});
```

Random themes
-------------

You can render a placeholder with a random theme using the `random` flag:
```html
<img data-src="holder.js/300x200/random">
```

Fluid placeholders
------------------

Specifying a dimension in percentages creates a fluid placeholder that responds to media queries.

```html
<img data-src="holder.js/100%x75/social">
```

By default, the fluid placeholder will show its current size in pixels. To display the original dimensions, i.e. 100%x75, set the ``textmode`` flag to ``literal`` like so: `holder.js/100%x75/textmode:literal`.

Fluid placeholders need to be visible in order to work. In cases when a placeholder is not visible, the `Holder.invisibleErrorFn` function is called, which takes the callee function as an argument and returns a function that takes the placeholder element as an argument. This function by default throws an exception, however its behavior can and should be overridden by the user.

Automatically sized placeholders
--------------------------------

If you'd like to avoid Holder enforcing an image size, use the ``auto`` flag like so:

```html
<img data-src="holder.js/200x200/auto">
```

The above will render a placeholder without any embedded CSS for height or width.

To show the current size of an automatically sized placeholder, set the ``textmode`` flag to ``exact`` like so: `holder.js/200x200/auto/textmode:exact`.

Background placeholders
-----------------------

Holder can render placeholders as background images for elements with the `holderjs` class, like this:

```css
#sample {background:url(?holder.js/200x200/social) no-repeat}
```

```html
<div id="sample" class="holderjs"></div>
```

The Holder URL in CSS should have a `?` in front. Like in image placeholders, you can specify the Holder URL in a `data-background-src` attribute:

```html
<div data-background-src="?holder.js/300x200"></div>
```

**Important:** Make sure to define a height and/or width for elements with background placeholders. Fluid background placeholders are not yet supported.

**Important:** Some browsers can't parse URLs like `?holder.js/300x200/#fff:#000` due to the `#` characters. You can use `^` in place of `#` like this: `?holder.js/300x200/^fff:^000`.

Custom settings
---------------

Holder extends its default settings with the settings you provide, so you only have to include those settings you want changed. For example, you can run Holder on a specific domain like this:

```js
Holder.run({domain:"example.com"});
```

Using custom settings on load
-----------------------------

You can prevent Holder from running its default configuration by executing ``Holder.run`` with your custom settings right after including ``holder.js``. However, you'll have to execute ``Holder.run`` again to render any placeholders that use the default configuration.

Inserting an image with optional custom theme
---------------------------------------------

You can add a placeholder programmatically by chaining Holder calls:

```js
Holder.addTheme("new", {
  foreground: "#ccc",
  background: "#000",
  size: 10
}).addImage("holder.js/200x100/new", "body").run();
```

The first argument in ``addImage`` is the ``src`` attribute, and the second is a CSS selector of the parent element.

Using different renderers
-------------------------

Holder has three renderers: canvas, SVG, and HTML. The SVG renderer is used by default, however you can set the renderer using the `renderer` option, with either `svg`, `canvas`, or `html` values.

```js
Holder.run({renderer: 'canvas'});
```

Using with [lazyload.js](https://github.com/tuupola/jquery_lazyload)
------------------------

Holder is compatible with ``lazyload.js`` and works with both fluid and fixed-width images. For best results, run `.lazyload({skip_invisible:false})`.

Using with Angular.js
---------------------

You can use Holder in Angular projects with the following JS and HTML code (by [Nick Clark](https://github.com/NickClark)):

```js
angular.module('MyModule').directive('myHolder', function() {
  return {
    link: function(scope, element, attrs) {
      attrs.$set('data-src', attrs.myHolder);
      Holder.run({images:element[0]});
    }
  };
});
```

```html
<img my-holder="holder.js/200x300">
```

Browser support
---------------

* Chrome
* Firefox 3+
* Safari 4+
* Internet Explorer 9+ (with partial support for 6-8)
* Opera 15+ (with partial support for 12)
* Android (with fallback)

License
-------

Holder is provided under the [MIT License](http://opensource.org/licenses/MIT).

Credits
-------

Holder is a project by [Ivan Malopinsky](http://imsky.co).
# Morris.js - pretty time-series line graphs

[![Build Status](https://secure.travis-ci.org/morrisjs/morris.js.png?branch=master)](http://travis-ci.org/morrisjs/morris.js)

Morris.js is the library that powers the graphs on http://howmanyleft.co.uk/.
It's a very simple API for drawing line, bar, area and donut charts.

Cheers!

\- Olly (olly@oesmith.co.uk)

## Contributors wanted

I'm unfortunately not able to actively support Morris.js any more. I keep an eye
on the issues, but I rarely have the time to fix bugs or review pull requests.

If you're interested in actively contributing to Morris.js, please contact me on
the email address above.

## Requirements

- [jQuery](http://jquery.com/) (>= 1.7 recommended, but it'll probably work with
  older versions)
- [Raphael.js](http://raphaeljs.com/) (>= 2.0)

## Usage

See [the website](http://morrisjs.github.com/morris.js/).

## Development

Very daring.

Fork, hack, possibly even add some tests, then send a pull request :)

Remember that Morris.js is a coffeescript project. Please make your changes in
the `.coffee` files, not in the compiled javascript files in the root directory
of the project.

### Developer quick-start

You'll need [node.js](https://nodejs.org).  I recommend using
[nvm](https://github.com/creationix/nvm) for installing node in
development environments.

With node installed, install [grunt](https://github.com/cowboy/grunt) using
`npm install -g grunt-cli`, and then the rest of the test/build dependencies
with `npm install` in the morris.js project folder.

Once you're all set up, you can compile, minify and run the tests using `grunt`.

Note: I'm experimenting with using perceptual diffs to catch rendering
regressions. Due to font rendering differences between platforms, the pdiff
tests currently *only* pass on OS X.

## Changelog

### 0.5.1 - 15th June 2014

- Fix touch event handling.
- Fix stacked=false in bar chart [#275](https://github.com/morrisjs/morris.js/issues/275)
- Configurable vertical segments [#297](https://github.com/morrisjs/morris.js/issues/297)
- Deprecate continuousLine option.

### 0.5.0 - 19th March 2014

- Update grunt dependency [#288](https://github.com/morrisjs/morris.js/issues/228)
- Donut segment color config in data objects [#281](https://github.com/morrisjs/morris.js/issues/281)
- Customisable line widths and point drawing [#272](https://github.com/morrisjs/morris.js/issues/272)
- Bugfix for @options.smooth [#266](https://github.com/morrisjs/morris.js/issues/266)
- Option to disable axes individually [#253](https://github.com/morrisjs/morris.js/issues/253)
- Range selection [#252](https://github.com/morrisjs/morris.js/issues/252)
- Week format for x-labels [#250](https://github.com/morrisjs/morris.js/issues/250)
- Update developer quickstart instructions [#243](https://github.com/morrisjs/morris.js/issues/243)
- Experimenting with perceptual diffs.
- Add original data row to hover callback [#264](https://github.com/morrisjs/morris.js/issues/264)
- setData method for donut charts [#211](https://github.com/morrisjs/morris.js/issues/211)
- Automatic resizing [#111](https://github.com/morrisjs/morris.js/issues/111)
- Fix travis builds [#298](https://github.com/morrisjs/morris.js/issues/298)
- Option for rounded corners on bar charts [#305](https://github.com/morrisjs/morris.js/issues/305)
- Option to set padding for X axis labels [#306](https://github.com/morrisjs/morris.js/issues/306)
- Use local javascript for examples.
- Events on non-time series [#314](https://github.com/morrisjs/morris.js/issues/314)

### 0.4.3 - 12th May 2013

- Fix flickering hover box [#186](https://github.com/morrisjs/morris.js/issues/186)
- xLabelAngle option (diagonal labels!!) [#239](https://github.com/morrisjs/morris.js/issues/239)
- Fix area chart fill bug [#190](https://github.com/morrisjs/morris.js/issues/190)
- Make event handlers chainable
- gridTextFamily and gridTextWeight options
- Fix hovers with setData [#213](https://github.com/morrisjs/morris.js/issues/213)
- Fix hideHover behaviour [#236](https://github.com/morrisjs/morris.js/issues/236)

### 0.4.2 - 14th April 2013

- Fix DST handling [#191](https://github.com/morrisjs/morris.js/issues/191)
- Parse data values from strings in Morris.Donut [#189](https://github.com/morrisjs/morris.js/issues/189)
- Non-cumulative area charts [#199](https://github.com/morrisjs/morris.js/issues/199)
- Round Y-axis labels to significant numbers [#162](https://github.com/morrisjs/morris.js/162)
- Customising default hover content [#179](https://github.com/morrisjs/morris.js/179)

### 0.4.1 - 8th February 2013

- Fix goal and event rendering. [#181](https://github.com/morrisjs/morris.js/issues/181)
- Don't break when empty data is passed to setData [#142](https://github.com/morrisjs/morris.js/issues/142)
- labelColor option for donuts [#159](https://github.com/morrisjs/morris.js/issues/159)

### 0.4.0 - 26th January 2013

- Goals and events [#103](https://github.com/morrisjs/morris.js/issues/103).
- Bower package manager metadata.
- More flexible formatters [#107](https://github.com/morrisjs/morris.js/issues/107).
- Color callbacks.
- Decade intervals for time-axis labels.
- Non-continous line tweaks [#116](https://github.com/morrisjs/morris.js/issues/116).
- Stacked bars [#120](https://github.com/morrisjs/morris.js/issues/120).
- HTML hover [#134](https://github.com/morrisjs/morris.js/issues/134).
- yLabelFormat [#139](https://github.com/morrisjs/morris.js/issues/139).
- Disable axes [#114](https://github.com/morrisjs/morris.js/issues/114).

### 0.3.3 - 1st November 2012

- **Bar charts!** [#101](https://github.com/morrisjs/morris.js/issues/101).

### 0.3.2 - 28th October 2012

- **Area charts!** [#47](https://github.com/morrisjs/morris.js/issues/47).
- Some major refactoring and test suite improvements.
- Set smooth parameter per series [#91](https://github.com/morrisjs/morris.js/issues/91).
- Custom dateFormat for string x-values [#90](https://github.com/morrisjs/morris.js/issues/90).

### 0.3.1 - 13th October 2012

- Add `formatter` option for customising value labels in donuts [#75](https://github.com/morrisjs/morris.js/issues/75).
- Cycle `lineColors` on line charts to avoid running out of colours [#78](https://github.com/morrisjs/morris.js/issues/78).
- Add method to select donut segments. [#79](https://github.com/morrisjs/morris.js/issues/79).
- Don't go negative on yMin when all y values are zero. [#80](https://github.com/morrisjs/morris.js/issues/80).
- Don't sort data when parseTime is false [#83](https://github.com/morrisjs/morris.js/issues/83).
- Customise styling for points. [#87](https://github.com/morrisjs/morris.js/issues/87).

### 0.3.0 - 15th September 2012

- Donut charts!
- Bugfix: ymin/ymax bug [#71](https://github.com/morrisjs/morris.js/issues/71).
- Bugfix: infinite loop when data indicates horizontal line [#66](https://github.com/morrisjs/morris.js/issues/66).

### 0.2.10 - 26th June 2012

- Support for decimal labels on y-axis [#58](https://github.com/morrisjs/morris.js/issues/58).
- Better axis label clipping [#63](https://github.com/morrisjs/morris.js/issues/63).
- Redraw graphs with updated data using `setData` method [#64](https://github.com/morrisjs/morris.js/issues/64).
- Bugfix: series with zero or one non-null values [#65](https://github.com/morrisjs/morris.js/issues/65).

### 0.2.9 - 15th May 2012

- Bugfix: Fix zero-value regression
- Bugfix: Don't modify user-supplied data

### 0.2.8 - 10th May 2012

- Customising x-axis labels with `xLabelFormat` option
- Only use timezones when timezone info is specified
- Fix old IE bugs (mostly in examples!)
- Added `preunits` and `postunits` options
- Better non-continuous series data support

### 0.2.7 - 2nd April 2012

- Added `xLabels` option
- Refactored x-axis labelling
- Better ISO date support
- Fix bug with single value in non time-series graphs

### 0.2.6 - 18th March 2012

- Partial series support (see `null` y-values in `examples/quarters.html`)
- `parseTime` option bugfix for non-time-series data

### 0.2.5 - 15th March 2012

- Raw millisecond timestamp support (with `dateFormat` option)
- YYYY-MM-DD HH:MM[:SS[.SSS]] date support
- Decimal number labels

### 0.2.4 - 8th March 2012

- Negative y-values support
- `ymin` option
- `units` options

### 0.2.3 - 6th Mar 2012

- jQuery no-conflict compatibility
- Support ISO week-number dates
- Optionally hide hover on mouseout (`hideHover`)
- Optionally skip parsing dates, treating X values as an equally-spaced series (`parseTime`)

### 0.2.2 - 29th Feb 2012

- Bugfix: mouseover error when options.data.length == 2
- Automatically sort options.data

### 0.2.1 - 28th Feb 2012

- Accept a DOM element *or* an ID in `options.element`
- Add `smooth` option
- Bugfix: clone `@default`
- Add `ymax` option

## License

Copyright (c) 2012-2014, Olly Smith
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# [Bootstrap](http://getbootstrap.com)
[![Slack](https://bootstrap-slack.herokuapp.com/badge.svg)](https://bootstrap-slack.herokuapp.com)
![Bower version](https://img.shields.io/bower/v/bootstrap.svg)
[![npm version](https://img.shields.io/npm/v/bootstrap.svg)](https://www.npmjs.com/package/bootstrap)
[![Build Status](https://img.shields.io/travis/twbs/bootstrap/master.svg)](https://travis-ci.org/twbs/bootstrap)
[![devDependency Status](https://img.shields.io/david/dev/twbs/bootstrap.svg)](https://david-dm.org/twbs/bootstrap#info=devDependencies)
[![Selenium Test Status](https://saucelabs.com/browser-matrix/bootstrap.svg)](https://saucelabs.com/u/bootstrap)

Bootstrap is a sleek, intuitive, and powerful front-end framework for faster and easier web development, created by [Mark Otto](https://twitter.com/mdo) and [Jacob Thornton](https://twitter.com/fat), and maintained by the [core team](https://github.com/orgs/twbs/people) with the massive support and involvement of the community.

To get started, check out <http://getbootstrap.com>!

## Table of contents

- [Quick start](#quick-start)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Community](#community)
- [Versioning](#versioning)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

## Quick start

Several quick start options are available:

- [Download the latest release](https://github.com/twbs/bootstrap/archive/v3.3.5.zip).
- Clone the repo: `git clone https://github.com/twbs/bootstrap.git`.
- Install with [Bower](http://bower.io): `bower install bootstrap`.
- Install with [npm](https://www.npmjs.com): `npm install bootstrap`.
- Install with [Meteor](https://www.meteor.com): `meteor add twbs:bootstrap`.
- Install with [Composer](https://getcomposer.org): `composer require twbs/bootstrap`.

Read the [Getting started page](http://getbootstrap.com/getting-started/) for information on the framework contents, templates and examples, and more.

### What's included

Within the download you'll find the following directories and files, logically grouping common assets and providing both compiled and minified variations. You'll see something like this:

```
bootstrap/
├── css/
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap-theme.css
│   ├── bootstrap-theme.css.map
│   └── bootstrap-theme.min.css
├── js/
│   ├── bootstrap.js
│   └── bootstrap.min.js
└── fonts/
    ├── glyphicons-halflings-regular.eot
    ├── glyphicons-halflings-regular.svg
    ├── glyphicons-halflings-regular.ttf
    ├── glyphicons-halflings-regular.woff
    └── glyphicons-halflings-regular.woff2
```

We provide compiled CSS and JS (`bootstrap.*`), as well as compiled and minified CSS and JS (`bootstrap.min.*`). CSS [source maps](https://developer.chrome.com/devtools/docs/css-preprocessors) (`bootstrap.*.map`) are available for use with certain browsers' developer tools. Fonts from Glyphicons are included, as is the optional Bootstrap theme.



## Bugs and feature requests

Have a bug or a feature request? Please first read the [issue guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md#using-the-issue-tracker) and search for existing and closed issues. If your problem or idea is not addressed yet, [please open a new issue](https://github.com/twbs/bootstrap/issues/new).


## Documentation

Bootstrap's documentation, included in this repo in the root directory, is built with [Jekyll](http://jekyllrb.com) and publicly hosted on GitHub Pages at <http://getbootstrap.com>. The docs may also be run locally.

### Running documentation locally

1. If necessary, [install Jekyll](http://jekyllrb.com/docs/installation) (requires v2.5.x).
  - **Windows users:** Read [this unofficial guide](http://jekyll-windows.juthilo.com/) to get Jekyll up and running without problems.
2. Install the Ruby-based syntax highlighter, [Rouge](https://github.com/jneen/rouge), with `gem install rouge`.
3. From the root `/bootstrap` directory, run `jekyll serve` in the command line.
4. Open <http://localhost:9001> in your browser, and voilà.

Learn more about using Jekyll by reading its [documentation](http://jekyllrb.com/docs/home/).

### Documentation for previous releases

Documentation for v2.3.2 has been made available for the time being at <http://getbootstrap.com/2.3.2/> while folks transition to Bootstrap 3.

[Previous releases](https://github.com/twbs/bootstrap/releases) and their documentation are also available for download.



## Contributing

Please read through our [contributing guidelines](https://github.com/twbs/bootstrap/blob/master/CONTRIBUTING.md). Included are directions for opening issues, coding standards, and notes on development.

Moreover, if your pull request contains JavaScript patches or features, you must include [relevant unit tests](https://github.com/twbs/bootstrap/tree/master/js/tests). All HTML and CSS should conform to the [Code Guide](https://github.com/mdo/code-guide), maintained by [Mark Otto](https://github.com/mdo).

Editor preferences are available in the [editor config](https://github.com/twbs/bootstrap/blob/master/.editorconfig) for easy use in common text editors. Read more and download plugins at <http://editorconfig.org>.



## Community

Get updates on Bootstrap's development and chat with the project maintainers and community members.

- Follow [@getbootstrap on Twitter](https://twitter.com/getbootstrap).
- Read and subscribe to [The Official Bootstrap Blog](http://blog.getbootstrap.com).
- Join [the official Slack room](https://bootstrap-slack.herokuapp.com).
- Chat with fellow Bootstrappers in IRC. On the `irc.freenode.net` server, in the `##bootstrap` channel.
- Implementation help may be found at Stack Overflow (tagged [`twitter-bootstrap-3`](https://stackoverflow.com/questions/tagged/twitter-bootstrap-3)).
- Developers should use the keyword `bootstrap` on packages which modify or add to the functionality of Bootstrap when distributing through [npm](https://www.npmjs.com/browse/keyword/bootstrap) or similar delivery mechanisms for maximum discoverability.



## Versioning

For transparency into our release cycle and in striving to maintain backward compatibility, Bootstrap is maintained under [the Semantic Versioning guidelines](http://semver.org/). Sometimes we screw up, but we'll adhere to those rules whenever possible.



## Creators

**Mark Otto**

- <https://twitter.com/mdo>
- <https://github.com/mdo>

**Jacob Thornton**

- <https://twitter.com/fat>
- <https://github.com/fat>



## Copyright and license

Code and documentation copyright 2011-2015 Twitter, Inc. Code released under [the MIT license](https://github.com/twbs/bootstrap/blob/master/LICENSE). Docs released under [Creative Commons](https://github.com/twbs/bootstrap/blob/master/docs/LICENSE).
= Mechanize {<img src="https://secure.travis-ci.org/sparklemotion/mechanize.png?rvm=1.9.3" />}[http://travis-ci.org/sparklemotion/mechanize]

* http://mechanize.rubyforge.org
* https://github.com/sparklemotion/mechanize

== Description

The Mechanize library is used for automating interaction with websites.
Mechanize automatically stores and sends cookies, follows redirects,
and can follow links and submit forms.  Form fields can be populated and
submitted.  Mechanize also keeps track of the sites that you have visited as
a history.

== Dependencies

* ruby 1.9.2 or newer
* nokogiri[http://nokogiri.rubyforge.org]

== Support:

The mechanize mailing list is available here:

* http://rubyforge.org/mailman/listinfo/mechanize-users

The bug tracker is available here:

* https://github.com/sparklemotion/mechanize/issues

== Examples

If you are just starting, check out the GUIDE[http://mechanize.rubyforge.org/GUIDE_rdoc.html] or
the EXAMPLES[http://mechanize.rubyforge.org/EXAMPLES_rdoc.html] file.

== Developers

To run the tests for the first time:

  gem install hoe rake
  rake newb

This will install all the required dependencies for running the tests.  For
subsequent test runs:

  rake test

You can also use +autotest+ from the ZenTest gem to run tests.

See also Mechanize::TestCase to read about the built-in testing
infrastructure.

== Authors

Copyright (c) 2005 by Michael Neumann (mneumann@ntecs.de)

Copyright (c) 2006-2011:

* {Aaron Patterson}[http://tenderlovemaking.com] (aaronp@rubyforge.org)
* {Mike Dalessio}[http://mike.daless.io] (mike@csa.net)

Copyright (c) 2011-2013:

* {Eric Hodel}[http://blog.segment7.net] (drbrain@segment7.net)
* {Akinori MUSHA}[http://blog.akinori.org] (knu@idaemons.org)
* {Lee Jarvis}[http://aeroproof.com] (ljjarvis@gmail.com)

This library comes with a shameless plug for employing me
(Aaron[http://tenderlovemaking.com/]) programming Ruby, my favorite language!

== Acknowledgments

This library was heavily influenced by its namesake in the Perl world.  A big
thanks goes to {Andy Lester}[http://petdance.com],
the author of the original Perl module WWW::Mechanize which is available
here[http://search.cpan.org/dist/WWW-Mechanize/].  Ruby Mechanize would not be around without you!

Thank you to Michael Neumann for starting the Ruby version.  Thanks to everyone
who's helped out in various ways.  Finally, thank you to the people using this
library!

== License

This library is distributed under the MIT license.  Please see the LICENSE[http://mechanize.rubyforge.org/LICENSE_rdoc.html] file.

ruby-unf
========

Synopsis
--------

* A wrapper library to bring Unicode Normalization Form support to Ruby/JRuby

Description
-----------

* Uses `unf_ext` on CRuby and `java.text.Normalizer` on JRuby.

* Normalizes UTF-8 strings into and from NFC, NFD, NFKC or NFKD

        # For bulk conversion
        normalizer = UNF::Normalizer.instance
        a_bunch_of_strings.map! { |string|
          normalizer.normalize(string, :nfc) #=> string in NFC
        }

        # Class method
        UNF::Normalizer.normalize(string, :nfc)

        # Instance methods of String
        string.to_nfc

Installation
------------

	gem install unf

License
-------

Copyright (c) 2011, 2012, 2013 Akinori MUSHA

Licensed under the 2-clause BSD license.
See `LICENSE` for details.
# Active Job -- Make work happen later

Active Job is a framework for declaring jobs and making them run on a variety
of queueing backends. These jobs can be everything from regularly scheduled
clean-ups, to billing charges, to mailings. Anything that can be chopped up into
small units of work and run in parallel, really.

It also serves as the backend for Action Mailer's #deliver_later functionality
that makes it easy to turn any mailing into a job for running later. That's
one of the most common jobs in a modern web application: Sending emails outside
of the request-response cycle, so the user doesn't have to wait on it.

The main point is to ensure that all Rails apps will have a job infrastructure
in place, even if it's in the form of an "immediate runner". We can then have
framework features and other gems build on top of that, without having to worry
about API differences between Delayed Job and Resque. Picking your queuing
backend becomes more of an operational concern, then. And you'll be able to
switch between them without having to rewrite your jobs.


## Usage

Set the queue adapter for Active Job:

``` ruby
ActiveJob::Base.queue_adapter = :inline # default queue adapter
```
Note: To learn how to use your preferred queueing backend see its adapter
documentation at
[ActiveJob::QueueAdapters](http://api.rubyonrails.org/classes/ActiveJob/QueueAdapters.html).

Declare a job like so:

```ruby
class MyJob < ActiveJob::Base
  queue_as :my_jobs

  def perform(record)
    record.do_work
  end
end
```

Enqueue a job like so:

```ruby
MyJob.perform_later record  # Enqueue a job to be performed as soon the queueing system is free.
```

```ruby
MyJob.set(wait_until: Date.tomorrow.noon).perform_later(record)  # Enqueue a job to be performed tomorrow at noon.
```

```ruby
MyJob.set(wait: 1.week).perform_later(record) # Enqueue a job to be performed 1 week from now.
```

That's it!


## GlobalID support

Active Job supports [GlobalID serialization](https://github.com/rails/globalid/) for parameters. This makes it possible
to pass live Active Record objects to your job instead of class/id pairs, which
you then have to manually deserialize. Before, jobs would look like this:

```ruby
class TrashableCleanupJob
  def perform(trashable_class, trashable_id, depth)
    trashable = trashable_class.constantize.find(trashable_id)
    trashable.cleanup(depth)
  end
end
```

Now you can simply do:

```ruby
class TrashableCleanupJob
  def perform(trashable, depth)
    trashable.cleanup(depth)
  end
end
```

This works with any class that mixes in GlobalID::Identification, which
by default has been mixed into Active Record classes.


## Supported queueing systems

Active Job has built-in adapters for multiple queueing backends (Sidekiq,
Resque, Delayed Job and others). To get an up-to-date list of the adapters
see the API Documentation for [ActiveJob::QueueAdapters](http://api.rubyonrails.org/classes/ActiveJob/QueueAdapters.html).

## Auxiliary gems

* [activejob-stats](https://github.com/seuros/activejob-stats)

## Download and installation

The latest version of Active Job can be installed with RubyGems:

```
  % [sudo] gem install activejob
```

Source code can be downloaded as part of the Rails project on GitHub

* https://github.com/rails/rails/tree/4-2-stable/activejob

## License

Active Job is released under the MIT license:

* http://www.opensource.org/licenses/MIT


## Support

API documentation is at

* http://api.rubyonrails.org

Bug reports can be filed for the Ruby on Rails project here:

* https://github.com/rails/rails/issues

Feature requests should be discussed on the rails-core mailing list here:

* https://groups.google.com/forum/?fromgroups#!forum/rubyonrails-core
[![Build Status](https://travis-ci.org/rocky/columnize.png)](https://travis-ci.org/rocky/columnize) [![Gem Version](https://badge.fury.io/rb/columnize.svg)](http://badge.fury.io/rb/columnize)

Columnize - Format an Array as a Column-aligned String
============================================================================

In showing a long lists, sometimes one would prefer to see the value
arranged aligned in columns. Some examples include listing methods of
an object, listing debugger commands, or showing a numeric array with data
aligned.

Setup
-----

    $ irb
    >> require 'columnize'
    => true

With numeric data
-----------------

    >> a = (1..10).to_a
    => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >> a.columnize
    => "1  2  3  4  5  6  7  8  9  10"

    >> puts a.columnize :arrange_array => true, :displaywidth => 10
    [1, 2, 3,
     4, 5, 6,
     7, 8, 9,
     10]
    => nil

    >> puts a.columnize :arrange_array => true, :displaywidth => 20
    [1, 2, 3,  4, 5,  6,
     7, 8, 9, 10]
    => nil

With String data
----------------

    >> g = %w(bibrons golden madascar leopard mourning suras tokay)
    => ["bibrons", "golden", "madascar", "leopard", "mourning", "suras", "tokay"]

    >> puts g.columnize :displaywidth => 15
    bibrons   suras
    golden    tokay
    madascar
    leopard
    mourning
    => nil

    >> puts g.columnize :displaywidth => 19, :colsep => ' | '
    bibrons  | suras
    golden   | tokay
    madascar
    leopard
    mourning
    => nil

    >> puts g.columnize :displaywidth => 18, :colsep => ' | ', :ljust => false
    bibrons  | mourning
    golden   | suras
    madascar | tokay
    leopard
    => nil

Using Columnize.columnize
-------------------------

    >> Columnize.columnize(a)
    => "1  2  3  4  5  6  7  8  9  10"

    >> puts Columnize.columnize(a, :displaywidth => 10)
    1  5   9
    2  6  10
    3  7
    4  8
    => nil

    >> Columnize.columnize(g)
    => "bibrons  golden  madascar  leopard  mourning  suras  tokay"

    >> puts Columnize.columnize(g, :displaywidth => 19, :colsep => ' | ')
    bibrons  | mourning
    golden   | suras
    madascar | tokay
    leopard
    => nil


Credits
-------

This is adapted from a method of the same name from Python's cmd module.

Other stuff
-----------

Authors:   Rocky Bernstein <rockyb@rubyforge.org> [![endorse](https://api.coderwall.com/rocky/endorsecount.png)](https://coderwall.com/rocky) and [Martin Davis](https://github.com/waslogic)

License:   Copyright (c) 2011,2013 Rocky Bernstein

Warranty
--------

You can redistribute it and/or modify it under either the terms of the GPL
version 2 or the conditions listed in COPYING
= Diff::LCS

home :: http://diff-lcs.rubyforge.org/
code :: https://github.com/halostatue/diff-lcs
bugs :: https://github.com/halostatue/diff-lcs/issues
rdoc :: http://rubydoc.info/github/halostatue/diff-lcs

== Description

Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

This is release 1.2.4, fixing a bug introduced after diff-lcs 1.1.3 that did
not properly prune common sequences at the beginning of a comparison set.
Thanks to Paul Kunysch for fixing this issue.

Coincident with the release of diff-lcs 1.2.3, we reported an issue with
Rubinius in 1.9 mode
({rubinius/rubinius#2268}[https://github.com/rubinius/rubinius/issues/2268]).
We are happy to report that this issue has been resolved.

== Synopsis

Using this module is quite simple. By default, Diff::LCS does not extend
objects with the Diff::LCS interface, but will be called as if it were a
function:

  require 'diff/lcs'

  seq1 = %w(a b c e h j l m n p)
  seq2 = %w(b c d e f j k l m r s t)

  lcs = Diff::LCS.LCS(seq1, seq2)
  diffs = Diff::LCS.diff(seq1, seq2)
  sdiff = Diff::LCS.sdiff(seq1, seq2)
  seq = Diff::LCS.traverse_sequences(seq1, seq2, callback_obj)
  bal = Diff::LCS.traverse_balanced(seq1, seq2, callback_obj)
  seq2 == Diff::LCS.patch!(seq1, diffs)
  seq1 == Diff::LCS.unpatch!(seq2, diffs)
  seq2 == Diff::LCS.patch!(seq1, sdiff)
  seq1 == Diff::LCS.unpatch!(seq2, sdiff)

Objects can be extended with Diff::LCS:

  seq1.extend(Diff::LCS)
  lcs = seq1.lcs(seq2)
  diffs = seq1.diff(seq2)
  sdiff = seq1.sdiff(seq2)
  seq = seq1.traverse_sequences(seq2, callback_obj)
  bal = seq1.traverse_balanced(seq2, callback_obj)
  seq2 == seq1.patch!(diffs)
  seq1 == seq2.unpatch!(diffs)
  seq2 == seq1.patch!(sdiff)
  seq1 == seq2.unpatch!(sdiff)

By requiring 'diff/lcs/array' or 'diff/lcs/string', Array or String will be
extended for use this way.

Note that Diff::LCS requires a sequenced enumerable container, which means that
the order of enumeration is both predictable and consistent for the same set of
data. While it is theoretically possible to generate a diff for an unordered
hash, it will only be meaningful if the enumeration of the hashes is
consistent. In general, this will mean that containers that behave like String
or Array will perform best.

== History

Diff::LCS is a port of Perl's Algorithm::Diff that uses the McIlroy-Hunt
longest common subsequence (LCS) algorithm to compute intelligent differences
between two sequenced enumerable containers. The implementation is based on
Mario I. Wolczko's {Smalltalk version 1.2}[ftp://st.cs.uiuc.edu/pub/Smalltalk/MANCHESTER/manchester/4.0/diff.st]
(1993) and Ned Konz's Perl version
{Algorithm::Diff 1.15}[http://search.cpan.org/~nedkonz/Algorithm-Diff-1.15/].

This library is called Diff::LCS because of an early version of Algorithm::Diff
which was restrictively licensed.

== Continuous Integration Status

{<img src="https://travis-ci.org/halostatue/diff-lcs.png" />}[https://travis-ci.org/halostatue/diff-lcs]

:include: Contributing.rdoc

:include: License.rdoc
connection\_pool
=================
[![Build Status](https://travis-ci.org/mperham/connection_pool.svg)](https://travis-ci.org/mperham/connection_pool)

Generic connection pooling for Ruby.

MongoDB has its own connection pool.  ActiveRecord has its own connection pool.
This is a generic connection pool that can be used with anything, e.g. Redis,
Dalli and other Ruby network clients.

**WARNING**: Don't ever use `Timeout.timeout` in your Ruby code or you will see
occasional silent corruption and mysterious errors.  The Timeout API is unsafe
and cannot be used correctly, ever.  Use proper socket timeout options as
exposed by Net::HTTP, Redis, Dalli, etc.


Usage
-----

Create a pool of objects to share amongst the fibers or threads in your Ruby
application:

``` ruby
$memcached = ConnectionPool.new(size: 5, timeout: 5) { Dalli::Client.new }
```

Then use the pool in your application:

``` ruby
$memcached.with do |conn|
  conn.get('some-count')
end
```

If all the objects in the connection pool are in use, `with` will block
until one becomes available.  If no object is available within `:timeout` seconds,
`with` will raise a `Timeout::Error`.

Optionally, you can specify a timeout override using the with-block semantics:

``` ruby
$memcached.with(timeout: 2.0) do |conn|
  conn.get('some-count')
end
```

This will only modify the resource-get timeout for this particular
invocation. This is useful if you want to fail-fast on certain non critical
sections when a resource is not available, or conversely if you are comfortable
blocking longer on a particular resource. This is not implemented in the below
`ConnectionPool::Wrapper` class.

You can use `ConnectionPool::Wrapper` to wrap a single global connection,
making it easier to port your connection code over time:

``` ruby
$redis = ConnectionPool::Wrapper.new(size: 5, timeout: 3) { Redis.connect }
$redis.sadd('foo', 1)
$redis.smembers('foo')
```

The wrapper uses `method_missing` to checkout a connection, run the requested
method and then immediately check the connection back into the pool.  It's
**not** high-performance so you'll want to port your performance sensitive code
to use `with` as soon as possible.

``` ruby
$redis.with do |conn|
  conn.sadd('foo', 1)
  conn.smembers('foo')
end
```

Once you've ported your entire system to use `with`, you can simply remove
`Wrapper` and use the simpler and faster `ConnectionPool`.

You can shut down a ConnectionPool instance once it should no longer be used.
Further checkout attempts will immediately raise an error but existing checkouts
will work.

```ruby
cp = ConnectionPool.new { Redis.new }
cp.shutdown { |conn| conn.close }
```

Shutting down a connection pool will block until all connections are checked in and closed.
Note that shutting down is completely optional; Ruby's garbage collector will reclaim
unreferenced pools under normal circumstances.


Notes
-----

- Connections are lazily created as needed.
- There is no provision for repairing or checking the health of a connection;
  connections should be self-repairing.  This is true of the Dalli and Redis
  clients.


Install
-------

```
$ gem install connection_pool
```


Author
------

Mike Perham, [@mperham](https://twitter.com/mperham), <http://mikeperham.com>
= Rack::Test {<img src="https://codeclimate.com/github/brynary/rack-test.png" />}[https://codeclimate.com/github/brynary/rack-test] {<img src="https://codeclimate.com/github/brynary/rack-test/coverage.png" />}[https://codeclimate.com/github/brynary/rack-test]

- Code: http://github.com/brynary/rack-test

== Description

Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries
to build on. Most of its initial functionality is an extraction of Merb 1.0's
request helpers feature.

== Features

* Maintains a cookie jar across requests
* Easily follow redirects when desired
* Set request headers to be used by all subsequent requests
* Small footprint. Approximately 200 LOC

== Examples

  require "rack/test"

  class HomepageTest < Test::Unit::TestCase
    include Rack::Test::Methods

    def app
      MyApp.new
    end

    def test_redirect_logged_in_users_to_dashboard
      authorize "bryan", "secret"
      get "/"
      follow_redirect!

      assert_equal "http://example.org/redirected", last_request.url
      assert last_response.ok?
    end

  end


If you want to test one app in isolation, you just return that app as shown above. But if you want to test the entire app stack, including middlewares, cascades etc. you need to parse the app defined in config.ru.

    OUTER_APP = Rack::Builder.parse_file('config.ru').first

    class TestApp < Test::Unit::TestCase
      include Rack::Test::Methods

      def app
        OUTER_APP
      end

      def test_root
        get '/'
        assert last_response.ok?
      end
    end


== Install

To install the latest release as a gem:

  sudo gem install rack-test

Or via Bundler:

  gem "rack-test", require: "rack/test"

== Authors

- Maintained by {Bryan Helmkamp}[mailto:bryan@brynary.com]
- Contributions from Simon Rozet, Pat Nakajima and others
- Much of the original code was extracted from Merb 1.0's request helper

== License

Copyright (c) 2008-2009 Bryan Helmkamp, Engine Yard Inc.
See MIT-LICENSE.txt in this directory.

== Releasing

* Ensure History.txt is up-to-date
* Bump VERSION in lib/rack/test.rb
* thor :release
Slop
====

Slop is a simple option parser with an easy to remember syntax and friendly API.
API Documentation is available [here](http://leejarvis.github.com/rdoc/slop/).

[![Build Status](https://travis-ci.org/leejarvis/slop.png?branch=master)](http://travis-ci.org/leejarvis/slop)

Usage
-----

```ruby
opts = Slop.parse do
  banner 'Usage: foo.rb [options]'

  on 'name=', 'Your name'
  on 'p', 'password', 'An optional password', argument: :optional
  on 'v', 'verbose', 'Enable verbose mode'
end

# if ARGV is `--name Lee -v`
opts.verbose?  #=> true
opts.password? #=> false
opts[:name]    #=> 'lee'
opts.to_hash   #=> {:name=>"Lee", :password=>nil, :verbose=>true}
```

Installation
------------

    gem install slop

Printing Help
-------------

Slop attempts to build a good looking help string to print to your users. You
can see this by calling `opts.help` or simply `puts opts`.

Configuration Options
---------------------

All of these options can be sent to `Slop.new` or `Slop.parse` in Hash form.

| Option | Description | Default/Example |
| ------ | ----------- | --------------- |
| strict | Enable strict mode. Slop will raise an `InvalidOptionError` for unkown options. | `false` |
| help   | Automatically add the `--help` option. | `false` |
| banner | Set the help banner text. | `nil` |
| ignore_case | When enabled, `-A` will look for the `-a` option if `-A` does not exist. | `false` |
| autocreate | Autocreate options on the fly. | `false` |
| arguments | Force all options to expect arguments. | `false` |
| optional_arguments | Force all options to accept optional arguments. | `false` |
| multiple_switches | When disabled, Slop will parse `-abc` as the option `a` with the argument `bc` rather than 3 separate options. | `true` |

Lists
-----

```ruby
opts = Slop.parse do
  on :list=, as: Array
end
# ruby run.rb --list one,two
opts[:list] #=> ["one", "two"]
# ruby run.rb --list one,two --list three
opts[:list] #=> ["one", "two", "three"]
```

You can also specify a delimiter and limit.

```ruby
opts = Slop.parse do
  on :list=, as: Array, delimiter: ':', limit: 2
end
# ruby run.rb --list one:two:three
opts[:list] #=> ["one", "two:three"]
```

Ranges
------

```ruby
opts = Slop.parse do
  on :range=, as: Range
end
# ruby run.rb --range 1..10
opts[:range] #=> 1..10
# ruby run.rb --range 1...10
opts[:range] #=> 1...10
# ruby run.rb --range 1-10
opts[:range] #=> 1..10
# ruby run.rb --range 1,10
opts[:range] #=> 1..10
```

Autocreate
----------

Slop has an 'autocreate' feature. This feature is intended to create
options on the fly, without having to specify them yourself. In some case,
using this code could be all you need in your application:

```ruby
# ruby run.rb --foo bar --baz --name lee
opts = Slop.parse(autocreate: true)
opts.to_hash #=> {:foo=>"bar", :baz=>true, :name=>"lee"}
opts.fetch_option(:name).expects_argument? #=> true
```

Commands
--------

Slop supports git style sub-commands, like so:

```ruby
opts = Slop.parse do
  on '-v', 'Print the version' do
    puts "Version 1.0"
  end

  command 'add' do
    on :v, :verbose, 'Enable verbose mode'
    on :name=, 'Your name'

    run do |opts, args|
      puts "You ran 'add' with options #{opts.to_hash} and args: #{args.inspect}"
    end
  end
end

# ruby run.rb -v
#=> Version 1.0
# ruby run.rb add -v foo --name Lee
#=> You ran 'add' with options {:verbose=>true,:name=>"Lee"} and args ["foo"]
opts.to_hash(true) # Pass true to tell Slop to merge sub-command option values.
# => { :v => nil, :add => { :v => true, :name => "Lee" } }
```

Remaining arguments
-------------------

The *parse!*  method will remove any options and option arguments from the original Array:

```ruby
# restarguments.rb
opts = Slop.parse! do
  on :foo
end
```

Example:

```
ruby restarguments.rb --foo bar
```

```
opts.to_hash = { :foo => true }

ARGV #=> ["bar"]
```

Woah woah, why you hating on OptionParser?
------------------------------------------

I'm not, honestly! I love OptionParser. I really do, it's a fantastic library.
So why did I build Slop? Well, I find myself using OptionParser to simply
gather a bunch of key/value options, usually you would do something like this:

```ruby
require 'optparse'

things = {}

opt = OptionParser.new do |opt|
  opt.on('-n', '--name NAME', 'Your name') do |name|
    things[:name] = name
  end

  opt.on('-a', '--age AGE', 'Your age') do |age|
    things[:age] = age.to_i
  end

  # you get the point
end

opt.parse
things #=> { :name => 'lee', :age => 105 }
```

Which is all great and stuff, but it can lead to some repetition. The same
thing in Slop:

```ruby
require 'slop'

opts = Slop.parse do
  on :n, :name=, 'Your name'
  on :a, :age=, 'Your age', as: Integer
end

opts.to_hash #=> { :name => 'lee', :age => 105 }
```
# Sprockets: Rack-based asset packaging

Sprockets is a Ruby library for compiling and serving web assets.
It features declarative dependency management for JavaScript and CSS
assets, as well as a powerful preprocessor pipeline that allows you to
write assets in languages like CoffeeScript, Sass and SCSS.


## Installation

Install Sprockets from RubyGems:

``` sh
$ gem install sprockets
```

Or include it in your project's `Gemfile` with Bundler:

``` ruby
gem 'sprockets', '~> 3.0'
```


## Understanding the Sprockets Environment

You'll need an instance of the `Sprockets::Environment` class to
access and serve assets from your application. Under Rails 4.0 and
later, `YourApp::Application.assets` is a preconfigured
`Sprockets::Environment` instance. For Rack-based applications, create
an instance in `config.ru`.

The Sprockets `Environment` has methods for retrieving and serving
assets, manipulating the load path, and registering processors. It is
also a Rack application that can be mounted at a URL to serve assets
over HTTP.

### The Load Path

The *load path* is an ordered list of directories that Sprockets uses
to search for assets.

In the simplest case, a Sprockets environment's load path will consist
of a single directory containing your application's asset source
files. When mounted, the environment will serve assets from this
directory as if they were static files in your public root.

The power of the load path is that it lets you organize your source
files into multiple directories -- even directories that live outside
your application -- and combine those directories into a single
virtual filesystem. That means you can easily bundle JavaScript, CSS
and images into a Ruby library or [Bower](http://bower.io) package and import them into your application.

#### Manipulating the Load Path

To add a directory to your environment's load path, use the
`append_path` and `prepend_path` methods. Directories at the beginning
of the load path have precedence over subsequent directories.

``` ruby
environment = Sprockets::Environment.new
environment.append_path 'app/assets/javascripts'
environment.append_path 'lib/assets/javascripts'
environment.append_path 'vendor/assets/bower_components'
```

In general, you should append to the path by default and reserve
prepending for cases where you need to override existing assets.

### Accessing Assets

Once you've set up your environment's load path, you can mount the
environment as a Rack server and request assets via HTTP. You can also
access assets programmatically from within your application.

#### Logical Paths

Assets in Sprockets are always referenced by their *logical path*.

The logical path is the path of the asset source file relative to its
containing directory in the load path. For example, if your load path
contains the directory `app/assets/javascripts`:

<table>
  <tr>
    <th>Asset source file</th>
    <th>Logical path</th>
  </tr>
  <tr>
    <td>app/assets/javascripts/application.js</td>
    <td>application.js</td>
  </tr>
  <tr>
    <td>app/assets/javascripts/models/project.js</td>
    <td>models/project.js</td>
  </tr>
</table>

In this way, all directories in the load path are merged to create a
virtual filesystem whose entries are logical paths.

#### Serving Assets Over HTTP

When you mount an environment, all of its assets are accessible as
logical paths underneath the *mount point*. For example, if you mount
your environment at `/assets` and request the URL
`/assets/application.js`, Sprockets will search your load path for the
file named `application.js` and serve it.

Under Rails 4.0 and later, your Sprockets environment is automatically
mounted at `/assets`. If you are using Sprockets with a Rack
application, you will need to mount the environment yourself. A good
way to do this is with the `map` method in `config.ru`:

``` ruby
require 'sprockets'
map '/assets' do
  environment = Sprockets::Environment.new
  environment.append_path 'app/assets/javascripts'
  environment.append_path 'app/assets/stylesheets'
  run environment
end

map '/' do
  run YourRackApp
end
```

#### Accessing Assets Programmatically

You can use the `find_asset` method (aliased as `[]`) to retrieve an
asset from a Sprockets environment. Pass it a logical path and you'll
get a `Sprockets::Asset` instance back:

``` ruby
environment['application.js']
# => #<Sprockets::Asset ...>
```

Call `to_s` on the resulting asset to access its contents, `length` to
get its length in bytes, `mtime` to query its last-modified time, and
`filename` to get its full path on the filesystem.


## Using Processors

Asset source files can be written in another format, like SCSS or
CoffeeScript, and automatically compiled to CSS or JavaScript by
Sprockets. Processors that convert a file from one format to another are called *transformers*.

### Minifying Assets

Several JavaScript and CSS minifiers are available through shorthand.

``` ruby
environment.js_compressor  = :uglify
environment.css_compressor = :scss
```

### Styling with Sass and SCSS

[Sass](http://sass-lang.com/) is a language that compiles to CSS and
adds features like nested rules, variables, mixins and selector
inheritance.

If the `sass` gem is available to your application, you can use Sass
to write CSS assets in Sprockets.

Sprockets supports both Sass syntaxes. For the original
whitespace-sensitive syntax, use the extension `.sass`. For the
new SCSS syntax, use the extension `.scss`.

### Scripting with CoffeeScript

[CoffeeScript](http://jashkenas.github.com/coffee-script/) is a
language that compiles to the "good parts" of JavaScript, featuring a
cleaner syntax with array comprehensions, classes, and function
binding.

If the `coffee-script` gem is available to your application, you can
use CoffeeScript to write JavaScript assets in Sprockets. Note that
the CoffeeScript compiler is written in JavaScript, and you will need
an [ExecJS](https://github.com/rails/execjs)-supported runtime
on your system to invoke it.

To write JavaScript assets with CoffeeScript, use the extension
`.coffee`.

### JavaScript Templating with EJS and Eco

Sprockets supports *JavaScript templates* for client-side rendering of
strings or markup. JavaScript templates have the special format
extension `.jst` and are compiled to JavaScript functions.

When loaded, a JavaScript template function can be accessed by its
logical path as a property on the global `JST` object. Invoke a
template function to render the template as a string. The resulting
string can then be inserted into the DOM.

```
<!-- templates/hello.jst.ejs -->
<div>Hello, <span><%= name %></span>!</div>

// application.js
//= require templates/hello
$("#hello").html(JST["templates/hello"]({ name: "Sam" }));
```

Sprockets supports two JavaScript template languages:
[EJS](https://github.com/sstephenson/ruby-ejs), for embedded
JavaScript, and [Eco](https://github.com/sstephenson/ruby-eco), for
embedded CoffeeScript. Both languages use the familiar `<% … %>`
syntax for embedding logic in templates.

If the `ejs` gem is available to your application, you can use EJS
templates in Sprockets. EJS templates have the extension `.jst.ejs`.

If the `eco` gem is available to your application, you can use [Eco
templates](https://github.com/sstephenson/eco) in Sprockets. Eco
templates have the extension `.jst.eco`. Note that the `eco` gem
depends on the CoffeeScript compiler, so the same caveats apply as
outlined above for the CoffeeScript engine.

### Invoking Ruby with ERB

Sprockets provides an ERB engine for preprocessing assets using
embedded Ruby code. Append `.erb` to a CSS or JavaScript asset's
filename to enable the ERB engine.

Ruby code embedded in an asset is evaluated in the context of a
`Sprockets::Context` instance for the given asset. Common uses for ERB
include:

- embedding another asset as a Base64-encoded `data:` URI with the
  `asset_data_uri` helper
- inserting the URL to another asset, such as with the `asset_path`
  helper provided by the Sprockets Rails plugin
- embedding other application resources, such as a localized string
  database, in a JavaScript asset via JSON
- embedding version constants loaded from another file

See the [Helper Methods](lib/sprockets/context.rb) section for more information about
interacting with `Sprockets::Context` instances via ERB.


## Managing and Bundling Dependencies

You can create *asset bundles* -- ordered concatenations of asset
source files -- by specifying dependencies in a special comment syntax
at the top of each source file.

Sprockets reads these comments, called *directives*, and processes
them to recursively build a dependency graph. When you request an
asset with dependencies, the dependencies will be included in order at
the top of the file.

### The Directive Processor

Sprockets runs the *directive processor* on each CSS and JavaScript
source file. The directive processor scans for comment lines beginning
with `=` in comment blocks at the top of the file.

``` js
//= require jquery
//= require jquery-ui
//= require backbone
//= require_tree .
```

The first word immediately following `=` specifies the directive
name. Any words following the directive name are treated as
arguments. Arguments may be placed in single or double quotes if they
contain spaces, similar to commands in the Unix shell.

**Note**: Non-directive comment lines will be preserved in the final
  asset, but directive comments are stripped after
  processing. Sprockets will not look for directives in comment blocks
  that occur after the first line of code.

#### Supported Comment Types

The directive processor understands comment blocks in three formats:

``` css
/* Multi-line comment blocks (CSS, SCSS, JavaScript)
 *= require foo
 */
```

``` js
// Single-line comment blocks (SCSS, JavaScript)
//= require foo
```

``` coffee
# Single-line comment blocks (CoffeeScript)
#= require foo
```

### Sprockets Directives

You can use the following directives to declare dependencies in asset
source files.

For directives that take a *path* argument, you may specify either a
logical path or a relative path. Relative paths begin with `./` and
reference files relative to the location of the current file.

#### The `require` Directive

`require` *path* inserts the contents of the asset source file
specified by *path*. If the file is required multiple times, it will
appear in the bundle only once.

### The `require_directory` Directive ###

`require_directory` *path* requires all source files of the same
format in the directory specified by *path*. Files are required in
alphabetical order.

#### The `require_tree` Directive

`require_tree` *path* works like `require_directory`, but operates
recursively to require all files in all subdirectories of the
directory specified by *path*.

#### The `require_self` Directive

`require_self` tells Sprockets to insert the body of the current
source file before any subsequent `require` directives.

#### The `link` Directive

`link` *path* declares a dependency on the target *path* and adds it to a list
of subdependencies to automatically be compiled when the asset is written out to
disk.

For an example, in a CSS file you might reference an external image that always
needs to be compiled along with the css file.

``` css
/*= link "logo.png" */
.logo {
  background-image: url(logo.png)
}
```

However, if you use a `asset-path` or `asset-url` SCSS helper, these links will
automatically be defined for you.

``` css
.logo {
  background-image: asset-url("logo.png")
}
```

#### The `depend_on` Directive

`depend_on` *path* declares a dependency on the given *path* without
including it in the bundle. This is useful when you need to expire an
asset's cache in response to a change in another file.

#### The `depend_on_asset` Directive

`depend_on_asset` *path* works like `depend_on`, but operates
recursively reading the file and following the directives found. This is automatically implied if you use `link`, so consider if it just makes sense using `link` instead of `depend_on_asset`.

#### The `stub` Directive

`stub` *path* allows dependency to be excluded from the asset bundle.
The *path* must be a valid asset and may or may not already be part
of the bundle. `stub` should only be used at the top level bundle, not
within any subdependencies.


## Processor Interface

Sprockets 2.x was originally design around [Tilt](https://github.com/rtomayko/tilt)'s engine interface. However, starting with 3.x, a new interface has been introduced deprecating Tilt.

Similar to Rack, a processor is a any "callable" (an object that responds to `call`). This maybe a simple Proc or a full class that defines a `def self.call(input)` method. The `call` method accepts an `input` Hash and returns a Hash of metadata.

Also see [`Sprockets::ProcessorUtils`](https://github.com/rails/sprockets/blob/master/lib/sprockets/processor_utils.rb) for public helper methods.

### input Hash

The `input` Hash defines the following public fields.

* `:data` - String asset contents
* `:environment` - Current `Sprockets::Environment` instance.
* `:cache` - A `Sprockets::Cache` instance. See [`Sprockets::Cache#fetch`](https://github.com/rails/sprockets/blob/master/lib/sprockets/cache.rb).
* `:uri` - String Asset URI.
* `:filename` - String full path to original file.
* `:load_path` - String current load path for filename.
* `:name` - String logical path for filename.
* `:content_type` - String content type of the output asset.
* `:metadata` - Hash of processor metadata.

``` ruby
def self.call(input)
  input[:cache].fetch("my:cache:key:v1") do
    # Remove all semicolons from source
    input[:data].gsub(";", "")
  end
end
```

### return Hash

The processor should return metadata `Hash`. With the exception of the `:data` key, the processor can store arbitrary JSON valid values in this Hash. The data will be stored and exposed on `Asset#metadata`.

The returned `:data` replaces the assets `input[:data]` to the next processor in the chain. Returning a `String` is shorthand for returning `{ data: str }`. And returning `nil` is shorthand for a no-op where the input data is not transformed, `{ data: input[:data] }`.

### metadata

The metadata Hash provides an open format for processors to extend the pipeline processor. Internally, built-in processors use it for passing data to each other.

* `:required` - A `Set` of String Asset URIs that the Bundle processor should concatenate together.
* `:stubbed` - A `Set` of String Asset URIs that will be omitted from the `:required` set.
* `:links` - A `Set` of String Asset URIs that should be compiled along with this asset.
* `:dependencies` - A `Set` of String Cache URIs that should be monitored for caching.

``` ruby
def self.call(input)
  # Any metadata may start off as nil, so initialize it the value
  required = Set.new(input[:metadata][:required])

  # Manually add "foo.js" asset uri to our bundle
  required << input[:environment].resolve("foo.js")

  { required: required }
end
```


## Development

### Contributing

The Sprockets source code is [hosted on
GitHub](https://github.com/rails/sprockets). You can check out a
copy of the latest code using Git:

    $ git clone https://github.com/rails/sprockets

If you've found a bug or have a question, please open an issue on the
[Sprockets issue
tracker](https://github.com/rails/sprockets/issues). Or, clone
the Sprockets repository, write a failing test case, fix the bug and
submit a pull request.

### Version History

Please see the [CHANGELOG](https://github.com/rails/sprockets/tree/master/CHANGELOG.md)

## License

Copyright &copy; 2014 Sam Stephenson <<sstephenson@gmail.com>>

Copyright &copy; 2014 Joshua Peek <<josh@joshpeek.com>>

Sprockets is distributed under an MIT-style license. See LICENSE for
details.
# Haml-rails

Haml-rails provides Haml generators for Rails 4. It also enables Haml as the templating engine for you, so you don't have to screw around in your own application.rb when your Gemfile already clearly indicated what templating engine you have installed. Hurrah.

To use it, add this line to your Gemfile:

    gem "haml-rails", "~> 0.9"

This ensures that:

  * Any time you generate a resource, view, or mailer, you'll get Haml templates (instead of ERB)
  * When your Rails application loads, Haml will be loaded and initialized automatically
  * Haml templates will be respected by the view template cache digestor

Pretty fancy, eh? The modern world is just so amazing.

### Converting Rails application layout file to haml format

Once Haml-rails is installed on the Rails application,
you can convert the erb layout file, `app/views/layouts/application.html.erb`
to `app/views/layouts/application.html.haml` using this command:

    $ rails generate haml:application_layout convert

After the application layout file is converted successfully,
make sure to delete `app/views/layouts/application.html.erb`, so Rails can
start using `app/views/layouts/application.html.haml` instead.

### Converting all .erb views to haml format

If you want to convert all of your .erb views into .haml, you can do so using the following command:

    $ rake haml:erb2haml

If you already have .haml files for one or more of the .erb files, the rake task will give you the option of either
replacing these .haml files or leaving them in place.

Once the task is complete, you will have the option of deleting the original .erb files. Unless you are under
version control, it is recommended that you decline this option.

### Older versions of Rails

The current version of Haml-rails requires 4.0.1 or later.

Haml-rails version 0.4 is the last version to support Rails 3. To use it, add this line to your Gemfile:

    gem "haml-rails", "~> 0.4.0"

### Contributors

Haml generators originally from [rails3-generators](http://github.com/indirect/rails3-generators), and written by José Valim, André Arko, Paul Barry, Anuj Dutta, Louis T, and Chris Rhoden. Tests originally written by Louis T.

### Code Status

[![Build Status](https://travis-ci.org/indirect/haml-rails.png)](https://travis-ci.org/indirect/haml-rails)

### License

Ruby license or MIT license, take your pick.
BSON [![Build Status](https://secure.travis-ci.org/durran/optionable.png?branch=master&.png)](http://travis-ci.org/durran/optionable) [![Code Climate](https://codeclimate.com/github/durran/optionable.png)](https://codeclimate.com/github/durran/optionable) [![Coverage Status](https://coveralls.io/repos/durran/optionable/badge.png?branch=master)](https://coveralls.io/r/durran/optionable?branch=master)
====

Robust validation of options passed to Ruby methods.

Compatibility
-------------

BSON is tested against MRI (1.9.2+), JRuby (1.7.0+), Rubinius (2.0.0+).

Installation
------------

With bundler, add the `optionable` gem to your `Gemfile`.

```ruby
gem "optionable",
```

Require the `optionable` gem in your application.

```ruby
require "optionable"
```

Usage
-----

Include the optional module in your object, and use the DSL for define what values
are valid for the specified options. Currently you can match on exact values or
values of a specific type. Then to validate your options, simply call `validate_strict`
and pass it the hash of options.

```ruby
class Parser
  include Optionable

  option(:streaming).allow(true, false)
  option(:timeout).allow(Optionable.any(Integer))

  def initialize(options = {})
    validate_strict(options)
  end
end
```

If the options are invalid, an `Optionable::Invalid` error will be raised.

If an unknown option is provided, an `Optionable::Unknown` error will be
raised.

API Documentation
-----------------

The [API Documentation](http://rdoc.info/github/durran/optionable/master/frames) is
located at rdoc.info.

Versioning
----------

This project adheres to the [Semantic Versioning Specification](http://semver.org/).

License
-------

Copyright (c) 2013 Durran Jordan

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Tilt [![Build Status](https://secure.travis-ci.org/rtomayko/tilt.png)](http://travis-ci.org/rtomayko/tilt) [![Dependency Status](https://gemnasium.com/rtomayko/tilt.png)](https://gemnasium.com/rtomayko/tilt)
====

Tilt is a thin interface over a bunch of different Ruby template engines in
an attempt to make their usage as generic possible. This is useful for web
frameworks, static site generators, and other systems that support multiple
template engines but don't want to code for each of them individually.

The following features are supported for all template engines (assuming the
feature is relevant to the engine):

 * Custom template evaluation scopes / bindings
 * Ability to pass locals to template evaluation
 * Support for passing a block to template evaluation for "yield"
 * Backtraces with correct filenames and line numbers
 * Template file caching and reloading
 * Fast, method-based template source compilation

The primary goal is to get all of the things listed above right for all
template engines included in the distribution.

Support for these template engines is included with the package:

    ENGINE                     FILE EXTENSIONS         REQUIRED LIBRARIES
    -------------------------- ----------------------- ----------------------------
    Asciidoctor                .ad, .adoc, .asciidoc   asciidoctor (>= 0.1.0)
    ERB                        .erb, .rhtml            none (included ruby stdlib)
    Interpolated String        .str                    none (included ruby core)
    Erubis                     .erb, .rhtml, .erubis   erubis
    Haml                       .haml                   haml
    Sass                       .sass                   haml (< 3.1) or sass (>= 3.1)
    Scss                       .scss                   haml (< 3.1) or sass (>= 3.1)
    Less CSS                   .less                   less
    Builder                    .builder                builder
    Liquid                     .liquid                 liquid
    RDiscount                  .markdown, .mkd, .md    rdiscount
    Redcarpet                  .markdown, .mkd, .md    redcarpet
    BlueCloth                  .markdown, .mkd, .md    bluecloth
    Kramdown                   .markdown, .mkd, .md    kramdown
    Maruku                     .markdown, .mkd, .md    maruku
    RedCloth                   .textile                redcloth
    RDoc                       .rdoc                   rdoc
    Radius                     .radius                 radius
    Markaby                    .mab                    markaby
    Nokogiri                   .nokogiri               nokogiri
    CoffeeScript               .coffee                 coffee-script (+ javascript)
    Creole (Wiki markup)       .wiki, .creole          creole
    WikiCloth (Wiki markup)    .wiki, .mediawiki, .mw  wikicloth
    Yajl                       .yajl                   yajl-ruby
    CSV                        .rcsv                   none (Ruby >= 1.9), fastercsv (Ruby < 1.9)

These template engines ship with their own Tilt integration:

    ENGINE                     FILE EXTENSIONS   REQUIRED LIBRARIES
    -------------------------- ----------------- ----------------------------
    Slim                       .slim             slim (>= 0.7)
    Embedded JavaScript                          sprockets
    Embedded CoffeeScript                        sprockets
    JST                                          sprockets
    Org-mode                   .org              org-ruby (>= 0.6.2)

See [TEMPLATES.md][t] for detailed information on template engine
options and supported features.

[t]: http://github.com/rtomayko/tilt/blob/master/TEMPLATES.md
   "Tilt Template Engine Documentation"

Basic Usage
-----------

Instant gratification:

    require 'erb'
    require 'tilt'
    template = Tilt.new('templates/foo.erb')
    => #<Tilt::ERBTemplate @file="templates/foo.rb" ...>
    output = template.render
    => "Hello world!"

It's recommended that calling programs explicitly require template engine
libraries (like 'erb' above) at load time. Tilt attempts to lazy require the
template engine library the first time a template is created but this is
prone to error in threaded environments.

The `Tilt` module contains generic implementation classes for all supported
template engines. Each template class adheres to the same interface for
creation and rendering. In the instant gratification example, we let Tilt
determine the template implementation class based on the filename, but
`Tilt::Template` implementations can also be used directly:

    template = Tilt::HamlTemplate.new('templates/foo.haml')
    output = template.render

The `render` method takes an optional evaluation scope and locals hash
arguments. Here, the template is evaluated within the context of the
`Person` object with locals `x` and `y`:

    template = Tilt::ERBTemplate.new('templates/foo.erb')
    joe = Person.find('joe')
    output = template.render(joe, :x => 35, :y => 42)

If no scope is provided, the template is evaluated within the context of an
object created with `Object.new`.

A single `Template` instance's `render` method may be called multiple times
with different scope and locals arguments. Continuing the previous example,
we render the same compiled template but this time in jane's scope:

    jane = Person.find('jane')
    output = template.render(jane, :x => 22, :y => nil)

Blocks can be passed to `render` for templates that support running
arbitrary ruby code (usually with some form of `yield`). For instance,
assuming the following in `foo.erb`:

    Hey <%= yield %>!

The block passed to `render` is called on `yield`:

    template = Tilt::ERBTemplate.new('foo.erb')
    template.render { 'Joe' }
    # => "Hey Joe!"

Template Mappings
-----------------

The `Tilt` module includes methods for associating template implementation
classes with filename patterns and for locating/instantiating template
classes based on those associations.

The `Tilt::register` method associates a filename pattern with a specific
template implementation. To use ERB for files ending in a `.bar` extension:

     >> Tilt.register Tilt::ERBTemplate, 'bar'
     >> Tilt.new('views/foo.bar')
     => #<Tilt::ERBTemplate @file="views/foo.bar" ...>

Retrieving the template class for a file or file extension:

     >> Tilt['foo.bar']
     => Tilt::ERBTemplate
     >> Tilt['haml']
     => Tilt::HamlTemplate

It's also possible to register template file mappings that are more specific
than a file extension. To use Erubis for `bar.erb` but ERB for all other `.erb`
files:

     >> Tilt.register Tilt::ErubisTemplate, 'bar.erb'
     >> Tilt.new('views/foo.erb')
     => Tilt::ERBTemplate
     >> Tilt.new('views/bar.erb')
     => Tilt::ErubisTemplate

The template class is determined by searching for a series of decreasingly
specific name patterns. When creating a new template with
`Tilt.new('views/foo.html.erb')`, we check for the following template
mappings:

  1. `views/foo.html.erb`
  2. `foo.html.erb`
  3. `html.erb`
  4. `erb`

### Fallback mode

If there are more than one template class registered for a file extension, Tilt
will automatically try to load the version that works on your machine:

  1. If any of the template engines has been loaded already: Use that one.
  2. If not, it will try to initialize each of the classes with an empty template.
  3. Tilt will use the first that doesn't raise an exception.
  4. If however *all* of them failed, Tilt will raise the exception of the first
     template engine, since that was the most preferred one.

Template classes that were registered *last* would be tried first. Because the
Markdown extensions are registered like this:

    Tilt.register Tilt::BlueClothTemplate, 'md'
    Tilt.register Tilt::RDiscountTemplate, 'md'

Tilt will first try RDiscount and then BlueCloth. You could say that RDiscount
has a *higher priority* than BlueCloth.

The fallback mode works nicely when you just need to render an ERB or Markdown
template, but if you depend on a specific implementation, you should use #prefer:

    # Prefer BlueCloth for all its registered extensions (markdown, mkd, md)
    Tilt.prefer Tilt::BlueClothTemplate

    # Prefer Erubis for .erb only:
    Tilt.prefer Tilt::ErubisTemplate, 'erb'

When a file extension has a preferred template class, Tilt will *always* use
that class, even if it raises an exception.

Encodings
---------

Tilt needs to know the encoding of the template in order to work properly:

Tilt will use `Encoding.default_external` as the encoding when reading external
files. If you're mostly working with one encoding (e.g. UTF-8) we *highly*
recommend setting this option. When providing a custom reader block (`Tilt.new
{ custom_string }`) you'll have ensure the string is properly encoded yourself.

Most of the template engines in Tilt also allows you to override the encoding
using the `:default_encoding`-option:

```ruby
tmpl = Tilt.new('hello.erb', :default_encoding => 'Big5')
```

Ultimately it's up to the template engine how to handle the encoding: It might
respect `:default_encoding`, it might always assume it's UTF-8 (like
CoffeScript), or it can do its own encoding detection.

Template Compilation
--------------------

Tilt compiles generated Ruby source code produced by template engines and reuses
it on subsequent template invocations. Benchmarks show this yields a 5x-10x
performance increase over evaluating the Ruby source on each invocation.

Template compilation is currently supported for these template engines:
StringTemplate, ERB, Erubis, Haml, Nokogiri, Builder and Yajl.

LICENSE
-------

Tilt is Copyright (c) 2010 [Ryan Tomayko](http://tomayko.com/about) and
distributed under the MIT license. See the `COPYING` file for more info.
# Foreman

[![Build Status](https://travis-ci.org/ddollar/foreman.svg?branch=master)](https://travis-ci.org/ddollar/foreman)
[![Code Climate](https://codeclimate.com/github/ddollar/foreman.png)](https://codeclimate.com/github/ddollar/foreman)
[![Inline docs](http://inch-ci.org/github/ddollar/foreman.svg?branch=master)](http://inch-ci.org/github/ddollar/foreman)

Manage Procfile-based applications

<table>
  <tr>
    <th>If you have...</th>
    <th>Install with...</th>
  </tr>
  <tr>
    <td>Ruby (MRI, JRuby, Windows)</td>
    <td><pre>$ gem install foreman</pre></td>
  </tr>
  <tr>
    <td>Mac OS X</td>
    <td><a href="http://assets.foreman.io/foreman/foreman.pkg">foreman.pkg</a></td>
  </tr>
</table>

## Installation

    $ gem install foreman

Ruby users should take care *not* to install foreman in their project's `Gemfile`.

## Getting Started

* http://blog.daviddollar.org/2011/05/06/introducing-foreman.html

## Supported Ruby versions

See [.travis.yml](.travis.yml) for a list of Ruby versions against which Foreman is tested.

## Documentation

* [man page](http://ddollar.github.com/foreman)
* [wiki](http://github.com/ddollar/foreman/wiki)
* [changelog](https://github.com/ddollar/foreman/blob/master/Changelog.md)

## Ports

* [forego](https://github.com/ddollar/forego) - Go
* [gaffer](https://github.com/jingweno/gaffer) - Java/JVM
* [honcho](https://github.com/nickstenning/honcho) - python
* [proclet](https://github.com/kazeburo/Proclet) - Perl
* [shoreman](https://github.com/hecticjeff/shoreman) - shell

## Authors

#### Created and maintained by
David Dollar

#### Patches contributed by
[Contributor List](https://github.com/ddollar/foreman/contributors)

## License

Foreman is licensed under the MIT license.

See LICENSE for the full license text.
method_source
=============

(C) John Mair (banisterfiend) 2011

_retrieve the sourcecode for a method_

*NOTE:* This simply utilizes `Method#source_location`; it
 does not access the live AST.

`method_source` is a utility to return a method's sourcecode as a
Ruby string. Also returns `Proc` and `Lambda` sourcecode.

Method comments can also be extracted using the `comment` method.

It is written in pure Ruby (no C).

* Some Ruby 1.8 support now available.
* Support for MRI, RBX, JRuby, REE

`method_source` provides the `source` and `comment` methods to the `Method` and
`UnboundMethod` and `Proc` classes.

* Install the [gem](https://rubygems.org/gems/method_source): `gem install method_source`
* Read the [documentation](http://rdoc.info/github/banister/method_source/master/file/README.markdown)
* See the [source code](http://github.com/banister/method_source)

Example: display method source
------------------------------

    Set.instance_method(:merge).source.display
    # =>
    def merge(enum)
      if enum.instance_of?(self.class)
        @hash.update(enum.instance_variable_get(:@hash))
      else
        do_with_enum(enum) { |o| add(o) }
      end

      self
    end

Example: display method comments
--------------------------------

    Set.instance_method(:merge).comment.display
    # =>
    # Merges the elements of the given enumerable object to the set and
    # returns self.

Limitations:
------------

* Occasional strange behaviour in Ruby 1.8
* Cannot return source for C methods.
* Cannot return source for dynamically defined methods.

Special Thanks
--------------

[Adam Sanderson](https://github.com/adamsanderson) for `comment` functionality.

[Dmitry Elastic](https://github.com/dmitryelastic) for the brilliant Ruby 1.8 `source_location` hack.

[Samuel Kadolph](https://github.com/samuelkadolph) for the JRuby 1.8 `source_location`.

License
-------

(The MIT License)

Copyright (c) 2011 John Mair (banisterfiend)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# SDoc

[![Build Status](https://travis-ci.org/zzak/sdoc.png?branch=master)](https://travis-ci.org/zzak/sdoc)

**Powering http://api.rubyonrails.org/ and http://railsapi.com/**

### What is sdoc?

RDoc generator to build searchable HTML documentation for Ruby code.

* `sdoc` - command line tool to run rdoc with `generator=shtml` (searchable HTML)
* `sdoc-merge` - command line tool to merge multiple sdoc folders into a single documentation site


### Getting Started

```bash
  # Install the gem
  gem install sdoc

  # Generate documentation for 'projectdir'
  sdoc projectdir
```

### sdoc

`sdoc` is simply a wrapper for the `rdoc` command line tool. See `sdoc --help`
for more details. `--fmt` is set to `shtml` by default. The default template `-T` is `shtml`, but you can also use the `direct` template.

Example:

```bash
sdoc -o doc/rails -T direct rails
```

### sdoc-merge

<pre>
Usage: sdoc-merge [options] directories
    -n, --names [NAMES]              Names of merged repositories. Comma separated
    -o, --op [DIRECTORY]             Set the output directory
    -t, --title [TITLE]              Set the title of merged file
</pre>

Example:

```bash
sdoc-merge --title "Ruby v1.9, Rails v2.3.2.1" --op merged --names "Ruby,Rails" ruby-v1.9 rails-v2.3.2.1
```

### Rake Task

```ruby
# Rakefile
require 'sdoc' # and use your RDoc task the same way you used it before

Rake::RDocTask.new do |rdoc|
  rdoc.rdoc_dir = 'doc/rdoc'
  rdoc.options << '--fmt' << 'shtml' # explictly set shtml generator
  rdoc.template = 'direct' # lighter template used on railsapi.com
  ...
end
```

# Who?

* Vladimir Kolesnikov ([voloko](https://github.com/voloko))
* Nathan Broadbent ([ndbroadbent](https://github.com/ndbroadbent))
* Zachary Scott ([zzak](https://github.com/zzak))
= Nokogiri {<img src="https://secure.travis-ci.org/sparklemotion/nokogiri.png?rvm=1.9.3" />}[http://travis-ci.org/sparklemotion/nokogiri] {<img src="https://codeclimate.com/github/sparklemotion/nokogiri.png" />}[https://codeclimate.com/github/sparklemotion/nokogiri] {<img src="https://www.versioneye.com/ruby/nokogiri/badge.png" alt="Dependency Status" />}[https://www.versioneye.com/ruby/nokogiri]

* http://nokogiri.org
* https://github.com/sparklemotion/nokogiri
* https://groups.google.com/group/nokogiri-talk
* https://github.com/sparklemotion/nokogiri/issues

== DESCRIPTION:

Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.

XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.

== FEATURES:

* XPath 1.0 support for document searching
* CSS3 selector support for document searching
* XML/HTML builder

Nokogiri parses and searches XML/HTML very quickly, and also has
correctly implemented CSS3 selector support as well as XPath 1.0 support.

== SUPPORT:

Before filing a bug report, please read our {submission guidelines}[http://nokogiri.org/tutorials/getting_help.html] at:

  * http://nokogiri.org/tutorials/getting_help.html

The Nokogiri {mailing list}[https://groups.google.com/group/nokogiri-talk]
is available here:

  * https://groups.google.com/group/nokogiri-talk

The {bug tracker}[https://github.com/sparklemotion/nokogiri/issues]
is available here:

  * https://github.com/sparklemotion/nokogiri/issues

The IRC channel is #nokogiri on freenode.

== SYNOPSIS:

  require 'nokogiri'
  require 'open-uri'

  # Fetch and parse HTML document
  doc = Nokogiri::HTML(open('http://www.nokogiri.org/tutorials/installing_nokogiri.html'))

  ####
  # Search for nodes by css
  doc.css('nav ul.menu li a').each do |link|
    puts link.content
  end

  ####
  # Search for nodes by xpath
  doc.xpath('//h2 | //h3').each do |link|
    puts link.content
  end

  ####
  # Or mix and match.
  doc.search('code.sh', '//h2').each do |link|
    puts link.content
  end


== REQUIREMENTS:

* ruby 1.9.3 or higher

* in Nokogiri 1.6.0 and later libxml2 and libxslt are bundled with the
  gem, but if you want to use them installed on the system:

  * libxml2 >=2.6.21 with iconv support
    (libxml2-dev/-devel is required too)

  * libxslt, built with and supported by the given libxml2
    (libxslt-dev/-devel is required too)

== ENCODING:

Strings are always stored as UTF-8 internally.  Methods that return
text values will always return UTF-8 encoded strings.  Methods that
return XML (like to_xml, to_html and inner_html) will return a string
encoded like the source document.

*WARNING*

Some documents declare one particular encoding, but use a different
one. So, which encoding should the parser choose?

Remember that data is just a stream of bytes. Only we humans add
meaning to that stream. Any particular set of bytes could be valid
characters in multiple encodings, so detecting encoding with 100%
accuracy is not possible. libxml2 does its best, but it can't be right
100% of the time.

If you want Nokogiri to handle the document encoding properly, your
best bet is to explicitly set the encoding.  Here is an example of
explicitly setting the encoding to EUC-JP on the parser:

    doc = Nokogiri.XML('<foo><bar /><foo>', nil, 'EUC-JP')

== INSTALL:

* sudo gem install nokogiri

=== Binary packages

Binary packages are available for:

* SuSE[https://download.opensuse.org/repositories/devel:/languages:/ruby:/extensions/]
* Fedora[http://s390.koji.fedoraproject.org/koji/packageinfo?packageID=6756]

== DEVELOPMENT:

=== Developing on C Ruby (MRI)

Developing Nokogiri requires racc and rexical to generate the parser and
tokenizer.  To start development, make sure you have `libxml2` and `libxslt`
installed.

Then install core gems and bootstrap:

    $ gem install hoe rake-compiler mini_portile
    $ rake newb

=== Developing on JRuby

Currently, development with JRuby depends on CRuby being installed.  With
CRuby, install racc and rexical:

    $ gem install racc rexical

Make sure hoe and rake compiler are installed with JRuby:

    $ jgem install hoe rake-compiler

Then run rake:

    $ jruby -S rake

== LICENSE:

(The MIT License)

Copyright (c) 2008 - 2015:

* {Aaron Patterson}[http://tenderlovemaking.com]
* {Mike Dalessio}[http://mike.daless.io]
* {Charles Nutter}[http://blog.headius.com]
* {Sergio Arbeo}[http://www.serabe.com]
* {Patrick Mahoney}[http://polycrystal.org]
* {Yoko Harada}[http://yokolet.blogspot.com]
* {Akinori MUSHA}[https://akinori.org]

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
= Nokogiri (鋸) {<img src="https://secure.travis-ci.org/sparklemotion/nokogiri.png?rvm=1.9.3" />}[http://travis-ci.org/sparklemotion/nokogiri] {<img src="https://codeclimate.com/badge.png" />}[https://codeclimate.com/github/sparklemotion/nokogiri]

* http://nokogiri.org
* https://github.com/sparklemotion/nokogiri
* https://groups.google.com/group/nokogiri-talk
* https://github.com/sparklemotion/nokogiri/issues

== DESCRIPTION:

Nokogiri はHTMLとXMLとSAXとXSLTとReaderのパーサーです。とりわけ重要な特徴は、
ドキュメントをXPathやCSS3セレクター経由で探索する機能を持つことです。

XMLは暴力に似ている - XMLが君の問題を解決しないとしたら、君はXMLを十分に
使いこなしていない事になる。

== FEATURES:

* XPath 1.0による探索
* CSS3 のセレクターによる探索
* XML/HTMLのビルダー

XML/HTMLの高速な解析と探索検索、ならびにCSS3セレクタとXPath 1.0をサポートしています。

== SUPPORT:

日本語でNokogiriの
{メーリングリスト}[https://groups.google.com/group/nokogiri-list]

  * https://groups.google.com/group/nokogiri-list

{バグ報告}[https://github.com/sparklemotion/nokogiri/issues]

  * https://github.com/sparklemotion/nokogiri/issues

IRCのチャンネルはfreenodeの #nokogiri です。

== SYNOPSIS:

  require 'nokogiri'
  require 'open-uri'

  # Fetch and parse HTML document
  doc = Nokogiri::HTML(open('http://www.nokogiri.org/tutorials/installing_nokogiri.html'))

  ####
  # Search for nodes by css
  doc.css('nav ul.menu li a').each do |link|
    puts link.content
  end

  ####
  # Search for nodes by xpath
  doc.xpath('//h2 | //h3').each do |link|
    puts link.content
  end

  ####
  # Or mix and match.
  doc.search('code.sh', '//h2').each do |link|
    puts link.content
  end


== REQUIREMENTS:

* ruby 1.9.3以上

* Nokogiri 1.6.0以降ではlibxml2とlibxsltは同梱されているが、
  もしインストール済みのものを使いたい場合:

  * libxml2 2.6.21以上, iconvサポート付きのもの
    (libxml2-dev/-develパッケージも必要)

  * libxslt 上記のlibxml2でビルドされ、サポートされているもの
    (libxslt-dev/-develパッケージも必要)

== INSTALL:

* sudo gem install nokogiri

== LICENSE:

(The MIT License)

Copyright (c) 2008 - 2015:

* {Aaron Patterson}[http://tenderlovemaking.com]
* {Mike Dalessio}[http://mike.daless.io]
* {Charles Nutter}[http://blog.headius.com]
* {Sergio Arbeo}[http://www.serabe.com]
* {Patrick Mahoney}[http://polycrystal.org]
* {Yoko Harada}[http://yokolet.blogspot.com]
* {Akinori MUSHA}[https://akinori.org]

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
This directory contains valgrind suppression files generated by the hoe-debugging gem.
= net-http-digest_auth

code  :: http://github.com/drbrain/net-http-digest_auth
rdoc  :: http://docs.seattlerb.org/net-http-digest_auth
other :: http://www.rfc-editor.org/rfc/rfc2617.txt

== DESCRIPTION:

An implementation of RFC 2617 - Digest Access Authentication.  At this time
the gem does not drop in to Net::HTTP and can be used for with other HTTP
clients.

In order to use net-http-digest_auth you'll need to perform some request
wrangling on your own.  See the class documentation at Net::HTTP::DigestAuth
for an example.

== INSTALL:

  gem install net-http-digest_auth

== LICENSE:

(The MIT License)

Copyright (c) Eric Hodel

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
= ruby_parser

home :: https://github.com/seattlerb/ruby_parser
bugs :: https://github.com/seattlerb/ruby_parser/issues
rdoc :: http://docs.seattlerb.org/ruby_parser

== DESCRIPTION:

ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc--which does by default use a C extension). RP's output is
the same as ParseTree's output: s-expressions using ruby's arrays and
base types.

As an example:

    def conditional1 arg1
      return 1 if arg1 == 0
      return 0
    end

becomes:

    s(:defn, :conditional1, s(:args, :arg1),
      s(:if,
        s(:call, s(:lvar, :arg1), :==, s(:lit, 0)),
        s(:return, s(:lit, 1)),
        nil),
      s(:return, s(:lit, 0)))

Tested against 801,039 files from the latest of all rubygems (as of 2013-05):

* 1.8 parser is at 99.9739% accuracy, 3.651 sigma
* 1.9 parser is at 99.9940% accuracy, 4.013 sigma
* 2.0 parser is at 99.9939% accuracy, 4.008 sigma

== FEATURES/PROBLEMS:

* Pure ruby, no compiles.
* Includes preceding comment data for defn/defs/class/module nodes!
* Incredibly simple interface.
* Output is 100% equivalent to ParseTree.
  * Can utilize PT's SexpProcessor and UnifiedRuby for language processing.
* Known Issue: Speed is now pretty good, but can always improve:
  * RP parses a corpus of 3702 files in 125s (avg 108 Kb/s)
  * MRI+PT parsed the same in 67.38s (avg 200.89 Kb/s)
* Known Issue: Code is much better, but still has a long way to go.
* Known Issue: Totally awesome.
* Known Issue: line number values can be slightly off. Parsing LR sucks.

== SYNOPSIS:

  RubyParser.new.parse "1+1"
  # => s(:call, s(:lit, 1), :+, s(:lit, 1))

You can also use Ruby19Parser, Ruby18Parser, or RubyParser.for_current_ruby:

  RubyParser.for_current_ruby.parse "1+1"
  # => s(:call, s(:lit, 1), :+, s(:lit, 1))

== REQUIREMENTS:

* ruby. woot.
* sexp_processor for Sexp and SexpProcessor classes, and testing.
* racc full package for parser development (compiling .y to .rb).

== INSTALL:

* sudo gem install ruby_parser

== LICENSE:

(The MIT License)

Copyright (c) Ryan Davis, seattle.rb

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Mail [![Build Status](https://travis-ci.org/mikel/mail.png?branch=master)](https://travis-ci.org/mikel/mail)
====

Introduction
------------

Mail is an internet library for Ruby that is designed to handle emails
generation, parsing and sending in a simple, rubyesque manner.

The purpose of this library is to provide a single point of access to handle
all email functions, including sending and receiving emails.  All network
type actions are done through proxy methods to Net::SMTP, Net::POP3 etc.

Built from my experience with TMail, it is designed to be a pure ruby
implementation that makes generating, sending and parsing emails a no
brainer.

It is also designed from the ground up to work with the more modern versions
of Ruby.  This is because Ruby > 1.9 handles text encodings much more wonderfully
than Ruby 1.8.x and so these features have been taken full advantage of in this
library allowing Mail to handle a lot more messages more cleanly than TMail.
Mail does run on Ruby 1.8.x... it's just not as fun to code.

Finally, Mail has been designed with a very simple object oriented system
that really opens up the email messages you are parsing, if you know what
you are doing, you can fiddle with every last bit of your email directly.

Donations
-------------

Mail has been downloaded millions of times, by people around the world, in fact,
it represents more than 1% of *all* gems downloaded.

It is (like all open source software) a labour of love and something I am doing
with my own free time.  If you would like to say thanks, please feel free to
[make a donation](http://www.pledgie.com/campaigns/8790) and feel free to send
me a nice email :)

<a href='http://www.pledgie.com/campaigns/8790'><img alt='Click here to lend your support to: mail and make a donation at www.pledgie.com !' src='http://www.pledgie.com/campaigns/8790.png?skin_name=chrome' border='0' /></a>


Compatibility
-------------

Every Mail commit is tested by Travis on the [following platforms](https://github.com/mikel/mail/blob/master/.travis.yml)

* ruby-1.8.7 [ i686 ]
* ruby-1.9.2 [ x86_64 ]
* ruby-1.9.3 [ x86_64 ]
* ruby-2.0.0 [ x86_64 ]
* ruby-2.1.2 [ x86_64 ]
* ruby-head [ x86_64 ]
* jruby [ x86_64 ]
* jruby-head [ x86_64 ]
* rbx-2 [ x86_64 ]

Testing a specific mime type (needed for 1.8.7 for example) can be done manually with:

```sh
BUNDLE_GEMFILE=gemfiles/mime_types_1.16.gemfile (bundle check || bundle) && rake
```

Discussion
----------

If you want to discuss mail with like minded individuals, please subscribe to
the [Google Group](http://groups.google.com/group/mail-ruby).

Current Capabilities of Mail
----------------------------

* RFC2822 Support, Reading and Writing
* RFC2045-2049 Support for multipart emails
* Support for creating multipart alternate emails
* Support for reading multipart/report emails &amp; getting details from such
* Support for multibyte emails - needs quite a lot of work and testing
* Wrappers for File, Net/POP3, Net/SMTP
* Auto encoding of non US-ASCII header fields
* Auto encoding of non US-ASCII bodies

Mail is RFC2822 compliant now, that is, it can parse and generate valid US-ASCII
emails.  There are a few obsoleted syntax emails that it will have problems with, but
it also is quite robust, meaning, if it finds something it doesn't understand it will
not crash, instead, it will skip the problem and keep parsing.  In the case of a header
it doesn't understand, it will initialise the header as an optional unstructured
field and continue parsing.

This means Mail won't (ever) crunch your data (I think).

You can also create MIME emails.  There are helper methods for making a
multipart/alternate email for text/plain and text/html (the most common pair)
and you can manually create any other type of MIME email.

Roadmap
-------

Next TODO:

* Improve MIME support for character sets in headers, currently works, mostly, needs
  refinement.

Testing Policy
--------------

Basically... we do BDD on Mail.  No method gets written in Mail without a
corresponding or covering spec.  We expect as a minimum 100% coverage
measured by RCov.  While this is not perfect by any measure, it is pretty
good.  Additionally, all functional tests from TMail are to be passing before
the gem gets released.

It also means you can be sure Mail will behave correctly.

API Policy
----------

No API removals within a single point release.  All removals to be deprecated with
warnings for at least one MINOR point release before removal.

Also, all private or protected methods to be declared as such - though this is still I/P.

Installation
------------

Installation is fairly simple, I host mail on rubygems, so you can just do:

    # gem install mail

Encodings
---------

If you didn't know, handling encodings in Emails is not as straight forward as you
would hope.

I have tried to simplify it some:

1. All objects that can render into an email, have an `#encoded` method.  Encoded will
   return the object as a complete string ready to send in the mail system, that is,
   it will include the header field and value and CRLF at the end and wrapped as
   needed.

2. All objects that can render into an email, have a `#decoded` method.  Decoded will
   return the object's "value" only as a string.  This means it will not include
   the header fields (like 'To:' or 'Subject:').

3. By default, calling <code>#to_s</code> on a container object will call its encoded
   method, while <code>#to_s</code> on a field object will call its decoded method.
   So calling <code>#to_s</code> on a Mail object will return the mail, all encoded
   ready to send, while calling <code>#to_s</code> on the From field or the body will
   return the decoded value of the object. The header object of Mail is considered a
   container. If you are in doubt, call <code>#encoded</code>, or <code>#decoded</code>
   explicitly, this is safer if you are not sure.

4. Structured fields that have parameter values that can be encoded (e.g. Content-Type) will
   provide decoded parameter values when you call the parameter names as methods against
   the object.

5. Structured fields that have parameter values that can be encoded (e.g. Content-Type) will
   provide encoded parameter values when you call the parameter names through the
   <code>object.parameters['<parameter_name>']</code> method call.

Contributing
------------

Please do!  Contributing is easy in Mail.  Please read the CONTRIBUTING.md document for more info

Usage
-----

All major mail functions should be able to happen from the Mail module.
So, you should be able to just <code>require 'mail'</code> to get started.

### Making an email

```ruby
mail = Mail.new do
  from    'mikel@test.lindsaar.net'
  to      'you@test.lindsaar.net'
  subject 'This is a test email'
  body    File.read('body.txt')
end

mail.to_s #=> "From: mikel@test.lindsaar.net\r\nTo: you@...
```

### Making an email, have it your way:

```ruby
mail = Mail.new do
  body File.read('body.txt')
end

mail['from'] = 'mikel@test.lindsaar.net'
mail[:to]    = 'you@test.lindsaar.net'
mail.subject = 'This is a test email'

mail.header['X-Custom-Header'] = 'custom value'

mail.to_s #=> "From: mikel@test.lindsaar.net\r\nTo: you@...
```

### Don't Worry About Message IDs:

```ruby
mail = Mail.new do
  to   'you@test.lindsaar.net'
  body 'Some simple body'
end

mail.to_s =~ /Message\-ID: <[\d\w_]+@.+.mail/ #=> 27
```

Mail will automatically add a Message-ID field if it is missing and
give it a unique, random Message-ID along the lines of:

    <4a7ff76d7016_13a81ab802e1@local.host.mail>

### Or do worry about Message-IDs:

```ruby
mail = Mail.new do
  to         'you@test.lindsaar.net'
  message_id '<ThisIsMyMessageId@some.domain.com>'
  body       'Some simple body'
end

mail.to_s =~ /Message\-ID: <ThisIsMyMessageId@some.domain.com>/ #=> 27
```

Mail will take the message_id you assign to it trusting that you know
what you are doing.

### Sending an email:

Mail defaults to sending via SMTP to local host port 25.  If you have a
sendmail or postfix daemon running on on this port, sending email is as
easy as:

```ruby
Mail.deliver do
  from     'me@test.lindsaar.net'
  to       'you@test.lindsaar.net'
  subject  'Here is the image you wanted'
  body     File.read('body.txt')
  add_file '/full/path/to/somefile.png'
end
```

or

```ruby
mail = Mail.new do
  from     'me@test.lindsaar.net'
  to       'you@test.lindsaar.net'
  subject  'Here is the image you wanted'
  body     File.read('body.txt')
  add_file :filename => 'somefile.png', :content => File.read('/somefile.png')
end

mail.deliver!
```

Sending via sendmail can be done like so:

```ruby
mail = Mail.new do
  from     'me@test.lindsaar.net'
  to       'you@test.lindsaar.net'
  subject  'Here is the image you wanted'
  body     File.read('body.txt')
  add_file :filename => 'somefile.png', :content => File.read('/somefile.png')
end

mail.delivery_method :sendmail

mail.deliver
```

Sending via smtp (for example to [mailcatcher](https://github.com/sj26/mailcatcher))
```ruby

Mail.defaults do
  delivery_method :smtp, address: "localhost", port: 1025
end
```


Exim requires its own delivery manager, and can be used like so:

```ruby
mail.delivery_method :exim, :location => "/usr/bin/exim"

mail.deliver
```

### Getting emails from a pop server:

You can configure Mail to receive email using <code>retriever_method</code>
within <code>Mail.defaults</code>:

```ruby
Mail.defaults do
  retriever_method :pop3, :address    => "pop.gmail.com",
                          :port       => 995,
                          :user_name  => '<username>',
                          :password   => '<password>',
                          :enable_ssl => true
end
```

You can access incoming email in a number of ways.

The most recent email:

```ruby
Mail.all    #=> Returns an array of all emails
Mail.first  #=> Returns the first unread email
Mail.last   #=> Returns the last unread email
```

The first 10 emails sorted by date in ascending order:

```ruby
emails = Mail.find(:what => :first, :count => 10, :order => :asc)
emails.length #=> 10
```

Or even all emails:

```ruby
emails = Mail.all
emails.length #=> LOTS!
```


### Reading an Email

```ruby
mail = Mail.read('/path/to/message.eml')

mail.envelope_from   #=> 'mikel@test.lindsaar.net'
mail.from.addresses  #=> ['mikel@test.lindsaar.net', 'ada@test.lindsaar.net']
mail.sender.address  #=> 'mikel@test.lindsaar.net'
mail.to              #=> 'bob@test.lindsaar.net'
mail.cc              #=> 'sam@test.lindsaar.net'
mail.subject         #=> "This is the subject"
mail.date.to_s       #=> '21 Nov 1997 09:55:06 -0600'
mail.message_id      #=> '<4D6AA7EB.6490534@xxx.xxx>'
mail.body.decoded    #=> 'This is the body of the email...
```

Many more methods available.

### Reading a Multipart Email

```ruby
mail = Mail.read('multipart_email')

mail.multipart?          #=> true
mail.parts.length        #=> 2
mail.body.preamble       #=> "Text before the first part"
mail.body.epilogue       #=> "Text after the last part"
mail.parts.map { |p| p.content_type }  #=> ['text/plain', 'application/pdf']
mail.parts.map { |p| p.class }         #=> [Mail::Message, Mail::Message]
mail.parts[0].content_type_parameters  #=> {'charset' => 'ISO-8859-1'}
mail.parts[1].content_type_parameters  #=> {'name' => 'my.pdf'}
```

Mail generates a tree of parts.  Each message has many or no parts.  Each part
is another message which can have many or no parts.

A message will only have parts if it is a multipart/mixed or multipart/related
content type and has a boundary defined.

### Testing and extracting attachments
```ruby
mail.attachments.each do | attachment |
  # Attachments is an AttachmentsList object containing a
  # number of Part objects
  if (attachment.content_type.start_with?('image/'))
    # extracting images for example...
    filename = attachment.filename
    begin
      File.open(images_dir + filename, "w+b", 0644) {|f| f.write attachment.body.decoded}
    rescue => e
      puts "Unable to save data for #{filename} because #{e.message}"
    end
  end
end
```
### Writing and sending a multipart/alternative (html and text) email

Mail makes some basic assumptions and makes doing the common thing as
simple as possible.... (asking a lot from a mail library)

```ruby
mail = Mail.deliver do
  to      'nicolas@test.lindsaar.net.au'
  from    'Mikel Lindsaar <mikel@test.lindsaar.net.au>'
  subject 'First multipart email sent with Mail'

  text_part do
    body 'This is plain text'
  end

  html_part do
    content_type 'text/html; charset=UTF-8'
    body '<h1>This is HTML</h1>'
  end
end
```

Mail then delivers the email at the end of the block and returns the
resulting Mail::Message object, which you can then inspect if you
so desire...

```
puts mail.to_s #=>

To: nicolas@test.lindsaar.net.au
From: Mikel Lindsaar <mikel@test.lindsaar.net.au>
Subject: First multipart email sent with Mail
Content-Type: multipart/alternative;
  boundary=--==_mimepart_4a914f0c911be_6f0f1ab8026659
Message-ID: <4a914f12ac7e_6f0f1ab80267d1@baci.local.mail>
Date: Mon, 24 Aug 2009 00:15:46 +1000
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit


----==_mimepart_4a914f0c911be_6f0f1ab8026659
Content-ID: <4a914f12c8c4_6f0f1ab80268d6@baci.local.mail>
Date: Mon, 24 Aug 2009 00:15:46 +1000
Mime-Version: 1.0
Content-Type: text/plain
Content-Transfer-Encoding: 7bit

This is plain text
----==_mimepart_4a914f0c911be_6f0f1ab8026659
Content-Type: text/html; charset=UTF-8
Content-ID: <4a914f12cf86_6f0f1ab802692c@baci.local.mail>
Date: Mon, 24 Aug 2009 00:15:46 +1000
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit

<h1>This is HTML</h1>
----==_mimepart_4a914f0c911be_6f0f1ab8026659--
```

Mail inserts the content transfer encoding, the mime version,
the content-id's and handles the content-type and boundary.

Mail assumes that if your text in the body is only us-ascii, that your
transfer encoding is 7bit and it is text/plain.  You can override this
by explicitly declaring it.

### Making Multipart/Alternate, without a block

You don't have to use a block with the text and html part included, you
can just do it declaratively.  However, you need to add Mail::Parts to
an email, not Mail::Messages.

```ruby
mail = Mail.new do
  to      'nicolas@test.lindsaar.net.au'
  from    'Mikel Lindsaar <mikel@test.lindsaar.net.au>'
  subject 'First multipart email sent with Mail'
end

text_part = Mail::Part.new do
  body 'This is plain text'
end

html_part = Mail::Part.new do
  content_type 'text/html; charset=UTF-8'
  body '<h1>This is HTML</h1>'
end

mail.text_part = text_part
mail.html_part = html_part
```

Results in the same email as done using the block form

### Getting error reports from an email:

```ruby
@mail = Mail.read('/path/to/bounce_message.eml')

@mail.bounced?         #=> true
@mail.final_recipient  #=> rfc822;mikel@dont.exist.com
@mail.action           #=> failed
@mail.error_status     #=> 5.5.0
@mail.diagnostic_code  #=> smtp;550 Requested action not taken: mailbox unavailable
@mail.retryable?       #=> false
```

### Attaching and Detaching Files

You can just read the file off an absolute path, Mail will try
to guess the mime_type and will encode the file in Base64 for you.

```ruby
@mail = Mail.new
@mail.add_file("/path/to/file.jpg")
@mail.parts.first.attachment? #=> true
@mail.parts.first.content_transfer_encoding.to_s #=> 'base64'
@mail.attachments.first.mime_type #=> 'image/jpg'
@mail.attachments.first.filename #=> 'file.jpg'
@mail.attachments.first.decoded == File.read('/path/to/file.jpg') #=> true
```

Or You can pass in file_data and give it a filename, again, mail
will try and guess the mime_type for you.

```ruby
@mail = Mail.new
@mail.attachments['myfile.pdf'] = File.read('path/to/myfile.pdf')
@mail.parts.first.attachment? #=> true
@mail.attachments.first.mime_type #=> 'application/pdf'
@mail.attachments.first.decoded == File.read('path/to/myfile.pdf') #=> true
```

You can also override the guessed MIME media type if you really know better
than mail (this should be rarely needed)

```ruby
@mail = Mail.new
file_data = File.read('path/to/myfile.pdf')
@mail.attachments['myfile.pdf'] = { :mime_type => 'application/x-pdf',
                                    :content => File.read('path/to/myfile.pdf') }
@mail.parts.first.mime_type #=> 'application/x-pdf'
```

Of course... Mail will round trip an attachment as well

```ruby
@mail = Mail.new do
  to      'nicolas@test.lindsaar.net.au'
  from    'Mikel Lindsaar <mikel@test.lindsaar.net.au>'
  subject 'First multipart email sent with Mail'

  text_part do
    body 'Here is the attachment you wanted'
  end

  html_part do
    content_type 'text/html; charset=UTF-8'
    body '<h1>Funky Title</h1><p>Here is the attachment you wanted</p>'
  end

  add_file '/path/to/myfile.pdf'
end

@round_tripped_mail = Mail.new(@mail.encoded)

@round_tripped_mail.attachments.length #=> 1
@round_tripped_mail.attachments.first.filename #=> 'myfile.pdf'
```
See "Testing and extracting attachments" above for more details.

Using Mail with Testing or Spec'ing Libraries
---------------------------------------------

If mail is part of your system, you'll need a way to test it without actually
sending emails, the TestMailer can do this for you.

```ruby
require 'mail'
=> true
Mail.defaults do
  delivery_method :test
end
=> #<Mail::Configuration:0x19345a8 @delivery_method=Mail::TestMailer>
Mail::TestMailer.deliveries
=> []
Mail.deliver do
  to 'mikel@me.com'
  from 'you@you.com'
  subject 'testing'
  body 'hello'
end
=> #<Mail::Message:0x19284ec ...
Mail::TestMailer.deliveries.length
=> 1
Mail::TestMailer.deliveries.first
=> #<Mail::Message:0x19284ec ...
Mail::TestMailer.deliveries.clear
=> []
```

There is also a set of RSpec matchers stolen fr^H^H^H^H^H^H^H^H inspired by Shoulda's ActionMailer matchers (you'll want to set <code>delivery_method</code> as above too):

```ruby
Mail.defaults do
  delivery_method :test # in practice you'd do this in spec_helper.rb
end

describe "sending an email" do
  include Mail::Matchers

  before(:each) do
    Mail::TestMailer.deliveries.clear

    Mail.deliver do
      to ['mikel@me.com', 'mike2@me.com']
      from 'you@you.com'
      subject 'testing'
      body 'hello'
    end
  end

  it { should have_sent_email } # passes if any email at all was sent

  it { should have_sent_email.from('you@you.com') }
  it { should have_sent_email.to('mike1@me.com') }

  # can specify a list of recipients...
  it { should have_sent_email.to(['mike1@me.com', 'mike2@me.com']) }

  # ...or chain recipients together
  it { should have_sent_email.to('mike1@me.com').to('mike2@me.com') }

  it { should have_sent_email.with_subject('testing') }

  it { should have_sent_email.with_body('hello') }

  # Can match subject or body with a regex
  # (or anything that responds_to? :match)

  it { should have_sent_email.matching_subject(/test(ing)?/) }
  it { should have_sent_email.matching_body(/h(a|e)llo/) }

  # Can chain together modifiers
  # Note that apart from recipients, repeating a modifier overwrites old value.

  it { should have_sent_email.from('you@you.com').to('mike1@me.com').matching_body(/hell/)
end
```

Excerpts from TREC Spam Corpus 2005
-----------------------------------

The spec fixture files in spec/fixtures/emails/from_trec_2005 are from the
2005 TREC Public Spam Corpus. They remain copyrighted under the terms of
that project and license agreement. They are used in this project to verify
and describe the development of this email parser implementation.

http://plg.uwaterloo.ca/~gvcormac/treccorpus/

They are used as allowed by 'Permitted Uses, Clause 3':

    "Small excerpts of the information may be displayed to others
     or published in a scientific or technical context, solely for
     the purpose of describing the research and development and
     related issues."

     -- http://plg.uwaterloo.ca/~gvcormac/treccorpus/

License
-------

(The MIT License)

Copyright (c) 2009-2013 Mikel Lindsaar

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# RSpec

Behaviour Driven Development for Ruby

# Description

rspec is a meta-gem, which depends on the [rspec-core](https://github.com/rspec/rspec-core), [rspec-expectations](https://github.com/rspec/rspec-expectations)
and [rspec-mocks](https://github.com/rspec/rspec-mocks) gems. Each of these can be installed separately and loaded in
isolation using `require`. Among other benefits, this allows you to use
rspec-expectations, for example, in Test::Unit::TestCase if you happen to
prefer that style.

Conversely, if you like RSpec's approach to declaring example groups and
examples (`describe` and `it`) but prefer Test::Unit assertions and mocha, rr
or flexmock for mocking, you'll be able to do that without having to install or load the
components of RSpec that you're not using.

## Documentation

See http://rspec.info/documentation/ for links to documentation for all gems.

## Install

    gem install rspec

## Contribute

* [http://github.com/rspec/rspec-dev](http://github.com/rspec/rspec-dev)

## Also see

* <http://github.com/rspec/rspec-core>
* <http://github.com/rspec/rspec-expectations>
* <http://github.com/rspec/rspec-mocks>
## Welcome to Rails

Rails is a web-application framework that includes everything needed to
create database-backed web applications according to the
[Model-View-Controller (MVC)](http://en.wikipedia.org/wiki/Model-view-controller)
pattern.

Understanding the MVC pattern is key to understanding Rails. MVC divides your
application into three layers, each with a specific responsibility.

The _Model layer_ represents your domain model (such as Account, Product,
Person, Post, etc.) and encapsulates the business logic that is specific to
your application. In Rails, database-backed model classes are derived from
`ActiveRecord::Base`. Active Record allows you to present the data from
database rows as objects and embellish these data objects with business logic
methods. You can read more about Active Record in its [README](activerecord/README.rdoc).
Although most Rails models are backed by a database, models can also be ordinary
Ruby classes, or Ruby classes that implement a set of interfaces as provided by
the Active Model module. You can read more about Active Model in its [README](activemodel/README.rdoc).

The _Controller layer_ is responsible for handling incoming HTTP requests and
providing a suitable response. Usually this means returning HTML, but Rails controllers
can also generate XML, JSON, PDFs, mobile-specific views, and more. Controllers load and
manipulate models, and render view templates in order to generate the appropriate HTTP response.
In Rails, incoming requests are routed by Action Dispatch to an appropriate controller, and
controller classes are derived from `ActionController::Base`. Action Dispatch and Action Controller
are bundled together in Action Pack. You can read more about Action Pack in its
[README](actionpack/README.rdoc).

The _View layer_ is composed of "templates" that are responsible for providing
appropriate representations of your application's resources. Templates can
come in a variety of formats, but most view templates are HTML with embedded
Ruby code (ERB files). Views are typically rendered to generate a controller response,
or to generate the body of an email. In Rails, View generation is handled by Action View.
You can read more about Action View in its [README](actionview/README.rdoc).

Active Record, Action Pack, and Action View can each be used independently outside Rails.
In addition to them, Rails also comes with Action Mailer ([README](actionmailer/README.rdoc)), a library
to generate and send emails; Active Job ([README](activejob/README.md)), a
framework for declaring jobs and making them run on a variety of queueing
backends; and Active Support ([README](activesupport/README.rdoc)), a collection
of utility classes and standard library extensions that are useful for Rails,
and may also be used independently outside Rails.

## Getting Started

1. Install Rails at the command prompt if you haven't yet:

        gem install rails

2. At the command prompt, create a new Rails application:

        rails new myapp

   where "myapp" is the application name.

3. Change directory to `myapp` and start the web server:

        cd myapp
        rails server

   Run with `--help` or `-h` for options.

4. Using a browser, go to `http://localhost:3000` and you'll see:
"Welcome aboard: You're riding Ruby on Rails!"

5. Follow the guidelines to start developing your application. You may find
   the following resources handy:
    * [Getting Started with Rails](http://guides.rubyonrails.org/getting_started.html)
    * [Ruby on Rails Guides](http://guides.rubyonrails.org)
    * [The API Documentation](http://api.rubyonrails.org)
    * [Ruby on Rails Tutorial](http://www.railstutorial.org/book)

## Contributing

We encourage you to contribute to Ruby on Rails! Please check out the
[Contributing to Ruby on Rails guide](http://edgeguides.rubyonrails.org/contributing_to_ruby_on_rails.html) for guidelines about how to proceed. [Join us!](http://contributors.rubyonrails.org)

## Code Status

* [![Build Status](https://travis-ci.org/rails/rails.svg?branch=4-2-stable)](https://travis-ci.org/rails/rails)

## License

Ruby on Rails is released under the [MIT License](http://www.opensource.org/licenses/MIT).
Replaced the plain DocBook XSL admonition icons with Jimmac's DocBook
icons (http://jimmac.musichall.cz/ikony.php3). I dropped transparency
from the Jimmac icons to get round MS IE and FOP PNG incompatibilities.

Stuart Rackham
= Active Support -- Utility classes and Ruby extensions from Rails

Active Support is a collection of utility classes and standard library
extensions that were found useful for the Rails framework. These additions
reside in this package so they can be loaded as needed in Ruby projects
outside of Rails.


== Download and installation

The latest version of Active Support can be installed with RubyGems:

  % [sudo] gem install activesupport

Source code can be downloaded as part of the Rails project on GitHub:

* https://github.com/rails/rails/tree/4-2-stable/activesupport


== License

Active Support is released under the MIT license:

* http://www.opensource.org/licenses/MIT


== Support

API documentation is at:

* http://api.rubyonrails.org

Bug reports can be filed for the Ruby on Rails project here:

* https://github.com/rails/rails/issues

Feature requests should be discussed on the rails-core mailing list here:

* https://groups.google.com/forum/?fromgroups#!forum/rubyonrails-core

[![Build Status](https://secure.travis-ci.org/banister/binding_of_caller.png)](http://travis-ci.org/banister/binding_of_caller)

binding_of_caller
===========

(C) John Mair (banisterfiend) 2012

_Retrieve the binding of a method's caller in MRI 1.9.2+, MRI 2.0 and RBX (Rubinius)_

The `binding_of_caller` gem provides the `Binding#of_caller` method.

Using `binding_of_caller` we can grab bindings from higher up the call
stack and evaluate code in that context. Allows access to bindings arbitrarily far up the
call stack, not limited to just the immediate caller.

**Recommended for use only in debugging situations. Do not use this in production apps.**

**Only works in MRI Ruby 1.9.2, 1.9.3, 2.0 and RBX (Rubinius)**

* Install the [gem](https://rubygems.org/gems/binding_of_caller): `gem install binding_of_caller`
* See the [source code](http://github.com/banister/binding_of_caller)

Example: Modifying a local inside the caller of a caller
--------

```ruby
def a
  var = 10
  b
  puts var
end

def b
  c
end

def c
  binding.of_caller(2).eval('var = :hello')
end

a()

# OUTPUT
# => hello
```

Spinoff project
-------

This project is a spinoff from the [Pry REPL project.](http://pry.github.com)

Features and limitations
-------------------------

* Only works with MRI 1.9.2, 1.9.3, 2.0 and RBX (Rubinius)
* Does not work in 1.8.7, but there is a well known (continuation-based) hack to get a `Binding#of_caller` there.

Contact
-------

Problems or questions contact me at [github](http://github.com/banister)


License
-------

(The MIT License)

Copyright (c) 2012 (John Mair)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# RSpec::Support

`RSpec::Support` provides common functionality to `RSpec::Core`,
`RSpec::Expectations` and `RSpec::Mocks`. It is considered
suitable for internal use only at this time.

## Installation / Usage

Install one or more of the `RSpec` gems.

Want to run against the `master` branch? You'll need to include the dependent
RSpec repos as well. Add the following to your `Gemfile`:

```ruby
%w[rspec-core rspec-expectations rspec-mocks rspec-support].each do |lib|
  gem lib, :git => "git://github.com/rspec/#{lib}.git", :branch => 'master'
end
```

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
[![Build Status](https://img.shields.io/travis/pry/pry.svg)](https://travis-ci.org/pry/pry)
[![Code Climate](https://img.shields.io/codeclimate/github/pry/pry.svg)](https://codeclimate.com/github/pry/pry)
[![Inline docs](http://inch-ci.org/github/pry/pry.svg)](http://inch-ci.org/github/pry/pry)

<center>
![The Pry Logo](https://dl.dropbox.com/u/26521875/pry%20stuff/logo/pry_logo_350.png)

© John Mair ([banisterfiend](https://twitter.com/banisterfiend)) 2013<br>

**Please** [DONATE](http://www.pledgie.com/campaigns/15899) to the Pry project - Pry was a **huge** amount of work and every donation received is encouraging and supports Pry's continued development!

**Sponsors**

[Tealeaf Academy](http://www.gotealeaf.com)<br/>
[Atomic Object](http://www.atomicobject.com/)<br/>
[Hashrocket](http://hashrocket.com/)<br/>
[Intridea](http://intridea.com/)<br/>
[Gaslight](http://gaslight.co/home)<br/>

**Other Resources**

[Skip to the website (recommended)](http://pry.github.com) <br />
[Skip to the wiki](https://github.com/pry/pry/wiki)
</center>

Pry is a powerful alternative to the standard IRB shell for Ruby. It is
written from scratch to provide a number of advanced features,
including:

* Source code browsing (including core C source with the pry-doc gem)
* Documentation browsing
* Live help system
* Open methods in editors (`edit Class#method`)
* Syntax highlighting
* Command shell integration (start editors, run git, and rake from within Pry)
* Gist integration
* Navigation around state (`cd`, `ls` and friends)
* Runtime invocation (use Pry as a developer console or debugger)
* Exotic object support (BasicObject instances, IClasses, ...)
* A Powerful and flexible command system
* Ability to view and replay history
* Many convenience commands inspired by IPython, Smalltalk and other advanced REPLs
* A wide-range number of [plugins](https://github.com/pry/pry/wiki/Available-plugins) that provide remote sessions, full debugging functionality, and more.

Pry also aims to be more than an IRB replacement; it is an
attempt to bring REPL driven programming to the Ruby language. It is
currently not as powerful as tools like [SLIME](http://en.wikipedia.org/wiki/SLIME) for lisp, but that is the
general direction Pry is heading.

Pry is also fairly flexible and allows significant user
[customization](https://github.com/pry/pry/wiki/Customization-and-configuration)
is trivial to set it to read from any object that has a `readline` method and write to any object that has a
`puts` method - many other aspects of Pry are also configurable making
it a good choice for implementing custom shells.

Pry comes with an executable so it can be invoked at the command line.
Just enter `pry` to start. A `.pryrc` file in the user's home directory will
be loaded if it exists. Type `pry --help` at the command line for more
information.

Try `gem install pry-doc` for additional documentation on Ruby Core
methods. The additional docs are accessed through the `show-doc` and
`show-method` commands.

* Install the [gem](https://rubygems.org/gems/pry): `gem install pry`
* Browse the comprehensive [documentation at the official Pry wiki](https://github.com/pry/pry/wiki)
* Read the [YARD API documentation](http://rdoc.info/github/pry/pry/master/file/README.markdown)
* See the [source code](http://github.com/pry/pry)

### Commands

Nearly every piece of functionality in a Pry session is implemented as
a command. Commands are not methods and must start at the beginning of a line, with no
whitespace in between. Commands support a flexible syntax and allow
'options' in the same way as shell commands, for example the following
Pry command will show a list of all private instance methods (in
scope) that begin with 'pa'

    pry(YARD::Parser::SourceParser):5> ls -Mp --grep ^pa
    YARD::Parser::SourceParser#methods: parse  parser_class  parser_type  parser_type=  parser_type_for_filename

### Navigating around state

Pry allows us to pop in and out of different scopes (objects) using
the `cd` command. This enables us to explore the run-time view of a
program or library. To view which variables and methods are available
within a particular scope we use the versatile [ls command.](https://gist.github.com/c0fc686ef923c8b87715)

Here we will begin Pry at top-level, then Pry on a class and then on
an instance variable inside that class:

    pry(main)> class Hello
    pry(main)*   @x = 20
    pry(main)* end
    => 20
    pry(main)> cd Hello
    pry(Hello):1> ls -i
    instance variables: @x
    pry(Hello):1> cd @x
    pry(20):2> self + 10
    => 30
    pry(20):2> cd ..
    pry(Hello):1> cd ..
    pry(main)> cd ..

The number after the `:` in the pry prompt indicates the nesting
level. To display more information about nesting, use the `nesting`
command. E.g

    pry("friend"):3> nesting
    Nesting status:
    0. main (Pry top level)
    1. Hello
    2. 100
    3. "friend"
    => nil

We can then jump back to any of the previous nesting levels by using
the `jump-to` command:

    pry("friend"):3> jump-to 1
    => 100
    pry(Hello):1>

### Runtime invocation

Pry can be invoked in the middle of a running program. It opens a Pry
session at the point it's called and makes all program state at that
point available. It can be invoked on any object using the
`my_object.pry` syntax or on the current binding (or any binding)
using `binding.pry`. The Pry session will then begin within the scope
of the object (or binding). When the session ends the program continues with any
modifications you made to it.

This functionality can be used for such things as: debugging,
implementing developer consoles and applying hot patches.

code:

    # test.rb
    require 'pry'

    class A
      def hello() puts "hello world!" end
    end

    a = A.new

    # start a REPL session
    binding.pry

    # program resumes here (after pry session)
    puts "program resumes here."

Pry session:

    pry(main)> a.hello
    hello world!
    => nil
    pry(main)> def a.goodbye
    pry(main)*   puts "goodbye cruel world!"
    pry(main)* end
    => nil
    pry(main)> a.goodbye
    goodbye cruel world!
    => nil
    pry(main)> exit

    program resumes here.

### Command Shell Integration

A line of input that begins with a '.' will be forwarded to the
command shell. This enables us to navigate the file system, spawn
editors, and run git and rake directly from within Pry.

Further, we can use the `shell-mode` command to incorporate the
present working directory into the Pry prompt and bring in (limited at this stage, sorry) file name completion.
We can also interpolate Ruby code directly into the shell by
using the normal `#{}` string interpolation syntax.

In the code below we're going to switch to `shell-mode` and edit the
`.pryrc` file in the home directory. We'll then cat its contents and
reload the file.

    pry(main)> shell-mode
    pry main:/home/john/ruby/projects/pry $ .cd ~
    pry main:/home/john $ .emacsclient .pryrc
    pry main:/home/john $ .cat .pryrc
    def hello_world
      puts "hello world!"
    end
    pry main:/home/john $ load ".pryrc"
    => true
    pry main:/home/john $ hello_world
    hello world!

We can also interpolate Ruby code into the shell. In the
example below we use the shell command `cat` on a random file from the
current directory and count the number of lines in that file with
`wc`:

    pry main:/home/john $ .cat #{Dir['*.*'].sample} | wc -l
    44

### Code Browsing

You can browse method source code with the `show-method` command. Nearly all Ruby methods (and some C methods, with the pry-doc
gem) can have their source viewed. Code that is longer than a page is
sent through a pager (such as less), and all code is properly syntax
highlighted (even C code).

The `show-method` command accepts two syntaxes, the typical ri
`Class#method` syntax and also simply the name of a method that's in
scope. You can optionally pass the `-l` option to show-method to
include line numbers in the output.

In the following example we will enter the `Pry` class, list the
instance methods beginning with 're' and display the source code for the `rep` method:

    pry(main)> cd Pry
    pry(Pry):1> ls -M --grep re
    Pry#methods: re  readline  refresh  rep  repl  repl_epilogue  repl_prologue  retrieve_line
    pry(Pry):1> show-method rep -l

    From: /home/john/ruby/projects/pry/lib/pry/pry_instance.rb @ line 143:
    Number of lines: 6

    143: def rep(target=TOPLEVEL_BINDING)
    144:   target = Pry.binding_for(target)
    145:   result = re(target)
    146:
    147:   show_result(result) if should_print?
    148: end

Note that we can also view C methods (from Ruby Core) using the
`pry-doc` plugin; we also show off the alternate syntax for
`show-method`:

    pry(main)> show-method Array#select

    From: array.c in Ruby Core (C Method):
    Number of lines: 15

    static VALUE
    rb_ary_select(VALUE ary)
    {
        VALUE result;
        long i;

        RETURN_ENUMERATOR(ary, 0, 0);
        result = rb_ary_new2(RARRAY_LEN(ary));
        for (i = 0; i < RARRAY_LEN(ary); i++) {
            if (RTEST(rb_yield(RARRAY_PTR(ary)[i]))) {
                rb_ary_push(result, rb_ary_elt(ary, i));
            }
        }
        return result;
    }

### Documentation Browsing

One use-case for Pry is to explore a program at run-time by `cd`-ing
in and out of objects and viewing and invoking methods. In the course
of exploring it may be useful to read the documentation for a
specific method that you come across. Like `show-method` the `show-doc` command supports
two syntaxes - the normal `ri` syntax as well as accepting the name of
any method that is currently in scope.

The Pry documentation system does not rely on pre-generated `rdoc` or
`ri`, instead it grabs the comments directly above the method on
demand. This results in speedier documentation retrieval and allows
the Pry system to retrieve documentation for methods that would not be
picked up by `rdoc`. Pry also has a basic understanding of both the
rdoc and yard formats and will attempt to syntax highlight the
documentation appropriately.

Nonetheless, the `ri` functionality is very good and
has an advantage over Pry's system in that it allows documentation
lookup for classes as well as methods. Pry therefore has good
integration with  `ri` through the `ri` command. The syntax
for the command is exactly as it would be in command-line -
so it is not necessary to quote strings.

In our example we will enter the `Gem` class and view the
documentation for the `try_activate` method:

    pry(main)> cd Gem
    pry(Gem):1> show-doc try_activate

    From: /Users/john/.rvm/rubies/ruby-1.9.2-p180/lib/ruby/site_ruby/1.9.1/rubygems.rb @ line 201:
    Number of lines: 3

    Try to activate a gem containing path. Returns true if
    activation succeeded or wasn't needed because it was already
    activated. Returns false if it can't find the path in a gem.
    pry(Gem):1>

We can also use `ri` in the normal way:

    pry(main) ri Array#each
    ----------------------------------------------------------- Array#each
         array.each {|item| block }   ->   array
    ------------------------------------------------------------------------
         Calls _block_ once for each element in _self_, passing that element
         as a parameter.

            a = [ "a", "b", "c" ]
            a.each {|x| print x, " -- " }

         produces:

            a -- b -- c --

### Gist integration

If the `gist` gem is installed then method source or documentation can be gisted to github with the
`gist` command.  The `gist` command is capable of gisting [almost any REPL content](https://gist.github.com/cae143e4533416529726), including methods, documentation,
input expressions, command source, and so on. In the example below we will gist the C source
code for the `Symbol#to_proc` method to github:

    pry(main)> gist -m Symbol#to_proc
    Gist created at https://gist.github.com/5332c38afc46d902ce46 and added to clipboard.
    pry(main)>

You can see the actual gist generated here: [https://gist.github.com/5332c38afc46d902ce46](https://gist.github.com/5332c38afc46d902ce46)

### Edit methods

You can use `edit Class#method` or `edit my_method`
(if the method is in scope) to open a method for editing directly in
your favorite editor. Pry has knowledge of a few different editors and
will attempt to open the file at the line the method is defined.

You can set the editor to use by assigning to the `Pry.editor`
accessor. `Pry.editor` will default to `$EDITOR` or failing that will
use `nano` as the backup default. The file that is edited will be
automatically reloaded after exiting the editor - reloading can be
suppressed by passing the `--no-reload` option to `edit`

In the example below we will set our default editor to "emacsclient"
and open the `Pry#repl` method for editing:

    pry(main)> Pry.editor = "emacsclient"
    pry(main)> edit Pry#repl

### Live Help System

Many other commands are available in Pry; to see the full list type
`help` at the prompt. A short description of each command is provided
with basic instructions for use; some commands have a more extensive
help that can be accessed via typing `command_name --help`. A command
will typically say in its description if the `--help` option is
avaiable.

### Use Pry as your Rails Console

The recommended way to use Pry as your Rails console is to add
[the `pry-rails` gem](https://github.com/rweng/pry-rails) to
your Gemfile. This replaces the default console with Pry, in
addition to loading the Rails console helpers and adding some
useful Rails-specific commands.

If you don't want to change your Gemfile, you can still run a Pry
console in your app's environment using Pry's `-r` flag:

    pry -r ./config/environment

Also check out the [wiki](https://github.com/pry/pry/wiki/Setting-up-Rails-or-Heroku-to-use-Pry)
for more information about integrating Pry with Rails.

### Limitations:

* Tab completion is currently a bit broken/limited this will have a
  major overhaul in a future version.

### Syntax Highlighting

Syntax highlighting is on by default in Pry. If you want to change
the colors, check out the [pry-theme](https://github.com/kyrylo/pry-theme)
gem.

You can toggle the syntax highlighting on and off in a session by
using the `toggle-color` command. Alternatively, you can turn it off
permanently by putting the line `Pry.color = false` in your `~/.pryrc`
file.

### Future Directions

Many new features are planned such as:

* Increase modularity (rely more on plugin system)
* Much improved documentation system, better support for YARD
* Better support for code and method reloading and saving code
* Extended and more sophisticated command system, allowing piping
between commands and running commands in background

### Contact

Problems or questions? file an issue at [github](https://github.com/pry/pry/issues)

### Contributors

Pry is primarily the work of [John Mair (banisterfiend)](http://github.com/banister), for full list
of contributors see the
[CONTRIBUTORS](https://github.com/pry/pry/blob/master/CONTRIBUTORS) file.
Ruby CoffeeScript
=================

Ruby CoffeeScript is a bridge to the official CoffeeScript compiler.

    CoffeeScript.compile File.read("script.coffee")


Installation
------------

    gem install coffee-script

*Note: This compiler library has replaced the original CoffeeScript
 compiler that was written in Ruby.*


Dependencies
------------

This library depends on the `coffee-script-source` gem which is
updated any time a new version of CoffeeScript is released. (The
`coffee-script-source` gem's version number is synced with each
official CoffeeScript release.) This way you can build against
different versions of CoffeeScript by requiring the correct version of
the `coffee-script-source` gem.

In addition, you can use this library with unreleased versions of
CoffeeScript by setting the `COFFEESCRIPT_SOURCE_PATH` environment
variable:

    export COFFEESCRIPT_SOURCE_PATH=/path/to/coffee-script/extras/coffee-script.js

### JSON

The `json` library is also required but is not explicitly stated as a
gem dependency. If you're on Ruby 1.8 you'll need to install the
`json` or `json_pure` gem. On Ruby 1.9, `json` is included in the
standard library.

### ExecJS

The [ExecJS](https://github.com/sstephenson/execjs) library is used to automatically choose the best JavaScript engine for your platform. Check out its [README](https://github.com/sstephenson/execjs/blob/master/README.md) for a complete list of supported engines.
# Rails Html Sanitizers

In Rails 4.2 and above this gem will be responsible for sanitizing HTML fragments in Rails
applications, i.e. in the `sanitize`, `sanitize_css`, `strip_tags` and `strip_links` methods.

Rails Html Sanitizer is only intended to be used with Rails applications. If you need similar functionality in non Rails apps consider using [Loofah](https://github.com/flavorjones/loofah) directly (that's what handles sanitization under the hood).

## Installation

Add this line to your application's Gemfile:

    gem 'rails-html-sanitizer'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install rails-html-sanitizer

## Usage

### Sanitizers

All sanitizers respond to `sanitize`.

#### FullSanitizer

```ruby
full_sanitizer = Rails::Html::FullSanitizer.new
full_sanitizer.sanitize("<b>Bold</b> no more!  <a href='more.html'>See more here</a>...")
# => Bold no more!  See more here...
```

#### LinkSanitizer

```ruby
link_sanitizer = Rails::Html::LinkSanitizer.new
link_sanitizer.sanitize('<a href="example.com">Only the link text will be kept.</a>')
# => Only the link text will be kept.
```

#### WhiteListSanitizer

```ruby
white_list_sanitizer = Rails::Html::WhiteListSanitizer.new

# sanitize via an extensive white list of allowed elements
white_list_sanitizer.sanitize(@article.body)

# white list only the supplied tags and attributes
white_list_sanitizer.sanitize(@article.body, tags: %w(table tr td), attributes: %w(id class style))

# white list via a custom scrubber
white_list_sanitizer.sanitize(@article.body, scrubber: ArticleScrubber.new)

# white list sanitizer can also sanitize css
white_list_sanitizer.sanitize_css('background-color: #000;')
```

### Scrubbers

Scrubbers are objects responsible for removing nodes or attributes you don't want in your HTML document.

This gem includes two scrubbers `Rails::Html::PermitScrubber` and `Rails::Html::TargetScrubber`.

#### `Rails::Html::PermitScrubber`

This scrubber allows you to permit only the tags and attributes you want.

```ruby
scrubber = Rails::Html::PermitScrubber.new
scrubber.tags = ['a']

html_fragment = Loofah.fragment('<a><img/ ></a>')
html_fragment.scrub!(scrubber)
html_fragment.to_s # => "<a></a>"
```

#### `Rails::Html::TargetScrubber`

Where `PermitScrubber` picks out tags and attributes to permit in sanitization,
`Rails::Html::TargetScrubber` targets them for removal.


```ruby
scrubber = Rails::Html::TargetScrubber.new
scrubber.tags = ['img']

html_fragment = Loofah.fragment('<a><img/ ></a>')
html_fragment.scrub!(scrubber)
html_fragment.to_s # => "<a></a>"
```

#### Custom Scrubbers

You can also create custom scrubbers in your application if you want to.

```ruby
class CommentScrubber < Rails::Html::PermitScrubber
  def allowed_node?(node)
    !%w(form script comment blockquote).include?(node.name)
  end

  def skip_node?(node)
    node.text?
  end

  def scrub_attribute?(name)
    name == "style"
  end
end
```

See `Rails::Html::PermitScrubber` documentation to learn more about which methods can be overridden.

#### Custom Scrubber in a Rails app

Using the `CommentScrubber` from above, you can use this in a Rails view like so:

```ruby
<%= sanitize @comment, scrubber: CommentScrubber.new %>
```

## Read more

Loofah is what underlies the sanitizers and scrubbers of rails-html-sanitizer.
- [Loofah and Loofah Scrubbers](https://github.com/flavorjones/loofah)

The `node` argument passed to some methods in a custom scrubber is an instance of `Nokogiri::XML::Node`.
- [`Nokogiri::XML::Node`](http://nokogiri.org/Nokogiri/XML/Node.html)
- [Nokogiri](http://nokogiri.org)

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
ExecJS
======

ExecJS lets you run JavaScript code from Ruby. It automatically picks
the best runtime available to evaluate your JavaScript program, then
returns the result to you as a Ruby object.

ExecJS supports these runtimes:

* [therubyracer](https://github.com/cowboyd/therubyracer) - Google V8
  embedded within Ruby
* [therubyrhino](https://github.com/cowboyd/therubyrhino) - Mozilla
  Rhino embedded within JRuby
* [Duktape.rb](https://github.com/judofyr/duktape.rb) - Duktape JavaScript interpreter
* [Node.js](http://nodejs.org/)
* Apple JavaScriptCore - Included with Mac OS X
* [Microsoft Windows Script Host](http://msdn.microsoft.com/en-us/library/9bbdkx3k.aspx) (JScript)

A short example:

``` ruby
require "execjs"
ExecJS.eval "'red yellow blue'.split(' ')"
# => ["red", "yellow", "blue"]
```

A longer example, demonstrating how to invoke the CoffeeScript compiler:

``` ruby
require "execjs"
require "open-uri"
source = open("http://coffeescript.org/extras/coffee-script.js").read

context = ExecJS.compile(source)
context.call("CoffeeScript.compile", "square = (x) -> x * x", bare: true)
# => "var square;\nsquare = function(x) {\n  return x * x;\n};"
```

# Installation

```
$ gem install execjs
```


# FAQ

**Why can't I use CommonJS `require()` inside ExecJS?**

ExecJS provides a lowest common denominator interface to any JavaScript runtime.
Use ExecJS when it doesn't matter which JavaScript interpreter your code runs
in. If you want to access the Node API, you should check another library like
[commonjs.rb](https://github.com/cowboyd/commonjs.rb) designed to provide a
consistent interface.

**Why can't I use `setTimeout`?**

For similar reasons as modules, not all runtimes guarantee a full JavaScript
event loop. So `setTimeout`, `setInterval` and other timers are not defined.

**Why can't I use ES5 features?**

Some runtimes like Node will implement many of the latest ES5 features. However
older stock runtimes like JSC on OSX and JScript on Windows may not. You should
only count on ES3 features being available. Prefer feature checking these APIs
rather than hard coding support for specific runtimes.

**Can ExecJS be used to sandbox scripts?**

No, ExecJS shouldn't be used for any security related sandboxing. Since runtimes
are automatically detected, each runtime has different sandboxing properties.
You shouldn't use `ExecJS.eval` on any inputs you wouldn't feel comfortable Ruby
`eval()`ing.


# License

Copyright (c) 2015 Sam Stephenson and Josh Peek.

Released under the MIT license. See `LICENSE` for details.
Origin [![Build Status](https://secure.travis-ci.org/mongoid/origin.png?branch=master&.png)](http://travis-ci.org/mongoid/origin) [![Code Climate](https://codeclimate.com/github/mongoid/origin.png)](https://codeclimate.com/github/mongoid/origin) [![Coverage Status](https://coveralls.io/repos/mongoid/origin/badge.png?branch=master)](https://coveralls.io/r/mongoid/origin?branch=master)
========

Origin is a DSL for building MongoDB queries.

Project Tracking
----------------

* [Mongoid Google Group](http://groups.google.com/group/mongoid)
* [Origin Website and Documentation](http://mongoid.org/en/origin/)

Compatibility
-------------

Origin is tested against MRI 1.9.2, 1.9.3, 2.0.0, and JRuby (1.9).

Documentation
-------------

Please see the new Mongoid website for up-to-date documentation in
the Origin section: [mongoid.org](http://mongoid.org/en/origin/)

License
-------

Copyright (c) 2011-2013 Durran Jordan

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Credits
-------

Durran Jordan: durran at gmail dot com
# Uglifier [![Build Status](https://travis-ci.org/lautis/uglifier.svg?branch=master)](https://travis-ci.org/lautis/uglifier) [![Dependency Status](https://gemnasium.com/lautis/uglifier.svg)](https://gemnasium.com/lautis/uglifier)

Ruby wrapper for [UglifyJS](https://github.com/mishoo/UglifyJS2) JavaScript compressor.

## Installation

Uglifier is available as a ruby gem.

    $ gem install uglifier

Ensure that your environment has a JavaScript interpreter supported by
[ExecJS](https://github.com/sstephenson/execjs). Using `therubyracer` gem
is a safe choice if a runtime isn't already present. Note that while JScript built-in Windows 7 and older works, it is extremely slow.

## Usage

```ruby
require 'uglifier'

Uglifier.new.compile(File.read("source.js"))
# => js file minified

# Or alternatively
Uglifier.compile(File.read("source.js"))
```

Uglifier also supports generating source maps:

```ruby
uglified, source_map = Uglifier.new.compile_with_map(source)
```

When initializing UglifyJS, you can tune the behavior of UglifyJS by passing options. For example, if you want disable variable name mangling:

```ruby
Uglifier.new(:mangle => false).compile(source)

# Or
Uglifier.compile(source, :mangle => false)
```

Available options and their defaults are

```ruby
{
  :output => {
    :ascii_only => true,        # Escape non-ASCII characters
    :comments => :copyright,    # Preserve comments (:all, :jsdoc, :copyright, :none, Regexp (see below))
    :inline_script => false,    # Escape occurrences of </script in strings
    :quote_keys => false,       # Quote keys in object literals
    :max_line_len => 32 * 1024, # Maximum line length in minified code
    :bracketize => false,       # Bracketize if, for, do, while or with statements, even if their body is a single statement
    :semicolons => true,        # Separate statements with semicolons
    :preserve_line => false,    # Preserve line numbers in outputs
    :beautify => false,         # Beautify output
    :indent_level => 4,         # Indent level in spaces
    :indent_start => 0,         # Starting indent level
    :space_colon => false,      # Insert space before colons (only with beautifier)
    :width => 80,               # Specify line width when beautifier is used (only with beautifier)
    :preamble => nil            # Preamble for the generated JS file. Can be used to insert any code or comment.
  },
  :mangle => {
    :eval => false,             # Mangle names when eval of when is used in scope
    :except => ["$super"],      # Argument names to be excluded from mangling
    :sort => false,             # Assign shorter names to most frequently used variables. Often results in bigger output after gzip.
    :toplevel => false          # Mangle names declared in the toplevel scope
  },                            # Mangle variable and function names, set to false to skip mangling
  :compress => {
    :sequences => true,         # Allow statements to be joined by commas
    :properties => true,        # Rewrite property access using the dot notation
    :dead_code => true,         # Remove unreachable code
    :drop_debugger => true,     # Remove debugger; statements
    :unsafe => false,           # Apply "unsafe" transformations
    :conditionals => true,      # Optimize for if-s and conditional expressions
    :comparisons => true,       # Apply binary node optimizations for comparisons
    :evaluate => true,          # Attempt to evaluate constant expressions
    :booleans => true,          # Various optimizations to boolean contexts
    :loops => true,             # Optimize loops when condition can be statically determined
    :unused => true,            # Drop unreferenced functions and variables
    :hoist_funs => true,        # Hoist function declarations
    :hoist_vars => false,       # Hoist var declarations
    :if_return => true,         # Optimizations for if/return and if/continue
    :join_vars => true,         # Join consecutive var statements
    :cascade => true,           # Cascade sequences
    :negate_iife => true,       # Negate immediately invoked function expressions to avoid extra parens
    :pure_getters => false,     # Assume that object property access does not have any side-effects
    :pure_funcs => nil,         # List of functions without side-effects. Can safely discard function calls when the result value is not used
    :drop_console => false,     # Drop calls to console.* functions
    :angular => false           # Process @ngInject annotations
    :keep_fargs => false        # Preserve unused function arguments
  },                            # Apply transformations to code, set to false to skip
  :define => {},                # Define values for symbol replacement
  :enclose => false,            # Enclose in output function wrapper, define replacements as key-value pairs
  :source_filename => nil,      # The filename of the input file
  :source_root => nil,          # The URL of the directory which contains :source_filename
  :output_filename => nil,      # The filename or URL where the minified output can be found
  :input_source_map => nil,     # The contents of the source map describing the input
  :screw_ie8 => false,          # Don't bother to generate safe code for IE8
  :source_map_url => false,     # Url for source mapping to be appended in minified source
  :source_url => false          # Url to original source to be appended in minified source
}
```

When passing a regular expression to the output => comments option, be sure to pass a valid Ruby Regexp.
The beginning and ending of comments are removed and cannot be matched (/*, */, //). For example:
When matching

```
/*!
 * comment
 */
```

use `Uglifier.new(output: {comments: /^!/})`.

## Development

Tests are run using

    bundle exec rake

See [CONTRIBUTING](https://github.com/lautis/uglifier/blob/master/CONTRIBUTING.md) for details about working on and contributing to Uglifier.

## Copyright

© Ville Lautanala. Released under MIT license, see [LICENSE](https://github.com/lautis/uglifier/blob/master/LICENSE.txt) for details.
# Jbuilder

[![Build Status](https://api.travis-ci.org/rails/jbuilder.svg)][travis]
[![Gem Version](http://img.shields.io/gem/v/jbuilder.svg)][gem]
[![Code Climate](http://img.shields.io/codeclimate/github/rails/jbuilder.svg)][codeclimate]
[![Dependencies Status](http://img.shields.io/gemnasium/rails/jbuilder.svg)][gemnasium]

[travis]: https://travis-ci.org/rails/jbuilder
[gem]: https://rubygems.org/gems/jbuilder
[codeclimate]: https://codeclimate.com/github/rails/jbuilder
[gemnasium]: https://gemnasium.com/rails/jbuilder

Jbuilder gives you a simple DSL for declaring JSON structures that beats
massaging giant hash structures. This is particularly helpful when the
generation process is fraught with conditionals and loops. Here's a simple
example:

``` ruby
# app/views/message/show.json.jbuilder

json.content format_content(@message.content)
json.(@message, :created_at, :updated_at)

json.author do
  json.name @message.creator.name.familiar
  json.email_address @message.creator.email_address_with_name
  json.url url_for(@message.creator, format: :json)
end

if current_user.admin?
  json.visitors calculate_visitors(@message)
end

json.comments @message.comments, :content, :created_at

json.attachments @message.attachments do |attachment|
  json.filename attachment.filename
  json.url url_for(attachment)
end
```

This will build the following structure:

``` javascript
{
  "content": "<p>This is <i>serious</i> monkey business</p>",
  "created_at": "2011-10-29T20:45:28-05:00",
  "updated_at": "2011-10-29T20:45:28-05:00",

  "author": {
    "name": "David H.",
    "email_address": "'David Heinemeier Hansson' <david@heinemeierhansson.com>",
    "url": "http://example.com/users/1-david.json"
  },

  "visitors": 15,

  "comments": [
    { "content": "Hello everyone!", "created_at": "2011-10-29T20:45:28-05:00" },
    { "content": "To you my good sir!", "created_at": "2011-10-29T20:47:28-05:00" }
  ],

  "attachments": [
    { "filename": "forecast.xls", "url": "http://example.com/downloads/forecast.xls" },
    { "filename": "presentation.pdf", "url": "http://example.com/downloads/presentation.pdf" }
  ]
}
```

To define attribute and structure names dynamically, use the `set!` method:

``` ruby
json.set! :author do
  json.set! :name, 'David'
end

# => "author": { "name": "David" }
```

Top level arrays can be handled directly.  Useful for index and other collection actions.

``` ruby
# @comments = @post.comments

json.array! @comments do |comment|
  next if comment.marked_as_spam_by?(current_user)

  json.body comment.body
  json.author do
    json.first_name comment.author.first_name
    json.last_name comment.author.last_name
  end
end

# => [ { "body": "great post...", "author": { "first_name": "Joe", "last_name": "Bloe" }} ]
```

You can also extract attributes from array directly.

``` ruby
# @people = People.all

json.array! @people, :id, :name

# => [ { "id": 1, "name": "David" }, { "id": 2, "name": "Jamie" } ]
```

Jbuilder objects can be directly nested inside each other.  Useful for composing objects.

``` ruby
class Person
  # ... Class Definition ... #
  def to_builder
    Jbuilder.new do |person|
      person.(self, :name, :age)
    end
  end
end

class Company
  # ... Class Definition ... #
  def to_builder
    Jbuilder.new do |company|
      company.name name
      company.president president.to_builder
    end
  end
end

company = Company.new('Doodle Corp', Person.new('John Stobs', 58))
company.to_builder.target!

# => {"name":"Doodle Corp","president":{"name":"John Stobs","age":58}}
```

You can either use Jbuilder stand-alone or directly as an ActionView template
language. When required in Rails, you can create views ala show.json.jbuilder
(the json is already yielded):

``` ruby
# Any helpers available to views are available to the builder
json.content format_content(@message.content)
json.(@message, :created_at, :updated_at)

json.author do
  json.name @message.creator.name.familiar
  json.email_address @message.creator.email_address_with_name
  json.url url_for(@message.creator, format: :json)
end

if current_user.admin?
  json.visitors calculate_visitors(@message)
end
```


You can use partials as well. The following will render the file
`views/comments/_comments.json.jbuilder`, and set a local variable
`comments` with all this message's comments, which you can use inside
the partial.

```ruby
json.partial! 'comments/comments', comments: @message.comments
```

It's also possible to render collections of partials:

```ruby
json.array! @posts, partial: 'posts/post', as: :post

# or

json.partial! 'posts/post', collection: @posts, as: :post

# or

json.partial! partial: 'posts/post', collection: @posts, as: :post

# or

json.comments @post.comments, partial: 'comment/comment', as: :comment
```

You can pass any objects into partial templates with or without `:locals` option.

```ruby
json.partial! 'sub_template', locals: { user: user }

# or

json.partial! 'sub_template', user: user
```


You can explicitly make Jbuilder object return null if you want:

``` ruby
json.extract! @post, :id, :title, :content, :published_at
json.author do
  if @post.anonymous?
    json.null! # or json.nil!
  else
    json.first_name @post.author_first_name
    json.last_name @post.author_last_name
  end
end
```

Fragment caching is supported, it uses `Rails.cache` and works like caching in
HTML templates:

```ruby
json.cache! ['v1', @person], expires_in: 10.minutes do
  json.extract! @person, :name, :age
end
```

You can also conditionally cache a block by using `cache_if!` like this:

```ruby
json.cache_if! !admin?, ['v1', @person], expires_in: 10.minutes do
  json.extract! @person, :name, :age
end
```

If you are rendering fragments for a collection of objects, have a look at
`jbuilder_cache_multi` gem. It uses fetch_multi (>= Rails 4.1) to fetch
multiple keys at once.

Keys can be auto formatted using `key_format!`, this can be used to convert
keynames from the standard ruby_format to camelCase:

``` ruby
json.key_format! camelize: :lower
json.first_name 'David'

# => { "firstName": "David" }
```

You can set this globally with the class method `key_format` (from inside your
environment.rb for example):

``` ruby
Jbuilder.key_format camelize: :lower
```

Faster JSON backends
--------------------

Jbuilder uses MultiJson, which by default will use the JSON gem. That gem is
currently tangled with ActiveSupport's all-Ruby `#to_json` implementation,
which is slow (fixed in Rails >= 4.1). For faster Jbuilder rendering, you can
specify something like the Yajl JSON generator instead. You'll need to include
the `yajl-ruby` gem in your Gemfile and then set the following configuration
for MultiJson:

``` ruby
require 'multi_json'
MultiJson.use :yajl
 ```
# High Voltage [![Build Status](https://travis-ci.org/thoughtbot/high_voltage.png)](http://travis-ci.org/thoughtbot/high_voltage)

Rails engine for static pages.

... but be careful. [Danger!](http://www.youtube.com/watch?v=HD5tnb2RBYg)

## Static pages?

Yeah, like "About us", "Directions", marketing pages, etc.

## Installation

    $ gem install high_voltage

Include in your Gemfile:

```ruby
gem 'high_voltage', '~> 2.3.0`
```

For Rails versions prior to 3.0, use the 0.9.2 tag of high_voltage:

    https://github.com/thoughtbot/high_voltage/tree/v0.9.2

## Usage

Write your static pages and put them in the RAILS_ROOT/app/views/pages directory.

    $ mkdir app/views/pages
    $ touch app/views/pages/about.html.erb

After putting something interesting there, you can link to it from anywhere in your app with:

```ruby
link_to 'About', page_path('about')
```

You can nest pages in a directory structure, if that makes sense from a URL perspective for you:

```ruby
link_to 'Q4 Reports', page_path('about/corporate/policies/HR/en_US/biz/sales/Quarter-Four')
```

Bam.

## Configuration

#### Routing overview

By default, the static page routes will be like /pages/:id (where :id is the view filename).

If you want to route to a static page in another location (for example, a homepage), do this:

```ruby
get 'pages/home' => 'high_voltage/pages#show', id: 'home'
```

In that case, you'd need an `app/views/pages/home.html.erb` file.

Generally speaking, you need to route to the 'show' action with an `:id` param of the view filename.

High Voltage will generate a named route method of `page_path`. If you want to generate
your own named route (with the :as routing option), make sure not to use `:page`
as it will conflict with the High Voltage named route.

#### Specifying a root path

You can configure the root route to a High Voltage page like this:

```ruby
# config/initializers/high_voltage.rb
HighVoltage.configure do |config|
  config.home_page = 'home'
end
```

Which will render the page from `app/views/pages/home.html.erb` when the '/'
route of the site is accessed.

Note: High Voltage also creates a search engine friendly 301 redirect. Any attempt to
access the path '/home' will be redirected to '/'.

#### Top-level routes

You can remove the directory `pages` from the URL path and serve up routes from
the root of the domain path:

    http://www.example.com/about
    http://www.example.com/company

Would look for corresponding files:

    app/views/pages/about.html.erb
    app/views/pages/company.html.erb

This is accomplished by setting the `route_drawer` to `HighVoltage::RouteDrawers::Root`

```ruby
# config/initializers/high_voltage.rb
HighVoltage.configure do |config|
  config.route_drawer = HighVoltage::RouteDrawers::Root
end
```

#### Disabling routes

The default routes can be completely removed by setting the `routes` to `false`:

```ruby
# config/initializers/high_voltage.rb
HighVoltage.configure do |config|
  config.routes = false
end
```

#### Specifying Rails engine for routes

If you are using multiple Rails engines within your application, you can
specify which engine to define the default HighVoltage routes on.

```ruby
# config/initializers/high_voltage.rb
HighVoltage.configure do |config|
  config.parent_engine = MyEngine
end
```

#### Page titles and meta-data

We suggest using `content_for` and `yield` for setting custom page titles and
meta-data on High Voltage pages.

```ruby
# app/views/pages/about.html.erb
<%= content_for :page_title, 'About Us - Custom page title' %>
```

Then print the contents of `:title` into the layout:

```ruby
# app/views/layouts/application.html.erb
<title><%= yield(:page_title) %></title>
```
#### Content path

High Voltage uses a default path and folder of 'pages', i.e. 'url.com/pages/contact',
'app/views/pages'.

You can change this in an initializer:

```ruby
# config/initializers/high_voltage.rb
HighVoltage.configure do |config|
  config.content_path = 'site/'
end
```

#### Caching

Caching has been deprecated and will be removed in the next release.

Page caching and action caching can be done via Rails. Visit the [Caching with
Rails: An overview](http://guides.rubyonrails.org/caching_with_rails.html) guide
for more details. You can utilize the methods described there by overriding the
HighVoltage controller as described [below](#override).

## Override

Most common reasons to override?

  * You need authentication around the pages to make sure a user is signed in.
  * You need to render different layouts for different pages.
  * You need to render a partial from the `app/views/pages` directory.

Create a `PagesController` of your own:

    $ rails generate controller pages

Disable the default routes:

```ruby
# config/initializers/high_voltage.rb
HighVoltage.configure do |config|
  config.routes = false
end
```

Define a route for the new `PagesController`:

```ruby
# config/routes.rb
get "/pages/*id" => 'pages#show', as: :page, format: false

# if routing the root path, update for your controller
root to: 'pages#show', id: 'home'
```

Then modify new `PagesController` to include the High Voltage static page concern:

```ruby
# app/controllers/pages_controller.rb
class PagesController < ApplicationController
  include HighVoltage::StaticPage

  before_filter :authenticate
  layout :layout_for_page

  private

  def layout_for_page
    case params[:id]
    when 'home'
      'home'
    else
      'application'
    end
  end
end
```

To set up a different layout for all High Voltage static pages, use an initializer:

```ruby
# config/initializers/high_voltage.rb
HighVoltage.configure do |config|
  config.layout = 'your_layout'
end
```

## Custom finding

You can further control the algorithm used to find pages by overriding
the `page_finder_factory` method:

```ruby
# app/controllers/pages_controller.rb
class PagesController < ApplicationController
  include HighVoltage::StaticPage

  private

  def page_finder_factory
    Rot13PageFinder
  end
end
```

The easiest thing is to subclass `HighVoltage::PageFinder`, which
provides you with `page_id`:

```ruby
class Rot13PageFinder < HighVoltage::PageFinder
  def find
    paths = super.split('/')
    directory = paths[0..-2]
    filename = paths[-1].tr('a-z','n-za-m')

    File.join(*directory, filename)
  end
end
```

Use this to create a custom file mapping, clean filenames for your file
system, A/B test, and so on.

## Localization

[Rails I18n guides](http://guides.rubyonrails.org/i18n.html).

Add a before filter to the Application controller

```ruby
# app/controllers/application_controller.rb
before_action :set_locale

def set_locale
  I18n.locale = params[:locale] || I18n.default_locale
end
```

Disable the default High Voltage routes

```ruby
# config/initializers/high_voltage.rb
HighVoltage.configure do |config|
  config.routes = false
end
```

```ruby
# config/routes.rb
scope "/:locale", locale: /en|bn|hi/ do
  get "/pages/:id" => "high_voltage/pages#show", :as => :page, :format => false
end
```

Add a static page to the project

```
# app/views/pages/about.html.erb
<%= t "hello" %>
```

Make sure that there are corresponding locale files

```
/config/locale/bn.yml
/config/locale/en.yml
/config/locale/hi.yml
```

One last note is there is a [know
issue](https://github.com/thoughtbot/high_voltage/issues/59) with High Voltage.

You'll need to specify routes like this `<%= link_to "About Us", page_path(id:
"about") %>`

## Testing

You can test your static pages using [RSpec](https://github.com/rspec/rspec-rails)
and [shoulda-matchers](https://github.com/thoughtbot/shoulda-matchers):

```ruby
# spec/controllers/pages_controller_spec.rb
describe PagesController, '#show' do
  %w(earn_money screencast about contact).each do |page|
    context 'on GET to /pages/#{page}' do
      before do
        get :show, id: page
      end

      it { should respond_with(:success) }
      it { should render_template(page) }
    end
  end
end
```

If you're not using a custom PagesController be sure to test
`HighVoltage::PagesController` instead.

Enjoy!

## Contributing

Please see [CONTRIBUTING.md].
Thank you, [contributors]!

[CONTRIBUTING.md]: /CONTRIBUTING.md
[contributors]: https://github.com/thoughtbot/high_voltage/graphs/contributors

## License

High Voltage is copyright © 2009-2015 thoughtbot. It is free software, and may
be redistributed under the terms specified in the [`LICENSE`] file.

[`LICENSE`]: /MIT-LICENSE

## About thoughtbot

![thoughtbot](https://thoughtbot.com/logo.png)

High Voltage is maintained and funded by thoughtbot, inc.
The names and logos for thoughtbot are trademarks of thoughtbot, inc.

We love open source software!
See [our other projects][community].
We are [available for hire][hire].

[community]: https://thoughtbot.com/community?utm_source=github
[hire]: https://thoughtbot.com/hire-us?utm_source=github
# rspec-rails [![Build Status](https://secure.travis-ci.org/rspec/rspec-rails.svg?branch=master)](http://travis-ci.org/rspec/rspec-rails) [![Code Climate](https://img.shields.io/codeclimate/github/rspec/rspec-rails.svg)](https://codeclimate.com/github/rspec/rspec-rails)
**rspec-rails** is a testing framework for Rails 3.x and 4.x.

Use **[rspec-rails 1.x](http://github.com/dchelimsky/rspec-rails)** for Rails
2.x.

## Installation

Add `rspec-rails` to **both** the `:development` and `:test` groups in the
`Gemfile`:

```ruby
group :development, :test do
  gem 'rspec-rails', '~> 3.0'
end
```

Want to run against the `master` branch? You'll need to include the dependent
RSpec repos as well. Add the following to your `Gemfile`:

```ruby
%w[rspec-core rspec-expectations rspec-mocks rspec-rails rspec-support].each do |lib|
  gem lib, :git => "git://github.com/rspec/#{lib}.git", :branch => 'master'
end
```

Download and install by running:

```
bundle install
```

Initialize the `spec/` directory (where specs will reside) with:

```
rails generate rspec:install
```

This adds the following files which are used for configuration:

- `.rspec`
- `spec/spec_helper.rb`
- `spec/rails_helper.rb`

Check the comments in each file for more information.

Use the `rspec` command to run your specs:

```
bundle exec rspec
```

By default the above will run all `_spec.rb` files in the `spec` directory. For
more details about this see the [RSpec spec file
docs](https://www.relishapp.com/rspec/rspec-core/docs/spec-files).

To run only a subset of these specs use the following command:

```
# Run only model specs
bundle exec rspec spec/models

# Run only specs for AccountsController
bundle exec rspec spec/controllers/accounts_controller_spec.rb
```

Specs can also be run via `rake spec`, though this command may be slower to
start than the `rspec` command.

In Rails 4, you may want to create a binstub for the `rspec` command so it can
be run via `bin/rspec`:

```
bundle binstubs rspec-core
```

### Upgrade Note

For detailed information on the general RSpec 3.x upgrade process see the
[RSpec Upgrade docs](https://relishapp.com/rspec/docs/upgrade).

There are three particular `rspec-rails` specific changes to be aware of:

1. [The default helper files created in RSpec 3.x have changed](https://www.relishapp.com/rspec/rspec-rails/docs/upgrade#default-helper-files)
2. [File-type inference disabled by default](https://www.relishapp.com/rspec/rspec-rails/docs/upgrade#file-type-inference-disabled)
3. [Rails 4.x `ActiveRecord::Migration` pending migration checks](https://www.relishapp.com/rspec/rspec-rails/docs/upgrade#pending-migration-checks)
4. Extraction of `stub_model` and `mock_model` to
   [`rspec-activemodel-mocks`](https://github.com/rspec/rspec-activemodel-mocks)

Please see the [RSpec Rails Upgrade
docs](https://www.relishapp.com/rspec/rspec-rails/docs/upgrade) for full
details.

**NOTE:** Generators run in RSpec 3.x will now require `rails_helper` instead
of `spec_helper`.

### Generators

Once installed, RSpec will generate spec files instead of Test::Unit test files
when commands like `rails generate model` and `rails generate controller` are
used.

You may also invoke RSpec generators independently. For instance,
running `rails generate rspec:model` will generate a model spec. For more
information, see [list of all
generators](https://www.relishapp.com/rspec/rspec-rails/docs/generators).

## Model Specs

Use model specs to describe behavior of models (usually ActiveRecord-based) in
the application.

Model specs default to residing in the `spec/models` folder. Tagging any
context with the metadata `:type => :model` treats its examples as model
specs.

For example:

```ruby
require "rails_helper"

RSpec.describe User, :type => :model do
  it "orders by last name" do
    lindeman = User.create!(first_name: "Andy", last_name: "Lindeman")
    chelimsky = User.create!(first_name: "David", last_name: "Chelimsky")

    expect(User.ordered_by_last_name).to eq([chelimsky, lindeman])
  end
end
```

For more information, see [cucumber scenarios for model
specs](https://www.relishapp.com/rspec/rspec-rails/docs/model-specs).

## Controller Specs

Use controller specs to describe behavior of Rails controllers.

Controller specs default to residing in the `spec/controllers` folder. Tagging
any context with the metadata `:type => :controller` treats its examples as
controller specs.

For example:

```ruby
require "rails_helper"

RSpec.describe PostsController, :type => :controller do
  describe "GET #index" do
    it "responds successfully with an HTTP 200 status code" do
      get :index
      expect(response).to be_success
      expect(response).to have_http_status(200)
    end

    it "renders the index template" do
      get :index
      expect(response).to render_template("index")
    end

    it "loads all of the posts into @posts" do
      post1, post2 = Post.create!, Post.create!
      get :index

      expect(assigns(:posts)).to match_array([post1, post2])
    end
  end
end
```

For more information, see [cucumber scenarios for controller
specs](https://www.relishapp.com/rspec/rspec-rails/docs/controller-specs).

**Note:** To encourage more isolated testing, views are not rendered by default
in controller specs. If you are verifying discrete view logic, use a [view
spec](#view-specs). If you are verifying the behaviour of a controller and view
together, consider a [request spec](#request-specs). You can use
[render\_views](https://www.relishapp.com/rspec/rspec-rails/docs/controller-specs/render-views)
if you must verify the rendered view contents within a controller spec, but
this is not recommended.

## Request Specs

Use request specs to specify one or more request/response cycles from end to
end using a black box approach.

Request specs default to residing in the `spec/requests`, `spec/api`, and
`spec/integration` directories. Tagging any context with the metadata `:type =>
:request` treats its examples as request specs.

Request specs mix in behavior from
[ActionDispatch::Integration::Runner](http://api.rubyonrails.org/classes/ActionDispatch/Integration/Runner.html),
which is the basis for [Rails' integration
tests](http://guides.rubyonrails.org/testing.html#integration-testing).

```ruby
require 'rails_helper'

RSpec.describe "home page", :type => :request do
  it "displays the user's username after successful login" do
    user = User.create!(:username => "jdoe", :password => "secret")
    get "/login"
    assert_select "form.login" do
      assert_select "input[name=?]", "username"
      assert_select "input[name=?]", "password"
      assert_select "input[type=?]", "submit"
    end

    post "/login", :username => "jdoe", :password => "secret"
    assert_select ".header .username", :text => "jdoe"
  end
end
```

The above example uses only standard Rails and RSpec APIs, but many
RSpec/Rails users like to use extension libraries like
[FactoryGirl](https://github.com/thoughtbot/factory_girl) and
[Capybara](https://github.com/jnicklas/capybara):

```ruby
require 'rails_helper'

RSpec.describe "home page", :type => :request do
  it "displays the user's username after successful login" do
    user = FactoryGirl.create(:user, :username => "jdoe", :password => "secret")
    visit "/login"
    fill_in "Username", :with => "jdoe"
    fill_in "Password", :with => "secret"
    click_button "Log in"

    expect(page).to have_selector(".header .username", :text => "jdoe")
  end
end
```

FactoryGirl decouples this example from changes to validation requirements,
which can be encoded into the underlying factory definition without requiring
changes to this example.

Among other benefits, Capybara binds the form post to the generated HTML, which
means we don't need to specify them separately. Note that Capybara's DSL as
shown is, by default, only available in specs in the spec/features directory.
For more information, see the [Capybara integration
docs](http://rubydoc.info/gems/rspec-rails/file/Capybara.md).

There are several other Ruby libs that implement the factory pattern or provide
a DSL for request specs (a.k.a. acceptance or integration specs), but
FactoryGirl and Capybara seem to be the most widely used. Whether you choose
these or other libs, we strongly recommend using something for each of these
roles.

## Feature Specs

Feature specs test your application from the outside by simulating a browser.
[`capybara`](https://github.com/jnicklas/capybara) is used to manage the
simulated browser.

Feature specs default to residing in the `spec/features` folder. Tagging any
context with the metadata `:type => :feature` treats its examples as feature
specs.

Feature specs mix in functionality from the capybara gem, thus they require
`capybara` to use. To use feature specs, add `capybara` to the `Gemfile`:

```ruby
gem "capybara"
```

For more information, see the [cucumber scenarios for feature
specs](https://www.relishapp.com/rspec/rspec-rails/v/3-0/docs/feature-specs/feature-spec).

## View specs

View specs default to residing in the `spec/views` folder. Tagging any context
with the metadata `:type => :view` treats its examples as view specs.

View specs mix in `ActionView::TestCase::Behavior`.

```ruby
require 'rails_helper'

RSpec.describe "events/index", :type => :view do
  it "renders _event partial for each event" do
    assign(:events, [double(Event), double(Event)])
    render
    expect(view).to render_template(:partial => "_event", :count => 2)
  end
end

RSpec.describe "events/show", :type => :view do
  it "displays the event location" do
    assign(:event, Event.new(:location => "Chicago"))
    render
    expect(rendered).to include("Chicago")
  end
end
```

View specs infer the controller name and path from the path to the view
template. e.g. if the template is `events/index.html.erb` then:

```ruby
controller.controller_path == "events"
controller.request.path_parameters[:controller] == "events"
```

This means that most of the time you don't need to set these values. When
spec'ing a partial that is included across different controllers, you _may_
need to override these values before rendering the view.

To provide a layout for the render, you'll need to specify _both_ the template
and the layout explicitly. For example:

```ruby
render :template => "events/show", :layout => "layouts/application"
```

### `assign(key, val)`

Use this to assign values to instance variables in the view:

```ruby
assign(:widget, Widget.new)
render
```

The code above assigns `Widget.new` to the `@widget` variable in the view, and
then renders the view.

Note that because view specs mix in `ActionView::TestCase` behavior, any
instance variables you set will be transparently propagated into your views
(similar to how instance variables you set in controller actions are made
available in views). For example:

```ruby
@widget = Widget.new
render # @widget is available inside the view
```

RSpec doesn't officially support this pattern, which only works as a
side-effect of the inclusion of `ActionView::TestCase`. Be aware that it may be
made unavailable in the future.

#### Upgrade note

```ruby
# rspec-rails-1.x
assigns[key] = value

# rspec-rails-2.x+
assign(key, value)
```

### `rendered`

This represents the rendered view.

```ruby
render
expect(rendered).to match /Some text expected to appear on the page/
```

#### Upgrade note

```ruby
# rspec-rails-1.x
render
response.should xxx

# rspec-rails-2.x+
render
rendered.should xxx

# rspec-rails-2.x+ with expect syntax
render
expect(rendered).to xxx
```

## Routing specs

Routing specs default to residing in the `spec/routing` folder. Tagging any
context with the metadata `:type => :routing` treats its examples as routing
specs.

```ruby
require 'rails_helper'

RSpec.describe "routing to profiles", :type => :routing do
  it "routes /profile/:username to profile#show for username" do
    expect(:get => "/profiles/jsmith").to route_to(
      :controller => "profiles",
      :action => "show",
      :username => "jsmith"
    )
  end

  it "does not expose a list of profiles" do
    expect(:get => "/profiles").not_to be_routable
  end
end
```

### Upgrade note

`route_for` from rspec-rails-1.x is gone. Use `route_to` and `be_routable`
instead.

## Helper specs

Helper specs default to residing in the `spec/helpers` folder. Tagging any
context with the metadata `:type => :helper` treats its examples as helper
specs.

Helper specs mix in ActionView::TestCase::Behavior. A `helper` object is
provided which mixes in the helper module being spec'd, along with
`ApplicationHelper` (if present).

```ruby
require 'rails_helper'

RSpec.describe EventsHelper, :type => :helper do
  describe "#link_to_event" do
    it "displays the title, and formatted date" do
      event = Event.new("Ruby Kaigi", Date.new(2010, 8, 27))
      # helper is an instance of ActionView::Base configured with the
      # EventsHelper and all of Rails' built-in helpers
      expect(helper.link_to_event).to match /Ruby Kaigi, 27 Aug, 2010/
    end
  end
end
```

## Matchers

Several domain-specific matchers are provided to each of the example group
types. Most simply delegate to their equivalent Rails' assertions.

### `be_a_new`

- Available in all specs
- Primarily intended for controller specs

```ruby
expect(object).to be_a_new(Widget)
```

Passes if the object is a `Widget` and returns true for `new_record?`

### `render_template`

- Delegates to Rails' `assert_template`
- Available in request, controller, and view specs

In request and controller specs, apply to the `response` object:

```ruby
expect(response).to render_template("new")
```

In view specs, apply to the `view` object:

```ruby
expect(view).to render_template(:partial => "_form", :locals => { :widget => widget } )
```

### `redirect_to`

- Delegates to `assert_redirect`
- Available in request and controller specs

```ruby
expect(response).to redirect_to(widgets_path)
```

### `route_to`

- Delegates to Rails' `assert_routing`
- Available in routing and controller specs

```ruby
expect(:get => "/widgets").to route_to(:controller => "widgets", :action => "index")
```

### `be_routable`

Passes if the path is recognized by Rails' routing. This is primarily intended
to be used with `not_to` to specify standard CRUD routes which should not be
routable.

```ruby
expect(:get => "/widgets/1/edit").not_to be_routable
```

### `have_http_status`

- Passes if `response` has a matching HTTP status code
- The following symbolic status codes are allowed:
  - `Rack::Utils::SYMBOL_TO_STATUS_CODE`
  - One of the defined `ActionDispatch::TestResponse` aliases:
    - `:error`
    - `:missing`
    - `:redirect`
    - `:success`
- Available in controller, feature, and request specs.

In controller and request specs, apply to the `response` object:

```ruby
expect(response).to have_http_status(201)
expect(response).not_to have_http_status(:created)
```

In feature specs, apply to the `page` object:

```ruby
expect(page).to have_http_status(:success)
```

## `rake` tasks

Several rake tasks are provided as a convenience for working with RSpec. To run
the entire spec suite use `rake spec`. To run a subset of specs use the
associated type task, for example `rake spec:models`.

A full list of the available rake tasks can be seen by running `rake -T | grep
spec`.

### Customizing `rake` tasks

If you want to customize the behavior of `rake spec`, you may [define your own
task in the `Rakefile` for your
project](https://www.relishapp.com/rspec/rspec-core/docs/command-line/rake-task).
However, you must first clear the task that rspec-rails defined:

```ruby
task("spec").clear
```

## Contribute

See [http://github.com/rspec/rspec-dev](http://github.com/rspec/rspec-dev).

For `rspec-rails`-specific development information, see
[README_DEV](https://github.com/rspec/rspec-rails/blob/master/README_DEV.md).

## Also see

* [http://github.com/rspec/rspec](http://github.com/rspec/rspec)
* [http://github.com/rspec/rspec-core](http://github.com/rspec/rspec-core)
* [http://github.com/rspec/rspec-expectations](http://github.com/rspec/rspec-expectations)
* [http://github.com/rspec/rspec-mocks](http://github.com/rspec/rspec-mocks)

## Feature Requests & Bugs

See <http://github.com/rspec/rspec-rails/issues>
= minitest/{unit,spec,mock,benchmark}

home :: https://github.com/seattlerb/minitest
bugs :: https://github.com/seattlerb/minitest/issues
rdoc :: http://docs.seattlerb.org/minitest
vim  :: https://github.com/sunaku/vim-ruby-minitest
emacs:: https://github.com/arthurnn/minitest-emacs

== DESCRIPTION:

minitest provides a complete suite of testing facilities supporting
TDD, BDD, mocking, and benchmarking.

    "I had a class with Jim Weirich on testing last week and we were
     allowed to choose our testing frameworks. Kirk Haines and I were
     paired up and we cracked open the code for a few test
     frameworks...

     I MUST say that minitest is *very* readable / understandable
     compared to the 'other two' options we looked at. Nicely done and
     thank you for helping us keep our mental sanity."

    -- Wayne E. Seguin

minitest/unit is a small and incredibly fast unit testing framework.
It provides a rich set of assertions to make your tests clean and
readable.

minitest/spec is a functionally complete spec engine. It hooks onto
minitest/unit and seamlessly bridges test assertions over to spec
expectations.

minitest/benchmark is an awesome way to assert the performance of your
algorithms in a repeatable manner. Now you can assert that your newb
co-worker doesn't replace your linear algorithm with an exponential
one!

minitest/mock by Steven Baker, is a beautifully tiny mock (and stub)
object framework.

minitest/pride shows pride in testing and adds coloring to your test
output. I guess it is an example of how to write IO pipes too. :P

minitest/unit is meant to have a clean implementation for language
implementors that need a minimal set of methods to bootstrap a working
test suite. For example, there is no magic involved for test-case
discovery.

    "Again, I can't praise enough the idea of a testing/specing
     framework that I can actually read in full in one sitting!"

    -- Piotr Szotkowski

Comparing to rspec:

    rspec is a testing DSL. minitest is ruby.

    -- Adam Hawkins, "Bow Before MiniTest"

minitest doesn't reinvent anything that ruby already provides, like:
classes, modules, inheritance, methods. This means you only have to
learn ruby to use minitest and all of your regular OO practices like
extract-method refactorings still apply.

== FEATURES/PROBLEMS:

* minitest/autorun - the easy and explicit way to run all your tests.
* minitest/unit - a very fast, simple, and clean test system.
* minitest/spec - a very fast, simple, and clean spec system.
* minitest/mock - a simple and clean mock/stub system.
* minitest/benchmark - an awesome way to assert your algorithm's performance.
* minitest/pride - show your pride in testing!
* Incredibly small and fast runner, but no bells and whistles.

== RATIONALE:

See design_rationale.rb to see how specs and tests work in minitest.

== SYNOPSIS:

Given that you'd like to test the following class:

  class Meme
    def i_can_has_cheezburger?
      "OHAI!"
    end

    def will_it_blend?
      "YES!"
    end
  end

=== Unit tests

Define your tests as methods beginning with `test_`.

  require "minitest/autorun"

  class TestMeme < Minitest::Test
    def setup
      @meme = Meme.new
    end

    def test_that_kitty_can_eat
      assert_equal "OHAI!", @meme.i_can_has_cheezburger?
    end

    def test_that_it_will_not_blend
      refute_match /^no/i, @meme.will_it_blend?
    end

    def test_that_will_be_skipped
      skip "test this later"
    end
  end

=== Specs

  require "minitest/autorun"

  describe Meme do
    before do
      @meme = Meme.new
    end

    describe "when asked about cheeseburgers" do
      it "must respond positively" do
        @meme.i_can_has_cheezburger?.must_equal "OHAI!"
      end
    end

    describe "when asked about blending possibilities" do
      it "won't say no" do
        @meme.will_it_blend?.wont_match /^no/i
      end
    end
  end

For matchers support check out:

https://github.com/wojtekmach/minitest-matchers
https://github.com/rmm5t/minitest-matchers_vaccine

=== Benchmarks

Add benchmarks to your tests.

  # optionally run benchmarks, good for CI-only work!
  require "minitest/benchmark" if ENV["BENCH"]

  class TestMeme < Minitest::Benchmark
    # Override self.bench_range or default range is [1, 10, 100, 1_000, 10_000]
    def bench_my_algorithm
      assert_performance_linear 0.9999 do |n| # n is a range value
        @obj.my_algorithm(n)
      end
    end
  end

Or add them to your specs. If you make benchmarks optional, you'll
need to wrap your benchmarks in a conditional since the methods won't
be defined. In minitest 5, the describe name needs to match
/Bench(mark)?$/.

  describe "Meme Benchmark" do
    if ENV["BENCH"] then
      bench_performance_linear "my_algorithm", 0.9999 do |n|
        100.times do
          @obj.my_algorithm(n)
        end
      end
    end
  end

outputs something like:

  # Running benchmarks:

  TestBlah	100	1000	10000
  bench_my_algorithm	 0.006167	 0.079279	 0.786993
  bench_other_algorithm	 0.061679	 0.792797	 7.869932

Output is tab-delimited to make it easy to paste into a spreadsheet.

=== Mocks

Mocks and stubs defined using terminology by Fowler & Meszaros at
http://www.martinfowler.com/bliki/TestDouble.html:

"Mocks are pre-programmed with expectations which form a specification
of the calls they are expected to receive. They can throw an exception
if they receive a call they don't expect and are checked during
verification to ensure they got all the calls they were expecting."

  class MemeAsker
    def initialize(meme)
      @meme = meme
    end

    def ask(question)
      method = question.tr(" ", "_") + "?"
      @meme.__send__(method)
    end
  end

  require "minitest/autorun"

  describe MemeAsker, :ask do
    describe "when passed an unpunctuated question" do
      it "should invoke the appropriate predicate method on the meme" do
        @meme = Minitest::Mock.new
        @meme_asker = MemeAsker.new @meme
        @meme.expect :will_it_blend?, :return_value

        @meme_asker.ask "will it blend"

        @meme.verify
      end
    end
  end

=== Stubs

Mocks and stubs are defined using terminology by Fowler & Meszaros at
http://www.martinfowler.com/bliki/TestDouble.html:

"Stubs provide canned answers to calls made during the test".

Minitest's stub method overrides a single method for the duration of
the block.

  def test_stale_eh
    obj_under_test = Something.new

    refute obj_under_test.stale?

    Time.stub :now, Time.at(0) do   # stub goes away once the block is done
      assert obj_under_test.stale?
    end
  end

A note on stubbing: In order to stub a method, the method must
actually exist prior to stubbing. Use a singleton method to create a
new non-existing method:

  def obj_under_test.fake_method
    ...
  end

=== Running Your Tests

Ideally, you'll use a rake task to run your tests, either piecemeal or
all at once. Both rake and rails ship with rake tasks for running your
tests. BUT! You don't have to:

    % ruby -Ilib:test test/minitest/test_minitest_unit.rb
    Run options: --seed 37685

    # Running:

    ...................................................................... (etc)

    Finished in 0.107130s, 1446.8403 runs/s, 2959.0217 assertions/s.

    155 runs, 317 assertions, 0 failures, 0 errors, 0 skips

There are runtime options available, both from minitest itself, and also
provided via plugins. To see them, simply run with `--help`:

    % ruby -Ilib:test test/minitest/test_minitest_unit.rb --help
    minitest options:
        -h, --help                       Display this help.
        -s, --seed SEED                  Sets random seed
        -v, --verbose                    Verbose. Show progress processing files.
        -n, --name PATTERN               Filter run on /pattern/ or string.

    Known extensions: pride, autotest
        -p, --pride                      Pride. Show your testing pride!
        -a, --autotest                   Connect to autotest server.

== Writing Extensions

To define a plugin, add a file named minitest/XXX_plugin.rb to your
project/gem. That file must be discoverable via ruby's LOAD_PATH (via
rubygems or otherwise). Minitest will find and require that file using
Gem.find_files. It will then try to call plugin_XXX_init during
startup. The option processor will also try to call plugin_XXX_options
passing the OptionParser instance and the current options hash. This
lets you register your own command-line options. Here's a totally
bogus example:

    # minitest/bogus_plugin.rb:

    module Minitest
      def self.plugin_bogus_options(opts, options)
        opts.on "--myci", "Report results to my CI" do
          options[:myci] = true
          options[:myci_addr] = get_myci_addr
          options[:myci_port] = get_myci_port
        end
      end

      def self.plugin_bogus_init(options)
        self.reporter << MyCI.new(options) if options[:myci]
      end
    end

=== Adding custom reporters

Minitest uses composite reporter to output test results using multiple
reporter instances. You can add new reporters to the composite during
the init_plugins phase. As we saw in +plugin_bonus_init+ above, you
simply add your reporter instance to the composite via +<<+.

+AbstractReporter+ defines the API for reporters. You may subclass it
and override any method you want to achieve your desired behavior.

start   :: Called when the run has started.
record  :: Called for each result, passed or otherwise.
report  :: Called at the end of the run.
passed? :: Called to see if you detected any problems.

Using our example above, here is how we might implement MyCI:

    # minitest/bogus_plugin.rb

    module Minitest
      class MyCI < AbstractReporter
        attr_accessor :results, :addr, :port

        def initialize options
          self.results = []
          self.addr = options[:myci_addr]
          self.port = options[:myci_port]
        end

        def record result
          self.results << result
        end

        def report
          CI.connect(addr, port).send_results self.results
        end
      end

      # code from above...
    end

== FAQ

=== How to test SimpleDelegates?

The following implementation and test:

    class Worker < SimpleDelegator
      def work
      end
    end

    describe Worker do
      before do
        @worker = Worker.new(Object.new)
      end

      it "must respond to work" do
        @worker.must_respond_to :work
      end
    end

outputs a failure:

      1) Failure:
    Worker#test_0001_must respond to work [bug11.rb:16]:
    Expected #<Object:0x007f9e7184f0a0> (Object) to respond to #work.

Worker is a SimpleDelegate which in 1.9+ is a subclass of BasicObject.
Expectations are put on Object (one level down) so the Worker
(SimpleDelegate) hits `method_missing` and delegates down to the
`Object.new` instance. That object doesn't respond to work so the test
fails.

You can bypass `SimpleDelegate#method_missing` by extending the worker
with `Minitest::Expectations`. You can either do that in your setup at
the instance level, like:

    before do
      @worker = Worker.new(Object.new)
      @worker.extend Minitest::Expectations
    end

or you can extend the Worker class (within the test file!), like:

    class Worker
      include ::Minitest::Expectations
    end

=== How to share code across test classes?

Use a module. That's exactly what they're for:

    module UsefulStuff
      def useful_method
        # ...
      end
    end

    describe Blah do
      include UsefulStuff

      def test_whatever
        # useful_method available here
      end
    end

Remember, `describe` simply creates test classes. It's just ruby at
the end of the day and all your normal Good Ruby Rules (tm) apply. If
you want to extend your test using setup/teardown via a module, just
make sure you ALWAYS call super. before/after automatically call super
for you, so make sure you don't do it twice.

=== Why am I seeing `uninitialized constant MiniTest::Test (NameError)`?

Are you running the test with Bundler (e.g. via `bundle exec`)? If so, 
in order to require minitest, you must first add the `gem 'minitest'`
to your Gemfile and run `bundle`. Once it's installed, you should be 
able to require minitest and run your tests.

== Prominent Projects using Minitest:

* arel
* journey
* mime-types
* nokogiri
* rails (active_support et al)
* rake
* rdoc
* ...and of course, everything from seattle.rb...

== Known Extensions:

capybara_minitest_spec      :: Bridge between Capybara RSpec matchers and
                               Minitest::Spec expectations (e.g.
                               page.must_have_content("Title")).
color_pound_spec_reporter   :: Test names print Ruby Object types in color with
                               your Minitest Spec style tests.
minispec-metadata           :: Metadata for describe/it blocks & CLI tag filter.
                               E.g. `it "requires JS driver", js: true do` &
                               `ruby test.rb --tag js` runs tests tagged :js.
minitest-ansi               :: Colorize minitest output with ANSI colors.
minitest-around             :: Around block for minitest. An alternative to
                               setup/teardown dance.
minitest-autotest           :: autotest is a continous testing facility meant to
                               be used during development.
minitest-bacon              :: minitest-bacon extends minitest with bacon-like
                               functionality.
minitest-bang               :: Adds support for RSpec-style let! to immediately
                               invoke let statements before each test.
minitest-bisect             :: Helps you isolate and debug random test failures.
minitest-capistrano         :: Assertions and expectations for testing
                               Capistrano recipes.
minitest-capybara           :: Capybara matchers support for minitest unit and
                               spec.
minitest-chef-handler       :: Run Minitest suites as Chef report handlers
minitest-ci                 :: CI reporter plugin for Minitest.
minitest-colorize           :: Colorize Minitest output and show failing tests
                               instantly.
minitest-context            :: Defines contexts for code reuse in Minitest
                               specs that share common expectations.
minitest-debugger           :: Wraps assert so failed assertions drop into
                               the ruby debugger.
minitest-display            :: Patches Minitest to allow for an easily
                               configurable output.
minitest-documentation      :: Minimal documentation format inspired by rspec's.
minitest-doc_reporter       :: Detailed output inspired by rspec's documentation
                               format.
minitest-emoji              :: Print out emoji for your test passes, fails, and
                               skips.
minitest-english            :: Semantically symmetric aliases for assertions and
                               expectations.
minitest-excludes           :: Clean API for excluding certain tests you
                               don't want to run under certain conditions.
minitest-fail-fast          :: Reimplements RSpec's "fail fast" feature
minitest-filecontent        :: Support unit tests with expectation results in files.
                               Differing results will be stored again in files.
minitest-filesystem         :: Adds assertion and expectation to help testing
                               filesystem contents.
minitest-firemock           :: Makes your Minitest mocks more resilient.
minitest-focus              :: Focus on one test at a time.
minitest-gcstats            :: A minitest plugin that adds a report of the top
                               tests by number of objects allocated.
minitest-great_expectations :: Generally useful additions to minitest's
                               assertions and expectations.
minitest-growl              :: Test notifier for minitest via growl.
minitest-happy              :: GLOBALLY ACTIVATE MINITEST PRIDE! RAWR!
minitest-hooks              :: Around and before_all/after_all/around_all hooks
minitest-implicit-subject   :: Implicit declaration of the test subject.
minitest-instrument         :: Instrument ActiveSupport::Notifications when
                               test method is executed.
minitest-instrument-db      :: Store information about speed of test execution
                               provided by minitest-instrument in database.
minitest-junit              :: JUnit-style XML reporter for minitest.
minitest-libnotify          :: Test notifier for minitest via libnotify.
minitest-line               :: Run test at line number.
minitest-logger             :: Define assert_log and enable minitest to test log messages.
                               Supports Logger and Log4r::Logger.
minitest-macruby            :: Provides extensions to minitest for macruby UI
                               testing.
minitest-matchers           :: Adds support for RSpec-style matchers to
                               minitest.
minitest-matchers_vaccine   :: Adds assertions that adhere to the matcher spec,
                               but without any expectation infections.
minitest-metadata           :: Annotate tests with metadata (key-value).
minitest-mongoid            :: Mongoid assertion matchers for Minitest.
minitest-must_not           :: Provides must_not as an alias for wont in
                               Minitest.
minitest-osx                :: Reporter for the Mac OS X notification center.
minitest-parallel_fork      :: Fork-based parallelization
minitest-parallel-db        :: Run tests in parallel with a single database.
minitest-power_assert       :: PowerAssert for Minitest.
minitest-predicates         :: Adds support for .predicate? methods.
minitest-profile            :: List the 10 slowest tests in your suite.
minitest-rails              :: Minitest integration for Rails 3.x.
minitest-rails-capybara     :: Capybara integration for Minitest::Rails.
minitest-reporters          :: Create customizable Minitest output formats.
minitest-rg                 :: Colored red/green output for Minitest.
minitest-rspec_mocks        :: Use RSpec Mocks with Minitest.
minitest-server             :: minitest-server provides a client/server setup 
                               with your minitest process, allowing your test 
                               run to send its results directly to a handler.
minitest-shared_description :: Support for shared specs and shared spec
                               subclasses
minitest-should_syntax      :: RSpec-style +x.should == y+ assertions for
                               Minitest.
minitest-shouldify          :: Adding all manner of shoulds to Minitest (bad
                               idea)
minitest-snail              :: Print a list of tests that take too long
minitest-spec-context       :: Provides rspec-ish context method to
                               Minitest::Spec.
minitest-spec-expect        :: Expect syntax for Minitest::Spec (e.g.
                               expect(sequences).to_include :celery_man).
minitest-spec-magic         :: Minitest::Spec extensions for Rails and beyond.
minitest-spec-rails         :: Drop in Minitest::Spec superclass for
                               ActiveSupport::TestCase.
minitest-sprint             :: Runs (Get it? It's fast!) your tests and makes
                               it easier to rerun individual failures.
minitest-stately            :: Find leaking state between tests
minitest-stub_any_instance  :: Stub any instance of a method on the given class
                               for the duration of a block.
minitest-stub-const         :: Stub constants for the duration of a block.
minitest-tags               :: Add tags for minitest.
minitest-unordered          :: Adds a new assertion to minitest for checking the
                               contents of a collection, ignoring element order.
minitest-vcr                :: Automatic cassette managment with Minitest::Spec
                               and VCR.
minitest-wscolor            :: Yet another test colorizer.
minitest_owrapper           :: Get tests results as a TestResult object.
minitest_should             :: Shoulda style syntax for minitest test::unit.
minitest_tu_shim            :: Bridges between test/unit and minitest.
mongoid-minitest            :: Minitest matchers for Mongoid.
pry-rescue                  :: A pry plugin w/ minitest support. See
                               pry-rescue/minitest.rb.
rspec2minitest              :: Easily translate any RSpec matchers to Minitest
                               assertions and expectations.

== Unknown Extensions:

Authors... Please send me a pull request with a description of your minitest extension.

* assay-minitest
* detroit-minitest
* em-minitest-spec
* flexmock-minitest
* guard-minitest
* guard-minitest-decisiv
* minitest-activemodel
* minitest-ar-assertions
* minitest-capybara-unit
* minitest-colorer
* minitest-deluxe
* minitest-extra-assertions
* minitest-rails-shoulda
* minitest-spec
* minitest-spec-should
* minitest-sugar
* spork-minitest

== REQUIREMENTS:

* Ruby 1.8.7+. No magic is involved. I hope.

== INSTALL:

  sudo gem install minitest

On 1.9, you already have it. To get newer candy you can still install
the gem, and then requiring "minitest/autorun" should automatically
pull it in. If not, you'll need to do it yourself:

  gem "minitest"     # ensures you"re using the gem, and not the built-in MT
  require "minitest/autorun"

  # ... usual testing stuffs ...

DO NOTE: There is a serious problem with the way that ruby 1.9/2.0
packages their own gems. They install a gem specification file, but
don't install the gem contents in the gem path. This messes up
Gem.find_files and many other things (gem which, gem contents, etc).

Just install minitest as a gem for real and you'll be happier.

== LICENSE:

(The MIT License)

Copyright (c) Ryan Davis, seattle.rb

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# New Relic Ruby Agent

New Relic is a performance management system, developed by
New Relic, Inc (http://www.newrelic.com).  It provides you with deep
information about the performance of your Rails or Ruby
application as it runs in production. The New Relic Ruby Agent is
dual-purposed as a either a Gem or a Rails plugin, hosted on
[github](http://github.com/newrelic/rpm/tree/master).

The New Relic Ruby Agent runs in one of two modes:

**Production Mode**
Low overhead instrumentation that captures detailed information on
your application running in production and transmits them to
newrelic.com where you can monitor them in real time.

**Developer Mode**
A Rack middleware that maps `/newrelic` to an application for showing
detailed performance metrics on a page by page basis.  Installed
automatically in Rails applications.

## Supported Environments

* Ruby 1.8.7, REE, 1.9.x, 2.0.x, 2.1.x, 2.2.x
* JRuby 1.6 and 1.7
* Rubinius 2.x (Experimental support only)
* Rails 2.1 or later for Production Mode
* Rails 2.3 or later for Developer Mode
* Sinatra
* Rack

An up to date list of Ruby versions and frameworks for the latest agent
can be found on [our docs site](http://docs.newrelic.com/docs/ruby/supported-frameworks).

Any Rack based framework should work but may not be tested.  Install
the Ruby Agent as a gem and add the Developer Mode middleware if
desired.  Report any problems by visiting support.newrelic.com.

You can also monitor non-web applications. Refer to the "Other
Environments" section under "Getting Started".

## Contributing Code

We welcome code contributions (in the form of pull requests) from our user
community.  Before submitting a pull request please review
[GUIDELINES_FOR_CONTRIBUTING](https://github.com/newrelic/rpm/blob/master/GUIDELINES_FOR_CONTRIBUTING.md).

Following these helps us efficiently review and incorporate your contribution
and avoid breaking your code with future changes to the agent.


## Getting Started

Add the Ruby Agent to your project's Gemfile.

    gem 'newrelic_rpm'

To monitor your applications in production, create an account at
http://newrelic.com/ .  There you can
sign up for a free Lite account or one of our paid subscriptions.

Once you receive the welcome e-mail with a license key and
`newrelic.yml` file. You can copy the `newrelic.yml` file into your app config
directory OR can generate the file manually with command:

    newrelic install --license_key="YOUR_KEY" "My application"

The initial configuration is done in the `newrelic.yml` file.  This file
is by default read from the `config` directory of the application root
and is subsequently searched for in the application root directory,
and then in a `~/.newrelic` directory.  Once you're up and running you can
enable Server Side Config and manage your newrelic configuration from the web
UI.

#### Rails Installation

You can install the agent as a Gem:

For Bundler:

Add the following line to your Gemfile:

    gem 'newrelic_rpm'

For Rails 2.x without Bundler:

edit `environment.rb` and add to the initalizer block:

    config.gem "newrelic_rpm"

#### Sinatra Installation

To use the Ruby Agent with a Sinatra app, add

    require 'newrelic_rpm'

in your Sinatra app, below the Sinatra require directive.

Then make sure you set `RACK_ENV` to the environment corresponding to the
configuration definitions in the newrelic.yml file; e.g., development,
staging, production, etc.

To use Developer Mode in Sinatra, add `NewRelic::Rack::DeveloperMode` to
the middleware stack.  See the `config.ru` sample below.

#### Other Environments

You can use the Ruby Agent to monitor any Ruby application.  Add

    require 'newrelic_rpm'

to your startup sequence and then manually start the agent using

    NewRelic::Agent.manual_start

For information about instrumenting pure Rack applications, see our
[Rack middlewares documentation](http://docs.newrelic.com/docs/ruby/rack-middlewares).

Refer to the [New Relic's Docs](http://newrelic.com/docs) for details on how to
monitor other web frameworks, background jobs, and daemons.

The Ruby Agent provides an API that allows custom instrumentation of additional
frameworks.  You can find a list of community created intrumentation plugins
(e.g. [newrelic-redis](https://github.com/evanphx/newrelic-redis)) in the
[extends_newrelic_rpm project](https://github.com/newrelic/extends_newrelic_rpm).

## Developer Mode

When running the Developer Mode, the Ruby Agent will track the
performance of every HTTP request serviced by your application, and
store in memory this information for the last 100 HTTP transactions.

To view this performance information, including detailed SQL statement
analysis, open `/newrelic` in your web application.  For instance if
you are running mongrel or thin on port 3000, enter the following into
your browser:

    http://localhost:3000/newrelic

Developer Mode is only initialized if the `developer_mode` setting in
the newrelic.yml file is set to true.  By default, it is turned off in
all environments but `development`.

#### Developer Mode in Rails

Developer Mode is available automatically in Rails Applications based
on Rails 2.3 and later.  No additional configuration is required. When
your application starts and `developer_mode` is enabled, the Ruby
Agent injects a middleware into your Rails middleware stack.

For earlier versions of Rails that support Rack, you can use
a `config.ru` as below.

#### Developer Mode in Rack Applications

Developer Mode is available for any Rack based application such as
Sinatra by installing the NewRelic::Rack::DeveloperMode
middleware. This middleware passes all requests that do not start with
/newrelic.

Here's an example entry for Developer Mode in a `config.ru` file:

    require 'new_relic/rack/developer_mode'
    use NewRelic::Rack::DeveloperMode

## Production Mode

When your application runs in the production environment, the New
Relic agent runs in production mode. It connects to the New Relic
service and sends deep performance data to the UI for your
analysis. To view this data, log in to http://rpm.newrelic.com.

NOTE: You must have a valid account and license key to view this data
online.  Refer to instructions in *Getting Started*.

## Recording Deploys

The Ruby Agent supports recording deployments in New Relic via a command line
tool or Capistrano recipes. For more information on these features see
[our deployment documentation](http://docs.newrelic.com/docs/ruby/recording-deployments-with-the-ruby-agent)
for more information.

## Support

You can find more detailed documentation [on our website](http://newrelic.com/docs),
and specifically in the [Ruby category](http://newrelic.com/docs/ruby).

If you can't find what you're looking for there, reach out to us on our [support
site](http://support.newrelic.com/) or our [community forum](http://forum.newrelic.com)
and we'll be happy to help you.

Also available is community support on IRC: we generally use #newrelic
on irc.freenode.net

Find a bug? Contact us via [support.newrelic.com](http://support.newrelic.com/),
or e-mail support @ newrelic.com.

Thank you, and may your application scale to infinity plus one.

Lew Cirne, Founder and CEO

New Relic, Inc.
# Cross Agent Tests

### Data Policy

None of these tests should contain customer data such as SQL strings.
Please be careful when adding new tests from real world failures.

### Tests

| Test Files    | Description   |
| ------------- |-------------|
| [rum_loader_insertion_location](rum_loader_insertion_location) | Describe where the RUM loader (formerly known as header) should be inserted. |
| [rum_footer_insertion_location](rum_footer_insertion_location) | Describe where the RUM footer (aka "client config") should be inserted.  These tests do not apply to agents which insert the footer directly after the loader. |
| [rules.json](rules.json) | Describe how url/metric/txn-name rules should be applied. |
| [rum_client_config.json](rum_client_config.json) | These tests dictate the format and contents of the browser monitoring client configuration.  For more information see: [SPEC](https://newrelic.atlassian.net/wiki/display/eng/JavaScript+Agent+Auto-Instrumentation) |
| [sql_parsing.json](sql_parsing.json) | These tests show how an SQL string should be parsed for the operation and table name. |
| [url_clean.json](url_clean.json) | These tests show how URLs should be cleaned before putting them into a trace segment's parameter hash (under the key 'uri'). |
| [url_domain_extraction.json](url_domain_extraction.json) | These tests show how the domain of a URL should be extracted (for the purpose of creating external metrics). |
| [postgres_explain_obfuscation](postgres_explain_obfuscation) | These tests show how plain-text explain plan output from PostgreSQL should be obfuscated when SQL obfuscation is enabled. |
| [sql_obfuscation](sql_obfuscation) | Describe how agents should obfuscate SQL queries before transmission to the collector. |
| [attribute_configuration](attribute_configuration.json) | These tests show how agents should respond to the various attribute configuration settings.  For more information see: [Attributes SPEC](https://newrelic.atlassian.net/wiki/display/eng/Agent+Attributes) |
| [cat_map](cat_map.json) | These tests cover the new Dirac attributes that are added for the CAT Map project. See the [CAT Map Spec](https://newrelic.jiveon.com/docs/DOC-1798) and the section below for details.|
| [labels](labels.json) | These tests cover the Labels for Language Agents project. See the [Labels for Language Agents Spec](https://newrelic.atlassian.net/wiki/display/eng/Labels+for+Language+Agents) for details.|
| [proc_cpuinfo](proc_cpuinfo) | These test correct processing of `/proc/cpuinfo` output on Linux hosts. |
| [proc_meminfo](proc_meminfo) | These test correct processing of `/proc/meminfo` output on Linux hosts. |
| [transaction_segment_terms.json](transaction_segment_terms.json) | These tests cover agent implementations of the `transaction_segment_terms` transaction renaming rules introduced in collector protocol 14. See [the spec](https://newrelic.atlassian.net/wiki/display/eng/Language+agent+transaction+segment+terms+rules) for details. |
| [docker_container_id](docker_container_id) | These tests cover parsing of Docker container IDs from `/proc/*/cgroup` on Linux hosts. |

### CAT Map test details

The CAT map test cases in `cat_map.json` are meant to be used to verify the
attributes that agents collect and attach to analytics transaction events for
the CAT map project.

**NOTE** currently `nr.apdexPerfZone` is not covered by these tests, make sure you test for this yourself until it is added to these tests.

Each test case should correspond to a simulated transaction in the agent under
test. Here's what the various fields in each test case mean:

| Name | Meaning |
| ---- | ------- |
| `name` | A human-meaningful name for the test case. |
| `appName` | The name of the New Relic application for the simulated transaction. |
| `transactionName` | The final name of the simulated transaction. |
| `transactionGuid` | The GUID of the simulated transaction. |
| `inboundPayload` | The (non-serialized) contents of the `X-NewRelic-Transaction` HTTP request header on the simulated transaction. Note that this value should be serialized to JSON, obfuscated using the CAT obfuscation algorithm, and Base64-encoded before being used in the header value. Note also that the `X-NewRelic-ID` header should be set on the simulated transaction, though its value is not specified in these tests. |
| `expectedIntrinsicFields` | A set of key-value pairs that are expected to be present in the analytics event generated for the simulated transaction. These fields should be present in the first hash of the analytic event payload (built-in agent-supplied fields). |
| `nonExpectedIntrinsicFields` | An array of attribute names that should *not* be present in the analytics event generated for the simulated transaction. |
| `outboundRequests` | An array of objects representing outbound requests that should be made in the context of the simulated transaction. See the table below for details. Only present if the test case involves making outgoing requests from the simulated transaction. |

Here's what the fields of each entry in the `outboundRequests` array mean:

| Name | Meaning |
| ---- | ------- |
| `outboundTxnName` | The name of the simulated transaction at the time this outbound request is made. Your test driver should set the transaction name to this value prior to simulating the outbound request. |
| `expectedOutboundPayload` | The expected (un-obfuscated) content of the outbound `X-NewRelic-Transaction` request header for this request. |
These tests are for determining the numbers of physical packages, physical cores,
and logical processors from the data returned by /proc/cpuinfo on Linux hosts.
Each text file in this directory is the output of /proc/cpuinfo on various machines.

The names of all test files should be of the form `Apack_Bcore_Clogical.txt`
where `A`, `B`, and `C` are integers or the character `X`. For example,
a single quad-core processor without hyperthreading would correspond to
`1pack_4core_4logical.txt`, while two 6-core processors with hyperthreading
would correspond to `2pack_12core_24logical.txt`, and would be pretty sweet.

Using `A`, `B`, and `C` from above, code processing the text in these files
should produce the following expected values:

| property             | value   |
| -------------------- |---------|
| # physical packages  | `A`     |
| # physical cores     | `B`     |
| # logical processors | `C`     |

(Obviously, the processing code should do this with no knowledge of the filenames.)

If any of `A`, `B`, or `C` are the character `X` instead of an integer, then
processing code should not return a value (return `null`, return `nil`,
raise an exception... whatever makes most sense for your agent).
These test cases cover obfuscation (more properly, masking) of literal values
from SQL statements captured by agents. SQL statements may be captured and
attached to transaction trace nodes, or to slow SQL traces.

`sql_obfuscation.json` contains an array of test cases.  The inputs for each
test case are in the `sql` property of each object. Each test case also has an
`obfuscated` property which is an array containing at least one valid output.

Test cases also have a `dialects` property, which is an array of strings which
specify which sql dialects the test should apply to. Currently the options are
`mysql`, `postgres`, or `all`  This is relevant because PostgreSQL uses
different identifier and string quoting rules than MySQL (most notably,
double-quoted string literals are not allowed in PostgreSQL, where
double-quotes are instead used around identifiers).

Test cases may also contain the following properties:
  * `malformed`: (boolean) tests who's SQL queries are not valid SQL in any
  quoting mode. Some agents may choose to attempt to obfuscate these cases,
  and others may instead just replace the query entirely with a placeholder
  message.
  * `pathological`: (boolean) tests which are designed specifically to break
  specific methods of obfuscation, or contain patterns that are known to be
  difficult to handle correctly
  * `comments`: an array of strings that could be usefult for understanding
  the test.

The following database documentation may be helpful in understanding these test
cases:
* [MySQL String Literals](http://dev.mysql.com/doc/refman/5.5/en/string-literals.html)
* [PostgreSQL String Constants](http://www.postgresql.org/docs/8.2/static/sql-syntax-lexical.html#SQL-SYNTAX-CONSTANTS)
These tests cover parsing of Docker container IDs on Linux hosts out of 
`/proc/self/cgroup` (or `/proc/<pid>/cgroup` more generally).

The `cases.json` file lists each filename in this directory containing 
example `/proc/self/cgroup` content, and the expected Docker container ID that
should be parsed from that file.
# Synthetics Tests

The Synthetics tests are designed to verify that the agent handles valid and invalid Synthetics requests.

Each test should run a simulated web transaction. A Synthetics HTTP request header is added to the incoming request at the beginning of a web transaction. During the course of the web transaction, an external request is made. And, at the completion of the web transaction, both a Transaction Trace and Transaction Event are recorded.

Each test then verifies that the correct attributes are added to the Transaction Trace and Transaction Event, and the proper request header is added to the external request when required. Or, in the case of an invalid Synthetics request, that the attributes and request header are **not** added.

## Name

| Name | Meaning |
| ---- | ------- |
| `name` | A human-meaningful name for the test case. |

## Settings

The `settings` hash contains a number of key-value pairs that the agent will need to use for configuration for the test.

| Name | Meaning |
| ---- | ------- |
| `agentEncodingKey`| The encoding key used by the agent for deobfuscation of the Synthetics request header. |
| `syntheticsEncodingKey` | The encoding key used by Synthetics to obfuscate the Synthetics request header. In most tests, `encodingKey` and `syntheticsEncodingKey` are the same. |
| `transactionGuid` | The GUID of the simulated transaction. In a non-simulated transaction, this will be randomly generated. But, for testing purposes, you should assign this value as the GUID, since the tests will check for this value to be set in the `nr.guid` attribute of the Transaction Event. |
| `trustedAccountIds` | A list of accounts ids that the agent trusts. If the Synthetics request contains a non-trusted account id, it is an invalid request.|

## Inputs

The input for each test is a Synthetics request header. The test fixture file shows both the de-obfuscated version of the payload, as well as the resulting obfuscated version.

| Name | Meaning |
| ---- | ------- |
| `inputHeaderPayload` | A decoded form of the contents of the `X-NewRelic-Synthetics` request header. |
| `inputObfuscatedHeader` | An obfuscated form of the `X-NewRelic-Synthetics` request header. If you obfuscate `syntheticsHeaderPayload` using the CAT obfuscation algorithm, this should be the output. |

## Outputs

There are three different outputs that are tested for: Transaction Trace, Transaction Event, and External Request Header.

### outputTransactionTrace

The `outputTransactionTrace` hash contains three objects:

| Name | Meaning |
| ---- | ------- |
| `header` | The last field of the transaction sample array should be set to the Synthetics Resource ID for a Synthetics request, and should be set to `null` if it isn't. (The last field in the array is the 10th element in the header array, but is `header[9]` in zero-based array notation, so the key name is `field_9`.) |
| `expectedIntrinsics` | A set of key-value pairs that represent the attributes that should be set in the intrinsics section of the Transaction Trace. **Note**: If the agent has not implemented the Agent Attributes spec, then the agent should save the attributes in the `Custom` section, and the attribute names should have 'nr.' prepended to them. Read the spec for details. For agents in this situation, they will need to adjust the expected output of the tests accordingly. |
| `nonExpectedIntrinsics` | An array of names that represent the attributes that should **not** be set in the intrinsics section of the Transaction Trace.|

### outputTransactionEvent

The `outputTransactionEvent` hash contains two objects:

| Name | Meaning |
| ---- | ------- |
| `expectedAttributes` | A set of key-value pairs that represent the attributes that should be set in the `Intrinsic` hash of the Transaction Event. |
| `nonExpectedAttributes` | An array of names that represent the attributes that should **not** be set in the `Intrinsic` hash of the Transaction Event. |

### outputExternalRequestHeader

The `outputExternalRequestHeader` hash contains two objects:

| Name | Meaning |
| ---- | ------- |
| `expectedHeader` | The outbound header that should be added to external requests (similar to the CAT header), when the original request was made from a valid Synthetics request. |
| `nonExpectedHeader` | The outbound header that should **not** be added to external requests, when the original request was made from a non-Synthetics request. |
# PostgreSQL explain plan obfuscation tests

These tests show how explain plans for PostgreSQL should be obfuscated when
SQL obfuscation is enabled. Obfuscation of explain plans for PostgreSQL is
necessary because they can include portions of the original query that may
contain sensitive data.

Each test case consists of a set of files with the following extensions:

* `.query.txt` - the original SQL query that is being explained
* `.explain.txt` - the raw un-obfuscated output from running `EXPLAIN <query>`
* `.colon_obfuscated.txt` - the desired obfuscated explain output if using the
default, more aggressive obfuscation strategy described [here](https://newrelic.atlassian.net/wiki/display/eng/Obfuscating+PostgreSQL+Explain+plans).
* `.obfuscated.txt` - the desired obfuscated explain output if using a more
accurate, less aggressive obfuscation strategy detailed in this
[Jive thread](https://newrelic.jiveon.com/thread/1851).
These tests are for determining the physical memory from the data returned by
/proc/meminfo on Linux hosts. The total physical memory of the linux system is 
reported as part of the enviornment values. The key used by the Python agent
is 'Total Physical Memory (MB)'. 

The names of all test files should be of the form `meminfo_nnnnMB.txt`. The
value `nnnn` in the filename is the physical memory of that system in MB.
# Multiverse

## Testing in a multitude of environments

Multiverse was created to solve a specific problem experienced by the Agent
team.  Not only does the New Relic Agent run in a wide variety of environments,
but its expected behavior *changes* based on the environment.  Instrumenation is
toggled on and off based on the presence of certain libraries, and some of these
libraries are incompatible with each other.  Effective testing requires us to
specify different environments for different tests; Multiverse aims to make this
painless.


## Getting started

You can invoke this via rake

    rake test:multiverse

If you only want to run some test suites you can filter by their names

    rake test:multiverse[sinatra]

You can run tests of multiverse itself with

    rake test:multiverse:self

### Adding a test suite

To add tests add a directory to the `suites` directory.  This directory should
contain at least two files.

#### Envfile

The Envfile is a meta gem file.  It allows you to specify one or more gemset
that the tests in this directory should be run against.  For example:

    gemfile <<-GEMFILE
      gem "rails", "~>3.2.0"
    GEMFILE

    gemfile <<-GEMFILE
      gem "rails", "~>3.1.0"
    GEMFILE

This will run these tests against 2 environments, one running rails 3.1, the
other running rails 3.2.

New Relic is automatically included in the environment.  Specifying it in the
Envfile will trigger and error.  You can override where newrelic is loaded from
using two environment variables.

The default gemfile line is

    gem 'newrelic_rpm', :path => '../../../ruby_agent'

`ENV['NEWRELIC_GEMFILE_LINE']` will specify the full line for the gemfile

`ENV['NEWRELIC_GEM_PATH']` will override the `:path` option in the default line.


#### Test files

All files in a test suite directory that end with .rb will be executed as test
files.  These should use test unit.

For example:

    require 'test/unit'
    class ATest < Test::Unit::TestCase
      def test_json_is_loaded
        assert JSON
      end

      def test_haml_is_not_loaded
        assert !defined?(Haml)
      end
    end


## Testing Multiverse

Multiverse has a suite of tests in the `test` directory for testing the
framework itself (sooo meta).  These help confirm that the system is working as
expected.
# Ruby Agent Performance Tests

This is a performance testing framework for the Ruby Agent.

## Motivation

There are two main goals driving the development of this framework:

1. Add a way for automated performance tests to be run against the Ruby Agent
   and ingested into a system for tracking these results over time.
2. Provide a tool for Ruby Agent engineers to use while working on performance
   improvements.

## Examples

### Invoking via rake task

Basic performance test invocations can be done using a rake task provided in the
newrelic_rpm Rakefile.

Run all performance tests, reporting results to the console:

```
$ rake test:performance
```

Run one specific suite:

```
$ rake test:performance[TransactionTracingPerfTests]
```

Run one specific suite and test (test name matching is via regex):

```
$ rake test:performance[TransactionTracingPerfTests,test_short_transactions]
```

### Invoking via the runner directly

More advanced options can be specified by invoking the runner script directly.
See `./test/performance/script/runner -h` for a full list of options.

Run all tests, report detailed results in a human-readable form

```
$ ./test/performance/script/runner
```

List all available test suites and names:

```
$ ./test/performance/script/runner -l
```

Run a specific test (test name matching is via regex):

```
$ ./test/performance/script/runner -n short
```

To compare results for a specific test between two versions of the code, use the
`-B` (for Baseline) and `-C` for (for Compare) switches:

```
$ ./test/performance/script/runner -n short -B
1 tests, 0 failures, 8.199975 s total
Saved 1 results as baseline.

... switch to another branch and run again with -C ...

$ ./test/performance/script/runner -n short -C
1 tests, 0 failures, 8.220509 s total
+-----------------------------------------------------+-----------+-----------+-------+---------------+--------------+--------------+
| name                                                | before    | after     | delta | allocs_before | allocs_after | allocs_delta |
|-----------------------------------------------------+-----------+-----------+-------+---------------+--------------+--------------|
| TransactionTracingPerfTests#test_short_transactions | 214.27 µs | 210.31 µs | -1.8% |            97 |           97 |         0.0% |
+-----------------------------------------------------+-----------+-----------+-------+---------------+--------------+--------------+
```

Run all the tests, produce machine readable JSON output (for eventual ingestion into a storage system):

```
$ ./test/performance/script/runner -j | json_reformat
```

Run a specific test under a profiler (either stackprof or perftools.rb, depending on your Ruby version):

```
$ ./test/performance/script/runner -n short --profile
```

Run with a set number of iterations, and do object allocation profiling (again to a call-graph dot file):

```
$ ./test/performance/script/runner -n short -a -N 1000
```

## Pointing at a different copy of the agent

If you want to run performance tests against an older copy of the agent that
doesn't have the performance test framework embedded within it, you can do that
by specifying the path to the agent you want to test against by passing the `-A`
flag to the `runner` script, or by setting the `AGENT_PATH` environment variable
when using the rake task.

## Sending results to Hako

This is currently considered experimental, but you can send results
automatically to Hako by passing `-R HakoReporter` on the command line to the
`runner`. This will produce JSON-formatted versions of each test result, and
submit them to Hako. You will need to set the `HAKO_TOKEN` environment variable
to a valid Hako access token when doing this.

## Writing tests

Performance tests are written in the style of `test/unit`: create a `.rb` file
under `test/performance/suites`, subclass `Performance::TestCase`, and write
test methods that start with `test_`. You can also write `setup` and `teardown`
methods that will be run before/after each test.

Within your `test_` method, you must call `measure` and pass it a block
containing the code that you'd like to actually measure the timing of. This
allows you to do test-specific setup that doesn't get counted towards your
test timing.

The block that you pass to `measure` will automatically be run in a loop for a
fixed amount of time by the performance runner harness (5s by default), and the
number of iterations performed will be recorded so that measurements can be
normalized to per-iteration values.

You can look at the [existing tests](suites) for examples.

## Test Isolation

Initial testing suggested that certain kinds of tests would have a large impact
on tests run later on in the same process (e.g. tests that create lots of
long-lived objects will slow down all future GC runs for as long as those
objects remain live).

In order to address this problem, the test runner will attempt to isolate each
test to its own process by re-spawning itself for each test invocation. This is
done using `IO.popen` rather than `Process.fork` in order to maintain
compatibility with JRuby.

Additionally, when operating in this mode, the `newrelic_rpm` gem will not be
loaded until *after* the fork call. This means that your **test cases must be
loadable (though not necessarily runnable) without the `newrelic_rpm` gem
avaiable**.

Not all command-line options to the runner work with this test isolation yet.
You can disable it by passing the `-I/--inline` flag to the runner.

## Adding instrumentation layers

The GC stats that are collected with each test run, and the perftools.rb
profiling are examples of Instrumentors which can be wrapped around each test run.

The basic idea is that each instrumentor gets callbacks before and after each
test, and add information to the test results, or attach artifacts (a fancy name
for file paths, currently) to the result.

Instrumentors inherit from `Performance::Instrumentation::Instrumentor`, and may
constrain themselves to running only on certain platforms (see `instrumentor.rb`
for a list) by calling the `platforms` method in their class definitions. They
may also signal that they should be used by default by calling `on_by_default`.
They should imlement the `before`, `after` and `results` methods as follows:

The `before` method is called before each test is run. The test class and test
name are passed as arguments.

The `after` method is called after each test is run. The test class, and test
name are passed as arguments. Artifacts may be attached to the result here by
appending to the `@artifacts` array. You may obtain paths to store artifacts at
by calling `Performance::Instrumentation::Instrumentor#artifact_path` (see
perf_tools.rb for an example).

The `results` method must return a Hash of key-value pairs to be attached to the
`Result` object produced by running each test.

If your instrumentation layer needs to do one-time setup (requiring a gem, for
example), implement the `setup` class method to do this setup.
= MiniPortile

* {Source Code}[https://github.com/flavorjones/mini_portile]
* {Bug Reports}[https://github.com/flavorjones/mini_portile/issues]

This project is a minimalistic, simplistic and stupid implementation of a port/recipe
system <b>for developers</b>.

== Another port system, srsly?

No, is not a general port system, is not aimed to take over apt, macports or
anything like that.

The rationale is simple.

You create a library A that uses B at runtime or compile time. Target audience
of your library might have different versions of B installed than yours.

You know, <em>Works on my machine</em> is not what you expect from one
developer to another.

Developers having problems report them back to you, and what you do then?
Compile B locally, replacing your existing installation of B or simply hacking
things around so nothing breaks.

All this, manually.

Computers are tools, are meant to help us, not the other way around.

What if I tell you the above scenario can be simplified with something like
this:

  rake compile B_VERSION=1.2.3

And your library will use the version of B you specified. Done.

== You make it sound easy, where is the catch?

You got me, there is a catch. At this time (and highly likely will be always)
MiniPortile is only compatible with GCC compilers and autoconf/configure-based
projects.

It assumes the library you want to build contains a <tt>configure</tt> script,
which all the autoconf-based libraries do.

=== How to use

Now that you know the catch, and you're still reading this, let me show you a
quick example:

  require "mini_portile"
  recipe = MiniPortile.new("libiconv", "1.13.1")
  recipe.files = ["http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.13.1.tar.gz"]
  recipe.cook
  recipe.activate

That's all. <tt>cook</tt> will download, extract, patch, configure and compile
the library into a namespaced structure. <tt>activate</tt> ensures GCC find
this library and prefers it over a system-wide installation.

=== Structure

At this time, if you haven't digged into the code yet, are wondering <em>what
is all that structure talk about?</em>.

MiniPortile follows the principle of <b>convention over configuration</b> and
established a folder structure where is going to place files and perform work.

Take the above example, and let's draw some picture:

  mylib
    |-- ports
    |   |-- archives
    |   |   `-- libiconv-1.13.1.tar.gz
    |   `-- <platform>
    |       `-- libiconv
    |           `-- 1.13.1
    |               |-- bin
    |               |-- include
    |               `-- lib
    `-- tmp
        `-- <platform>
            `-- ports

In above structure, <tt>platform</tt> refers to the architecture that represents
the operating system you're using (e.g. i686-linux, i386-mingw32, etc).

Inside this folder, MiniPortile will store the artifacts that result from the
compilation process. As you cans see, it versions out the library so you can
run multiple version combination without compromising these overlap each other.

<tt>archives</tt> is where downloaded source files are stored. It is recommended
you avoid trashing that folder so no further downloads will be required (save
bandwidth, save the world).

The <tt>tmp</tt> is where compilation is performed and can be safely discarded.

Don't worry, you don't need to know the path structure by memory, just use recipe's
<tt>path</tt> to obtain the full path to the installation directory:

  recipe.cook
  recipe.path # => /home/luis/projects/myapp/ports/i686-linux/libiconv/1.13.1

=== How can I combine this with my compilation task?

In the simplified proposal, the idea is that using Rake, your <tt>compile</tt>
task depends on MiniPortile compilation and most important, activation.

Take the following as a simplification of how you can use MiniPortile with
Rake:

  task :libiconv do
    recipe = MiniPortile.new("libiconv", "1.13.1")
    recipe.files = ["http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.13.1.tar.gz"]
    checkpoint = ".#{recipe.name}-#{recipe.version}.installed"

    unless File.exist?(checkpoint)
      recipe.cook
      touch checkpoint
    end

    recipe.activate
  end

  task :compile => [:libiconv] do
    # ...
  end

This example will:

* Compile the library only once (using a timestamp file)
* Ensure compiled library gets activated every time
* Make compile task depend on compiled library activation

For your homework, you can make libiconv version be taken from <tt>ENV</tt>
variables.

=== Native or cross-compilation

Above examples cover the normal use case: compile support libraries natively.

MiniPortile also covers another use case, which is the cross-compilation of the
support libraries to be used as part of a binary gem compilation.

It is the perfect complementary tool for rake-compiler and it's <tt>cross</tt>
Rake task.

Depending on your usage of rake-compiler, you will need to use <tt>host</tt> to
match the installed cross-compiler toolchain.

Please refer to the examples directory for simplified and practical usage.

=== Supported scenarios

As mentioned before, MiniPortile requires a GCC compiler toolchain. This has
been tested against Ubuntu, OSX and even Windows (RubyInstaller with DevKit)

== Disclaimer

If you have any trouble, don't hesitate to contact the author. As always,
I'm not going to say <em>Use at your own risk</em> because I don't want this
library to be risky.

If you trip on something, I'll share the liability by repairing things
as quickly as I can. Your responsibility is to report the inadequacies.

== License

This library is licensed under MIT license. Please see LICENSE.txt for details.
= mime-types

home :: https://github.com/mime-types/ruby-mime-types/
code :: https://github.com/mime-types/ruby-mime-types/
bugs :: https://github.com/mime-types/ruby-mime-types/issues
rdoc :: http://rdoc.info/gems/mime-types/
continuous integration :: {<img src="https://travis-ci.org/mime-types/ruby-mime-types.png" />}[https://travis-ci.org/mime-types/ruby-mime-types]
test coverage :: {<img src="https://coveralls.io/repos/mime-types/ruby-mime-types/badge.png" alt="Coverage Status" />}[https://coveralls.io/r/mime-types/ruby-mime-types]

== Description

The mime-types library provides a library and registry for information about
MIME content type definitions. It can be used to determine defined filename
extensions for MIME types, or to use filename extensions to look up the likely
MIME type definitions.

MIME content types are used in MIME-compliant communications, as in e-mail or
HTTP traffic, to indicate the type of content which is transmitted. The
mime-types library provides the ability for detailed information about MIME
entities (provided as an enumerable collection of MIME::Type objects) to be
determined and used. There are many types defined by RFCs and vendors, so the
list is long but by definition incomplete; don't hesitate to add additional
type definitions. MIME type definitions found in mime-types are from RFCs, W3C
recommendations, the {IANA Media Types
registry}[https://www.iana.org/assignments/media-types/media-types.xhtml], and
user contributions. It conforms to RFCs 2045 and 2231.

This is release 2.6 with two new experimental features. The first new feature
is a new default registry storage format that greatly reduces the initial
memory use of the mime-types library. This feature is enabled by requiring
+mime/types/columnar+ instead of +mime/types+ with a small performance cost and
no change in *total* memory use if certain methods are called (see {Columnar
Store}[#columnar-store] for more details). The second new feature is a logger
interface that conforms to the expectations of an ActiveSupport::Logger so that
warnings can be written to an application's log rather than the default
location for +warn+. This interface may be used for other logging purposes in
the future.

mime-types 2.6 is the last planned version of mime-types 2.x, so deprecation
warnings are no longer cached but provided every time the method is called.
mime-types 2.6 supports Ruby 1.9.2 or later.

=== mime-types 1.x End of Life

mime-types 2.0 was released in late 2013, and as of early 2015 there have been
no reported security issues for mime-types 1.x. With the release of mime-types
2.5, I set the formal End of Life for mime-types 1.x for 2015-10-27 (the second
anniversary of the release of mime-types 2.0). After this date, absolutely no
pull requests for mime-types 1.x will be accepted.

=== mime-types Future

There are a number of issues open that make clear to me that there are some
fundamental changes that need to happen to both the data representation and the
API provided by mime-types. This cannot happen under the current release, so
all new development is focussing on an upcoming 3.0 release. The target for the
release is on or before the beginning of RubyConf 2015 (2015-11-15).

When 3.0 is released, mime-types 2.x will receive regular updates of the IANA
registry for two years following the release. It will also receive security
updates, if needed, for the same period. There will be no further feature
development on mime-types 2.x following the 3.0 release.

Coincident with the 3.0 release, I will release mime-types 2.99.0 that no
longer imports the data to fields that have been deprecated, or exports it if
it is present. If they work because they derive data from the data that is
still present, the will continue to work. The quarterly updates will be against
2.99.x.

If the possible loss of this deprecated data matters, be sure to set your
dependency appropriately:

   gem 'mime-types', '~> 2.6, < 2.99'

== Synopsis

MIME types are used in MIME entities, as in email or HTTP traffic. It is useful
at times to have information available about MIME types (or, inversely, about
files). A MIME::Type stores the known information about one MIME type.

   require 'mime/types'

   plaintext = MIME::Types['text/plain'] # => [ text/plain ]
   text = plaintext.first
   puts text.media_type            # => 'text'
   puts text.sub_type              # => 'plain'

   puts text.extensions.join(' ')  # => 'txt asc c cc h hh cpp hpp dat hlp'
   puts text.preferred_extension   # => 'txt'
   puts text.friendly              # => 'Text Document'
   puts text.i18n_key              # => 'text.plain'

   puts text.encoding              # => quoted-printable
   puts text.default_encoding      # => quoted-printable
   puts text.binary?               # => false
   puts text.ascii?                # => true
   puts text.obsolete?             # => false
   puts text.registered?           # => true
   puts text.complete?             # => true

   puts text                       # => 'text/plain'

   puts text == 'text/plain'       # => true
   puts 'text/plain' == text       # => true
   puts text == 'text/x-plain'     # => false
   puts 'text/x-plain' == text     # => false

   puts MIME::Type.simplified('x-appl/x-zip') # => 'appl/zip'
   puts MIME::Type.i18n_key('x-appl/x-zip') # => 'appl.zip'

   puts text.like?('text/x-plain') # => true
   puts text.like?(MIME::Type.new('x-text/x-plain')) # => true

   puts text.xrefs.inspect # => { "rfc" => [ "rfc2046", "rfc3676", "rfc5147" ] }
   puts text.urls # => [ "http://www.iana.org/go/rfc2046",
                  #      "http://www.iana.org/go/rfc3676",
                  #      "http://www.iana.org/go/rfc5147" ]

   xtext = MIME::Type.new('x-text/x-plain')
   puts xtext.media_type # => 'text'
   puts xtext.raw_media_type # => 'x-text'
   puts xtext.sub_type # => 'plain'
   puts xtext.raw_sub_type # => 'x-plain'
   puts xtext.complete? # => false

   puts MIME::Types.any? { |type| type.content_type == 'text/plain' } # => true
   puts MIME::Types.all?(&:registered?) # => false

   # Various string representations of MIME types
   qcelp = MIME::Types['audio/QCELP'].first # => audio/QCELP
   puts qcelp.content_type         # => 'audio/QCELP'
   puts qcelp.simplified           # => 'audio/qcelp'

   xwingz = MIME::Types['application/x-Wingz'].first # => application/x-Wingz
   puts xwingz.content_type        # => 'application/x-Wingz'
   puts xwingz.simplified          # => 'application/wingz'

=== Columnar Store

mime-types 2.6 has an experimental columnar storage format that reduces the
default memory footprint. It does this by selectively loading data. When a
registry is first loaded from a columnar store, only the canonical MIME type
and registered extensions will be loaded and the MIME type will be connected to
its registry. When extended data is required (including #registered, #obsolete,
#use_instead), that data is loaded from its own column file for all types in
the registry. This load is done with a Mutex to ensure that the types are
updated safely in a multithreaded environment.

Columnar storage is slated to become the default storage format for mime-types
3.0, but until that is released, the default is still to use the JSON storage
format. As such, columnar storage can only currently be loaded at an
application level with the following specification in the application Gemfile:

   gem 'mime-types', require: 'mime/types/columnar'

Projects that do not use Bundler, and libraries that wish to suggest this
behaviour to applications are encouraged to require this directly, but only if
you specify a dependency on mime-types 2.6.

   require 'mime/types/columnar'

Although this require will not be necessary after mime-types 3, it will work
through at least {version
4}[https://github.com/mime-types/ruby-mime-types/pull/96#issuecomment-100725400]
and possibly beyond.

Note that the new Columnar class (MIME::Type::Columnar) and module
(MIME::Types::Columnar) are considered private variant implementations of
MIME::Type and MIME::Types and the specific implementation should not be relied
upon by consumers of the mime-types library. Instead, depend on the public
implementations only.

=== Cached Storage

Since version 2.0, mime-types has supported a cache of MIME types based on
<tt>Marshal.dump</tt>. The cache is invalidated for each released version of
mime-types so that version 2.5 is not reused for version 2.6. If the
environment variable +RUBY_MIME_TYPES_CACHE+ is set to a cache file, mime-types
will attempt to load the MIME type registry from the cache file. If it cannot,
it will load the types normally and then saves the registry to the cache file.

The current mime-types cache is not compatible with the columnar storage
format. This will be resolved for mime-types 3.

== mime-types Modified Semantic Versioning

The mime-types library has one version number, but this single version number
tracks both API changes and registry data changes; this is not wholly
compatible with all aspects of {Semantic Versioning}[http://semver.org/];
removing a MIME type from the registry *could* be considered a breaking change
under some interpretations of semantic versioning (as lookups for that
particular type would no longer work by default).

mime-types uses a modified semantic versioning scheme. Given the version
MAJOR.MINOR:

1. If an incompatible API (code) change is made, the MAJOR version will be
   incremented, MINOR will be set to zero, and PATCH will be reset to the
   implied zero.

2. If an API (code) feature is added that does not break compatibilty OR if
   there are MIME types added, removed, or changed in the registry, the MINOR
   version will be incremented and PATCH will be reset to the implied zero.

3. If there is a bugfix to a feature added in the most recent MAJOR.MINOR
   release, OR if purely typographical errors are fixed in MIME types, the
   implied PATCH value will be incremented resulting in MAJOR.MINOR.PATCH.

In practical terms, there should be a MINOR release roughly monthly to track
updated or changed MIME types from the official IANA registry. This does not
indicate when new API features have been added, but all minor versions of
mime-types 2.x will be backwards compatible; the interfaces marked deprecated
will be removed in mime-types 3.x.

:include: Contributing.rdoc

:include: Licence.rdoc
= SexpProcessor

home :: https://github.com/seattlerb/sexp_processor
rdoc :: http://docs.seattlerb.org/sexp_processor

== DESCRIPTION:

sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all
for your language processing pleasure.

== FEATURES/PROBLEMS:

* Includes SexpProcessor and CompositeSexpProcessor.

  * Allows you to write very clean filters.

* Sexp provides a simple and clean interface to creating and manipulating ASTs.

== SYNOPSIS:

  class MyProcessor < SexpProcessor
    def initialize
      super
      self.strict = false
    end
    def process_lit(exp)
      val = exp.shift
      return val
    end
  end

== REQUIREMENTS:

* rubygems

== INSTALL:

* sudo gem install sexp_processor

== LICENSE:

(The MIT License)

Copyright (c) Ryan Davis, seattle.rb

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Rails::Dom::Testing
[![Build Status](https://travis-ci.org/rails/rails-dom-testing.svg)](https://travis-ci.org/rails/rails-dom-testing)

This gem is responsible for comparing HTML doms and asserting that DOM elements are present in Rails applications.
Doms are compared via `assert_dom_equal` and `assert_dom_not_equal`.
Elements are asserted via `assert_select`, `assert_select_encoded`, `assert_select_email` and a subset of the dom can be selected with `css_select`.
The gem is developed for Rails 4.2 and above, and will not work on previous versions.

## Deprecation warnings when upgrading to Rails 4.2:

Nokogiri is slightly more strict about the format of css selectors than the previous implementation. That's why you have warnings like:

```
DEPRECATION WARNING: The assertion was not run because of an invalid css selector.
```

Check the 4.2 release notes [section on `assert_select`](http://edgeguides.rubyonrails.org/4_2_release_notes.html#assert-select) for help.

## Installation

Add this line to your application's Gemfile:

    gem 'rails-dom-testing'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install rails-dom-testing

## Usage

### Dom Assertions

```ruby
assert_dom_equal '<h1>Lingua França</h1>', '<h1>Lingua França</h1>'

assert_dom_not_equal '<h1>Portuguese</h1>', '<h1>Danish</h1>'
```

### Selector Assertions

```ruby
# implicitly selects from the document_root_element
css_select '.hello' # => Nokogiri::XML::NodeSet of elements with hello class

# select from a supplied node. assert_select asserts elements exist.
assert_select document_root_element.at('.hello'), '.goodbye'

# elements in CDATA encoded sections can also be selected
assert_select_encoded '#out-of-your-element'

# assert elements within an html email exists
assert_select_email '#you-got-mail'
```

The documentation in [selector_assertions.rb](https://github.com/kaspth/rails-dom-testing/blob/master/lib/rails/dom/testing/assertions/selector_assertions.rb) goes into a lot more detail of how selector assertions can be used.

## Read more

Under the hood the doms are parsed with Nokogiri and you'll generally be working with these two classes:
- [`Nokogiri::XML::Node`](http://nokogiri.org/Nokogiri/XML/Node.html)
- [`Nokogiri::XML::NodeSet`](http://nokogiri.org/Nokogiri/XML/NodeSet.html)

Read more about Nokogiri:
- [Nokogiri](http://nokogiri.org)

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
Airbrake on Heroku
==================

Send your application errors to our hosted service and reclaim your inbox.

1. Installing the Heroku add-on
----------------------------
To use Airbrake on Heroku, install the Airbrake add-on:

    $ heroku addons:add airbrake:developer # If you'd like another plan, specify that instead.
                                           # Check https://addons.heroku.com/airbrake for a full list of plans.

2. Including the Airbrake notifier in your application
--------------------------------------------------
After adding the Airbrake add-on, you will need to install and configure the Airbrake notifier.

Your application connects to Airbrake with an API key. On Heroku, this is automatically provided to your
application in `ENV['AIRBRAKE_API_KEY']`, so installation should be a snap!

### Rails 3.x

Add the airbrake and heroku gems to your Gemfile.  In Gemfile:

    gem 'airbrake'
    gem 'heroku'

Then from your project's RAILS_ROOT, run:

    $ bundle install
    $ script/rails generate airbrake --heroku

### Rails 2.x

Install the heroku gem if you haven't already:

    gem install heroku

Add the airbrake gem to your app. In config/environment.rb:

    config.gem 'airbrake'

Then from your project's RAILS_ROOT, run:

    $ rake gems:install
    $ rake gems:unpack GEM=airbrake
    $ script/generate airbrake --heroku

As always, if you choose not to vendor the airbrake gem, make sure
every server you deploy to has the gem installed or your application won't start.

### Rack applications

In order to use airbrake in a non-Rails rack app, just load the airbrake, configure your API key, and use the Airbrake::Rack middleware:

    require 'rubygems'
    require 'rack'
    require 'airbrake'

    Airbrake.configure do |config|
      config.api_key = `ENV['AIRBRAKE_API_KEY']`
    end

    app = Rack::Builder.app do
      use Airbrake::Rack
      run lambda { |env| raise "Rack down" }
    end

### Rails 1.x

For Rails 1.x, visit the [Airbrake's README on GitHub](http://github.com/airbrake/airbrake),
and be sure to use `ENV['AIRBRAKE_API_KEY']` where your API key is required in configuration code.

3. Configure your notification settings (important!)
---------------------------------------------------

Once you have included and configured the notifier in your application,
you will want to configure your notification settings.

This is important - without setting your email address, you won't receive notification emails.

Airbrake can deliver exception notifications to your email inbox.  To configure these delivery settings:

1. Visit your applications resources page, like [ http://api.heroku.com/myapps/my-great-app/resources ](http://api.heroku.com/myapps/my-great-app/resources).
2. Click the name of your Airbrake addon. (It may still be called Hoptoad.)
3. Click "Settings" to configure the Airbrake Add-on.

4. Optionally: Set up deploy notification
-----------------------------------------

If your Airbrake plan supports deploy notification, set it up for your Heroku application like this:

    rake airbrake:heroku:add_deploy_notification

This will install a Heroku [HTTP Deploy Hook](http://docs.heroku.com/deploy-hooks) to notify Airbrake of the deploy.

You can pass in additional information for the deploy hook, in the ENV. Here are the available parameters:
* `ENV["RAILS_ENV"]`         - Rails environment you're deploying to, if not set on Heroku
* `ENV["AIRBRAKE_API_KEY"]`  - API key if not saved on Heroku or in initializer
* `ENV["HEROKU_APP"]`        - app name if you have multiple Heroku apps
* `ENV["REPO"]`              - Github url of the repo you're deploying, set this if you're not using remote named "origin"

We will also set "username" and "revision" from Heroku variables.
Airbrake
========

[![Circle CI](https://circleci.com/gh/airbrake/airbrake/tree/master.png?circle-token=66cb9cfc6d20f550a2dbde522f5f0f9f81bd653b)](https://circleci.com/gh/airbrake/airbrake)
[![Code Climate](https://codeclimate.com/github/airbrake/airbrake.png)](https://codeclimate.com/github/airbrake/airbrake)
[![Coverage Status](https://coveralls.io/repos/airbrake/airbrake/badge.png?branch=master)](https://coveralls.io/r/airbrake/airbrake?branch=master)
[![Dependency Status](https://gemnasium.com/airbrake/airbrake.png)](https://gemnasium.com/airbrake/airbrake)

<img src="http://f.cl.ly/items/3Q163w1r2K1J1b030k0g/ruby%2009.19.32.jpg" width=800px>

This is the notifier gem for integrating apps with [Airbrake](http://airbrake.io).

When an uncaught exception occurs, Airbrake will POST the relevant data
to the Airbrake server specified in your environment.

<img scr="http://f.cl.ly/items/142j0Z2u0R1Y2L0L3D26/ruby.jpg" width=800px;>

Help
----

For help with using Airbrake and this notifier visit [our support site](http://help.airbrake.io).

For **SSL** verification see the [Resources](https://github.com/airbrake/airbrake/blob/master/resources/README.md).

Rails Installation
------------------

### Rails 3.x/4.x

Add the airbrake gem to your Gemfile.  In Gemfile:

    gem 'airbrake'

Then from your project's RAILS_ROOT, and in your development environment, run:

    bundle install
    rails generate airbrake --api-key your_key_here

The generator creates a file under `config/initializers/airbrake.rb` configuring Airbrake with your API key. This file should be checked into your version control system so that it is deployed to your staging and production environments.

### Rails 2.x

Add the airbrake gem to your app. In config/environment.rb:

    config.gem 'airbrake'

or if you are using bundler:

    gem 'airbrake', :require => 'airbrake/rails'

Then from your project's RAILS_ROOT, and in your development environment, run:

    rake gems:install
    rake gems:unpack GEM=airbrake
    script/generate airbrake --api-key your_key_here

As always, if you choose not to vendor the airbrake gem, make sure
every server you deploy to has the gem installed or your application won't start.

The generator creates a file under `config/initializers/airbrake.rb` configuring Airbrake with your API key. This file should be checked into your version control system so that it is deployed to your staging and production environments.

Ignored exceptions
------------------------

Exceptions raised from Rails environments named **development**, **test** or **cucumber** will be ignored by default.

You can clear the list of ignored environments with this setting:

    config.development_environments = []

List of ignored exception classes includes:

    ActiveRecord::RecordNotFound
    ActionController::RoutingError
    ActionController::InvalidAuthenticityToken
    CGI::Session::CookieStore::TamperedWithCookie
    ActionController::UnknownHttpMethod
    ActionController::UnknownAction
    AbstractController::ActionNotFound
    Mongoid::Errors::DocumentNotFound
    ActionController::UnknownFormat

You can alter this list with

    config.ignore_only = []

which will cause none of the exception classes to be ignored.

Check the [wiki](https://github.com/airbrake/airbrake/wiki/Customizing-your-airbrake.rb) for more customization options.

Supported frameworks
------------------------

See **[TESTED_AGAINST](https://github.com/airbrake/airbrake/blob/master/TESTED_AGAINST)** for a full list of frameworks and versions we test against.

Airbrake wiki pages
------------------------
Our wiki contains a lot of additional information about Airbrake configuration. Please browse the wiki when finished reading this
README:

https://github.com/airbrake/airbrake/wiki

Development
-----------

For running unit tests, you should run

    bundle
    bundle exec rake test:unit

If you wish to run the entire suite, which checks the different framework
integrations with cucumber, you should run the following commands

    bundle
    bundle exec rake appraisal:install
    bundle exec rake

We use [Appraisals](https://github.com/thoughtbot/appraisal) to run the integration
tests.

Maintainers
-----------

Make sure all tests are passing before pushing the new version. Also, make sure integration
test is passing. You can run it with:

    ./script/integration_test.rb <api_key> <host>

After this is passing, change the version inside *lib/airbrake/version.rb* and
push the new version with Changeling:

    rake changeling:change

Credits
-------

![thoughtbot](https://secure.gravatar.com/avatar/a95a04df2dae60397c38c9bd04492c53)

Airbrake is maintained and funded by [airbrake.io](http://airbrake.io).

Thank you to all [the contributors](https://github.com/airbrake/airbrake/contributors)!

The names and logos for Airbrake, thoughtbot are trademarks of their respective holders.

License
-------

Airbrake is Copyright © 2008-2015 Airbrake.
Airbrake Resources
==================

Airbrake has an SSL mode available to paying plans. SSL Certificate Authority (CA) certificates are not kept current by default on many environments. When CA certs are stale, Airbrake cannot verify Airbrake's production SSL cert and error reports fail. To avoid this, we now package local CA certs. The production of these certs is detailed here.

Building ca-bundle.crt
----------------------

From https://gist.github.com/996292.

If you want to use curl or net-http/open-uri to access https resources, you will often (always?) get an error, because they don't have the large number of root certificates installed that web browsers have.

You can manually install the root certs, but first you have to get them from somewhere. [This article](http://notetoself.vrensk.com/2008/09/verified-https-in-ruby/) gives a nice description of how to do that. The [source of the cert files](http://curl.haxx.se/ca/cacert.pem) it points to is hosted by the curl project, who kindly provide it in the .pem format.

**problem:** Sadly, ironically, and comically, it's not possible to access that file via https! Luckily, the awesome curl project does provide us with the script that they use to produce the file, so we can do it securely ourselves. Here's how.

1. `git clone https://github.com/bagder/curl.git`
2. `cd curl/lib`
3. edit `mk-ca-bundle.pl` and change:

    ```perl
    my $url = 'http://mxr.mozilla.org/mozilla/source/security/nss/lib/ckfw/builtins/certdata.txt?raw=1';
    ```

    to

    ```perl
    my $url = 'https://mxr.mozilla.org/mozilla/source/security/nss/lib/ckfw/builtins/certdata.txt?raw=1';
    ```

    (change `http` to `https`)
4. `./mk-ca-bundle.pl`

Ta da!
# MultiJSON

[![Gem Version](http://img.shields.io/gem/v/multi_json.svg)][gem]
[![Build Status](http://travis-ci.org/intridea/multi_json.svg)][travis]
[![Dependency Status](http://img.shields.io/gemnasium/intridea/multi_json.svg)][gemnasium]
[![Code Climate](http://img.shields.io/codeclimate/github/intridea/multi_json.svg)][codeclimate]

[gem]: https://rubygems.org/gems/multi_json
[travis]: http://travis-ci.org/intridea/multi_json
[gemnasium]: https://gemnasium.com/intridea/multi_json
[codeclimate]: https://codeclimate.com/github/intridea/multi_json

Lots of Ruby libraries parse JSON and everyone has their favorite JSON coder.
Instead of choosing a single JSON coder and forcing users of your library to be
stuck with it, you can use MultiJSON instead, which will simply choose the
fastest available JSON coder. Here's how to use it:

```ruby
require 'multi_json'

MultiJson.load('{"abc":"def"}') #=> {"abc" => "def"}
MultiJson.load('{"abc":"def"}', :symbolize_keys => true) #=> {:abc => "def"}
MultiJson.dump({:abc => 'def'}) # convert Ruby back to JSON
MultiJson.dump({:abc => 'def'}, :pretty => true) # encoded in a pretty form (if supported by the coder)
```

When loading invalid JSON, MultiJson will throw a `MultiJson::ParseError`. `MultiJson::DecodeError` and `MultiJson::LoadError` are aliases for backwards compatibility.

```ruby
begin
  MultiJson.load('{invalid json}')
rescue MultiJson::ParseError => exception
  exception.data # => "{invalid json}"
  exception.cause # => JSON::ParserError: 795: unexpected token at '{invalid json}'
end
```

`ParseError` instance has `cause` reader which contains the original exception.
It also has `data` reader with the input that caused the problem.

The `use` method, which sets the MultiJson adapter, takes either a symbol or a
class (to allow for custom JSON parsers) that responds to both `.load` and `.dump`
at the class level.

When MultiJson fails to load the specified adapter, it'll throw `MultiJson::AdapterError`
which inherits from `ArgumentError`.

MultiJSON tries to have intelligent defaulting. That is, if you have any of the
supported engines already loaded, it will utilize them before attempting to
load any. When loading, libraries are ordered by speed. First Oj, then Yajl,
then the JSON gem, then JSON pure. If no other JSON library is available,
MultiJSON falls back to [OkJson][], a simple, vendorable JSON parser.

[okjson]: https://github.com/kr/okjson

## Supported JSON Engines

* [Oj](https://github.com/ohler55/oj) Optimized JSON by Peter Ohler
* [Yajl](https://github.com/brianmario/yajl-ruby) Yet Another JSON Library by Brian Lopez
* [JSON](https://github.com/flori/json) The default JSON gem with C-extensions (ships with Ruby 1.9)
* [JSON Pure](https://github.com/flori/json) A Ruby variant of the JSON gem
* [NSJSONSerialization](https://developer.apple.com/library/ios/#documentation/Foundation/Reference/NSJSONSerialization_Class/Reference/Reference.html) Wrapper for Apple's NSJSONSerialization in the Cocoa Framework (MacRuby only)
* [gson.rb](https://github.com/avsej/gson.rb) A Ruby wrapper for google-gson library (JRuby only)
* [JrJackson](https://github.com/guyboertje/jrjackson) JRuby wrapper for Jackson (JRuby only)
* [OkJson][okjson] A simple, vendorable JSON parser

## Supported Ruby Versions
This library aims to support and is [tested against][travis] the following Ruby
implementations:

* Ruby 1.8.7
* Ruby 1.9.2
* Ruby 1.9.3
* Ruby 2.0.0
* Ruby 2.1.1
* [JRuby][]
* [Rubinius][]
* [MacRuby][] (not tested on Travis CI)

[jruby]: http://www.jruby.org/
[rubinius]: http://rubini.us/
[macruby]: http://www.macruby.org/

If something doesn't work on one of these interpreters, it's a bug.

This library may inadvertently work (or seem to work) on other Ruby
implementations, however support will only be provided for the versions listed
above.

If you would like this library to support another Ruby version, you may
volunteer to be a maintainer. Being a maintainer entails making sure all tests
run and pass on that implementation. When something breaks on your
implementation, you will be responsible for providing patches in a timely
fashion. If critical issues for a particular implementation exist at the time
of a major release, support for that Ruby version may be dropped.

## Versioning

This library aims to adhere to [Semantic Versioning 2.0.0][semver]. Violations
of this scheme should be reported as bugs. Specifically, if a minor or patch
version is released that breaks backward compatibility, that version should be
immediately yanked and/or a new version should be immediately released that
restores compatibility. Breaking changes to the public API will only be
introduced with new major versions. As a result of this policy, you can (and
should) specify a dependency on this gem using the [Pessimistic Version
Constraint][pvc] with two digits of precision. For example:

```ruby
spec.add_dependency 'multi_json', '~> 1.0'
```

[semver]: http://semver.org/
[pvc]: http://docs.rubygems.org/read/chapter/16#page74

## Copyright
Copyright (c) 2010-2013 Michael Bleigh, Josh Kalderimis, Erik Michaels-Ober,
and Pavel Pravosud. See [LICENSE][] for details.

[license]: LICENSE.md
# Threadsafe

[![Gem Version](https://badge.fury.io/rb/thread_safe.svg)](http://badge.fury.io/rb/thread_safe) [![Build Status](https://travis-ci.org/ruby-concurrency/thread_safe.svg?branch=master)](https://travis-ci.org/ruby-concurrency/thread_safe) [![Coverage Status](https://img.shields.io/coveralls/ruby-concurrency/thread_safe/master.svg)](https://coveralls.io/r/ruby-concurrency/thread_safe) [![Code Climate](https://codeclimate.com/github/ruby-concurrency/thread_safe.svg)](https://codeclimate.com/github/ruby-concurrency/thread_safe) [![Dependency Status](https://gemnasium.com/ruby-concurrency/thread_safe.svg)](https://gemnasium.com/ruby-concurrency/thread_safe) [![License](https://img.shields.io/badge/license-apache-green.svg)](http://opensource.org/licenses/MIT) [![Gitter chat](http://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-brightgreen.svg)](https://gitter.im/ruby-concurrency/concurrent-ruby)

A collection of thread-safe versions of common core Ruby classes.

## Installation

Add this line to your application's Gemfile:

    gem 'thread_safe'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install thread_safe

## Usage

```ruby
require 'thread_safe'

sa = ThreadSafe::Array.new # supports standard Array.new forms
sh = ThreadSafe::Hash.new # supports standard Hash.new forms
```

`ThreadSafe::Cache` also exists, as a hash-like object, and should have
much better performance characteristics esp. under high concurrency than
`ThreadSafe::Hash`. However, `ThreadSafe::Cache` is not strictly semantically
equivalent to a ruby `Hash` -- for instance, it does not necessarily retain
ordering by insertion time as `Hash` does. For most uses it should do fine
though, and we recommend you consider `ThreadSafe::Cache` instead of
`ThreadSafe::Hash` for your concurrency-safe hash needs. It understands some
options when created (depending on your ruby platform) that control some of the
internals - when unsure just leave them out:


```ruby
require 'thread_safe'

cache = ThreadSafe::Cache.new
```

## Contributing

1. Fork it
2. Clone it (`git clone git@github.com:you/thread_safe.git`)
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Build the jar (`rake jar`) NOTE: Requires JRuby
5. Install dependencies (`bundle install`)
6. Commit your changes (`git commit -am 'Added some feature'`)
7. Push to the branch (`git push origin my-new-feature`)
8. Create new Pull Request
Thor
====

[![Gem Version](http://img.shields.io/gem/v/thor.svg)][gem]
[![Build Status](http://img.shields.io/travis/erikhuda/thor.svg)][travis]
[![Dependency Status](http://img.shields.io/gemnasium/erikhuda/thor.svg)][gemnasium]
[![Code Climate](http://img.shields.io/codeclimate/github/erikhuda/thor.svg)][codeclimate]
[![Coverage Status](http://img.shields.io/coveralls/erikhuda/thor.svg)][coveralls]

[gem]: https://rubygems.org/gems/thor
[travis]: http://travis-ci.org/erikhuda/thor
[gemnasium]: https://gemnasium.com/erikhuda/thor
[codeclimate]: https://codeclimate.com/github/erikhuda/thor
[coveralls]: https://coveralls.io/r/erikhuda/thor

Description
-----------
Thor is a simple and efficient tool for building self-documenting command line
utilities.  It removes the pain of parsing command line options, writing
"USAGE:" banners, and can also be used as an alternative to the [Rake][rake]
build tool.  The syntax is Rake-like, so it should be familiar to most Rake
users.

[rake]: https://github.com/jimweirich/rake

Installation
------------
    gem install thor

Usage and documentation
-----------------------
Please see the [wiki][] for basic usage and other documentation on using Thor. You can also checkout the [official homepage][homepage].

[wiki]: https://github.com/erikhuda/thor/wiki
[homepage]: http://whatisthor.com/

License
-------
Released under the MIT License.  See the [LICENSE][] file for further details.

[license]: LICENSE.md
__start__
README
__end__
__start__
README
__end__
__start__
README
__end__
__start__
README
__end__
Moped [![Build Status](https://secure.travis-ci.org/mongoid/moped.svg?branch=master)](http://travis-ci.org/mongoid/moped) [![Code Climate](https://codeclimate.com/github/mongoid/moped.svg)](https://codeclimate.com/github/mongoid/moped) [![Coverage Status](https://coveralls.io/repos/mongoid/moped/badge.png?branch=master)](https://coveralls.io/r/mongoid/moped?branch=master)
========

Moped is a MongoDB driver for Ruby, which exposes a simple, elegant, and fast
API.

Project Tracking
----------------

* [Mongoid Google Group](http://groups.google.com/group/mongoid)
* [Moped Website and Documentation](http://mongoid.org/en/moped/)
* [Moped Code Climate](https://codeclimate.com/github/mongoid/moped)

Compatibility
-------------

Moped is tested against MRI 1.9.3, 2.0.0, and JRuby (1.9).

Documentation
-------------

Please see the new Mongoid website for up-to-date documentation in
the Moped section: [mongoid.org](http://mongoid.org/en/moped/)

License
-------

Copyright (c) 2011-2014 Bernerd Schaefer, Durran Jordan

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Credits
-------

Bernerd Schaefer and Durran Jordan
= JSON implementation for Ruby {<img src="https://secure.travis-ci.org/flori/json.png" />}[http://travis-ci.org/flori/json]

== Description

This is a implementation of the JSON specification according to RFC 4627
http://www.ietf.org/rfc/rfc4627.txt . Starting from version 1.0.0 on there
will be two variants available:

* A pure ruby variant, that relies on the iconv and the stringscan
  extensions, which are both part of the ruby standard library.
* The quite a bit faster native extension variant, which is in parts
  implemented in C or Java and comes with its own unicode conversion
  functions and a parser generated by the ragel state machine compiler
  http://www.cs.queensu.ca/~thurston/ragel .

Both variants of the JSON generator generate UTF-8 character sequences by
default. If an :ascii_only option with a true value is given, they escape all
non-ASCII and control characters with \uXXXX escape sequences, and support
UTF-16 surrogate pairs in order to be able to generate the whole range of
unicode code points.

All strings, that are to be encoded as JSON strings, should be UTF-8 byte
sequences on the Ruby side. To encode raw binary strings, that aren't UTF-8
encoded, please use the to_json_raw_object method of String (which produces
an object, that contains a byte array) and decode the result on the receiving
endpoint.

The JSON parsers can parse UTF-8, UTF-16BE, UTF-16LE, UTF-32BE, and UTF-32LE
JSON documents under Ruby 1.8. Under Ruby 1.9 they take advantage of Ruby's
M17n features and can parse all documents which have the correct
String#encoding set. If a document string has ASCII-8BIT as an encoding the
parser attempts to figure out which of the UTF encodings from above it is and
trys to parse it.

== Installation

It's recommended to use the extension variant of JSON, because it's faster than
the pure ruby variant. If you cannot build it on your system, you can settle
for the latter.

Just type into the command line as root:

  # rake install

The above command will build the extensions and install them on your system.

  # rake install_pure

or

  # ruby install.rb

will just install the pure ruby implementation of JSON.

If you use Rubygems you can type

  # gem install json

instead, to install the newest JSON version.

There is also a pure ruby json only variant of the gem, that can be installed
with:

  # gem install json_pure

== Compiling the extensions yourself

If you want to build the extensions yourself you need rake:

  You can get it from rubyforge:
    http://rubyforge.org/projects/rake

  or just type

  # gem install rake

  for the installation via rubygems.

If you want to create the parser.c file from its parser.rl file or draw nice
graphviz images of the state machines, you need ragel from: http://www.cs.queensu.ca/~thurston/ragel


== Usage

To use JSON you can
  require 'json'
to load the installed variant (either the extension 'json' or the pure
variant 'json_pure'). If you have installed the extension variant, you can
pick either the extension variant or the pure variant by typing
  require 'json/ext'
or
  require 'json/pure'

Now you can parse a JSON document into a ruby data structure by calling

  JSON.parse(document)

If you want to generate a JSON document from a ruby data structure call
  JSON.generate(data)

You can also use the pretty_generate method (which formats the output more
verbosely and nicely) or fast_generate (which doesn't do any of the security
checks generate performs, e. g. nesting deepness checks).

To create a valid JSON document you have to make sure, that the output is
embedded in either a JSON array [] or a JSON object {}. The easiest way to do
this, is by putting your values in a Ruby Array or Hash instance.

There are also the JSON and JSON[] methods which use parse on a String or
generate a JSON document from an array or hash:

  document = JSON 'test'  => 23 # => "{\"test\":23}"
  document = JSON['test'] => 23 # => "{\"test\":23}"

and

  data = JSON '{"test":23}'  # => {"test"=>23}
  data = JSON['{"test":23}'] # => {"test"=>23}

You can choose to load a set of common additions to ruby core's objects if
you
  require 'json/add/core'

After requiring this you can, e. g., serialise/deserialise Ruby ranges:

  JSON JSON(1..10) # => 1..10

To find out how to add JSON support to other or your own classes, read the
section "More Examples" below.

To get the best compatibility to rails' JSON implementation, you can
  require 'json/add/rails'

Both of the additions attempt to require 'json' (like above) first, if it has
not been required yet.

== More Examples

To create a JSON document from a ruby data structure, you can call
JSON.generate like that:

 json = JSON.generate [1, 2, {"a"=>3.141}, false, true, nil, 4..10]
 # => "[1,2,{\"a\":3.141},false,true,null,\"4..10\"]"

To get back a ruby data structure from a JSON document, you have to call
JSON.parse on it:

 JSON.parse json
 # => [1, 2, {"a"=>3.141}, false, true, nil, "4..10"]

Note, that the range from the original data structure is a simple
string now. The reason for this is, that JSON doesn't support ranges
or arbitrary classes. In this case the json library falls back to call
Object#to_json, which is the same as #to_s.to_json.

It's possible to add JSON support serialization to arbitrary classes by
simply implementing a more specialized version of the #to_json method, that
should return a JSON object (a hash converted to JSON with #to_json) like
this (don't forget the *a for all the arguments):

 class Range
   def to_json(*a)
     {
       'json_class'   => self.class.name, # = 'Range'
       'data'         => [ first, last, exclude_end? ]
     }.to_json(*a)
   end
 end

The hash key 'json_class' is the class, that will be asked to deserialise the
JSON representation later. In this case it's 'Range', but any namespace of
the form 'A::B' or '::A::B' will do. All other keys are arbitrary and can be
used to store the necessary data to configure the object to be deserialised.

If a the key 'json_class' is found in a JSON object, the JSON parser checks
if the given class responds to the json_create class method. If so, it is
called with the JSON object converted to a Ruby hash. So a range can
be deserialised by implementing Range.json_create like this:

 class Range
   def self.json_create(o)
     new(*o['data'])
   end
 end

Now it possible to serialise/deserialise ranges as well:

 json = JSON.generate [1, 2, {"a"=>3.141}, false, true, nil, 4..10]
 # => "[1,2,{\"a\":3.141},false,true,null,{\"json_class\":\"Range\",\"data\":[4,10,false]}]"
 JSON.parse json
 # => [1, 2, {"a"=>3.141}, false, true, nil, 4..10]

JSON.generate always creates the shortest possible string representation of a
ruby data structure in one line. This is good for data storage or network
protocols, but not so good for humans to read. Fortunately there's also
JSON.pretty_generate (or JSON.pretty_generate) that creates a more readable
output:

 puts JSON.pretty_generate([1, 2, {"a"=>3.141}, false, true, nil, 4..10])
 [
   1,
   2,
   {
     "a": 3.141
   },
   false,
   true,
   null,
   {
     "json_class": "Range",
     "data": [
       4,
       10,
       false
     ]
   }
 ]

There are also the methods Kernel#j for generate, and Kernel#jj for
pretty_generate output to the console, that work analogous to Core Ruby's p and
the pp library's pp methods.

The script tools/server.rb contains a small example if you want to test, how
receiving a JSON object from a webrick server in your browser with the
javasript prototype library http://www.prototypejs.org works.

== Speed Comparisons

I have created some benchmark results (see the benchmarks/data-p4-3Ghz
subdir of the package) for the JSON-parser to estimate the speed up in the C
extension:

 Comparing times (call_time_mean):
  1 ParserBenchmarkExt#parser   900 repeats:
        553.922304770 (  real) ->   21.500x 
          0.001805307
  2 ParserBenchmarkYAML#parser  1000 repeats:
        224.513358139 (  real) ->    8.714x 
          0.004454078
  3 ParserBenchmarkPure#parser  1000 repeats:
         26.755020642 (  real) ->    1.038x 
          0.037376163
  4 ParserBenchmarkRails#parser 1000 repeats:
         25.763381731 (  real) ->    1.000x 
          0.038814780
            calls/sec (  time) ->    speed  covers
            secs/call

In the table above 1 is JSON::Ext::Parser, 2 is YAML.load with YAML
compatbile JSON document, 3 is is JSON::Pure::Parser, and 4 is
ActiveSupport::JSON.decode. The ActiveSupport JSON-decoder converts the
input first to YAML and then uses the YAML-parser, the conversion seems to
slow it down so much that it is only as fast as the JSON::Pure::Parser!

If you look at the benchmark data you can see that this is mostly caused by
the frequent high outliers - the median of the Rails-parser runs is still
overall smaller than the median of the JSON::Pure::Parser runs:

 Comparing times (call_time_median):
  1 ParserBenchmarkExt#parser   900 repeats:
        800.592479481 (  real) ->   26.936x 
          0.001249075
  2 ParserBenchmarkYAML#parser  1000 repeats:
        271.002390644 (  real) ->    9.118x 
          0.003690004
  3 ParserBenchmarkRails#parser 1000 repeats:
         30.227910865 (  real) ->    1.017x 
          0.033082008
  4 ParserBenchmarkPure#parser  1000 repeats:
         29.722384421 (  real) ->    1.000x 
          0.033644676
            calls/sec (  time) ->    speed  covers
            secs/call

I have benchmarked the JSON-Generator as well. This generated a few more
values, because there are different modes that also influence the achieved
speed:

 Comparing times (call_time_mean):
  1 GeneratorBenchmarkExt#generator_fast    1000 repeats:
        547.354332608 (  real) ->   15.090x 
          0.001826970
  2 GeneratorBenchmarkExt#generator_safe    1000 repeats:
        443.968212317 (  real) ->   12.240x 
          0.002252414
  3 GeneratorBenchmarkExt#generator_pretty  900 repeats:
        375.104545883 (  real) ->   10.341x 
          0.002665923
  4 GeneratorBenchmarkPure#generator_fast   1000 repeats:
         49.978706968 (  real) ->    1.378x 
          0.020008521
  5 GeneratorBenchmarkRails#generator       1000 repeats:
         38.531868759 (  real) ->    1.062x 
          0.025952543
  6 GeneratorBenchmarkPure#generator_safe   1000 repeats:
         36.927649925 (  real) ->    1.018x 7 (>=3859)
          0.027079979
  7 GeneratorBenchmarkPure#generator_pretty 1000 repeats:
         36.272134441 (  real) ->    1.000x 6 (>=3859)
          0.027569373
            calls/sec (  time) ->    speed  covers
            secs/call

In the table above 1-3 are JSON::Ext::Generator methods. 4, 6, and 7 are
JSON::Pure::Generator methods and 5 is the Rails JSON generator. It is now a
bit faster than the generator_safe and generator_pretty methods of the pure
variant but slower than the others.

To achieve the fastest JSON document output, you can use the fast_generate
method. Beware, that this will disable the checking for circular Ruby data
structures, which may cause JSON to go into an infinite loop.

Here are the median comparisons for completeness' sake:

 Comparing times (call_time_median):
  1 GeneratorBenchmarkExt#generator_fast    1000 repeats:
        708.258020939 (  real) ->   16.547x 
          0.001411915
  2 GeneratorBenchmarkExt#generator_safe    1000 repeats:
        569.105020353 (  real) ->   13.296x 
          0.001757145
  3 GeneratorBenchmarkExt#generator_pretty  900 repeats:
        482.825371244 (  real) ->   11.280x 
          0.002071142
  4 GeneratorBenchmarkPure#generator_fast   1000 repeats:
         62.717626652 (  real) ->    1.465x 
          0.015944481
  5 GeneratorBenchmarkRails#generator       1000 repeats:
         43.965681162 (  real) ->    1.027x 
          0.022745013
  6 GeneratorBenchmarkPure#generator_safe   1000 repeats:
         43.929073409 (  real) ->    1.026x 7 (>=3859)
          0.022763968
  7 GeneratorBenchmarkPure#generator_pretty 1000 repeats:
         42.802514491 (  real) ->    1.000x 6 (>=3859)
          0.023363113
            calls/sec (  time) ->    speed  covers
            secs/call

== Author

Florian Frank <mailto:flori@ping.de>

== License

Ruby License, see the COPYING file included in the source distribution. The
Ruby License includes the GNU General Public License (GPL), Version 2, so see
the file GPL as well.

== Download

The latest version of this library can be downloaded at

* http://rubyforge.org/frs?group_id=953

Online Documentation should be located at

* http://json.rubyforge.org
JSON-JRuby
==========

JSON-JRuby is a port of Florian Frank's native
[`json` library](http://json.rubyforge.org/) to JRuby.
It aims to be a perfect drop-in replacement for `json_pure`.


Development version
===================

The latest version is available from the
[Git repository](http://github.com/mernen/json-jruby/tree):

    git clone git://github.com/mernen/json-jruby.git


Compiling
=========

You'll need JRuby version 1.2 or greater to build JSON-JRuby.
Its path must be set on the `jruby.dir` property of
`nbproject/project.properties` (defaults to `../jruby`).

Additionally, you'll need [Ant](http://ant.apache.org/), and
[Ragel](http://www.cs.queensu.ca/~thurston/ragel/) 6.4 or greater.

Then, from the folder where the sources are located, type:

    ant clean jar

to clean any leftovers from previous builds and generate the `.jar` files.
To generate a RubyGem, specify the `gem` action rather than `jar`.
# Mongoid
[![Build Status](https://travis-ci.org/mongoid/mongoid.svg?branch=master)](https://travis-ci.org/mongoid/mongoid) 
[![Code Climate](https://codeclimate.com/github/mongoid/mongoid.svg)](https://codeclimate.com/github/mongoid/mongoid)
[![Coverage Status](https://img.shields.io/coveralls/mongoid/mongoid/master.svg)](https://coveralls.io/r/mongoid/mongoid?branch=master)
[![Dependency Status](https://www.versioneye.com/ruby/mongoid/4.0.0/badge.svg)](https://www.versioneye.com/ruby/mongoid/4.0.0)


Mongoid is an ODM (Object-Document-Mapper) framework for MongoDB in Ruby.

Project Tracking
----------------

* [Mongoid Website and Documentation](http://mongoid.org)
* [Mongoid Google Group](http://groups.google.com/group/mongoid)
* [Stackoverflow](http://stackoverflow.com/questions/tagged/mongoid)
* [#mongoid](http://webchat.freenode.net/?channels=mongoid) on freenode IRC

Compatibility
-------------

Mongoid is tested against MRI 1.9.3, 2.0.0, 2.1.0 and JRuby (1.9).

Documentation
-------------

Please see the new Mongoid website for up-to-date documentation:
[mongoid.org](http://mongoid.org)

Donating
--------

[Support Mongoid at Pledgie](http://www.pledgie.com/campaigns/7757)

<a href='http://www.pledgie.com/campaigns/7757'>
<img alt='Click here to lend your support to: Mongoid and make a donation at www.pledgie.com !' src='http://www.pledgie.com/campaigns/7757.png?skin_name=chrome' border='0'/>
</a>

[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=durran&url=http://github.com/mongoid&title=mongoid&language=&tags=github&category=software)

License
-------

Copyright (c) 2009-2013 Durran Jordan

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Credits
-------

Durran Jordan: durran at gmail dot com
domain_name
===========

Synopsis
--------

Domain Name manipulation library for Ruby

Description
-----------

* Parses a domain name ready for extracting the registered domain and
  TLD.

        require "domain_name"

        host = DomainName("a.b.example.co.uk")
        host.domain         #=> "example.co.uk"
        host.tld            #=> "uk"
        host.cookie_domain?("example.co.uk")    #=> true
        host.cookie_domain?("co.uk")            #=> false

        host = DomainName("[::1]")  # IP addresses like "192.168.1.1" and "::1" are also acceptable
        host.ipaddr?        #=> true
        host.cookie_domain?("0:0:0:0:0:0:0:1")  #=> true

* Implements rudimental IDNA support.

To-do's
-------

* Implement IDNA 2008 (and/or 2003) including the domain label
  validation and mapping defined in RFC 5891-5895 and UTS #46.
  (work in progress)

* Define a compact YAML serialization format.

Installation
------------

	gem install domain_name

References
----------

* [RFC 3492](http://tools.ietf.org/html/rfc3492) (Obsolete; just for test cases)

* [RFC 5890](http://tools.ietf.org/html/rfc5890)

* [RFC 5891](http://tools.ietf.org/html/rfc5891)

* [RFC 5892](http://tools.ietf.org/html/rfc5892)

* [RFC 5893](http://tools.ietf.org/html/rfc5892)

* [Public Suffix List](http://publicsuffix.org/list/)

* [Effective TLD Names List](http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1)

License
-------

Copyright (c) 2011, 2012, 2013 Akinori MUSHA

Licensed under the 2-clause BSD license.

Some portion of this library is copyrighted by third parties and
licensed under MPL 1.1/GPL 2.0/LGPL 2.1 or 3-clause BSD license,
See `LICENSE.txt` for details.
# RSpec Mocks [![Build Status](https://secure.travis-ci.org/rspec/rspec-mocks.svg?branch=master)](http://travis-ci.org/rspec/rspec-mocks) [![Code Climate](https://codeclimate.com/github/rspec/rspec-mocks.svg)](https://codeclimate.com/github/rspec/rspec-mocks)
rspec-mocks is a test-double framework for rspec with support for method stubs,
fakes, and message expectations on generated test-doubles and real objects
alike.

## Install

    gem install rspec       # for rspec-core, rspec-expectations, rspec-mocks
    gem install rspec-mocks # for rspec-mocks only

Want to run against the `master` branch? You'll need to include the dependent
RSpec repos as well. Add the following to your `Gemfile`:

```ruby
%w[rspec-core rspec-expectations rspec-mocks rspec-support].each do |lib|
  gem lib, :git => "git://github.com/rspec/#{lib}.git", :branch => 'master'
end
```

## Test Doubles

A test double is an object that stands in for another object in your system
during a code example. Use the `double` method, passing in an optional identifier, to create one:

```ruby
book = double("book")
```

Most of the time you will want some confidence that your doubles resemble an
existing object in your system. Verifying doubles are provided for this
purpose. If the existing object is available, they will prevent you from adding
stubs and expectations for methods that do not exist or that have an invalid
number of parameters.

```ruby
book = instance_double("Book", :pages => 250)
```

Verifying doubles have some clever tricks to enable you to both test in
isolation without your dependencies loaded while still being able to validate
them against real objects. More detail is available in [their
documentation](https://github.com/rspec/rspec-mocks/blob/master/features/verifying_doubles).

Verifying doubles can also accept custom identifiers, just like double(), e.g.:

```ruby
books = []
books << instance_double("Book", :rspec_book, :pages => 250)
books << instance_double("Book", "(Untitled)", :pages => 5000)

puts books.inspect # with names, it's clearer which were actually added
```

## Method Stubs

A method stub is an implementation that returns a pre-determined value.  Method
stubs can be declared on test doubles or real objects using the same syntax.
rspec-mocks supports 3 forms for declaring method stubs:

```ruby
allow(book).to receive(:title) { "The RSpec Book" }
allow(book).to receive(:title).and_return("The RSpec Book")
allow(book).to receive_messages(
    :title => "The RSpec Book",
    :subtitle => "Behaviour-Driven Development with RSpec, Cucumber, and Friends")
```

You can also use this shortcut, which creates a test double and declares a
method stub in one statement:

```ruby
book = double("book", :title => "The RSpec Book")
```

The first argument is a name, which is used for documentation and appears in
failure messages. If you don't care about the name, you can leave it out,
making the combined instantiation/stub declaration very terse:

```ruby
double(:foo => 'bar')
```

This is particularly nice when providing a list of test doubles to a method
that iterates through them:

```ruby
order.calculate_total_price(double(:price => 1.99), double(:price => 2.99))
```

## Consecutive return values

When a stub might be invoked more than once, you can provide additional
arguments to `and_return`.  The invocations cycle through the list. The last
value is returned for any subsequent invocations:

```ruby
allow(die).to receive(:roll).and_return(1, 2, 3)
die.roll # => 1
die.roll # => 2
die.roll # => 3
die.roll # => 3
die.roll # => 3
```

To return an array in a single invocation, declare an array:

```ruby
allow(team).to receive(:players).and_return([double(:name => "David")])
```

## Message Expectations

A message expectation is an expectation that the test double will receive a
message some time before the example ends. If the message is received, the
expectation is satisfied. If not, the example fails.

```ruby
validator = double("validator")
expect(validator).to receive(:validate) { "02134" }
zipcode = Zipcode.new("02134", validator)
zipcode.valid?
```

## Test Spies

Verifies the given object received the expected message during the course of
the test. For a message to be verified, the given object must be setup to spy
on it, either by having it explicitly stubbed or by being a null object double
(e.g. `double(...).as_null_object`). Convenience methods are provided to easily
create null object doubles for this purpose:

```ruby
spy("invitation") # => same as `double("invitation").as_null_object`
instance_spy("Invitation") # => same as `instance_double("Invitation").as_null_object`
class_spy("Invitation") # => same as `class_double("Invitation").as_null_object`
object_spy("Invitation") # => same as `object_double("Invitation").as_null_object`
```

Verifying messages received in this way implements the Test Spy pattern.

```ruby
invitation = spy('invitation')

user.accept_invitation(invitation)

expect(invitation).to have_received(:accept)

# You can also use other common message expectations. For example:
expect(invitation).to have_received(:accept).with(mailer)
expect(invitation).to have_received(:accept).twice
expect(invitation).to_not have_received(:accept).with(mailer)

# One can specify a return value on the spy the same way one would a double.
invitation = spy('invitation', :accept => true)
expect(invitation).to have_received(:accept).with(mailer)
expect(invitation.accept).to eq(true)
```

Note that `have_received(...).with(...)` is unable to work properly when
passed arguments are mutated after the spy records the received message.
For example, this does not work properly:

```ruby
greeter = spy("greeter")

message = "Hello"
greeter.greet_with(message)
message << ", World"

expect(greeter).to have_received(:greet_with).with("Hello")
```

## Nomenclature

### Mock Objects and Test Stubs

The names Mock Object and Test Stub suggest specialized Test Doubles.  i.e.
a Test Stub is a Test Double that only supports method stubs, and a Mock
Object is a Test Double that supports message expectations and method
stubs.

There is a lot of overlapping nomenclature here, and there are many
variations of these patterns (fakes, spies, etc). Keep in mind that most of
the time we're talking about method-level concepts that are variations of
method stubs and message expectations, and we're applying to them to _one_
generic kind of object: a Test Double.

### Test-Specific Extension

a.k.a. Partial Double, a Test-Specific Extension is an extension of a
real object in a system that is instrumented with test-double like
behaviour in the context of a test. This technique is very common in Ruby
because we often see class objects acting as global namespaces for methods.
For example, in Rails:

```ruby
person = double("person")
allow(Person).to receive(:find) { person }
```

In this case we're instrumenting Person to return the person object we've
defined whenever it receives the `find` message. We can also set a message
expectation so that the example fails if `find` is not called:

```ruby
person = double("person")
expect(Person).to receive(:find) { person }
```

RSpec replaces the method we're stubbing or mocking with its own
test-double-like method. At the end of the example, RSpec verifies any message
expectations, and then restores the original methods.

## Expecting Arguments

```ruby
expect(double).to receive(:msg).with(*args)
expect(double).to_not receive(:msg).with(*args)
```

You can set multiple expectations for the same message if you need to:

```ruby
expect(double).to receive(:msg).with("A", 1, 3)
expect(double).to receive(:msg).with("B", 2, 4)
```

## Argument Matchers

Arguments that are passed to `with` are compared with actual arguments
received using ==. In cases in which you want to specify things about the
arguments rather than the arguments themselves, you can use any of the
matchers that ship with rspec-expectations. They don't all make syntactic
sense (they were primarily designed for use with RSpec::Expectations), but
you are free to create your own custom RSpec::Matchers.

rspec-mocks also adds some keyword Symbols that you can use to
specify certain kinds of arguments:

```ruby
expect(double).to receive(:msg).with(no_args)
expect(double).to receive(:msg).with(any_args)
expect(double).to receive(:msg).with(1, any_args) # any args acts like an arg splat and can go anywhere
expect(double).to receive(:msg).with(1, kind_of(Numeric), "b") #2nd argument can be any kind of Numeric
expect(double).to receive(:msg).with(1, boolean(), "b") #2nd argument can be true or false
expect(double).to receive(:msg).with(1, /abc/, "b") #2nd argument can be any String matching the submitted Regexp
expect(double).to receive(:msg).with(1, anything(), "b") #2nd argument can be anything at all
expect(double).to receive(:msg).with(1, duck_type(:abs, :div), "b") #2nd argument can be object that responds to #abs and #div
expect(double).to receive(:msg).with(hash_including(:a => 5)) # first arg is a hash with a: 5 as one of the key-values
expect(double).to receive(:msg).with(array_including(5)) # first arg is an array with 5 as one of the key-values
expect(double).to receive(:msg).with(hash_excluding(:a => 5)) # first arg is a hash without a: 5 as one of the key-values
```

## Receive Counts

```ruby
expect(double).to receive(:msg).once
expect(double).to receive(:msg).twice
expect(double).to receive(:msg).exactly(n).times
expect(double).to receive(:msg).at_least(:once)
expect(double).to receive(:msg).at_least(:twice)
expect(double).to receive(:msg).at_least(n).times
expect(double).to receive(:msg).at_most(:once)
expect(double).to receive(:msg).at_most(:twice)
expect(double).to receive(:msg).at_most(n).times
```

## Ordering

```ruby
expect(double).to receive(:msg).ordered
expect(double).to receive(:other_msg).ordered
  # This will fail if the messages are received out of order
```

This can include the same message with different arguments:

```ruby
expect(double).to receive(:msg).with("A", 1, 3).ordered
expect(double).to receive(:msg).with("B", 2, 4).ordered
```

## Setting Responses

Whether you are setting a message expectation or a method stub, you can
tell the object precisely how to respond. The most generic way is to pass
a block to `receive`:

```ruby
expect(double).to receive(:msg) { value }
```

When the double receives the `msg` message, it evaluates the block and returns
the result.

```ruby
expect(double).to receive(:msg).and_return(value)
expect(double).to receive(:msg).exactly(3).times.and_return(value1, value2, value3)
  # returns value1 the first time, value2 the second, etc
expect(double).to receive(:msg).and_raise(error)
  # error can be an instantiated object or a class
  # if it is a class, it must be instantiable with no args
expect(double).to receive(:msg).and_throw(:msg)
expect(double).to receive(:msg).and_yield(values, to, yield)
expect(double).to receive(:msg).and_yield(values, to, yield).and_yield(some, other, values, this, time)
  # for methods that yield to a block multiple times
```

Any of these responses can be applied to a stub as well

```ruby
allow(double).to receive(:msg).and_return(value)
allow(double).to receive(:msg).and_return(value1, value2, value3)
allow(double).to receive(:msg).and_raise(error)
allow(double).to receive(:msg).and_throw(:msg)
allow(double).to receive(:msg).and_yield(values, to, yield)
allow(double).to receive(:msg).and_yield(values, to, yield).and_yield(some, other, values, this, time)
```

## Arbitrary Handling

Once in a while you'll find that the available expectations don't solve the
particular problem you are trying to solve. Imagine that you expect the message
to come with an Array argument that has a specific length, but you don't care
what is in it. You could do this:

```ruby
expect(double).to receive(:msg) do |arg|
  expect(arg.size).to eq 7
end
```

If the method being stubbed itself takes a block, and you need to yield to it
in some special way, you can use this:

```ruby
expect(double).to receive(:msg) do |&arg|
  begin
    arg.call
  ensure
    # cleanup
  end
end
```

## Delegating to the Original Implementation

When working with a partial mock object, you may occasionally
want to set a message expecation without interfering with how
the object responds to the message. You can use `and_call_original`
to achieve this:

```ruby
expect(Person).to receive(:find).and_call_original
Person.find # => executes the original find method and returns the result
```

## Combining Expectation Details

Combining the message name with specific arguments, receive counts and responses
you can get quite a bit of detail in your expectations:

```ruby
expect(double).to receive(:<<).with("illegal value").once.and_raise(ArgumentError)
```

While this is a good thing when you really need it, you probably don't really
need it! Take care to specify only the things that matter to the behavior of
your code.

## Stubbing and Hiding Constants

See the [mutating constants
README](https://github.com/rspec/rspec-mocks/blob/master/features/mutating_constants/README.md)
for info on this feature.

## Use `before(:example)`, not `before(:context)`

Stubs in `before(:context)` are not supported. The reason is that all stubs and mocks get cleared out after each example, so any stub that is set in `before(:context)` would work in the first example that happens to run in that group, but not for any others.

Instead of `before(:context)`, use `before(:example)`.

## Settings mocks or stubs on any instance of a class

rspec-mocks provides two methods, `allow_any_instance_of` and
`expect_any_instance_of`, that will allow you to stub or mock any instance
of a class. They are used in place of `allow` or `expect`:

```ruby
allow_any_instance_of(Widget).to receive(:name).and_return("Wibble")
expect_any_instance_of(Widget).to receive(:name).and_return("Wobble")
```

These methods add the appropriate stub or expectation to all instances of
`Widget`.

This feature is sometimes useful when working with legacy code, though in
general we discourage its use for a number of reasons:

* The `rspec-mocks` API is designed for individual object instances, but this
  feature operates on entire classes of objects. As a result there are some
  semantically confusing edge cases. For example in
  `expect_any_instance_of(Widget).to receive(:name).twice` it isn't clear
  whether each specific instance is expected to receive `name` twice, or if two
  receives total are expected. (It's the former.)
* Using this feature is often a design smell. It may be
  that your test is trying to do too much or that the object under test is too
  complex.
* It is the most complicated feature of `rspec-mocks`, and has historically
  received the most bug reports. (None of the core team actively use it,
  which doesn't help.)


## Further Reading

There are many different viewpoints about the meaning of mocks and stubs. If
you are interested in learning more, here is some recommended reading:

* Mock Objects: http://www.mockobjects.com/
* Endo-Testing: http://www.ccs.neu.edu/research/demeter/related-work/extreme-programming/MockObjectsFinal.PDF
* Mock Roles, Not Objects: http://www.jmock.org/oopsla2004.pdf
* Test Double: http://www.martinfowler.com/bliki/TestDouble.html
* Test Double Patterns: http://xunitpatterns.com/Test%20Double%20Patterns.html
* Mocks aren't stubs: http://www.martinfowler.com/articles/mocksArentStubs.html

## Also see

* [http://github.com/rspec/rspec](http://github.com/rspec/rspec)
* [http://github.com/rspec/rspec-core](http://github.com/rspec/rspec-core)
* [http://github.com/rspec/rspec-expectations](http://github.com/rspec/rspec-expectations)
= Kaminari {<img src="https://travis-ci.org/amatsuda/kaminari.svg"/>}[http://travis-ci.org/amatsuda/kaminari] {<img src="https://img.shields.io/codeclimate/github/amatsuda/kaminari.svg" />}[https://codeclimate.com/github/amatsuda/kaminari] {<img src="http://inch-ci.org/github/amatsuda/kaminari.svg" alt="Inline docs" />}[http://inch-ci.org/github/amatsuda/kaminari]

A Scope & Engine based, clean, powerful, customizable and sophisticated paginator for modern web app frameworks and ORMs


== Features

=== Clean
Does not globally pollute +Array+, +Hash+, +Object+ or <tt>AR::Base</tt>.

=== Easy to use
Just bundle the gem, then your models are ready to be paginated. No configuration required. Don't have to define anything in your models or helpers.

=== Simple scope-based API
Everything is method chainable with less "Hasheritis". You know, that's the Rails 3 way.
No special collection class or anything for the paginated values, instead using a general <tt>AR::Relation</tt> instance. So, of course you can chain any other conditions before or after the paginator scope.

=== Customizable engine-based I18n-aware helper
As the whole pagination helper is basically just a collection of links and non-links, Kaminari renders each of them through its own partial template inside the Engine. So, you can easily modify their behaviour, style or whatever by overriding partial templates.

=== ORM & template engine agnostic
Kaminari supports multiple ORMs (ActiveRecord, DataMapper, Mongoid, MongoMapper) multiple web frameworks (Rails, Sinatra, Grape), and multiple template engines (ERB, Haml, Slim).

=== Modern
The pagination helper outputs the HTML5 <nav> tag by default. Plus, the helper supports Rails 3 unobtrusive Ajax.


== Supported versions

* Ruby 1.8.7, 1.9.2, 1.9.3, 2.0.0, 2.1.x, 2.2.x

* Rails 3.0, 3.1, 3.2, 4.0, 4.1, 4.2

* Haml 3+

* Mongoid 2+

* MongoMapper 0.9+

* DataMapper 1.1.0+

== Install

Put this line in your Gemfile:
  gem 'kaminari'

Then bundle:
  % bundle


== Usage

=== Query Basics

* the +page+ scope

  To fetch the 7th page of users (default +per_page+ is 25)
    User.page(7)

* the +per+ scope

  To show a lot more users per each page (change the +per_page+ value)
    User.page(7).per(50)
  Note that the +per+ scope is not directly defined on the models but is just a method defined on the page scope. This is absolutely reasonable because you will never actually use +per_page+ without specifying the +page+ number.

  Keep in mind that +per+ utilizes internally +limit+ and so it will override any +limit+ that was set previously
    User.count                  # => 1000
    a = User.limit(5).count     # => 5
    b = a.page(1).per(20).size  # => 20

* the +padding+ scope

  Occasionally you need to pad a number of records that is not a multiple of the page size.
    User.page(7).per(50).padding(3)
  Note that the +padding+ scope also is not directly defined on the models.

=== General configuration options

You can configure the following default values by overriding these values using <tt>Kaminari.configure</tt> method.
  default_per_page  # 25 by default
  max_per_page      # nil by default
  max_pages         # nil by default
  window            # 4 by default
  outer_window      # 0 by default
  left              # 0 by default
  right             # 0 by default
  page_method_name  # :page by default
  param_name        # :page by default

There's a handy generator that generates the default configuration file into config/initializers directory.
Run the following generator command, then edit the generated file.
  % rails g kaminari:config

* changing +page_method_name+

  You can change the method name +page+ to +bonzo+ or +plant+ or whatever you like, in order to play nice with existing +page+ method or association or scope or any other plugin that defines +page+ method on your models.


=== Configuring default +per_page+ value for each model

* +paginates_per+

  You can specify default +per_page+ value per each model using the following declarative DSL.
    class User < ActiveRecord::Base
      paginates_per 50
    end

=== Configuring max +per_page+ value for each model

* +max_paginates_per+

  You can specify max +per_page+ value per each model using the following declarative DSL.
  If the variable that specified via +per+ scope is more than this variable, +max_paginates_per+ is used instead of it. Default value is nil, which means you are not imposing any max +per_page+ value.
    class User < ActiveRecord::Base
      max_paginates_per 100
    end

=== Controllers

* the page parameter is in <tt>params[:page]</tt>

  Typically, your controller code will look like this:
    @users = User.order(:name).page params[:page]

=== Views

* the same old helper method

  Just call the +paginate+ helper:
    <%= paginate @users %>

  This will render several <tt>?page=N</tt> pagination links surrounded by an HTML5 <+nav+> tag.

=== Helpers

* the +paginate+ helper method

    <%= paginate @users %>
  This would output several pagination links such as <tt>« First ‹ Prev ... 2 3 4 5 6 7 8 9 10 ... Next › Last »</tt>

* specifying the "inner window" size (4 by default)

    <%= paginate @users, :window => 2 %>
  This would output something like <tt>... 5 6 7 8 9 ...</tt> when 7 is the current page.

* specifying the "outer window" size (0 by default)

    <%= paginate @users, :outer_window => 3 %>
  This would output something like <tt>1 2 3 4 ...(snip)... 17 18 19 20</tt> while having 20 pages in total.

* outer window can be separately specified by +left+, +right+ (0 by default)

    <%= paginate @users, :left => 1, :right => 3 %>
  This would output something like <tt>1 ...(snip)... 18 19 20</tt> while having 20 pages in total.

* changing the parameter name (:+param_name+) for the links

    <%= paginate @users, :param_name => :pagina %>
  This would modify the query parameter name on each links.

* extra parameters (:+params+) for the links

    <%= paginate @users, :params => {:controller => 'foo', :action => 'bar'} %>
  This would modify each link's +url_option+. :+controller+ and :+action+ might be the keys in common.

* Ajax links (crazy simple, but works perfectly!)

    <%= paginate @users, :remote => true %>
  This would add <tt>data-remote="true"</tt> to all the links inside.

* specifying an alternative views directory (default is <tt>kaminari/</tt>)

    <%= paginate @users, :views_prefix => 'templates/' %>
  This would search for partials in <tt>app/views/templates/kaminari</tt>. This option makes it easier to do things like A/B testing pagination templates/themes, using new/old templates at the same time as well as better intergration with other gems sush as {cells}[https://github.com/apotonick/cells].

* the +link_to_next_page+ and +link_to_previous_page+ helper method

    <%= link_to_next_page @items, 'Next Page' %>
  This simply renders a link to the next page. This would be helpful for creating a Twitter-like pagination feature.

* the +page_entries_info+ helper method

    <%= page_entries_info @users %>
  This renders a helpful message with numbers of displayed vs. total entries.

=== I18n and labels

The default labels for 'first', 'last', 'previous', '...' and 'next' are stored in the I18n yaml inside the engine, and rendered through I18n API. You can switch the label value per I18n.locale for your internationalized application.
Keys and the default values are the following. You can override them by adding to a YAML file in your <tt>Rails.root/config/locales</tt> directory.

  en:
    views:
      pagination:
        first: "&laquo; First"
        last: "Last &raquo;"
        previous: "&lsaquo; Prev"
        next: "Next &rsaquo;"
        truncate: "&hellip;"
    helpers:
      page_entries_info:
        one_page:
          display_entries:
            zero: "No %{entry_name} found"
            one: "Displaying <b>1</b> %{entry_name}"
            other: "Displaying <b>all %{count}</b> %{entry_name}"
        more_pages:
          display_entries: "Displaying %{entry_name} <b>%{first}&nbsp;-&nbsp;%{last}</b> of <b>%{total}</b> in total"

=== Customizing the pagination helper

Kaminari includes a handy template generator.

* to edit your paginator

  Run the generator first,
    % rails g kaminari:views default

  then edit the partials in your app's <tt>app/views/kaminari/</tt> directory.

* for Haml users

  Haml templates generator is also available by adding the <tt>-e haml</tt> option (this is automatically invoked when the default template_engine is set to Haml).

    % rails g kaminari:views default -e haml

* themes

  The generator has the ability to fetch several sample template themes from
  the external repository (https://github.com/amatsuda/kaminari_themes) in
  addition to the bundled "default" one, which will help you creating a nice
  looking paginator.
    % rails g kaminari:views THEME

  To see the full list of avaliable themes, take a look at the themes repository,
  or just hit the generator without specifying +THEME+ argument.
    % rails g kaminari:views

* multiple themes

  To utilize multiple themes from within a single application, create a directory within the app/views/kaminari/ and move your custom template files into that directory.
    % rails g kaminari:views default (skip if you have existing kaminari views)
    % cd app/views/kaminari
    % mkdir my_custom_theme
    % cp _*.html.* my_custom_theme/

  Next, reference that directory when calling the +paginate+ method:

    <%= paginate @users, :theme => 'my_custom_theme' %>

  Customize away!

  Note: if the theme isn't present or none is specified, kaminari will default back to the views included within the gem.

=== Paginating a generic Array object

Kaminari provides an Array wrapper class that adapts a generic Array object to the <tt>paginate</tt> view helper.
However, the <tt>paginate</tt> helper doesn't automatically handle your Array object (this is intentional and by design).
<tt>Kaminari::paginate_array</tt> method converts your Array object into a paginatable Array that accepts <tt>page</tt> method.

  @paginatable_array = Kaminari.paginate_array(my_array_object).page(params[:page]).per(10)

You can specify the +total_count+ value through options Hash. This would be helpful when handling an Array-ish object that has a different +count+ value from actual +count+ such as RSolr search result or when you need to generate a custom pagination. For example:

  @paginatable_array = Kaminari.paginate_array([], total_count: 145).page(params[:page]).per(10)

== Creating friendly URLs and caching

Because of the +page+ parameter and Rails 3 routing, you can easily generate SEO and user-friendly URLs. For any resource you'd like to paginate, just add the following to your +routes.rb+:

    resources :my_resources do
      get 'page/:page', :action => :index, :on => :collection
    end

This will create URLs like <tt>/my_resources/page/33</tt> instead of <tt>/my_resources?page=33</tt>. This is now a friendly URL, but it also has other added benefits...

Because the +page+ parameter is now a URL segment, we can leverage on Rails page caching[http://guides.rubyonrails.org/caching_with_rails.html#page-caching]!

NOTE: In this example, I've pointed the route to my <tt>:index</tt> action. You may have defined a custom pagination action in your controller - you should point <tt>:action => :your_custom_action</tt> instead.


== Sinatra/Padrino support

Since version 0.13.0, kaminari started to support Sinatra or Sinatra-based frameworks experimentally.

To use kaminari and its helpers with these frameworks,

    require 'kaminari/sinatra'

or edit gemfile:

    gem 'kaminari', :require => 'kaminari/sinatra'

This line just enables model-side features, such as <tt>Model#page</tt> and <tt>Model#per</tt>. If you want to use view helpers, please explicitly <tt>register</tt> helpers in your Sinatra or Padrino app:

    register Kaminari::Helpers::SinatraHelpers

Or, you can implement your own awesome helper :)

More features are coming, and again, this is still experimental. Please let us know if you found anything wrong with the Sinatra support.


== For more information

Check out Kaminari recipes on the GitHub Wiki for more advanced tips and techniques.
https://github.com/amatsuda/kaminari/wiki/Kaminari-recipes


== Questions, Feedback

Feel free to message me on Github (amatsuda) or Twitter (@a_matsuda)  ☇☇☇  :)


== Contributing to Kaminari

Fork, fix, then send a pull request.

To run the test suite locally against all supported frameworks:

  % bundle install
  % rake spec:all

To target the test suite against one framework:

  % rake spec:active_record_40

You can find a list of supported spec tasks by running <tt>rake -T</tt>. You may also find it useful to run a specific test
for a specific framework. To do so, you'll have to first make sure you have bundled everything for that configuration,
then you can run the specific test:

  % BUNDLE_GEMFILE='gemfiles/active_record_40.gemfile' bundle install
  % BUNDLE_GEMFILE='gemfiles/active_record_40.gemfile' bundle exec rspec ./spec/requests/users_spec.rb


== Copyright

Copyright (c) 2011 Akira Matsuda. See MIT-LICENSE for further details.
= Rack, a modular Ruby webserver interface {<img src="https://secure.travis-ci.org/rack/rack.svg" alt="Build Status" />}[http://travis-ci.org/rack/rack] {<img src="https://gemnasium.com/rack/rack.svg" alt="Dependency Status" />}[https://gemnasium.com/rack/rack]

Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.

The exact details of this are described in the Rack specification,
which all Rack applications should conform to.

== Supported web servers

The included *handlers* connect all kinds of web servers to Rack:
* Mongrel
* EventedMongrel
* SwiftipliedMongrel
* WEBrick
* FCGI
* CGI
* SCGI
* LiteSpeed
* Thin

These web servers include Rack handlers in their distributions:
* Ebb
* Fuzed
* Glassfish v3
* Phusion Passenger (which is mod_rack for Apache and for nginx)
* Puma
* Rainbows!
* Reel
* Unicorn
* unixrack
* uWSGI
* yahns
* Zbatery

Any valid Rack app will run the same on all these handlers, without
changing anything.

== Supported web frameworks

These frameworks include Rack adapters in their distributions:
* Camping
* Coset
* Espresso
* Halcyon
* Mack
* Maveric
* Merb
* Racktools::SimpleApplication
* Ramaze
* Ruby on Rails
* Rum
* Sinatra
* Sin
* Vintage
* Waves
* Wee
* ... and many others.

== Available middleware

Between the server and the framework, Rack can be customized to your
applications needs using middleware, for example:
* Rack::URLMap, to route to multiple applications inside the same process.
* Rack::CommonLogger, for creating Apache-style logfiles.
* Rack::ShowException, for catching unhandled exceptions and
  presenting them in a nice and helpful way with clickable backtrace.
* Rack::File, for serving static files.
* ...many others!

All these components use the same interface, which is described in
detail in the Rack specification.  These optional components can be
used in any way you wish.

== Convenience

If you want to develop outside of existing frameworks, implement your
own ones, or develop middleware, Rack provides many helpers to create
Rack applications quickly and without doing the same web stuff all
over:
* Rack::Request, which also provides query string parsing and
  multipart handling.
* Rack::Response, for convenient generation of HTTP replies and
  cookie handling.
* Rack::MockRequest and Rack::MockResponse for efficient and quick
  testing of Rack application without real HTTP round-trips.

== rack-contrib

The plethora of useful middleware created the need for a project that
collects fresh Rack middleware.  rack-contrib includes a variety of
add-on components for Rack and it is easy to contribute new modules.

* https://github.com/rack/rack-contrib

== rackup

rackup is a useful tool for running Rack applications, which uses the
Rack::Builder DSL to configure middleware and build up applications
easily.

rackup automatically figures out the environment it is run in, and
runs your application as FastCGI, CGI, or standalone with Mongrel or
WEBrick---all from the same configuration.

== Quick start

Try the lobster!

Either with the embedded WEBrick starter:

    ruby -Ilib lib/rack/lobster.rb

Or with rackup:

    bin/rackup -Ilib example/lobster.ru

By default, the lobster is found at http://localhost:9292.

== Installing with RubyGems

A Gem of Rack is available at rubygems.org.  You can install it with:

    gem install rack

I also provide a local mirror of the gems (and development snapshots)
at my site:

    gem install rack --source http://chneukirchen.org/releases/gems/

== Running the tests

Testing Rack requires the bacon testing framework:

    bundle install --without extra # to be able to run the fast tests

Or:

    bundle install # this assumes that you have installed native extensions!

There are two rake-based test tasks:

    rake test       tests all the fast tests (no Handlers or Adapters)
    rake fulltest   runs all the tests

The fast testsuite has no dependencies outside of the core Ruby
installation and bacon.

To run the test suite completely, you need:

  * fcgi
  * memcache-client
  * mongrel
  * thin

The full set of tests test FCGI access with lighttpd (on port
9203) so you will need lighttpd installed as well as the FCGI
libraries and the fcgi gem:

Download and install lighttpd:

    http://www.lighttpd.net/download

Installing the FCGI libraries:

    curl -O http://www.fastcgi.com/dist/fcgi-2.4.0.tar.gz
    tar xzvf fcgi-2.4.0.tar.gz
    cd fcgi-2.4.0
    ./configure --prefix=/usr/local
    make
    sudo make install
    cd ..

Installing the Ruby fcgi gem:

    gem install fcgi

Furthermore, to test Memcache sessions, you need memcached (will be
run on port 11211) and memcache-client installed.

== Configuration

Several parameters can be modified on Rack::Utils to configure Rack behaviour.

e.g:

    Rack::Utils.key_space_limit = 128

=== key_space_limit

The default number of bytes to allow a single parameter key to take up.
This helps prevent a rogue client from flooding a Request.

Default to 65536 characters (4 kiB in worst case).

=== multipart_part_limit

The maximum number of parts a request can contain.
Accepting too many part can lead to the server running out of file handles.

The default is 128, which means that a single request can't upload more than 128 files at once.

Set to 0 for no limit.

Can also be set via the RACK_MULTIPART_PART_LIMIT environment variable.

== History

See <https://github.com/rack/HISTORY.md>.

== Contact

Please post bugs, suggestions and patches to
the bug tracker at <https://github.com/rack/rack/issues>.

Please post security related bugs and suggestions to the core team at
<https://groups.google.com/group/rack-core> or rack-core@googlegroups.com. This
list is not public. Due to wide usage of the library, it is strongly preferred
that we manage timing in order to provide viable patches at the time of
disclosure. Your assistance in this matter is greatly appreciated.

Mailing list archives are available at
<https://groups.google.com/group/rack-devel>.

Git repository (send Git patches to the mailing list):
* https://github.com/rack/rack
* http://git.vuxu.org/cgi-bin/gitweb.cgi?p=rack-github.git

You are also welcome to join the #rack channel on irc.freenode.net.

== Thanks

The Rack Core Team, consisting of

* Christian Neukirchen (chneukirchen)
* James Tucker (raggi)
* Josh Peek (josh)
* José Valim (josevalim)
* Michael Fellinger (manveru)
* Aaron Patterson (tenderlove)
* Santiago Pastorino (spastorino)
* Konstantin Haase (rkh)

and the Rack Alumnis

* Ryan Tomayko (rtomayko)
* Scytrin dai Kinthra (scytrin)

would like to thank:

* Adrian Madrid, for the LiteSpeed handler.
* Christoffer Sawicki, for the first Rails adapter and Rack::Deflater.
* Tim Fletcher, for the HTTP authentication code.
* Luc Heinrich for the Cookie sessions, the static file handler and bugfixes.
* Armin Ronacher, for the logo and racktools.
* Alex Beregszaszi, Alexander Kahn, Anil Wadghule, Aredridel, Ben
  Alpert, Dan Kubb, Daniel Roethlisberger, Matt Todd, Tom Robinson,
  Phil Hagelberg, S. Brent Faulkner, Bosko Milekic, Daniel Rodríguez
  Troitiño, Genki Takiuchi, Geoffrey Grosenbach, Julien Sanchez, Kamal
  Fariz Mahyuddin, Masayoshi Takahashi, Patrick Aljordm, Mig, Kazuhiro
  Nishiyama, Jon Bardin, Konstantin Haase, Larry Siden, Matias
  Korhonen, Sam Ruby, Simon Chiang, Tim Connor, Timur Batyrshin, and
  Zach Brock for bug fixing and other improvements.
* Eric Wong, Hongli Lai, Jeremy Kemper for their continuous support
  and API improvements.
* Yehuda Katz and Carl Lerche for refactoring rackup.
* Brian Candler, for Rack::ContentType.
* Graham Batty, for improved handler loading.
* Stephen Bannasch, for bug reports and documentation.
* Gary Wright, for proposing a better Rack::Response interface.
* Jonathan Buch, for improvements regarding Rack::Response.
* Armin Röhrl, for tracking down bugs in the Cookie generator.
* Alexander Kellett for testing the Gem and reviewing the announcement.
* Marcus Rückert, for help with configuring and debugging lighttpd.
* The WSGI team for the well-done and documented work they've done and
  Rack builds up on.
* All bug reporters and patch contributors not mentioned above.

== Copyright

Copyright (C) 2007, 2008, 2009, 2010 Christian Neukirchen <http://purl.org/net/chneukirchen>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

== Links

Rack:: <http://rack.github.io/>
Official Rack repositories:: <https://github.com/rack>
Rack Bug Tracking:: <https://github.com/rack/rack/issues>
rack-devel mailing list:: <https://groups.google.com/group/rack-devel>
Rack's Rubyforge project:: <http://rubyforge.org/projects/rack>

Christian Neukirchen:: <http://chneukirchen.org/>

# Spring

[![Build Status](https://travis-ci.org/rails/spring.svg?branch=master)](https://travis-ci.org/rails/spring)
[![Gem Version](https://badge.fury.io/rb/spring.svg)](http://badge.fury.io/rb/spring)

Spring is a Rails application preloader. It speeds up development by
keeping your application running in the background so you don't need to
boot it every time you run a test, rake task or migration.

## Features

* Totally automatic; no need to explicitly start and stop the background process
* Reloads your application code on each run
* Restarts your application when configs / initializers / gem
  dependencies are changed

## Compatibility

* Ruby versions: MRI 1.9.3, MRI 2.0, MRI 2.1
* Rails versions: 4.0+ (in Rails 4.1 and up Spring is included by default)

Spring makes extensive use of `Process.fork`, so won't be able to
provide a speed up on platforms which don't support forking (Windows, JRuby).

## Walkthrough

### Setup

Add spring to your Gemfile:

``` ruby
gem "spring", group: :development
```

(Note: using `gem "spring", git: "..."` *won't* work and is not a
supported way of using spring.)

It's recommended to 'springify' the executables in your `bin/`
directory:

```
$ bundle install
$ bundle exec spring binstub --all
```

This generates a `bin/spring` executable, and inserts a small snippet of
code into relevant existing executables. The snippet looks like this:

``` ruby
begin
  load File.expand_path("../spring", __FILE__)
rescue LoadError
end
```

On platforms where spring is installed and supported, this snippet
hooks spring into the execution of commands. In other cases, the snippet
will just be silently ignored and the lines after it will be executed as
normal.

If you don't want to prefix every command you type with `bin/`, you
can [use direnv](https://github.com/zimbatm/direnv#the-stdlib) to
automatically add `./bin` to your `PATH` when you `cd` into your application.
Simply create an `.envrc` file with the command `PATH_add bin` in your
Rails directory.

### Usage

For this walkthrough I've generated a new Rails application, and run
`rails generate scaffold post name:string`.

Let's run a test:

```
$ time bin/rake test test/controllers/posts_controller_test.rb
Run options:

# Running tests:

.......

Finished tests in 0.127245s, 55.0121 tests/s, 78.5887 assertions/s.

7 tests, 10 assertions, 0 failures, 0 errors, 0 skips

real    0m2.165s
user    0m0.281s
sys     0m0.066s
```

That wasn't particularly fast because it was the first run, so spring
had to boot the application. It's now running:

```
$ bin/spring status
Spring is running:

26150 spring server | spring-demo-app | started 3 secs ago
26155 spring app    | spring-demo-app | started 3 secs ago | test mode
```

The next run is faster:

```
$ time bin/rake test test/controllers/posts_controller_test.rb
Run options:

# Running tests:

.......

Finished tests in 0.176896s, 39.5714 tests/s, 56.5305 assertions/s.

7 tests, 10 assertions, 0 failures, 0 errors, 0 skips

real    0m0.610s
user    0m0.276s
sys     0m0.059s
```

If we edit any of the application files, or test files, the changes will
be picked up on the next run without the background process having to
restart. This works in exactly the same way as the code reloading
which allows you to refresh your browser and instantly see changes during
development.

But if we edit any of the files which were used to start the application
(configs, initializers, your gemfile), the application needs to be fully
restarted. This happens automatically.

Let's "edit" `config/application.rb`:

```
$ touch config/application.rb
$ bin/spring status
Spring is running:

26150 spring server | spring-demo-app | started 36 secs ago
26556 spring app    | spring-demo-app | started 1 sec ago | test mode
```

The application detected that `config/application.rb` changed and
automatically restarted itself.

If we run a command that uses a different environment, then that
environment gets booted up:

```
$ bin/rake routes
    posts GET    /posts(.:format)          posts#index
          POST   /posts(.:format)          posts#create
 new_post GET    /posts/new(.:format)      posts#new
edit_post GET    /posts/:id/edit(.:format) posts#edit
     post GET    /posts/:id(.:format)      posts#show
          PUT    /posts/:id(.:format)      posts#update
          DELETE /posts/:id(.:format)      posts#destroy

$ bin/spring status
Spring is running:

26150 spring server | spring-demo-app | started 1 min ago
26556 spring app    | spring-demo-app | started 42 secs ago | test mode
26707 spring app    | spring-demo-app | started 2 secs ago | development mode
```

There's no need to "shut down" spring. This will happen automatically
when you close your terminal. However if you do want to do a manual shut
down, use the `stop` command:

```
$ bin/spring stop
Spring stopped.
```

### Removal

To remove spring:

* 'Unspring' your bin/ executables: `bin/spring binstub --remove --all`
* Remove spring from your Gemfile

### Deployment

You must not install Spring on your production environment. To prevent it from
being installed, provide the `--without development test` argument to the
`bundle install` command which is used to install gems on your production
machines:

```
$ bundle install --without development test
```

## Commands

### `rake`

Runs a rake task. Rake tasks run in the `development` environment by
default. You can change this on the fly by using the `RAILS_ENV`
environment variable. The environment is also configurable with the
`Spring::Commands::Rake.environment_matchers` hash. This has sensible
defaults, but if you need to match a specific task to a specific
environment, you'd do it like this:

``` ruby
Spring::Commands::Rake.environment_matchers["perf_test"] = "test"
Spring::Commands::Rake.environment_matchers[/^perf/]     = "test"

# To change the environment when you run `rake` with no arguments
Spring::Commands::Rake.environment_matchers[:default] = "development"
```

### `rails console`, `rails generate`, `rails runner`

These execute the rails command you already know and love. If you run
a different sub command (e.g. `rails server`) then spring will automatically
pass it through to the underlying `rails` executable (without the
speed-up).

### Additional commands

You can add these to your Gemfile for additional commands:

* [spring-commands-rspec](https://github.com/jonleighton/spring-commands-rspec)
* [spring-commands-cucumber](https://github.com/jonleighton/spring-commands-cucumber)
* [spring-commands-spinach](https://github.com/jvanbaarsen/spring-commands-spinach)
* [spring-commands-testunit](https://github.com/jonleighton/spring-commands-testunit) - useful for
  running `Test::Unit` tests on Rails 3, since only Rails 4 allows you
  to use `rake test path/to/test` to run a particular test/directory.
* [spring-commands-teaspoon](https://github.com/alejandrobabio/spring-commands-teaspoon.git)

## Use without adding to bundle

If you don't want spring-related code checked into your source
repository, it's possible to use spring without adding to your Gemfile.
However, using spring binstubs without adding spring to the Gemfile is not
supported.

To use spring like this, do a `gem install spring` and then prefix
commands with `spring`. For example, rather than running `bin/rake -T`,
you'd run `spring rake -T`.

## Temporarily disabling Spring

If you're using Spring binstubs, but temporarily don't want commands to
run through Spring, set the `DISABLE_SPRING` environment variable.

## Class reloading

Spring uses Rails' class reloading mechanism
(`ActiveSupport::Dependencies`) to keep your code up to date between
test runs. This is the same mechanism which allows you to see changes
during development when you refresh the page. However, you may never
have used this mechanism with your `test` environment before, and this
can cause problems.

It's important to realise that code reloading means that the constants
in your application are *different objects* after files have changed:

```
$ bin/rails runner 'puts User.object_id'
70127987886040
$ touch app/models/user.rb
$ bin/rails runner 'puts User.object_id'
70127976764620
```

Suppose you have an initializer `config/initializers/save_user_class.rb`
like so:

``` ruby
USER_CLASS = User
```

This saves off the *first* version of the `User` class, which will not
be the same object as `User` after the code has been reloaded:

```
$ bin/rails runner 'puts User == USER_CLASS'
true
$ touch app/models/user.rb
$ bin/rails runner 'puts User == USER_CLASS'
false
```

So to avoid this problem, don't save off references to application
constants in your initialization code.

## Configuration

Spring will read `~/.spring.rb` and `config/spring.rb` for custom
settings. Note that `~/.spring.rb` is loaded *before* bundler, but
`config/spring.rb` is loaded *after* bundler. So if you have any
`spring-commands-*` gems installed that you want to be available in all
projects without having to be added to the project's Gemfile, require
them in your `~/.spring.rb`.

### Application root

Spring must know how to find your Rails application. If you have a
normal app everything works out of the box. If you are working on a
project with a special setup (an engine for example), you must tell
Spring where your app is located:

```ruby
Spring.application_root = './test/dummy'
```

### Running code before forking

There is no `Spring.before_fork` callback. To run something before the
fork, you can place it in `~/.spring.rb` or `config/spring.rb` or in any of the files
which get run when your application initializes, such as
`config/application.rb`, `config/environments/*.rb` or
`config/initializers/*.rb`.

### Running code after forking

You might want to run code after Spring forked off the process but
before the actual command is run. You might want to use an
`after_fork` callback if you have to connect to an external service,
do some general cleanup or set up dynamic configuration.

```ruby
Spring.after_fork do
  # run arbitrary code
end
```

If you want to register multiple callbacks you can simply call
`Spring.after_fork` multiple times with different blocks.

### Watching files and directories

Spring will automatically detect file changes to any file loaded when the server
boots. Changes will cause the affected environments to be restarted.

If there are additional files or directories which should trigger an
application restart, you can specify them with `Spring.watch`:

```ruby
Spring.watch "config/some_config_file.yml"
```

By default Spring polls the filesystem for changes once every 0.2 seconds. This
method requires zero configuration, but if you find that it's using too
much CPU, then you can use event-based file system listening by
installing the
[spring-watcher-listen](https://github.com/jonleighton/spring-watcher-listen)
gem.

## Troubleshooting

If you want to get more information about what spring is doing, you can
specify a log file with the `SPRING_LOG` environment variable:

```
spring stop # if spring is already running
export SPRING_LOG=/tmp/spring.log
spring rake -T
```
# Official Ruby-on-Rails Integration with Sass

This gem provides official integration for Ruby on Rails projects with the Sass stylesheet language.

## Installing

Since Rails 3.1, new Rails projects will be already configured to use Sass. If you are upgrading to Rails 3.1 you will need to add the following to your Gemfile:

    gem 'sass-rails'

## Configuration

To configure Sass via Rails set use `config.sass` in your
application and/or environment files to set configuration
properties that will be passed to Sass.

### Options

- `preferred_syntax` - This option determines the default Sass syntax and file extensions that will be used by Rails generators. Can be `:scss` (default CSS-compatible SCSS syntax) or `:sass` (indented Sass syntax).

The [list of supported Sass options](http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html#options)
can be found on the Sass Website with the following caveats:

- `:style` - This option is not supported. This is determined by the Rails environment. It's `:expanded` only on development, otherwise it's `:compressed`.
- `:never_update` - This option is not supported. Instead set `config.assets.enabled = false`
- `:always_update` - This option is not supported. Sprockets uses a controller to access stylesheets in development mode instead of a full scan for changed files.
- `:always_check` - This option is not supported. Sprockets always checks in development.
- `:syntax` - This is determined by the file's extensions.
- `:filename` - This is determined by the file's name.
- `:line` - This is provided by the template handler.

### Example

    MyProject::Application.configure do
      config.sass.preferred_syntax = :sass
      config.sass.line_comments = false
      config.sass.cache = false
    end

## Important Note

Sprockets provides some directives that are placed inside of comments called `require`, `require_tree`, and
`require_self`. **<span style="color:#c00">DO NOT USE THEM IN YOUR SASS/SCSS FILES.</span>** They are very
primitive and do not work well with Sass files. Instead, use Sass's native `@import` directive which
`sass-rails` has customized to integrate with the conventions of your Rails projects.

## Features

### Glob Imports

When in Rails, there is a special import syntax that allows you to
glob imports relative to the folder of the stylesheet that is doing the importing.

* `@import "mixins/*"` will import all the files in the mixins folder
* `@import "mixins/**/*"` will import all the files in the mixins tree

Any valid ruby glob may be used. The imports are sorted alphabetically.

**NOTE:** It is recommended that you only use this when importing pure library
files (containing mixins and variables) because it is difficult to control the
cascade ordering for imports that contain styles using this approach.

### Asset Helpers
When using the asset pipeline, paths to assets must be rewritten.
When referencing assets use the following asset helpers (underscored in Ruby, hyphenated
in Sass):

#### `asset-path($relative-asset-path)`
Returns a string to the asset.

* `asset-path("rails.png")` becomes `"/assets/rails.png"`

#### `asset-url($relative-asset-path)`
Returns a url reference to the asset.

* `asset-url("rails.png")` becomes `url(/assets/rails.png)`

As a convenience, for each of the following asset classes there are
corresponding `-path` and `-url` helpers:
image, font, video, audio, javascript, stylesheet.

* `image-path("rails.png")` becomes `"/assets/rails.png"`
* `image-url("rails.png")` becomes `url(/assets/rails.png)`

#### `asset-data-url($relative-asset-path)`
Returns a url reference to the Base64-encoded asset at the specified path.

* `asset-data-url("rails.png")` becomes `url(data:image/png;base64,iVBORw0K...)`

## Running Tests

    $ bundle install
    $ bundle exec rake test

If you need to test against local gems, use Bundler's gem :path option in the Gemfile and also edit `test/support/test_helper.rb` and tell the tests where the gem is checked out.

## Code Status

* [![Travis CI](https://api.travis-ci.org/rails/sass-rails.svg)](http://travis-ci.org/rails/sass-rails)
* [![Gem Version](https://badge.fury.io/rb/sass-rails.svg)](http://badge.fury.io/rb/sass-rails)
* [![Dependencies](https://gemnasium.com/rails/sass-rails.svg)](https://gemnasium.com/rails/sass-rails)
bower-rails
===========

[![Gem Version](http://img.shields.io/gem/v/bower-rails.svg)][gem]
[![Code Climate](http://img.shields.io/codeclimate/github/42dev/bower-rails.svg)][codeclimate]
[![Dependency Status](http://img.shields.io/gemnasium/SergeyKishenin/bower-rails.svg)][gemnasium]
[![Build Status](https://travis-ci.org/42dev/bower-rails.svg?branch=master)][travis]
[![Coverage Status](https://coveralls.io/repos/42dev/bower-rails/badge.png)][coveralls]

[gem]: https://rubygems.org/gems/bower-rails
[travis]: https://travis-ci.org/42dev/bower-rails
[gemnasium]: https://gemnasium.com/SergeyKishenin/bower-rails
[codeclimate]: https://codeclimate.com/github/42dev/bower-rails
[coveralls]: https://coveralls.io/r/42dev/bower-rails

Bower support for Rails projects. Dependency file is bower.json in Rails root dir or Bowerfile if you use DSL.
Check out [changelog][] for the latest changes and releases.

[changelog]: https://github.com/42dev/bower-rails/blob/master/CHANGELOG.md

**Requirements**

* [node](http://nodejs.org) ([on github](https://github.com/joyent/node))
* [bower](https://github.com/bower/bower) (>= 0.10.0) installed with npm

**Install**

in Gemfile

``` Ruby
  gem "bower-rails", "~> 0.9.1"
```

##JSON configuration

Bower-rails now supports the standard [bower package](https://github.com/bower/bower#defining-a-package) format out-of-the-box. Simply place your bower.json file the Rails root directory to start. Using the standard format will default all bower components to be installed under the `vendor` directory.

To install dependencies into both `lib` and `vendor` directories, run the initializer to generate a custom bower.json:

``` Bash
  rails g bower_rails:initialize json
```

This will generate a `config/initializers/bower_rails.rb` config file and a special bower.json that combines two standard bower packages into one. Simply specify your dependencies under each folder name to install them into the corresponding directories.

**example bower.json file**

``` javascript
{
   "lib": {
    "name": "bower-rails generated lib assets",
    "dependencies": {
      "threex"      : "git@github.com:rharriso/threex.git",
      "gsvpano.js"  : "https://github.com/rharriso/GSVPano.js/blob/master/src/GSVPano.js"
    }
  },
  "vendor": {
    "name": "bower-rails generated vendor assets",
    "dependencies": {
      "three.js"    : "https://raw.github.com/mrdoob/three.js/master/build/three.js"
    }
  }
}
```

##Ruby DSL configuration

The Ruby DSL configuration is a Bowerfile at the project's root with DSL syntax similar to Bundler.

Run the initializer to generate a sample Bowerfile inside the Rails root and a `config/initializers/bower_rails.rb` config file:

``` Bash
  rails g bower_rails:initialize
```

**Example Bowerfile**

By default assets are put to `./vendor/assets/bower_components` directory:

``` ruby

# Puts to ./vendor/assets/bower_components
asset "backbone"
asset "moment", "2.0.0" # get exactly version 2.0.0
asset "secret_styles", "git@github.com:initech/secret_styles" # get from a git repo

# get from a git repo using the tag 1.0.0
asset "secret_logic", "1.0.0", git: "git@github.com:initech/secret_logic"

# get from a github repo
asset "secret_logic", "1.0.0", github: "initech/secret_logic"

# get a specific revision from a git endpoint
asset "secret_logic", github: "initech/secret_logic", ref: '0adff'
```

But the default value can be overridden by `assets_path` method:

``` ruby
assets_path "assets/my_javascripts"

# Puts to ./vendor/assets/my_javascripts/bower_components
asset "backbone"
asset "moment"
```

The `assets_path` method can be overridden by an option in a `group` call:

``` ruby
assets_path "assets/javascript"

# Puts files under ./vendor/assets/js/bower_components
group :vendor, :assets_path => "assets/js"  do
  asset "jquery"            # Defaults to 'latest'
  asset "backbone", "1.1.1"
end

# Puts files under ./lib/assets/javascript/bower_components
group :lib do
  asset "jquery"
  asset "backbone", "1.1.1"
end
```
NOTE: Available groups are `:lib` and `:vendor`. Others are not allowed according to the Rails convention.
NOTE: All the assets should be stored in `/assets` subdirectory so putting it under `./vendor/js` directory is unavailable

And finally, you can specify the assets to be in the devDependencies block:

``` ruby
asset "backbone", "1.1.1"

# Adds jasmine-sinon and jasmine-matchers to devDependencies
dependency_group :dev_dependencies  do
  asset "jasmine-sinon"            # Defaults to 'latest'
  asset "jasmine-matchers"         # Defaults to 'latest'
end

# Explicit dependency group notation ( not neccessary )
dependency_group :dependencies  do
  asset "emberjs"                  # Defaults to 'latest'
end
```
results in the following bower.json file:

```
{
  "name": "dsl-generated dependencies",
  "dependencies": {
    "backbone": "1.1.1"
    "angular": "1.2.18",
  },
  "devDependencies": {
    "jasmine-sinon": "latest",
    "jasmine-matchers": "latest"
  }
}
```
NOTE: Available dependency groups are `:dependencies` (default) and `:dev_dependencies`. Others are not allowed according to the Rails convention.

## Bower Resolutions

To specify a [bower resolution][] use `resolution` DSL method in your Bowerfile:

```ruby
resolution "angular", "1.2.22"
```

That will produce `bower.json` like:

``` javascript
{
  "name" : "dsl-generated dependencies",
  "dependencies" : {
    "angular" : "1.2.22"
  },
  "resolutions": {
    "angular": "1.2.22"
  }
}
```

[bower resolution]: http://jaketrent.com/post/bower-resolutions/

##Configuration

Change options in your `config/initializers/bower_rails.rb`:

``` ruby
BowerRails.configure do |bower_rails|
  # Tell bower-rails what path should be considered as root. Defaults to Dir.pwd
  bower_rails.root_path = Dir.pwd

  # Invokes rake bower:install before precompilation. Defaults to false
  bower_rails.install_before_precompile = true

  # Invokes rake bower:resolve before precompilation. Defaults to false
  bower_rails.resolve_before_precompile = true

  # Invokes rake bower:clean before precompilation. Defaults to false
  bower_rails.clean_before_precompile = true

  # Invokes rake bower:install:deployment instead rake bower:install. Defaults to false
  bower_rails.use_bower_install_deployment = true
end
```

If you are using Rails version < 4.0.0 then you are to require `bower_rails.rb` initializer manually in `application.rb`:

```ruby
module YourAppName
  class Application < Rails::Application
    require "#{Rails.root}/config/initializers/bower_rails.rb"
    ...
  end
end
```

By default this line is added while running the generator.

##Rake tasks

Once you are done with `bower.json` or `Bowerfile` you can run

* `rake bower:install` to install packages
* `rake bower:install:deployment` to install packages from bower.json
* `rake bower:update` to update packages
* `rake bower:update:prune` to update components and uninstall extraneous packages
* `rake bower:list` to list all packages
* `rake bower:clean` to remove all files not listed as [main files](#bower-main-files) (if specified)
* `rake bower:resolve` to resolve [relative asset paths](#relative-asset-paths) in components
* `rake bower:cache:clean` to clear the bower cache. This is useful when you know a component has been updated. 

If you'd like to pass any bower CLI options to a rake task, like `-f`, `-j`, you can simply do:

```bash
rake bower:install['-f']
```

##Bower Configuration

If you provide a `.bowerrc` in the rails project root, bower-rails will use it for bower configuration.
Some .bowerrc options are not supported: `directory`, `cwd`, and `interactive`. Bower-rails
will ignore the `directory` property and instead will use the automatically generated asset path.

###Bower Installation

[Bower](https://github.com/bower/bower) should be installed using npm. Bower can be installed globally (with `$ npm install -g bower`) or in `node_modules` in the root directory of your project.

##Relative asset paths

Some bower components (eg. [Bootstrap](https://github.com/twbs/bootstrap/blob/0016c17f9307bc71fc96d8d4680a9c861f137cae/dist/css/bootstrap.css#L2263)) have relative urls in the CSS files for imports, images, etc. Rails prefers using [helper methods](http://guides.rubyonrails.org/asset_pipeline.html#coding-links-to-assets) for linking to assets within CSS. Relative paths can cause issues when assets are precompiled for production.

Remember that you should have [bower installed](#bower-installation) either locally in your project or on a remote server.

##Bower Main Files

Each bower component should follow the [bower.json spec](https://github.com/bower/bower.json-spec) which designates a recommended `main` directive that lists the primary files of that component. You may choose to reference these files if you are using the asset pipeline, in which case other extraneous includes of the bower component are not needed. The `rake bower:clean` task removes every file that isn't listed in the `main` directive, if the component specifies a `main` directive. Otherwise, the library will remain as bower installed it. It supports wildcards in files listed in `main` directive.
# Ruby I18n

[![Build Status](https://api.travis-ci.org/svenfuchs/i18n.svg?branch=master)](https://travis-ci.org/svenfuchs/i18n)

Ruby Internationalization and localization solution.

Features:

* translation and localization
* interpolation of values to translations (Ruby 1.9 compatible syntax)
* pluralization (CLDR compatible)
* customizable transliteration to ASCII
* flexible defaults
* bulk lookup
* lambdas as translation data
* custom key/scope separator
* custom exception handlers
* extensible architecture with a swappable backend

Pluggable features:

* Cache
* Pluralization: lambda pluralizers stored as translation data
* Locale fallbacks, RFC4647 compliant (optionally: RFC4646 locale validation)
* Gettext support
* Translation metadata

Alternative backends:

* Chain
* ActiveRecord (optionally: ActiveRecord::Missing and ActiveRecord::StoreProcs)
* KeyValue (uses active_support/json and cannot store procs)

For more information and lots of resources see: [http://ruby-i18n.org/wiki](http://ruby-i18n.org/wiki)

## Installation

```
gem install i18n
```

## Tests

You can run tests both with

* `rake test` or just `rake`
* run any test file directly, e.g. `ruby -Ilib:test test/api/simple_test.rb`

You can run all tests against all Gemfiles with

* `ruby test/run_all.rb`

The structure of the test suite is a bit unusual as it uses modules to reuse
particular tests in different test cases.

The reason for this is that we need to enforce the I18n API across various
combinations of extensions. E.g. the Simple backend alone needs to support
the same API as any combination of feature and/or optimization modules included
to the Simple backend. We test this by reusing the same API defition (implemented
as test methods) in test cases with different setups.

You can find the test cases that enforce the API in test/api. And you can find
the API definition test methods in test/api/tests.

All other test cases (e.g. as defined in test/backend, test/core_ext) etc.
follow the usual test setup and should be easy to grok.

## Authors

* [Sven Fuchs](http://www.artweb-design.de)
* [Joshua Harvey](http://www.workingwithrails.com/person/759-joshua-harvey)
* [Stephan Soller](http://www.arkanis-development.de)
* [Saimon Moore](http://saimonmoore.net)
* [Matt Aimonetti](http://railsontherun.com)

## Contributors

https://github.com/svenfuchs/i18n/graphs/contributors

## License

MIT License. See the included MIT-LICENSE file.
Geocoder
========

Geocoder is a complete geocoding solution for Ruby. With Rails it adds geocoding (by street or IP address), reverse geocoding (finding street address based on given coordinates), and distance queries. It's as simple as calling `geocode` on your objects, and then using a scope like `Venue.near("Billings, MT")`.

_Please note that this README is for the current `HEAD` and may document features not present in the latest gem release. For this reason, you may want to instead view the README for your particular version._


Compatibility
-------------

* Supports multiple Ruby versions: Ruby 1.9.3, 2.0.x, 2.1.x, JRuby, and Rubinius.
* Supports multiple databases: MySQL, PostgreSQL, SQLite, and MongoDB (1.7.0 and higher).
* Supports Rails 3 and 4. If you need to use it with Rails 2 please see the `rails2` branch (no longer maintained, limited feature set).
* Works very well outside of Rails, you just need to install either the `json` (for MRI) or `json_pure` (for JRuby) gem.


Rails 4.1 Note
--------------

Due to [a change in ActiveRecord's `count` method](https://github.com/rails/rails/pull/10710) you will need to use `count(:all)` to explicitly count all columns ("*") when using a `near` scope. Using `near` and calling `count` with no argument will cause exceptions in many cases.


Installation
------------

Install Geocoder like any other Ruby gem:

    gem install geocoder

Or, if you're using Rails/Bundler, add this to your Gemfile:

    gem 'geocoder'

and run at the command prompt:

    bundle install


Object Geocoding
----------------

### ActiveRecord

Your model must have two attributes (database columns) for storing latitude and longitude coordinates. By default they should be called `latitude` and `longitude` but this can be changed (see "Model Configuration" below):

    rails generate migration AddLatitudeAndLongitudeToModel latitude:float longitude:float
    rake db:migrate

For reverse geocoding your model must provide a method that returns an address. This can be a single attribute, but it can also be a method that returns a string assembled from different attributes (eg: `city`, `state`, and `country`).

Next, your model must tell Geocoder which method returns your object's geocodable address:

    geocoded_by :full_street_address   # can also be an IP address
    after_validation :geocode          # auto-fetch coordinates

For reverse geocoding, tell Geocoder which attributes store latitude and longitude:

    reverse_geocoded_by :latitude, :longitude
    after_validation :reverse_geocode  # auto-fetch address

### Mongoid

First, your model must have an array field for storing coordinates:

    field :coordinates, :type => Array

You may also want an address field, like this:

    field :address

but if you store address components (city, state, country, etc) in separate fields you can instead define a method called `address` that combines them into a single string which will be used to query the geocoding service.

Once your fields are defined, include the `Geocoder::Model::Mongoid` module and then call `geocoded_by`:

    include Geocoder::Model::Mongoid
    geocoded_by :address               # can also be an IP address
    after_validation :geocode          # auto-fetch coordinates

Reverse geocoding is similar:

    include Geocoder::Model::Mongoid
    reverse_geocoded_by :coordinates
    after_validation :reverse_geocode  # auto-fetch address

Once you've set up your model you'll need to create the necessary spatial indices in your database:

    rake db:mongoid:create_indexes

Be sure to read _Latitude/Longitude Order_ in the _Notes on MongoDB_ section below on how to properly retrieve latitude/longitude coordinates from your objects.

### MongoMapper

MongoMapper is very similar to Mongoid, just be sure to include `Geocoder::Model::MongoMapper`.

### Mongo Indices

By default, the methods `geocoded_by` and `reverse_geocoded_by` create a geospatial index. You can avoid index creation with the `:skip_index option`, for example:

    include Geocoder::Model::Mongoid
    geocoded_by :address, :skip_index => true

### Bulk Geocoding

If you have just added geocoding to an existing application with a lot of objects you can use this Rake task to geocode them all:

    rake geocode:all CLASS=YourModel

Geocoder will print warnings if you exceed the rate limit for your geocoding service. Some services — Google notably — enforce a per-second limit in addition to a per-day limit. To avoid exceeding the per-second limit, you can add a `SLEEP` option to pause between requests for a given amount of time. You can also load objects in batches to save memory, for example:

    rake geocode:all CLASS=YourModel SLEEP=0.25 BATCH=100

### Avoiding Unnecessary API Requests

Geocoding only needs to be performed under certain conditions. To avoid unnecessary work (and quota usage) you will probably want to geocode an object only when:

* an address is present
* the address has been changed since last save (or it has never been saved)

The exact code will vary depending on the method you use for your geocodable string, but it would be something like this:

    after_validation :geocode, if: ->(obj){ obj.address.present? and obj.address_changed? }


Request Geocoding by IP Address
-------------------------------

Geocoder adds `location` and `safe_location` methods to the standard `Rack::Request` object so you can easily look up the location of any HTTP request by IP address. For example, in a Rails controller or a Sinatra app:

    # returns Geocoder::Result object
    result = request.location

**The `location` method is vulnerable to trivial IP address spoofing via HTTP headers.**  If that's a problem for your application, use `safe_location` instead, but be aware that `safe_location` will *not* try to trace a request's originating IP through proxy headers; you will instead get the location of the last proxy the request passed through, if any (excepting any proxies you have explicitly whitelisted in your Rack config).

Note that these methods will usually return `nil` in your test and development environments because things like "localhost" and "0.0.0.0" are not an Internet IP addresses.

See _Advanced Geocoding_ below for more information about `Geocoder::Result` objects.


Location-Aware Database Queries
-------------------------------

To find objects by location, use the following scopes:

    Venue.near('Omaha, NE, US', 20)    # venues within 20 miles of Omaha
    Venue.near([40.71, -100.23], 20)    # venues within 20 miles of a point
    Venue.near([40.71, -100.23], 20, :units => :km)
                                       # venues within 20 kilometres of a point
    Venue.geocoded                     # venues with coordinates
    Venue.not_geocoded                 # venues without coordinates

With geocoded objects you can do things like this:

    if obj.geocoded?
      obj.nearbys(30)                      # other objects within 30 miles
      obj.distance_from([40.714,-100.234]) # distance from arbitrary point to object
      obj.bearing_to("Paris, France")      # direction from object to arbitrary point
    end

Some utility methods are also available:

    # look up coordinates of some location (like searching Google Maps)
    Geocoder.coordinates("25 Main St, Cooperstown, NY")
     => [42.700149, -74.922767]

    # distance between Eiffel Tower and Empire State Building
    Geocoder::Calculations.distance_between([47.858205,2.294359], [40.748433,-73.985655])
     => 3619.77359999382 # in configured units (default miles)

    # find the geographic center (aka center of gravity) of objects or points
    Geocoder::Calculations.geographic_center([city1, city2, [40.22,-73.99], city4])
     => [35.14968, -90.048929]

Please see the code for more methods and detailed information about arguments (eg, working with kilometers).


Distance and Bearing
--------------------

When you run a location-aware query the returned objects have two attributes added to them (only w/ ActiveRecord):

* `obj.distance` - number of miles from the search point to this object
* `obj.bearing` - direction from the search point to this object

Results are automatically sorted by distance from the search point, closest to farthest. Bearing is given as a number of clockwise degrees from due north, for example:

* `0` - due north
* `180` - due south
* `90` - due east
* `270` - due west
* `230.1` - southwest
* `359.9` - almost due north

You can convert these numbers to compass point names by using the utility method provided:

    Geocoder::Calculations.compass_point(355) # => "N"
    Geocoder::Calculations.compass_point(45)  # => "NE"
    Geocoder::Calculations.compass_point(208) # => "SW"

_Note: when using SQLite `distance` and `bearing` values are provided for interface consistency only. They are not very accurate._

To calculate accurate distance and bearing with SQLite or MongoDB:

    obj.distance_to([43.9,-98.6])  # distance from obj to point
    obj.bearing_to([43.9,-98.6])   # bearing from obj to point
    obj.bearing_from(obj2)         # bearing from obj2 to obj

The `bearing_from/to` methods take a single argument which can be: a `[lat,lon]` array, a geocoded object, or a geocodable address (string). The `distance_from/to` methods also take a units argument (`:mi`, `:km`, or `:nm` for nautical miles).


Model Configuration
-------------------

You are not stuck with using the `latitude` and `longitude` database column names (with ActiveRecord) or the `coordinates` array (Mongo) for storing coordinates. For example:

    geocoded_by :address, :latitude  => :lat, :longitude => :lon # ActiveRecord
    geocoded_by :address, :coordinates => :coords                # MongoDB

The `address` method can return any string you'd use to search Google Maps. For example, any of the following are acceptable:

* "714 Green St, Big Town, MO"
* "Eiffel Tower, Paris, FR"
* "Paris, TX, US"

If your model has `street`, `city`, `state`, and `country` attributes you might do something like this:

    geocoded_by :address

    def address
      [street, city, state, country].compact.join(', ')
    end

For reverse geocoding you can also specify an alternate name attribute where the address will be stored, for example:

    reverse_geocoded_by :latitude, :longitude, :address => :location  # ActiveRecord
    reverse_geocoded_by :coordinates, :address => :loc                # MongoDB

You can also configure a specific lookup for your model which will override the globally-configured lookup, for example:

    geocoded_by :address, :lookup => :yandex

You can also specify a proc if you want to choose a lookup based on a specific property of an object, for example you can use specialized lookups for different regions:

    geocoded_by :address, :lookup => lambda{ |obj| obj.geocoder_lookup }

    def geocoder_lookup
      if country_code == "RU"
        :yandex
      elsif country_code == "CN"
        :baidu
      else
        :google
      end
    end


Advanced Querying
-----------------

When querying for objects (if you're using ActiveRecord) you can also look within a square rather than a radius (circle) by using the `within_bounding_box` scope:

    distance = 20
    center_point = [40.71, 100.23]
    box = Geocoder::Calculations.bounding_box(center_point, distance)
    Venue.within_bounding_box(box)

This can also dramatically improve query performance, especially when used in conjunction with indexes on the latitude/longitude columns. Note, however, that returned results do not include `distance` and `bearing` attributes. Note that `#near` performs both bounding box and radius queries for speed.

You can also specify a minimum radius (if you're using ActiveRecord and not Sqlite) to constrain the
lower bound (ie. think of a donut, or ring) by using the `:min_radius` option:

    box = Geocoder::Calculations.bounding_box(center_point, distance, :min_radius => 10.5)

With ActiveRecord, you can specify alternate latitude and longitude column names for a geocoded model (useful if you store multiple sets of coordinates for each object):

    Venue.near("Paris", 50, latitude: :secondary_latitude, longitude: :secondary_longitude)


Advanced Geocoding
------------------

So far we have looked at shortcuts for assigning geocoding results to object attributes. However, if you need to do something fancy you can skip the auto-assignment by providing a block (takes the object to be geocoded and an array of `Geocoder::Result` objects) in which you handle the parsed geocoding result any way you like, for example:

    reverse_geocoded_by :latitude, :longitude do |obj,results|
      if geo = results.first
        obj.city    = geo.city
        obj.zipcode = geo.postal_code
        obj.country = geo.country_code
      end
    end
    after_validation :reverse_geocode

Every `Geocoder::Result` object, `result`, provides the following data:

* `result.latitude` - float
* `result.longitude` - float
* `result.coordinates` - array of the above two
* `result.address` - string
* `result.city` - string
* `result.state` - string
* `result.state_code` - string
* `result.postal_code` - string
* `result.country` - string
* `result.country_code` - string

If you're familiar with the results returned by the geocoding service you're using you can access even more data (call the `#data` method of any Geocoder::Result object to get the full parsed response), but you'll need to be familiar with the particular `Geocoder::Result` object you're using and the structure of your geocoding service's responses. (See below for links to geocoding service documentation.)


Geocoding Service ("Lookup") Configuration
------------------------------------------

Geocoder supports a variety of street and IP address geocoding services. The default lookups are `:google` for street addresses and `:freegeoip` for IP addresses. Please see the listing and comparison below for details on specific geocoding services (not all settings are supported by all services).

To create a Rails initializer with an example configuration:

    rails generate geocoder:config

Some common configuration options are:

    # config/initializers/geocoder.rb
    Geocoder.configure(

      # geocoding service (see below for supported options):
      :lookup => :yandex,

      # IP address geocoding service (see below for supported options):
      :ip_lookup => :maxmind,

      # to use an API key:
      :api_key => "...",

      # geocoding service request timeout, in seconds (default 3):
      :timeout => 5,

      # set default units to kilometers:
      :units => :km,

      # caching (see below for details):
      :cache => Redis.new,
      :cache_prefix => "..."

    )

Please see lib/geocoder/configuration.rb for a complete list of configuration options. Additionally, some lookups have their own configuration options, some of which are directly supported by Geocoder. For example, to specify a value for Google's `bounds` parameter:

    # with Google:
    Geocoder.search("Paris", :bounds => [[32.1,-95.9], [33.9,-94.3]])

Please see the [source code for each lookup](https://github.com/alexreisner/geocoder/tree/master/lib/geocoder/lookups) to learn about directly supported parameters. Parameters which are not directly supported can be specified using the `:params` option, by which you can pass arbitrary parameters to any geocoding service. For example, to use Nominatim's `countrycodes` parameter:

    # with Nominatim:
    Geocoder.search("Paris", :params => {:countrycodes => "gb,de,fr,es,us"})

You can also configure multiple geocoding services at once, like this:

    Geocoder.configure(

      :timeout => 2,
      :cache => Redis.new,

      :yandex => {
        :api_key => "...",
        :timeout => 5
      },

      :baidu => {
        :api_key => "..."
      },

      :maxmind => {
        :api_key => "...",
        :service => :omni
      }

    )

The above combines global and service-specific options and could be useful if you specify different geocoding services for different models or under different conditions. Lookup-specific settings override global settings so, for example, in the above the timeout for all lookups would be 2 seconds, except for Yandex which would be 5.


### Street Address Services

The following is a comparison of the supported geocoding APIs. The "Limitations" listed for each are a very brief and incomplete summary of some special limitations beyond basic data source attribution. Please read the official Terms of Service for a service before using it.

#### Google (`:google`, `:google_premier`)

* **API key**: required for Premier, optional for the free service (if using the free service with API key, https is required. Add `:use_https  => true` to `Geocoder.configure`)
* **Key signup**: https://developers.google.com/maps/documentation/business/
* **Quota**: 2,500 requests/day, 100,000 with Google Maps API Premier
* **Region**: world
* **SSL support**: yes
* **Languages**: ar, eu, bg, bn, ca, cs, da, de, el, en, en-AU, en-GB, es, eu, fa, fi, fil, fr, gl, gu, hi, hr, hu, id, it, iw, ja, kn, ko, lt, lv, ml, mr, nl, no, pl, pt, pt-BR, pt-PT, ro, ru, sk, sl, sr, sv, tl, ta, te, th, tr, uk, vi, zh-CN, zh-TW (see http://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)
* **Extra options**: `:bounds` - pass SW and NE coordinates as an array of two arrays to bias results towards a viewport
* **Documentation**: http://code.google.com/apis/maps/documentation/geocoding/#JSON
* **Terms of Service**: http://code.google.com/apis/maps/terms.html#section_10_12
* **Limitations**: "You must not use or display the Content without a corresponding Google map, unless you are explicitly permitted to do so in the Maps APIs Documentation, or through written permission from Google." "You must not pre-fetch, cache, or store any Content, except that you may store: (i) limited amounts of Content for the purpose of improving the performance of your Maps API Implementation..."
* **Notes**: To use Google Premier set `Geocoder.configure(:lookup => :google_premier, :api_key => [key, client, channel])`.

#### Google Places Details (`:google_places_details`)

The [Google Places Details API](https://developers.google.com/places/documentation/details) is not, strictly speaking, a geocoding service. It accepts a Google `place_id` and returns address information, ratings and reviews. A `place_id` can be obtained from the Google Places Autocomplete API and should be passed to Geocoder as the first search argument: `Geocoder.search("ChIJhRwB-yFawokR5Phil-QQ3zM", :lookup => :google_places_details)`.

* **API key**: required
* **Key signup**: https://code.google.com/apis/console/
* **Quota**: 1,000 request/day, 100,000 after credit card authentication
* **Region**: world
* **SSL support**: yes
* **Languages**: ar, eu, bg, bn, ca, cs, da, de, el, en, en-AU, en-GB, es, eu, fa, fi, fil, fr, gl, gu, hi, hr, hu, id, it, iw, ja, kn, ko, lt, lv, ml, mr, nl, no, pl, pt, pt-BR, pt-PT, ro, ru, sk, sl, sr, sv, tl, ta, te, th, tr, uk, vi, zh-CN, zh-TW (see http://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)
* **Documentation**: https://developers.google.com/places/documentation/details
* **Terms of Service**: https://developers.google.com/places/policies
* **Limitations**: "If your application displays Places API data on a page or view that does not also display a Google Map, you must show a "Powered by Google" logo with that data."

#### Yahoo BOSS (`:yahoo`)

* **API key**: requires OAuth consumer key and secret (set `Geocoder.configure(:api_key => [key, secret])`)
* **Key signup**: http://developer.yahoo.com/boss/geo/
* **Quota**: unlimited, but subject to usage fees
* **Region**: world
* **SSL support**: no
* **Languages**: en, fr, de, it, es, pt, nl, zh, ja, ko
* **Documentation**: http://developer.yahoo.com/boss/geo/docs/index.html
* **Terms of Service**: http://info.yahoo.com/legal/us/yahoo/boss/tou/?pir=ucJPcJ1ibUn.h.d.lVmlcbcEkoHjwJ_PvxG9SLK9VIbIQAw1XFrnDqY-
* **Limitations**: No mass downloads, no commercial map production based on the data, no storage of data except for caching.

#### Bing (`:bing`)

* **API key**: required (set `Geocoder.configure(:lookup => :bing, :api_key => key)`)
* **Key signup**: https://www.microsoft.com/maps/create-a-bing-maps-key.aspx
* **Quota**: 50,0000 requests/day (Windows app), 125,000 requests/year (non-Windows app)
* **Region**: world
* **SSL support**: no
* **Languages**: ?
* **Documentation**: http://msdn.microsoft.com/en-us/library/ff701715.aspx
* **Terms of Service**: http://www.microsoft.com/maps/product/terms.html
* **Limitations**: No country codes or state names. Must be used on "public-facing, non-password protected web sites," "in conjunction with Bing Maps or an application that integrates Bing Maps."

#### Nominatim (`:nominatim`)

* **API key**: none
* **Quota**: 1 request/second
* **Region**: world
* **SSL support**: no
* **Languages**: ?
* **Documentation**: http://wiki.openstreetmap.org/wiki/Nominatim
* **Terms of Service**: http://wiki.openstreetmap.org/wiki/Nominatim_usage_policy
* **Limitations**: Please limit request rate to 1 per second and include your contact information in User-Agent headers (eg: `Geocoder.configure(:http_headers => { "User-Agent" => "your contact info" })`). Data licensed under CC-BY-SA (you must provide attribution).

#### OpenCageData (`:opencagedata`)

* **API key**: required
* **Key signup**: http://geocoder.opencagedata.com
* **Quota**: 2500 requests / day, then ability to purchase more (free during beta)
* **Region**: world
* **SSL support**: yes
* **Languages**: worldwide
* **Documentation**: http://geocoder.opencagedata.com/api.html
* **Limitations**: Data licensed under CC-BY-SA or (you must provide attribution).

#### Yandex (`:yandex`)

* **API key**: none
* **Quota**: 25000 requests / day
* **Region**: world
* **SSL support**: no
* **Languages**: Russian, Belarusian, Ukrainian, English, Turkish (only for maps of Turkey)
* **Documentation**: http://api.yandex.com.tr/maps/doc/intro/concepts/intro.xml
* **Terms of Service**: http://api.yandex.com.tr/maps/doc/intro/concepts/intro.xml#rules
* **Limitations**: ?

#### Geocoder.ca (`:geocoder_ca`)

* **API key**: none
* **Quota**: ?
* **Region**: US and Canada
* **SSL support**: no
* **Languages**: English
* **Documentation**: ?
* **Terms of Service**: http://geocoder.ca/?terms=1
* **Limitations**: "Under no circumstances can our data be re-distributed or re-sold by anyone to other parties without our written permission."

#### Geocoder.us (`:geocoder_us`)

* **API key**: HTTP Basic Auth
* **Sign up**: http://geocoder.us/user/signup
* **Quota**: You can purchase 20,000 credits at a time for $50
* **Region**: US
* **SSL support**: no
* **Languages**: English
* **Documentation**: http://geocoder.us/help/
* **Terms of Service**: http://geocoder.us/terms.shtml
* **Limitations**: ?

#### Mapquest (`:mapquest`)

* **API key**: required
* **Key signup**: http://developer.mapquest.com/web/products/open
* **Quota**: ?
* **HTTP Headers**: when using the licensed API you can specify a referer like so:
    `Geocoder.configure(:http_headers => { "Referer" => "http://foo.com" })`
* **Region**: world
* **SSL support**: no
* **Languages**: English
* **Documentation**: http://www.mapquestapi.com/geocoding/
* **Terms of Service**: http://info.mapquest.com/terms-of-use/
* **Limitations**: ?
* **Notes**: You can use the open (non-licensed) API by setting: `Geocoder.configure(:mapquest => {:open => true})` (defaults to licensed version)

#### Ovi/Nokia (`:ovi`)

* **API key**: not required, but performance restricted without it
* **Quota**: ?
* **Region**: world
* **SSL support**: no
* **Languages**: English
* **Documentation**: http://api.maps.ovi.com/devguide/overview.html
* **Terms of Service**: http://www.developer.nokia.com/Develop/Maps/TC.html
* **Limitations**: ?

#### Here/Nokia (`:here`)

* **API key**: required (set `Geocoder.configure(:api_key => [app_id, app_code])`)
* **Quota**: Depending on the API key
* **Region**: world
* **SSL support**: yes
* **Languages**: The preferred language of address elements in the result. Language code must be provided according to RFC 4647 standard.
* **Documentation**: http://developer.here.com/rest-apis/documentation/geocoder
* **Terms of Service**: http://developer.here.com/faqs#l&t
* **Limitations**: ?

#### ESRI (`:esri`)

* **API key**: none
* **Quota**: Required for some scenarios (see Terms of Service)
* **Region**: world
* **SSL support**: yes
* **Languages**: English
* **Documentation**: http://resources.arcgis.com/en/help/arcgis-online-geocoding-rest-api/
* **Terms of Service**: http://www.esri.com/legal/software-license
* **Limitations**: ?
* **Notes**: You can specify which projection you want to use by setting, for example: `Geocoder.configure(:esri => {:outSR => 102100})`.

#### Data Science Toolkit (`:dstk`)

Data Science Toolkit provides an API whose reponse format is like Google's but which can be set up as a privately hosted service.

* **API key**: none
* **Quota**: None quota if you are self-hosting the service.
* **Region**: world
* **SSL support**: ?
* **Languages**: en
* **Documentation**: http://www.datasciencetoolkit.org/developerdocs
* **Terms of Service**: http://www.datasciencetoolkit.org/developerdocs#googlestylegeocoder
* **Limitations**: No reverse geocoding.
* **Notes**: If you are hosting your own DSTK server you will need to configure the host name, eg: `Geocoder.configure(:lookup => :dstk, :host => "localhost:4567")`.

#### Baidu (`:baidu`)

* **API key**: required
* **Quota**: No quota limits for geocoding
* **Region**: China
* **SSL support**: no
* **Languages**: Chinese (Simplified)
* **Documentation**: http://developer.baidu.com/map/webservice-geocoding.htm
* **Terms of Service**: http://developer.baidu.com/map/law.htm
* **Limitations**: Only good for non-commercial use. For commercial usage please check http://developer.baidu.com/map/question.htm#qa0013
* **Notes**: To use Baidu set `Geocoder.configure(:lookup => :baidu, :api_key => "your_api_key")`.

#### Geocodio (`:geocodio`)

* **API key**: required
* **Quota**: 2,500 free requests/day then purchase $.001 for each
* **Region**: US
* **SSL support**: no
* **Languages**: en
* **Documentation**: http://geocod.io/docs
* **Terms of Service**: http://geocod.io/terms-of-use
* **Limitations**: ?

#### SmartyStreets (`:smarty_streets`)

* **API key**: requires auth_id and auth_token (set `Geocoder.configure(:api_key => [id, token])`)
* **Quota**: 10,000 free, 250/month then purchase at sliding scale.
* **Region**: US
* **SSL support**: yes (required)
* **Languages**: en
* **Documentation**: http://smartystreets.com/kb/liveaddress-api/rest-endpoint
* **Terms of Service**: http://smartystreets.com/legal/terms-of-service
* **Limitations**: No reverse geocoding.


#### OKF Geocoder (`:okf`)

* **API key**: none
* **Quota**: none
* **Region**: FI
* **SSL support**: no
* **Languages**: fi
* **Documentation**: http://books.okf.fi/geocoder/_full/
* **Terms of Service**: http://www.itella.fi/liitteet/palvelutjatuotteet/yhteystietopalvelut/Postinumeropalvelut-Palvelukuvausjakayttoehdot.pdf
* **Limitations**: ?


#### PostcodeAnywhere Uk (`:postcode_anywhere_uk`)

This uses the PostcodeAnywhere UK Geocode service, this will geocode any string from UK postcode, placename, point of interest or location.

* **API key**: required
* **Quota**: Dependant on service plan?
* **Region**: UK
* **SSL support**: yes
* **Languages**: English
* **Documentation**: [http://www.postcodeanywhere.co.uk/Support/WebService/Geocoding/UK/Geocode/2/](http://www.postcodeanywhere.co.uk/Support/WebService/Geocoding/UK/Geocode/2/)
* **Terms of Service**: ?
* **Limitations**: ?
* **Notes**: To use PostcodeAnywhere you must include an API key: `Geocoder.configure(:lookup => :postcode_anywhere_uk, :api_key => 'your_api_key')`.


### IP Address Services

#### FreeGeoIP (`:freegeoip`)

* **API key**: none
* **Quota**: 10000 requests per hour. After reaching the hourly quota, all of your requests will result in HTTP 403 (Forbidden) until it clears up on the next roll over.
* **Region**: world
* **SSL support**: no
* **Languages**: English
* **Documentation**: http://github.com/fiorix/freegeoip/blob/master/README.md
* **Terms of Service**: ?
* **Limitations**: ?
* **Notes**: If you are [running your own local instance of the FreeGeoIP service](https://github.com/fiorix/freegeoip) you can configure the host like this: `Geocoder.configure(freegeoip: {host: "..."})`.

#### Pointpin (`:pointpin`)

* **API key**: required
* **Quota**: 50,000/mo for €9 through 1m/mo for €49
* **Region**: world
* **SSL support**: yes
* **Languages**: English
* **Documentation**: https://pointp.in/docs/get-started
* **Terms of Service**: https://pointp.in/terms
* **Limitations**: ?
* **Notes**: To use Pointpin set `Geocoder.configure(:ip_lookup => :pointpin, :api_key => "your_pointpin_api_key")`.

#### Telize (`:telize`)

* **API key**: none
* **Quota**: none
* **Region**: world
* **SSL support**: no
* **Languages**: English
* **Documentation**: http://www.telize.com/
* **Terms of Service**: ?
* **Limitations**: ?

#### MaxMind Legacy Web Services (`:maxmind`)

* **API key**: required
* **Quota**: Request Packs can be purchased
* **Region**: world
* **SSL support**: yes
* **Languages**: English
* **Documentation**: http://dev.maxmind.com/geoip/legacy/web-services/
* **Terms of Service**: ?
* **Limitations**: ?
* **Notes**: You must specify which MaxMind service you are using in your configuration. For example: `Geocoder.configure(:maxmind => {:service => :omni})`.

#### Baidu IP (`:baidu_ip`)

* **API key**: required
* **Quota**: No quota limits for geocoding
* **Region**: China
* **SSL support**: no
* **Languages**: Chinese (Simplified)
* **Documentation**: http://developer.baidu.com/map/webservice-geocoding.htm
* **Terms of Service**: http://developer.baidu.com/map/law.htm
* **Limitations**: Only good for non-commercial use. For commercial usage please check http://developer.baidu.com/map/question.htm#qa0013
* **Notes**: To use Baidu set `Geocoder.configure(:lookup => :baidu_ip, :api_key => "your_api_key")`.


### IP Address Local Database Services

#### MaxMind Local (`:maxmind_local`) - EXPERIMENTAL

This lookup provides methods for geocoding IP addresses without making a call to a remote API (improves speed and availability). It works, but support is new and should not be considered production-ready. Please [report any bugs](https://github.com/alexreisner/geocoder/issues) you encounter.

* **API key**: none (requires the GeoLite City database which can be downloaded from [MaxMind](http://dev.maxmind.com/geoip/legacy/geolite/))
* **Quota**: none
* **Region**: world
* **SSL support**: N/A
* **Languages**: English
* **Documentation**: http://www.maxmind.com/en/city
* **Terms of Service**: ?
* **Limitations**: ?
* **Notes**: There are two supported formats for MaxMind local data: binary file, and CSV file imported into an SQL database. **You must download a database from MaxMind and set either the `:file` or `:package` configuration option for local lookups to work.**

**To use a binary file** you must add the *geoip* (or *jgeoip* for JRuby) gem to your Gemfile or have it installed in your system, and specify the path of the MaxMind database in your configuration. For example:

    Geocoder.configure(ip_lookup: :maxmind_local, maxmind_local: {file: File.join('folder', 'GeoLiteCity.dat')})

**To use a CSV file** you must import it into an SQL database. The GeoLite *City* and *Country* packages are supported. Configure like so:

    Geocoder.configure(ip_lookup: :maxmind_local, maxmind_local: {package: :city})

You can generate ActiveRecord migrations and download and import data via provided rake tasks:

    # generate migration to create tables
    rails generate geocoder:maxmind:geolite_city

    # download, unpack, and import data
    rake geocoder:maxmind:geolite:load PACKAGE=city

You can replace `city` with `country` in any of the above tasks, generators, and configurations.

#### GeoLite2 (`:geoip2`)

This lookup provides methods for geocoding IP addresses without making a call to a remote API (improves speed and availability). It works, but support is new and should not be considered production-ready. Please [report any bugs](https://github.com/alexreisner/geocoder/issues) you encounter.

* **API key**: none (requires a GeoIP2 or free GeoLite2 City or Country binary database which can be downloaded from [MaxMind](http://dev.maxmind.com/geoip/geoip2/))
* **Quota**: none
* **Region**: world
* **SSL support**: N/A
* **Languages**: English
* **Documentation**: http://www.maxmind.com/en/city
* **Terms of Service**: ?
* **Limitations**: ?
* **Notes**: **You must download a binary database file from MaxMind and set the `:file` configuration option.** The CSV format databases are not yet supported since they are still in alpha stage. Set the path to the database file in your configuration:

    Geocoder.configure(
      ip_lookup: :geoip2,
      geoip2: {
        file: File.join('folder', 'GeoLite2-City.mmdb')
      }
    )

You must add either the *[hive_geoip2](https://rubygems.org/gems/hive_geoip2)* gem (native extension that relies on libmaxminddb) or the *[maxminddb](http://rubygems.org/gems/maxminddb)* gem (pure Ruby implementation) to your Gemfile or have it installed in your system. The pure Ruby gem (maxminddb) will be used by default. To use `hive_geoip2`:

    Geocoder.configure(
      ip_lookup: :geoip2,
      geoip2: {
        lib: 'hive_geoip2',
        file: File.join('folder', 'GeoLite2-City.mmdb')
      }
    )

Caching
-------

It's a good idea, when relying on any external service, to cache retrieved data. When implemented correctly it improves your app's response time and stability. It's easy to cache geocoding results with Geocoder, just configure a cache store:

    Geocoder.configure(:cache => Redis.new)

This example uses Redis, but the cache store can be any object that supports these methods:

* `store#[](key)` or `#get` or `#read` - retrieves a value
* `store#[]=(key, value)` or `#set` or `#write` - stores a value
* `store#del(url)` - deletes a value

Even a plain Ruby hash will work, though it's not a great choice (cleared out when app is restarted, not shared between app instances, etc).

You can also set a custom prefix to be used for cache keys:

    Geocoder.configure(:cache_prefix => "...")

By default the prefix is `geocoder:`

If you need to expire cached content:

    Geocoder::Lookup.get(Geocoder.config[:lookup]).cache.expire(:all)  # expire cached results for current Lookup
    Geocoder::Lookup.get(:google).cache.expire("http://...")           # expire cached result for a specific URL
    Geocoder::Lookup.get(:google).cache.expire(:all)                   # expire cached results for Google Lookup
    # expire all cached results for all Lookups.
    # Be aware that this methods spawns a new Lookup object for each Service
    Geocoder::Lookup.all_services.each{|service| Geocoder::Lookup.get(service).cache.expire(:all)}

Do *not* include the prefix when passing a URL to be expired. Expiring `:all` will only expire keys with the configured prefix (won't kill every entry in your key/value store).

For an example of a cache store with URL expiry please see examples/autoexpire_cache.rb

_Before you implement caching in your app please be sure that doing so does not violate the Terms of Service for your geocoding service._


Forward and Reverse Geocoding in the Same Model
-----------------------------------------------

If you apply both forward and reverse geocoding functionality to the same model (say users can supply an address or coordinates and you want to fill in whatever's missing), you will provide two address methods:

* one for storing the fetched address (reverse geocoding)
* one for providing an address to use when fetching coordinates (forward geocoding)

For example:

    class Venue

      # build an address from street, city, and state attributes
      geocoded_by :address_from_components

      # store the fetched address in the full_address attribute
      reverse_geocoded_by :latitude, :longitude, :address => :full_address
    end

However, there can be only one set of latitude/longitude attributes, and whichever you specify last will be used. For example:

    class Venue

      geocoded_by :address,
        :latitude  => :fetched_latitude,  # this will be overridden by the below
        :longitude => :fetched_longitude  # same here

      reverse_geocoded_by :latitude, :longitude
    end

The reason for this is that we don't want ambiguity when doing distance calculations. We need a single, authoritative source for coordinates!

Once both forward and reverse geocoding has been applied, it is possible to call them sequentially.

For example:

    class Venue

      after_validation :geocode, :reverse_geocode

    end

For certain geolocation services such as Google geolocation API this may cause issues during subsequent updates to database records if the longtitude and latitude coordinates cannot be associated known location address (on a large body of water for example). On subsequent callbacks the following call:

     after_validation :geocode

will alter the longtitude and latitude attributes based on the location field, which would be the closest known location to the original coordinates. In this case it is better to add conditions to each call, as not to override coordinates that do not have known location addresses associated with them.

For example:

    class Venue

      after_validation :reverse_geocode, :if => :has_coordinates
      after_validation :geocode, :if => :has_location, :unless => :has_coordinates

    end

Use Outside of Rails
--------------------

You can use Geocoder outside of Rails by calling the `Geocoder.search` method:

    results = Geocoder.search("McCarren Park, Brooklyn, NY")

This returns an array of `Geocoder::Result` objects with all data provided by the geocoding service.


Testing Apps that Use Geocoder
------------------------------

When writing tests for an app that uses Geocoder it may be useful to avoid network calls and have Geocoder return consistent, configurable results. To do this, configure and use the `:test` lookup. For example:

    Geocoder.configure(:lookup => :test)

    Geocoder::Lookup::Test.add_stub(
      "New York, NY", [
        {
          'latitude'     => 40.7143528,
          'longitude'    => -74.0059731,
          'address'      => 'New York, NY, USA',
          'state'        => 'New York',
          'state_code'   => 'NY',
          'country'      => 'United States',
          'country_code' => 'US'
        }
      ]
    )

Now, any time Geocoder looks up "New York, NY" its results array will contain one result with the above attributes. You can also set a default stub, to be returned when no other stub is found for a given query:

    Geocoder.configure(:lookup => :test)

    Geocoder::Lookup::Test.set_default_stub(
      [
        {
          'latitude'     => 40.7143528,
          'longitude'    => -74.0059731,
          'address'      => 'New York, NY, USA',
          'state'        => 'New York',
          'state_code'   => 'NY',
          'country'      => 'United States',
          'country_code' => 'US'
        }
      ]
    )


Command Line Interface
----------------------

When you install the Geocoder gem it adds a `geocode` command to your shell. You can search for a street address, IP address, postal code, coordinates, etc just like you can with the Geocoder.search method for example:

    $ geocode 29.951,-90.081
    Latitude:         29.952211
    Longitude:        -90.080563
    Full address:     1500 Sugar Bowl Dr, New Orleans, LA 70112, USA
    City:             New Orleans
    State/province:   Louisiana
    Postal code:      70112
    Country:          United States
    Google map:       http://maps.google.com/maps?q=29.952211,-90.080563

There are also a number of options for setting the geocoding API, key, and language, viewing the raw JSON reponse, and more. Please run `geocode -h` for details.

Numeric Data Types and Precision
--------------------------------

Geocoder works with any numeric data type (e.g. float, double, decimal) on which trig (and other mathematical) functions can be performed.

A summary of the relationship between geographic precision and the number of decimal places in latitude and longitude degree values is available on [Wikipedia](http://en.wikipedia.org/wiki/Decimal_degrees#Accuracy). As an example: at the equator, latitude/longitude values with 4 decimal places give about 11 metres precision, whereas 5 decimal places gives roughly 1 metre precision.

Notes on MongoDB
----------------

### The Near Method

Mongo document classes (Mongoid and MongoMapper) have a built-in `near` scope, but since it only works two-dimensions Geocoder overrides it with its own spherical `near` method in geocoded classes.

### Latitude/Longitude Order

Coordinates are generally printed and spoken as latitude, then longitude ([lat,lon]). Geocoder respects this convention and always expects method arguments to be given in [lat,lon] order. However, MongoDB requires that coordinates be stored in [lon,lat] order as per the GeoJSON spec (http://geojson.org/geojson-spec.html#positions), so internally they are stored "backwards." However, this does not affect order of arguments to methods when using Mongoid or MongoMapper.

To access an object's coordinates in the conventional order, use the `to_coordinates` instance method provided by Geocoder. For example:

    obj.to_coordinates  # => [37.7941013, -122.3951096] # [lat, lon]

Calling `obj.coordinates` directly returns the internal representation of the coordinates which, in the case of MongoDB, is probably the reverse of what you want:

    obj.coordinates     # => [-122.3951096, 37.7941013] # [lon, lat]

For consistency with the rest of Geocoder, always use the `to_coordinates` method instead.

Notes on Non-Rails Frameworks
-----------------------------

If you are using Geocoder with ActiveRecord and a framework other than Rails (like Sinatra or Padrino) you will need to add this in your model before calling Geocoder methods:

    extend Geocoder::Model::ActiveRecord

Optimisation of Distance Queries
--------------------------------

In MySQL and Postgres the finding of objects near a given point is speeded up by using a bounding box to limit the number of points over which a full distance calculation needs to be done.

To take advantage of this optimisation you need to add a composite index on latitude and longitude. In your Rails migration:

    add_index :table, [:latitude, :longitude]


Distance Queries in SQLite
--------------------------

SQLite's lack of trigonometric functions requires an alternate implementation of the `near` scope. When using SQLite, Geocoder will automatically use a less accurate algorithm for finding objects near a given point. Results of this algorithm should not be trusted too much as it will return objects that are outside the given radius, along with inaccurate distance and bearing calculations.


### Discussion

There are few options for finding objects near a given point in SQLite without installing extensions:

1. Use a square instead of a circle for finding nearby points. For example, if you want to find points near 40.71, 100.23, search for objects with latitude between 39.71 and 41.71 and longitude between 99.23 and 101.23. One degree of latitude or longitude is at most 69 miles so divide your radius (in miles) by 69.0 to get the amount to add and subtract from your center coordinates to get the upper and lower bounds. The results will not be very accurate (you'll get points outside the desired radius), but you will get all the points within the required radius.

2. Load all objects into memory and compute distances between them using the `Geocoder::Calculations.distance_between` method. This will produce accurate results but will be very slow (and use a lot of memory) if you have a lot of objects in your database.

3. If you have a large number of objects (so you can't use approach #2) and you need accurate results (better than approach #1 will give), you can use a combination of the two. Get all the objects within a square around your center point, and then eliminate the ones that are too far away using `Geocoder::Calculations.distance_between`.

Because Geocoder needs to provide this functionality as a scope, we must go with option #1, but feel free to implement #2 or #3 if you need more accuracy.


Tests
-----

Geocoder comes with a test suite (just run `rake test`) that mocks ActiveRecord and is focused on testing the aspects of Geocoder that do not involve executing database queries. Geocoder uses many database engine-specific queries which must be tested against all supported databases (SQLite, MySQL, etc). Ideally this involves creating a full, working Rails application, and that seems beyond the scope of the included test suite. As such, I have created a separate repository which includes a full-blown Rails application and some utilities for easily running tests against multiple environments:

http://github.com/alexreisner/geocoder_test


Error Handling
--------------

By default Geocoder will rescue any exceptions raised by calls to a geocoding service and return an empty array. You can override this on a per-exception basis, and also have Geocoder raise its own exceptions for certain events (eg: API quota exceeded) by using the `:always_raise` option:

    Geocoder.configure(:always_raise => [SocketError, TimeoutError])

You can also do this to raise all exceptions:

    Geocoder.configure(:always_raise => :all)

The raise-able exceptions are:

    SocketError
    TimeoutError
    Geocoder::OverQueryLimitError
    Geocoder::RequestDenied
    Geocoder::InvalidRequest
    Geocoder::InvalidApiKey
    Geocoder::ServiceUnavailable

Note that only a few of the above exceptions are raised by any given lookup, so there's no guarantee if you configure Geocoder to raise `ServiceUnavailable` that it will actually be raised under those conditions (because most APIs don't return 503 when they should; you may get a `TimeoutError` instead). Please see the source code for your particular lookup for details.


Troubleshooting
---------------

### Mongoid

If you get one of these errors:

    uninitialized constant Geocoder::Model::Mongoid
    uninitialized constant Geocoder::Model::Mongoid::Mongo

you should check your Gemfile to make sure the Mongoid gem is listed _before_ Geocoder. If Mongoid isn't loaded when Geocoder is initialized, Geocoder will not load support for Mongoid.

### ActiveRecord

A lot of debugging time can be saved by understanding how Geocoder works with ActiveRecord. When you use the `near` scope or the `nearbys` method of a geocoded object, Geocoder creates an ActiveModel::Relation object which adds some attributes (eg: distance, bearing) to the SELECT clause. It also adds a condition to the WHERE clause to check that distance is within the given radius. Because the SELECT clause is modified, anything else that modifies the SELECT clause may produce strange results, for example:

* using the `pluck` method (selects only a single column)
* specifying another model through `includes` (selects columns from other tables)

### Unexpected Responses from Geocoding Services

Take a look at the server's raw response. You can do this by getting the request URL in an app console:

    Geocoder::Lookup.get(:google).query_url(Geocoder::Query.new("..."))

Replace `:google` with the lookup you are using and replace `...` with the address you are trying to geocode. Then visit the returned URL in your web browser. Often the API will return an error message that helps you resolve the problem. If, after reading the raw response, you believe there is a problem with Geocoder, please post an issue and include both the URL and raw response body.

You can also fetch the response in the console:

    Geocoder::Lookup.get(:google).send(:fetch_raw_data, Geocoder::Query.new("..."))


Reporting Issues
----------------

When reporting an issue, please list the version of Geocoder you are using and any relevant information about your application (Rails version, database type and version, etc). Also avoid vague language like "it doesn't work." Please describe as specifically as you can what behavior your are actually seeing (eg: an error message? a nil return value?).

Please DO NOT use GitHub issues to ask questions about how to use Geocoder. Sites like [StackOverflow](http://www.stackoverflow.com/) are a better forum for such discussions.


### Known Issue

You cannot use the `near` scope with another scope that provides an `includes` option because the `SELECT` clause generated by `near` will overwrite it (or vice versa).

Instead of using `includes` to reduce the number of database queries, try using `joins` with either the `:select` option or a call to `preload`. For example:

    # Pass a :select option to the near scope to get the columns you want.
    # Instead of City.near(...).includes(:venues), try:
    City.near("Omaha, NE", 20, :select => "cities.*, venues.*").joins(:venues)

    # This preload call will normally trigger two queries regardless of the
    # number of results; one query on hotels, and one query on administrators.
    # Instead of Hotel.near(...).includes(:administrator), try:
    Hotel.near("London, UK", 50).joins(:administrator).preload(:administrator)

If anyone has a more elegant solution to this problem I am very interested in seeing it.


Contributing
------------

Contributions are welcome via pull requests on Github. Please respect the following guidelines:

* Each pull request should implement ONE feature or bugfix. If you want to add or fix more than one thing, submit more than one pull request.
* Do not commit changes to files that are irrelevant to your feature or bugfix (eg: `.gitignore`).
* Do not add dependencies on other gems.
* Do not add unnecessary `require` statements which could cause LoadErrors on certain systems.
* Remember: Geocoder needs to run outside of Rails. Don't assume things like ActiveSupport are available.
* Be willing to accept criticism and work on improving your code; Geocoder is used by thousands of developers and care must be taken not to introduce bugs.
* Be aware that the pull request review process is not immediate, and is generally proportional to the size of the pull request.


Copyright (c) 2009-15 Alex Reisner, released under the MIT license
# Sprockets Rails

Provides Sprockets implementation for Rails 4.x (and beyond) Asset Pipeline.


## Installation

``` ruby
gem 'sprockets-rails', :require => 'sprockets/railtie'
```

Or alternatively `require 'sprockets/railtie'` in your `config/application.rb` if you have Bundler auto-require disabled.


## Usage


### Rake task

**`rake assets:precompile`**

Deployment task that compiles any assets listed in `config.assets.precompile` to `public/assets`.

**`rake assets:clean`**

Only removes old assets (keeps the most recent 3 copies) from `public/assets`. Useful when doing rolling deploys that may still be serving old assets while the new ones are being compiled.

**`rake assets:clobber`**

Nuke `public/assets` and clear the Sprockets file system cache.

#### Customize

If the basic tasks don't do all that you need, it's straight forward to redefine them and replace them with something more specific to your app.

You can also redefine the task with the built in task generator.

``` ruby
require 'sprockets/rails/task'
# clean the old tasks
Rake::Task["assets:environment"].clear
Rake::Task["assets:precompile"].clear
Rake::Task["assets:clean"].clear
Rake::Task["assets:clobber"].clear
Sprockets::Rails::Task.new(Rails.application) do |t|
  t.environment = lambda { Rails.application.assets }
  t.assets = %w( application.js application.css )
  t.keep = 5
end
```

Each asset task will invoke `assets:environment` first. By default this loads the Rails environment. You can override this task to add or remove dependencies for your specific compilation environment.

Also see [Sprockets::Rails::Task](https://github.com/rails/sprockets-rails/blob/master/lib/sprockets/rails/task.rb) and [Rake::SprocketsTask](https://github.com/sstephenson/sprockets/blob/master/lib/rake/sprocketstask.rb).


### Initializer options

**`config.assets.precompile`**

Add additional assets to compile on deploy. Defaults to `application.js`, `application.css` and any other non-js/css file under `app/assets`.

**`config.assets.raise_runtime_errors`**

Set to `true` to enable additional runtime error checking. Recommended in the `development` environment to minimize unexpected behavior when deploying to `production`.

**`config.assets.paths`**

Add additional load paths to this Array. Rails includes `app/assets`, `lib/assets` and `vendor/assets` for you already. Plugins might want to add their custom paths to this.


**`config.assets.version`**

Set a custom cache buster string. Changing it will cause all assets to recompile on the next build.

``` ruby
config.assets.version = 'v1'
# after installing a new plugin, change loads paths
config.assets.version = 'v2'
```

**`config.assets.prefix`**

Defaults to `/assets`. Changes the directory to compile assets to.

**`config.assets.manifest`**

Defines the full path to be used for the asset precompiler's manifest file. Defaults to a randomly-generated filename in the `config.assets.prefix` directory within the public folder.

**`config.assets.digest`**

Link to undigest asset filenames. This option will eventually go away. Unless when `compile` is disabled.

**`config.assets.debug`**

Enable expanded asset debugging mode. Individual files will be served to make referencing filenames in the web console easier. This feature will eventually be deprecated and replaced by Source Maps in Sprockets 3.x.

**`config.assets.compile`**

Enables Sprockets compile environment. If disabled, `Rails.application.assets` will be unavailable to any ActionView helpers. View helpers will depend on assets being precompiled to `public/assets` in order to link to them. You can still access the environment by directly calling `Rails.application.assets`.

**`config.assets.configure`**

Invokes block with environment when the environment is initialized. Allows direct access to the environment instance and lets you lazily load libraries only needed for asset compiling.

``` ruby
config.assets.configure do |env|
  env.js_compressor  = :uglify # or :closure, :yui
  env.css_compressor = :sass   # or :yui

  require 'my_processor'
  env.register_preprocessor 'application/javascript', MyProcessor

  env.logger = Rails.logger

  env.cache = ActiveSupport::Cache::FileStore.new("tmp/cache/assets")
end
```


## Complementary plugins

The following plugins provide some extras for the Sprockets Asset Pipeline.

* [coffee-rails](https://github.com/rails/coffee-rails)
* [sass-rails](https://github.com/rails/sass-rails)

**NOTE** That these plugins are optional. The core coffee-script, sass, less, uglify, (any many more) features are built into Sprockets itself. Many of these plugins only provide generators and extra helpers. You can probably get by without them.


## Changes from Rails 3.x

* Only compiles digest filenames. Static non-digest assets should simply live in public/.
* Unmanaged asset paths and urls fallback to linking to public/. This should make it easier to work with both compiled assets and simple static assets. As a side effect, there will never be any "asset not precompiled errors" when linking to missing assets. They will just link to a public file which may or may not exist.
* JS and CSS compressors must be explicitly set. Magic detection has been removed to avoid loading compressors in environments where you want to avoid loading any of the asset libraries. Assign `config.assets.js_compressor = :uglify` or `config.assets.css_compressor = :sass` for the standard compressors.
* The manifest file is now in a JSON format. Since it lives in public/ by default, the initial filename is also randomized to obfuscate public access to the resource.
* `config.assets.manifest` (if used) must now include the manifest filename, e.g. `Rails.root.join('config/manifest.json')`. It cannot be a directory.
* Two cleanup tasks. `rake assets:clean` is now a safe cleanup that only removes older assets that are no longer used. While `rake assets:clobber` nukes the entire `public/assets` directory and clears your filesystem cache. The clean task allows for rolling deploys that may still be linking to an old asset while the new assets are being built.


## Contributing

Usual bundler workflow.

``` shell
$ git clone https://github.com/rails/sprockets-rails.git
$ cd sprockets-rails/
$ bundle install
$ bundle exec rake test
```

[![Build Status](https://secure.travis-ci.org/rails/sprockets-rails.png)](http://travis-ci.org/rails/sprockets-rails)


## Releases

sprockets-rails 2.x will primarily target sprockets 2.x with future compatibility for 3.x. Consider upgrading to sprockets-rails 3.x to take full advantage of 3.x features.

The minor and patch version will be updated according to [semver](http://semver.org/).

* Any new APIs or config options that don't break compatibility will be in a minor release
* Any time the sprockets dependency is bumped, there will be a new minor release
* Simple bug fixes will be patch releases


## License

Copyright &copy; 2014 Joshua Peek.

Released under the MIT license. See `LICENSE` for details.
# Rails::Deprecated::Sanitizer

In Rails 4.2 HTML sanitization has been rewritten using a more secure library.

This gem includes the old behavior shipping with Rails 4.2 and before. It is
strictly provided to ease migration. It will be supported until Rails 5.

To downgrade add `gem 'rails-deprecated_sanitizer'` to your Gemfile.

See the Rails 4.2 upgrade guide for more information.

You can read more about the new sanitization implementation here: [rails-html-sanitizer](https://github.com/rails/rails-html-sanitizer).

# Reporting XSS Security Issues

The code provided here deals with XSS attacks and is therefore a security concern.
So if you find a security issue please follow the [regular security reporting guidelines](http://rubyonrails.org/security/).
# Puma: A Ruby Web Server Built For Concurrency

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/puma/puma?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) [![Build Status](https://secure.travis-ci.org/puma/puma.png)](http://travis-ci.org/puma/puma) [![Dependency Status](https://gemnasium.com/puma/puma.png)](https://gemnasium.com/puma/puma) <a href="https://codeclimate.com/github/puma/puma"><img src="https://codeclimate.com/github/puma/puma.png" /></a>

## Description

Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for Ruby/Rack applications. Puma is intended for use in both development and production environments. In order to get the best throughput, it is highly recommended that you use a  Ruby implementation with real threads like Rubinius or JRuby.

## Built For Speed &amp; Concurrency

Puma is a simple, fast, and highly concurrent HTTP 1.1 server for Ruby web applications. It can be used with any application that supports Rack, and is considered the replacement for Webrick and Mongrel. It was designed to be the go-to server for [Rubinius](http://rubini.us), but also works well with JRuby and MRI. Puma is intended for use in both development and production environments.

Under the hood, Puma processes requests using a C-optimized Ragel extension (inherited from Mongrel) that provides fast, accurate HTTP 1.1 protocol parsing in a portable way. Puma then serves the request in a thread from an internal thread pool (which you can control). This allows Puma to provide real concurrency for your web application!

With Rubinius 2.0, Puma will utilize all cores on your CPU with real threads, meaning you won't have to spawn multiple processes to increase throughput. You can expect to see a similar benefit from JRuby.

On MRI, there is a Global Interpreter Lock (GIL) that ensures only one thread can be run at a time. But if you're doing a lot of blocking IO (such as HTTP calls to external APIs like Twitter), Puma still improves MRI's throughput by allowing blocking IO to be run concurrently (EventMachine-based servers such as Thin turn off this ability, requiring you to use special libraries). Your mileage may vary. In order to get the best throughput, it is highly recommended that you use a Ruby implementation with real threads like [Rubinius](http://rubini.us) or [JRuby](http://jruby.org).

## Quick Start

The easiest way to get started with Puma is to install it via RubyGems. You can do this easily:

    $ gem install puma

Now you should have the `puma` command available in your PATH, so just do the following in the root folder of your Rack application:

    $ puma app.ru

## Advanced Setup

### Sinatra

You can run your Sinatra application with Puma from the command line like this:

    $ ruby app.rb -s Puma

Or you can configure your application to always use Puma:

    require 'sinatra'
    configure { set :server, :puma }

If you use Bundler, make sure you add Puma to your Gemfile (see below).

### Rails

First, make sure Puma is in your Gemfile:

    gem 'puma'

Then start your server with the `rails` command:

    $ rails s Puma

### Rackup

You can pass it as an option to `rackup`:

    $ rackup -s Puma

Alternatively, you can modify your `config.ru` to choose Puma by default, by adding the following as the first line:

    #\ -s puma

## Configuration

Puma provides numerous options for controlling the operation of the server. Consult `puma -h` (or `puma --help`) for a full list.

### Thread Pool

Puma utilizes a dynamic thread pool which you can modify. You can set the minimum and maximum number of threads that are available in the pool with the `-t` (or `--threads`) flag:

    $ puma -t 8:32

Puma will automatically scale the number of threads based on how much traffic is present. The current default is `0:16`. Feel free to experiment, but be careful not to set the number of maximum threads to a very large number, as you may exhaust resources on the system (or hit resource limits).

### Clustered mode

Puma 2 offers clustered mode, allowing you to use forked processes to handle multiple incoming requests concurrently, in addition to threads already provided. You can tune the number of workers with the `-w` (or `--workers`) flag:

    $ puma -t 8:32 -w 3

On a ruby implementation that offers native threads, you should tune this number to match the number of cores available.
Note that threads are still used in clustered mode, and the `-t` thread flag setting is per worker, so `-w 2 -t 16:16` will be 32 threads.

If you're running in Clustered Mode you can optionally choose to preload your application before starting up the workers. This is necessary in order to take advantage of the [Copy on Write](http://en.wikipedia.org/wiki/Copy-on-write) feature introduced in [MRI Ruby 2.0](https://blog.heroku.com/archives/2013/3/6/matz_highlights_ruby_2_0_at_waza). To do this simply specify the `--preload` flag in invocation:

    # CLI invocation
    $ puma -t 8:32 -w 3 --preload

If you're using a configuration file, use the `preload_app!` method, and be sure to specify your config file's location with the `-C` flag:

    $ puma -C config/puma.rb

    # config/puma.rb
    threads 8,32
    workers 3
    preload_app!

Additionally, you can specify a block in your configuration file that will be run on boot of each worker:

    # config/puma.rb
    on_worker_boot do
      # configuration here
    end

This code can be used to setup the process before booting the application, allowing
you to do some Puma-specific things that you don't want to embed in your application.
For instance, you could fire a log notification that a worker booted or send something to statsd.
This can be called multiple times to add hooks.

If you're preloading your application and using ActiveRecord, it's recommend you setup your connection pool here:

    # config/puma.rb
    on_worker_boot do
      ActiveSupport.on_load(:active_record) do
        ActiveRecord::Base.establish_connection
      end
    end

When you use preload_app, your new code goes all in the master process, and is then copied in the workers (meaning it’s only compatible with cluster mode). General rule is to use preload_app when your workers die often and need fast starts. If you don’t have many workers, you probably should not use preload_app.

Note that preload_app can’t be used with phased restart, since phased restart kills and restarts workers one-by-one, and preload_app is all about copying the code of master into the workers.

### Binding TCP / Sockets

In contrast to many other server configs which require multiple flags, Puma simply uses one URI parameter with the `-b` (or `--bind`) flag:

    $ puma -b tcp://127.0.0.1:9292

Want to use UNIX Sockets instead of TCP (which can provide a 5-10% performance boost)? No problem!

    $ puma -b unix:///var/run/puma.sock

If you need to change the permissions of the UNIX socket, just add a umask parameter:

    $ puma -b 'unix:///var/run/puma.sock?umask=0111'

Need a bit of security? Use SSL sockets!

    $ puma -b 'ssl://127.0.0.1:9292?key=path_to_key&cert=path_to_cert'

### Control/Status Server

Puma comes with a builtin status/control app that can be used query and control Puma itself. Here is an example of starting Puma with the control server:

    $ puma --control tcp://127.0.0.1:9293 --control-token foo

This directs Puma to start the control server on localhost port 9293. Additionally, all requests to the control server will need to include `token=foo` as a query parameter. This allows for simple authentication. Check out [status.rb](https://github.com/puma/puma/blob/master/lib/puma/app/status.rb) to see what the app has available.

### Configuration file

You can also provide a configuration file which Puma will use with the `-C` (or `--config`) flag:

    $ puma -C /path/to/config

By default, if no configuration file is specifed, Puma will look for a configuration file at config/puma.rb. If an environment is specified, either via the `-e` and `--environment` flags, or through the `RACK_ENV` environment variable, the default file location will be config/puma/environment_name.rb.

If you want to prevent Puma from looking for a configuration file in those locations, provide a dash as the argument to the `-C` (or `--config`) flag:

    $ puma -C "-"

Take the following [sample configuration](https://github.com/puma/puma/blob/master/examples/config.rb) as inspiration or check out [configuration.rb](https://github.com/puma/puma/blob/master/lib/puma/configuration.rb) to see all available options.

## Restart

Puma includes the ability to restart itself allowing easy upgrades to new versions. When available (MRI, Rubinius, JRuby), Puma performs a "hot restart". This is the same functionality available in *unicorn* and *nginx* which keep the server sockets open between restarts. This makes sure that no pending requests are dropped while the restart is taking place.

To perform a restart, there are 2 builtin mechanisms:

  * Send the `puma` process the `SIGUSR2` signal
  * Use the status server and issue `/restart`

No code is shared between the current and restarted process, so it should be safe to issue a restart any place where you would manually stop Puma and start it again.

If the new process is unable to load, it will simply exit. You should therefore run Puma under a supervisor when using it in production.

### Normal vs Hot vs Phased Restart

A hot restart means that no requests while deploying your new code will be lost, since the server socket is kept open between restarts.

But beware, hot restart does not mean that the incoming requests won’t hang for multiple seconds while your new code has not fully deployed. If you need a zero downtime and zero hanging requests deploy, you must use phased restart.

When you run pumactl phased-restart, Puma kills workers one-by-one, meaning that at least another worker is still available to serve requests, which lead in zero hanging request (yay!).

But again beware, upgrading an application sometimes involves upgrading the database schema. With phased restart, there may be a moment during the deployment where processes belonging to the previous version and processes belonging to the new version both exist at the same time. Any database schema upgrades you perform must therefore be backwards-compatible with the old application version.

if you perform a lot of database migrations, you probably should not use phased restart and use a normal/hot restart instead (pumactl restart). That way, no code is shared while deploying (in that case, preload_app might help for quicker deployment, see below).


### Cleanup Code

Puma isn't able to understand all the resources that your app may use, so it provides a hook in the configuration file you pass to `-C` called `on_restart`. The block passed to `on_restart` will be called, unsurprisingly, just before Puma restarts itself.

You should place code to close global log files, redis connections, etc in this block so that their file descriptors don't leak into the restarted process. Failure to do so will result in slowly running out of descriptors and eventually obscure crashes as the server is restart many times.

### Platform Constraints

Because of various platforms not being implement certain things, the following differences occur when Puma is used on different platforms:

  * **JRuby**, **Windows**: server sockets are not seamless on restart, they must be closed and reopened. These platforms have no way to pass descriptors into a new process that is exposed to ruby
  * **JRuby**, **Windows**: cluster mode is not supported due to a lack of  fork(2)
  * **Windows**: daemon mode is not supported due to a lack of fork(2)

## pumactl

`pumactl` is a simple CLI frontend to the control/status app described above.  Please refer to `pumactl --help` for available commands.

## Managing multiple Pumas / init.d / upstart scripts

If you want an easy way to manage multiple scripts at once check [tools/jungle](https://github.com/puma/puma/tree/master/tools/jungle) for init.d and upstart scripts.

## Capistrano deployment

Puma has support for Capistrano3 with an [external gem](https://github.com/seuros/capistrano-puma), you just need require that in Gemfile:

```ruby
gem 'capistrano3-puma'
```
And then execute:

```bash
bundle
```

Then add to Capfile

```ruby
require 'capistrano/puma'
```

and then

```bash
$ bundle exec cap puma:start
$ bundle exec cap puma:restart
$ bundle exec cap puma:stop
$ bundle exec cap puma:phased_restart
```

## Contributing

To run the test suite:

```bash
$ bundle install
$ bundle exec rake
```

## License

Puma is copyright 2014 Evan Phoenix and contributors. It is licensed under the BSD 3-Clause license. See the include LICENSE file for details.
# Puma as a service

## Init.d

See `/tools/jungle/init.d` for tools to use with init.d and start-stop-daemon.

## Upstart

See `/tools/jungle/upstart` for Ubuntu's upstart scripts.
# Puma as a service using Upstart

Manage multiple Puma servers as services on the same box using Ubuntu upstart.

## Installation 

    # Copy the scripts to services directory 
    sudo cp puma.conf puma-manager.conf /etc/init
    
    # Create an empty configuration file
    sudo touch /etc/puma.conf

## Managing the jungle 

Puma apps are referenced in /etc/puma.conf by default. Add each app's path as a new line, e.g.:

```
/home/apps/my-cool-ruby-app
/home/apps/another-app/current
```

Start the jungle running:

`sudo start puma-manager`

This script will run at boot time.

Start a single puma like this:

`sudo start puma app=/path/to/app`

## Logs

Everything is logged by upstart, defaulting to `/var/log/upstart`.

Each puma instance is named after its directory, so for an app called `/home/apps/my-app` the log file would be `/var/log/upstart/puma-_home_apps_my-app.log`.

## Conventions 

* The script expects:
  * a config file to exist under `config/puma.rb` in your app. E.g.: `/home/apps/my-app/config/puma.rb`.
  * a temporary folder to put the PID, socket and state files to exist called `tmp/puma`. E.g.: `/home/apps/my-app/tmp/puma`. Puma will take care of the files for you.

You can always change those defaults by editing the scripts.

## Here's what a minimal app's config file should have

```
pidfile "/path/to/app/tmp/puma/pid"
state_path "/path/to/app/tmp/puma/state"
activate_control_app
```

## Before starting...

You need to customise `puma.conf` to:

* Set the right user your app should be running on unless you want root to execute it!
  * Look for `setuid apps` and `setgid apps`, uncomment those lines and replace `apps` to whatever your deployment user is.
  * Replace `apps` on the paths (or set the right paths to your user's home) everywhere else.
* Uncomment the source lines for `rbenv` or `rvm` support unless you use a system wide installation of Ruby.
# Puma daemon service

Init script to manage multiple Puma servers on the same box using start-stop-daemon.

## Installation 

    # Copy the init script to services directory 
    sudo cp puma /etc/init.d
    sudo chmod +x /etc/init.d/puma
    
    # Make it start at boot time. 
    sudo update-rc.d -f puma defaults

    # Copy the Puma runner to an accessible location
    sudo cp run-puma /usr/local/bin
    sudo chmod +x /usr/local/bin/run-puma

    # Create an empty configuration file
    sudo touch /etc/puma.conf

## Managing the jungle 

Puma apps are held in /etc/puma.conf by default. It's mainly a CSV file and every line represents one app. Here's the syntax:

    app-path,user,config-file-path,log-file-path

You can add an instance by editing the file or running the following command:

    sudo /etc/init.d/puma add /path/to/app user /path/to/app/config/puma.rb /path/to/app/log/puma.log

The config and log paths are optional parameters and default to:

* config: /path/to/app/*config/puma.rb*
* log: /path/to/app/*log/puma.log*

To remove an app, simply delete the line from the config file or run:

    sudo /etc/init.d/puma remove /path/to/app

The command will make sure the Puma instance stops before removing it from the jungle.

## Assumptions 

* The script expects a temporary folder named /path/to/app/*tmp/puma* to exist. Create it if it's not there by default.
The pid and state files should live there and must be called: *tmp/puma/pid* and *tmp/puma/state*.
You can change those if you want but you'll have to adapt the script for it to work.

* Here's what a minimal app's config file should have:

```
pidfile "/path/to/app/tmp/puma/pid"
state_path "/path/to/app/tmp/puma/state"
activate_control_app
```
# HTTP::Cookie

HTTP::Cookie is a ruby library to handle HTTP cookies in a way both
compliant with RFCs and compatible with today's major browsers.

It was originally a part of the
[Mechanize](https://github.com/sparklemotion/mechanize) library,
separated as an independent library in the hope of serving as a common
component that is reusable from any HTTP related piece of software.

The following is an incomplete list of its features:

* Its behavior is highly compatible with that of today's major web
  browsers.

* It is based on and conforms to RFC 6265 (the latest standard for the
  HTTP cookie mechanism) to a high extent, with real world conventions
  deeply in mind.

* It takes eTLD (effective TLD, also known as "Public Suffix") into
  account just as major browsers do, to reject cookies with an eTLD
  domain like "org", "co.jp", or "appspot.com".  This feature is
  brought to you by the domain_name gem.

* The number of cookies and the size are properly capped so that a
  cookie store does not get flooded.

* It supports the legacy Netscape cookies.txt format for
  serialization, maximizing the interoperability with other
  implementations.

* It supports the cookies.sqlite format adopted by Mozilla Firefox for
  backend store database which can be shared among multiple program
  instances.

* It is relatively easy to add a new serialization format or a backend
  store because of its modular API.

## Installation

Add this line to your application's `Gemfile`:

    gem 'http-cookie'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install http-cookie

## Usage

    ########################
    # Client side example 1
    ########################

    # Initialize a cookie jar
    jar = HTTP::CookieJar.new

    # Load from a file
    jar.load(filename) if File.exist?(filename)

    # Store received cookies, where uri is the origin of this header
    header["Set-Cookie"].each { |value|
      jar.parse(value, uri)
    }

    # ...

    # Set the Cookie header value, where uri is the destination URI
    header["Cookie"] = HTTP::Cookie.cookie_value(jar.cookies(uri))

    # Save to a file
    jar.save(filename)


    ########################
    # Client side example 2
    ########################

    # Initialize a cookie jar using a Mozilla compatible SQLite3 backend
    jar = HTTP::CookieJar.new(store: :mozilla, filename: 'cookies.sqlite')

    # There is no need for load & save in this backend.

    # Store received cookies, where uri is the origin of this header
    header["Set-Cookie"].each { |value|
      jar.parse(value, uri)
    }

    # ...

    # Set the Cookie header value, where uri is the destination URI
    header["Cookie"] = HTTP::Cookie.cookie_value(jar.cookies(uri))


    ########################
    # Server side example
    ########################

    # Generate a domain cookie
    cookie1 = HTTP::Cookie.new("uid", "u12345", domain: 'example.org',
                                                for_domain: true,
                                                path: '/',
                                                max_age: 7*86400)

    # Add it to the Set-Cookie response header
    header['Set-Cookie'] = cookie1.set_cookie_value

    # Generate a host-only cookie
    cookie2 = HTTP::Cookie.new("aid", "a12345", origin: my_url,
                                                path: '/',
                                                max_age: 7*86400)

    # Add it to the Set-Cookie response header
    header['Set-Cookie'] = cookie2.set_cookie_value


## Incompatibilities with Mechanize::Cookie/CookieJar

There are several incompatibilities between
Mechanize::Cookie/CookieJar and HTTP::Cookie/CookieJar.  Below
is how to rewrite existing code written for Mechanize::Cookie with
equivalent using HTTP::Cookie:

- Mechanize::Cookie.parse

    The parameter order changed in HTTP::Cookie.parse.

        # before
        cookies1 = Mechanize::Cookie.parse(uri, set_cookie1)
        cookies2 = Mechanize::Cookie.parse(uri, set_cookie2, log)

        # after
        cookies1 = HTTP::Cookie.parse(set_cookie1, uri_or_url)
        cookies2 = HTTP::Cookie.parse(set_cookie2, uri_or_url, logger: log)
        # or you can directly store parsed cookies in your jar
        jar.parse(set_cookie1, uri_or_url)
        jar.parse(set_cookie1, uri_or_url, logger: log)

- Mechanize::Cookie#version, #version=

    There is no longer a sense of version in the HTTP cookie
    specification.  The only version number ever defined was zero, and
    there will be no other version defined since the version attribute
    has been removed in RFC 6265.

- Mechanize::Cookie#comment, #comment=

    Ditto.  The comment attribute has been removed in RFC 6265.

- Mechanize::Cookie#set_domain

    This method was unintentionally made public.  Simply use
    HTTP::Cookie#domain=.

        # before
        cookie.set_domain(domain)

        # after
        cookie.domain = domain

- Mechanize::CookieJar#add, #add!

    Always use HTTP::CookieJar#add.

        # before
        jar.add!(cookie1)
        jar.add(uri, cookie2)

        # after
        jar.add(cookie1)
        cookie2.origin = uri; jar.add(cookie2)  # or specify origin in parse() or new()

- Mechanize::CookieJar#clear!

    Use HTTP::Cookiejar#clear.

        # before
        jar.clear!

        # after
        jar.clear

- Mechanize::CookieJar#save_as

    Use HTTP::CookieJar#save.

        # before
        jar.save_as(file)

        # after
        jar.save(file)

- Mechanize::CookieJar#jar

    There is no direct access to the internal hash in HTTP::CookieJar
    since it has introduced an abstract store layer.  If you want to
    tweak the internals of the hash store, try creating a new store
    class referring to the default store class
    HTTP::CookieJar::HashStore.

    If you desperately need it you can access it by
    `jar.store.instance_variable_get(:@jar)`, but there is no
    guarantee that it will remain available in the future.


HTTP::Cookie/CookieJar raise runtime errors to help migration, so
after replacing the class names, try running your test code once to
find out how to fix your code base.

### File formats

The YAML serialization format has changed, and HTTP::CookieJar#load
cannot import what is written in a YAML file saved by
Mechanize::CookieJar#save_as.  HTTP::CookieJar#load will not raise an
exception if an incompatible YAML file is given, but the content is
silently ignored.

Note that there is (obviously) no forward compatibillity with this.
Trying to load a YAML file saved by HTTP::CookieJar with
Mechanize::CookieJar will fail in runtime error.

On the other hand, there has been (and will ever be) no change in the
cookies.txt format, so use it instead if compatibility is significant.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
BSON [![Build Status](https://secure.travis-ci.org/mongodb/bson-ruby.png?branch=master&.png)](http://travis-ci.org/mongodb/bson-ruby)  [![Code Climate](https://codeclimate.com/github/mongodb/bson-ruby.png)](https://codeclimate.com/github/mongodb/bson-ruby) [![Coverage Status](https://coveralls.io/repos/mongodb/bson-ruby/badge.png?branch=master)](https://coveralls.io/r/mongodb/bson-ruby?branch=master) [![Inline docs](http://inch-ci.org/github/mongodb/bson-ruby.svg?branch=master)](http://inch-ci.org/github/mongodb/bson-ruby)
====

An implementation of the BSON specification in Ruby.

Compatibility
-------------

BSON is tested against MRI (1.9.2+), JRuby (1.7.0+) and Rubinius (2.0.0+).

Documentation
-------------

Current documentation can be found [here](http://docs.mongodb.org/ecosystem/tutorial/ruby-bson-tutorial/#ruby-bson-tutorial)

API Documentation
-----------------

The [API Documentation](http://rdoc.info/github/mongodb/bson-ruby/master/frames) is
located at rdoc.info.

BSON Specification
------------------

The [BSON specification](http://bsonspec.org) is at bsonspec.org.

Versioning
----------

As of 2.0.0, this project adheres to the [Semantic Versioning Specification](http://semver.org/).

License
-------

Copyright (C) 2009-2014 MongoDB Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# Haml

[![Build Status](https://secure.travis-ci.org/haml/haml.png?branch=master)](http://travis-ci.org/haml/haml)

Haml is a templating engine for HTML. It's designed to make it both easier and
more pleasant to write HTML documents, by eliminating redundancy, reflecting the
underlying structure that the document represents, and providing an elegant syntax
that's both powerful and easy to understand.

## Basic Usage

Haml can be used from the command line or as part of a Ruby web framework. The
first step is to install the gem:

    gem install haml

After you write some Haml, you can run

    haml document.haml

to compile it to HTML. For more information on these commands, check out

    haml --help

To use Haml programatically, check out the [YARD
documentation](http://haml.info/docs/yardoc/).

## Using Haml with Rails

To use Haml with Rails, simply add Haml to your Gemfile and run `bundle`.

If you'd like to replace Rails's Erb-based generators with Haml, add
[haml-rails](https://github.com/indirect/haml-rails) to your Gemfile as well.

## Formatting

The most basic element of Haml is a shorthand for creating HTML:

    %tagname{:attr1 => 'value1', :attr2 => 'value2'} Contents

No end-tag is needed; Haml handles that automatically. If you prefer HTML-style
attributes, you can also use:

    %tagname(attr1='value1' attr2='value2') Contents

Adding `class` and `id` attributes is even easier. Haml uses the same syntax as
the CSS that styles the document:

    %tagname#id.class

In fact, when you're using the `<div>` tag, it becomes _even easier_. Because
`<div>` is such a common element, a tag without a name defaults to a div. So

    #foo Hello!

becomes

    <div id='foo'>Hello!</div>

Haml uses indentation to bring the individual elements to represent the HTML
structure. A tag's children are indented beneath than the parent tag. Again, a
closing tag is automatically added. For example:

    %ul
      %li Salt
      %li Pepper

becomes:

    <ul>
      <li>Salt</li>
      <li>Pepper</li>
    </ul>

You can also put plain text as a child of an element:

    %p
      Hello,
      World!

It's also possible to embed Ruby code into Haml documents. An equals sign, `=`,
will output the result of the code. A hyphen, `-`, will run the code but not
output the result. You can even use control statements like `if` and `while`:

    %p
      Date/Time:
      - now = DateTime.now
      %strong= now
      - if now > DateTime.parse("December 31, 2006")
        = "Happy new " + "year!"

Haml provides far more tools than those presented here. Check out the [reference
documentation](http://haml.info/docs/yardoc/file.REFERENCE.html)
for full details.

### Indentation

Haml's indentation can be made up of one or more tabs or spaces. However,
indentation must be consistent within a given document. Hard tabs and spaces
can't be mixed, and the same number of tabs or spaces must be used throughout.

## Contributing

Contributions are welcomed, but before you get started please read the
[guidelines](http://haml.info/development.html#contributing).

After forking and then cloning the repo locally, install Bundler and then use it
to install the development gem dependecies:

    gem install bundler
    bundle install

Once this is complete, you should be able to run the test suite:

    rake

You'll get a warning that you need to install haml-spec, so run this:

    git submodule update --init

At this point `rake` should run without error or warning and you are ready to
start working on your patch!

Note that you can also run just one test out of the test suite if you're working
on a specific area:

    ruby -Itest test/helper_test.rb -n test_buffer_access

Haml supports Ruby 1.8.7 and higher, so please make sure your changes run on
both 1.9 and 1.8.

## Team

### Current Maintainers

* [Norman Clarke](http://github.com/norman)
* [Matt Wildig](http://github.com/mattwildig)
* [Akira Matsuda](https://github.com/amatsuda)

### Alumni

Haml was created by [Hampton Catlin](http://hamptoncatlin.com), the author of
the original implementation. Hampton is no longer involved in day-to-day coding,
but still consults on language issues.

[Nathan Weizenbaum](http://nex-3.com) was for many years the primary developer
and architect of the "modern" Ruby implementation of Haml.


## License

Some of Nathan's work on Haml was supported by Unspace Interactive.

Beyond that, the implementation is licensed under the MIT License.

Copyright (c) 2006-2013 Hampton Catlin, Nathan Weizenbaum and the Haml team

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# jquery-rails

jQuery! For Rails! So great.

This gem provides:

  * jQuery 1.11.1 and jQuery 2.1.1
  * the jQuery UJS adapter
  * assert_select_jquery to test jQuery responses in Ruby tests

## Versions

Starting with v2.1, the jquery-rails gem follows these version guidelines
to provide more control over your app's jQuery version from your Gemfile:

```
patch version bump = updates to jquery-ujs, jquery-rails, and patch-level updates to jQuery
minor version bump = minor-level updates to jQuery
major version bump = major-level updates to jQuery and updates to Rails which may be backwards-incompatible
```

See [VERSIONS.md](VERSIONS.md) to see which versions of jquery-rails bundle which
versions of jQuery.

## Installation

The jquery and jquery-ujs files will be added to the asset pipeline and available for you to use. If they're not already in `app/assets/javascripts/application.js` by default, add these lines:

```js
//= require jquery
//= require jquery_ujs
```

If you want to use jQuery 2, you can require `jquery2` instead:

```js
//= require jquery2
//= require jquery_ujs
```

For jQuery UI, we recommend the [jquery-ui-rails](https://github.com/joliss/jquery-ui-rails) gem, as it includes the jquery-ui css and allows easier customization.

*As of v3.0, jquery-rails no longer includes jQuery UI. Use the
jquery-ui-rails gem above.*

## Contributing

Feel free to open an issue ticket if you find something that could be improved. A couple notes:

* If it's an issue pertaining to the jquery-ujs javascript, please report it to the [jquery-ujs project](https://github.com/rails/jquery-ujs).

* If the jQuery scripts are outdated (i.e. maybe a new version of jquery was released yesterday), feel free to open an issue and prod us to get that thing updated. However, for security reasons, we won't be accepting pull requests with updated jQuery scripts.

## Acknowledgements

Many thanks are due to all of [the jquery-rails contributors](https://github.com/rails/jquery-rails/graphs/contributors). Special thanks to [JangoSteve](http://github.com/JangoSteve) for tirelessly answering questions and accepting patches, and the [Rails Core Team](https://github.com/organizations/rails/teams/617) for making jquery-rails an official part of Rails 3.1.

Copyright [André Arko](http://arko.net), released under the MIT License.
= README

release::	2.7.0
copyright::	copyright(c) 2006-2011 kuwata-lab.com all rights reserved.



== About Erubis

Erubis is an implementation of eRuby. It has the following features.
* Very fast, almost three times faster than ERB and even 10% faster than eruby
* Multi-language support (Ruby/PHP/C/Java/Scheme/Perl/Javascript)
* Auto escaping support
* Auto trimming spaces around '<% %>'
* Embedded pattern changeable (default '<% %>')
* Enable to handle Processing Instructions (PI) as embedded pattern (ex. '<?rb ... ?>')
* Context object available and easy to combine eRuby template with YAML datafile
* Print statement available
* Easy to extend and customize in subclass
* Ruby on Rails support

Erubis is implemented in pure Ruby.  It requires Ruby 1.8 or higher.
Erubis now supports Ruby 1.9.

See doc/users-guide.html for details.



== Installation

* If you have installed RubyGems, just type <tt>gem install erubis</tt>.

    $ sudo gem install erubis

* Else install abstract[http://rubyforge.org/projects/abstract/] at first,
  and download erubis_X.X.X.tar.bz2 and install it by setup.rb.

    $ tar xjf abstract_X.X.X.tar.bz2
    $ cd abstract_X.X.X/
    $ sudo ruby setup.rb
    $ cd ..
    $ tar xjf erubis_X.X.X.tar.bz2
    $ cd erubis_X.X.X/
    $ sudo ruby setup.rb

* (Optional) It is able to merge 'lib/**/*.rb' into 'bin/erubis' by
  'contrib/inline-require' script.

    $ tar xjf erubis_X.X.X.tar.bz2
    $ cd erubis_X.X.X/
    $ cp /tmp/abstract_X.X.X/lib/abstract.rb lib
    $ unset RUBYLIB
    $ contrib/inline-require -I lib bin/erubis > contrib/erubis



== Ruby on Rails Support

Erubis supports Ruby on Rails.
All you have to do is to add the following code into your 'config/environment.rb'
and restart web server.

     require 'erubis/helpers/rails_helper'
     #Erubis::Helpers::RailsHelper.engine_class = Erubis::Eruby
     #Erubis::Helpers::RailsHelper.init_properties = {}
     #Erubis::Helpers::RailsHelper.show_src = nil

If Erubis::Helpers::RailsHelper.show_src is ture, Erubis prints converted Ruby code
into log file ('log/development.log' or so).  It is useful for debug.



== Exploring Guide

If you are exploring Eruby, see the following class at first.
* Erubis::TinyEruby (erubis/tiny.rb) --
  the most simple eRuby implementation.
* Erubis::Engine (erubis/engine.rb) --
  base class of Eruby, Ephp, Ejava, and so on.
* Erubis::Eruby (erubis/engine/eruby.rb) --
  engine class for eRuby.
* Erubis::Converter (erubis/converter.rb) --
  convert eRuby script into Ruby code.



== Benchmark

'benchmark/erubybenchmark.rb' is a benchmark script of Erubis.
Try 'ruby erubybenchmark.rb' in benchmark directory.



== License

MIT License



== Author

makoto kuwata <kwa(at)kuwata-lab.com>
<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html 
     PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
  <title>File: README.txt</title>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
  <meta http-equiv="Content-Script-Type" content="text/javascript" />
  <link rel="stylesheet" href=".././rdoc-style.css" type="text/css" media="screen" />
  <script type="text/javascript">
  // <![CDATA[

  function popupCode( url ) {
    window.open(url, "Code", "resizable=yes,scrollbars=yes,toolbar=no,status=no,height=150,width=400")
  }

  function toggleCode( id ) {
    if ( document.getElementById )
      elem = document.getElementById( id );
    else if ( document.all )
      elem = eval( "document.all." + id );
    else
      return false;

    elemStyle = elem.style;
    
    if ( elemStyle.display != "block" ) {
      elemStyle.display = "block"
    } else {
      elemStyle.display = "none"
    }

    return true;
  }
  
  // Make codeblocks hidden by default
  document.writeln( "<style type=\"text/css\">div.method-source-code { display: none }</style>" )
  
  // ]]>
  </script>

</head>
<body>



  <div id="fileHeader">
    <h1>README.txt</h1>
    <table class="header-table">
    <tr class="top-aligned-row">
      <td><strong>Path:</strong></td>
      <td>README.txt
      </td>
    </tr>
    <tr class="top-aligned-row">
      <td><strong>Last Update:</strong></td>
      <td>Sat Apr 02 07:53:01 +0900 2011</td>
    </tr>
    </table>
  </div>
  <!-- banner header -->

  <div id="bodyContent">



  <div id="contextContent">

    <div id="description">
      <h1>README</h1>
<table>
<tr><td valign="top">release:</td><td>2.7.0

</td></tr>
<tr><td valign="top">copyright:</td><td>copyright(c) 2006-2011 kuwata-lab.com all rights reserved.

</td></tr>
</table>
<h2>About <a href="../classes/Erubis.html">Erubis</a></h2>
<p>
<a href="../classes/Erubis.html">Erubis</a> is an implementation of eRuby.
It has the following features.
</p>
<ul>
<li>Very fast, almost three times faster than <a
href="../classes/ERB.html">ERB</a> and even 10% faster than eruby

</li>
<li>Multi-language support (Ruby/PHP/C/Java/Scheme/Perl/Javascript)

</li>
<li>Auto escaping support

</li>
<li>Auto trimming spaces around &#8217;&lt;% %&gt;&#8217;

</li>
<li>Embedded pattern changeable (default &#8217;&lt;% %&gt;&#8217;)

</li>
<li>Enable to handle Processing Instructions (PI) as embedded pattern (ex.
&#8217;&lt;?rb &#8230; ?&gt;&#8217;)

</li>
<li>Context object available and easy to combine eRuby template with YAML
datafile

</li>
<li>Print statement available

</li>
<li>Easy to extend and customize in subclass

</li>
<li>Ruby on Rails support

</li>
</ul>
<p>
<a href="../classes/Erubis.html">Erubis</a> is implemented in pure Ruby. It
requires Ruby 1.8 or higher. <a href="../classes/Erubis.html">Erubis</a>
now supports Ruby 1.9.
</p>
<p>
See doc/users-guide.html for details.
</p>
<h2>Installation</h2>
<ul>
<li>If you have installed RubyGems, just type <tt>gem install erubis</tt>.

<pre>
  $ sudo gem install erubis
</pre>
</li>
<li>Else install <a href="http://rubyforge.org/projects/abstract/">abstract</a>
at first, and download erubis_X.X.X.tar.bz2 and install it by setup.rb.

<pre>
  $ tar xjf abstract_X.X.X.tar.bz2
  $ cd abstract_X.X.X/
  $ sudo ruby setup.rb
  $ cd ..
  $ tar xjf erubis_X.X.X.tar.bz2
  $ cd erubis_X.X.X/
  $ sudo ruby setup.rb
</pre>
</li>
<li>(Optional) It is able to merge &#8216;lib/**/*.rb&#8217; into
&#8216;bin/erubis&#8217; by &#8216;contrib/inline-require&#8217; script.

<pre>
  $ tar xjf erubis_X.X.X.tar.bz2
  $ cd erubis_X.X.X/
  $ cp /tmp/abstract_X.X.X/lib/abstract.rb lib
  $ unset RUBYLIB
  $ contrib/inline-require -I lib bin/erubis &gt; contrib/erubis
</pre>
</li>
</ul>
<h2>Ruby on Rails Support</h2>
<p>
<a href="../classes/Erubis.html">Erubis</a> supports Ruby on Rails. All you
have to do is to add the following code into your
&#8216;config/environment.rb&#8217; and restart web server.
</p>
<pre>
     require 'erubis/helpers/rails_helper'
     #Erubis::Helpers::RailsHelper.engine_class = Erubis::Eruby
     #Erubis::Helpers::RailsHelper.init_properties = {}
     #Erubis::Helpers::RailsHelper.show_src = nil
</pre>
<p>
If Erubis::Helpers::RailsHelper.show_src is ture, <a
href="../classes/Erubis.html">Erubis</a> prints converted Ruby code into
log file (&#8216;log/development.log&#8217; or so). It is useful for debug.
</p>
<h2>Exploring Guide</h2>
<p>
If you are exploring Eruby, see the following class at first.
</p>
<ul>
<li><a href="../classes/Erubis/TinyEruby.html">Erubis::TinyEruby</a>
(erubis/tiny.rb) &#8212; the most simple eRuby implementation.

</li>
<li><a href="../classes/Erubis/Engine.html">Erubis::Engine</a>
(erubis/engine.rb) &#8212; base class of Eruby, Ephp, Ejava, and so on.

</li>
<li><a href="../classes/Erubis/Eruby.html">Erubis::Eruby</a>
(erubis/engine/eruby.rb) &#8212; engine class for eRuby.

</li>
<li><a href="../classes/Erubis/Converter.html">Erubis::Converter</a>
(erubis/converter.rb) &#8212; convert eRuby script into Ruby code.

</li>
</ul>
<h2>Benchmark</h2>
<p>
&#8216;benchmark/erubybenchmark.rb&#8217; is a benchmark script of <a
href="../classes/Erubis.html">Erubis</a>. Try &#8216;ruby
erubybenchmark.rb&#8217; in benchmark directory.
</p>
<h2>License</h2>
<p>
MIT License
</p>
<h2>Author</h2>
<p>
makoto kuwata &lt;kwa(at)kuwata-lab.com&gt;
</p>

    </div>


   </div>


  </div>


    <!-- if includes -->

    <div id="section">





      


    <!-- if method_list -->


  </div>


<div id="validator-badges">
  <p><small><a href="http://validator.w3.org/check/referer">[Validate]</a></small></p>
</div>

</body>
</html>= net-http-persistent

* http://docs.seattlerb.org/net-http-persistent
* https://github.com/drbrain/net-http-persistent

== DESCRIPTION:

Manages persistent connections using Net::HTTP plus a speed fix for Ruby 1.8.
It's thread-safe too!

Using persistent HTTP connections can dramatically increase the speed of HTTP.
Creating a new HTTP connection for every request involves an extra TCP
round-trip and causes TCP congestion avoidance negotiation to start over.

Net::HTTP supports persistent connections with some API methods but does not
handle reconnection gracefully.  Net::HTTP::Persistent supports reconnection
and retry according to RFC 2616.

== FEATURES/PROBLEMS:

* Supports SSL
* Thread-safe
* Pure ruby
* Timeout-less speed boost for Ruby 1.8 (by Aaron Patterson)

== SYNOPSIS

The following example will make two requests to the same server.  The
connection is kept alive between requests:

    require 'net/http/persistent'

    uri = URI 'http://example.com/awesome/web/service'

    http = Net::HTTP::Persistent.new 'my_app_name'

    # perform a GET
    response = http.request uri

    # create a POST
    post_uri = uri + 'create'
    post = Net::HTTP::Post.new post_uri.path
    post.set_form_data 'some' => 'cool data'

    # perform the POST, the URI is always required
    response = http.request post_uri, post

    # if you are done making http requests, or won't make requests for several
    # minutes
    http.shutdown

Please see the documentation on Net::HTTP::Persistent for more information,
including SSL connection verification, header handling and tunable options.

== INSTALL:

  gem install net-http-persistent

== LICENSE:

(The MIT License)

Copyright (c) 2010 Eric Hodel, Aaron Patterson

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
= Active Record -- Object-relational mapping in Rails

Active Record connects classes to relational database tables to establish an
almost zero-configuration persistence layer for applications. The library
provides a base class that, when subclassed, sets up a mapping between the new
class and an existing table in the database. In the context of an application,
these classes are commonly referred to as *models*. Models can also be
connected to other models; this is done by defining *associations*.

Active Record relies heavily on naming in that it uses class and association
names to establish mappings between respective database tables and foreign key
columns. Although these mappings can be defined explicitly, it's recommended
to follow naming conventions, especially when getting started with the
library.

A short rundown of some of the major features:

* Automated mapping between classes and tables, attributes and columns.

   class Product < ActiveRecord::Base
   end

  {Learn more}[link:classes/ActiveRecord/Base.html]

The Product class is automatically mapped to the table named "products",
which might look like this:

   CREATE TABLE products (
     id int(11) NOT NULL auto_increment,
     name varchar(255),
     PRIMARY KEY  (id)
   );

This would also define the following accessors: `Product#name` and
`Product#name=(new_name)`.


* Associations between objects defined by simple class methods.

   class Firm < ActiveRecord::Base
     has_many   :clients
     has_one    :account
     belongs_to :conglomerate
   end

  {Learn more}[link:classes/ActiveRecord/Associations/ClassMethods.html]


* Aggregations of value objects.

   class Account < ActiveRecord::Base
     composed_of :balance, class_name: 'Money',
                 mapping: %w(balance amount)
     composed_of :address,
                 mapping: [%w(address_street street), %w(address_city city)]
   end

  {Learn more}[link:classes/ActiveRecord/Aggregations/ClassMethods.html]


* Validation rules that can differ for new or existing objects.

    class Account < ActiveRecord::Base
      validates :subdomain, :name, :email_address, :password, presence: true
      validates :subdomain, uniqueness: true
      validates :terms_of_service, acceptance: true, on: :create
      validates :password, :email_address, confirmation: true, on: :create
    end

  {Learn more}[link:classes/ActiveRecord/Validations.html]


* Callbacks available for the entire life cycle (instantiation, saving, destroying, validating, etc.).

   class Person < ActiveRecord::Base
     before_destroy :invalidate_payment_plan
     # the `invalidate_payment_plan` method gets called just before Person#destroy
   end

  {Learn more}[link:classes/ActiveRecord/Callbacks.html]


* Inheritance hierarchies.

   class Company < ActiveRecord::Base; end
   class Firm < Company; end
   class Client < Company; end
   class PriorityClient < Client; end

  {Learn more}[link:classes/ActiveRecord/Base.html]


* Transactions.

    # Database transaction
    Account.transaction do
      david.withdrawal(100)
      mary.deposit(100)
    end

  {Learn more}[link:classes/ActiveRecord/Transactions/ClassMethods.html]


* Reflections on columns, associations, and aggregations.

    reflection = Firm.reflect_on_association(:clients)
    reflection.klass # => Client (class)
    Firm.columns # Returns an array of column descriptors for the firms table

  {Learn more}[link:classes/ActiveRecord/Reflection/ClassMethods.html]


* Database abstraction through simple adapters.

    # connect to SQLite3
    ActiveRecord::Base.establish_connection(adapter: 'sqlite3', database: 'dbfile.sqlite3')

    # connect to MySQL with authentication
    ActiveRecord::Base.establish_connection(
      adapter:  'mysql2',
      host:     'localhost',
      username: 'me',
      password: 'secret',
      database: 'activerecord'
    )

  {Learn more}[link:classes/ActiveRecord/Base.html] and read about the built-in support for
  MySQL[link:classes/ActiveRecord/ConnectionAdapters/MysqlAdapter.html],
  PostgreSQL[link:classes/ActiveRecord/ConnectionAdapters/PostgreSQLAdapter.html], and
  SQLite3[link:classes/ActiveRecord/ConnectionAdapters/SQLite3Adapter.html].


* Logging support for Log4r[https://github.com/colbygk/log4r] and Logger[http://www.ruby-doc.org/stdlib/libdoc/logger/rdoc].

    ActiveRecord::Base.logger = ActiveSupport::Logger.new(STDOUT)
    ActiveRecord::Base.logger = Log4r::Logger.new('Application Log')


* Database agnostic schema management with Migrations.

    class AddSystemSettings < ActiveRecord::Migration
      def up
        create_table :system_settings do |t|
          t.string  :name
          t.string  :label
          t.text    :value
          t.string  :type
          t.integer :position
        end

        SystemSetting.create name: 'notice', label: 'Use notice?', value: 1
      end

      def down
        drop_table :system_settings
      end
    end

  {Learn more}[link:classes/ActiveRecord/Migration.html]


== Philosophy

Active Record is an implementation of the object-relational mapping (ORM)
pattern[http://www.martinfowler.com/eaaCatalog/activeRecord.html] by the same
name described by Martin Fowler:

  "An object that wraps a row in a database table or view,
  encapsulates the database access, and adds domain logic on that data."

Active Record attempts to provide a coherent wrapper as a solution for the inconvenience that is
object-relational mapping. The prime directive for this mapping has been to minimize
the amount of code needed to build a real-world domain model. This is made possible
by relying on a number of conventions that make it easy for Active Record to infer
complex relations and structures from a minimal amount of explicit direction.

Convention over Configuration:
* No XML files!
* Lots of reflection and run-time extension
* Magic is not inherently a bad word

Admit the Database:
* Lets you drop down to SQL for odd cases and performance
* Doesn't attempt to duplicate or replace data definitions


== Download and installation

The latest version of Active Record can be installed with RubyGems:

  % [sudo] gem install activerecord

Source code can be downloaded as part of the Rails project on GitHub:

* https://github.com/rails/rails/tree/4-2-stable/activerecord


== License

Active Record is released under the MIT license:

* http://www.opensource.org/licenses/MIT


== Support

API documentation is at:

* http://api.rubyonrails.org

Bug reports can be filed for the Ruby on Rails project here:

* https://github.com/rails/rails/issues

Feature requests should be discussed on the rails-core mailing list here:

* https://groups.google.com/forum/?fromgroups#!forum/rubyonrails-core

= Ruby/NTLM -- NTLM Authentication Library for Ruby

Ruby/NTLM provides message creator and parser for the NTLM authentication.

Some features:
* Independent from non-standard Ruby libraries.
* Supports NTLM and NTLMv2 reponses.

== Simple Example

* Creating NTLM Type 1 message

   t1 = NTLM::Message::Type1.new()

* Parsing NTLM Type 2 message from server

   t2 = NTLM::Message.parse(message_from_server)

* Creating NTLM Type 3 message

   t3 = t2.response({:user => 'user', :password => 'passwd'})

== Support

You can find Ruby/NTLM RubyForge page at http://rubyforge.org/projects/rubyntlm.
# Arel [![Build Status](https://secure.travis-ci.org/rails/arel.svg?branch=master)](http://travis-ci.org/rails/arel) [![Dependency Status](https://gemnasium.com/rails/arel.svg)](https://gemnasium.com/rails/arel)

* http://github.com/rails/arel

## DESCRIPTION

Arel Really Exasperates Logicians

Arel is a SQL AST manager for Ruby. It

1. Simplifies the generation of complex SQL queries
2. Adapts to various RDBMSes

It is intended to be a framework framework; that is, you can build your own ORM
with it, focusing on innovative object and collection modeling as opposed to
database compatibility and query generation.

## Status

For the moment, Arel uses Active Record's connection adapters to connect to the various engines, connection pooling, perform quoting, and do type conversion.

## A Gentle Introduction

Generating a query with Arel is simple. For example, in order to produce

```sql
SELECT * FROM users
```

you construct a table relation and convert it to sql:

```ruby
users = Arel::Table.new(:users)
query = users.project(Arel.sql('*'))
query.to_sql
```

### More Sophisticated Queries

Here is a whirlwind tour through the most common SQL operators. These will probably cover 80% of all interaction with the database.

First is the 'restriction' operator, `where`:

```ruby
users.where(users[:name].eq('amy'))
# => SELECT * FROM users WHERE users.name = 'amy'
```

What would, in SQL, be part of the `SELECT` clause is called in Arel a `projection`:

```ruby
users.project(users[:id])
# => SELECT users.id FROM users
```

Comparison operators `=`, `!=`, `<`, `>`, `<=`, `>=`, `IN`:

```ruby
users.where(users[:age].eq(10)).project(Arel.sql('*')) # => SELECT * FROM "users"  WHERE "users"."age" = 10
users.where(users[:age].not_eq(10)).project(Arel.sql('*')) # => SELECT * FROM "users"  WHERE "users"."age" != 10
users.where(users[:age].lt(10)).project(Arel.sql('*')) # => SELECT * FROM "users"  WHERE "users"."age" < 10
users.where(users[:age].gt(10)).project(Arel.sql('*')) # => SELECT * FROM "users"  WHERE "users"."age" > 10
users.where(users[:age].lteq(10)).project(Arel.sql('*')) # => SELECT * FROM "users"  WHERE "users"."age" <= 10
users.where(users[:age].gteq(10)).project(Arel.sql('*')) # => SELECT * FROM "users"  WHERE "users"."age" >= 10
users.where(users[:age].in([20, 16, 17])).project(Arel.sql('*')) # => SELECT * FROM "users"  WHERE "users"."age" IN (20, 16, 17)
```

Joins resemble SQL strongly:

```ruby
users.join(photos).on(users[:id].eq(photos[:user_id]))
# => SELECT * FROM users INNER JOIN photos ON users.id = photos.user_id
```

Left Joins

```ruby
users.join(photos, Arel::Nodes::OuterJoin).on(users[:id].eq(photos[:user_id]))
# => SELECT FROM users LEFT OUTER JOIN photos ON users.id = photos.user_id
```

What are called `LIMIT` and `OFFSET` in SQL are called `take` and `skip` in Arel:

```ruby
users.take(5) # => SELECT * FROM users LIMIT 5
users.skip(4) # => SELECT * FROM users OFFSET 4
```

`GROUP BY` is called `group`:

```ruby
users.project(users[:name]).group(users[:name])
# => SELECT users.name FROM users GROUP BY users.name
```

The best property of arel is its "composability", or closure under all operations. For example, to restrict AND project, just "chain" the method invocations:

```ruby
users                                 \
  .where(users[:name].eq('amy'))      \
  .project(users[:id])                \
# => SELECT users.id FROM users WHERE users.name = 'amy'
```

All operators are chainable in this way, and they are chainable any number of times, in any order.

```ruby
users.where(users[:name].eq('bob')).where(users[:age].lt(25))
```

The `OR` operator works like this:

```ruby
users.where(users[:name].eq('bob').or(users[:age].lt(25)))
```

The `AND` operator behaves similarly.

Aggregate functions `AVG`, `SUM`, `COUNT`, `MIN`, `MAX`, `HAVING`:

```ruby
photos.group(photos[:user_id]).having(photos[:id].count.gt(5)) # => SELECT FROM photos GROUP BY photos.user_id HAVING COUNT(photos.id) > 5
users.project(users[:age].sum) # => SELECT SUM(users.age) FROM users
users.project(users[:age].average) # => SELECT AVG(users.age) FROM users
users.project(users[:age].maximum) # => SELECT MAX(users.age) FROM users
users.project(users[:age].minimum) # => SELECT MIN(users.age) FROM users
users.project(users[:age].count) # => SELECT COUNT(users.age) FROM users
```

Aliasing Aggregate Functions:

```ruby
users.project(users[:age].average.as("mean_age")) # => SELECT AVG(users.age) AS mean_age FROM users
```

### The Crazy Features

The examples above are fairly simple and other libraries match or come close to matching the expressiveness of Arel (e.g., `Sequel` in Ruby).

#### Inline math operations

Suppose we have a table `products` with prices in different currencies. And we have a table `currency_rates`, of constantly changing currency rates. In Arel:

```ruby
products = Arel::Table.new(:products)
# Attributes: [:id, :name, :price, :currency_id]

currency_rates = Arel::Table.new(:currency_rates)
# Attributes: [:from_id, :to_id, :date, :rate]
```

Now, to order products by price in user preferred currency simply call:

```ruby
products.
  join(:currency_rates).on(products[:currency_id].eq(currency_rates[:from_id])).
  where(currency_rates[:to_id].eq(user_preferred_currency), currency_rates[:date].eq(Date.today)).
  order(products[:price] * currency_rates[:rate])
```

#### Complex Joins

Where Arel really shines is in its ability to handle complex joins and aggregations. As a first example, let's consider an "adjacency list", a tree represented in a table. Suppose we have a table `comments`, representing a threaded discussion:

```ruby
comments = Arel::Table.new(:comments)
```

And this table has the following attributes:

```ruby
# [:id, :body, :parent_id]
```

The `parent_id` column is a foreign key from the `comments` table to itself.
Joining a table to itself requires aliasing in SQL. This aliasing can be handled from Arel as below:

```ruby
replies = comments.alias
comments_with_replies = \
  comments.join(replies).on(replies[:parent_id].eq(comments[:id])).where(comments[:id].eq(1))
# => SELECT * FROM comments INNER JOIN comments AS comments_2 WHERE comments_2.parent_id = comments.id AND comments.id = 1
```

This will return the reply for the first comment.

[Common Table Expressions(CTE)](https://en.wikipedia.org/wiki/Common_table_expressions#Common_table_expression) support via:

Create a `CTE`

```ruby
cte_table = Arel::Table.new(:cte_table)
composed_cte = Arel::Nodes::As.new(cte_table, photos.where(photos[:created_at].gt(Date.current)))
```

Use the created `CTE`:

```ruby
users.
  join(cte_table).on(users[:id].eq(cte_table[:user_id])).
  project(users[:id], cte_table[:click].sum).
  with(composed_cte)

# => WITH cte_table AS (SELECT FROM photos  WHERE photos.created_at > '2014-05-02') SELECT users.id, SUM(cte_table.click) FROM users INNER JOIN cte_table ON users.id = cte_table.user_id
```

When your query is too complex for `Arel`, you can use `Arel::SqlLiteral`:

```ruby
photo_clicks = Arel::Nodes::SqlLiteral.new(<<-SQL
    CASE WHEN condition1 THEN calculation1
    WHEN condition2 THEN calculation2
    WHEN condition3 THEN calculation3
    ELSE default_calculation END
SQL
)
photos.project(photo_clicks.as("photo_clicks"))
# => SELECT CASE WHEN condition1 THEN calculation1
    WHEN condition2 THEN calculation2
    WHEN condition3 THEN calculation3
    ELSE default_calculation END
 FROM "photos"
```

### License

Arel is released under the [MIT License](http://opensource.org/licenses/MIT).
# factory_girl [![Build Status](https://secure.travis-ci.org/thoughtbot/factory_girl.png)](http://travis-ci.org/thoughtbot/factory_girl?branch=master) [![Dependency Status](https://gemnasium.com/thoughtbot/factory_girl.png)](https://gemnasium.com/thoughtbot/factory_girl) [![Code Climate](https://codeclimate.com/github/thoughtbot/factory_girl.png)](https://codeclimate.com/github/thoughtbot/factory_girl)

factory_girl is a fixtures replacement with a straightforward definition syntax, support for multiple build strategies (saved instances, unsaved instances, attribute hashes, and stubbed objects), and support for multiple factories for the same class (user, admin_user, and so on), including factory inheritance.

If you want to use factory_girl with Rails, see
[factory_girl_rails](https://github.com/thoughtbot/factory_girl_rails).

Documentation
-------------

You should find the documentation for your version of factory_girl on [Rubygems](https://rubygems.org/gems/factory_girl).

See [GETTING_STARTED] for information on defining and using factories.

Install
--------

```shell
gem install factory_girl
```
or add the following line to Gemfile:

```ruby
gem 'factory_girl'
```
and run `bundle install` from your shell.

Supported Ruby versions
-----------------------

The factory_girl 3.x+ series supports MRI Ruby 1.9. Additionally, factory_girl
3.6+ supports JRuby 1.6.7.2+ while running in 1.9 mode. See [GETTING_STARTED]
for more information on configuring the JRuby environment.

For versions of Ruby prior to 1.9, please use factory_girl 2.x.

More Information
----------------

* [Rubygems](https://rubygems.org/gems/factory_girl)
* [Stack Overflow](http://stackoverflow.com/questions/tagged/factory-girl)
* [Issues](https://github.com/thoughtbot/factory_girl/issues)
* [GIANT ROBOTS SMASHING INTO OTHER GIANT ROBOTS](http://robots.thoughtbot.com/)

[GETTING_STARTED]: http://rubydoc.info/gems/factory_girl/file/GETTING_STARTED.md

Contributing
------------

Please see [CONTRIBUTING.md](https://github.com/thoughtbot/factory_girl/blob/master/CONTRIBUTING.md).

Credits
-------

factory_girl was originally written by Joe Ferris and is now maintained by Josh
Clayton. Many improvements and bugfixes were contributed by the [open source
community](https://github.com/thoughtbot/factory_girl/graphs/contributors).

![thoughtbot](http://thoughtbot.com/assets/tm/logo.png)

factory_girl is maintained and funded by [thoughtbot, inc](http://thoughtbot.com/community)

The names and logos for thoughtbot are trademarks of thoughtbot, inc.

License
-------

factory_girl is Copyright © 2008-2014 Joe Ferris and thoughtbot. It is free software, and may be redistributed under the terms specified in the [LICENSE](https://github.com/thoughtbot/factory_girl/blob/master/LICENSE) file.
# factory_girl_rails [![Build Status][ci-image]][ci] [![Code Climate][grade-image]][grade]

[factory_girl][fg] is a fixtures replacement with a straightforward definition
syntax, support for multiple build strategies (saved instances, unsaved
instances, attribute hashes, and stubbed objects), and support for multiple
factories for the same class (`user`, `admin_user`, and so on), including factory
inheritance.

## Rails

factory_girl_rails provides Rails integration for [factory_girl][fg].

Currently, automatic factory definition loading is the only Rails-specific feature.

Supported Rails versions are listed in [`Appraisals`](Appraisals). Supported
Ruby versions are listed in [`.travis.yml`](.travis.yml).

## Download

Github: http://github.com/thoughtbot/factory_girl_rails

Gem:

    gem install factory_girl_rails

## Configuration

Add `factory_girl_rails` to your Gemfile:

```ruby
gem 'factory_girl_rails'
```

Generators for factories will automatically substitute fixture (and maybe any other
`fixture_replacement` you set). If you want to disable this feature, add the
following to your application.rb file:

```ruby
config.generators do |g|
  g.factory_girl false
end
```

Default factories directory is `test/factories`, or `spec/factories` if
`test_framework` generator is set to `:rspec`; change this behavior with:

```ruby
config.generators do |g|
  g.factory_girl dir: 'custom/dir/for/factories'
end
```

If you use factory_girl for fixture replacement, ensure that
factory_girl_rails is available in the development group. If it's not, Rails
will generate standard .yml files instead of factory files.

factory_girl takes an option `suffix: 'some_suffix'` to generate factories as
`modelname_some_suffix.rb`.

If you use factory_girl for fixture replacement and already have a
`factories.rb` file in the directory that contains your tests,
factory_girl_rails will insert new factory definitions at the top of
`factories.rb`.

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits

[factory_girl][fg] was originally written by Joe Ferris.

![thoughtbot](http://thoughtbot.com/images/tm/logo.png)

factory_girl is maintained and funded by [thoughtbot, inc](http://thoughtbot.com/community)

The names and logos for thoughtbot are trademarks of thoughtbot, inc.

## License

factory_girl_rails is Copyright © 2008-2014 Joe Ferris and thoughtbot. It is free
software, and may be redistributed under the terms specified in the
[LICENSE]() file.

[fg]: https://github.com/thoughtbot/factory_girl
[ci]: http://travis-ci.org/thoughtbot/factory_girl_rails?branch=master
[ci-image]: https://secure.travis-ci.org/thoughtbot/factory_girl_rails.png
[grade]: https://codeclimate.com/github/thoughtbot/factory_girl_rails
[grade-image]: https://codeclimate.com/github/thoughtbot/factory_girl_rails.png
Turbolinks
===========

Turbolinks makes following links in your web application faster. Instead of letting the browser recompile the JavaScript and CSS between each page change, it keeps the current page instance alive and replaces only the body and the title in the head. Think CGI vs persistent process.

This is similar to [pjax](https://github.com/defunkt/jquery-pjax), but instead of worrying about what element on the page to replace, and tailoring the server-side response to fit, we replace the entire body. This means that you get the bulk of the speed benefits from pjax (no recompiling of the JavaScript or CSS) without having to tailor the server-side response. It just works.

Do note that this of course means that you'll have a long-running, persistent session with maintained state. That's what's making it so fast. But it also means that you may have to pay additional care not to leak memory or otherwise bloat that long-running state. That should rarely be a problem unless you're doing something really funky, but you do have to be aware of it. Your memory leaking sins will not be swept away automatically by the cleansing page change any more.


How much faster is it really?
-----------------------------

It depends. The more CSS and JavaScript you have, the bigger the benefit of not throwing away the browser instance and recompiling all of it for every page. Just like a CGI script that says "hello world" will be fast, but a CGI script loading Rails on every request will not.

In any case, the benefit can be up to [twice as fast](https://github.com/steveklabnik/turbolinks_test/tree/all_the_assets) in apps with lots of JS and CSS. Of course, your mileage may vary, be dependent on your browser version, the moon cycle, and all other factors affecting performance testing. But at least it's a yardstick.

The best way to find out just how fast it is? Try it on your own application. It hardly takes any effort at all.


No jQuery or any other library
--------------------------------

Turbolinks is designed to be as light-weight as possible (so you won't think twice about using it even for mobile stuff). It does not require jQuery or any other library to work. But it works great _with_ the jQuery or Prototype framework, or whatever else have you.


Events
------

With Turbolinks pages will change without a full reload, so you can't rely on `DOMContentLoaded` or `jQuery.ready()` to trigger your code. Instead Turbolinks fires events on `document` to provide hooks into the lifecycle of the page.

***Load* a fresh version of a page from the server:**
* `page:before-change` a Turbolinks-enabled link has been clicked *(see below for more details)*
* `page:fetch` starting to fetch a new target page
* `page:receive` the page has been fetched from the server, but not yet parsed
* `page:before-unload` the page has been parsed and is about to be changed
* `page:change` the page has been changed to the new version (and on DOMContentLoaded)
* `page:update` is triggered alongside both page:change and jQuery's ajaxSuccess (if jQuery is available - otherwise you can manually trigger it when calling XMLHttpRequest in your own code)
* `page:load` is fired at the end of the loading process.

Handlers bound to the `page:before-change` event may return `false`, which will cancel the Turbolinks process.

By default, Turbolinks caches 10 of these page loads. It listens to the [popstate](https://developer.mozilla.org/en-US/docs/DOM/Manipulating_the_browser_history#The_popstate_event) event and attempts to restore page state from the cache when it's triggered. When `popstate` is fired the following process happens:

***Restore* a cached page from the client-side cache:**
* `page:before-unload` page has been fetched from the cache and is about to be changed
* `page:change` page has changed to the cached page.
* `page:restore` is fired at the end of restore process.

The number of pages Turbolinks caches can be configured to suit your application's needs:

```javascript
// View the current cache size
Turbolinks.pagesCached();

// Set the cache size
Turbolinks.pagesCached(20);
```

When a page is removed from the cache due to the cache reaching its size limit, the `page:expire` event is triggered.  Listeners bound to this event can access the cached page object using `event.originalEvent.data`.  Keys of note for this page cache object include `url`, `body`, and `title`.  

To implement a client-side spinner, you could listen for `page:fetch` to start it and `page:receive` to stop it.

```javascript
// using jQuery for simplicity
    
$(document).on("page:fetch", startSpinner);
$(document).on("page:receive", stopSpinner);
```

DOM transformations that are idempotent are best. If you have transformations that are not, bind them to `page:load` (in addition to the initial page load) instead of `page:change` (as that would run them again on the cached pages):

```javascript
// using jQuery for simplicity

$(document).on("ready page:load", nonIdempotentFunction);
```

Transition Cache: A Speed Boost
-------------------------------

Transition Cache, added in v2.2.0, makes loading cached pages instantaneous. Once a user has visited a page, returning later to the page results in an instant load.

For example, if Page A is already cached by Turbolinks and you are on Page B, clicking a link to Page A will *immediately* display the cached copy of Page A. Turbolinks will then fetch Page A from the server and replace the cached page once the new copy is returned.

To enable Transition Cache, include the following in your javascript:
```javascript
Turbolinks.enableTransitionCache();
```

The one drawback is that dramatic differences in appearance between a cached copy and new copy may lead to a jarring affect for the end-user. This will be especially true for pages that have many moving parts (expandable sections, sortable tables, infinite scrolling, etc.).

If you find that a page is causing problems, you can have Turbolinks skip displaying the cached copy by adding `data-no-transition-cache` to any DOM element on the offending page.

Progress Bar
------------

Because Turbolinks skips the traditional full page reload, browsers won't display their native progress bar when changing pages. To fill this void, Turbolinks offers an optional JavaScript-and-CSS-based progress bar to display page loading progress.

To enable the progress bar, include the following in your JavaScript:
```javascript
Turbolinks.enableProgressBar();
```

The progress bar is implemented on the `<html>` element's pseudo `:before` element and can be **customized** by including CSS with higher specificity than the included styles. For example:

```css
html.turbolinks-progress-bar::before {
  background-color: red !important;
  height: 5px !important;
}
```

In Turbolinks 3.0, the progress bar will be turned on by default.


Initialization
--------------

Turbolinks will be enabled **only** if the server has rendered a `GET` request.

Some examples, given a standard RESTful resource:

* `POST :create` => resource successfully created => redirect to `GET :show`
  * Turbolinks **ENABLED**
* `POST :create` => resource creation failed => render `:new`
  * Turbolinks **DISABLED**

**Why not all request types?** Some browsers track the request method of each page load, but triggering pushState methods don't change this value.  This could lead to the situation where pressing the browser's reload button on a page that was fetched with Turbolinks would attempt a `POST` (or something other than `GET`) because the last full page load used that method.


Opting out of Turbolinks
------------------------

By default, all internal HTML links will be funneled through Turbolinks, but you can opt out by marking links or their parent container with `data-no-turbolink`. For example, if you mark a div with `data-no-turbolink`, then all links inside of that div will be treated as regular links. If you mark the body, every link on that entire page will be treated as regular links.

```html
<a href="/">Home (via Turbolinks)</a>
<div id="some-div" data-no-turbolink>
  <a href="/">Home (without Turbolinks)</a>
</div>
```

Note that internal links to files containing a file extension other than **.html** will automatically be opted out of Turbolinks. So links to /images/panda.gif will just work as expected.  To whitelist additional file extensions to be processed by Turbolinks, use `Turbolinks.allowLinkExtensions()`.

```javascript
Turbolinks.allowLinkExtensions();                 // => ['html']
Turbolinks.allowLinkExtensions('md');             // => ['html', 'md']
Turbolinks.allowLinkExtensions('coffee', 'scss'); // => ['html', 'md', 'coffee', 'scss']
```

Also, Turbolinks is installed as the last click handler for links. So if you install another handler that calls event.preventDefault(), Turbolinks will not run. This ensures that you can safely use Turbolinks with stuff like `data-method`, `data-remote`, or `data-confirm` from Rails.


jquery.turbolinks
-----------------

If you have a lot of existing JavaScript that binds elements on jQuery.ready(), you can pull the [jquery.turbolinks](https://github.com/kossnocorp/jquery.turbolinks) library into your project that will trigger ready() when Turbolinks triggers the `page:load` event. It may restore functionality of some libraries.

Add the gem to your project, then add the following line to your JavaScript manifest file, after `jquery.js` but before `turbolinks.js`:

``` js
//= require jquery.turbolinks
```

Additional details and configuration options can be found in the [jquery.turbolinks README](https://github.com/kossnocorp/jquery.turbolinks/blob/master/README.md).

Asset change detection
----------------------

You can track certain assets, like application.js and application.css, that you want to ensure are always of the latest version inside a Turbolinks session. This is done by marking those asset links with data-turbolinks-track, like so:

```html
<link href="/assets/application-9bd64a86adb3cd9ab3b16e9dca67a33a.css" rel="stylesheet"
      type="text/css" data-turbolinks-track>
```

If those assets change URLs (embed an md5 stamp to ensure this), the page will do a full reload instead of going through Turbolinks. This ensures that all Turbolinks sessions will always be running off your latest JavaScript and CSS.

When this happens, you'll technically be requesting the same page twice. Once through Turbolinks to detect that the assets changed, and then again when we do a full redirect to that page.


Evaluating script tags
----------------------

Turbolinks will evaluate any script tags in pages it visits, if those tags do not have a type or if the type is text/javascript. All other script tags will be ignored.

As a rule of thumb when switching to Turbolinks, move all of your javascript tags inside the `head` and then work backwards, only moving javascript code back to the body if absolutely necessary. If you have any script tags in the body you do not want to be re-evaluated then you can set the `data-turbolinks-eval` attribute to `false`:

```html
<script type="text/javascript" data-turbolinks-eval=false>
  console.log("I'm only run once on the initial page load");
</script>
```

Triggering a Turbolinks visit manually
---------------------------------------

You can use `Turbolinks.visit(path)` to go to a URL through Turbolinks.

You can also use `redirect_via_turbolinks_to` in Rails to perform a redirect via Turbolinks.


Full speed for pushState browsers, graceful fallback for everything else
------------------------------------------------------------------------

Like pjax, this naturally only works with browsers capable of pushState. But of course we fall back gracefully to full page reloads for browsers that do not support it.


Compatibility
-------------

Turbolinks is designed to work with any browser that fully supports pushState and all the related APIs. This includes Safari 6.0+ (but not Safari 5.1.x!), IE10, and latest Chromes and Firefoxes.

Do note that existing JavaScript libraries may not all be compatible with Turbolinks out of the box due to the change in instantiation cycle. You might very well have to modify them to work with Turbolinks' new set of events.  For help with this, check out the [Turbolinks Compatibility](http://reed.github.io/turbolinks-compatibility) project.


Installation
------------

1. Add `gem 'turbolinks'` to your Gemfile.
1. Run `bundle install`.
1. Add `//= require turbolinks` to your Javascript manifest file (usually found at `app/assets/javascripts/application.js`). If your manifest requires both turbolinks and jQuery, make sure turbolinks is listed *after* jQuery.
1. Restart your server and you're now using turbolinks!

Language Ports
--------------

*These projects are not affiliated with or endorsed by the Rails Turbolinks team.*

* [Flask Turbolinks](https://github.com/lepture/flask-turbolinks) (Python Flask)
* [Django Turbolinks](https://github.com/dgladkov/django-turbolinks) (Python Django)
* [ASP.NET MVC Turbolinks](https://github.com/kazimanzurrashid/aspnetmvcturbolinks)
* [PHP Turbolinks Component](https://github.com/helthe/Turbolinks) (Symfony Component)
* [PHP Turbolinks Package](https://github.com/frenzyapp/turbolinks) (Laravel Package)
* [Grails Turbolinks](http://grails.org/plugin/turbolinks) (Grails Plugin)

Credits
-------

Thanks to Chris Wanstrath for his original work on Pjax. Thanks to Sam Stephenson and Josh Peek for their additional work on Pjax and Stacker and their help with getting Turbolinks released. Thanks to David Estes and Nick Reed for handling the lion's share of post-release issues and feature requests. And thanks to everyone else who's fixed or reported an issue!
# Sass [![Gem Version](https://badge.fury.io/rb/sass.png)](http://badge.fury.io/rb/sass) [![Inline docs](http://inch-ci.org/github/sass/sass.svg)](http://inch-ci.org/github/sass/sass)

**Sass makes CSS fun again**. Sass is an extension of CSS3,
adding nested rules, variables, mixins, selector inheritance, and more.
It's translated to well-formatted, standard CSS
using the command line tool or a web-framework plugin.

Sass has two syntaxes. The new main syntax (as of Sass 3)
is known as "SCSS" (for "Sassy CSS"),
and is a superset of CSS3's syntax.
This means that every valid CSS3 stylesheet is valid SCSS as well.
SCSS files use the extension `.scss`.

The second, older syntax is known as the indented syntax (or just "Sass").
Inspired by Haml's terseness, it's intended for people
who prefer conciseness over similarity to CSS.
Instead of brackets and semicolons,
it uses the indentation of lines to specify blocks.
Although no longer the primary syntax,
the indented syntax will continue to be supported.
Files in the indented syntax use the extension `.sass`.

## Using

Sass can be used from the command line
or as part of a web framework.
The first step is to install the gem:

    gem install sass

After you convert some CSS to Sass, you can run

    sass style.scss

to compile it back to CSS.
For more information on these commands, check out

    sass --help

To install Sass in Rails 2,
just add `config.gem "sass"` to `config/environment.rb`.
In Rails 3, add `gem "sass"` to your Gemfile instead.
`.sass` or `.scss` files should be placed in `public/stylesheets/sass`,
where they'll be automatically compiled
to corresponding CSS files in `public/stylesheets` when needed
(the Sass template directory is customizable...
see [the Sass reference](http://sass-lang.com/docs/yardoc/file.SASS_REFERENCE.html#template_location-option) for details).

Sass can also be used with any Rack-enabled web framework.
To do so, just add

```ruby
require 'sass/plugin/rack'
use Sass::Plugin::Rack
```

to `config.ru`.
Then any Sass files in `public/stylesheets/sass`
will be compiled into CSS files in `public/stylesheets` on every request.

To use Sass programmatically,
check out the [YARD documentation](http://sass-lang.com/documentation/file.SASS_REFERENCE.html#using_sass).

## Formatting

Sass is an extension of CSS
that adds power and elegance to the basic language.
It allows you to use [variables][vars], [nested rules][nested],
[mixins][mixins], [inline imports][imports],
and more, all with a fully CSS-compatible syntax.
Sass helps keep large stylesheets well-organized,
and get small stylesheets up and running quickly,
particularly with the help of
[the Compass style library](http://compass-style.org).

[vars]:    http://sass-lang.com/documentation/file.SASS_REFERENCE.html#variables_
[nested]:  http://sass-lang.com/documentation/file.SASS_REFERENCE.html#nested_rules
[mixins]:  http://sass-lang.com/documentation/file.SASS_REFERENCE.html#mixins
[imports]: http://sass-lang.com/documentation/file.SASS_REFERENCE.html#import

Sass has two syntaxes.
The one presented here, known as "SCSS" (for "Sassy CSS"),
is fully CSS-compatible.
The other (older) syntax, known as the indented syntax or just "Sass",
is whitespace-sensitive and indentation-based.
For more information, see the [reference documentation][syntax].

[syntax]: http://sass-lang.com/documentation/file.SASS_REFERENCE.html#syntax

To run the following examples and see the CSS they produce,
put them in a file called `test.scss` and run `sass test.scss`.

### Nesting

Sass avoids repetition by nesting selectors within one another.
The same thing works for properties.

```scss
table.hl {
  margin: 2em 0;
  td.ln { text-align: right; }
}

li {
  font: {
    family: serif;
    weight: bold;
    size: 1.2em;
  }
}
```

### Variables

Use the same color all over the place?
Need to do some math with height and width and text size?
Sass supports variables, math operations, and many useful functions.

```scss
$blue: #3bbfce;
$margin: 16px;

.content_navigation {
  border-color: $blue;
  color: darken($blue, 10%);
}

.border {
  padding: $margin / 2;
  margin: $margin / 2;
  border-color: $blue;
}
```

### Mixins

Even more powerful than variables,
mixins allow you to re-use whole chunks of CSS,
properties or selectors.
You can even give them arguments. 

```scss
@mixin table-scaffolding {
  th {
    text-align: center;
    font-weight: bold;
  }
  td, th { padding: 2px; }
}

@mixin left($dist) {
  float: left;
  margin-left: $dist;
}

#data {
  @include left(10px);
  @include table-scaffolding;
}
```

A comprehensive list of features is available
in the [Sass reference](http://sass-lang.com/documentation/file.SASS_REFERENCE.html).

## Executables

The Sass gem includes several executables that are useful
for dealing with Sass from the command line.

### `sass`

The `sass` executable transforms a source Sass file into CSS.
See `sass --help` for further information and options.

### `sass-convert`

The `sass-convert` executable converts between CSS, Sass, and SCSS.
When converting from CSS to Sass or SCSS,
nesting is applied where appropriate.
See `sass-convert --help` for further information and options.

### Running locally

To run the Sass executables from a source checkout instead of from rubygems:

```
$ cd <SASS_CHECKOUT_DIRECTORY>
$ bundle
$ bundle exec sass ...
$ bundle exec scss ...
$ bundle exec sass-convert ...
```

## Authors

Sass was envisioned by [Hampton Catlin](http://www.hamptoncatlin.com)
(@hcatlin). However, Hampton doesn't even know his way around the code anymore
and now occasionally consults on the language issues. Hampton lives in San
Francisco, California and works as VP of Technology
at [Moovweb](http://www.moovweb.com/).

[Natalie Weizenbaum](https://twitter.com/nex3) is the primary developer and architect of
Sass. Her hard work has kept the project alive by endlessly answering forum
posts, fixing bugs, refactoring, finding speed improvements, writing
documentation, implementing new features, and getting Hampton coffee (a fitting
task for a girl genius). Natalie lives in Seattle, Washington and works on
[Dart](http://dartlang.org) application libraries at Google.

[Chris Eppstein](http://acts-as-architect.blogspot.com) is a core contributor to
Sass and the creator of Compass, the first Sass-based framework. Chris focuses
on making Sass more powerful, easy to use, and on ways to speed its adoption
through the web development community. Chris lives in San Jose, California with
his wife and daughter. He is an Engineer for
[LinkedIn.com](http://linkedin.com), where one of his responsibilities is to
maintain Sass & Compass.

If you use this software, you must pay Hampton a compliment. And buy Natalie
some candy. Maybe pet a kitten. Yeah. Pet that kitty.

Beyond that, the implementation is licensed under the MIT License.
Okay, fine, I guess that means compliments aren't __required__.
# Listen [![Gem Version](https://badge.fury.io/rb/listen.png)](http://badge.fury.io/rb/listen) [![Build Status](https://secure.travis-ci.org/guard/listen.png?branch=master)](http://travis-ci.org/guard/listen) [![Dependency Status](https://gemnasium.com/guard/listen.png)](https://gemnasium.com/guard/listen) [![Code Climate](https://codeclimate.com/github/guard/listen.png)](https://codeclimate.com/github/guard/listen) [![Coverage Status](https://coveralls.io/repos/guard/listen/badge.png?branch=master)](https://coveralls.io/r/guard/listen)

The Listen gem listens to file modifications and notifies you about the changes.

## Features

* Works everywhere!
* Supports watching multiple directories from a single listener.
* OS-specific adapters for Mac OS X 10.6+, Linux, *BSD and Windows.
* Automatic fallback to polling if OS-specific adapter doesn't work.
* Detects file modification, addition and removal.
* File content checksum comparison for modifications made under the same second.
* Allows supplying regexp-patterns to ignore and filter paths for better results.
* Tested on all Ruby environments via [Travis CI](https://travis-ci.org/guard/listen).

## Pending features

Still not implemented, pull requests are welcome.

* Symlinks support. [#25](https://github.com/guard/listen/issues/25)
* Signal handling. [#105](https://github.com/guard/listen/issues/105)
* Non-recursive directory scanning. [#111](https://github.com/guard/listen/issues/111)

## Install

### Using Bundler

The simplest way to install Listen is to use Bundler.

Add Listen to your Gemfile:

```ruby
group :development do
  gem 'listen'
end
```

and install it by running Bundler:

```bash
$ bundle
```

### Install the gem with RubyGems

```bash
$ gem install listen
```

### On Windows

If your are on Windows and using Ruby MRI >= 1.9.2 you can try to use the [`wdm`](https://github.com/Maher4Ever/wdm) instead of polling.
Please add the following to your Gemfile:

```ruby
require 'rbconfig'
gem 'wdm', '>= 0.1.0' if RbConfig::CONFIG['target_os'] =~ /mswin|mingw/i
```

## Usage

There are **two ways** to use Listen:

1. Block API: Call `Listen.to`/`Listen.to!` with either a single directory or multiple directories, then define the `change` callback in a block.
2. "Object" API: Create a `listener` object and use it in a chainable way.

### Block API

``` ruby
# Listen to a single directory.
Listen.to('dir/path/to/listen', :filter => /\.rb$/, :ignore => %r{ignored/path/}) do |modified, added, removed|
  # ...
end

# Listen to multiple directories.
Listen.to('dir/to/awesome_app', 'dir/to/other_app', :filter => /\.rb$/, :latency => 0.1) do |modified, added, removed|
  # ...
end
```

### "Object" API

``` ruby
listener = Listen.to('dir/path/to/listen')
listener = listener.ignore(%r{^ignored/path/})
listener = listener.filter(/\.rb$/)
listener = listener.latency(0.5)
listener = listener.force_polling(true)
listener = listener.polling_fallback_message(false)
listener = listener.force_adapter(Listen::Adapters::Linux)
listener = listener.change(&callback)
listener.start
```

**Note**: All the "Object" API methods except `start`/`start!` return the listener
and are thus chainable:

``` ruby
Listen.to('dir/path/to/listen')
      .ignore(%r{^ignored/path/})
      .filter(/\.rb$/)
      .latency(0.5)
      .force_polling(true)
      .polling_fallback_message('custom message')
      .change(&callback)
      .start
```

### Pause/Unpause

Listener can also easily be paused/unpaused:

``` ruby
listener = Listen.to('dir/path/to/listen')
listener.start   # non-blocking mode
listener.pause   # stop listening to changes
listener.paused? # => true
listener.unpause # start listening to changes again
listener.stop    # stop completely the listener
```

## Changes callback

Changes to the listened-to directories gets reported back to the user in a callback.
The registered callback gets invoked, when there are changes, with **three** parameters:
`modified_paths`, `added_paths` and `removed_paths` in that particular order.

You can register a callback in two ways. The first way is by passing a block when calling
the `Listen.to`/`Listen.to!` method or when initializing a listener object:

```ruby
Listen.to('path/to/app') do |modified, added, removed|
  # This block will be called when there are changes.
end

# or ...

listener = Listen::Listener.new('path/to/app') do |modified, added, removed|
  # This block will be called when there are changes.
end

```

The second way to register a callback is by calling the `#change` method on a
listener passing it a block:

```ruby
# Create a callback
callback = Proc.new do |modified, added, removed|
  # This proc will be called when there are changes.
end

listener = Listen.to('dir')
listener.change(&callback) # convert the callback to a block and register it

listener.start
```

### Paths in callbacks

Listeners invoke callbacks passing them absolute paths by default:

```ruby
# Assume someone changes the 'style.css' file in '/home/user/app/css' after creating
# the listener.
Listen.to('/home/user/app/css') do |modified, added, removed|
  modified.inspect # => ['/home/user/app/css/style.css']
end
```

#### Relative paths in callbacks

When creating a listener for a **single** path (more specifically a `Listen::Listener` instance),
you can pass `:relative_paths => true` as an option to get relative paths in
your callback:

```ruby
# Assume someone changes the 'style.css' file in '/home/user/app/css' after creating
# the listener.
Listen.to('/home/user/app/css', :relative_paths => true) do |modified, added, removed|
  modified.inspect # => ['style.css']
end
```

Passing the `:relative_paths => true` option won't work when listening to multiple
directories:

```ruby
# Assume someone changes the 'style.css' file in '/home/user/app/css' after creating
# the listener.
Listen.to('/home/user/app/css', '/home/user/app/js', :relative_paths => true) do |modified, added, removed|
  modified.inspect # => ['/home/user/app/css/style.css']
end
```

## Options

All the following options can be set through the `Listen.to`/`Listen.to!` params
or via ["Object" API](#object-api) methods:

```ruby
:ignore => %r{app/CMake/}, /\.pid$/           # Ignore a list of paths (root directory or sub-dir)
                                              # default: See DEFAULT_IGNORED_DIRECTORIES and DEFAULT_IGNORED_EXTENSIONS in Listen::DirectoryRecord

:filter => /\.rb$/, /\.coffee$/               # Filter files to listen to via a regexps list.
                                              # default: none

:latency => 0.5                               # Set the delay (**in seconds**) between checking for changes
                                              # default: 0.25 sec (1.0 sec for polling)

:force_adapter => Listen::Adapters::Linux     # Force the use of a particular adapter class
                                              # default: none

:force_polling => true                        # Force the use of the polling adapter
                                              # default: none

:polling_fallback_message => 'custom message' # Set a custom polling fallback message (or disable it with false)
                                              # default: "Listen will be polling for changes. Learn more at https://github.com/guard/listen#polling-fallback."

:relative_paths => true                       # Enable the use of relative paths in the callback.
                                              # default: false
```

### Note on the patterns for ignoring and filtering paths

Just like the unix convention of beginning absolute paths with the
directory-separator (forward slash `/` in unix) and with no prefix for relative paths,
Listen doesn't prefix relative paths (to the watched directory) with a directory-separator.

Therefore make sure _NOT_ to prefix your regexp-patterns for filtering or ignoring paths
with a directory-separator, otherwise they won't work as expected.

As an example: to ignore the `build` directory in a C-project, use `%r{build/}`
and not `%r{/build/}`.

Use `#filter!` and `#ignore!` methods to overwrites default patterns.

## Blocking listening to changes

Calling `Listen.to` with a block doesn't block the current thread. If you want
to block the current thread instead until the listener is stopped (which needs
to be done from another thread), you can use `Listen.to!`.

Similarly, if you're using the "Object" API, you can use `#start!` instead of `#start` to block the
current thread until the listener is stopped.

Here is an example of using a listener in the blocking mode:

```ruby
Listen.to!('dir/path/to/listen') # block execution

# Code here will not run until the listener is stopped

```

Here is an example of using a listener started with the "Object" API in blocking mode:

```ruby
listener = Listen.to('dir/path/to/listen')
listener.start! # block execution

# Code here will not run until the listener is stopped

```

**Note**: Using the `Listen.to!` helper-method with or without a callback-block
will always start the listener right away and block execution of the current thread.

## Listen adapters

The Listen gem has a set of adapters to notify it when there are changes.
There are 4 OS-specific adapters to support Mac, Linux, *BSD and Windows.
These adapters are fast as they use some system-calls to implement the notifying function.

There is also a polling adapter which is a cross-platform adapter and it will
work on any system. This adapter is unfortunately slower than the rest of the adapters.

The Listen gem will choose the best and working adapter for your machine automatically. If you
want to force the use of the polling adapter, either use the `:force_polling` option
while initializing the listener or call the `#force_polling` method on your listener
before starting it.

It is also possible to force the use of a particular adapter, by using the `:force_adapter`
option.  This option skips the usual adapter choosing mechanism and uses the given
adapter class instead.  The adapter choosing mechanism requires write permission
to your watched directories and will needlessly load code, which isn't always desirable.

## Polling fallback

When a OS-specific adapter doesn't work the Listen gem automatically falls back to the polling adapter.
Here are some things you could try to avoid the polling fallback:

* [Update your Dropbox client](http://www.dropbox.com/downloading) (if used).
* Increase latency. (Please [open an issue](https://github.com/guard/listen/issues/new)
if you think that default is too low.)
* Move or rename the listened folder.
* Update/reboot your OS.

If your application keeps using the polling-adapter and you can't figure out why, feel free to [open an issue](https://github.com/guard/listen/issues/new) (and be sure to [give all the details](https://github.com/guard/listen/blob/master/CONTRIBUTING.md)).

## Development [![Dependency Status](https://gemnasium.com/guard/listen.png?branch=master)](https://gemnasium.com/guard/listen)

* Documentation hosted at [RubyDoc](http://rubydoc.info/github/guard/listen/master/frames).
* Source hosted at [GitHub](https://github.com/guard/listen).

Pull requests are very welcome! Please try to follow these simple rules if applicable:

* Please create a topic branch for every separate change you make.
* Make sure your patches are well tested. All specs must pass on [Travis CI](https://travis-ci.org/guard/listen).
* Update the [Yard](http://yardoc.org/) documentation.
* Update the [README](https://github.com/guard/listen/blob/master/README.md).
* Update the [CHANGELOG](https://github.com/guard/listen/blob/master/CHANGELOG.md) for noteworthy changes (don't forget to run `bundle exec pimpmychangelog` and watch the magic happen)!
* Please **do not change** the version number.

For questions please join us in our [Google group](http://groups.google.com/group/guard-dev) or on
`#guard` (irc.freenode.net).

## Acknowledgments

* [Michael Kessler (netzpirat)][] for having written the [initial specs](https://github.com/guard/listen/commit/1e457b13b1bb8a25d2240428ce5ed488bafbed1f).
* [Travis Tilley (ttilley)][] for this awesome work on [fssm][] & [rb-fsevent][].
* [Nathan Weizenbaum (nex3)][] for [rb-inotify][], a thorough inotify wrapper.
* [Mathieu Arnold (mat813)][] for [rb-kqueue][], a simple kqueue wrapper.
* [stereobooster][] for [rb-fchange][], windows support wouldn't exist without him.
* [Yehuda Katz (wycats)][] for [vigilo][], that has been a great source of inspiration.

## Authors

* [Thibaud Guillaume-Gentil][] ([@thibaudgg](http://twitter.com/thibaudgg))
* [Maher Sallam][] ([@mahersalam](http://twitter.com/mahersalam))

## Contributors

[https://github.com/guard/listen/contributors](https://github.com/guard/listen/contributors)

[Thibaud Guillaume-Gentil]: https://github.com/thibaudgg
[Maher Sallam]: https://github.com/Maher4Ever
[Michael Kessler (netzpirat)]: https://github.com/netzpirat
[Travis Tilley (ttilley)]: https://github.com/ttilley
[fssm]: https://github.com/ttilley/fssm
[rb-fsevent]: https://github.com/thibaudgg/rb-fsevent
[Mathieu Arnold (mat813)]: https://github.com/mat813
[Nathan Weizenbaum (nex3)]: https://github.com/nex3
[rb-inotify]: https://github.com/nex3/rb-inotify
[stereobooster]: https://github.com/stereobooster
[rb-fchange]: https://github.com/stereobooster/rb-fchange
[rb-kqueue]: https://github.com/mat813/rb-kqueue
[Yehuda Katz (wycats)]: https://github.com/wycats
[vigilo]: https://github.com/wycats/vigilo
# mongoid-rspec

[![Build Status][travis_badge]][travis]
[![Gem Version][rubygems_badge]][rubygems]
[![Code Climate][codeclimate_badge]][codeclimate]

mongoid-rspec provides a collection of RSpec-compatible matchers that help to test mongoid documents.

## Installation

### With Mongoid 4.x

Use mongoid-rspec [2.1.0][mongoid4]

    gem 'mongoid-rspec', '~> 2.1.0'

### With Mongoid 3.x

Use mongoid-rspec [1.13.0][mongoid3].

    gem 'mongoid-rspec', '~> 1.13.0'

### With Mongoid 2.x

Use mongoid-rspec [1.4.5][mongoid2]

    gem 'mongoid-rspec', '1.4.5'

### Configuring

Drop in existing or dedicated support file in spec/support.
i.e: `spec/support/mongoid.rb`

```ruby
RSpec.configure do |config|
  config.include Mongoid::Matchers, type: :model
end
```

If you aren't using rails then you don't have to specify the type.
If you want to know why visit [the rspec documentation](https://relishapp.com/rspec/rspec-rails/docs/directory-structure).

## Matchers

### Association Matchers

```ruby
RSpec.describe User do
  it { is_expected.to have_many(:articles).with_foreign_key(:author_id).ordered_by(:title) }

  it { is_expected.to have_one(:record) }
  #can verify autobuild is set to true
  it { is_expected.to have_one(:record).with_autobuild }

  it { is_expected.to have_many :comments }

  #can also specify with_dependent to test if :dependent => :destroy/:destroy_all/:delete is set
  it { is_expected.to have_many(:comments).with_dependent(:destroy) }
  #can verify autosave is set to true
  it { is_expected.to have_many(:comments).with_autosave }

  it { is_expected.to embed_one :profile }

  it { is_expected.to have_and_belong_to_many(:children) }
  it { is_expected.to have_and_belong_to_many(:children).of_type(User) }
end

RSpec.describe Profile do
  it { is_expected.to be_embedded_in(:user).as_inverse_of(:profile) }
end

RSpec.describe Article do
  it { is_expected.to belong_to(:author).of_type(User).as_inverse_of(:articles) }
  it { is_expected.to belong_to(:author).of_type(User).as_inverse_of(:articles).with_index }
  it { is_expected.to embed_many(:comments) }
end

RSpec.describe Comment do
  it { is_expected.to be_embedded_in(:article).as_inverse_of(:comments) }
  it { is_expected.to belong_to(:user).as_inverse_of(:comments) }
end

RSpec.describe Record do
  it { is_expected.to belong_to(:user).as_inverse_of(:record) }
end

RSpec.describe Site do
  it { is_expected.to have_many(:users).as_inverse_of(:site).ordered_by(:email.asc).with_counter_cache }
end
```

### Mass Assignment Matcher

```ruby
RSpec.describe User do
  it { is_expected.to allow_mass_assignment_of(:login) }
  it { is_expected.to allow_mass_assignment_of(:email) }
  it { is_expected.to allow_mass_assignment_of(:age) }
  it { is_expected.to allow_mass_assignment_of(:password) }
  it { is_expected.to allow_mass_assignment_of(:password) }
  it { is_expected.to allow_mass_assignment_of(:role).as(:admin) }

  it { is_expected.not_to allow_mass_assignment_of(:role) }
end
```

### Validation Matchers

```ruby
RSpec.describe Site do
  it { is_expected.to validate_presence_of(:name) }
  it { is_expected.to validate_uniqueness_of(:name) }
end

RSpec.describe User do
  it { is_expected.to validate_presence_of(:login) }
  it { is_expected.to validate_uniqueness_of(:login).scoped_to(:site) }
  it { is_expected.to validate_uniqueness_of(:email).case_insensitive.with_message("is already taken") }
  it { is_expected.to validate_format_of(:login).to_allow("valid_login").not_to_allow("invalid login") }
  it { is_expected.to validate_associated(:profile) }
  it { is_expected.to validate_exclusion_of(:login).to_not_allow("super", "index", "edit") }
  it { is_expected.to validate_inclusion_of(:role).to_allow("admin", "member") }
  it { is_expected.to validate_confirmation_of(:email) }
  it { is_expected.to validate_presence_of(:age).on(:create, :update) }
  it { is_expected.to validate_numericality_of(:age).on(:create, :update) }
  it { is_expected.to validate_inclusion_of(:age).to_allow(23..42).on([:create, :update]) }
  it { is_expected.to validate_presence_of(:password).on(:create) }
  it { is_expected.to validate_presence_of(:provider_uid).on(:create) }
  it { is_expected.to validate_inclusion_of(:locale).to_allow([:en, :ru]) }
end

RSpec.describe Article do
  it { is_expected.to validate_length_of(:title).within(8..16) }
end

RSpec.describe Profile do
  it { is_expected.to validate_numericality_of(:age).greater_than(0) }
end

RSpec.describe MovieArticle do
  it { is_expected.to validate_numericality_of(:rating).to_allow(:greater_than => 0).less_than_or_equal_to(5) }
  it { is_expected.to validate_numericality_of(:classification).to_allow(:even => true, :only_integer => true, :nil => false) }
end

RSpec.describe Person do
   # in order to be able to use the custom_validate matcher, the custom validator class (in this case SsnValidator)
   # should redefine the kind method to return :custom, i.e. "def self.kind() :custom end"
  it { is_expected.to custom_validate(:ssn).with_validator(SsnValidator) }
end
```

### Accepts Nested Attributes Matcher

```ruby
RSpec.describe User do
  it { is_expected.to accept_nested_attributes_for(:articles) }
  it { is_expected.to accept_nested_attributes_for(:comments) }
end

RSpec.describe Article do
  it { is_expected.to accept_nested_attributes_for(:permalink) }
end
```

### Index Matcher

```ruby
RSpec.describe Article do
  it { is_expected.to have_index_for(published: 1) }
  it { is_expected.to have_index_for(title: 1).with_options(unique: true, background: true) }
end

RSpec.describe Profile do
  it { is_expected.to have_index_for(first_name: 1, last_name: 1) }
end

Rspec.describe Log do
  it { is_expected.to have_index_for(created_at: 1).with_options(bucket_size: 100, expire_after_seconds: 3600) }
end
```

### Others

```ruby
RSpec.describe User do
  it { is_expected.to have_fields(:email, :login) }
  it { is_expected.to have_field(:s).with_alias(:status) }
  it { is_expected.to have_fields(:birthdate, :registered_at).of_type(DateTime) }

  # if you're declaring 'include Mongoid::Timestamps'
  # or any of 'include Mongoid::Timestamps::Created' and 'Mongoid::Timestamps::Updated'
  it { is_expected.to be_timestamped_document }
  it { is_expected.to be_timestamped_document.with(:created) }
  it { is_expected.not_to be_timestamped_document.with(:updated) }

  it { is_expected.to be_versioned_document } # if you're declaring `include Mongoid::Versioning`
  it { is_expected.to be_paranoid_document } # if you're declaring `include Mongoid::Paranoia`
  it { is_expected.to be_multiparameted_document } # if you're declaring `include Mongoid::MultiParameterAttributes`
end

RSpec.describe Log do
  it { is_expected.to be_stored_in :logs }
  it { is_expected.to be_dynamic_document }
end

RSpec.describe Article do
  it { is_expected.to have_field(:published).of_type(Boolean).with_default_value_of(false) }
  it { is_expected.to have_field(:allow_comments).of_type(Boolean).with_default_value_of(true) }
  it { is_expected.not_to have_field(:allow_comments).of_type(Boolean).with_default_value_of(false) }
  it { is_expected.not_to have_field(:number_of_comments).of_type(Integer).with_default_value_of(1) }
end
```

## Known issues

accept_nested_attributes_for matcher must test options [issue 91](https://github.com/mongoid-rspec/mongoid-rspec/issues/91).

## Acknowledgement

Thanks to [Durran Jordan][durran] for providing the changes necessary to make
this compatible with mongoid 2.0.0.rc, and for other [contributors](https://github.com/mongoid-rspec/mongoid-rspec/contributors)
to this project.

[durran]: https://github.com/durran
[mongoid2]: http://rubygems.org/gems/mongoid-rspec/versions/1.4.5
[mongoid3]: http://rubygems.org/gems/mongoid-rspec/versions/1.13.0
[mongoid4]: http://rubygems.org/gems/mongoid-rspec/versions/2.0.0

[travis_badge]: http://img.shields.io/travis/mongoid-rspec/mongoid-rspec.svg?style=flat
[travis]: https://travis-ci.org/mongoid-rspec/mongoid-rspec

[rubygems_badge]: http://img.shields.io/gem/v/mongoid-rspec.svg?style=flat
[rubygems]: http://rubygems.org/gems/mongoid-rspec

[codeclimate_badge]: http://img.shields.io/codeclimate/github/mongoid-rspec/mongoid-rspec.svg?style=flat
[codeclimate]: https://codeclimate.com/github/mongoid-rspec/mongoid-rspec
= Action Pack -- From request to response

Action Pack is a framework for handling and responding to web requests. It
provides mechanisms for *routing* (mapping request URLs to actions), defining
*controllers* that implement actions, and generating responses by rendering
*views*, which are templates of various formats. In short, Action Pack
provides the view and controller layers in the MVC paradigm.

It consists of several modules:

* Action Dispatch, which parses information about the web request, handles
  routing as defined by the user, and does advanced processing related to HTTP
  such as MIME-type negotiation, decoding parameters in POST, PATCH, or PUT bodies,
  handling HTTP caching logic, cookies and sessions.

* Action Controller, which provides a base controller class that can be
  subclassed to implement filters and actions to handle requests. The result
  of an action is typically content generated from views.

With the Ruby on Rails framework, users only directly interface with the
Action Controller module. Necessary Action Dispatch functionality is activated
by default and Action View rendering is implicitly triggered by Action
Controller. However, these modules are designed to function on their own and
can be used outside of Rails.


== Download and installation

The latest version of Action Pack can be installed with RubyGems:

  % [sudo] gem install actionpack

Source code can be downloaded as part of the Rails project on GitHub

* https://github.com/rails/rails/tree/4-2-stable/actionpack


== License

Action Pack is released under the MIT license:

* http://www.opensource.org/licenses/MIT


== Support

API documentation is at

* http://api.rubyonrails.org

Bug reports can be filed for the Ruby on Rails project here:

* https://github.com/rails/rails/issues

Feature requests should be discussed on the rails-core mailing list here:

* https://groups.google.com/forum/?fromgroups#!forum/rubyonrails-core

# Project: Builder

## Goal

Provide a simple way to create XML markup and data structures.

## Classes

Builder::XmlMarkup:: Generate XML markup notation
Builder::XmlEvents:: Generate XML events (i.e. SAX-like)

**Notes:**

* An <tt>Builder::XmlTree</tt> class to generate XML tree
  (i.e. DOM-like) structures is also planned, but not yet implemented.
  Also, the events builder is currently lagging the markup builder in
  features.

## Usage

```ruby
  require 'rubygems'
  require_gem 'builder', '~> 2.0'

  builder = Builder::XmlMarkup.new
`  xml = builder.person { |b| b.name("Jim"); b.phone("555-1234") }
  xml #=> <person><name>Jim</name><phone>555-1234</phone></person>
```

or

```ruby
  require 'rubygems'
  require_gem 'builder'

  builder = Builder::XmlMarkup.new(:target=>STDOUT, :indent=>2)
  builder.person { |b| b.name("Jim"); b.phone("555-1234") }
  #
  # Prints:
  # <person>
  #   <name>Jim</name>
  #   <phone>555-1234</phone>
  # </person>
```

## Compatibility

### Version 2.0.0 Compatibility Changes

Version 2.0.0 introduces automatically escaped attribute values for
the first time.  Versions prior to 2.0.0 did not insert escape
characters into attribute values in the XML markup.  This allowed
attribute values to explicitly reference entities, which was
occasionally used by a small number of developers.  Since strings
could always be explicitly escaped by hand, this was not a major
restriction in functionality.

However, it did surprise most users of builder.  Since the body text is
normally escaped, everybody expected the attribute values to be
escaped as well.  Escaped attribute values were the number one support
request on the 1.x Builder series.

Starting with Builder version 2.0.0, all attribute values expressed as
strings will be processed and the appropriate characters will be
escaped (e.g. "&" will be translated to "&amp;").  Attribute values
that are expressed as Symbol values will not be processed for escaped
characters and will be unchanged in output. (Yes, this probably counts
as Symbol abuse, but the convention is convenient and flexible).

Example:

```ruby
  xml = Builder::XmlMarkup.new
  xml.sample(:escaped=>"This&That", :unescaped=>:"Here&amp;There")
  xml.target!  =>
    <sample escaped="This&amp;That" unescaped="Here&amp;There"/>
```

### Version 1.0.0 Compatibility Changes

Version 1.0.0 introduces some changes that are not backwards
compatible with earlier releases of builder.  The main areas of
incompatibility are:

* Keyword based arguments to +new+ (rather than positional based).  It
  was found that a developer would often like to specify indentation
  without providing an explicit target, or specify a target without
  indentation.  Keyword based arguments handle this situation nicely.

* Builder must now be an explicit target for markup tags.  Instead of
  writing

```ruby
    xml_markup = Builder::XmlMarkup.new
    xml_markup.div { strong("text") }
```

  you need to write

```ruby
    xml_markup = Builder::XmlMarkup.new
    xml_markup.div { xml_markup.strong("text") }
```

* The builder object is passed as a parameter to all nested markup
  blocks.  This allows you to create a short alias for the builder
  object that can be used within the block.  For example, the previous
  example can be written as:

```ruby
    xml_markup = Builder::XmlMarkup.new
    xml_markup.div { |xml| xml.strong("text") }
```

* If you have both a pre-1.0 and a post-1.0 gem of builder installed,
  you can choose which version to use through the RubyGems
  +require_gem+ facility.

```ruby
    require_gem 'builder', "~> 0.0"   # Gets the old version
    require_gem 'builder', "~> 1.0"   # Gets the new version
```

## Features

* XML Comments are supported ...

```ruby
    xml_markup.comment! "This is a comment"
      #=>  <!-- This is a comment -->
```

* XML processing instructions are supported ...

```ruby
    xml_markup.instruct! :xml, :version=>"1.0", :encoding=>"UTF-8"
      #=>  <?xml version="1.0" encoding="UTF-8"?>
```

  If the processing instruction is omitted, it defaults to "xml".
  When the processing instruction is "xml", the defaults attributes
  are:

  <b>version</b>: 1.0
  <b>encoding</b>: "UTF-8"

  (NOTE: if the encoding is set to "UTF-8" and $KCODE is set to
  "UTF8", then Builder will emit UTF-8 encoded strings rather than
  encoding non-ASCII characters as entities.)

* XML entity declarations are now supported to a small degree.

```ruby
    xml_markup.declare! :DOCTYPE, :chapter, :SYSTEM, "../dtds/chapter.dtd"
      #=>  <!DOCTYPE chapter SYSTEM "../dtds/chapter.dtd">
```

  The parameters to a declare! method must be either symbols or
  strings. Symbols are inserted without quotes, and strings are
  inserted with double quotes.  Attribute-like arguments in hashes are
  not allowed.

  If you need to have an argument to declare! be inserted without
  quotes, but the argument does not conform to the typical Ruby
  syntax for symbols, then use the :"string" form to specify a symbol.

  For example:

```ruby
    xml_markup.declare! :ELEMENT, :chapter, :"(title,para+)"
      #=>  <!ELEMENT chapter (title,para+)>
```

  Nested entity declarations are allowed.  For example:

```ruby
    @xml_markup.declare! :DOCTYPE, :chapter do |x|
      x.declare! :ELEMENT, :chapter, :"(title,para+)"
      x.declare! :ELEMENT, :title, :"(#PCDATA)"
      x.declare! :ELEMENT, :para, :"(#PCDATA)"
    end

    #=>

    <!DOCTYPE chapter [
      <!ELEMENT chapter (title,para+)>
      <!ELEMENT title (#PCDATA)>
      <!ELEMENT para (#PCDATA)>
    ]>
```

* Some support for XML namespaces is now available.  If the first
  argument to a tag call is a symbol, it will be joined to the tag to
  produce a namespace:tag combination.  It is easier to show this than
  describe it.

```ruby
   xml.SOAP :Envelope do ... end
```

  Just put a space before the colon in a namespace to produce the
  right form for builder (e.g. "<tt>SOAP:Envelope</tt>" =>
  "<tt>xml.SOAP :Envelope</tt>")

* String attribute values are <em>now</em> escaped by default by
  Builder (<b>NOTE:</b> this is _new_ behavior as of version 2.0).

  However, occasionally you need to use entities in attribute values.
  Using a symbol (rather than a string) for an attribute value will
  cause Builder to not run its quoting/escaping algorithm on that
  particular value.

  (<b>Note:</b> The +escape_attrs+ option for builder is now
  obsolete).

  Example:

```ruby
    xml = Builder::XmlMarkup.new
    xml.sample(:escaped=>"This&That", :unescaped=>:"Here&amp;There")
    xml.target!  =>
      <sample escaped="This&amp;That" unescaped="Here&amp;There"/>
```

* UTF-8 Support

  Builder correctly translates UTF-8 characters into valid XML.  (New
  in version 2.0.0).  Thanks to Sam Ruby for the translation code.

  You can get UTF-8 encoded output by making sure that the XML
  encoding is set to "UTF-8" and that the $KCODE variable is set to
  "UTF8".

```ruby
    $KCODE = 'UTF8'
    xml = Builder::Markup.new
    xml.instruct!(:xml, :encoding => "UTF-8")
    xml.sample("Iñtërnâtiônàl")
    xml.target!  =>
      "<sample>Iñtërnâtiônàl</sample>"
```

## Links

| Description | Link |
| :----: | :----: |
| Documents           | http://builder.rubyforge.org/ |
| Github Clone        | git://github.com/jimweirich/builder.git |
| Issue / Bug Reports | https://github.com/jimweirich/builder/issues?state=open |

## Contact

| Description | Value                  |
| :----:      | :----:                 |
| Author      | Jim Weirich            |
| Email       | jim.weirich@gmail.com  |
| Home Page   | http://onestepback.org |
| License     | MIT Licence (http://www.opensource.org/licenses/mit-license.html) |
= Loofah {<img src="https://travis-ci.org/flavorjones/loofah.png?branch=master" alt="Build Status" />}[https://travis-ci.org/flavorjones/loofah]

* https://github.com/flavorjones/loofah
* http://rubydoc.info/github/flavorjones/loofah/master/frames
* http://librelist.com/browser/loofah

== Description

Loofah is a general library for manipulating and transforming HTML/XML
documents and fragments. It's built on top of Nokogiri and libxml2, so
it's fast and has a nice API.

Loofah excels at HTML sanitization (XSS prevention). It includes some
nice HTML sanitizers, which are based on HTML5lib's whitelist, so it
most likely won't make your codes less secure. (These statements have
not been evaluated by Netexperts.)

ActiveRecord extensions for sanitization are available in the
`loofah-activerecord` gem (see
https://github.com/flavorjones/loofah-activerecord).

== Features

* Easily write custom scrubbers for HTML/XML leveraging the sweetness of Nokogiri (and HTML5lib's whitelists).
* Common HTML sanitizing tasks are built-in:
  * _Strip_ unsafe tags, leaving behind only the inner text.
  * _Prune_ unsafe tags and their subtrees, removing all traces that they ever existed.
  * _Escape_ unsafe tags and their subtrees, leaving behind lots of <tt>&lt;</tt> and <tt>&gt;</tt> entities.
  * _Whitewash_ the markup, removing all attributes and namespaced nodes.
* Common HTML transformation tasks are built-in:
  * Add the _nofollow_ attribute to all hyperlinks.
* Format markup as plain text, with or without sensible whitespace handling around block elements.
* Replace Rails's +strip_tags+ and +sanitize+ view helper methods.

== Compare and Contrast

Loofah is one of two known Ruby XSS/sanitization solutions that
guarantees well-formed and valid markup (the other is Sanitize, which
also uses Nokogiri).

Loofah works on XML, XHTML and HTML documents.

Also, it's pretty fast. Here is a benchmark comparing Loofah to other
commonly-used libraries (ActionView, Sanitize, HTML5lib and HTMLfilter):

* https://gist.github.com/170193

Lastly, Loofah is extensible. It's super-easy to write your own custom
scrubbers for whatever document manipulation you need. You don't like
the built-in scrubbers? Build your own, like a boss.

== The Basics

Loofah wraps Nokogiri[http://nokogiri.org] in a loving
embrace. Nokogiri[http://nokogiri.org] is an excellent HTML/XML
parser. If you don't know how Nokogiri[http://nokogiri.org] works, you
might want to pause for a moment and go check it out. I'll wait.

Loofah presents the following classes:

* Loofah::HTML::Document and Loofah::HTML::DocumentFragment
* Loofah::XML::Document and Loofah::XML::DocumentFragment
* Loofah::Scrubber

The documents and fragments are subclasses of the similar Nokogiri classes.

The Scrubber represents the document manipulation, either by wrapping
a block,

  span2div = Loofah::Scrubber.new do |node|
    node.name = "div" if node.name == "span"
  end

or by implementing a method.

=== Side Note: Fragments vs Documents

Generally speaking, unless you expect to have a DOCTYPE and a single
root node, you don't have a *document*, you have a *fragment*. For
HTML, another rule of thumb is that *documents* have +html+ and +body+
tags, and *fragments* usually do not.

HTML fragments should be parsed with Loofah.fragment. The result won't
be wrapped in +html+ or +body+ tags, won't have a DOCTYPE declaration,
+head+ elements will be silently ignored, and multiple root nodes are
allowed.

XML fragments should be parsed with Loofah.xml_fragment. The result
won't have a DOCTYPE declaration, and multiple root nodes are allowed.

HTML documents should be parsed with Loofah.document. The result will
have a DOCTYPE declaration, along with +html+, +head+ and +body+ tags.

XML documents should be parsed with Loofah.xml_document. The result
will have a DOCTYPE declaration and a single root node.

=== Loofah::HTML::Document and Loofah::HTML::DocumentFragment

These classes are subclasses of Nokogiri::HTML::Document and
Nokogiri::HTML::DocumentFragment, so you get all the markup
fixer-uppery and API goodness of Nokogiri.

The module methods Loofah.document and Loofah.fragment will parse an
HTML document and an HTML fragment, respectively.

  Loofah.document(unsafe_html).is_a?(Nokogiri::HTML::Document)         # => true
  Loofah.fragment(unsafe_html).is_a?(Nokogiri::HTML::DocumentFragment) # => true

Loofah injects a +scrub!+ method, which takes either a symbol (for
built-in scrubbers) or a Loofah::Scrubber object (for custom
scrubbers), and modifies the document in-place.

Loofah overrides +to_s+ to return HTML:

  unsafe_html = "ohai! <div>div is safe</div> <script>but script is not</script>"

  doc = Loofah.fragment(unsafe_html).scrub!(:strip)
  doc.to_s    # => "ohai! <div>div is safe</div> "

and +text+ to return plain text:

  doc.text    # => "ohai! div is safe "

Also, +to_text+ is available, which does the right thing with
whitespace around block-level elements.

  doc = Loofah.fragment("<h1>Title</h1><div>Content</div>")
  doc.text    # => "TitleContent"           # probably not what you want
  doc.to_text # => "\nTitle\n\nContent\n"   # better

=== Loofah::XML::Document and Loofah::XML::DocumentFragment

These classes are subclasses of Nokogiri::XML::Document and
Nokogiri::XML::DocumentFragment, so you get all the markup
fixer-uppery and API goodness of Nokogiri.

The module methods Loofah.xml_document and Loofah.xml_fragment will
parse an XML document and an XML fragment, respectively.

  Loofah.xml_document(bad_xml).is_a?(Nokogiri::XML::Document)         # => true
  Loofah.xml_fragment(bad_xml).is_a?(Nokogiri::XML::DocumentFragment) # => true

=== Nodes and NodeSets

Nokogiri::XML::Node and Nokogiri::XML::NodeSet also get a +scrub!+
method, which makes it easy to scrub subtrees.

The following code will apply the +employee_scrubber+ only to the
+employee+ nodes (and their subtrees) in the document:

  Loofah.xml_document(bad_xml).xpath("//employee").scrub!(employee_scrubber)

And this code will only scrub the first +employee+ node and its subtree:

  Loofah.xml_document(bad_xml).at_xpath("//employee").scrub!(employee_scrubber)

=== Loofah::Scrubber

A Scrubber wraps up a block (or method) that is run on a document node:

  # change all <span> tags to <div> tags
  span2div = Loofah::Scrubber.new do |node|
    node.name = "div" if node.name == "span"
  end

This can then be run on a document:

  Loofah.fragment("<span>foo</span><p>bar</p>").scrub!(span2div).to_s
  # => "<div>foo</div><p>bar</p>"

Scrubbers can be run on a document in either a top-down traversal (the
default) or bottom-up. Top-down scrubbers can optionally return
Scrubber::STOP to terminate the traversal of a subtree. Read below and
in the Loofah::Scrubber class for more detailed usage.

Here's an XML example:

  # remove all <employee> tags that have a "deceased" attribute set to true
  bring_out_your_dead = Loofah::Scrubber.new do |node|
    if node.name == "employee" and node["deceased"] == "true"
      node.remove
      Loofah::Scrubber::STOP # don't bother with the rest of the subtree
    end
  end
  Loofah.xml_document(File.read('plague.xml')).scrub!(bring_out_your_dead)

=== Built-In HTML Scrubbers

Loofah comes with a set of sanitizing scrubbers that use HTML5lib's
whitelist algorithm:

  doc.scrub!(:strip)       # replaces unknown/unsafe tags with their inner text
  doc.scrub!(:prune)       #  removes unknown/unsafe tags and their children
  doc.scrub!(:escape)      #  escapes unknown/unsafe tags, like this: &lt;script&gt;
  doc.scrub!(:whitewash)   #  removes unknown/unsafe/namespaced tags and their children,
                           #          and strips all node attributes

Loofah also comes with some common transformation tasks: 

  doc.scrub!(:nofollow)    #     adds rel="nofollow" attribute to links
  doc.scrub!(:unprintable) #  removes unprintable characters from text nodes

See Loofah::Scrubbers for more details and example usage.

=== Chaining Scrubbers

You can chain scrubbers:

  Loofah.fragment("<span>hello</span> <script>alert('OHAI')</script>") \
        .scrub!(:prune) \
        .scrub!(span2div).to_s
  # => "<div>hello</div> "

=== Shorthand

The class methods Loofah.scrub_fragment and Loofah.scrub_document are
shorthand.

  Loofah.scrub_fragment(unsafe_html, :prune)
  Loofah.scrub_document(unsafe_html, :prune)
  Loofah.scrub_xml_fragment(bad_xml, custom_scrubber)
  Loofah.scrub_xml_document(bad_xml, custom_scrubber)

are the same thing as (and arguably semantically clearer than):

  Loofah.fragment(unsafe_html).scrub!(:prune)
  Loofah.document(unsafe_html).scrub!(:prune)
  Loofah.xml_fragment(bad_xml).scrub!(custom_scrubber)
  Loofah.xml_document(bad_xml).scrub!(custom_scrubber)

=== View Helpers

Loofah has two "view helpers": Loofah::Helpers.sanitize and
Loofah::Helpers.strip_tags, both of which are drop-in replacements for
the Rails ActionView helpers of the same name.
These are no longer required automatically. You must require `loofah/helpers`. 

== Requirements

* Nokogiri >= 1.4.4

== Installation

Unsurprisingly:

* gem install loofah

== Support

The bug tracker is available here:

* https://github.com/flavorjones/loofah/issues

And the mailing list is on librelist:

* loofah@librelist.com / http://librelist.com

And the IRC channel is \#loofah on freenode.

== Related Links

* Nokogiri: http://nokogiri.org
* libxml2: http://xmlsoft.org
* html5lib: https://code.google.com/p/html5lib

== Authors

* {Mike Dalessio}[http://mike.daless.io] (@flavorjones[https://twitter.com/flavorjones])
* Bryan Helmkamp

Featuring code contributed by:

* Aaron Patterson
* John Barnette
* Josh Owens
* Paul Dix
* Luke Melia

And a big shout-out to Corey Innis for the name, and feedback on the API.

== Thank You

The following people have generously donated via the Pledgie[http://pledgie.com] badge on the {Loofah github page}[https://github.com/flavorjones/loofah]:

* Bill Harding

== Historical Note

This library was formerly known as Dryopteris, which was a very bad
name that nobody could spell properly.

== License

The MIT License

Copyright (c) 2009 -- 2014 by Mike Dalessio, Bryan Helmkamp

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
= Active Model -- model interfaces for Rails

Active Model provides a known set of interfaces for usage in model classes.
They allow for Action Pack helpers to interact with non-Active Record models,
for example. Active Model also helps with building custom ORMs for use outside of
the Rails framework.

Prior to Rails 3.0, if a plugin or gem developer wanted to have an object
interact with Action Pack helpers, it was required to either copy chunks of
code from Rails, or monkey patch entire helpers to make them handle objects
that did not exactly conform to the Active Record interface. This would result
in code duplication and fragile applications that broke on upgrades. Active
Model solves this by defining an explicit API. You can read more about the
API in <tt>ActiveModel::Lint::Tests</tt>.

Active Model provides a default module that implements the basic API required
to integrate with Action Pack out of the box: <tt>ActiveModel::Model</tt>.

    class Person
      include ActiveModel::Model

      attr_accessor :name, :age
      validates_presence_of :name
    end

    person = Person.new(name: 'bob', age: '18')
    person.name   # => 'bob'
    person.age    # => '18'
    person.valid? # => true

It includes model name introspections, conversions, translations and
validations, resulting in a class suitable to be used with Action Pack.
See <tt>ActiveModel::Model</tt> for more examples.

Active Model also provides the following functionality to have ORM-like
behavior out of the box:

* Add attribute magic to objects

    class Person
      include ActiveModel::AttributeMethods

      attribute_method_prefix 'clear_'
      define_attribute_methods :name, :age

      attr_accessor :name, :age

      def clear_attribute(attr)
        send("#{attr}=", nil)
      end
    end
  
    person = Person.new
    person.clear_name
    person.clear_age

  {Learn more}[link:classes/ActiveModel/AttributeMethods.html]

* Callbacks for certain operations

    class Person
      extend ActiveModel::Callbacks
      define_model_callbacks :create

      def create
        run_callbacks :create do
          # Your create action methods here
        end
      end
    end

  This generates +before_create+, +around_create+ and +after_create+
  class methods that wrap your create method.

  {Learn more}[link:classes/ActiveModel/Callbacks.html]

* Tracking value changes

    class Person
      include ActiveModel::Dirty

      define_attribute_methods :name

      def name
        @name
      end

      def name=(val)
        name_will_change! unless val == @name
        @name = val
      end

      def save
        # do persistence work
        changes_applied
      end
    end

    person = Person.new
    person.name             # => nil
    person.changed?         # => false
    person.name = 'bob'
    person.changed?         # => true
    person.changed          # => ['name']
    person.changes          # => { 'name' => [nil, 'bob'] }
    person.save
    person.name = 'robert'
    person.save
    person.previous_changes # => {'name' => ['bob, 'robert']}

  {Learn more}[link:classes/ActiveModel/Dirty.html]

* Adding +errors+ interface to objects

  Exposing error messages allows objects to interact with Action Pack
  helpers seamlessly.

    class Person

      def initialize
        @errors = ActiveModel::Errors.new(self)
      end

      attr_accessor :name
      attr_reader   :errors

      def validate!
        errors.add(:name, "cannot be nil") if name.nil?
      end

      def self.human_attribute_name(attr, options = {})
        "Name"
      end
    end
  
    person = Person.new
    person.name = nil
    person.validate!
    person.errors.full_messages
    # => ["Name cannot be nil"]

  {Learn more}[link:classes/ActiveModel/Errors.html]

* Model name introspection

    class NamedPerson
      extend ActiveModel::Naming
    end

    NamedPerson.model_name.name   # => "NamedPerson"
    NamedPerson.model_name.human  # => "Named person"

  {Learn more}[link:classes/ActiveModel/Naming.html]

* Making objects serializable

  ActiveModel::Serialization provides a standard interface for your object
  to provide +to_json+ or +to_xml+ serialization.

    class SerialPerson
      include ActiveModel::Serialization

      attr_accessor :name

      def attributes
        {'name' => name}
      end
    end

    s = SerialPerson.new
    s.serializable_hash   # => {"name"=>nil}

    class SerialPerson
      include ActiveModel::Serializers::JSON
    end

    s = SerialPerson.new
    s.to_json             # => "{\"name\":null}"

    class SerialPerson
      include ActiveModel::Serializers::Xml
    end

    s = SerialPerson.new
    s.to_xml              # => "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<serial-person...

  {Learn more}[link:classes/ActiveModel/Serialization.html]

* Internationalization (i18n) support

    class Person
      extend ActiveModel::Translation
    end

    Person.human_attribute_name('my_attribute')
    # => "My attribute"

  {Learn more}[link:classes/ActiveModel/Translation.html]

* Validation support

    class Person
      include ActiveModel::Validations

      attr_accessor :first_name, :last_name

      validates_each :first_name, :last_name do |record, attr, value|
        record.errors.add attr, 'starts with z.' if value.to_s[0] == ?z
      end
    end

    person = Person.new
    person.first_name = 'zoolander'
    person.valid?  # => false

  {Learn more}[link:classes/ActiveModel/Validations.html]

* Custom validators
  
    class HasNameValidator < ActiveModel::Validator
      def validate(record)
        record.errors[:name] = "must exist" if record.name.blank?
      end
    end

    class ValidatorPerson
      include ActiveModel::Validations
      validates_with HasNameValidator
      attr_accessor :name
    end

    p = ValidatorPerson.new
    p.valid?                  # =>  false
    p.errors.full_messages    # => ["Name must exist"]
    p.name = "Bob"
    p.valid?                  # =>  true

  {Learn more}[link:classes/ActiveModel/Validator.html]


== Download and installation

The latest version of Active Model can be installed with RubyGems:

  % [sudo] gem install activemodel

Source code can be downloaded as part of the Rails project on GitHub

* https://github.com/rails/rails/tree/4-2-stable/activemodel


== License

Active Model is released under the MIT license:

* http://www.opensource.org/licenses/MIT


== Support

API documentation is at

* http://api.rubyonrails.org

Bug reports can be filed for the Ruby on Rails project here:

* https://github.com/rails/rails/issues

Feature requests should be discussed on the rails-core mailing list here:

* https://groups.google.com/forum/?fromgroups#!forum/rubyonrails-core

# Rails Stdout Logging

Rails gem to configure your app to log to standard out.

[![Build Status](https://travis-ci.org/heroku/rails_stdout_logging.png?branch=master)](https://travis-ci.org/heroku/rails_stdout_logging)

Supports:

- Rails 3
- Rails 4



## Install

In your `Gemfile` add:

```
gem 'rails_stdout_logging'
```

Then run

```
$ bundle install`
```

You also need the `rails_serve_static_assets` gem. You can get both of them together by installing `rails_on_heroku` gem.

## Why is this needed?

By default Rails writes its logs to a file which is convenient but only you only have one log file to tail. When you start scaling your app to multiple machines or dynos then finding a single request or failure across multiple files becomes much harder. Storing logs on disk can also take down a server if the hard drive fills up. Because of these limitations: every Rails core member we talked to uses a custom logger to replace Rail's default functionality. By using the `rails_stdout_logging` gem with Heroku, we set the logger for you.

The gem `rails_stdout_logging` ensures that your logs will be sent to standard out, from there Heroku sends them to [logplex](https://github.com/heroku/logplex) so you can access them from the command line, `$ heroku logs --tail`, or from enabled addons like [papertrail](https://addons.heroku.com/papertrail). By using Heroku's logplex, you can [treat logs as event streams](http://www.12factor.net/logs).

## Why Didn't I need this before?

Why do you need to include this gem in Rails 4 and not Rails 3? Rails4 is getting rid of the concept of plugins. Before libraries were easily distributed as Gems and in the form of Engines, Rails had a folder `vendor/plugins`. Any code you put there would be initialized much like a Gem is today. This was a very simple and easy way to share and use libraries, but it wasn't very maintainable. You could use a library, and make a change locally and then deploy which makes your version incompatible from future versions. Even worse there was no concept of versioning aside from source control, so semantic versioning was out of the question. For these reasons and more Rails3 deprecated plugins. With Rails4 plugins have been removed completely. Why does this affect your app on Heroku?

In the past Heroku has used plugins as a safe way to configure your application where code was needed. While we advocate [separating config from code](http://12factor.net), this was the only option if we wanted your apps to work with no changes from you. With Rails3 Heroku will add the asset serving and standardout logging plugins to your app automatically. With Rails4, Heroku needs you to add these libraries to your Gemfile.

It is important to note that unlike Gems, plugins do not have a dependency resolution phase like what happens when you run `bundle install`. Heroku does not and will not add anything to your Gemfile on compilation.

## Tests

Since we're playing with stdout we need to capture stdout. If you want to use the non captured version use `DEBUG_STDOUT` instead. The `puts` method should still behave as you expect.

We're using appraisal to build multiple gemfiles for different versions of Rails.

You can run all tests by running

```
$ bundle exec rake appraisal test
```


## The Future

We will be working with Rails and the Rails core team to make future versions of Rails work on Heroku out of the box. Until then you'll need to add this gem to your project.


ruby-unf_ext
============

Synopsis
--------

* Unicode Normalization Form support library for CRuby

Description
-----------

* Normalizes UTF-8 strings into and from NFC, NFD, NFKC or NFKD

        # For bulk conversion
        normalizer = UNF::Normalizer.new
        a_bunch_of_strings.map! { |string|
          normalizer.normalize(string, :nfc) #=> string in NFC
        }

* Compliant with Unicode 6.0

Requirement
-----------

* Ruby 1.8.7+, 1.9.2+

* C++ compiler and libstdc++

Installation
------------

	gem install unf_ext

Or:

    ruby extconf.rb && make && make install

Development Resources
---------------------

* http://sourceforge.jp/projects/unf/
* http://sourceforge.jp/ticket/newticket.php?group_id=5256

    For issues regarding files under the directory `unf`, please
    contact this upstream.

* https://github.com/knu/ruby-unf_ext

    The development site and the repository.

License
-------

Copyright (c) 2010 Takeru Ohta
Copyright (c) 2011-2015 Akinori MUSHA

Licensed under the MIT license.
See `LICENSE` for details.
# Html2haml

[![Build Status](https://travis-ci.org/haml/html2haml.svg?branch=master)](https://travis-ci.org/haml/html2haml)
[![Code Climate](https://codeclimate.com/github/haml/html2haml.svg)](https://codeclimate.com/github/haml/html2haml)
[![Gem Version](https://badge.fury.io/rb/html2haml.svg)](https://rubygems.org/gems/html2haml)

Html2haml, not surprisingly, converts HTML to Haml. It works on HTML with
embedded ERB tags as well as plain old HTML.

## Installation

Add this line to your application's Gemfile:

    gem 'html2haml'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install html2haml

## Usage


### To convert a project from .erb to .haml

If your system has `sed` and `xargs` available and none of your .erb file names
have whitespace in them, you can convert all your templates like so:

    find . -name \*.erb -print | sed 'p;s/.erb$/.haml/' | xargs -n2 html2haml

If some of your file names have whitespace or you need finer-grained control
over the process, you can convert your files using `gsed` or multi-line script
techniques discussed [here](http://stackoverflow.com/questions/17576814/).


### Documentation

#### About version 2.0

Html2haml 2.0 differs from 1.x primarily in that it uses Nokgiri as its HTML
parser rather than Hpricot. At the current time however, there are some
problems running Html2haml 2.0 on JRuby due to differences in the way the Java
version of Nokogiri parses HTML. If you are using JRuby you may wish to run
HTML2Haml on MRI or use a 1.x version until these problems have been resolved.

#### Options

Here are the options currently available to Html2haml:

See `html2haml --help`:

    Usage: html2haml [options] [INPUT] [OUTPUT]

    Description: Transforms an HTML file into corresponding Haml code.

    Options:
        -e, --erb                        Parse ERb tags.
            --no-erb                     Don't parse ERb tags.
            --html-attributes            Use HTML style attributes instead of Ruby hash style.
            --ruby19-attributes          Use Ruby 1.9-style attributes when possible.
        -E ex[:in]                       Specify the default external and internal character encodings.
        -s, --stdin                      Read input from standard input instead of an input file
            --trace                      Show a full traceback on error
            --unix-newlines              Use Unix-style newlines in written files.
        -?, -h, --help                   Show this message
        -v, --version                    Print version

## License

Copyright (c) 2006-2014 Hampton Catlin, Natalie Weizenbaum and Norman Clarke

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# RSpec Expectations [![Build Status](https://secure.travis-ci.org/rspec/rspec-expectations.svg?branch=master)](http://travis-ci.org/rspec/rspec-expectations) [![Code Climate](https://codeclimate.com/github/rspec/rspec-expectations.svg)](https://codeclimate.com/github/rspec/rspec-expectations)

RSpec::Expectations lets you express expected outcomes on an object in an
example.

    expect(account.balance).to eq(Money.new(37.42, :USD))

## Install

If you want to use rspec-expectations with rspec, just install the rspec gem
and RubyGems will also install rspec-expectations for you (along with
rspec-core and rspec-mocks):

    gem install rspec

Want to run against the `master` branch? You'll need to include the dependent
RSpec repos as well. Add the following to your `Gemfile`:

```ruby
%w[rspec-core rspec-expectations rspec-mocks rspec-support].each do |lib|
  gem lib, :git => "git://github.com/rspec/#{lib}.git", :branch => 'master'
end
```

If you want to use rspec-expectations with another tool, like Test::Unit,
Minitest, or Cucumber, you can install it directly:

    gem install rspec-expectations

## Basic usage

Here's an example using rspec-core:

```ruby
RSpec.describe Order do
  it "sums the prices of the items in its line items" do
    order = Order.new
    order.add_entry(LineItem.new(:item => Item.new(
      :price => Money.new(1.11, :USD)
    )))
    order.add_entry(LineItem.new(:item => Item.new(
      :price => Money.new(2.22, :USD),
      :quantity => 2
    )))
    expect(order.total).to eq(Money.new(5.55, :USD))
  end
end
```

The `describe` and `it` methods come from rspec-core.  The `Order`, `LineItem`, `Item` and `Money` classes would be from _your_ code. The last line of the example
expresses an expected outcome. If `order.total == Money.new(5.55, :USD)`, then
the example passes. If not, it fails with a message like:

    expected: #<Money @value=5.55 @currency=:USD>
         got: #<Money @value=1.11 @currency=:USD>

## Built-in matchers

### Equivalence

```ruby
expect(actual).to eq(expected)  # passes if actual == expected
expect(actual).to eql(expected) # passes if actual.eql?(expected)
expect(actual).not_to eql(not_expected) # passes if not(actual.eql?(expected))
```

Note: The new `expect` syntax no longer supports the `==` matcher.

### Identity

```ruby
expect(actual).to be(expected)    # passes if actual.equal?(expected)
expect(actual).to equal(expected) # passes if actual.equal?(expected)
```

### Comparisons

```ruby
expect(actual).to be >  expected
expect(actual).to be >= expected
expect(actual).to be <= expected
expect(actual).to be <  expected
expect(actual).to be_within(delta).of(expected)
```

### Regular expressions

```ruby
expect(actual).to match(/expression/)
```

Note: The new `expect` syntax no longer supports the `=~` matcher.

### Types/classes

```ruby
expect(actual).to be_an_instance_of(expected) # passes if actual.class == expected
expect(actual).to be_a(expected)              # passes if actual.kind_of?(expected)
expect(actual).to be_an(expected)             # an alias for be_a
expect(actual).to be_a_kind_of(expected)      # another alias
```

### Truthiness

```ruby
expect(actual).to be_truthy   # passes if actual is truthy (not nil or false)
expect(actual).to be true     # passes if actual == true
expect(actual).to be_falsy    # passes if actual is falsy (nil or false)
expect(actual).to be false    # passes if actual == false
expect(actual).to be_nil      # passes if actual is nil
expect(actual).to_not be_nil  # passes if actual is not nil
```

### Expecting errors

```ruby
expect { ... }.to raise_error
expect { ... }.to raise_error(ErrorClass)
expect { ... }.to raise_error("message")
expect { ... }.to raise_error(ErrorClass, "message")
```

### Expecting throws

```ruby
expect { ... }.to throw_symbol
expect { ... }.to throw_symbol(:symbol)
expect { ... }.to throw_symbol(:symbol, 'value')
```

### Yielding

```ruby
expect { |b| 5.tap(&b) }.to yield_control # passes regardless of yielded args

expect { |b| yield_if_true(true, &b) }.to yield_with_no_args # passes only if no args are yielded

expect { |b| 5.tap(&b) }.to yield_with_args(5)
expect { |b| 5.tap(&b) }.to yield_with_args(Fixnum)
expect { |b| "a string".tap(&b) }.to yield_with_args(/str/)

expect { |b| [1, 2, 3].each(&b) }.to yield_successive_args(1, 2, 3)
expect { |b| { :a => 1, :b => 2 }.each(&b) }.to yield_successive_args([:a, 1], [:b, 2])
```

### Predicate matchers

```ruby
expect(actual).to be_xxx         # passes if actual.xxx?
expect(actual).to have_xxx(:arg) # passes if actual.has_xxx?(:arg)
```

### Ranges (Ruby >= 1.9 only)

```ruby
expect(1..10).to cover(3)
```

### Collection membership

```ruby
expect(actual).to include(expected)
expect(actual).to start_with(expected)
expect(actual).to end_with(expected)

expect(actual).to contain_exactly(individual, items)
# ...which is the same as:
expect(actual).to match_array(expected_array)
```

#### Examples

```ruby
expect([1, 2, 3]).to include(1)
expect([1, 2, 3]).to include(1, 2)
expect([1, 2, 3]).to start_with(1)
expect([1, 2, 3]).to start_with(1, 2)
expect([1, 2, 3]).to end_with(3)
expect([1, 2, 3]).to end_with(2, 3)
expect({:a => 'b'}).to include(:a => 'b')
expect("this string").to include("is str")
expect("this string").to start_with("this")
expect("this string").to end_with("ring")
expect([1, 2, 3]).to contain_exactly(2, 3, 1)
expect([1, 2, 3]).to match_array([3, 2, 1])
```

## `should` syntax

In addition to the `expect` syntax, rspec-expectations continues to support the
`should` syntax:

```ruby
actual.should eq expected
actual.should be > 3
[1, 2, 3].should_not include 4
```

See [detailed information on the `should` syntax and its usage.](https://github.com/rspec/rspec-expectations/blob/master/Should.md)

## Compound Matcher Expressions

You can also create compound matcher expressions using `and` or `or`:

``` ruby
expect(alphabet).to start_with("a").and end_with("z")
expect(stoplight.color).to eq("red").or eq("green").or eq("yellow")
```

## Composing Matchers

Many of the built-in matchers are designed to take matchers as
arguments, to allow you to flexibly specify only the essential
aspects of an object or data structure. In addition, all of the
built-in matchers have one or more aliases that provide better
phrasing for when they are used as arguments to another matcher.

### Examples

```ruby
expect { k += 1.05 }.to change { k }.by( a_value_within(0.1).of(1.0) )

expect { s = "barn" }.to change { s }
  .from( a_string_matching(/foo/) )
  .to( a_string_matching(/bar/) )

expect(["barn", 2.45]).to contain_exactly(
  a_value_within(0.1).of(2.5),
  a_string_starting_with("bar")
)

expect(["barn", "food", 2.45]).to end_with(
  a_string_matching("foo"),
  a_value > 2
)

expect(["barn", 2.45]).to include( a_string_starting_with("bar") )

expect(:a => "food", :b => "good").to include(:a => a_string_matching(/foo/))

hash = {
  :a => {
    :b => ["foo", 5],
    :c => { :d => 2.05 }
  }
}

expect(hash).to match(
  :a => {
    :b => a_collection_containing_exactly(
      a_string_starting_with("f"),
      an_instance_of(Fixnum)
    ),
    :c => { :d => (a_value < 3) }
  }
)

expect { |probe|
  [1, 2, 3].each(&probe)
}.to yield_successive_args( a_value < 2, 2, a_value > 2 )
```

## Usage outside rspec-core

You always need to load `rspec/expectations` even if you only want to use one part of the library:

```ruby
require 'rspec/expectations'
```

Then simply include `RSpec::Matchers` in any class:

```ruby
class MyClass
  include RSpec::Matchers

  def do_something(arg)
    expect(arg).to be > 0
    # do other stuff
  end
end
```

## Also see

* [http://github.com/rspec/rspec](http://github.com/rspec/rspec)
* [http://github.com/rspec/rspec-core](http://github.com/rspec/rspec-core)
* [http://github.com/rspec/rspec-mocks](http://github.com/rspec/rspec-mocks)
* [http://github.com/rspec/rspec-collection_matchers](https://github.com/rspec/rspec-collection_matchers)
= webrobots

This is a library to help write robots.txt compliant web robots.

== Usage

  require 'webrobots'
  require 'uri'
  require 'net/http'

  robots = WebRobots.new('MyBot/1.0')

  uri = URI('http://digg.com/news/24hr')
  if robots.disallowed?(uri)
    STDERR.puts "Access disallowed: #{uri}"
    exit 1
  end
  body = Net::HTTP.get(uri)
  # ...

== Requirements

- Ruby 1.8.7 or 1.9.2+

== Contributing to webrobots

* Check out the latest master to make sure the feature hasn't been implemented or the bug hasn't been fixed yet
* Check out the issue tracker to make sure someone already hasn't requested it and/or contributed it
* Fork the project
* Start a feature/bugfix branch
* Commit and push until you are happy with your contribution
* Make sure to add tests for it. This is important so I don't break it in a future version unintentionally.
* Please try not to mess with the Rakefile, version, or history. If you want to have your own version, or is otherwise necessary, that is fine, but please isolate to its own commit so I can cherry-pick around it.

== Copyright

Copyright (c) 2010, 2011, 2012, 2013 Akinori MUSHA. See LICENSE.txt for
further details.
= Action View

Action View is a framework for handling view template lookup and rendering, and provides
view helpers that assist when building HTML forms, Atom feeds and more.
Template formats that Action View handles are ERB (embedded Ruby, typically
used to inline short Ruby snippets inside HTML), and XML Builder.

== Download and installation

The latest version of Action View can be installed with RubyGems:

  % [sudo] gem install actionview

Source code can be downloaded as part of the Rails project on GitHub

* https://github.com/rails/rails/tree/4-2-stable/actionview


== License

Action View is released under the MIT license:

* http://www.opensource.org/licenses/MIT


== Support

API documentation is at

* http://api.rubyonrails.org

Bug reports can be filed for the Ruby on Rails project here:

* https://github.com/rails/rails/issues

Feature requests should be discussed on the rails-core mailing list here:

* https://groups.google.com/forum/?fromgroups#!forum/rubyonrails-core

= Action Mailer -- Easy email delivery and testing

Action Mailer is a framework for designing email service layers. These layers
are used to consolidate code for sending out forgotten passwords, welcome
wishes on signup, invoices for billing, and any other use case that requires
a written notification to either a person or another system.

Action Mailer is in essence a wrapper around Action Controller and the
Mail gem.  It provides a way to make emails using templates in the same
way that Action Controller renders views using templates.

Additionally, an Action Mailer class can be used to process incoming email,
such as allowing a blog to accept new posts from an email (which could even
have been sent from a phone).

== Sending emails

The framework works by initializing any instance variables you want to be
available in the email template, followed by a call to +mail+ to deliver
the email.

This can be as simple as:

  class Notifier < ActionMailer::Base
    default from: 'system@loudthinking.com'

    def welcome(recipient)
      @recipient = recipient
      mail(to: recipient,
           subject: "[Signed up] Welcome #{recipient}")
    end
  end

The body of the email is created by using an Action View template (regular
ERB) that has the instance variables that are declared in the mailer action.

So the corresponding body template for the method above could look like this:

  Hello there,

  Mr. <%= @recipient %>

  Thank you for signing up!

If the recipient was given as "david@loudthinking.com", the email
generated would look like this:

  Date: Mon, 25 Jan 2010 22:48:09 +1100
  From: system@loudthinking.com
  To: david@loudthinking.com
  Message-ID: <4b5d84f9dd6a5_7380800b81ac29578@void.loudthinking.com.mail>
  Subject: [Signed up] Welcome david@loudthinking.com
  Mime-Version: 1.0
  Content-Type: text/plain;
  	charset="US-ASCII";
  Content-Transfer-Encoding: 7bit

  Hello there,

  Mr. david@loudthinking.com

  Thank you for signing up!

In order to send mails, you simply call the method and then call +deliver_now+ on the return value.

Calling the method returns a Mail Message object:

  message = Notifier.welcome("david@loudthinking.com")   # => Returns a Mail::Message object
  message.deliver_now                                    # => delivers the email

Or you can just chain the methods together like:

  Notifier.welcome("david@loudthinking.com").deliver_now # Creates the email and sends it immediately

== Setting defaults

It is possible to set default values that will be used in every method in your
Action Mailer class. To implement this functionality, you just call the public
class method +default+ which you get for free from <tt>ActionMailer::Base</tt>.
This method accepts a Hash as the parameter. You can use any of the headers,
email messages have, like +:from+ as the key. You can also pass in a string as
the key, like "Content-Type", but Action Mailer does this out of the box for you,
so you won't need to worry about that. Finally, it is also possible to pass in a
Proc that will get evaluated when it is needed.

Note that every value you set with this method will get overwritten if you use the
same key in your mailer method.

Example:

  class AuthenticationMailer < ActionMailer::Base
    default from: "awesome@application.com", subject: Proc.new { "E-mail was generated at #{Time.now}" }
    .....
  end

== Receiving emails

To receive emails, you need to implement a public instance method called
+receive+ that takes an email object as its single parameter. The Action Mailer
framework has a corresponding class method, which is also called +receive+, that
accepts a raw, unprocessed email as a string, which it then turns into the email
object and calls the receive instance method.

Example:

  class Mailman < ActionMailer::Base
    def receive(email)
      page = Page.find_by(address: email.to.first)
      page.emails.create(
        subject: email.subject, body: email.body
      )

      if email.has_attachments?
        email.attachments.each do |attachment|
          page.attachments.create({
            file: attachment, description: email.subject
          })
        end
      end
    end
  end

This Mailman can be the target for Postfix or other MTAs. In Rails, you would use
the runner in the trivial case like this:

  rails runner 'Mailman.receive(STDIN.read)'

However, invoking Rails in the runner for each mail to be received is very
resource intensive. A single instance of Rails should be run within a daemon, if
it is going to process more than just a limited amount of email.

== Configuration

The Base class has the full list of configuration options. Here's an example:

  ActionMailer::Base.smtp_settings = {
    address:        'smtp.yourserver.com', # default: localhost
    port:           '25',                  # default: 25
    user_name:      'user',
    password:       'pass',
    authentication: :plain                 # :plain, :login or :cram_md5
  }


== Download and installation

The latest version of Action Mailer can be installed with RubyGems:

  % [sudo] gem install actionmailer

Source code can be downloaded as part of the Rails project on GitHub

* https://github.com/rails/rails/tree/4-2-stable/actionmailer


== License

Action Mailer is released under the MIT license:

* http://www.opensource.org/licenses/MIT


== Support

API documentation is at

* http://api.rubyonrails.org

Bug reports can be filed for the Ruby on Rails project here:

* https://github.com/rails/rails/issues

Feature requests should be discussed on the rails-core mailing list here:

* https://groups.google.com/forum/?fromgroups#!forum/rubyonrails-core

# rspec-core [![Build Status](https://secure.travis-ci.org/rspec/rspec-core.svg?branch=master)](http://travis-ci.org/rspec/rspec-core) [![Code Climate](https://codeclimate.com/github/rspec/rspec-core.svg)](https://codeclimate.com/github/rspec/rspec-core)

rspec-core provides the structure for writing executable examples of how your
code should behave, and an `rspec` command with tools to constrain which
examples get run and tailor the output.

## Install

    gem install rspec      # for rspec-core, rspec-expectations, rspec-mocks
    gem install rspec-core # for rspec-core only
    rspec --help

Want to run against the `master` branch? You'll need to include the dependent
RSpec repos as well. Add the following to your `Gemfile`:

```ruby
%w[rspec rspec-core rspec-expectations rspec-mocks rspec-support].each do |lib|
  gem lib, :git => "git://github.com/rspec/#{lib}.git", :branch => 'master'
end
```

## Basic Structure

RSpec uses the words "describe" and "it" so we can express concepts like a conversation:

    "Describe an order."
    "It sums the prices of its line items."

```ruby
RSpec.describe Order do
  it "sums the prices of its line items" do
    order = Order.new

    order.add_entry(LineItem.new(:item => Item.new(
      :price => Money.new(1.11, :USD)
    )))
    order.add_entry(LineItem.new(:item => Item.new(
      :price => Money.new(2.22, :USD),
      :quantity => 2
    )))

    expect(order.total).to eq(Money.new(5.55, :USD))
  end
end
```

The `describe` method creates an [ExampleGroup](http://rubydoc.info/gems/rspec-core/RSpec/Core/ExampleGroup).  Within the
block passed to `describe` you can declare examples using the `it` method.

Under the hood, an example group is a class in which the block passed to
`describe` is evaluated. The blocks passed to `it` are evaluated in the
context of an _instance_ of that class.

## Nested Groups

You can also declare nested nested groups using the `describe` or `context`
methods:

```ruby
RSpec.describe Order do
  context "with no items" do
    it "behaves one way" do
      # ...
    end
  end

  context "with one item" do
    it "behaves another way" do
      # ...
    end
  end
end
```

Nested groups are subclasses of the outer example group class, providing
the inheritance semantics you'd want for free.

## Aliases

You can declare example groups using either `describe` or `context`.
For a top level example group, `describe` and `context` are available
off of `RSpec`. For backwards compatibility, they are also available
off of the `main` object and `Module` unless you disable monkey
patching.

You can declare examples within a group using any of `it`, `specify`, or
`example`.

## Shared Examples and Contexts

Declare a shared example group using `shared_examples`, and then include it
in any group using `include_examples`.

```ruby
RSpec.shared_examples "collections" do |collection_class|
  it "is empty when first created" do
    expect(collection_class.new).to be_empty
  end
end

RSpec.describe Array do
  include_examples "collections", Array
end

RSpec.describe Hash do
  include_examples "collections", Hash
end
```

Nearly anything that can be declared within an example group can be declared
within a shared example group. This includes `before`, `after`, and `around`
hooks, `let` declarations, and nested groups/contexts.

You can also use the names `shared_context` and `include_context`. These are
pretty much the same as `shared_examples` and `include_examples`, providing
more accurate naming when you share hooks, `let` declarations, helper methods,
etc, but no examples.

## Metadata

rspec-core stores a metadata hash with every example and group, which
contains their descriptions, the locations at which they were
declared, etc, etc. This hash powers many of rspec-core's features,
including output formatters (which access descriptions and locations),
and filtering before and after hooks.

Although you probably won't ever need this unless you are writing an
extension, you can access it from an example like this:

```ruby
it "does something" do |example|
  expect(example.metadata[:description]).to eq("does something")
end
```

### `described_class`

When a class is passed to `describe`, you can access it from an example
using the `described_class` method, which is a wrapper for
`example.metadata[:described_class]`.

```ruby
RSpec.describe Widget do
  example do
    expect(described_class).to equal(Widget)
  end
end
```

This is useful in extensions or shared example groups in which the specific
class is unknown. Taking the collections shared example group from above, we can
clean it up a bit using `described_class`:

```ruby
RSpec.shared_examples "collections" do
  it "is empty when first created" do
    expect(described_class.new).to be_empty
  end
end

RSpec.describe Array do
  include_examples "collections"
end

RSpec.describe Hash do
  include_examples "collections"
end
```

## A Word on Scope

RSpec has two scopes:

* **Example Group**: Example groups are defined by a `describe` or
  `context` block, which is eagerly evaluated when the spec file is
  loaded. The block is evaluated in the context of a subclass of
  `RSpec::Core::ExampleGroup`, or a subclass of the parent example group
  when you're nesting them.
* **Example**: Examples -- typically defined by an `it` block -- and any other
  blocks with per-example semantics -- such as a `before(:example)` hook -- are
  evaluated in the context of
  an _instance_ of the example group class to which the example belongs.
  Examples are _not_ executed when the spec file is loaded; instead,
  RSpec waits to run any examples until all spec files have been loaded,
  at which point it can apply filtering, randomization, etc.

To make this more concrete, consider this code snippet:

``` ruby
RSpec.describe "Using an array as a stack" do
  def build_stack
    []
  end

  before(:example) do
    @stack = build_stack
  end

  it 'is initially empty' do
    expect(@stack).to be_empty
  end

  context "after an item has been pushed" do
    before(:example) do
      @stack.push :item
    end

    it 'allows the pushed item to be popped' do
      expect(@stack.pop).to eq(:item)
    end
  end
end
```

Under the covers, this is (roughly) equivalent to:

``` ruby
class UsingAnArrayAsAStack < RSpec::Core::ExampleGroup
  def build_stack
    []
  end

  def before_example_1
    @stack = build_stack
  end

  def it_is_initially_empty
    expect(@stack).to be_empty
  end

  class AfterAnItemHasBeenPushed < self
    def before_example_2
      @stack.push :item
    end

    def it_allows_the_pushed_item_to_be_popped
      expect(@stack.pop).to eq(:item)
    end
  end
end
```

To run these examples, RSpec would (roughly) do the following:

``` ruby
example_1 = UsingAnArrayAsAStack.new
example_1.before_example_1
example_1.it_is_initially_empty

example_2 = UsingAnArrayAsAStack::AfterAnItemHasBeenPushed.new
example_2.before_example_1
example_2.before_example_2
example_2.it_allows_the_pushed_item_to_be_popped
```

## The `rspec` Command

When you install the rspec-core gem, it installs the `rspec` executable,
which you'll use to run rspec. The `rspec` command comes with many useful
options.
Run `rspec --help` to see the complete list.

## Store Command Line Options `.rspec`

You can store command line options in a `.rspec` file in the project's root
directory, and the `rspec` command will read them as though you typed them on
the command line.

## Get Started

Start with a simple example of behavior you expect from your system. Do
this before you write any implementation code:

```ruby
# in spec/calculator_spec.rb
RSpec.describe Calculator do
  describe '#add' do
    it 'returns the sum of its arguments' do
      expect(Calculator.new.add(1, 2)).to eq(3)
    end
  end
end
```

Run this with the rspec command, and watch it fail:

```
$ rspec spec/calculator_spec.rb
./spec/calculator_spec.rb:1: uninitialized constant Calculator
```

Address the failure by defining a skeleton of the `Calculator` class:

```ruby
# in lib/calculator.rb
class Calculator
  def add(a, b)
  end
end
```

Be sure to require the implementation file in the spec:

```ruby
# in spec/calculator_spec.rb
# - RSpec adds ./lib to the $LOAD_PATH
require "calculator"
```

Now run the spec again, and watch the expectation fail:

```
$ rspec spec/calculator_spec.rb
F

Failures:

  1) Calculator#add returns the sum of its arguments
     Failure/Error: expect(Calculator.new.add(1, 2)).to eq(3)

       expected: 3
            got: nil

       (compared using ==)
     # ./spec/calcalator_spec.rb:6:in `block (3 levels) in <top (required)>'

Finished in 0.00131 seconds (files took 0.10968 seconds to load)
1 example, 1 failure

Failed examples:

rspec ./spec/calcalator_spec.rb:5 # Calculator#add returns the sum of its arguments
```

Implement the simplest solution, by changing the definition of `Calculator#add` to:

```ruby
def add(a, b)
  a + b
end
```

Now run the spec again, and watch it pass:

```
$ rspec spec/calculator_spec.rb
.

Finished in 0.000315 seconds
1 example, 0 failures
```

Use the `documentation` formatter to see the resulting spec:

```
$ rspec spec/calculator_spec.rb --format doc
Calculator
  #add
    returns the sum of its arguments

Finished in 0.000379 seconds
1 example, 0 failures
```

## Also see

* [http://github.com/rspec/rspec](http://github.com/rspec/rspec)
* [http://github.com/rspec/rspec-expectations](http://github.com/rspec/rspec-expectations)
* [http://github.com/rspec/rspec-mocks](http://github.com/rspec/rspec-mocks)
# Serve Static Assets

Rails gem to enable serving of static assets

Supports:

- Rails 3
- Rails 4

## What

This gem enables serving assets in production, required with Rails4.

## Install

In your `Gemfile` add:

```
gem 'rails_serve_static_assets'
```

Then run

```
$ bundle install
```

You also need the `rails_stdout_logging` gem. You can get both of them together by installing [`rails_12factor`](https://github.com/heroku/rails_12factor) gem.

## Rails 4 Serve Static Assets

In the default Rails development environment assets are served through a middleware called [sprockets](https://github.com/sstephenson/sprockets). In production however most one off Rails deployments will put their ruby server behind reverse HTTP proxy server such as Nginx which can load balance their sites and can serve static files directly. When Nginx sees a request for an asset such as `/assets/rails.png` it will grab it from disk at `/public/assets/rails.png` and serve it. The Rails server will never even see the request.

On a 12factor platform, Nginx is not required to run your application. Your app should be capable of handling requests directly, or through a [routing layer](https://devcenter.heroku.com/articles/http-routing) that may handles load balancing while you scale out horizontally. The caching behavior of Nginx is not needed if your application is serving static assets through an [edge caching CDN](https://en.wikipedia.org/wiki/Content_delivery_network).

By default Rails4 will return a 404 if an asset is not handled via an external proxy such as Nginx. While this default behavior may help you debug your Nginx configuration, it makes a default Rails app with assets unusable on a 12factor platform. To fix this we've released a gem `rails_serve_static_assets`.

This gem, `rails_serve_static_assets`, enables your Rails server to deliver your assets instead of returning a 404. You can use this to populate an edge cache CDN, or serve files directly from your web app. This gives your app total control and allows you to do things like redirects, or setting headers in your Ruby code. To enable this behavior in your app we only need to set two configuration options through this gem:

```
config.serve_static_assets = true
config.action_dispatch.x_sendfile_header = nil
```

Note: this gem will set these values for you, you don't need to change any configuration manually.

All you need to do to get this functionality of both gems is add the `rails_12factor` gem to your project.

## Why Didn't I need this before?

Why do you need to include this gem in Rails 4 and not Rails 3? Rails4 is getting rid of the concept of plugins. Before libraries were easily distributed as Gems and in the form of Engines, Rails had a folder `vendor/plugins`. Any code you put there would be initialized much like a Gem is today. This was a very simple and easy way to share and use libraries, but it wasn't very maintainable. You could use a library, and make a change locally and then deploy which makes your version incompatible from future versions. Even worse there was no concept of versioning aside from source control, so semantic versioning was out of the question. For these reasons and more Rails3 deprecated plugins. With Rails4 plugins have been removed completely. Why does this affect your app on Heroku?

In the past Heroku has used plugins as a safe way to configure your application where code was needed. While we advocate [separating config from code](http://12factor.net), this was the only option if we wanted your apps to work with no changes from you. With Rails3 Heroku will add the asset serving and standardout logging plugins to your app automatically. With Rails4, Heroku needs you to add these libraries to your Gemfile.

It is important to note that unlike Gems, plugins do not have a dependency resolution phase like what happens when you run `bundle install`. Heroku does not and will not add anything to your Gemfile on compilation.


## The Future

We will be working with Rails and the Rails core team to make future versions of Rails work on Heroku out of the box. Until then you'll need to add this gem to your project.


= Railties -- Gluing the Engine to the Rails

Railties is responsible for gluing all frameworks together. Overall, it:

* handles the bootstrapping process for a Rails application;

* manages the +rails+ command line interface;

* and provides the Rails generators core.


== Download

The latest version of Railties can be installed with RubyGems:

* gem install railties

Source code can be downloaded as part of the Rails project on GitHub

* https://github.com/rails/rails/tree/4-2-stable/railties

== License

Railties is released under the MIT license:

* http://www.opensource.org/licenses/MIT

== Support

API documentation is at

* http://api.rubyonrails.org

Bug reports can be filed for the Ruby on Rails project here:

* https://github.com/rails/rails/issues

Feature requests should be discussed on the rails-core mailing list here:

* https://groups.google.com/forum/?fromgroups#!forum/rubyonrails-core

== README

This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to cover:

* Ruby version

* System dependencies

* Configuration

* Database creation

* Database initialization

* How to run the test suite

* Services (job queues, cache servers, search engines, etc.)

* Deployment instructions

* ...


Please feel free to use a different markup language if you do not plan to run
<tt>rake doc:app</tt>.
= <%= camelized %>

This project rocks and uses MIT-LICENSE.debug_inspector
===============

(C) John Mair (banisterfiend) 2012

_A Ruby wrapper for the new MRI 2.0 debug\_inspector API_

**This library only works on MRI 2.0. Requiring it on unsupported Rubies will result in a no-op**

Usage
-----

```ruby
require 'debug_inspector'

# binding of nth caller frame (returns a Binding object)
RubyVM::DebugInspector.open { |i| i.frame_binding(n) }

# iseq of nth caller frame (returns a RubyVM::InstructionSequence object)
RubyVM::DebugInspector.open { |i| i.frame_iseq(n) }

# class of nth caller frame
RubyVM::DebugInspector.open { |i| i.frame_class(n) }

# backtrace locations (returns an array of Thread::Backtrace::Location objects)
RubyVM::DebugInspector.open { |i| i.backtrace_locations }
```

Contact
-------

Problems or questions contact me at [github](http://github.com/banister)

License
-------

(The MIT License)

Copyright (c) 2012 (John Mair)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Byebug

[![Ver][gem]][gem_url]
[![Gpa][gpa]][gpa_url]
[![Dep][dep]][dep_url]
[![Cov][cov]][cov_url]
[![Git][tip]][tip_url]

[gem]: https://img.shields.io/gem/v/byebug.svg
[gpa]: https://img.shields.io/codeclimate/github/deivid-rodriguez/byebug.svg
[dep]: https://img.shields.io/gemnasium/deivid-rodriguez/byebug.svg
[cov]: https://img.shields.io/codeclimate/coverage/github/deivid-rodriguez/byebug.svg
[tip]: https://img.shields.io/gittip/deivid-rodriguez.svg

[gem_url]: https://rubygems.org/gems/byebug
[gpa_url]: https://codeclimate.com/github/deivid-rodriguez/byebug
[dep_url]: https://gemnasium.com/deivid-rodriguez/byebug
[cov_url]: https://codeclimate.com/github/deivid-rodriguez/byebug
[tip_url]: https://www.gittip.com/deivid-rodriguez

_Debugging in Ruby 2_

Byebug is a simple to use, feature rich debugger for Ruby 2. It uses the new
TracePoint API for execution control and the new Debug Inspector API for call
stack navigation, so it doesn't depend on internal core sources. It's developed
as a C extension, so it's fast. And it has a full test suite so it's reliable.

It allows you to see what is going on _inside_ a Ruby program while it executes
and offers many of the traditional debugging features such as:

* Stepping: Running your program one line at a time.
* Breaking: Pausing the program at some event or specified instruction, to
examine the current state.
* Evaluating: Basic REPL functionality, although [pry][] does a better job at
that.
* Tracking: Keeping track of the different values of your variables or the
different lines executed by your program.


## Build Status

Linux & OSX [![Tra][tra]][tra_url]

Windows [![Vey][vey]][vey_url]

[tra]: https://img.shields.io/travis/deivid-rodriguez/byebug.svg?branch=master
[vey]: https://ci.appveyor.com/api/projects/status/github/deivid-rodriguez/byebug?svg=true

[tra_url]: https://travis-ci.org/deivid-rodriguez/byebug
[vey_url]: https://ci.appveyor.com/project/deivid-rodriguez/byebug


## Requirements

* Required: MRI 2.0.0 or higher. For debugging ruby 1.9.3 or older, use
[debugger][].

* Recommended:
  - MRI 2.0.0-p576 or higher.
  - MRI 2.1.3 or higher.
  - MRI 2.2.1 or higher.


## Install

    $ gem install byebug


## Usage

Simply drop

    byebug

wherever you want to start debugging and the execution will stop there. If you
are debugging rails, start the server and once the execution gets to your
`byebug` command you will get a debugging prompt.


## Byebug's commands

    Command     | Aliases      | Subcommands
    ----------- |:------------ |:-----------
    `backtrace` | `bt` `where` |
    `break`     |              |
    `catch`     |              |
    `condition` |              |
    `continue`  |              |
    `delete`    |              |
    `disable`   |              | `breakpoints` `display`
    `display`   |              |
    `down`      |              |
    `edit`      |              |
    `enable`    |              | `breakpoints` `display`
    `eval`      |              |
    `finish`    |              |
    `frame`     |              |
    `help`      |              |
    `history`   |              |
    `info`      |              | `args` `breakpoints` `catch` `display` `file` `line` `program`
    `irb`       |              |
    `kill`      |              |
    `list`      |              |
    `method`    |              | `instance`
    `next`      |              |
    `pp`        |              |
    `pry`       |              |
    `ps`        |              |
    `putl`      |              |
    `quit`      | `exit`       |
    `restart`   |              |
    `save`      |              |
    `set`       |              | `autoeval` `autoirb` `autolist` `autosave` `basename` `callstyle` `fullpath` `histfile` `histsize` `linetrace` `listsize` `post_mortem` `savefile` `stack_on_error` `verbose` `width`
    `show`      |              | `autoeval` `autoirb` `autolist` `autosave` `basename` `callstyle` `fullpath` `histfile` `histsize` `linetrace` `listsize` `post_mortem` `savefile` `stack_on_error` `verbose` `width`
    `source`    |              |
    `step`      |              |
    `thread`    |              | `current` `list` `resume` `stop` `switch`
    `tracevar`  |              |
    `undisplay` |              |
    `up`        |              |
    `var`       |              | `all` `constant` `global` `instance` `local`


## Semantic Versioning

Byebug tries to follow [semantic versioning](http://semver.org) and tries to
bump major version only when backwards incompatible changes are released.
Backwards compatibility is targeted to [pry-byebug][] and any other plugins
relying on `byebug`.


## Getting Started

Read [byebug's markdown
guide](https://github.com/deivid-rodriguez/byebug/blob/master/GUIDE.md) to get
started. Proper documentation will be eventually written.


## Related projects

* [pry-byebug][] adds `next`, `step`, `finish`, `continue` and `break` commands
to `pry` using `byebug`.
* [ruby-debug-passenger][] adds a rake task that restarts Passenger with Byebug
connected.
* [minitest-byebug][] starts a byebug session on minitest failures.
* [sublime_debugger][] provides a plugin for ruby debugging on Sublime Text.


## Contribute

See [Getting Started with Development](CONTRIBUTING.md).


## Credits

Everybody who has ever contributed to this forked and reforked piece of
software, specially:

* @ko1, author of the awesome TracePoint API for Ruby.
* @cldwalker, [debugger][]'s mantainer.
* @denofevil, author of [debase][], the starting point of this.
* @kevjames3 for testing, bug reports and the interest in the project.
* @FooBarWidget for working and helping with remote debugging.

[debugger]: https://github.com/cldwalker/debugger
[pry]: https://github.com/pry/pry
[debase]: https://github.com/denofevil/debase
[pry-byebug]: https://github.com/deivid-rodriguez/pry-byebug
[ruby-debug-passenger]: https://github.com/davejamesmiller/ruby-debug-passenger
[minitest-byebug]: https://github.com/kaspth/minitest-byebug
[sublime_debugger]: https://github.com/shuky19/sublime_debugger
= CodeRay

Tired of blue'n'gray? Try the original version of this documentation on
coderay.rubychan.de[http://coderay.rubychan.de/doc/] :-)

== About

CodeRay is a Ruby library for syntax highlighting.

You put your code in, and you get it back colored; Keywords, strings,
floats, comments - all in different colors. And with line numbers.

*Syntax* *Highlighting*...
* makes code easier to read and maintain
* lets you detect syntax errors faster
* helps you to understand the syntax of a language
* looks nice
* is what everybody wants to have on their website
* solves all your problems and makes the girls run after you


== Installation

 % gem install coderay


=== Dependencies

CodeRay needs Ruby 1.8.7+ or 1.9.2+. It also runs on Rubinius and JRuby.


== Example Usage

 require 'coderay'
 
 html = CodeRay.scan("puts 'Hello, world!'", :ruby).div(:line_numbers => :table)


== Documentation

See CodeRay.


== Credits

=== Special Thanks to

* licenser (Heinz N. Gies) for ending my QBasic career, inventing the Coder
  project and the input/output plugin system.
  CodeRay would not exist without him.
* bovi (Daniel Bovensiepen) for helping me out on various occasions.

=== Thanks to

* Caleb Clausen for writing RubyLexer (see
  http://rubyforge.org/projects/rubylexer) and lots of very interesting mail
  traffic
* birkenfeld (Georg Brandl) and mitsuhiku (Arnim Ronacher) for PyKleur, now pygments.
  You guys rock!
* Jamis Buck for writing Syntax (see http://rubyforge.org/projects/syntax)
  I got some useful ideas from it.
* Doug Kearns and everyone else who worked on ruby.vim - it not only helped me
  coding CodeRay, but also gave me a wonderful target to reach for the Ruby
  scanner.
* everyone who uses CodeBB on http://www.rubyforen.de and http://www.python-forum.de
* iGEL, magichisoka, manveru, WoNáDo and everyone I forgot from rubyforen.de
* Dethix from ruby-mine.de
* zickzackw
* Dookie (who is no longer with us...) and Leonidas from http://www.python-forum.de
* Andreas Schwarz for finding out that CaseIgnoringWordList was not case
  ignoring! Such things really make you write tests.
* closure for the first version of the Scheme scanner.
* Stefan Walk for the first version of the JavaScript and PHP scanners.
* Josh Goebel for another version of the JavaScript scanner, a SQL and a Diff scanner.
* Jonathan Younger for pointing out the licence confusion caused by wrong LICENSE file.
* Jeremy Hinegardner for finding the shebang-on-empty-file bug in FileType.
* Charles Oliver Nutter and Yehuda Katz for helping me benchmark CodeRay on JRuby.
* Andreas Neuhaus for pointing out a markup bug in coderay/for_redcloth.
* 0xf30fc7 for the FileType patch concerning Delphi file extensions.
* The folks at redmine.org - thank you for using and fixing CodeRay!
* Keith Pitt for his SQL scanners
* Rob Aldred for the terminal encoder
* Trans for pointing out $DEBUG dependencies
* Flameeyes for finding that Term::ANSIColor was obsolete
* matz and all Ruby gods and gurus
* The inventors of: the computer, the internet, the true color display, HTML &
  CSS, VIM, Ruby, pizza, microwaves, guitars, scouting, programming, anime, 
  manga, coke and green ice tea.

Where would we be without all those people?

=== Created using

* Ruby[http://ruby-lang.org/]
* Chihiro (my Sony VAIO laptop); Henrietta (my old MacBook);
  Triella, born Rico (my new MacBook); as well as
  Seras and Hikari (my PCs)
* RDE[http://homepage2.nifty.com/sakazuki/rde_e.html],
  VIM[http://vim.org] and TextMate[http://macromates.com]
* Subversion[http://subversion.tigris.org/]
* Redmine[http://redmine.org/]
* Firefox[http://www.mozilla.org/products/firefox/],
  Firebug[http://getfirebug.com/], Safari[http://www.apple.com/safari/], and
  Thunderbird[http://www.mozilla.org/products/thunderbird/]
* RubyGems[http://docs.rubygems.org/] and Rake[http://rake.rubyforge.org/]
* TortoiseSVN[http://tortoisesvn.tigris.org/] using Apache via
  XAMPP[http://www.apachefriends.org/en/xampp.html]
* RDoc (though I'm quite unsatisfied with it)
* Microsoft Windows (yes, I confess!) and MacOS X
* GNUWin32, MinGW and some other tools to make the shell under windows a bit
  less useless
* Term::ANSIColor[http://term-ansicolor.rubyforge.org/]
* PLEAC[http://pleac.sourceforge.net/] code examples
* Github
* Travis CI (http://travis-ci.org/rubychan/github)

=== Free

* As you can see, CodeRay was created under heavy use of *free* software.
* So CodeRay is also *free*.
* If you use CodeRay to create software, think about making this software
  *free*, too.
* Thanks :)
<p align=right>
  Documentation for:
  <a href=https://github.com/rails/web-console/tree/v2.0.0>v2.0.0</a>
</p>

# Web Console [![Build Status](https://travis-ci.org/rails/web-console.svg?branch=master)](https://travis-ci.org/rails/web-console)

_Web Console_ is a debugging tool for your Ruby on Rails applications.

- [Installation](#installation)
- [Runtime](#runtime)
  - [CRuby](#cruby)
  - [JRuby](#jruby)
  - [Rubinius](#rubinius)
- [Configuration](#configuration)
- [Usage](#usage)
- [FAQ](#faq)
- [Credits](#credits)

## Installation

_Web Console_ is meant to work as a Rails plugin. To install it in your current
application, add the following to your `Gemfile`.

```ruby
group :development do
  gem 'web-console', '~> 2.0'
end
```

After you save the `Gemfile` changes, make sure to run `bundle install` and
restart your server for the _Web Console_ to kick in.

## Runtime

_Web Console_ uses [John Mair]'s [binding_of_caller] to spawn a console in a
specific binding. This comes at the price of limited Ruby runtime support.

### CRuby

CRuby 1.9.2 and below is **not** supported.

### JRuby

JRuby needs to run in interpreted mode. You can enable it by:

```bash
export JRUBY_OPTS=-J-Djruby.compile.mode=OFF

# If you run JRuby 1.7.12 and above, you can use:
export JRUBY_OPTS=--dev
```

An unstable version of [binding_of_caller] is needed as the latest stable one
won't compile on _JRuby_. To install it, put the following in your application
`Gemfile`:

```ruby
group :development do
  gem 'binding_of_caller', '0.7.3.pre1'
end
```

Only _JRuby_ 1.7, is supported (no JRuby 9K support at the moment).

### Rubinius

Internal errors like `ZeroDevisionError` aren't caught.

## Usage

The web console allows you to create an interactive Ruby session in your
browser. Those sessions are launched automatically in case on an error, but
they can also be launched manually in in any page.

For example, calling `console` in a view will display a console in the current
page in the context of the view binding.

```html
<% console %>
```

Calling `console` in a controller will result in a console in the context of
the controller action:

```ruby
class PostsController < ApplicationController
  def new
    console
    @post = Post.new
  end
end
```

Only one `console` invocation is allowed per request. If you happen to have
multiple ones, a `WebConsole::DoubleRenderError` is raised.

## Configuration

_Web Console_ allows you to execute arbitrary code on the server, so you
should be very careful, who you give access to.

### config.web_console.whitelisted_ips

By default, only requests coming from IPv4 and IPv6 localhosts are allowed.

`config.web_console.whitelisted_ips` lets you control which IP's have access to
the console.

You can whitelist single IP's or whole networks. Say you want to share your
console with `192.168.0.100`. You can do this:

```ruby
class Application < Rails::Application
  config.web_console.whitelisted_ips = '192.168.0.100'
end
```

If you want to whitelist the whole private network, you can do:

```ruby
class Application < Rails::Application
  config.web_console.whitelisted_ips = '192.168.0.0/16'
end
```

Take a note that IPv4 and IPv6 localhosts are always allowed. This wasn't the
case in 2.0.

### config.web_console.whiny_requests

When a console cannot be shown for a given IP address or content type, a
messages like the following is printed in the server logs:

> Cannot render console from 192.168.1.133! Allowed networks:
> 127.0.0.0/127.255.255.255, ::1

If you don't wanna see this message anymore, set this option to `false`:

```ruby
class Application < Rails::Application
  config.web_console.whiny_requests = false
end
```

### config.web_console.templates_path

If you wanna style the console yourself, you can place `style.css` at a
directory pointed by `config.web_console.templates_path`:

```ruby
class Application < Rails::Application
  config.web_console.templates_path = 'app/views/web_console'
end
```

You may wanna check the [templates] folder at the source tree for the files you
may override.

## FAQ

### Where did /console go?

The remote terminal emulator was extracted in its own gem that is no longer
bundled with _Web Console_.

If you miss this feature, check out [rvt].

### Why I constantly get unavailable session errors?

All of _Web Console_ sessions are stored in memory. If you happen to run on a
multi-process server (like Unicorn) you may get unavailable session errors
while the server is still running. This is because a request may hit a
different worker (process) that doesn't have the desired session in memory.

To avoid that, if you use such servers in development, configure them so they
server requests only out of one process.

### How to inspect local and instance variables?

The interactive console executes Ruby code. Invoking `instance_variables` and
`local_variables` will give you what you want.

## Credits

* Shoutout to [Charlie Somerville] for [better_errors] and [this] code.
* Kudos to [John Mair] for [binding_of_caller].
* Thanks to [Charles Oliver Nutter] for all the _JRuby_ feedback.
* Hugs and kisses to all of our [contributors].

[better_errors]: https://github.com/charliesome/better_errors
[binding_of_caller]: https://github.com/banister/binding_of_caller
[Charlie Somerville]: https://github.com/charliesome
[John Mair]: https://github.com/banister
[Charles Oliver Nutter]: https://github.com/headius
[templates]: https://github.com/rails/web-console/tree/master/lib/web_console/templates
[this]: https://github.com/rails/web-console/blob/master/lib/web_console/integration/cruby.rb#L20-L32
[rvt]: https://github.com/gsamokovarov/rvt
[contributors]: https://github.com/rails/web-console/graphs/contributors
== README

This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to cover:

* Ruby version

* System dependencies

* Configuration

* Database creation

* Database initialization

* How to run the test suite

* Services (job queues, cache servers, search engines, etc.)

* Deployment instructions

* ...


Please feel free to use a different markup language if you do not plan to run
<tt>rake doc:app</tt>.
Rack::Timeout
=============

Abort requests that are taking too long; a subclass of `Rack::Timeout::Error` is raised.

A generous timeout of 15s is the default. It's recommended to set the timeout as low as realistically viable for your application. Most applications will do fine with a setting between 2 and 5 seconds.

There's a handful of other settings, read on for details.

Rack::Timeout is not a solution to the problem of long-running requests, it's a debug and remediation tool. App developers should track rack-timeout's data and address recurring instances of particular timeouts, for example by refactoring code so it runs faster or offseting lengthy work to happen asynchronously.


Basic Usage
-----------

The following covers currently supported versions of Rails, Rack, Ruby, and Bundler. See the Compatibility section at the end for legacy versions.

### Rails apps

```ruby
# Gemfile
gem "rack-timeout"
```

That's all that's required if you want to use the default timeout of 15s. To use a custom timeout, create an initializer file:

```ruby
# config/initializers/timeout.rb
Rack::Timeout.timeout = 5  # seconds
```

### Sinatra and other Rack apps

```ruby
# config.ru
require "rack-timeout"
use Rack::Timeout          # Call as early as possible so rack-timeout runs before all other middleware.
Rack::Timeout.timeout = 5  # Recommended. If omitted, defaults to 15 seconds.
```


The Rabbit Hole
---------------

### Service Timeout

`Rack::Timeout.timeout` (or `Rack::Timeout.service_timeout`) is our principal setting.

*Service time* is the time taken from when a request first enters rack to when its response is sent back. When the application takes longer than `service_timeout` to process a request, the request's status is logged as `timed_out` and a `Rack::Timeout::RequestTimeoutError` error is raised on the application thread. This may be automatically caught by the framework or plugins, so beware. Also, the error is not guaranteed to be raised in a timely fashion, see section below about IO blocks.

Service timeout can be disabled entirely by setting the property to `0` or `false`, at which point the request skips Rack::Timeout's machinery (so no logging will be present).


### Wait Timeout

Before a request reaches the rack application, it may have spent some time being received by the web server, or waiting in the application server's queue before being dispatched to rack. The time between when a request is received by the web server and when rack starts handling it is called the *wait time*.

On Heroku, a request will be dropped when the routing layer sees no data being transferred for over 30 seconds. (You can read more about the specifics of Heroku routing's timeout [here][heroku-routing] and [here][heroku-timeout].) In this case, it makes no sense to process a request that reaches the application after having waited more than 30 seconds. That's where the `Rack::Timeout.wait_timeout` setting comes in. When a request has a wait time greater than `wait_timeout`, it'll be dropped without ever being sent down to the application, and a `Rack::Timeout::RequestExpiryError` is raised. Such requests are logged as `expired`.

[heroku-routing]: https://devcenter.heroku.com/articles/http-routing#timeouts
[heroku-timeout]: https://devcenter.heroku.com/articles/request-timeout

`Rack::Timeout.wait_timeout` is set at a default of 30 seconds, matching Heroku's router's timeout.

Wait timeout can be disabled entirely by setting the property to `0` or `false`.

A request's computed wait time may affect the service timeout used for it. Basically, a request's wait time plus service time may not exceed the wait timeout. The reasoning for that is based on Heroku router's behavior, that the request would be dropped anyway after the wait timeout. So, for example, with the default settings of `service_timeout=15`, `wait_timeout=30`, a request that had 20 seconds of wait time will not have a service timeout of 15, but instead of 10, as there are only 10 seconds left before `wait_timeout` is reached. This behavior can be disabled by setting `Rack::Timeout.service_past_wait` to `true`. When set, the `service_timeout` setting will always be honored.

The way we're able to infer a request's start time, and from that its wait time, is through the availability of the `X-Request-Start` HTTP header, which is expected to contain the time since epoch in milliseconds. (A concession is made for nginx's sec.msec notation.)

If the `X-Request-Start` header is not present `wait_timeout` handling is skipped entirely.


### Wait Overtime

Relying on `X-Request-Start` is less than ideal, as it computes the time since the request *started* being received by the web server, rather than the time the request *finished* being received by the web server. That poses a problem for lengthy requests.

Lengthy requests are requests with a body, such as POST requests. These take time to complete being received by the application server, especially when the client has a slow upload speed, as is common for example with mobile clients or asymmetric connections.

While we can infer the time since a request started being received, we can't tell when it completed being received, which would be preferable. We're also unable to tell the time since the last byte was sent in the request, which would be relevant in tracking Heroku's router timeout appropriately.

A request that took longer than 30s to be fully received, but that had been uploading data all that while, would be dropped immediately by Rack::Timeout because it'd be considered too old. Heroku's router, however, would not have dropped this request because data was being transmitted all along.

As a concession to these shortcomings, for requests that have a body present, we allow some additional wait time on top of `wait_timeout`. This aims to make up for time lost to long uploads.

This extra time is called *wait overtime* and can be set via `Rack::Timeout.wait_overtime`. It defaults to 60 seconds. This can be disabled as usual by setting the property to `0` or `false`. When disabled, there's no overtime. If you want lengthy requests to never get expired, set `wait_overtime` to a very high number.

Keep in mind that Heroku [recommends][uploads] uploading large files directly to S3, so as to prevent the dyno from being blocked for too long and hence unable to handle further incoming requests.

[uploads]: https://devcenter.heroku.com/articles/s3#file-uploads


### Timing Out During IO Blocks

Sometimes a request is taking too long to complete because it's blocked waiting on synchronous IO. Such IO does not need to be file operations, it could be, say, network or database operations. If said IO is happening in a C library that's unaware of ruby's interrupt system (i.e. anything written without ruby in mind), calling `Thread#raise` (that's what rack-timeout uses) will not have effect until after the IO block is gone.

At the moment rack-timeout does not try to address this issue. As a fail-safe against these cases, a blunter solution that kills the entire process is recommended, such as unicorn's timeouts.

More detailed explanations of the issues surrounding timing out in ruby during IO blocks can be found at:

- http://redgetan.cc/understanding-timeouts-in-cruby/
- https://shellycloud.com/blog/2013/06/the-pesky-problem-of-freezing-thin


### Timing Out Inherently Unsafe

Raising mid-flight in stateful applications is inherently unsafe. A request can be aborted at any moment in the code flow, and the application cam be left in an inconsistent state. There's little way rack-timeout could be aware of ongoing state changes. Applications that rely on a set of globals (like class variables) or any other state that lives beyond a single request may find those left in an unexpected/inconsistent state after an aborted request. Some cleanup code might not have run, or only half of a set of related changes may have been applied.

A lot more can go wrong. An intricate explanation of the issue by JRuby's Charles Nutter can be found [here][broken-timeout].

Ruby 2.1 provides a way to defer the result of raising exceptions through the [Thread.handle_interrupt][handle-interrupt] method. This could be used in critical areas of your application code to prevent Rack::Timeout from accidentally wreaking havoc by raising just in the wrong moment. That said, `handle_interrupt` and threads in general are hard to reason about, and detecting all cases where it would be needed in an application is a tall order, and the added code complexity is probably not worth the trouble.

Your time is better spent ensuring requests run fast and don't need to timeout.

That said, it's something to be aware of, and may explain some eerie wonkiness seen in logs.

[broken-timeout]: http://headius.blogspot.de/2008/02/rubys-threadraise-threadkill-timeoutrb.html
[handle-interrupt]: http://www.ruby-doc.org/core-2.1.3/Thread.html#method-c-handle_interrupt


Request Lifetime
----------------

Throughout a request's lifetime, Rack::Timeout keeps details about the request in `env[Rack::Timeout::ENV_INFO_KEY]`, or, more explicitly, `env["rack-timeout.info"]`.

The value of that entry is an instance of `Rack::Timeout::RequestDetails`, which is a `Struct` consisting of the following fields:

*   `id`: a unique ID per request. Either the value of the `X-Request-ID` header or a random ID
    generated internally.

*   `wait`: time in seconds since `X-Request-Start` at the time the request was initially seen by Rack::Timeout. Only set if `X-Request-Start` is present.

*   `timeout`: the final timeout value that was used or to be used, in seconds. For `expired` requests, that would be the `wait_timeout`, possibly with `wait_overtime` applied. In all other cases it's the `service_timeout`, potentially reduced to make up for time lost waiting. (See discussion regarding `service_past_wait` above, under the Wait Timeout section.)

*   `service`: set after a request completes (or times out). The time in seconds it took being processed. This is also updated while a request is still active, around every second, with the time taken so far.

*   `state`: the possible states, and their log level, are:

    *   `expired` (`ERROR`): the request is considered too old and is skipped entirely. This happens when `X-Request-Start` is present and older than `wait_timeout`. When in this state, a `Rack::Timeout::RequestExpiryError` exception is raised. See earlier discussion about the `wait_overtime` setting, too.

    *   `ready` (`INFO`): this is the state a request is in right before it's passed down the middleware chain. Once it's being processed, it'll move on to `active`, and then on to `timed_out` and/or `completed`.

    *   `active` (`DEBUG`): the request is being actively processed in the application thread. This is signaled repeatedly every ~1s until the request completes or times out.

    *   `timed_out` (`ERROR`): the request ran for longer than the determined timeout and was aborted. A `Rack::Timeout::RequestTimeoutError` error is raised in the application when this occurs. If this error gets caught, handled, and not re-raised in the app or framework (which will generally happen with Rails and Sinatra), this state will not be final, `completed` will be set after the framework is done with it.

    *   `completed` (`INFO`): the request completed and Rack::Timeout is done with it. This does not mean the request completed *successfully*. Rack::Timeout does not concern itself with that. As mentioned just above, a timed out request may still end up with a `completed` state if the framework has dealt with the timeout exception.


Errors
------

Rack::Timeout can raise two types of exceptions. Both descend from `Rack::Timeout::Error`, which itself descends from `RuntimeError`. They are:

*   `Rack::Timeout::RequestTimeoutError`: this is raised when a request has run for longer than the specified timeout. It's raised by the rack-timeout timer thread in the application thread, at the point in the stack the app happens to be in when the timeout is triggered. This exception can generally be caught within the application, but in doing so you're working past the timeout. This is ok for quick cleanup work but shouldn't be abused as Rack::Timeout will not kick in twice for the same request.

*   `Rack::Timeout::RequestExpiryError`: this is raised when a request is skipped for being too old (see Wait Timeout section). This error cannot generally be rescued from inside a Rails controller action as it happens before the request has a chance to enter Rails.

    This shouldn't be different for other frameworks, unless you have something above Rack::Timeout in the middleware stack, which you generally shouldn't.

You shouldn't rescue from these errors for reporting purposes. Instead, you can subscribe for state change notifications with observers.

If you're trying to test that a `Rack::Timeout::RequestTimeoutError` is raised in an action in your Rails application, you **must do so in integration tests**. Please note that Rack::Timeout will not kick in for functional tests as they bypass the rack middleware stack.

[More details about testing middleware with Rails here][pablobm].

[pablobm]: http://stackoverflow.com/a/8681208/13989


Observers
---------

Observers are blocks that are notified about state changes during a request's lifetime. Keep in mind that the `active` state is set every ~1s, so you'll be notified every time.

You can register an observer with:

```ruby
Rack::Timeout.register_state_change_observer(:a_unique_name) { |env| do_things env }
```

There's currently no way to subscribe to changes into or out of a particular state. To check the actual state we're moving into, read `env['rack-timeout.info'].state`. Handling going out of a state would require some additional logic in the observer.

You can remove an observer with `unregister_state_change_observer`:

```ruby
Rack::Timeout.unregister_state_change_observer(:a_unique_name)
```


rack-timeout's logging is implemented using an observer; see `Rack::Timeout::StageChangeLoggingObserver` in logger.rb for the implementation.

Custom observers might be used to do cleanup, store statistics on request length, timeouts, etc., and potentially do performance tuning on the fly.


Logging
-------

Rack::Timeout logs a line every time there's a change in state in a request's lifetime.

Request state changes into `timed_out` and `expired` are logged at the `ERROR` level, most other things are logged as `INFO`. The `active` state is logged as `DEBUG`, every ~1s while the request is still active.

Rack::Timeout will try to use `Rails.logger` if present, otherwise it'll look for a logger in `env['rack.logger']`, and if neither are present, it'll create its own logger, either writing to `env['rack.errors']`, or to `$stderr` if the former is not set.

A custom logger can be set via `Rack::Timeout::StageChangeLoggingObserver.logger`. This takes priority over the automatic logger detection:

```ruby
Rack::Timeout::StageChangeLoggingObserver.logger = Logger.new
```

When creating its own logger, rack-timeout will use a log level of `INFO`. Otherwise whatever log level is already set on the logger being used continues in effect.

Logging is enabled by default if Rack::Timeout is loaded via the `rack-timeout` file (recommended), but can be removed by unregistering its observer:

```ruby
Rack::Timeout.unregister_state_change_observer(:logger)
```

Each log line is a set of `key=value` pairs, containing the entries from the `env["rack-timeout.info"]` struct that are not `nil`. See the Request Lifetime section above for a description of each field. Note that while the values for `wait`, `timeout`, and `service` are stored internally as seconds, they are logged as milliseconds for readability.

A sample log excerpt might look like:

```
source=rack-timeout id=13793c wait=369ms timeout=10000ms state=ready at=info
source=rack-timeout id=13793c wait=369ms timeout=10000ms service=15ms state=completed at=info
source=rack-timeout id=ea7bd3 wait=371ms timeout=10000ms state=timed_out at=error
```


Compatibility
-------------

This version of Rack::Timeout is compatible with Ruby 1.9.1 and up, and, for Rails apps, Rails 3.x and up.

For applications running Ruby 1.8.x and/or Rails 2.x, use [version 0.0.4][v0.0.4].

[v0.0.4]: https://github.com/heroku/rack-timeout/tree/v0.0.4


---
Copyright © 2010-2014 Caio Chassot, released under the MIT license  
<http://github.com/heroku/rack-timeout>
# Rails 12factor [![Build Status](https://travis-ci.org/heroku/rails_12factor.png)](https://travis-ci.org/heroku/rails_12factor)

Makes running your Rails app easier. Based on the ideas behind [12factor.net](http://12factor.net)

## What

Rails gets a lot right when it comes to twelve-factor apps, but it could still be better. The two biggest areas right now are that in production [logs should be directed to stdout](http://www.12factor.net/logs) and [dev/prod parity](http://www.12factor.net/dev-prod-parity) while delivering assets.

This gem enables serving assets in production and setting your logger to standard out, both of which are required to run a Rails 4 application on a twelve-factor provider. The gem also makes the appropriate changes for Rails 3 apps.

## Install

In your `Gemfile` add:

```ruby
gem 'rails_12factor', group: :production
```

Then run

```sh
$ bundle install
```

Now you're good to go.

## How

This gem adds two other gems `rails_serve_static_assets` and `rails_stdout_logging`. These gems are required to run your Rails app with both logging aggregation and static assets serving in production. All you need to do to get the functionality of both gems is to add the `rails_12factor` gem to your project. Here is how they work:

## Rails 4 Logging

By default Rails writes its logs to a specific file, which is convenient if you only have one log file to tail. When you start scaling to multiple instances running your app, finding a single request or failure across multiple files becomes much harder. Storing logs on disk can also take down a server if the hard drive fills up. Because of these limitations, every Rails core member we’ve  talked to uses a custom logger to replace Rail's default functionality. By using the `rails_stdout_logging` gem, the logger is set for you.

The gem `rails_stdout_logging` ensures that your logs will be sent to standard out, and from there the twelve-factor platform can send them to a log aggregation service ( like  [logplex](https://github.com/heroku/logplex) on Heroku, or [Papertrail](https://papertrailapp.com)) so you can access them from one place. By using stdout instead of files, you can [treat logs as event streams](http://www.12factor.net/logs).


## Rails 4 Serve Static Assets

In the default Rails development environment assets are served through a middleware called [sprockets](https://github.com/sstephenson/sprockets). In production however most one-off Rails deployments will put their ruby server behind a reverse HTTP proxy server such as Nginx, which can then load balance the app and serve static files directly. When Nginx sees a request for an asset such as `/assets/rails.png` it will grab it from disk at `/public/assets/rails.png` and serve it. The Rails server will never see these requests.

On a twelve-factor platform, Nginx is typically not required to run your application. Your app should be capable of handling requests directly, or through a [routing layer](https://devcenter.heroku.com/articles/http-routing) that may handle load balancing while you scale out horizontally. Note that the caching behavior of Nginx is not needed if your application is serving static assets through an [edge caching CDN](https://en.wikipedia.org/wiki/Content_delivery_network), which is generally recommended.

By default Rails 4 will return a 404 if an asset is not handled via an external proxy such as Nginx. While this default behavior may help you debug your Nginx configuration, it makes a default Rails app with assets unusable on a twelve-factor platform. To fix this we've released a gem: `rails_serve_static_assets`.

The `rails_serve_static_assets` gem enables your Rails server to deliver your assets directly, instead of returning a 404. You can use this to populate an edge cache CDN, or serve files directly from your web app. This gives your app total control, allowing you to do things like redirects or setting headers in your Ruby code. The gem achieves this behavior in your app by simply setting a single configuration option, `config.serve_static_assets = true`. By using the `rails_serve_static_assets` gem, you do not need to set this configuration manually.



## The Future

We will be working with Rails and the Rails core team to make future versions of Rails work on twelve-factor platforms out of the box. Until then you'll need to add this gem to your project.

# Coffee-Rails

CoffeeScript adapter for the Rails asset pipeline. Also adds support to use CoffeeScript to respond to JavaScript requests (use .js.coffee views).

## Installation

Since Rails 3.1 Coffee-Rails is included in the default Gemfile when you create a new application. If you are upgrading to Rails 3.1 you must add the coffee-rails to your Gemfile:

    gem 'coffee-rails'

If you are precompiling your assets (with rake assets:precompile) before run your application in production, you might want add it to the assets group to prevent the gem being required in the production environment. _Note that this may prevent you from using Coffeescript for UJS responses_.

    group :assets do
      gem 'coffee-rails'
    end

## Running tests

    $ bundle install
    $ bundle exec rake test

If you need to test against local gems, use Bundler's gem :path option in the Gemfile.

## Code Status

* [![Travis CI](https://api.travis-ci.org/rails/coffee-rails.png)](http://travis-ci.org/rails/coffee-rails)
* [![Gem Version](https://badge.fury.io/rb/coffee-rails.png)](http://badge.fury.io/rb/coffee-rails)
* [![Dependencies](https://gemnasium.com/rails/coffee-rails.png)](https://gemnasium.com/rails/coffee-rails)
TZInfo - Ruby Timezone Library
==============================

[![Gem Version](https://badge.fury.io/rb/tzinfo.svg)](http://badge.fury.io/rb/tzinfo) [![Build Status](https://travis-ci.org/tzinfo/tzinfo.svg?branch=master)](https://travis-ci.org/tzinfo/tzinfo)

[TZInfo](http://tzinfo.github.io) provides daylight savings aware 
transformations between times in different timezones.


Data Sources
------------

TZInfo requires a source of timezone data. There are two built-in options:

1. The TZInfo::Data library (the tzinfo-data gem). TZInfo::Data contains a set 
   of Ruby modules that are generated from the [IANA Time Zone Database](http://www.iana.org/time-zones).
2. A zoneinfo directory. Most Unix-like systems include a zoneinfo directory 
   containing timezone definitions. These are also generated from the 
   [IANA Time Zone Database](http://www.iana.org/time-zones).

By default, TZInfo::Data will be used. If TZInfo::Data is not available (i.e. 
if `require 'tzinfo/data'` fails), then TZInfo will search for a zoneinfo
directory instead (using the search path specified by 
`TZInfo::ZoneinfoDataSource::DEFAULT_SEARCH_PATH`).

If no data source can be found, a `TZInfo::DataSourceNotFound` exception will be
raised when TZInfo is used. Further information is available 
[in the wiki](http://tzinfo.github.io/datasourcenotfound) to help with 
resolving `TZInfo::DataSourceNotFound` errors.

The default data source selection can be overridden using 
`TZInfo::DataSource.set`.

Custom data sources can also be used. See `TZInfo::DataSource.set` for
further details.


Installation
------------

The TZInfo gem can be installed by running:

    gem install tzinfo

To use the Ruby modules as the data source, TZInfo::Data will also need to be
installed:

    gem install tzinfo-data
  

Example Usage
-------------

The following code will obtain the America/New_York timezone (as an instance
of `TZInfo::Timezone`) and convert a time in UTC to local New York time:

    require 'tzinfo'
    
    tz = TZInfo::Timezone.get('America/New_York')
    local = tz.utc_to_local(Time.utc(2005,8,29,15,35,0))

Note that the local Time returned will have a UTC timezone (`local.zone` will 
return `"UTC"`). This is because the Ruby Time class only supports two timezones: 
UTC and the current system local timezone.
  
To convert from a local time to UTC, the `local_to_utc` method can be used as
follows:

    utc = tz.local_to_utc(local)

Note that the timezone information of the local Time object is ignored (TZInfo
will just read the date and time and treat them as if there were in the `tz`
timezone). The following two lines will return the same result regardless of 
the system's local timezone:

    tz.local_to_utc(Time.local(2006,6,26,1,0,0))
    tz.local_to_utc(Time.utc(2006,6,26,1,0,0))
  
To obtain information about the rules in force at a particular UTC or local 
time, the `TZInfo::Timezone.period_for_utc` and 
`TZInfo::Timezone.period_for_local` methods can be used. Both of these methods 
return `TZInfo::TimezonePeriod` objects. The following gets the identifier for 
the period (in this case EDT).

    period = tz.period_for_utc(Time.utc(2005,8,29,15,35,0))
    id = period.zone_identifier
  
The current local time in a `Timezone` can be obtained with the 
`TZInfo::Timezone#now` method:

    now = tz.now

All methods in TZInfo that operate on a time can be used with either `Time` or 
`DateTime` instances or with Integer timestamps (i.e. as returned by 
`Time#to_i`). The type of the values returned will match the type passed in.

A list of all the available timezone identifiers can be obtained using the
`TZInfo::Timezone.all_identifiers` method. `TZInfo::Timezone.all` can be called
to get an `Array` of all the `TZInfo::Timezone` instances.

Timezones can also be accessed by country (using an ISO 3166-1 alpha-2 country 
code). The following code retrieves the `TZInfo::Country` instance representing 
the USA (country code 'US') and then gets all the timezone identifiers used in 
the USA.

    us = TZInfo::Country.get('US')
    timezones = us.zone_identifiers
  
The `TZInfo::Country#zone_info` method provides an additional description and 
geographic location for each timezone in a country.

A list of all the available country codes can be obtained using the
`TZInfo::Country.all_codes` method. `TZInfo::Country.all` can be called to get 
an `Array` of all the `Country` instances.
  
For further detail, please refer to the API documentation for the 
`TZInfo::Timezone` and `TZInfo::Country` classes.


Thread-Safety
-------------

The `TZInfo::Country` and `TZInfo::Timezone` classes are thread-safe. It is safe
to use class and instance methods of `TZInfo::Country` and `TZInfo::Timezone` in 
concurrently executing threads. Instances of both classes can be shared across 
thread boundaries.


Documentation
-------------

API documentation for TZInfo is available on [RubyDoc.info](http://rubydoc.info/gems/tzinfo/frames).


License
-------

TZInfo is released under the MIT license, see LICENSE for details.


Source Code
-----------

Source code for TZInfo is available on [GitHub](https://github.com/tzinfo/tzinfo).


Issue Tracker
-------------

Please post any bugs, issues, feature requests or questions to the 
[GitHub issue tracker](https://github.com/tzinfo/tzinfo/issues).
