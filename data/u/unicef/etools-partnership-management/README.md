eTools Partnership Management
====================================

Installation
------------

Using git, clone to a local directory:

```bash
$ git clone https://github.com/unicef/etools-partnership-management.git
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

or run:

```bash
$ ./dev-reinstall.sh
```

Build Application
-----------------
Lint your code:
```bash
$ npm run lint
```
and fix all ESLint and `polymer lint` errors.

For `polymer lint` there are some exception:
* `The element app-shell is not defined` - caused by file import being made in js code.
* `data-* attributes must be accessed as attributes. i.e. you must write:  data-items$="{{...}}` - `dataItems` property 
exists, escape or rename in future updates.

To build the app, just run (**the build will fail if there are eslint errors**):

```bash
$ npm run build
```

We will be using a bundled build since we don't support
HHTP/2 and server push.

2 builds are generated: ES5 and ES6 and the server will know which build to serve 
by browser capabilities.

Run Application
---------------

This application is part of [etools-infra](https://github.com/unicef/etools-infra) 
and runs under a customized setup of etools apps. After `etools-infra` is installed the PMP ap can be accessed 
for devs at `http://localhost:8082/pmp`


