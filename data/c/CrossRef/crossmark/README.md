# Crossmark Dialog Server

Service for showing the Crossmark dialog and serving up assets.

## Versioning

The server (i.e. the 'Crossmark service') is versioned, and the version number can be found in the `project.clj` file. Major, minor and point release numbers are used. This is the version of the service, which serves up both the widget code and the contents of the dialog. There is only one current version of Crossmark service.

The widget itself is versioned. Major and minor versions are used, and correspond to the current server version, but point releases are not used. This is because the script must be referenced explicitly in the publisher's site when they embed the version. A major or minor release requires a publisher to change their HTML, which should happen very infrequently. As such, point releases are not reflected in the version as indicated in the path of the script. However, the full version is included in the content of the script.

## CDN

A CDN should be provided for assets, mirroring the URLs on this service. The CDN ensures that hotlinked assets, such as the logo image and the widget script, load fast. The CDN should cache assets for no longer than 24 hours (and optionally be invalidated on a deploy).

The widget script should be hotlinked directly to the CDNed version, *not rehosted*. The technical documentation for Crossmark includes instructions for how to implement Crossmark on a page. It's important to know when an out-of-date script is being used because out-of-date versions may not include bugfixes.

When the script is served, a signed JWT is included that indicates when the script was generated. When served through a CDN this will be cached, so the script will always contain a cryptographically verifiable tag of when it was originally served up. This is passed back to the service when the dialog is called. The script verification functionality will raise an error when a script older than 5 days is used, leaving a few days' grace.

## Configuration

Configuration is done via environment variables.

 - `PORT` - port to run server on
 - `CDN_URL` - public URL of CDN, e.g. `https://crossmark-cdn.crossref.org`. For development, should be set to e.g. `http://localhost:8000`.
 - `CROSSMARK_SERVER` - public url of where this service is running, e.g. `https://crossmark.crossref.org`. For development, should be set to e.g. `http://localhost:8000`.
 - `JWT_SECRET` - a secret for encoding JWTs
 - `API_BASE` - custom base of REST API. Defaults to `https://api.crossref.org`
 - `PUSH_URL` - URL for reporting stats
 - `PUSH_TOKEN` - token for reporting status

## Deployment

The server can be deployed either running directly or via Docker.

### Running directly

1. Generate a JWT secret.
2. Create a file that resembles `run.sh.example`
3. Run it! 

### Running with Docker

Run via Docker Swarm, or create a `docker-compose.yml` file with above environment variables.

## Tinkering

Run the server:

    time docker-compose run --service-ports -w /usr/src/app test lein run

Then visit, e.g.:

    http://localhost:8000/dialog?doi=10.1016/j.earscirev.2013.04.010

## Quality

### Tests 

Tests are split into two categories:

 - 'server' tests generally take a metadata API response and build a context object (passed into the HTML render). The context object is tested.
 - 'browser' tests execute the widget in a headless browser

#### Server tests

To run server tests:

    time docker-compose run -w /usr/src/app test lein test

#### Browser tests

For browser tests PhantomJS must be installed. This runs on the host machine (for now).

Run the server in the background:

    time docker-compose run --service-ports -w /usr/src/app test lein run

Then run tests:

    phantomjs js-tests/tests.js

Errors are reported on console, plus a nonzero exit code for any failure.

Tests are written in `js-tests/tests.js` with accompanying HTML files in the `resources/test` directory. Each HTML file makes a callback to say that it's ready. See examples.

### Quality

Run code quality check:

    time docker-compose run -w /usr/src/app test lein eastwood

### Coverage

Code coverage from running all tests. Results are found in `target/coverage`.

    lein cloverage

### Test TODOs

Test stubs are marked with the `:todo` tag.

### Check

Pre-release check everything. Don't release unless this passes!

    ./check.sh

## License

Copyright © Crossref

Distributed under the The MIT License (MIT).
