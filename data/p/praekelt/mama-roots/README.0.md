# mama-roots

The static site front-end for MAMA.

-------------------------

### Setup Instructions

> **Note:** for the best build experience, it is advised
> you use a Unix based OS that supports Make.

- You need to have [Node.js](http://nodejs.org) and [npm](http://npmjs.com) installed. The latest versions of Node come with `npm` built in.
- You also need to have [Roots](http://roots.cx) installed. You can install Roots using `npm` like so (the `g` flag makes it a global package):

```bash
$ npm install roots -g
```

> ***Important Note:*** You will also need to run `$ node _query_apis.js` or `$ make build-dev` before running any of the below commands, to fetch the initial data necessary for the compilation. The `_data.json` file was ignored from this repository because it can get rather large.

---------------------------

### Commands you need to know

- `$ roots compile`
  - compiles the default environment (English development) to `/public/`
- `$ roots compile -e production-sw`
  - compiles the `production-sw` (Swahili) environment to `public/lang/sw/`. Have a look at any of the `app.*.coffee` files - these are what register different environments.
- `$ roots clean`
  - removes the `public/` folder.
- `$ roots watch`
  - starts a development file watching utility for the default environment (`app.coffee`) and opens a live-reload development server on `http://localhost:1111`
- `$ node _query_apis.js`
  - running this command will fetch data from the endpoints, consolidate said data, and save it to a file called `_data.json` in the project root.

---------------------------

### Bonus `Make` commands to ease development/testing

- `$ make clean`
  - removes the `public/` folder
- `$ make build-dev`
  - cleans the `public/` folder, fetches the latest data from the MAMA api, caches the data in a local file as JSON, and then sequentially builds out each `development` environment.
- `$ make build-prod`
  - does the same as the previous command, except for `production`.

------------------------------

### What are all these environments for?

Roots is an amazing static site generator, but it unfortunately lacks support
for internationalization standards for the time being. Using environments is a necessary compromise in that regard.

--------------------------------

### What's going on behind the scenes here?

This repository uses a Roots extension called [roots-records](https://github.com/carrot/roots-records) and a manual HTTP request inside a `before` compile hook (which can be found in any of the `app.coffee` files) to consolidate data
found at 3 endpoints into one more easily-consumable local API by transforming
the data and writing it as JSON to a local file. That data is then read in and passed to the templating engine as local variables.

---------------------------------

### Any important notes?

Yes. The locals provided to the templating engine via the `before` hook
are absolutely necessary in order to provide layout files and `roots-records`-specific single view template files with the necessary local variables, due to a bug in `roots-records`. So, if you wish to use new local variables inside layout files or single view templates, that `before` hook is where you should put them. The existing code there is fairly simple to learn from.

---------------------------------
