# Extras
This folder a place for platform-specific helpers, configuration, and READMEs, as well as addtional tasks you may find helpful. The contents of a platform folder should reflect the placement of files and folders in the project directory. For example, [`extras/rails`](/gulpfile.js/extras/rails) contains `app/helpers/blendid_asset_helper.rb`, which is where the file should go in a Rails app. 

Pull requests are very welcome!
Coming soon...# Blendid on Drupal

### Important Notes:
* The theme foldername is used as the basename to rename folders and config files.
# HTTP2 component styles

HTTP/2 allows for multiplexing, which allows you to sprinkle your CSS files in where they are needed, rather than loading them all in one big CSS file on the initial session to your application.

A recommended way to approach this is for each HTML component (within `src/html/components`) you create a corresponding CSS component within this directory (`src/stylesheets/components`). The CSS component only loads when the HTML template is built on page (see *Using component styles in your HTML templates* below on how to do this).

Every CSS component should import the config files (variables, mixins and functions) so that anything defined there can be used to calculate values within the component.

## Organizing your stylesheets directory
Standard component directory structure should include an index file that imports the config files as well as any files in the directory, usually just one that is either named `_base.scss` or `_[component-name].scss` for easier fuzzy finder location.

For example:

```
/components
  |
  /example-component
  | |
  | index.scss // imports config and any underscored files in this directory
  | _example-component.scss // has all the styles for this component
  |
  /another-component
    |
    index.scss
    // etc
```

## Using component styles in your HTML templates
Using the `css()` macro defined in `src/html/macros/helpers.html` will allow you to easily pull in the styles defined for that component inline. To use simply call `{{ macros.css('example-component') }}` before writing any HTML in the template and it will find pull in the *index file* of that directory.
## Gulp Server Task
This will start a static server that serves your production files to `http://localhost:5000`. This is primarily meant as a way to preview your production build locally, not necessarily for use as a live production server.

Addtional `devDependencies` needed:

```json
  "compression": "1.6.2",
  "express": "4.14.0",
  "morgan": "1.7.0",
  "open": "0.0.5",
```

## IconFont Task
```
gulpfile.js/tasks/iconFont
```

Addtional `devDependencies` needed:

```json
  "gulp-data": "1.2.1",
  "gulp-iconfont": "8.0.1",
  "gulp-nunjucks-render": "2.0.0",
  "gulp-rename": "1.2.2",
```

SVGs added to `src/icons` will be automatically compiled into an iconFont, and output to `./public/fonts`. At the same time, a `.sass` file will be output to `src/stylesheets/generated/_icons.sass`. This file contains mixins and classes based on the svg filename. If you want to edit the template that generates this file, it's at `gulpfile.js/tasks/iconFont/template.sass`. If you have the option, I'd recommend using SVG sprites (see below) over this method for icons.

##### Usage:
With generated classes:
```
<span class="icon -twitter"></span>
```

With mixins:
```sass
.lil-birdy-guy
  +icon--twitter
```

```scss
.lil-birdy-guy {
  @include icon--twitter;
}
```

```html
<span class="lil-birdy-guy"></span>
```

*Don't forget about accessibility!*

```html
<span aria-label="Twitter" class="icon -twitter"></span>
<!-- or -->
<div class="icon -twitter"><span class="screen-reader">Twitter</span></div>
```
# Gulp Shopify Upload Task

Using gulp-starter with Shopify creates a simple workflow that makes iteration loops fairly tight. This directory contains the extra pieces you'll need to get going.

## Overview

It is expected that you're working with a Shopify Theme which should have a folder structure that resembles the following:

```
myproject
  ├── assets
  ├── config
  ├── gulpfile.js
  ├── layout
  ├── locales
  ├── snippets
  ├── src (your uncompiled source files)
  └── templates
```

#### Dependencies

    npm install gulp-shopify-upload --save-dev

#### Gulp Tasks

This example contains two gulp tasks: `shopifywatch` and `shopifydeploy` defined in `gulpfile.js/tasks/shopify.js`. The watch task starts a watching process that monitors at all Shopify directories and uploads saved files (whether they have changed or not). The deploy task simply deploys all files at once.

Not depicted in this example is the integration of these gulp tasks with your configured task pipelines. It is up to you to add `shopifywatch` to a list of tasks executed during development, and `shopifydeploy` to a deploy task.

**One Caveat**: It is true that, during development, you will actually be deploying (uploading) files to the Shopify server that holds your theme files, overwriting what's there. Keep this in mind! Always develop against a test theme on a dev Shopify project and if you're working with a team, take care not to overwrite eachother's work.

#### API Credentials

In order to upload files, the gulp plugin requires your store's API key and API password, along with the store URL. As you can see in `.gitignore`, it is recommended that you ignore the file with the credentials filled in, and only store the example file in source control. Here's the procedure for setting this up (you probably want to include these instructions in _your_ project's README).

1. Copy `shopify_api.json.example` and rename it to `shopify_api.json` in the root directory of your project
2. Fill in the fields with your store's information
3. Make sure to add `shopify_api.json` to your `.gitignore` so that your secret key isn't stored in source control
# Gulp Starter on Docker

This extra allows you to run gulp-starter in a Docker container. You can use the included development server, or use Docker to manage assets for another server environment, which may or may not also use Docker. 

## Requirements

Requires [Docker](https://www.docker.com/products/overview), naturally.

## Usage

### In development
```bash
git clone https://github.com/vigetlabs/gulp-starter.git MyApp
cd MyApp
cp ./extras/docker/Dockerfile .
cp ./extras/docker/.dockerignore .
docker build -t myapp .
docker run -it --rm \
    -v "$PWD"/src:/app/src \
    -v "$PWD"/public:/app/public \
    -p 3000:3000 \
    myapp \
    npm start
```
Browse to [http://localhost:3000](http://localhost:3000).

### As part of an automated build
```bash
docker run --rm myrepo/myimage:mytag npm run gulp production
```

If you want to use this to process front-end assets for a different server environment, you can do that too. In the Browsersync section of [config.json](https://github.com/davidham/gulp-starter/blob/master/gulpfile.js/config.json), set Browsersync to proxy your app server. Here's an example pointing at a Rails app:

```json
"browserSync": {
  "proxy": "http://app:3000",
  "ghostMode": false,
  "port": "8080",
  "ui": {
    "port": "8081"
  },
  "files": "./app/views/**/*"
}
```

In this example `app` is the name of the Rails service from a `docker-compose.yml` file (sold separately).
