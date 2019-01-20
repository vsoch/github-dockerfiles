# Multiple Instances

This example uses Uppy with the RestoreFiles plugin.
It has two instances on the same page, side-by-side, but with different `id`s so their stored files don't interfere with each other.

## Run it

Move into this directory, then:

```bash
npm install
npm start
```
# Uploading to DigitalOcean Spaces

This example uses Uppy to upload files to a DigitolOcean Space. DigitalOcean Spaces has an identical API to S3, so we can use the [AwsS3](https://uppy.io/docs/aws-s3) plugin. We use @uppy/companion with a [custom `endpoint` configuration](./server.js#L32-L33) that points to DigitalOcean.

To try this example, first run:

```bash
npm install
```

Then configure some environment variables and run it:

```bash
COMPANION_AWS_REGION=ams3 \
COMPANION_AWS_KEY=your_access_key_id \
COMPANION_AWS_SECRET=your_secret_access_key \
COMPANION_AWS_BUCKET=your_space_name \
npm start
```
# Uppy + AWS S3 Example

This example uses @uppy/companion with a custom AWS S3 configuration.
Files are uploaded to a randomly named directory inside the `whatever/` directory in a bucket.

## Run it

First set up the `COMPANION_AWS_KEY`, `COMPANION_AWS_SECRET`, `COMPANION_AWS_REGION`, and `COMPANION_AWS_BUCKET` environment variables for @uppy/companion.

Move into this directory, then:

```bash
npm install
npm start
```
# XHR Bundle Upload

This example uses Uppy with XHRUpload plugin in `bundle` mode. Bundle mode uploads all files to the endpoint in a single request, instead of firing off a new request for each file. This makes uploading a bit slower, but it may be easier to handle on the server side, depending on your setup.

[serve.js](./serve.js) contains an example express.js server that receives a multipart form-data upload and responds with some information about the files that were received (name, size) as JSON. It uses [multer](https://npmjs.com/package/multer) to parse the upload stream.

## Run it

Move into this directory, then:

```bash
npm install
npm start
```
# Uppy + Companion + Custom Provider  Example

This example uses @uppy/companion with a dummy custom provider.
This serves as an illustration on how integrating custom providers would work

## Run it

Move into this directory, then:

```bash
npm install
npm start
```
# Redux

This example uses Uppy with a Redux store.
The same Redux store is also used for other parts of the application, namely the counter example.
Each action is logged to the console using [redux-logger](https://github.com/theaqua/redux-logger).

This example supports the [Redux Devtools extension](https://github.com/zalmoxisus/redux-devtools-extension), including time travel.

## Run it

Move into this directory, then:

```bash
npm install
npm start
```
# Uppy + AWS S3 Example

This example uses a server-side PHP endpoint to sign uploads to S3.

## Running It

This example uses the AWS PHP SDK.
To install it, [get composer](https://getcomposer.org) and run `composer update` in this folder.

```bash
cd ./examples/aws-presigned-url
composer update
```

Configure AWS S3 credentials using [environment variables](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/guide/credentials.html#environment-credentials) or a [credentials file in `~/.aws/credentials`](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/guide/credentials.html#credential-profiles).
Configure a bucket name and region in the `s3-sign.php` file.

Then install npm dependencies using

```bash
npm install
```

and start the demo server using

```bash
npm start
```

The demo should now be available at http://localhost:8080.

Optionally, provide a port in the `PORT` environment variable:

```bash
PORT=8080 npm start
```
# @uppy/companion example

This is a simple, lean example that combines the usage of @uppy/companion and uppy client.

## Test it

To test it, run `npm install` to install the required dependencies, and then run `npm start`

# Unused

These locale files are not currently used by Uppy. We are keeping them around because they will, hopefully, be used in the future.
# @uppy/react

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/react"><img src="https://img.shields.io/npm/v/@uppy/react.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

React component wrappers around Uppy's officially maintained UI plugins.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const { DashboardModal } = require('@uppy/react')

const uppy = Uppy()

class Example extends React.Component {
  state = { open: false }
  render () {
    return (
      <DashboardModal
        uppy={uppy}
        open={this.state.open}
        onRequestClose={this.handleClose}
      />
    )
  }
  // ..snip..
}
```

## Installation

```bash
$ npm install @uppy/react --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/react).

## License

[The MIT License](./LICENSE).
# @uppy/form

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/form"><img src="https://img.shields.io/npm/v/@uppy/form.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The Form plugin collects metadata from any specified `<form>` element, right before Uppy begins uploading/processing files. It optionally appends results back to the form. Currently the appended result is a stringified version of a result returned from `uppy.upload()`.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const Form = require('@uppy/form')

const uppy = Uppy()
uppy.use(Form, {
  target: document.querySelector('form'),
  getMetaFromForm: true,
  addResultToForm: true,
  resultName: 'uppyResult',
  submitOnSuccess: true
})
```

## Installation

```bash
$ npm install @uppy/form --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/form).

## License

[The MIT License](./LICENSE).
# @uppy/status-bar

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/status-bar"><img src="https://img.shields.io/npm/v/@uppy/status-bar.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The status-bar shows upload progress and speed, ETAs, pre- and post-processing information, and allows users to control (pause/resume/cancel) the upload.
Best used together with a simple file source plugin, such as [@uppy/file-input](https://uppy.io/docs/file-input) or [@uppy/drag-drop](https://uppy.io/docs/drag-drop), or a custom implementation. It is also included in the [@uppy/dashboard](https://uppy.io/docs/dashboard) plugin.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const StatusBar = require('@uppy/status-bar')

const uppy = Uppy()
uppy.use(StatusBar, {
  target: 'body',
  hideUploadButton: false,
  showProgressDetails: false,
  hideAfterFinish: true
})
```

## Installation

```bash
$ npm install @uppy/status-bar --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/status-bar).

## License

[The MIT License](./LICENSE).
# @uppy/store-redux

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/store-redux"><img src="https://img.shields.io/npm/v/@uppy/store-redux.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The `ReduxStore` stores Uppy state on a key in an existing Redux store.
The `ReduxStore` dispatches `uppy/STATE_UPDATE` actions to update state.
When the state in Redux changes, it notifies Uppy.
This way, you get most of the benefits of Redux, including support for the Redux Devtools and time traveling!

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const { combineReducers, createStore } = require('redux')
const Uppy = require('@uppy/core')
const ReduxStore = require('@uppy/store-redux')
const reducers = require('./reducers')

const reducer = combineReducers({
  ...reducers,
  uppy: ReduxStore.reducer
})

const store = createStore(reducer)

const uppy = Uppy({
  store: ReduxStore({
    store: store
  })
})
```

## Installation

```bash
$ npm install @uppy/store-redux --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/stores#ReduxStore).

## License

[The MIT License](./LICENSE).
# @uppy/golden-retriever

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/golden-retriever"><img src="https://img.shields.io/npm/v/@uppy/golden-retriever.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The GoldenRetriever plugin saves selected files in your browser cache (Local Storage for metadata, then Service Worker for all blobs + IndexedDB for small blobs), so that if the browser crashes, Uppy can restore everything and continue uploading like nothing happened. Read more about it [on the blog](https://uppy.io/blog/2017/07/golden-retriever/).

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const GoldenRetriever = require('@uppy/golden-retriever')

const uppy = Uppy()
uppy.use(GoldenRetriever, {
  // Options
})
```

## Installation

```bash
$ npm install @uppy/golden-retriever --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/golden-retriever).

## License

[The MIT License](./LICENSE).
# @uppy/core

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/core"><img src="https://img.shields.io/npm/v/@uppy/core.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

Uppy is a sleek, modular JavaScript file uploader that integrates seamlessly with any application. It’s fast, easy to use and lets you worry about more important problems than building a file uploader.

- **Fetch** files from local disk, remote urls, Google Drive, Dropbox, Instagram, or snap and record selfies with a camera;
- **Preview** and edit metadata with a nice interface;
- **Upload** to the final destination, optionally process/encode

**[Read the docs](https://uppy.io/docs)** | **[Try Uppy](https://uppy.io/examples/dashboard/)**

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')

const uppy = Uppy()
uppy.use(SomePlugin)
```

## Installation

```bash
$ npm install @uppy/core --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/uppy).

## License

[The MIT License](./LICENSE).
# @uppy/instagram

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/instagram"><img src="https://img.shields.io/npm/v/@uppy/instagram.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The Instagram plugin lets users import photos from their Instagram account.

A [Companion](https://uppy.io/docs/companion) instance is required for the Instagram plugin to work. Companion handles authentication with Instagram, downloads the pictures and videos, and uploads them to the destination. This saves the user bandwidth, especially helpful if they are on a mobile connection.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const Instagram = require('@uppy/instagram')

const uppy = Uppy()
uppy.use(Instagram, {
})
```

## Installation

```bash
$ npm install @uppy/instagram --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/instagram).

## License

[The MIT License](./LICENSE).
# @uppy/drag-drop

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/drag-drop"><img src="https://img.shields.io/npm/v/@uppy/drag-drop.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

Droppable zone UI for Uppy. Drag and drop files into it to upload.

**[Read the docs](https://uppy.io/docs/dragdrop)** | **[Try it](https://uppy.io/examples/dragdrop/)**

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const DragDrop = require('@uppy/drag-drop')

const uppy = Uppy()
uppy.use(DragDrop, {
  target: '#upload'
})
```

## Installation

```bash
$ npm install @uppy/drag-drop --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/dragdrop).

## License

[The MIT License](./LICENSE).
# @uppy/store-default

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/store-default"><img src="https://img.shields.io/npm/v/@uppy/store-default.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

A simple object-based store for Uppy. This one is used by default, you do not need to add it manually.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const DefaultStore = require('@uppy/store-default')

const uppy = Uppy({
  store: DefaultStore()
})
```

## Installation

```bash
$ npm install @uppy/store-default --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this package in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/stores#DefaultStore).

## License

[The MIT License](./LICENSE).
# @uppy/progress-bar

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/progress-bar"><img src="https://img.shields.io/npm/v/@uppy/progress-bar.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

ProgressBar is a minimalist plugin that shows the current upload progress in a thin bar element. Similar to the ones used by YouTube and GitHub when navigating between pages.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const ProgressBar = require('@uppy/progress-bar')

const uppy = Uppy()
uppy.use(ProgressBar, {
  // Options
})
```

## Installation

```bash
$ npm install @uppy/progress-bar --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/progressbar).

## License

[The MIT License](./LICENSE).
# @uppy/aws-s3

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/aws-s3"><img src="https://img.shields.io/npm/v/@uppy/aws-s3.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The AwsS3 plugin can be used to upload files directly to an S3 bucket. Uploads can be signed using Companion or a custom signing function.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const AwsS3 = require('@uppy/aws-s3')

const uppy = Uppy()
uppy.use(AwsS3, {
  limit: 2,
  timeout: ms('1 minute'),
  serverUrl: 'https://companion.myapp.com/'
})
```

## Installation

```bash
$ npm install @uppy/aws-s3 --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/aws-s3).

## License

[The MIT License](./LICENSE).
# @uppy/dashboard

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/dashboard"><img src="https://img.shields.io/npm/v/@uppy/dashboard.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

Dashboard is a universal UI plugin for Uppy:

 * Drag and Drop, paste, select from local disk / my device
 * UI for Webcam and remote sources: Google Drive, Dropbox, Instagram (all optional, added via plugins)
 * File previews and info
 * Metadata editor
 * Progress: total and for individual files
 * Ability to pause/resume or cancel (depending on uploader plugin) individual or all files

**[Read the docs](https://uppy.io/docs/dashboard/)** | **[Try it](https://uppy.io/examples/dashboard/)**

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const Dashboard = require('@uppy/dashboard')

const uppy = Uppy()
uppy.use(Dashboard, {
  target: 'body',
  inline: true
})
```

## Installation

```bash
$ npm install @uppy/dashboard --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/dashboard).

## License

[The MIT License](./LICENSE).
# Companion

<img src="http://uppy.io/images/logos/uppy-dog-full.svg" width="120" alt="Uppy logo — a superman puppy in a pink suit" align="right">

[![Build Status](https://travis-ci.org/transloadit/uppy.svg?branch=master)](https://travis-ci.org/transloadit/uppy)

Companion is a server integration for [Uppy](https://github.com/transloadit/uppy) file uploader.

It handles the server-to-server communication between your server and file storage providers such as Google Drive, Dropbox,
Instagram, etc. **Companion is not a target to upload files to**. For this, use a <https://tus.io> server (if you want resumable) or your existing Apache/Nginx server (if you don't). [See here for full documentation](https://uppy.io/docs/companion/)

## Install

```bash
npm install @uppy/companion
```

## Usage

companion may either be used as pluggable express app, which you plug to your already existing server, or it may simply be run as a standalone server:

### Plug to already existing server

```javascript

var express = require('express')
var bodyParser = require('body-parser')
var session = require('express-session')
var uppy = require('@uppy/companion')

var app = express()
app.use(bodyParser.json())
app.use(session({secret: 'some secrety secret'}))
...
// be sure to place this anywhere after app.use(bodyParser.json()) and app.use(session({...})
const options = {
  providerOptions: {
    google: {
      key: 'GOOGLE_KEY',
      secret: 'GOOGLE_SECRET'
    }
  },
  server: {
    host: 'localhost:3020',
    protocol: 'http',
  },
  filePath: '/path/to/folder/'
}

app.use(uppy.app(options))

```

To enable uppy socket for realtime feed to the client while upload is going on, you call the `socket` method like so.

```javascript
...
var server = app.listen(PORT)

uppy.socket(server, options)

```

### Run as standalone server
Please ensure that the required env variables are set before runnning/using companion as a standalone server. [See](https://uppy.io/docs/companion/#Configure-Standalone).

```bash
$ companion
```

If you cloned the repo from gtihub and want to run it as a standalone server, you may also run the following command from within its
directory

```bash
npm start
```

### Run as a serverless function

Companion can be deployed as a serverless function to AWS Lambda or other cloud providers through `serverless`. Check [this guide](https://serverless.com/framework/docs/getting-started/) to get started.

After you have cloned the repo go inside `examples/serverless`:
```
cd examples/serverless
```
 
You can enter your API Keys inside the `serverless.yml` file:
```
INSTAGRAM_KEY: <YOUR_INSTAGRAM_KEY>
INSTAGRAM_SECRET: <YOUR_INSTAGRAM_SECRET>
```

When you are all set install the dependencies and deploy your function:
```
npm install && sls deploy
```


See [full documentation](https://uppy.io/docs/companion/)
# @uppy/dropbox

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/dropbox"><img src="https://img.shields.io/npm/v/@uppy/dropbox.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

A description of this plugin or module goes here.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const Dropbox = require('@uppy/dropbox')

const uppy = Uppy()
uppy.use(Dropbox, {
  // Options
})
```

## Installation

```bash
$ npm install @uppy/dropbox --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/dropbox).

## License

[The MIT License](./LICENSE).
# @uppy/provider-views

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/provider-views"><img src="https://img.shields.io/npm/v/@uppy/provider-views.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

View library for Uppy remote provider plugins.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Plugin = require('@uppy/core/lib/plugin')
const ProviderViews = require('@uppy/provider-views')

class GoogleDrive extends Plugin {
  constructor () { /* snip */ }
  install () {
    this.view = new ProviderViews(this)
    // snip
  }

  render (state) {
    return this.view.render(state)
  }
}
```

## Installation

> Unless you are creating a custom provider plugin, you do not need to install this.

```bash
$ npm install @uppy/provider-views --save
```

<!-- Undocumented currently
## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/DOC_PAGE_HERE).
-->

## License

[The MIT License](./LICENSE).
# @uppy/file-input

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/file-input"><img src="https://img.shields.io/npm/v/@uppy/file-input.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

FileInput is the most barebones UI for selecting files—it shows a single button that, when clicked, opens up the browser’s file selector.

**[Read the docs](https://uppy.io/docs/fileinput)** | **[Try it](https://uppy.io/examples/xhrupload/)**

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const FileInput = require('@uppy/file-input')

const uppy = Uppy()
uppy.use(FileInput, {
  // Options
})
```

## Installation

```bash
$ npm install @uppy/file-input --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/fileinput).

## License

[The MIT License](./LICENSE).
# @uppy/xhr-upload

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/xhr-upload"><img src="https://img.shields.io/npm/v/@uppy/xhr-upload.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The XHRUpload plugin handles classic XHR uploads with Uppy. If you have an exiting Apache/Nginx/Node or whatever backend, this is probably the Uppy uploader plugin you are looking for.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const XHRUpload = require('@uppy/xhr-upload')

const uppy = Uppy()
uppy.use(Uppy, {
  // Options
})
```

## Installation

```bash
$ npm install @uppy/xhr-upload --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/xhr-upload).

## License

[The MIT License](./LICENSE).
# @uppy/aws-s3-multipart

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/aws-s3-multipart"><img src="https://img.shields.io/npm/v/@uppy/aws-s3-multipart.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The AwsS3Multipart plugin can be used to upload files directly to an S3 bucket using S3’s Multipart upload strategy. With this strategy, files are chopped up in parts of 5MB+ each, so they can be uploaded concurrently. It’s also very reliable: if a single part fails to upload, only that 5MB has to be retried.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const AwsS3Multipart = require('@uppy/aws-s3-multipart')

const uppy = Uppy()
uppy.use(AwsS3Multipart, {
  limit: 2,
  serverUrl: 'https://companion.myapp.com/'
})
```

## Installation

```bash
$ npm install @uppy/aws-s3-multipart --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/aws-s3-multipart).

## License

[The MIT License](./LICENSE).
# @uppy/thumbnail-generator

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/thumbnail-generator"><img src="https://img.shields.io/npm/v/@uppy/thumbnail-generator.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

Uppy plugin that generates small previews of images to show on your upload UI.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const ThumbnailGenerator = require('@uppy/thumbnail-generator')

const uppy = Uppy()
uppy.use(ThumbnailGenerator, {
  thumbnailWidth: 200
})
```

## Installation

```bash
$ npm install @uppy/thumbnail-generator --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

<!-- Undocumented currently
## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/DOC_PAGE_HERE).
-->

## License

[The MIT License](./LICENSE).
# @uppy/redux-dev-tools

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/redux-dev-tools"><img src="https://img.shields.io/npm/v/@uppy/redux-dev-tools.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

ReduxDevTools plugin that simply syncs with redux-devtools browser or JS extensions, and allows for basic time travel:

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const ReduxDevTools = require('uppy/redux-dev-tools')

const uppy = Uppy()
uppy.use(ReduxDevTools)
```

## Installation

```bash
$ npm install @uppy/redux-dev-tools --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/redux-dev-tools).

## License

[The MIT License](./LICENSE).
# @uppy/informer

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/informer"><img src="https://img.shields.io/npm/v/@uppy/informer.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The Informer is a pop-up bar for showing notifications. When other plugins have some exciting news (or error) to share, they can show a notification here.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const Informer = require('@uppy/informer')

const uppy = Uppy()
uppy.use(Informer, {
  target: '#mount-point'
})
```

## Installation

```bash
$ npm install @uppy/informer --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/informer).

## License

[The MIT License](./LICENSE).
# @uppy/tus

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/tus"><img src="https://img.shields.io/npm/v/@uppy/tus.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The Tus plugin brings [tus.io][] resumable file uploading to Uppy by wrapping the [tus-js-client][].

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const Tus = require('@uppy/tus')

const uppy = Uppy()
uppy.use(Tus, {
  endpoint: 'https://master.tus.io/files/', // use your tus endpoint here
  resume: true,
  autoRetry: true,
  retryDelays: [0, 1000, 3000, 5000]
})
```

## Installation

```bash
$ npm install @uppy/tus --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/tus).

## License

[The MIT License](./LICENSE).

[tus.io]: https://tus.io
[tus-js-client]: https://github.com/tus/tus-js-client
# @uppy/google-drive

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/google-drive"><img src="https://img.shields.io/npm/v/@uppy/google-drive.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The Google Drive plugin for Uppy lets users import files from their Google Drive account.

A Companion instance is required for the GoogleDrive plugin to work. Companion handles authentication with Google, downloads files from the Drive and uploads them to the destination. This saves the user bandwidth, especially helpful if they are on a mobile connection.


Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const GoogleDrive = require('@uppy/google-drive')

const uppy = Uppy()
uppy.use(GoogleDrive, {
  // Options
})
```

## Installation

```bash
$ npm install @uppy/google-drive --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/google-drive).

## License

[The MIT License](./LICENSE).
# @uppy/utils

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/utils"><img src="https://img.shields.io/npm/v/@uppy/utils.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

Shared utility functions for Uppy Core and the "official" plugins maintained by the Uppy team.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Installation

> Unless you are creating a custom plugin, you should not need to install this manually.

```bash
$ npm install @uppy/utils --save
```

## License

[The MIT License](./LICENSE).
# @uppy/companion-client

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/companion-client"><img src="https://img.shields.io/npm/v/@uppy/companion-client.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

Client library for communication with Companion. Intended for use in Uppy plugins.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const { Provider, RequestClient, Socket } = require('@uppy/companion-client')

const uppy = Uppy()

const client = new RequestClient(uppy, { serverUrl: 'https://uppy.mywebsite.com/' })
client.get('/drive/list').then(() => {})

const provider = new Provider(uppy, {
  serverUrl: 'https://uppy.mywebsite.com/',
  provider: providerPluginInstance
})
provider.checkAuth().then(() => {})

const socket = new Socket({ target: 'wss://uppy.mywebsite.com/' })
socket.on('progress', () => {})
```

## Installation

> Unless you are writing a custom provider plugin, you do not need to install this.

```bash
$ npm install @uppy/companion-client --save
```

<!-- Undocumented currently
## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/DOC_PAGE_HERE).
-->

## License

[The MIT License](./LICENSE).
# @uppy/url

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/url"><img src="https://img.shields.io/npm/v/@uppy/url.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The Url plugin lets users import files from the Internet. Paste any URL and it’ll be added!

A Companion instance is required for the Url plugin to work. Companion will download the files and upload them to their destination. This saves bandwidth for the user (especially on mobile connections) and helps avoid CORS restrictions.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const Url = require('@uppy/url')

const uppy = Uppy()
uppy.use(Url, {
  // Options
})
```

## Installation

```bash
$ npm install @uppy/url --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/url).

## License

[The MIT License](./LICENSE).
# @uppy/transloadit

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/transloadit"><img src="https://img.shields.io/npm/v/@uppy/transloadit.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The Transloadit plugin can be used to upload files to Transloadit for all kinds of processing, such as transcoding video, resizing images, zipping/unzipping, [and more](https://transloadit.com/services/).

[Try it live →](https://uppy.io/examples/transloadit/)

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const Transloadit = require('@uppy/transloadit')

const uppy = Uppy()
uppy.use(Transloadit, {
  // Plugins
})
```

## Installation

```bash
$ npm install @uppy/transloadit --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/transloadit).

## License

[The MIT License](./LICENSE).
# @uppy/webcam

<img src="https://uppy.io/images/logos/uppy-dog-head-arrow.svg" width="120" alt="Uppy logo: a superman puppy in a pink suit" align="right">

<a href="https://www.npmjs.com/package/@uppy/webcam"><img src="https://img.shields.io/npm/v/@uppy/webcam.svg?style=flat-square"></a>
<a href="https://travis-ci.org/transloadit/uppy"><img src="https://img.shields.io/travis/transloadit/uppy/master.svg?style=flat-square" alt="Build Status"></a>

The Webcam plugin for Uppy lets you take photos and record videos with a built-in camera on desktop and mobile devices.

Uppy is being developed by the folks at [Transloadit](https://transloadit.com), a versatile file encoding service.

## Example

```js
const Uppy = require('@uppy/core')
const Webcam = require('@uppy/webcam')

const uppy = Uppy()
uppy.use(Webcam, {
  mirror: true,
  facingMode: 'user'
})
```

## Installation

```bash
$ npm install @uppy/webcam --save
```

We recommend installing from npm and then using a module bundler such as [Webpack](http://webpack.github.io/), [Browserify](http://browserify.org/) or [Rollup.js](http://rollupjs.org/).

Alternatively, you can also use this plugin in a pre-built bundle from Transloadit's CDN: Edgly. In that case `Uppy` will attach itself to the global `window.Uppy` object. See the [main Uppy documentation](https://uppy.io/docs/#Installation) for instructions.

## Documentation

Documentation for this plugin can be found on the [Uppy website](https://uppy.io/docs/webcam).

## License

[The MIT License](./LICENSE).
