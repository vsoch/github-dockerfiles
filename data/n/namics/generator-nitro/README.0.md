# Your Project

Introduction …

## Usage

Before using, you need of course [node](https://nodejs.org/) installed.  
Ensure correct [node-version](./.node-version)

Run:

```
npm install
```

and start in development mode

```
npm start
```

# Usage with docker (experimental)

For information on how to use Nitro with docker, please refer to [nitro-docker.md](./project/docs/nitro-docker.md).

## Nitro

For information on how to use Nitro, please refer to [nitro.md](./project/docs/nitro.md).

## Possible Structure of this file

If you have writer's block – a possible structure for your project readme could look like [readme.md](https://github.com/namics/frontend-defaults/blob/master/doc/README.md).
# Backstop Visual Tests

Regression testing with backstopjs.  
For running these tests you need chrome headless installed.

[More about backstopjs](https://www.npmjs.com/package/backstopjs)

## Directories

default configuration:

* this directory is meant to be the place to setup your tests and to have a place for your reference screenshots.
* test results are placed in a /project/tmp/reports/... folder 
* the reports are generated inside public/reports/backstop/html

## Scripts

Use following npm scripts for your test workflow:

* `npm run visual-reference` generates new reference screenshots with current configuration
* `npm run visual-test` runs the tests, compares the results against the reference screenshots 
and generates a report under `public/reports/backstop/html/`
* `npm run visual-approve` updates the references with results from last test
# Shared

This is a place for shared assets and base codefragmets you want to use 
from different patterns or applications.

Recommended directory structure:

##`assets/`

This place is for assets you need in production

* images you want to minify with a gulp task (e.g. favicons, ...)
* ...

##`base/`

Use for "base patterns" like:

* base styling for html and body
* CSS normalize or reset
* webfonts definition
* ...

##`utils/`

Mainly for mixins and variable definitions. Every concept 

* responsive concept with breakpoints
* color system
* grid definition and helpers
* typography mixins
* ...
# Assets

Images in the folder `img` will be minified and copied to `/public/assets/img` by the gulp task "minify-images".

In views you can use them with "/assets/img/"

[Configuration](../../../config/default/gulp.js)
# Webfonts

Hosted Google Webfonts
# Security

[prevent-window-opener-attacks](https://www.npmjs.com/package/prevent-window-opener-attacks)
# Document

Base styles for html and body
# Reset

css reset example
# webfonts
# mixins

* input-visually-hidden
# Grid

Bootstrap Grid

[Bootstrap Documentation](https://getbootstrap.com/docs/4.1/layout/grid/)
Fixed ratio mixin will be set on the parent class of two nested elements.
Define the selector of the child element via fourth parameter $child to avoid '*' selector within css.
# Patterns

A pattern is an encapsulated block of markup with corresponding styles, scripts and data. 
The pattern should be documented in a `readme.md` and data can be described in `schema.json` 
with [JSON schema](http://json-schema.org) format (draft-04). Nitro uses [ajv](http://epoberezkin.github.io/ajv/) for validation.

For a better overview it is useful to define different types of patterns in [config](../../project/docs/nitro-config.md).
# cta

"Call To Action" example pattern with css keyframe animations

## Testing

[Example page](http://localhost:8081/example-patterns)
# stage

A stage pattern with css background animations

## Testing

[Example page](http://localhost:8081/example-patterns)
# button

Simple button atom example

You may use this pattern with transclusion, 
so either "text" or "children" are required [in schema.json](./schema.json)

## Testing

[Example page](http://localhost:8081/example-patterns)
# icon

This is an icon example using an [svg sprite](img/icons/readme.md).

## Testing

[Example page](http://localhost:8081/example-patterns)
# svg sprite generation

.svg files placed in this folder will be processed automatically 
and are combined into the svg sprite `public/assets/svg/icons.svg`
with the gulp task `svg-sprites`.
# loader

* This loader should be placed in a positioned parent (relative, absolute, fixed)
* Its used e.g. from [image pattern](../image/readme.md)

## Testing

[Example page](http://localhost:8081/example-patterns) (in image & box pattern)
# image

Responsive image example with [lazysizes](http://afarkas.github.io/lazysizes). Default image ratio is 16:9.

Allowed image widths are defined in [`schema.json`](./schema.json)
The width is taken from rendered container dimension (different screen resolutions are respected and multiplies the width accordingly)

```
["100", "180", "230", "290", "320", "360", "460", "580", "640", "760", "960", "1200", "1496", "1960", "2880", "3920"]
```

## API

Use modifier to change image sizes:

* `.a-image--1x1` (for images with ratio 1x1)
* `.a-image--parent-fit` (image should fit the container completely, independent of image ratio)

## Testing

[Example page](http://localhost:8081/example-patterns)
 
* Initially a loader should be visible
* Image should be loaded on entering the view
* Taken image size depends on your screen resolution and viewport size
# box

This is a box example pattern.

## Usage

It can be used as a pattern with a content string:
* from data.json 
* or {{pattern content='content <strong>string</string>'}}

... or use with transclusion to pass any content:

```
{{#pattern name='box'}}
    {{pattern name='button'}}
{{/pattern}}
```

## API

modifier `a-box--dark` for dark background

## Testing

[Example page](http://localhost:8081/example-patterns)

* Visual test
# list

Unordered list with icon as bullet point (default: checkmark).  
Icons will be extracted to an iconfont with the [iconfont-webpack-plugin](https://www.npmjs.com/package/iconfont-webpack-plugin)  
Possibility to add an svg icon at the end of the text using icon pattern

## API

modifier `a-list-mix` for different icons per line

## Testing

[Example page](http://localhost:8081/example-patterns)

* icon quality
# lottie

* Displays a [lottie](https://github.com/airbnb/lottie-web/) animation.
* Requires request on a json file

## Testing

[Example page](http://localhost:8081/example-patterns)

## Issues

Not every animation will work on all browsers
# gondel

A simple gondel pattern

## Testing

[Example page](http://localhost:8081/example-patterns)
# checkbox

Displays a custom checkbox example with label by using css and a fonticon

## Things to note

### Tag

You may use this pattern with a [div, li or span](./schema.json) root node.

### Utils

* [colors2](../../../shared/utils/colors2) for color variables
* 'input-visually-hidden' mixin from [hidden util](../../../shared/utils/hidden)

### Iconfont

The checkbox icon will be extracted to an iconfont with the [iconfont-webpack-plugin](https://www.npmjs.com/package/iconfont-webpack-plugin)

## Testing

[Example page](http://localhost:8081/example-patterns)
# date

Displays a datepicker using flatpickr library.

The flatpicker library including translations will be dynamically loaded (dynamic import)

## Testing

[Example page](http://localhost:8081/example-patterns)
# heading

A Heading pattern using webfonts.

## Testing

[Example page](http://localhost:8081/example-patterns)
# Example

This is an example. 
It show a basic example of a pattern:

* with a [visual modifier](./css/modifier/example-blue.scss)
* with a [functional decorator](./js/decorator/example-blue.js) (terrificJs)
* with an [example usage of clientside templates](./js/decorator/example-template.js) with handlebarsJS
# Proto

Place non productive code in the corresponding subfolders of this directory. 
Use this for all your development code which never should be on production.

CSS and JavaScript files here are builded with webpack. 
Files placed in the folder `proto` of each pattern are also taken.

You may change the [entry point](../proto.js)
# Develop Helpers

They are included in "proto" entry point

* press `ctrl`|`alt` and `1` to show & hide a banner with current viewport size
* press `ctrl`|`alt` and `2` to show & hide grid columns in your page
* press `ctrl`|`alt` and `3` to show & hide component, row and col wrappers in your page
* press `ctrl`|`alt` and `4` to show & hide accessibility helper tota11y
# Dynamic view data

If you want to use dynamic view data (i.e. using data from a database or data which is available in different views), 
you can define those routes in here. 
Like the `project/routes` directory, any file will be used, as long as it is a javascript file. 
You can add data to the `res.locals` property which will be merged later with the pattern and request data. 

The following code is an example of such a view data route:

    function getUser(req, res, next) {
       res.locals.user = {name: "my name", email: "me@test.com"};
       next();
    }
    
    module.exports = (app) => {
        app.route('/')
            .get(getUser);
    };

Now the called root view (or any pattern used within) can use the user properties for rendering userspecific content.
# Custom routes

If your project needs any additional or custom routes (e.g. to simulate an ajax call to an api) you can define 
them in this folder. Every file which has the .js extension will be included. 
The loader will call your file-function with the app itself as an argument. Feel free to register any routes you need. 

The following code is an example of such a data api route:
    
    function getData(req, res, next){
        return res.json({
            data: 'empty'
        });
    }

    function postData(req, res, next){
        return res.json({
            data: req.body
        });
    }

    module.exports = (app) => {
        app.route('/api/data')
            .get(getData)
            .post(postData);
    };

These routes will be loaded into Nitro automatically.
# Replacements Patterns

Nitro provides the following replacement patterns for your blueprints.

**In Content**:

```
<%= user.name %>        // Your name, eg. John Doe
<%= user.email %>       // Your email, eg. john@doe.com

<%= pattern.name %>	    // Pattern name, eg. Main Navigation
<%= pattern.folder %>   // Pattern folder, eg. MainNavigation
<%= pattern.js %>       // Pattern name for use in JS files, eg. MainNavigation
<%= pattern.css %>      // Pattern name for use in CSS files, eg. main-navigation
<%= pattern.prefix %>   // CSS class prefix, eg. o
<%= pattern.type %>     // Pattern type as specified in configuration, eg. atom, molecule etc. 
<%= pattern.file %>     // Pattern filename, eg. mainnavigation

<%= modifier.name %>    // Modifier name, eg. Highlight 
<%= modifier.css %>     // Modifier name for use in CSS files, eg. highlight
<%= modifier.file %>    // Modifier filename part, eg. highlight

<%= decorator.name %>   // Decorator name, eg. Highlight 
<%= decorator.js %>     // Decorator name for use in JS files, eg. Highlight
<%= decorator.file %>   // Decorator filename part, eg. highlight
```

**In Filename**:

```
$pattern$               // Pattern filename, eg. mainnavigation
$modifier$              // Modifier filename part eg. highlight
$decorator$             // Decorator filename part, eg. highlight
```
# <%= pattern.name %>

_Short summary and links to specification, jira, design, prototype, ..._

* [spez](https://wiki/)
* [proto](https://proto/)

## API

_Describe how to use this pattern_

## Testing

_Describe where and how to test this pattern_

## Issues

_List issues you already know_
# Custom <%= options.templateEngine %> helpers

If your project needs any additional or custom helpers, place them in this folder. 
Every file which has the .js extension will be included. 

These helpers will be loaded into Nitro automatically.

An example could look like this:

```js<% if (options.templateEngine === 'twig') { %>
const twigUtils = require('../utils');

module.exports = function (Twig) {
	return {
		type: 'helper-name',
		regex: /^helper-name/,
		next: [],
		open: true,
		compile: function(token) {
			// do any parameter logic here
			delete token.match;
			return token;
		},
		parse: function(token, context, chain) {
			try {
				// do any template / render logic here

				// return the markup
				return {
					chain: chain,
					output: 'Output Markup'
				};

			} catch (e) {
				return {
					chain: chain,
					output: twigUtils.logAndRenderError(e)
				};
			}
		}
	};
};<% } else { %>
module.exports = function(foo) {
    // Helper Logic
};<% } %>
```
<% if (options.templateEngine === 'twig') { %>
The helper name get's defined in the type property above. 
The regex property needs to be extended to contain any possible arguments of the helper.
For more complex example's please check out the core helpers.<% } else { %>
The helper name will automatically match the filename, so if you name your file `foo.js` your helper will be called `foo`.<% } %>
