eTools Frontend Template
====================================

Installation
------------

Using git, clone to a local directory:

```bash
$ git clone https://github.com/unicef-polymer/etools-frontend-template.git
```
Assuming node and npm are already installed, make sure bower is also installed, if not run:

```bash
$ npm install -g bower
```
Also install polymer-cli:
```bash
$ npm install -g polymer-cli
```

Install packages:
```bash
$ npm install
$ bower install
```

Build Application
-----------------

To build the distribution version:

```bash
$ gulp
```

We will be using a bundled build since we don't support
HHTP/2 and server push.

Before the build is created the CSS and images are minified,
Javascript is uglifyed, also there are javascript and html hints.
If any of these tasks fail, the entire build process fails.
So correct your code and try again :)

Run Application
---------------

To run the application you can use:

```bash
$ polymer serve
View your app at http://localhost:8082
```
This command will start the server and serve your files directly from app sources.
At this point you do not need to build anything, the files will not be served from build folder.

```bash
$ polymer serve build/bundled
View your app at http://localhost:8082
```
This command will start the server and use the bundled build (build/bundled folder) to serve the files from.
Before you can serve the bundled build you have to generate the build files.
Service worker only works in the built app, so test service worker functionality here.

Additional options for gulp tasks
---------------------------------

Set -l parameter for any gulp task to activate polymer logs during build process

```bash
$ gulp -l
```
