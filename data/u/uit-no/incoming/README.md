Incoming!!
==========

Large file uploads with web browsers are frustrating because you can not implement them in a straightforward and painless way. When implemented wrong, they stall your web app and might even break it, and implementing them right is not easily done. Incoming!! handles large file uploads for your web apps so you don't have to. In the browser, it chops up a large file into little pieces, transfers those over to its own server application, which puts them together, stores them, and finally hands the uploaded file over to your web app backend. Disconnects during upload are no problem, and explicit pause / resume is also supported. With Incoming!!, both the complexity and performance impact of large file uploads are off your web app's back.

Incoming!! consists of a server application and a JavaScript client library. The server(s) can run alongside your web app backend or centrally in your organization, and the JavaScript client is used directly in your web app's frontend in the browser.

When you want to upload a large file, your web app backend first fetches an upload ticket from the Incoming!! server. Then, using that ticket, your frontend can use the Incoming!! JavaScript library to send the large file to the Incoming!! server. When the upload is finished, the Incoming!! server hands the file over to your web app backend.

Your web app backend and the Incoming!! server communicate through simple HTTP requests: Incoming!! provides an endpoint for handing out upload tickets, and issues a request to your web app backend when an upload is finished. To its JavaScript library, Incoming!! exposes a WebSocket server. Incoming!! also hosts the JavaScript library file.

The Incoming!! server is implemented in Go, and the JavaScript library in, well, JavaScript, without use of external libraries. The whole thing is free and open source. The server is licensed under the copyleft [AGPLv3](http://choosealicense.com/licenses/agpl-3.0/), and the client library under the permissive [MIT License](http://choosealicense.com/licenses/mit/).


Status
------

Incoming!! is in development. Most of it is in place and works. It can already be used, but we don't consider it and the API stable yet.

At the present stage of development, Incoming!! can already be deployed together with an individual application, or centrally in your organization. However, for the latter case to be viable, Incoming!! should be able to scale out with several server instances in order to provide ample upload bandwidth. This has always been in the backs of our heads during design and implementation, and is the next major feature we will implement.


Quickstart
----------

If you have [Vagrant](http://www.vagrantup.com) (1.5 or newer) and [Ansible](http://www.ansible.com/home) installed, you can get a complete example installation of Incoming!!, including an example web app, up and running like this:

    $ git clone https://github.com/uit-no/incoming.git
    $ vagrant up

When the Vagrant VM is ready, point your browser (which must run on the same machine that hosts the Vagrant VM) to <http://10.20.1.4> and start playing with Incoming!!.


Usage example
-------------

Simple backend code in Python (using the tiny [Bottle](http://bottlepy.org/) web framework) can look like the following.

Request an upload ticket from the Incoming!! server like this (using the [Requests](http://python-requests.org) library):

```python
req = requests.post("http://INCOMING_HOSTNAME/incoming/0.1/backend/new_upload",
                     params = { "signalFinishURL" : "http://APP_HOSTNAME/api/backend/upload_finished" })
```

In the request for a ticket, you tell the Incoming!! server which URL to POST to later when the upload is finished.

The request returns the upload ticket ID, which you somehow give to your frontend. For example, if you are just answering a request for a file upload page, you could simply render the upload ticket ID into a template.

```python
upload_id = req.text
return template("upload_page_template.html", upload_id = upload_id)
```

Later, when the upload is finished, the Incoming!! server will POST to the URL you specified above. In that request, you get the path of the uploaded file so you can move the file to its destination. This is how a handler for that URL can look like in your web app backend:

```python
@post('/api/backend/upload_finished')
def retrieve_incoming_file() :
    upload_id = request.params["id"]

    if request.params["cancelled"] != "yes" :
        incoming_path = request.params["filename"]
        shutil.move(incoming_path, os.path.join("uploads", request.params["filenameFromBrowser"]))
    else :
        # we don't care. request.params["cancelReason"] contains a text describing
        # why the upload cancelled. It also doesn't matter what we answer.

    return "done"
```

After you return "done", the Incoming!! server notifies your frontend that the upload is all done. Then both your backend and your frontend know that the upload is finished.

Speaking of your frontend, here's what you need to do there. First, you have to load the Incoming!! JavaScript library:

```html
<script src="http[s]://INCOMING_HOSTNAME/incoming/0.1/frontend/incoming.js"></script>
```

Then, you need some sort of file input, for example a file input field. To that, you can attach an event handler to kick off an upload as soon as the user chooses a file:

```html
<input type="file" id="input_file" onchange="upload_file('{{ upload_id }}', this.files[0])"/>
```

Here, we have rendered in the upload ticket id in the backend. You could of course obtain a ticket in other ways, for example with an extra bit of JavaScript that does an HTTP request to your backend (one of our example apps does that).

You can then configure and start an upload like this:

```javascript
function upload_file(upload_id, f) {
    // define a callback for when upload is finished (i.e., the web app backend
    // got the file)
    var finished = function(uploader) {
        alert("yay, upload is finished");
    };

    // initialize and start uploader
    var uploader = incoming.Uploader(upload_id, f);
    uploader.onfinished = finished;
    uploader.start();
}
```

When `uploader.start()` is called, Incoming!! will do its thing. When everything is done, that is, when the file has been uploaded and handed over to your web app backend, your "upload is finished" callback is called. Then you know that your app has gotten the file.

This is basically it. We ship two example web apps that serve as more comprehensive code examples, handling errors and covering more of Incoming!!'s features. In most usage scenarios there is also the webserver / reverse proxy config to take care of. For that, we also document and ship an example.


Documentation
-------------

* [System overview: motivation, design, integration eight-miles-up](doc/overview.md)
* [Installation: manual or automated installation of Incoming!!, example apps, and an example reverse proxy](doc/installation.md)
* [Getting started: example web apps using Incoming!!](doc/examples.md)
* [Incoming!! Frontend and Backend API](doc/api.md)
* [Important notes for developers and users](doc/notes.md)


Changelog, roadmap etc.
-----------------------

* [Changelog](doc/changelog.md)
* [Roadmap](doc/roadmap.md)


Licensing and copyright
-----------------------

The Incoming!! server is licensed under the [AGPLv3](http://choosealicense.com/licenses/agpl-3.0/), while all the rest, most importantly the JavaScript client library, is licensed under the [MIT License](http://choosealicense.com/licenses/mit/). See individual files for details. If not stated otherwise, a source file is licensed under the MIT License.

The rationale behind using AGPL and MIT License for different parts of Incoming!! is the following: enhancements to Incoming!! itself should always be contributed back to the community, but applications that use Incoming!! need not. We think that the license model we chose reflects this best. A popular project that uses the same approach is [MongoDB](http://www.mongodb.org/about/licensing/#licensing-policy).

For clarity: *no application you write that just uses Incoming!! has to be open-sourced.* Your app's backend talks to an Incoming!! server via HTTP (which does not trigger a copyleft condition), and its frontend downloads and uses the Incoming!! JavaScript library, which is licensed under the permissive MIT license (like many other JavaScript libraries). So if you run an unmodified Incoming!! server and use Incoming!! in your web app, you have no obligations other than leaving the JavaScript libraries' copyright header intact. If you improve Incoming!! itself, you are obligated to share only your version of Incoming!!, not any of your apps that use it.

All documentation in the [doc](doc/) directory, including figures, is licensed under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/"), a permissive license for content that is not code.

All content in the repository, unless stated otherwise, is copyright (c) 2014 Lars Tiede, UiT The Arctic University of Norway


Acknowledgements
----------------

Incoming!! couldn't exist without many and more open source works that we either built on or used during development. In the following, we credit third-party works that we either include or link to.

Third-party libraries the Incoming!! server uses (none were modified, and none are distributed in this repository):

* [osext](https://bitbucket.org/kardianos/osext/src) is copyright (c) 2012 The Go Authors. [License](ext_licenses/osext.txt) (permissive).
* The Gorilla web framework's [mux](https://github.com/gorilla/mux) component is Copyright (c) 2012 Rodrigo Moraes. [License](ext_licenses/gorilla.txt) (permissive).
* The Gorilla web framework's [WebSocket](https://github.com/gorilla/websocket) component is Copyright (c) 2013 The Gorilla WebSocket Authors. [License](https://github.com/gorilla/websocket/blob/master/LICENSE) (permissive).
* [go-yaml](https://github.com/go-yaml/yaml/tree/v1) is Copyright (c) 2011-2014 - Canonical Inc. [License](ext_licenses/go-yaml.txt) (LGPL3 with exception for static linking).
* [go-uuid](https://code.google.com/p/go-uuid/) is Copyright (c) 2009,2014 Google Inc. [License](ext_licenses/go-uuid.txt) (permissive).


Third-party libraries and components used by the example web apps:

* The [Bottle](http://bottlepy.org/docs/dev/index.html#license) web framework is Copyright (c) 2014, Marcel Hellkamp, and licensed under the MIT license.
* The [Requests](http://docs.python-requests.org/en/latest/user/intro/#apache2) library is Copyright 2014 Kenneth Reitz, and licensed under the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0) license.
* The [click](http://click.pocoo.org/3/license/) package is Copyright (c) 2014 Armin Ronacher. [License](http://click.pocoo.org/3/license/) (permissive).

Third-party components used by the example Ansible, Docker and Vagrant setups:

* The [nginx Dockerfile](https://github.com/dockerfile/nginx) we use and distribute (unchanged) is Copyright (c) Dockerfile Project, and licensed under the MIT license.
* [https://github.com/phusion/open-vagrant-boxes](https://github.com/phusion/open-vagrant-boxes) (Docker-friendly base boxes for Vagrant) and [https://github.com/phusion/baseimage-docker](https://github.com/phusion/baseimage-docker) (Ubuntu base image modified for Docker-friendliness) are both Copyright (c) 2013-2014 Phusion, and licensed under the MIT license.
* Our Ansible role for installing the [Go](http://golang.org) programming language includes a binary distribution archive of it. Go's [license](http://golang.org/LICENSE) is permissive.
