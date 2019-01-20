Leaflet.NavBar
==============

Simple navigation toolbar for Leaflet.

Demo: http://davidchouse.github.io/Leaflet.NavBar/

![Leaflet.NavBar Screenshot](./screenshot.png)

## Install via Bower
````js
bower install leaflet-navbar
````

<a name="using" />
## Using the plugin

The default state for the control is just below the zoom control. This will allow map users to navigate forward and back in the map's view history as well as navigate to a home view.

````js
L.control.navbar().addTo(map);
````

Options for initialising the Leaflet.NavBar control.

| Option | Type | Default | Description
| --- | --- | --- | ---
| position | String | `'topleft'` | The initial position of the control.
| center | `L.LatLng` | Map's Current Position | The center point for the home view.
| zoom | Number | `0` | The zoom value for the home view.
# L.EasyButton

The easiest way to add buttons with Leaflet &mdash; so simple it fits in a gif:

![running demo](https://raw.githubusercontent.com/CliffCloud/Leaflet.EasyButton/dist/img/alert_example.gif)

### More [running examples and docs](http://danielmontague.com/projects/easyButton.js/v1/examples/)

-----------------------------------------------------------------------------------

## Boilerplate/Copy-Paste Examples

These use `YOUR_LEAFLET_MAP` as a placeholder;
remember to change it to the variable name of your map.

##### Hello World

open a popup

```javascript
var helloPopup = L.popup().setContent('Hello World!');

L.easyButton('fa-globe', function(btn, map){
    helloPopup.setLatLng(map.getCenter()).openOn(map);
}).addTo( YOUR_LEAFLET_MAP ); // probably just `map`
```

##### Map State

set the map's center and use an `img` for the icon

```javascript
var antarctica = [-77,70];

L.easyButton('<img src="/path/to/img/of/penguin.png">', function(btn, map){
    map.setView(antarctica);
}).addTo( YOUR_LEAFLET_MAP );
```

##### Button States

change the button's function and appearance

```javascript
var stateChangingButton = L.easyButton({
    states: [{
            stateName: 'zoom-to-forest',   // name the state
            icon:      'fa-tree',          // and define its properties
            title:     'zoom to a forest', // like its title
            onClick: function(btn, map) {  // and its callback
                map.setView([46.25,-121.8],10);
                btn.state('zoom-to-school'); // change state on click!
            }
        }, {
            stateName: 'zoom-to-school',
            icon:      'fa-university',
            title:     'zoom to a school',
            onClick: function(btn, map) {
                map.setView([42.3748204,-71.1161913],16);
                btn.state('zoom-to-forest');
            }
    }]
});

stateChangingButton.addTo( YOUR_LEAFLET_MAP );
```

-----------------------------------------------------------------------------------

## Download and Install

### Bower

    bower install --save Leaflet.EasyButton

### NPM

    npm install --save leaflet-easybutton

### Copy & Pasting

here are the links
the [js](https://raw.githubusercontent.com/CliffCloud/Leaflet.EasyButton/master/src/easy-button.js)
and [css](https://raw.githubusercontent.com/CliffCloud/Leaflet.EasyButton/master/src/easy-button.css)

### Curl download

    cd your/project/javascript-files/
    curl -O https://raw.githubusercontent.com/CliffCloud/Leaflet.EasyButton/master/src/easy-button.js
    # saved at your/project/javascript-files/easy-button.js

    cd your/project/css-files/
    curl -O https://raw.githubusercontent.com/CliffCloud/Leaflet.EasyButton/master/src/easy-button.css
    # saved at your/project/css-files/easy-button.css

### Icon Dependencies

If you haven't already, make sure to install/include the icon library of your
choice (your lib should have its own instructions)
&mdash; EasyButton should work with anything!
Leaflet.Control.FullScreen
============

What ?
------

Simple plugin for Leaflet that adds fullscreen button to your maps.

Inspired by http://elidupuis.github.com/leaflet.zoomfs/

Use the native javascript fullscreen API http://johndyer.name/native-fullscreen-javascript-api-plus-jquery-plugin/

Released under the MIT License http://opensource.org/licenses/mit-license.php

How ?
------

Include Control.FullScreen.js and Control.FullScreen.css in your page:

``` html
 <link rel="stylesheet" href="Control.FullScreen.css" />
 <script src="Control.FullScreen.js"></script>
```

Add the fullscreen control to the map:

``` js
var map = new L.Map('map', {
  fullscreenControl: true,
  fullscreenControlOptions: {
    position: 'topleft'
  }
});
```

If your map have a zoomControl the fullscreen button will be added at the bottom of this one.

If your map doesn't have a zoomContron the fullscreen button will be added to topleft corner of the map (same as the zoomcontrol).

If you want to use the plugin on a map embedded in an iframe, don't forget to set `allowfullscreen` attribute on your iframe.

__Events and options__:

``` js
// create a fullscreen button and add it to the map
L.control.fullscreen({
  position: 'topleft', // change the position of the button can be topleft, topright, bottomright or bottomleft, defaut topleft
  title: 'Show me the fullscreen !', // change the title of the button, default Full Screen
  titleCancel: 'Exit fullscreen mode', // change the title of the button when fullscreen is on, default Exit Full Screen
  content: null, // change the content of the button, can be HTML, default null
  forceSeparateButton: true, // force seperate button to detach from zoom buttons, default false
  forcePseudoFullscreen: true, // force use of pseudo full screen even if full screen API is available, default false
  fullscreenElement: false // Dom element to render in full screen, false by default, fallback to map._container
}).addTo(map);

// events are fired when entering or exiting fullscreen.
map.on('enterFullscreen', function(){
  console.log('entered fullscreen');
});

map.on('exitFullscreen', function(){
  console.log('exited fullscreen');
});
```

Where ?
------

Source code : https://github.com/brunob/leaflet.fullscreen

Downloads : https://github.com/brunob/leaflet.fullscreen/releases

Demo : http://brunob.github.com/leaflet.fullscreen/
# Leaflet.MarkerCluster.Freezable
Sub-plugin for [Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster)
plugin (MCG in short); adds the ability to freeze clusters at a specified zoom.

[Leaflet.markercluster](https://github.com/Leaflet/Leaflet.markercluster) plugin
provides beautiful animated Marker Clustering functionality.

[Leaflet](http://leafletjs.com/) is the leading open-source JavaScript library
for mobile-friendly interactive maps.

[![GitHub releases](https://img.shields.io/github/release/ghybs/leaflet.markercluster.freezable.svg?label=GitHub)](https://github.com/ghybs/Leaflet.MarkerCluster.Freezable/releases)
[![npm](https://img.shields.io/npm/v/leaflet.markercluster.freezable.svg)](https://www.npmjs.com/package/leaflet.markercluster.freezable)



## Requirements
This plugin should be compatible with both combinations:
- Leaflet 1.0.x + Leaflet.markercluster 1.0.0
- Leaflet legacy (0.7.x) + Leaflet.markercluster legacy (0.5.x)



## Demos
- [Leaflet.MarkerCluster.Freezable (Leaflet 1.0.1 + Leaflet.markercluster 1.0.0)](http://ghybs.github.io/Leaflet.MarkerCluster.Freezable/examples/mcg-freezable-leaflet1.0.0.html)
- [Leaflet.MarkerCluster.Freezable (Leaflet 0.7.7 + Leaflet.markercluster 0.5.0)](http://ghybs.github.io/Leaflet.MarkerCluster.Freezable/examples/mcg-freezable.html)


## Usage instructions

### Quick Guide
**HTML:**
```html
<!-- After Leaflet and Leaflet.markercluster scripts -->
<script src="leaflet.markercluster.freezable.js"></script>
```

**JavaScript:**
```javascript
var map = L.map("map"),
    mcg = L.markerClusterGroup(options);
    
mcg.addLayers(arrayOfMarkers);
mcg.addTo(map);

mcg.freezeAtZoom(15);
mcg.freezeAtZoom("maxKeepSpiderfy");
mcg.freezeAtZoom("max");
mcg.unfreeze(); // shortcut for mcg.freezeAtZoom(false)

mcg.disableClusteringKeepSpiderfy(); // shortcut for mcg.freezeAtZoom("maxKeepSpiderfy")
mcg.disableClustering(); // shortcut for mcg.freezeAtZoom("max")
mcg.enableClustering(); // alias for mcg.unfreeze()
```

When frozen / disabled, clusters will no longer split / merge on map zoom, but
retain their status as if they were on the specified zoom level. They will
directly spiderfy when clicked on, instead of zooming to bounds (since zooming
will not make them split apart).

In particular, freezing at `maxZoom + 1` removes all clusters.

Freezing at `maxZoom` removes all clusters except the bottom-most ones, so that
user can still spiderfy closely positioned markers.

**CAUTION: make sure your operations makes sense before freezing to high zoom
whereas the map is at a low zoom. It may have to load _thousands_ of markers
suddenly!**

_Note: while frozen, MCG will continue removing clusters and markers which are
far from the view port, accordingly with `removeOutsideVisibleBounds` option._



### Installing the sub-plugin

#### Local copy
1. Download the "<a href="https://github.com/ghybs/Leaflet.MarkerCluster.Freezable/releases/download/v0.1.1/leaflet.markercluster.freezable.js">`leaflet.markercluster.freezable.js`</a>" file from the [`v0.1.1` release](https://github.com/ghybs/Leaflet.MarkerCluster.Freezable/releases/tag/v0.1.1).
2. Place the file alongside your page.
3. Add the `script` tag (see [Quick Guide > HTML](#quick-guide)) to your page after Leaflet and Leaflet.markercluster scripts.

#### CDN
You can alternatively use the free [unpkg](https://unpkg.com) CDN service, but keep in mind that it "[_is a free, best-effort service and cannot provide any uptime or support guarantees_](https://unpkg.com/#/about)".

```html
<!-- After Leaflet script -->
<script src="https://unpkg.com/leaflet.markercluster.freezable@0.1.1/dist/leaflet.markercluster.freezable.js"></script>
```



### Creation
Simply use the the regular `L.markerClusterGroup` factory, as Freezable plugin
directly adds new methods to Leaflet.markercluster:

```javascript
var mcg = L.markerClusterGroup(options);

mcg.addTo(map);
```



## API Reference

### Methods
| Method  | Returns  | Description |
| :------ | :------- | :---------- |
| **freezeAtZoom**( `<Number>` or `<String>` or `<Boolean>` frozenZoom? ) | `this` | Freezes clusters at specified zoom, current zoom, or unfreeze. If passed a positive number (including 0), freezes at that zoom. If passed `"max"` (string), freezes at `maxZoom + 1`. If passed `"maxKeepSpiderfy"` (string), freezes at `maxZoom`. If passed nothing, `undefined`, `true` (boolean) or `NaN`, freezes at current zoom. If passed `false` (boolean) or any other non-number, unfreezes. |
| **unfreeze**() | `this` | Shortcut for `freezeAtZoom(false)`. |
| **disableClustering**() | `this` | Shortcut for `freezeAtZoom("max")`. |
| **disableClusteringKeepSpiderfy**() | `this` | Shortcut for `freezeAtZoom("maxKeepSpiderfy")`. |
| **enableClustering**() | `this` | Shortcut for `unfreeze()`. |

MCG.Freezable does not provide any extra option or event.


### Regular MCG options, events and methods
All regular MCG [options](https://github.com/Leaflet/Leaflet.markercluster#all-options),
[events](https://github.com/Leaflet/Leaflet.markercluster#events) and
[methods](https://github.com/Leaflet/Leaflet.markercluster#methods) are
available within MCG Layer Support. Refer to Leaflet.markercluster documentation.



## Limitations

### Freezing at current zoom while not on map
If you request MCG to freeze at current zoom, but MCG is not on any map at that
moment, it will freeze at the zoom the map is at when added to it.

## License
[![license](https://img.shields.io/github/license/ghybs/leaflet.markercluster.freezable.svg)](LICENSE)

Leaflet.MarkerCluster.Freezable is distributed under the
[MIT License](http://choosealicense.com/licenses/mit/) (Expat type), like
Leaflet.markercluster.
Leaflet.loading
===============

Leaflet.loading is a simple loading control for [Leaflet][]. An unobtrusive
loading indicator is added below the zoom control if one exists. The indicator
is visible when tiles are loading or when other data is loading, as indicated by
firing custom events on a map. The indicator can be an image, or a [spin.js][]
spinner (image-less).


## Usage

Leaflet.loading is only tested on Leaflet version 0.6 or greater. It will almost
certainly not work with older versions of Leaflet. Of course we intend to
support Leaflet 1.0, and we have tested against the latest release (beta 2).
Please create an issue if you find that any part of this project is not
compatible with Leaflet 1.0.

Include `Control.Loading.js` and `Control.Loading.css`, then create a map with
`loadingControl: true` in its options.

By default, Leaflet.loading includes a base64-encoded animagted loading image in
`Control.Loading.css`. You can customize this by changing `background-image` for
the selector `.leaflet-control-loading`. The simplest case would be adding a 16
x 16 loading gif in `.leaflet-control-loading`.

You can also set `spinjs: true` in the options, and load [spin.js][] to use that
instead of an image. A spin.js options object can be passed as the spin key when
initializing the control.

Whichever method you use, make sure you only use one.

Once the above is complete you will have a loading indicator that only appears
when tiles are loading.

If you want to show the loading indicator while other AJAX requests or something
else is occurring, fire the `dataloading` event on your map when you begin
loading and `dataload` when you are finished loading. Please note that there is
[an issue](https://github.com/ebrelsford/Leaflet.loading/issues/26) with the
way this control tracks these events and that this will be re-worked in a
future version.

### Options

 - **position**: (string) Where you want the control to show up on the map (standard
   Leaflet control option). Optional, defaults to `topleft`
 - **separate**: (boolean) Whether the control should be separate from the zoom
   control or not, defaults to false.
 - **zoomControl**: (L.Control.Zoom) The zoom control that the control should be
   added to. This is only necessary when adding a loading control to a zoom
   control that you added manually and do not want a separate loading control.
 - **delayIndicator**: (float) The number of milliseconds to wait before
   showing the loading indicator. Defaults to `null` (no delay).
 - **spinjs**: (boolean) Enable the use of [spin.js][]. Optional, defaults to
   `false`
 - **spin**: (object) A [spin.js][] options object. Optional, defaults to

    ```
    {
        lines: 7,
        length: 3,
        width: 3,
        radius: 5,
        rotate: 13,
        top: "83%"
    }
    ```


## Demos

See Leaflet.loading in action (zoom or pan to make tiles load):

 - Using the [simplest setup][simple], with the loading indicator attached to
   the zoom control.
 - With the loading indicator [separate][] from the zoom control.
 - With the loading indicator and zoom control on the [top right][topright] of
   the map.
 - The [simplest example using spin.js](http://ebrelsford.github.io/Leaflet.loading/spinjs.html) instead of an image
 - Combined with a [fullscreen control][combined] (e.g. [leaflet.fullscreen][]).


## License

Leaflet.loading is free software, and may be redistributed under the MIT
License.


 [Leaflet]: https://github.com/Leaflet/Leaflet
 [spin.js]: https://github.com/fgnass/spin.js/
 [simple]: http://ebrelsford.github.io/Leaflet.loading/simple.html
 [separate]: http://ebrelsford.github.io/Leaflet.loading/separate.html
 [topright]: http://ebrelsford.github.io/Leaflet.loading/topright.html
 [combined]: http://ebrelsford.github.io/Leaflet.loading/combined.html
 [leaflet.fullscreen]: https://github.com/brunob/leaflet.fullscreen
