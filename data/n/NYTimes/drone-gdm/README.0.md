Utilities
=========
:warning: These are _hacky developer utilities_ used by the maintainers to debug
on the fly!

#### Scripts
 - 0.4-test.bash: 0.4 convention plugin invocation using dummy data
 - 0.8-test.bash: 0.8 convention plugin invocation using dummy data
 - 0.8-extern-cfg-test.bash: 0.8 convention plugin invocation w/ extern config
Code Organization
=================
 * config.go: Plugin configuration object and validation functions
 * parse.go: Plugin environment/json parser
 * run.go: Utility functions to execute gcloud command line utility
 * context.go: Per-deployment/type configuration context
 * gdm.go: GDM business logic + command interface
 * composite.go: GDM "types" (composite) command implementation
 * deployment.go: GDM "deployments" command implementation


