jQuery.kinetic
==============
Dave Taylor <http://davetayls.me>
The MIT License (MIT)

> This code has been pretty stable for a while (with it's few restrictions) and so am not actively making changes. If you want to improve it in any way feel free to submit a pull request (with tests) and I will merge in any that make sense and don't add bloat to what is a simple plugin.

Master: [![Build Status](https://secure.travis-ci.org/davetayls/jquery.kinetic.png?branch=master)](http://travis-ci.org/davetayls/jquery.kinetic)

All branches: [![Build Status](https://secure.travis-ci.org/davetayls/jquery.kinetic.png)](http://travis-ci.org/davetayls/jquery.kinetic)

jQuery.kinetic is a simple plugin which adds smooth drag scrolling with
gradual deceleration to containers.

## Installation

### Bower

	$ bower install jquery.kinetic --save

### Script tag
You can add the script to the page.

	<script src="jquery.kinetic.js"></script>

## Major new release 2.0 has BREAKING CHANGES

See release history below for details.

## Compatibility

This plugin works with [jQuery](http://jquery.com) and
[Zepto](http://zeptojs.com/)

### Browsers ###

- ie: 7,8,9
- firefox: 3.6,4,5
- chrome: 13
- safari: 5
- iOS Safari: 4

## Demos
Take a look at a demo on <http://davetayls.me/jquery.kinetic>.

Filtering Clickable elements
---

If you need to allow events to be passed through the wrapper. For example to allow clicking on a link or an input then you can use `filterTarget` like so.

```javascript
$('#wrapper').kinetic({
    filterTarget: function(target, e){
        if (!/down|start/.test(e.type)){
            return !(/area|a|input/i.test(target.tagName));
        }
    }
});
```

## Options

    cursor          {string}    default: move   Specify the cursor to use on the wrapper
    slowdown        {number}    default: 0.9    This option affects the speed at which the scroll slows
    threshold       {number|function(target, e)}    default: 0   This is the number of pixels the mouse needs to move before the element starts scrolling
    x               {string}    default: true   Toggles movement along the x axis
    y               {string}    default: true   Toggles movement along the y axis
    maxvelocity     {number}    default: 40     This option puts a cap on speed at which the container
                                                can scroll
    throttleFPS     {number}    default: 60     This adds throttling to the mouse move events to boost
                                                performance when scrolling
    triggerHardware {boolean} false             This adds css to the wrapper which
                                                will trigger iOS to use hardware acceleration

    filterTarget    {function(target)}          Return false from this function to
                                                prevent capturing the scroll

    movingClass     {object}
        up:         {string}    default: 'kinetic-moving-up'
        down:       {string}    default: 'kinetic-moving-down'
        left:       {string}    default: 'kinetic-moving-left'
        right:      {string}    default: 'kinetic-moving-right'

    deceleratingClass {object}
        up:         {string}    default: 'kinetic-decelerating-up'
        down:       {string}    default: 'kinetic-decelerating-down'
        left:       {string}    default: 'kinetic-decelerating-left'
        right:      {string}    default: 'kinetic-decelerating-right'

    Listeners:  All listeners are called with:
                - this = the instance of the Kinetic class

    moved       {function()}           A function which is called on every move
    stopped     {function()}           A function which is called once all
                                               movement has stopped

    Methods:    You can call methods by running the kinetic plugin
                on an element which has already been activated.

                eg  $('#wrapper').kinetic(); // activate
                    $('#wrapper').kinetic('methodname', options);

    start       Start movement in the scroll container at a particular velocity.
                This velocity will not slow until the end method is called.

                The following line scrolls the container left.
                $('#wrapper#).kinetic('start', { velocity: -30 });

                The following line scrolls the container right.
                $('#wrapper#).kinetic('start', { velocity: 30 });

                The following line scrolls the container diagonally.
                $('#wrapper#).kinetic('start', { velocity: -30, velocityY: -10 });

    end         Begin slowdown of any scrolling velocity in the container.
                $('#wrapper#).kinetic('end');

    stop        Stop the scrolling immediately

    detach      Detach listeners and functionality from the wrapper

    attach      Re-attach listeners and functionality previously detached using
                the detach method

Add your own methods
--------------------

There are some example methods in the `extra-methods` folder. You can also add your own.

	$.Kinetic.prototype.do = function(options){
	  // this -> instance of Kinetic
	  // this.settings -> get current settings
	  // options -> options passed in from call
	};
	
	// use the method
	$('#elem').kinetic('do', { options });

Hack the core
-------------

You can now hook in to the core functionality to make changes.

    var _start = $.Kinetic.prototype.start;
    $.Kinetic.prototype.start = function(options){
   	  // -> do something
   	  _start.apply(this, arguments);
    };


Running the tests
-------

The test suite uses grunt's server and qunit functionality. The tests are being built up
but currently cover the core functionality. This runs all qUnit Html specs in the
`/test/specs` folder.

- grunt `npm install -g grunt`
- install devDependencies `npm install` from the root of the source

Then run from the root of the source

    $ grunt

### Manual tests

There are manual tests as html files within the `/test` folder.

Releasing a new version
-----------------------

Releasing a small fix or change. The following will update the patch version
number.

    $ grunt release
    
Releasing a potentially breaking feature. The following will update the minor
version number.

    $ grunt release:minor

Changes
-------
### 2.1.0
 - Added `threshold` option (@UziTech) https://github.com/davetayls/jquery.kinetic/pull/84
 
### 2.0.6
 - Fix touch and mouse bindings so that an external pointing device can be used with a touchscreen device.

### 2.0.5
 - Fix detach scroll event for touch devices (@Jaemu)

### 2.0.4
 - Fix the useTarget call to include the event as per the example in the readme for ignoring scroll events. (@mooreOn)

### 2.0.3
 - only prevent drag and drop if element is usable target (@andrew-pause)

### 2.0.1

 - changes to allow attaching to `<body>` with `$('body').kinetic()` #61

### 2.0

After several years, this plugin has had a major refactor. Big thanks to (@skovhus) for helping with this rewrite. Here's what has happened.

- rewrite of plugin to an OO plugin
- **BREAKING CHANGES**
  - call methods are now attached to the `$.Kinetic.prototype` and have
    slightly different arguments (see docs above)
  - no more $.kinetic namespace
  - `Kinetic` constructor is attached to $.Kinetic
  - `$('#wrapper').data('kinetic-settings')` has been removed in favour of
    `instance = $('#wrapper').data('kinetic'); settings = instance.settings`
  - All events `this` context is now the instance of `Kinetic`. 
    To access the `$scroller` which was previously the context you can use `this.$el`

### 1.8.2
- fix #34, #28, now will discard any subsequent attempts to bind `.kinetic()`

### 1.8.1
- tweak to hardware trigger css (@edmelly)
- upgrade to Grunt 0.4

### 1.8
- add scroll listener to trigger move events (@dennipahmah)

### 1.7
- add cursor option to change the default `move` cursor

### 1.6.1
- bug fix release for unbinding touch events

### 1.6
- use bind for touch events to fix issues on android

### 1.5
- added ability to prevent capturing scroll depending on the target
- fix for using alongside jQuery UI draggable #14 - thanks @sidoh, @NilsHolmstrom

### 1.4
- added ability to nest containers thanks @cc-lam
- added detach/attach methods
- added triggerHardware option

### 1.3
- IE bug fixes when dragging images
- Adding extensibility for methods by attaching functions to jQuery.

        // add the method
        $.kinetic.callMethods.do = function(settings, options){
            // method functionality
        };

        // use the method
        $('#elem').kinetic('do', { ... });

- Added stop method
- Fix bug with ignored axis triggering animation frames



# Chroma.js

Chroma.js is a tiny JavaScript library (8.5kB) for all kinds of color conversions and color scales.

### Usage


Initiate and manipulate colors:

```javascript
chroma('#D4F880').darken().hex();  // #9BC04B
```

Working with color scales is easy, too:

```javascript    
scale = chroma.scale(['white', 'red']);
scale(0.5).hex(); // #FF7F7F
```

Lab/Lch interpolation looks better than than RGB

```javascript    
chroma.scale(['white', 'red']).mode('lab');
```

Custom domains! Quantiles! Color Brewer!! 

```javascript    
chroma.scale('RdYlBu').domain(myValues, 7, 'quantiles');    
```

And why not use logarithmic color scales once in your life?

```javascript
chroma.scale(['lightyellow', 'navy']).domain([1, 100000], 7, 'log');    
```

### Like it?

Why not dive into the [API docs](https://github.com/gka/chroma.js/blob/master/doc/api.md) (quite short actually), and download [chroma.min.js](https://raw.github.com/gka/chroma.js/master/chroma.min.js) right away.

You can use it in node.js, too!

    npm install chroma-js


### Build instructions

To compile the coffee-script source files you have to run ``build.sh``.

To run the tests simply run

    vows test/*.coffee


### Similar Libraries / Prior Art

* [Chromatist](https://github.com/jrus/chromatist)
* [GrapeFruit](https://github.com/xav/Grapefruit) (Python)
* [colors.py](https://github.com/mattrobenolt/colors.py) (Python)
* [d3.js](https://github.com/mbostock/d3)


### Author

Chroma.js is written by [Gregor Aisch](http://driven-by-data.net).

### License

Released under [BSD license](http://opensource.org/licenses/BSD-3-Clause).
Versions prior to 0.4 were released under [GPL](http://www.gnu.org/licenses/gpl-3.0).

### Known issues

* HSI color conversion is experimental and produces weird results sometimes

### Further reading

* [How To Avoid Equidistant HSV Colors](https://vis4.net/blog/posts/avoid-equidistant-hsv-colors/)
* [Mastering Multi-hued Color Scales with Chroma.js](https://vis4.net/blog/posts/mastering-multi-hued-color-scales/)
# The HTML5 Shiv

The HTML5 Shiv enables use of HTML5 sectioning elements in legacy Internet Explorer and provides basic HTML5 styling for Internet Explorer 6-9, Safari 4.x (and iPhone 3.x), and Firefox 3.x.

### What do these files do?

#### `html5shiv.js`
*  This includes the basic `createElement()` shiv technique, along with monkeypatches for `document.createElement` and `document.createDocumentFragment` for IE6-8. It also applies [basic styling](https://github.com/aFarkas/html5shiv/blob/51da98dabd3c537891b7fe6114633fb10de52473/src/html5shiv.js#L216-220) for HTML5 elements for IE6-9, Safari 4.x and FF 3.x.

####`html5shiv-printshiv.js` 
*  This includes all of the above, as well as a mechanism allowing HTML5 elements to be styled and contain children while being printed in IE 6-8.

### Who can I get mad at now?

HTML5 Shiv is maintained by [Alexander Farkas](https://github.com/aFarkas/), [Jonathan Neal](https://twitter.com/jon_neal) and [Paul Irish](https://twitter.com/paul_irish), with many contributions from [John-David Dalton](https://twitter.com/jdalton). It is also distributed with [Modernizr](http://modernizr.com/).

If you have any issues in these implementations, you can report them here! :)

For the full story of HTML5 Shiv and all of the people involved in making it, read [The Story of the HTML5 Shiv](http://paulirish.com/2011/the-history-of-the-html5-shiv/).

## Installation

###Using [Bower](http://bower.io/)

`bower install html5shiv --save-dev`

This will clone the latest version of the HTML5 shiv into the `bower_components` directory at the root of your project and also create or update the file `bower.json` which specifies your projects dependencies.

Include the HTML5 shiv in the `<head>` of your page in a conditional comment and after any stylesheets.

```html
<!--[if lt IE 9]>
	<script src="bower_components/html5shiv/dist/html5shiv.js"></script>
<![endif]-->
```

###Manual installation

Download and extract the [latest zip package](https://github.com/aFarkas/html5shiv/archive/master.zip) from this repositiory and copy the two files `dist/html5shiv.js` and `dist/html5shiv-printshiv.js` into your project. Then include one of them into your `<head>` as above. 

## HTML5 Shiv API

HTML5 Shiv works as a simple drop-in solution. In most cases there is no need to configure HTML5 Shiv or use methods provided by HTML5 Shiv.

### `html5.elements` option

The `elements` option is a space separated string or array, which describes the **full** list of the elements to shiv. see also `addElements`.

**Configuring `elements` before `html5shiv.js` is included.**

```js
//create a global html5 options object
window.html5 = {
  'elements': 'mark section customelement' 
};
```
**Configuring `elements` after `html5shiv.js` is included.**

```js
//change the html5shiv options object 
window.html5.elements = 'mark section customelement';
//and re-invoke the `shivDocument` method
html5.shivDocument(document);
```

### `html5.shivCSS`

If `shivCSS` is set to `true` HTML5 Shiv will add basic styles (mostly display: block) to sectioning elements (like section, article). In most cases a webpage author should include those basic styles in his normal stylesheet to ensure older browser support (i.e. Firefox 3.6) without JavaScript.

The `shivCSS` is true by default and can be set false, only before html5shiv.js is included: 

```js
//create a global html5 options object
window.html5 = {
	'shivCSS': false
};
```

### `html5.shivMethods`

If the `shivMethods` option is set to `true` (by default) HTML5 Shiv will override `document.createElement`/`document.createDocumentFragment` in Internet Explorer 6-8 to allow dynamic DOM creation of HTML5 elements. 

Known issue: If an element is created using the overridden `createElement` method this element returns a document fragment as its `parentNode`, but should be normally `null`. If a script relies on this behavior, `shivMethods`should be set to `false`.
Note: jQuery 1.7+ has implemented his own HTML5 DOM creation fix for Internet Explorer 6-8. If all your scripts (including Third party scripts) are using jQuery's manipulation and DOM creation methods, you might want to set this option to `false`.

**Configuring `shivMethods` before `html5shiv.js` is included.**

```js
//create a global html5 options object
window.html5 = {
	'shivMethods': false
};
```
**Configuring `elements` after `html5shiv.js` is included.**

```js
//change the html5shiv options object 
window.html5.shivMethods = false;
```

### `html5.addElements( newElements [, document] )`

The `html5.addElements` method extends the list of elements to shiv. The newElements argument can be a whitespace separated list or an array.

```js
//extend list of elements to shiv
html5.addElements('element content');
```

### `html5.createElement( nodeName [, document] )`

The `html5.createElement` method creates a shived element, even if `shivMethods` is set to false.

```js
var container = html5.createElement('div');
//container is shived so we can add HTML5 elements using `innerHTML`
container.innerHTML = '<section>This is a section</section>';
```

### `html5.createDocumentFragment( [document] )`

The `html5.createDocumentFragment` method creates a shived document fragment, even if `shivMethods` is set to false.

```js
var fragment = html5.createDocumentFragment();
var container = document.createElement('div');
fragment.appendChild(container);
//fragment is shived so we can add HTML5 elements using `innerHTML`
container.innerHTML = '<section>This is a section</section>';
```

## HTML5 Shiv Known Issues and Limitations

- The `shivMethods` option (overriding `document.createElement`) and the `html5.createElement` method create elements, which are not disconnected and have a parentNode (see also issue #64)
- The cloneNode problem is currently not addressed by HTML5 Shiv. HTML5 elements can be dynamically created, but can't be cloned in all cases.
- The printshiv version of HTML5 Shiv has to alter the print styles and the whole DOM for printing. In case of complex websites and or a lot of print styles this might cause performance and/or styling issues. A possible solution could be the [htc-branch](https://github.com/aFarkas/html5shiv/tree/iepp-htc) of HTML5 Shiv, which uses another technique to implement print styles for Internet Explorer 6-8.

### What about the other HTML5 element projects?

- The original conception and community collaboration story of the project is described at [The History of the HTML5 Shiv](http://paulirish.com/2011/the-history-of-the-html5-shiv/). 
- [IEPP](https://code.google.com/p/ie-print-protector), by Jon Neal, addressed the printing fault of the original `html5shiv`. It was merged into `html5shiv`.
- **Shimprove**, in April 2010, patched `cloneNode` and `createElement` was later merged into `html5shiv`
- **innerShiv**, introduced in August 2010 by JD Barlett, addressed dynamically adding new HTML5 elements into the DOM. [jQuery added support](http://blog.jquery.com/2011/11/03/jquery-1-7-released/) that made innerShiv redundant and `html5shiv` addressed the same issues as well, so the project was completed.
- The **html5shim** and **html5shiv** sites on Google Code are maintained by Remy Sharp and are identical distribution points of this `html5shiv` project.
- **Modernizr** is developed by the same people as `html5shiv` and can include the latest version in any custom builds created at modernizr.com
- This `html5shiv` repo now contains tests for all the edge cases pursued by the above libraries and has been extensively tested, both in development and production. 

A [detailed changelog of html5shiv](https://github.com/aFarkas/html5shiv/wiki) is available.

### Why is it called a *shiv*?

The term **shiv** [originates](http://ejohn.org/blog/html5-shiv/) from [John Resig](https://github.com/jeresig), who was thought to have used the word for its slang meaning, *a sharp object used as a knife-like weapon*, intended for Internet Explorer. Truth be known, John probably intended to use the word [shim](http://en.wikipedia.org/wiki/Shim_(computing)), which in computing means *an application compatibility workaround*. Rather than correct his mispelling, most developers familiar with Internet Explorer appreciated the visual imagery. And that, [kids](http://html5homi.es/), is [etymology](https://en.wikipedia.org/wiki/Etymology).
This folder is for the census site from 2013-2014. 
This folder contains all the images for the index static pages
Do not delete this folder or it will break the images
Leaflet.label
=============

**NOTE: lastest Leaflet.label master requires Leaflet 0.7-dev**

Leaflet.label is plugin for adding labels to markers &amp; shapes on leaflet powered maps.

Check out the [demo](http://leaflet.github.com/Leaflet.label/).

##Usage examples

If you want to just bind a label to marker that will show when the mouse is over it, it's really easy:

````js
L.marker([-37.7772, 175.2606]).bindLabel('Look revealing label!').addTo(map);
````

Path overlays works the same:

````js
L.polyline([
	[-37.7612, 175.2756],
	[-37.7702, 175.2796],
	[-37.7802, 175.2750],
]).bindLabel('Even polylines can have labels.').addTo(map)	
````

If you would prefer the label to be always visible set the ````noHide: true```` option and call ````showLabel()```` once added to the map:

````js
L.marker([-37.785, 175.263])
	.bindLabel('A sweet static label!', { noHide: true })
	.addTo(map);
````

##Options

When you call ````bindLabel()```` you can pass in an options object. These options are:

 - **noHide**: doesn't attach event handler for showing/hiding the label on mouseover/out.
 - **className**: the css class to add to the label element
 - **direction**: one of `left`|`right`(default)|`auto`. The direction the label displays in relation to the marker. `auto` will choose the optimal direction depending on the position of the marker.

E.g. To create a static label that automatically positions the label

````js
var myIcon = L.icon({
	iconUrl: 'my-icon.png',
	iconSize: [20, 20],
	iconAnchor: [10, 10],
	labelAnchor: [6, 0] // as I want the label to appear 2px past the icon (10 + 2 - 6)
});
L.marker([-37.7772, 175.2606], {
	icon: myIcon
}).bindLabel('My label', {
	noHide: true,
	direction: 'auto'
});
````

##Positioning the label for custom icons

The label is positioned relative to the L.Icon's ````iconAnchor```` option. To reposition the label set the ````labelAnchor```` option of your icon. By default ````labelAnchor```` is set so the label will show vertically centered for the default icon (````L.Icon.Default````).

E.g. Vertically center an icon with ````iconAnchor```` set as the center of the icon:

````js
var myIcon = L.icon({
	iconUrl: 'my-icon.png',
	iconSize: [20, 20],
	iconAnchor: [10, 10],
	labelAnchor: [6, 0] // as I want the label to appear 2px past the icon (10 + 2 - 6)
});
L.marker([-37.7772, 175.2606], {
	icon: myIcon
}).bindLabel('Look revealing label!').addTo(map);
````

When positioning the label L.Label includes a 6px horizontal padding. you will need to take this into account when setting ````labelAnchor````.

##Setting the opacity of a label

You can set the opacity of a label by calling the `setOpacity` method on `L.Marker`. By default the opacity will either be **0** or **1**. 

````js
// Sets opacity of marker to 0.3 and opacity of label to 1
markerLabel.setOpacity(0.3);

// Sets opacity of marker to 0.3 and opacity of label to 0.3
markerLabel.setOpacity(0.3, true);

// Sets opacity of marker to 0 and opacity of label to 0
markerLabel.setOpacity(0);
markerLabel.setOpacity(0, true);

// Sets opacity of marker to 1 and opacity of label to 1
markerLabel.setOpacity(1);
markerLabel.setOpacity(1, true);
````

##Alternative label plugin

My previous label plugin is still available at https://github.com/jacobtoye/Leaflet.iconlabel. This plugin is a little harder to use, however if you want to have both the icon and label bound to the same event this plugin is for you.
tablesorter
===========

###Flexible client-side table sorting
####Getting started

To use the tablesorter plugin, include the jQuery library and the tablesorter plugin inside the head-tag of your HTML document:

```html
<script type="text/javascript" src="/path/to/jquery-latest.js"></script> 
<script type="text/javascript" src="/path/to/jquery.tablesorter.js"></script> 
```

Tablesorter works on all standard HTML tables. You must include THEAD and TBODY tags:

```html
<table id="myTable" class="tablesorter"> 
<thead> 
<tr> 
    <th>Last Name</th> 
    <th>First Name</th> 
    <th>Email</th> 
    <th>Due</th> 
    <th>Web Site</th> 
</tr> 
</thead> 
<tbody> 
<tr> 
    <td>Smith</td> 
    <td>John</td> 
    <td>jsmith@gmail.com</td> 
    <td>$50.00</td> 
    <td>http://www.jsmith.com</td> 
</tr> 
<tr> 
    <td>Bach</td> 
    <td>Frank</td> 
    <td>fbach@yahoo.com</td> 
    <td>$50.00</td> 
    <td>http://www.frank.com</td> 
</tr> 
<tr> 
    <td>Doe</td> 
    <td>Jason</td> 
    <td>jdoe@hotmail.com</td> 
    <td>$100.00</td> 
    <td>http://www.jdoe.com</td> 
</tr> 
<tr> 
    <td>Conway</td> 
    <td>Tim</td> 
    <td>tconway@earthlink.net</td> 
    <td>$50.00</td> 
    <td>http://www.timconway.com</td> 
</tr> 
</tbody> 
</table> 
```

Start by telling tablesorter to sort your table when the document is loaded:

```javascript
$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
); 
```

Click on the headers and you'll see that your table is now sortable! You can also pass in configuration options when you initialize the table. This tells tablesorter to sort on the first and second column in ascending order.

```javascript
$(document).ready(function() 
    { 
        $("#myTable").tablesorter( {sortList: [[0,0], [1,0]]} ); 
    } 
); 
```

For DateTime columns you can specify your format, like this:

```javascript
$(document).ready(function() 
    { 
        $("#myTable").tablesorter( {dateFormat: 'pt'} ); 
    } 
); 
```

The available ones (currently) are: us, pt and uk. (for pt you can use 'dd/MM/yyyy hh:mm:ss')
# Sticky-kit

A jQuery plugin for making smart sticky elements.

See the homepage for directions and examples: <http://leafo.net/sticky-kit/>

License: WTFPL
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
# PubSubJS

[![Build Status](https://travis-ci.org/mroderick/PubSubJS.png)](https://travis-ci.org/mroderick/PubSubJS) [![NPM version](https://badge.fury.io/js/pubsub-js.png)](http://badge.fury.io/js/pubsub-js)

PubSubJS is a [topic-based](http://en.wikipedia.org/wiki/Publish–subscribe_pattern#Message_filtering) [publish/subscribe](http://en.wikipedia.org/wiki/Publish/subscribe) library written in JavaScript.

PubSubJS has synchronisation decoupling, so topics are published asynchronously. This helps keep your program predictable as the originator of topics will not be blocked while consumers process them.

For the adventurous, PubSubJS also supports synchronous topic publication. This can give a speedup in some environments (browsers, not all), but can also lead to some very difficult to reason about programs, where one topic triggers publication of another topic in the same execution chain.

For benchmarks, see [A Comparison of JS Publish/Subscribe Approaches](http://jsperf.com/pubsubjs-vs-jquery-custom-events/51)

#### Single process

PubSubJS is designed to be used within a **single process**, and is not a good candidate for multi-process applications (like [Node.js – Cluster](http://nodejs.org/api/cluster.html) with many sub-processes). If your Node.js app is a single process app, you're good. If it is (or is going to be) a multi-process app, you're probably better off using [redis Pub/Sub](http://redis.io/topics/pubsub) or similar

## Key features

* Dependency free
* Synchronization decoupling
* ES3 compatible. PubSubJS should be able to run everywhere that can execute JavaScript. Browsers, servers, ebook readers, old phones, game consoles.
* AMD / CommonJS module support
* No modification of subscribers (jQuery custom events modify subscribers)
* Easy to understand and use (thanks to synchronization decoupling)
* Small(ish), less than 1kb minified and gzipped

## Getting PubSubJS

There are several ways of getting PubSubJS

* [Download a tagged version](https://github.com/mroderick/PubSubJS/tags) from GitHub
* Install via npm (`npm install pubsub-js`)
* Intall via bower (`bower install pubsub-js`)

## Examples

### Basic example

```javascript
// create a function to subscribe to topics
var mySubscriber = function( msg, data ){
    console.log( msg, data );
};

// add the function to the list of subscribers for a particular topic
// we're keeping the returned token, in order to be able to unsubscribe
// from the topic later on
var token = PubSub.subscribe( 'MY TOPIC', mySubscriber );

// publish a topic asyncronously
PubSub.publish( 'MY TOPIC', 'hello world!' );

// publish a topic syncronously, which is faster in some environments,
// but will get confusing when one topic triggers new topics in the
// same execution chain
// USE WITH CAUTION, HERE BE DRAGONS!!!
PubSub.publishSync( 'MY TOPIC', 'hello world!' );
```

### Cancel specific subscripiton

```javascript
// create a function to receive the topic
var mySubscriber = function( msg, data ){
    console.log( msg, data );
};

// add the function to the list of subscribers to a particular topic
// we're keeping the returned token, in order to be able to unsubscribe
// from the topic later on
var token = PubSub.subscribe( 'MY TOPIC', mySubscriber );

// unsubscribe this subscriber from this topic
PubSub.unsubscribe( token );
```

### Cancel all subscriptions for a function

```javascript
// create a function to receive the topic
var mySubscriber = function( msg, data ){
    console.log( msg, data );
};

// unsubscribe mySubscriber from ALL topics
PubSub.unsubscribe( mySubscriber );
```

### Clear all subscriptions for a topic

```javascript
PubSub.subscribe('a', myFunc1);
PubSub.subscribe('a.b', myFunc2);
PubSub.subscribe('a.b.c', myFunc3);

PubSub.unsubscribe('a.b');
// no further notications for 'a.b' and 'a.b.c' topics
// notifications for 'a' will still get published
```

### Clear all subscriptions

```javascript
PubSub.clearAllSubscriptions();
// all subscriptions are removed
```

### Hierarchical addressing

```javascript
// create a subscriber to receive all topics from a hierarchy of topics
var myToplevelSubscriber = function( msg, data ){
    console.log( 'top level: ', msg, data );
}

// subscribe to all topics in the 'car' hierarchy
PubSub.subscribe( 'car', myToplevelSubscriber );

// create a subscriber to receive only leaf topic from hierarchy op topics
var mySpecificSubscriber = function( msg, data ){
    console.log('specific: ', msg, data );
}

// subscribe only to 'car.drive' topics
PubSub.subscribe( 'car.drive', mySpecificSubscriber );

// Publish some topics
PubSub.publish( 'car.purchase', { name : 'my new car' } );
PubSub.publish( 'car.drive', { speed : '14' } );
PubSub.publish( 'car.sell', { newOwner : 'someone else' } );

// In this scenario, myToplevelSubscriber will be called for all
// topics, three times in total
// But, mySpecificSubscriber will only be called once, as it only
// subscribes to the 'car.drive' topic
```

## Tips

Use "constants" for topics and not string literals. PubSubJS uses strings as topics, and will happily try to deliver your topics with ANY topic. So, save yourself from frustrating debugging by letting the JavaScript engine complain
when you make typos.

### Example of use of "constants"

```javascript
// BAD
PubSub.subscribe("hello", function( msg, data ){
	console.log( data )
});

PubSub.publish("helo", "world");

// BETTER
var MY_TOPIC = "hello";
PubSub.subscribe(MY_TOPIC, function( msg, data ){
	console.log( data )
});

PubSub.publish(MY_TOPIC, "world");
```

### Immediate Exceptions for stack traces in developer tools

As of versions 1.3.2, you can force immediate exceptions (instead of delayed execeptions), which has the benefit of maintaining the stack trace when viewed in dev tools.

This should be considered a development only option, as PubSubJS was designed to try to deliver your topics to all subscribers, even when some fail.

Setting immediate exceptions in development is easy, just tell PubSubJS about it after it's been loaded.

```javascript
PubSub.immediateExceptions = true;
```

## Plugin for jQuery

By default PubSubJS can be used in any browser or CommonJS environment, including [node](http://nodejs.org). Additionally, PubSubJS can be built specifically for jQuery using Rake.

    $ rake jquery

or using Grunt

    $ grunt jquery

Produces jquery.pubsub.js

### Use with jQuery

```javascript
var topic = 'greeting',
    data = 'world'
    subscriber = function sayHello( data ){
        console.log( 'hello ' + data );
    };

// add a subscription
var token = $.pubsub('subscribe', topic, subscriber );

// unsubscribing
$.pubsub('unsubscribe', token)          // remove a specific subscription
$.pubsub('unsubscribe', subscriber);    // remove all subscriptions for subscriber

// publishing a topic
$.pubsub('publish', topic, data);

// publishing topic syncronously
$.pubsub('publishSync', topic, data);
```

In the jQuery build, the global ```PubSub``` global is still available, so you can mix and match both ```Pubsub``` and ```$.pubsub``` as needed.

There is also an article about [Using PubSubJS with jQuery](http://roderick.dk/resources/using-pubsubjs-with-jquery/)

## Contributing to PubSubJS

Please see [CONTRIBUTING.md](CONTRIBUTING.md)

## Future of PubSubJS

* Better and more extensive usage examples


## More about Publish/Subscribe

* [The Many Faces of Publish/Subscribe](http://www.cs.ru.nl/~pieter/oss/manyfaces.pdf) (PDF)
* [Addy Osmani's mini book on Patterns](http://addyosmani.com/resources/essentialjsdesignpatterns/book/#observerpatternjavascript)
* [Publish / Subscribe Systems, A summary of 'The Many Faces of Publish / Subscribe'](http://downloads.ohohlfeld.com/talks/hohlfeld_schroeder-publish_subscribe_systems-dsmware_eurecom2007.pdf)

## Versioning

PubSubJS uses [Semantic Versioning](http://semver.org/) for predictable versioning.

## Changelog

Please see [https://github.com/mroderick/PubSubJS/releases](https://github.com/mroderick/PubSubJS/releases)

## License

MIT: http://mrgnrdrck.mit-license.org

## Alternatives

These are a few alternative projects that also implement topic based publish subscribe in JavaScript.

* http://www.joezimjs.com/projects/publish-subscribe-jquery-plugin/
* http://amplifyjs.com/api/pubsub/
* http://radio.uxder.com/ — oriented towards 'channels', free of dependencies
* https://github.com/pmelander/Subtopic - supports vanilla, underscore, jQuery and is even available in NuGet
# marked

> A full-featured markdown parser and compiler, written in JavaScript. Built
> for speed.

[![NPM version](https://badge.fury.io/js/marked.png)][badge]

## Install

``` bash
npm install marked --save
```

## Usage

Minimal usage:

```js
var marked = require('marked');
console.log(marked('I am using __markdown__.'));
// Outputs: <p>I am using <strong>markdown</strong>.</p>
```

Example setting options with default values:

```js
var marked = require('marked');
marked.setOptions({
  renderer: new marked.Renderer(),
  gfm: true,
  tables: true,
  breaks: false,
  pedantic: false,
  sanitize: true,
  smartLists: true,
  smartypants: false
});

console.log(marked('I am using __markdown__.'));
```

### Browser

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Marked in the browser</title>
  <script src="lib/marked.js"></script>
</head>
<body>
  <div id="content"></div>
  <script>
    document.getElementById('content').innerHTML =
      marked('# Marked in browser\n\nRendered by **marked**.');
  </script>
</body>
</html>
```

## marked(markdownString [,options] [,callback])

### markdownString

Type: `string`

String of markdown source to be compiled.

### options

Type: `object`

Hash of options. Can also be set using the `marked.setOptions` method as seen
above.

### callback

Type: `function`

Function called when the `markdownString` has been fully parsed when using
async highlighting. If the `options` argument is omitted, this can be used as
the second argument.

## Options

### highlight

Type: `function`

A function to highlight code blocks. The first example below uses async highlighting with
[node-pygmentize-bundled][pygmentize], and the second is a synchronous example using
[highlight.js][highlight]:

```js
var marked = require('marked');

var markdownString = '```js\n console.log("hello"); \n```';

// Async highlighting with pygmentize-bundled
marked.setOptions({
  highlight: function (code, lang, callback) {
    require('pygmentize-bundled')({ lang: lang, format: 'html' }, code, function (err, result) {
      callback(err, result.toString());
    });
  }
});

// Using async version of marked
marked(markdownString, function (err, content) {
  if (err) throw err;
  console.log(content);
});

// Synchronous highlighting with highlight.js
marked.setOptions({
  highlight: function (code) {
    return require('highlight.js').highlightAuto(code).value;
  }
});

console.log(marked(markdownString));
```

#### highlight arguments

`code`

Type: `string`

The section of code to pass to the highlighter.

`lang`

Type: `string`

The programming language specified in the code block.

`callback`

Type: `function`

The callback function to call when using an async highlighter.

### renderer

Type: `object`
Default: `new Renderer()`

An object containing functions to render tokens to HTML.

#### Overriding renderer methods

The renderer option allows you to render tokens in a custom manner. Here is an
example of overriding the default heading token rendering by adding an embedded anchor tag like on GitHub:

```javascript
var marked = require('marked');
var renderer = new marked.Renderer();

renderer.heading = function (text, level) {
  var escapedText = text.toLowerCase().replace(/[^\w]+/g, '-');

  return '<h' + level + '><a name="' +
                escapedText +
                 '" class="anchor" href="#' +
                 escapedText +
                 '"><span class="header-link"></span></a>' +
                  text + '</h' + level + '>';
},

console.log(marked('# heading+', { renderer: renderer }));
```
This code will output the following HTML:
```html
<h1>
  <a name="heading-" class="anchor" href="#heading-">
    <span class="header-link"></span>
  </a>
  heading+
</h1>
```

#### Block level renderer methods

- code(*string* code, *string* language)
- blockquote(*string* quote)
- html(*string* html)
- heading(*string* text, *number*  level)
- hr()
- list(*string* body, *boolean* ordered)
- listitem(*string*  text)
- paragraph(*string* text)
- table(*string* header, *string* body)
- tablerow(*string* content)
- tablecell(*string* content, *object* flags)

`flags` has the following properties:

```js
{
    header: true || false,
    align: 'center' || 'left' || 'right'
}
```

#### Inline level renderer methods

- strong(*string* text)
- em(*string* text)
- codespan(*string* code)
- br()
- del(*string* text)
- link(*string* href, *string* title, *string* text)
- image(*string* href, *string* title, *string* text)

### gfm

Type: `boolean`
Default: `true`

Enable [GitHub flavored markdown][gfm].

### tables

Type: `boolean`
Default: `true`

Enable GFM [tables][tables].
This option requires the `gfm` option to be true.

### breaks

Type: `boolean`
Default: `false`

Enable GFM [line breaks][breaks].
This option requires the `gfm` option to be true.

### pedantic

Type: `boolean`
Default: `false`

Conform to obscure parts of `markdown.pl` as much as possible. Don't fix any of
the original markdown bugs or poor behavior.

### sanitize

Type: `boolean`
Default: `false`

Sanitize the output. Ignore any HTML that has been input.

### smartLists

Type: `boolean`
Default: `true`

Use smarter list behavior than the original markdown. May eventually be
default with the old behavior moved into `pedantic`.

### smartypants

Type: `boolean`
Default: `false`

Use "smart" typograhic punctuation for things like quotes and dashes.

## Access to lexer and parser

You also have direct access to the lexer and parser if you so desire.

``` js
var tokens = marked.lexer(text, options);
console.log(marked.parser(tokens));
```

``` js
var lexer = new marked.Lexer(options);
var tokens = lexer.lex(text);
console.log(tokens);
console.log(lexer.rules);
```

## CLI

``` bash
$ marked -o hello.html
hello world
^D
$ cat hello.html
<p>hello world</p>
```

## Philosophy behind marked

The point of marked was to create a markdown compiler where it was possible to
frequently parse huge chunks of markdown without having to worry about
caching the compiled output somehow...or blocking for an unnecesarily long time.

marked is very concise and still implements all markdown features. It is also
now fully compatible with the client-side.

marked more or less passes the official markdown test suite in its
entirety. This is important because a surprising number of markdown compilers
cannot pass more than a few tests. It was very difficult to get marked as
compliant as it is. It could have cut corners in several areas for the sake
of performance, but did not in order to be exactly what you expect in terms
of a markdown rendering. In fact, this is why marked could be considered at a
disadvantage in the benchmarks above.

Along with implementing every markdown feature, marked also implements [GFM
features][gfmf].

## Benchmarks

node v0.8.x

``` bash
$ node test --bench
marked completed in 3411ms.
marked (gfm) completed in 3727ms.
marked (pedantic) completed in 3201ms.
robotskirt completed in 808ms.
showdown (reuse converter) completed in 11954ms.
showdown (new converter) completed in 17774ms.
markdown-js completed in 17191ms.
```

__Marked is now faster than Discount, which is written in C.__

For those feeling skeptical: These benchmarks run the entire markdown test suite 1000 times. The test suite tests every feature. It doesn't cater to specific aspects.

### Pro level

You also have direct access to the lexer and parser if you so desire.

``` js
var tokens = marked.lexer(text, options);
console.log(marked.parser(tokens));
```

``` js
var lexer = new marked.Lexer(options);
var tokens = lexer.lex(text);
console.log(tokens);
console.log(lexer.rules);
```

``` bash
$ node
> require('marked').lexer('> i am using marked.')
[ { type: 'blockquote_start' },
  { type: 'paragraph',
    text: 'i am using marked.' },
  { type: 'blockquote_end' },
  links: {} ]
```

## Running Tests & Contributing

If you want to submit a pull request, make sure your changes pass the test
suite. If you're adding a new feature, be sure to add your own test.

The marked test suite is set up slightly strangely: `test/new` is for all tests
that are not part of the original markdown.pl test suite (this is where your
test should go if you make one). `test/original` is only for the original
markdown.pl tests. `test/tests` houses both types of tests after they have been
combined and moved/generated by running `node test --fix` or `marked --test
--fix`.

In other words, if you have a test to add, add it to `test/new/` and then
regenerate the tests with `node test --fix`. Commit the result. If your test
uses a certain feature, for example, maybe it assumes GFM is *not* enabled, you
can add `.nogfm` to the filename. So, `my-test.text` becomes
`my-test.nogfm.text`. You can do this with any marked option. Say you want
line breaks and smartypants enabled, your filename should be:
`my-test.breaks.smartypants.text`.

To run the tests:

``` bash
cd marked/
node test
```

### Contribution and License Agreement

If you contribute code to this project, you are implicitly allowing your code
to be distributed under the MIT license. You are also implicitly verifying that
all code is your original work. `</legalese>`

## License

Copyright (c) 2011-2014, Christopher Jeffrey. (MIT License)

See LICENSE for more info.

[gfm]: https://help.github.com/articles/github-flavored-markdown
[gfmf]: http://github.github.com/github-flavored-markdown/
[pygmentize]: https://github.com/rvagg/node-pygmentize-bundled
[highlight]: https://github.com/isagalaev/highlight.js
[badge]: http://badge.fury.io/js/marked
[tables]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#wiki-tables
[breaks]: https://help.github.com/articles/github-flavored-markdown#newlines
# requirejs-bower

Bower packaging for [RequireJS](http://requirejs.org).

# jQuery

> jQuery is a fast, small, and feature-rich JavaScript library.

For information on how to get started and how to use jQuery, please see [jQuery's documentation](http://api.jquery.com/).
For source files and issues, please visit the [jQuery repo](https://github.com/jquery/jquery).

## Including jQuery

Below are some of the most common ways to include jQuery.

### Browser

#### Script tag

```html
<script src="https://code.jquery.com/jquery-2.2.0.min.js"></script>
```

#### Babel

[Babel](http://babeljs.io/) is a next generation JavaScript compiler. One of the features is the ability to use ES6/ES2015 modules now, even though browsers do not yet support this feature natively.

```js
import $ from "jquery";
```

#### Browserify/Webpack

There are several ways to use [Browserify](http://browserify.org/) and [Webpack](https://webpack.github.io/). For more information on using these tools, please refer to the corresponding project's documention. In the script, including jQuery will usually look like this...

```js
var $ = require("jquery");
```

#### AMD (Asynchronous Module Definition)

AMD is a module format built for the browser. For more information, we recommend [require.js' documentation](http://requirejs.org/docs/whyamd.html).

```js
define(["jquery"], function($) {

});
```

### Node

To include jQuery in [Node](nodejs.org), first install with npm.

```sh
npm install jquery
```

For jQuery to work in Node, a window with a document is required. Since no such window exists natively in Node, one can be mocked by tools such as [jsdom](https://github.com/tmpvar/jsdom). This can be useful for testing purposes.

```js
require("jsdom").env("", function(err, window) {
	if (err) {
		console.error(err);
		return;
	}

	var $ = require("jquery")(window);
});
```
# Bootstrap for Sass
[![Gem Version](https://badge.fury.io/rb/bootstrap-sass.svg)](http://badge.fury.io/rb/bootstrap-sass)
[![npm version](https://img.shields.io/npm/v/bootstrap-sass.svg?style=flat)](https://www.npmjs.com/package/bootstrap-sass)
[![Bower Version](https://badge.fury.io/bo/bootstrap-sass.svg)](http://badge.fury.io/bo/bootstrap-sass)
[![Build Status](https://img.shields.io/travis/twbs/bootstrap-sass.svg)](https://travis-ci.org/twbs/bootstrap-sass)

`bootstrap-sass` is a Sass-powered version of [Bootstrap](https://github.com/twbs/bootstrap) 3, ready to drop right into your Sass powered applications.

This is Bootstrap 3. For Bootstrap 4 use the [Bootstrap Ruby gem](http://github.com/twbs/bootstrap-rubygem) if you use Ruby, and the [main repo](http://github.com/twbs/bootstrap) otherwise.

## Installation

Please see the appropriate guide for your environment of choice:

* [Ruby on Rails](#a-ruby-on-rails).
* [Compass](#b-compass-without-rails) not on Rails.
* [Bower](#c-bower).
* [npm / Node.js](#d-npm--nodejs).

### a. Ruby on Rails

`bootstrap-sass` is easy to drop into Rails with the asset pipeline.

In your Gemfile you need to add the `bootstrap-sass` gem, and ensure that the `sass-rails` gem is present - it is added to new Rails applications by default.

```ruby
gem 'bootstrap-sass', '~> 3.3.6'
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

Then, remove all the `*= require_self` and `*= require_tree .` statements from the sass file. Instead, use `@import` to import Sass files.

Do not use `*= require` in Sass or your other stylesheets will not be [able to access][antirequire] the Bootstrap mixins or variables.

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

If you use [mincer][mincer] with node-sass, import Bootstrap like so:

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

### d. npm / Node.js
```console
$ npm install bootstrap-sass
```


## Configuration

### Sass

By default all of Bootstrap is imported.

You can also import components explicitly. To start with a full list of modules copy
[`_bootstrap.scss`](assets/stylesheets/_bootstrap.scss) file into your assets as `_bootstrap-custom.scss`.
Then comment out components you do not want from `_bootstrap-custom`.
In the application Sass file, replace `@import 'bootstrap'` with:

```scss
@import 'bootstrap-custom';
```

### Sass: Number Precision

bootstrap-sass [requires](https://github.com/twbs/bootstrap-sass/issues/409) minimum [Sass number precision][sass-precision] of 8 (default is 5).

Precision is set for Rails and Compass automatically.
When using Ruby Sass compiler standalone or with the Bower version you can set it with:

```ruby
::Sass::Script::Value::Number.precision = [8, ::Sass::Script::Value::Number.precision].max
```

### Sass: Autoprefixer

Bootstrap requires the use of [Autoprefixer][autoprefixer].
[Autoprefixer][autoprefixer] adds vendor prefixes to CSS rules using values from [Can I Use](http://caniuse.com/).

To match [upstream Bootstrap's level of browser compatibility](http://getbootstrap.com/getting-started/#support), set Autoprefixer's `browsers` option to:
```json
[
  "Android 2.3",
  "Android >= 4",
  "Chrome >= 20",
  "Firefox >= 24",
  "Explorer >= 8",
  "iOS >= 6",
  "Opera >= 12",
  "Safari >= 6"
]
```

### JavaScript

[`assets/javascripts/bootstrap.js`](/assets/javascripts/bootstrap.js) contains all of Bootstrap's JavaScript,
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

### Fonts

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

Import Bootstrap into a Sass file (for example, `application.scss`) to get all of Bootstrap's styles, mixins and variables!

```scss
@import "bootstrap";
```

You can also include optional Bootstrap theme:

```scss
@import "bootstrap/theme";
```

The full list of Bootstrap variables can be found [here](http://getbootstrap.com/customize/#less-variables). You can override these by simply redefining the variable before the `@import` directive, e.g.:

```scss
$navbar-default-bg: #312312;
$light-orange: #ff8c00;
$navbar-default-color: $light-orange;

@import "bootstrap";
```

### Eyeglass

Bootstrap is available as an [Eyeglass](https://github.com/sass-eyeglass/eyeglass) module. After installing Bootstrap via NPM you can import the Bootstrap library via:

```scss
@import "bootstrap-sass/bootstrap"
```

or import only the parts of Bootstrap you need:

```scss
@import "bootstrap-sass/bootstrap/variables";
@import "bootstrap-sass/bootstrap/mixins";
@import "bootstrap-sass/bootstrap/carousel";
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
|    3.3.4+ |   same |
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

* Converts upstream Bootstrap LESS files to its matching SCSS file.
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
Michael Hartl's [Rails Tutorial](https://www.railstutorial.org/), [gitlabhq](http://gitlabhq.com/) and
[kandan](http://getkandan.com/).

[converter]: https://github.com/twbs/bootstrap-sass/blob/master/tasks/converter/less_conversion.rb
[version]: https://github.com/twbs/bootstrap-sass/blob/master/lib/bootstrap-sass/version.rb
[contrib]: https://github.com/twbs/bootstrap-sass/graphs/contributors
[antirequire]: https://github.com/twbs/bootstrap-sass/issues/79#issuecomment-4428595
[jsdocs]: http://getbootstrap.com/javascript/#transitions
[sass-precision]: http://sass-lang.com/documentation/Sass/Script/Value/Number.html#precision%3D-class_method
[mincer]: https://github.com/nodeca/mincer
[autoprefixer]: https://github.com/postcss/autoprefixer
# domReady

An AMD loader plugin for detecting DOM ready.

Known to work in RequireJS, but should work in other
AMD loaders that support the same loader plugin API.

## Docs

See the [RequireJS API "Page Load Event Support/DOM Ready" section](http://requirejs.org/docs/api.html#pageload).

## Latest release

The latest release will be available from the "latest" tag.

## License

Dual-licensed -- new BSD or MIT.

## Where are the tests?

They are in the [requirejs](https://github.com/jrburke/requirejs) and
[r.js](https://github.com/jrburke/r.js) repos.

## History

This plugin was in the [requirejs repo](https://github.com/jrburke/requirejs)
up until the requirejs 2.0 release.

## Contributing

domReady follows the [same contribution model as requirejs](http://requirejs.org/docs/contributing.html) and is considered a sub-project of requirejs.This folder contains markdown files for the website. 
WHY WE USE THIS?
- Because editing in the spreadsheet is a pain, and writing HTML code on GDocs is a pain as well.

- HOW THIS WILL WORK?
Easy - the files in this folders are already in markdown format. Edit all content here before copying and pasting it to the spreadsheet. Notice, do not copy text to the spreadsheet from the Google Drive, the files there are not in the right format!

You can find the file in their non markdown form on the Google Drive: 
https://drive.google.com/drive/u/1/folders/0BwCiEMnFOs0tZFhWQ0ExOTZ6Qjg

