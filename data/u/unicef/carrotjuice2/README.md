CarrotJuice
===========

### Dependencies

-   [MagicBox](<https://github.com/mikefab/majicbox>) must be running (and run
    its setup)

-   If you don' have token: `NODE_ENV=development nodemon server.js`

### Setup

-   `npm install`. Use Node 5.6.0; we suggest following NVM instructions for any
    OS.

-   Copy `config-example.js` to `config.js`. It should be good out-of-the-box,
    but take a look to see if you need to edit anything.

-   [deprecated] Add your email address to whitelist array

-   Concurrently run both `nodemon server.js` and `make dev`. The former is the
    actual server, and the latter watches for changes and rebuilds front-end
    files.

-   [deprecated] Sign up with email address

### Running tests

**Mocha frontend tests** use Mocha (to organize test suites and such) within the
browser, to test components as they modify the DOM. You can either run these by
simply going to `localhost:8080/test.html`, or running `make phantomjs-tests`
(which uses Docker, suitable for running tests automatically via the command
line).

New code path notes (React)
---------------------------

The new code path uses React, and P.js-based models (simple object-oriented
classes). The relationship between views and models is like,

![model](<https://github.com/mikefab/carrotjuice2/raw/master/icon/readme-figure.png>)

The design principles here are:

-   Stateless views: A huge tip for keeping front-end design clean is to **keep
    state out of views** (or controllers). Jason Merrill at Desmos mentioned
    that one could aim to model all view state, even animation, to reduce bugs.

-   Separation of views and models: All models are instantiated at root-level
    and passed down to views through props. If this ever becomes unwieldy, we
    should just make meta-models (models that contain other models). This
    obviously goes with the former, but also makes it effortless to shift around
    view structure. Different views require the same state, e.g. the date-picker
    references the currently-selected date, and also have the map reference the
    currently-selected date.

Developer API
-------------

### Dictionary

-   divis\_kind: division kind - Any polygon that can be drawn on a map. Kinds
    inlcude: admin, cell.

-   country\_iso: ISO 3166-1 alpha-2 – two-letter country codes

### Routes

-   /api/diagonal/:divis\_kind/:country\_iso

Called from function: `fetch_matrix_then_draw`

Fetches diagonal of the mobility matrix. i.e. the number of people who've made
two calls from the same tower. We think this is a measure of population density.
It's a dynamic estimate. It changes from day.

Currently fetches matrix for one single day

The max value of the Diagonal of matrix is used to normalize all diagonal
values. These values are used in the opacity of polygon colors to represent
population density.

-   /api/division/:divis\_kind/:country\_iso

Called from function: `fetch_geojson_for_divisions`

Fetches geojson for either admin 2 polygons or voranoi cells to be displayed on
map.

TODO(mikefab): Change 'division' to 'geojson'

Notes
-----

-   Clicking is not enabled (coming soon)
