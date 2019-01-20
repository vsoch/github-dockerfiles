## koki control

Command-line admin interface, in-cluster controller, and per-pod sidecar.

### Intended use

Deploy and manage koki applications in a Kubernetes cluster.

### Current functionality/architecture

Create a dummy koki application from a single Pod.
* The Pod is deployed with an additional container--the koki sidecar container.
* A koki application ConfigMap is created to track application state.
* The koki controller manages the application described in the ConfigMap,
  using the koki sidecar to perform tasks in the Pod.

### Pre-use setup

The koki controller uses the ServiceAccount koki.
For OpenShift clusters, create a new user `system:serviceaccount:{PROJECT_NAME a.k.a. namespace}:koki`
Then give that user `edit` permissions:

  `oc add-role-to-user edit system:serviceaccount:some-project:koki`

  `oc policy add-role-to-user edit system:serviceaccount:some-project:koki`

### Development

Dependencies are managed with `dep`. After `import`ing a new library, run `dep ensure` to add it to the `vendor` folder.

Build and publish the controller and sidecar containers using `scripts/build-*.sh` and `scripts/push-*.sh`. To push to your own container repository, set your env as illustrated in `artifacts/example-koki-profile`.

To build the CLI, use `scripts/build-cli.sh` (Docker) or `scripts/install-cli.sh` (local). The CLI uses `cobra`, so just run the `cli` executable to see what its commands are.

The code is organized like this:

* `cli/` is the CLI
* `controller/` is the controller
* `sidecar/` is the sidecar
* `pkg/` contains the shared code
