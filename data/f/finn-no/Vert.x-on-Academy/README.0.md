# eventbusbridge-cljs

An example of using the ClojureScript eventbus.

## Usage

First, compile the ClojureScript client:
  
    lein cljsbuild once
    
Then run the server:

    vertx run bridge-server.clj
   
And connect to http://localhost:8080/

See the implementation for the
[client](src/eventbusbridge_cljs/client.cljs) and the
[`vertx.client.eventbus`](https://github.com/vert-x/mod-lang-clojure/blob/master/api/src/main/clojure/vertx/client/eventbus.cljs).
# Docker on Academy - 2014.05.28

This is a presentation on Docker held at FINN Academy 2014.05.28.

To watch the presentation, just go to [http://finn-no.github.io/Docker-on-Academy](http://finn-no.github.io/Docker-on-Academy/).

Big thanks go to Hakim El Hattab for creating a great presentation framework in [reveal.js](https://github.com/hakimel/reveal.js).
## Dependencies

Themes are written using Sass to keep things modular and reduce the need for repeated selectors across files. Make sure that you have the reveal.js development environment including the Grunt dependencies installed before proceding: https://github.com/hakimel/reveal.js#full-setup

You also need to install Ruby and then Sass (with `gem install sass`).

## Creating a Theme

To create your own theme, start by duplicating any ```.scss``` file in [/css/theme/source](https://github.com/hakimel/reveal.js/blob/master/css/theme/source) and adding it to the compilation list in the [Gruntfile](https://github.com/hakimel/reveal.js/blob/master/Gruntfile.js).

Each theme file does four things in the following order:

1. **Include [/css/theme/template/mixins.scss](https://github.com/hakimel/reveal.js/blob/master/css/theme/template/mixins.scss)**
Shared utility functions.

2. **Include [/css/theme/template/settings.scss](https://github.com/hakimel/reveal.js/blob/master/css/theme/template/settings.scss)**
Declares a set of custom variables that the template file (step 4) expects. Can be overridden in step 3.

3. **Override**
This is where you override the default theme. Either by specifying variables (see [settings.scss](https://github.com/hakimel/reveal.js/blob/master/css/theme/template/settings.scss) for reference) or by adding full selectors with hardcoded styles.

4. **Include [/css/theme/template/theme.scss](https://github.com/hakimel/reveal.js/blob/master/css/theme/template/theme.scss)**
The template theme file which will generate final CSS output based on the currently defined variables.

When you are done, run `grunt themes` to compile the Sass file to CSS and you are ready to use your new theme.