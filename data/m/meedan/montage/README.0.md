The majority of the extension can be edited easily, however the Content Script
is written in Google Closure and thus needs to be built.

To build, run the following lines to compile the code:
`closure-library/closure/bin/build/closurebuilder.py --root=closure-library/ --root=js/ --namespace="greenday.extension.App" --output_mode=compiled --compiler_jar=compiler.jar > js/content_script.js`

You should then deploy it to the Chrome Webstore.

When making changes to the Chrome Webstore make sure you increase the version
number inside of the manifest.json.

If you change the URL of the web app you will need to update it inside of both
the app.js, background.js and manifest.json file.

If there are major changes to the YouTube UI you will also need to change the
extension.

If for some reason the closure-library does not exist. Then make sure you
download it using the line:
`git clone https://github.com/google/closure-library`

Enjoy the extension!
GAE Defer Manager (ALPHA)
========================

[![Build Status](https://travis-ci.org/nealedj/gae_defer_manager.svg?branch=master)](https://travis-ci.org/nealedj/gae_defer_manager)

## A library to wrap deferring tasks on the Google App Engine Taskqueue API

gae_defer_manager is a wrapper for the deferred library in the Google App Engine SDK to expose the following functionality:

* Task status
* Task ETA
* Allows prevention on duplicate tasks from being added based on an arbitrary reference key


## Setup

Include the deferred_manager folder in your project.

Add the following handlers to your app.yaml file (and any other module config files as required):

```yaml
handlers:
  - url: /_ah/queue/deferred
    script: deferred_manager.handler.application
    login: admin
    secure: always

  - url: /_ah/deferredconsole/static/
    static_dir: deferred_manager/static
    expiration: 1d

  - url: /_ah/deferredconsole.*
    script: deferred_manager.application
    login: admin
    secure: always
```

Change any calls to `google.appengine.ext.deferred.defer` to `deferred_manager.defer`

## Usage

Pass arguments to `defer()` in the same way as you would to the GAE defer function.

Optionally, you can pass the following arguments:

- **task_reference**: an arbitrary reference to allow you to identify the task
- **unique_until**: a datetime object. If passed then no other tasks with the same task_reference will be allowed to be deferred until after this datetime.

## Task console

The task console can be found at /_ah/deferredconsole/static/index.html

## Limitations

Adding deferred tasks is limited to one task per second per queue. This is because a datastore entity is saved to persist the task state. It is kept in an entity group to ensure that it returned when the task actually runs.

Screenshots
-----------

![screenshot1](/../screenshots/_screenshots/1.png?raw=true)
![screenshot1](/../screenshots/_screenshots/2.png?raw=true)
![screenshot1](/../screenshots/_screenshots/3.png?raw=true)
![screenshot1](/../screenshots/_screenshots/4.png?raw=true)
![screenshot1](/../screenshots/_screenshots/5.png?raw=true)
![screenshot1](/../screenshots/_screenshots/6.png?raw=true)
![screenshot1](/../screenshots/_screenshots/7.png?raw=true)
![screenshot1](/../screenshots/_screenshots/8.png?raw=true)
# Django ProtoRPC

[![Build Status](https://travis-ci.org/nealedj/django-protorpc.svg?branch=master)](https://travis-ci.org/nealedj/django-protorpc)

A library to construct [ProtoRPC](https://code.google.com/p/google-protorpc/) messages from Django models.

Designed to help you keep your [Google Cloud Endpoints](https://cloud.google.com/appengine/docs/python/endpoints/) APIs DRY.


## Installation

[Hosted on PyPI](https://pypi.python.org/pypi/django-protorpc). Either install with:


	$ pip install django-protorpc

Or:


	$ easy_install django-protorpc

If you prefer to use the development version of it, you can clone the repository
and build it manually:

	$ git clone https://github.com/nealedj/django-protorpc.git
	$ cd django_protorpc
	$ python setup.py install

## Usage

	from django_protorpc import DjangoProtoRPCMessage

	class MockMessageOne(DjangoProtoRPCMessage):
		class Meta:
			model = MyModel
			fields = ('foo', 'bar',)

	class MockMessageTwo(DjangoProtoRPCMessage):
		class Meta:
			model = MyModel
			exclude = ('baz',)
