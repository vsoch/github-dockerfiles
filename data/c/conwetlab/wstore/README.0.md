## 2.0 BOOTSTRAP JS PHILOSOPHY
These are the high-level design rules which guide the development of Bootstrap's plugin apis.

---

### DATA-ATTRIBUTE API

We believe you should be able to use all plugins provided by Bootstrap purely through the markup API without writing a single line of javascript.

We acknowledge that this isn't always the most performant and sometimes it may be desirable to turn this functionality off altogether. Therefore, as of 2.0 we provide the ability to disable the data attribute API by unbinding all events on the body namespaced with `'data-api'`. This looks like this:

    $('body').off('.data-api')

To target a specific plugin, just include the plugins name as a namespace along with the data-api namespace like this:

    $('body').off('.alert.data-api')

---

### PROGRAMATIC API

We also believe you should be able to use all plugins provided by Bootstrap purely through the JS API.

All public APIs should be single, chainable methods, and return the collection acted upon.

    $(".btn.danger").button("toggle").addClass("fat")

All methods should accept an optional options object, a string which targets a particular method, or null which initiates the default behavior:

    $("#myModal").modal() // initialized with defaults
    $("#myModal").modal({ keyboard: false }) // initialized with now keyboard
    $("#myModal").modal('show') // initializes and invokes show immediately afterqwe2

---

### OPTIONS

Options should be sparse and add universal value. We should pick the right defaults.

All plugins should have a default object which can be modified to effect all instance's default options. The defaults object should be available via `$.fn.plugin.defaults`.

    $.fn.modal.defaults = { … }

An options definition should take the following form:

    *noun*: *adjective* - describes or modifies a quality of an instance

examples:

    backdrop: true
    keyboard: false
    placement: 'top'

---

### EVENTS

All events should have an infinitive and past participle form. The infinitive is fired just before an action takes place, the past participle on completion of the action.

    show | shown
    hide | hidden

---

### CONSTRUCTORS

Each plugin should expose it's raw constructor on a `Constructor` property -- accessed in the following way:


    $.fn.popover.Constructor

---

### DATA ACCESSOR

Each plugin stores a copy of the invoked class on an object. This class instance can be accessed directly through jQuery's data API like this:

    $('[rel=popover]').data('popover') instanceof $.fn.popover.Constructor

---

### DATA ATTRIBUTES

Data attributes should take the following form:

- data-{{verb}}={{plugin}} - defines main interaction
- data-target || href^=# - defined on "control" element (if element controls an element other than self)
- data-{{noun}} - defines class instance options

examples:

    // control other targets
    data-toggle="modal" data-target="#foo"
    data-toggle="collapse" data-target="#foo" data-parent="#bar"

    // defined on element they control
    data-spy="scroll"

    data-dismiss="modal"
    data-dismiss="alert"

    data-toggle="dropdown"

    data-toggle="button"
    data-toggle="buttons-checkbox"
    data-toggle="buttons-radio"# How to use this Dockerfile

You can build a docker image based on this Dockerfile. This image will contain only a WStore instance, exposing port `8000`. This requires that you have [docker](https://docs.docker.com/installation/) installed on your machine.

If you just want to have a WStore running as quickly as possible jump to section *The Fastest Way*.

If you want to know what is behind the scenes of our container you can go ahead and read the build and run sections.

## The Fastest Way

To run WStore using Docker, just run the following command (*replace `PORT` by the port of your local machine that will be used to access the service*):

```
sudo docker run -d --name wstore -p PORT:8000 conwetlab/wstore 
```

You can access the WStore with a default user with user name `admin` and password `admin`. 

## Build the image

If you have downloaded the [WStore's source code](https://github.com/conwetlab/wstore/) you can build your own image. The end result will be the same, but this way you have a bit more of control of what's happening.

To create the image, just navigate to the `docker` directory and run:

    sudo docker build -t wstore .

> **Note**
> If you do not want to have to use `sudo` in this or in the next section follow [these instructions](http://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo).


The parameter `-t wstore` gives the image a name. This name could be anything, or even include an organization like `-t conwetlab/wstore`. This name is later used to run the container based on the image.

If you want to know more about images and the building process you can find it in [Docker's documentation](https://docs.docker.com/userguide/dockerimages/).
    
### Run the container

The following line will run the container exposing port `8000`, give it a name -in this case `wstore1`. This uses the image built in the previous section.

    sudo docker run -d --name wstore1 -p 8000:8000 wstore

As a result of this command, there is WStore listening on port 8000 on localhost.

A few points to consider:

* The name `wstore1` can be anything and doesn't have to be related to the name given to the docker image in the previous section.
* In `-p 8000:8000` the first value represents the port to listen on localhost. If you want to run a second WStore on your machine you should change this value to something else, for example `-p 8001:8000`.
