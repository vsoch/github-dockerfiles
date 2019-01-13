## DataKit -- Orchestrate applications using a Git-like dataflow

*DataKit* is a tool to orchestrate applications using a Git-like dataflow. It
revisits the UNIX pipeline concept, with a modern twist: streams of
tree-structured data instead of raw text. DataKit allows you to define
complex build pipelines over version-controlled data.

DataKit is currently used as the coordination
layer for [HyperKit](http://github.com/docker/hyperkit), the
hypervisor component of
[Docker for Mac and Windows](https://blog.docker.com/2016/03/docker-for-mac-windows-beta/), and
for the [DataKitCI][] continuous integration system.

---

[![Build Status (OSX, Linux)](https://travis-ci.org/moby/datakit.svg)](https://travis-ci.org/moby/datakit)
[![Build status (Windows)](https://ci.appveyor.com/api/projects/status/6qrdgiqbhi4sehmy/branch/master?svg=true)](https://ci.appveyor.com/project/moby/datakit/branch/master)
[![docs](https://img.shields.io/badge/doc-online-blue.svg)](https://docker.github.io/datakit/)

There are several components in this repository:

- `src` contains the main DataKit service. This is a Git-like database to which other services can connect.
- `ci` contains [DataKitCI][], a continuous integration system that uses DataKit to monitor repositories and store build results.
- `ci/self-ci` is the CI configuration for DataKitCI that tests DataKit itself.
- `bridge/github` is a service that monitors repositories on GitHub and syncs their metadata with a DataKit database.
  e.g. when a pull request is opened or updated, it will commit that information to DataKit. If you commit a status message to DataKit, the bridge will push it to GitHub.
- `bridge/local` is a drop-in replacement for `bridge/github` that just monitors a local Git repository. This is useful for local testing.

### Quick Start

The easiest way to use DataKit is to start both the server and the client in containers.

To expose a Git repository as a 9p endpoint on port 5640 on a private network, run:

```shell
$ docker network create datakit-net # create a private network
$ docker run -it --net datakit-net --name datakit -v <path/to/git/repo>:/data datakit/db
```

*Note*: The `--name datakit` option is mandatory.  It will allow the client
to connect to a known name on the private network.

You can then start a DataKit client, which will mount the 9p endpoint and
expose the database as a filesystem API:

```shell
# In an other terminal
$ docker run -it --privileged --net datakit-net datakit/client
$ ls /db
branch     remotes    snapshots  trees
```

*Note*: the `--privileged` option is needed because the container will have
to mount the 9p endpoint into its local filesystem.

Now you can explore, edit and script `/db`. See the
[Filesystem API][]
for more details.

### Building

The easiest way to build the DataKit project is to use [docker](https://docker.com),
(which is what the
[start-datakit.sh](https://github.com/moby/datakit/blob/master/scripts/start-datakit.sh) script
does under the hood):

```shell
docker build -t datakit/db -f Dockerfile .
docker run -p 5640:5640 -it --rm datakit/db --listen-9p=tcp://0.0.0.0:5640
```
These commands will expose the database's 9p endpoint on port 5640.

If you want to build the project from source without Docker, you will need to install
[ocaml](http://ocaml.org/) and [opam](http://opam.ocaml.org/). Then write:

```shell
$ make depends
$ make && make test
```

For information about command-line options:

```shell
$ datakit --help
```

## Prometheus metric reporting

Run with `--listen-prometheus 9090` to expose metrics at `http://*:9090/metrics`.

Note: there is no encryption and no access control. You are expected to run the
database in a container and to not export this port to the outside world. You
can either collect the metrics by running a Prometheus service in a container
on the same Docker network, or front the service with nginx or similar if you
want to collect metrics remotely.

## Language bindings

* **Go** bindings are in the `api/go` directory.
* **OCaml** bindings are in the `api/ocaml` directory. See `examples/ocaml-client` for an example.

## Licensing

DataKit is licensed under the Apache License, Version 2.0. See
[LICENSE](https://github.com/moby/datakit/blob/master/LICENSE.md) for the full
license text.

Contributions are welcome under the terms of this license. You may wish to browse
the [weekly reports](reports) to read about overall activity in the repository.

[DataKitCI]: https://github.com/moby/datakit/tree/master/ci
[Filesystem API]: https://github.com/moby/datakit/tree/master/9p.md
To run test on windows, launch the a datakit server with --url \\.\pipe\datakit-test# DataKitCI

DataKitCI is a continuous integration service that monitors your GitHub project and tests each branch, tag and pull request.
It displays the test results as status indicators in the GitHub UI.
It keeps all of its state and logs in [DataKit][], rather than a traditional relational database, allowing review with the usual Git tools.

A complete deployment is made up of several components:


    GitHub  <-------------------- User
      ^                            |
      |                            |
      |                            |
      V                            V
    GitHub ----> DataKit <----- DataKitCI
    bridge

1. Users create and update pull requests on GitHub.
2. A GitHub bridge service monitors these events and records them in DataKit.
3. DataKitCI monitors DataKit and runs the tests.
4. The user can monitor the progress of the tests with DataKitCI's web interface.
5. DataKitCI writes status updates to DataKit.
6. The GitHub bridge pushes the status updates back to GitHub.

Since DataKitCI does not interact with GitHub directly, you can always turn off the bridge and test DataKitCI against a local DataKit to see what it would do without affecting your GitHub project.
When you're happy with the results, simply start the GitHub bridge to sync everything again.


## Installation

The `self-ci` directory contains the configuration we use to test DataKit itself.
`self-ci/README.md` explains how to use Docker Cloud to deploy your own instance.

The `skeleton` directory contains a very minimal example for this tutorial.
You can build the example using Docker:

    cd ci/skeleton
    docker build -t my-ci --build-arg CONFIG=exampleCI .

`--build-arg CONFIG=exampleCI` tells it to use the configuration in the file `exampleCI.ml`.
See below for information on writing configuration files.

Then run your new image:

    docker run --name=my-ci -p 8443:8443 my-ci --metadata-store tcp:127.0.0.1:5640

The arguments are:

- `--name=my-ci` is the name Docker will give to this container.
- `-p PORT:8443` tells Docker to expose port 8443 (the https web UI) on host port `PORT`.
- `my-ci` is the image you just built.
- `--metadata-store tcp:HOST:PORT` is the address of your running DataKit server.

On the first run, you will see a log message containing a setup URL, e.g.

```
2016-12-19 16:32.47 APP [datakit-ci] >>> Configure the CI by visiting
                                     https://127.0.0.1:8443/auth/intro/XK2qPqmIGnc3_VG1OQ_EDg==
```

To view your new service, open this URL in a web browser.

Note: The server automatically generates an X.509 certificate for itself on the first run.
Since this is self-signed, you'll probably have to click through some kind of security warning.
If you wish to use your own key and certificate, find the container's `secrets` volume, replace the files (`server.key` and `server.crt`) and restart.

Once the CI loads, it will prompt you to choose a password for the "admin" user.
Enter a password and then log in as your new user.

## Writing tests

DataKitCI is configured by writing a build expression.
Copy `exampleCI.ml` as `configCI.ml` and edit the copy.

The value `projects` is a [cmdliner][] term that describes how to create the configuration by parsing command-line arguments.
The result is a list of named projects and, for each one, a list of named tests (e.g. "build", "docs", etc).
Each test is of type `string Term.t`.
An `'a Term.t` is a term that can be evaluated in the context of a GitHub pull request or branch to produce a value of some type `'a`.
In this case, the `string` is the message to display on success (e.g. "All tests passed!").

Here's a trivial example:

```ocaml
(* An example test that just always returns success. *)
let my_test =
  Term.return "Success!"

(* The configuration for a project that has a single test called "my-test". *)
let my_project = [
  "my-test", my_test;
]

(* A list of GitHub projects to monitor and the tests to apply to the open PRs and branches in each one. *)
let my_projects = [
  "me/my-project", my_project;
]

(* Parsing of command-line options (none in this example). *)
let projects =
  Cmdliner.Term.pure my_projects

(* The main entry-point *)
let () =
  DataKitCI.Main.run projects
```

This parses no command-line arguments (it is a "pure" cmdliner value) and applies `my_test` to every open PR and branch in "https://github.com/me/my-project" (change `me/my-project` to your own project path, of course).

You can compile your new configuation with:

    docker build -t my-ci --build-arg CONFIG=configCI .

If you run DataKitCI now, you should see all your PRs reporting success for the "unit-tests" test on GitHub and in the web-UI (currently <https://localhost:8443>).

A Term can evaluate to a successful result (as here), to a failure, or to pending. e.g.

```ocaml
let my_test = Term.fail "Test failed!"
```

Note that DataKitCI keeps all open PRs up-to-date, so restarting DataKitCI after changing to the second example will switch all of your open PRs from success to failure.
You can set the status to pending in a similar way:

```ocaml
let my_test = Term.pending "Running your test now..."
```

More usefully, the result can depend on the pull request...

## The Git plugin

One very important term is `Git.fetch_head`, which fetches the PR's head commit to a local git repository, ready for testing:

```ocaml
open Datakit_ci
open Term.Infix   (* Provides the >>= operator *)

let local_repo = Git.v ~logs ~dir:"/tmp/example" ~remote:"https://github.com/example/project.git"

let my_test =
  Git.fetch_head local_repo >>= fun local_commit ->
  Term.return "Fetched head commit successfully"
```

The `>>=` operator is used to combine terms.
`x >>= f` first evaluates `x`.
If `x` is a success value then it evaluates to `f x`, otherwise it just reports the current status (pending or error) of `x`.

In this case, we `git fetch` the head commit into the `/tmp/example` repository (which DataKit will clone from `~remote` if it doesn't already exist).
This term will be pending while the `git fetch` is in progress and will then report success.

Use `Git.command` to configure a command to run on the commit (e.g. `make`) and use `Git.run` to execute it, e.g.

```
let one_hour = 60. *. 60.

let make = Git.command ~logs ~label:"make" ~timeout:one_hour ~clone:true [
    [| "make"; "build" |];
    [| "make"; "test" |];
  ]

let my_test =
  Git.fetch_head local_repo >>= fun src ->
  Git.run make src >>= fun () ->
  Term.return "Tests succeeded"
```


## Parallel execution

To evaluate two terms in parallel, use `Term.pair`:

```
let combine a b =
  Printf.sprintf "a=%d and b=%d" a b

let my_test =
  let a = Term.return 1 in
  let b = Term.return 2 in
  Term.pair a b >>= fun (a, b) ->
  Term.return (combine a b)
```

This allows you to run various downloading, building and testing operations in parallel where possible.

## Examples

### SelfCI

[SelfCI][] is the CI we use to test DataKit itself. It builds all of the Dockerfiles in this repository, handling the dependencies between them.

### MirageCI

DataKitCI is used as the basis of the [MirageCI service][], which builds all the packages in the main OCaml repository. Each time a package is submitted, it checks that it builds on multiple distributions and with multiple versions of the OCaml compiler. It also finds all packages that depend on the new one and checks that they still build too. See the [MirageCI source][] for inspiration.


## Extending DataKitCI

Various other terms are available. See the [`src/datakit_ci.mli`][DataKitCI API] file for details.
Other plugins are under development.
To make your own, you need to implement the `BUILDER` interface.
Consult the API documentation and the Git plugin example for more information.


## GitHub login

You can configure the CI to allow users to authenticate using their GitHub accounts using the `Settings` tab.

Once GitHub authentication is configured, you can write policies that depend on GitHub permissions. e.g.

    ~can_read:ACL.(
      any [
        username "admin";
        can_read_github "my-org/my-private-project";
      ]
    )

This will allow read access to the CI if the user is the local "admin" user, or
is a GitHub user who can read the "my-org/my-private-repository" repository.



[DataKit]: https://github.com/moby/datakit
[cmdliner]: http://erratique.ch/software/cmdliner/doc/Cmdliner
[DataKitCI API]: https://docker.github.io/datakit/Datakit_ci.html
[MirageCI service]: https://ci.mirage.io/
[MirageCI source]: https://github.com/avsm/mirage-ci/tree/master/src-bin
[SelfCI]: https://github.com/moby/datakit/blob/master/ci/self-ci/selfCI.ml
The CI configuration for testing DataKit itself, using DataKitCI.
The `docker-compose.yml` file describes a configuration for testing the CI locally with `docker-compose`.
The `datakit-ci.yml` file describes the configuration we use to run <https://datakit.datakit.ci>, managed by `docker stack`.

# Local testing

To test it locally, use:

```
$ docker-compose up
ci_1       | 2017-01-23 14:15.55 APP [datakit-ci] >>> Configure the CI by visiting
ci_1       |                                      http://localhost:8080/auth/intro/...
```

Visit the URL shown to configure an admin user.

In this configuration:

- The bridge that normally syncs the CI state with GitHub is replaced by `datakit/local-bridge`, which tracks the local DataKit Git repository (`../../.git`).
- Only the master branch is tested (`--canary=moby/datakit/heads/master`).
- Plain HTTP connections are used, to avoid browser warnings about self-signed certificates when testing.
- The main executable is called with `--profile=localhost`, which affects some settings in `selfCI.ml` (search for `Localhost` to find the changes).

This mode is useful for testing changes to the CI itself, or for testing your changes before making a public PR.


# Docker Cloud / Swarm Mode configuration

To use this as a template for your own projects:

1. Edit `datakit-ci.yml`.
   - For the `ci` service:
     - Change `--web-ui=https://datakit.datakit.ci/` to the URL users should use to see the web user interface of your service.
   - For the `datakit` service:
     - Edit (or remove) the `--auto-push git@github.com:moby/datakit.logs` option to point at a new, empty, GitHub repository
       which will mirror the results.
   - For the bridge, change `--webhook http://HOST:PORT` to a public endpoint that GitHub can use to send web events.
     If you change the port, change *both* ports in the `ports` configuration below.

2. Edit `selfCI.ml` to specify the tests you require. See the [DataKitCI][] README for details.

3. Add the token that the bridge will use to access GitHub.
   Get a token with `git jar` and add it as a Docker secret with:
   `docker secret create datakit-github-cookie - < ~/.github/jar/datakit-github-cookie`
   See [ocaml-github][]'s README for details.

4. Use `docker stack deploy self-ci -c datakit-ci.yml` to deploy the stack.

5. Check the logs for the `ci` service. You should see a configuration URL displayed near the start.
   Open this in a browser (you'll probably have to click through a security warning, as the server
   generates itself a self-signed X.509 certificate by default).

5. Configure an admin password when prompted, then log in as the new "admin" user.

You will need to add some SSH keys and (optionally) X.509 certificates:

1. Populate the `datakit-ssh` volume with a fresh ssh key (run `ssh-keygen`).
   DataKit can use this to `git push` if you configured `--auto-push` above.
   You'll also need a `known_hosts` file so it can recognise GitHub.
   The easiest way to set this up is to run `git push` manually once.

2. Restore the `datakit-public-data` volume (optional).
   If you are restoring the database from a backup, use `git clone --bare --mirror backup`.

3. Replace the X.509 certificates in the `ci-secrets` volume (optional).
   `server.crt` and `server.key` will be generated on first run if missing.
   They are used for the web UI. You can replace these with a proper certificate and key when you get one (e.g. using [certbot][]).

On startup, the CI should commit to the `datakit-public-data` repository's `github-metadata` branch a request to monitor the projects it is testing.
The `bridge` service should then start populating the branch with information about the branches, tags and open PRs in the repository, and the CI will start testing them.

## Prometheus metrics

All the DataKit services are run with `--listen-prometheus=9090`, which means that they will provide Prometheus metrics on port 9090 at `/metrics`. You can configure a Prometheus server to monitor these ports.

[DataKitCI]: https://github.com/moby/datakit/tree/master/ci/self-ci
[ocaml-github]: https://github.com/mirage/ocaml-github
[certbot]: https://certbot.eff.org/
## DataKit-GitHub bridge

The bridge monitors the state of one or more GitHub projects, writing the status (open PRs, branches and tags) to a DataKit branch.
It also monitors the branch and writes back any changes to GitHub.


### Build

Build using the `Dockerfile.github` file at the root of this repository:

    docker build -t datakit-github -f Dockerfile.github .

### Run

To see the help text:

    docker run -it --rm datakit-github --help

Create a GitHub API token:

    docker run -it --rm \
      -v /path/to/jar:/home/opam/.github/jar \
      --entrypoint opam \
      -u opam \
      datakit-github \
      config exec \
      git jar make my-user datakit

Replace `/path/to/jar` with the path of your new directory.
Replace `my-user` with your GitHub user name.

Using the GitHub web interface, edit the token to give it the `repo`, permission.
Also, ensure the user is an `admin` in the `Collaborators` settings.

Start a DataKit server running somewhere:

    mkdir test-store
    git init test-store/.git --bare
    datakit --git test-store --url tcp://127.0.0.1:6640 -v


To run it:

    docker run -it --rm \
      -v /path/to/jar/datakit:/run/secrets/datakit-github-cookie \
      datakit-github \
      --datakit=tcp:x.x.x.x:6640 \
      --verbose \
      --webhook=http://my-ip

Note: `/path/to/jar/datakit` MUST NOT have any "other" permissions set in its Unix permissions.
Otherwise, the bridge will refuse to start, saying that the file doesn't exist.

Replace:
- `/path/to/jar` with the path of your jar directory.
- `tcp:x.x.x.x:6640` with the path to your DataKit server.
- `http://my-ip` with a URL which GitHub can use to send events to the bridge.

### Start monitoring a repository

Connect to DataKit and create an empty file `repo/project/.monitor` on the `github-metadata` branch.
The bridge will immediately start querying GitHub and will populate the directory with information about the project.
## DataKit Local-Git bridge

This service is a drop-in replacement for the DataKit-GitHub bridge that instead just monitors a local Git repository.
It is useful for testing a new DataKitCI configuration without having to configure GitHub integration first.

The local bridge monitors the state of one or more local Git repositories, writing the current head of each branch to DataKit.
DataKitCI can be configured to run the CI tests against the project each time a commit is made.

Once you are happy with the way the CI is working, you can replace this service with the GitHub bridge service to have the CI test a project hosted on GitHub instead.

Unlike the GitHub bridge, this service:

- only reports on branches, not tags or pull requests;
- does not report build statuses from other CI systems; and
- does not push the statuses set by the CI anywhere.

For an example test configuration using this bridge, see `ci/self-ci/docker-compose.yml`.


### Build

Build using the `Dockerfile.bridge-local-git` file at the root of this repository:

    docker build -t datakit/local-bridge -f Dockerfile.bridge-local-git .

### Run

To see the help text:

    docker run -it --rm datakit/local-bridge --help

To run it (after starting a DataKit container called "datakit"):

    docker run -it --rm \
      --link datakit:datakit \
      -v /path/to/repos:/repos \
      datakit/local-bridge -v \
      me/my-project:/repos/my-project \
      --verbose \
      --webhook=http://my-ip

Replace:
- `/path/to/repos` with the path to your local repository or repositories.
- `me/my-project` (simulating the GitHub `http://github.com/my/my-project` repository) with the ID of your project.
