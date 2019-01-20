# Vega: A Visualization Grammar

**Vega** is a *visualization grammar*, a declarative format for creating,
saving, and sharing interactive visualization designs.
With Vega you can describe data visualizations in a JSON format,
and generate interactive views using either HTML5 Canvas or SVG.

For documentation, tutorials, and examples, see the
[Vega website](https://vega.github.io/vega). For a description of changes
between Vega 2 and Vega 3, please refer to the
[Vega 3 Porting Guide](https://vega.github.io/vega/docs/porting-guide/).
Additional API documentation for Vega 3 can be found in the associated
modules listed below.

## Basic Setup

For a basic setup allowing you to build Vega and run examples,
clone `https://github.com/vega/vega` and run `npm install`.

Once installation is complete, use `npm run test` to run tests and
`npm run build` to build output files.

This repo (`vega`) includes web-based demos within the `test` folder. To run
these, launch a local webserver in the top-level directory for the repo
(e.g., `python -m SimpleHTTPServer 8000` for Python 2,
`python -m http.server 8000` for Python 3) and then point your browser to
the right place (e.g., `http://localhost:8000/test/`).

## Development Setup

For a more advanced development setup in which you will be working on multiple
modules simultaneously, first clone the relevant Vega 3 modules. Here is a
list of all Vega 3 repositories:

* https://github.com/vega/vega
* https://github.com/vega/vega-crossfilter
* https://github.com/vega/vega-dataflow
* https://github.com/vega/vega-encode
* https://github.com/vega/vega-event-selector
* https://github.com/vega/vega-expression
* https://github.com/vega/vega-force
* https://github.com/vega/vega-geo
* https://github.com/vega/vega-hierarchy
* https://github.com/vega/vega-loader
* https://github.com/vega/vega-parser
* https://github.com/vega/vega-projection
* https://github.com/vega/vega-runtime
* https://github.com/vega/vega-scale
* https://github.com/vega/vega-scenegraph
* https://github.com/vega/vega-statistics
* https://github.com/vega/vega-transforms
* https://github.com/vega/vega-util
* https://github.com/vega/vega-view
* https://github.com/vega/vega-view-transforms
* https://github.com/vega/vega-voronoi
* https://github.com/vega/vega-wordcloud

Though not strictly required, we recommend using `npm link` to connect each
local copy of a repo with its 'vega-' dependencies. That way, any edits you
make in one repo will be immediately reflected within dependent repos,
accelerating testing.

For example, to link _vega-dataflow_ for use by other repos, do the following:
```
# register a link to vega-dataflow
cd vega-dataflow; npm link
# update vega-runtime to use the linked version of vega-dataflow
cd ../vega-runtime; npm link vega-dataflow
# update vega to use the linked version of vega-dataflow
cd ../vega; npm link vega-dataflow
```

Once links have been setup, you can use `npm install` as usual to gather all
remaining dependencies.
# D3: Data-Driven Documents

<a href="https://d3js.org"><img src="https://d3js.org/logo.svg" align="left" hspace="10" vspace="6"></a>

**D3** (or **D3.js**) is a JavaScript library for visualizing data using web standards. D3 helps you bring data to life using SVG, Canvas and HTML. D3 combines powerful visualization and interaction techniques with a data-driven approach to DOM manipulation, giving you the full capabilities of modern browsers and the freedom to design the right visual interface for your data.

## Resources

* [API Reference](https://github.com/d3/d3/blob/master/API.md)
* [Release Notes](https://github.com/d3/d3/releases)
* [Gallery](https://github.com/d3/d3/wiki/Gallery)
* [Examples](https://bl.ocks.org/mbostock)
* [Wiki](https://github.com/d3/d3/wiki)

## Installing

If you use npm, `npm install d3`. Otherwise, download the [latest release](https://github.com/d3/d3/releases/latest). The released bundle supports anonymous AMD, CommonJS, and vanilla environments. You can load directly from [d3js.org](https://d3js.org), [CDNJS](https://cdnjs.com/libraries/d3), or [unpkg](https://unpkg.com/d3/). For example:

```html
<script src="https://d3js.org/d3.v4.js"></script>
```

For the minified version:

```html
<script src="https://d3js.org/d3.v4.min.js"></script>
```

You can also use the standalone D3 microlibraries. For example, [d3-selection](https://github.com/d3/d3-selection):

```html
<script src="https://d3js.org/d3-selection.v1.js"></script>
```

D3 is written using [ES2015 modules](http://www.2ality.com/2014/09/es6-modules-final.html). Create a [custom bundle using Rollup](https://bl.ocks.org/mbostock/bb09af4c39c79cffcde4), Webpack, or your preferred bundler. To import D3 into an ES2015 application, either import specific symbols from specific D3 modules:

```js
import {scaleLinear} from "d3-scale";
```

Or import everything into a namespace (here, `d3`):

```js
import * as d3 from "d3";
```

In Node:

```js
var d3 = require("d3");
```

You can also require individual modules and combine them into a `d3` object using [Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign):

```js
var d3 = Object.assign({}, require("d3-format"), require("d3-geo"), require("d3-geo-projection"));
```
