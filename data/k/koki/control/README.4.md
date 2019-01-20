## simple but flexible parameterization of JSON and YAML documents

`scripts/build` and `scripts/test` to build and to test.

### what it does

`templates` takes a set of `name, value` pairs (the "parameters") from one JSON/YAML document and replaces `${name}` with `value` in another JSON/YAML document (the "template"). For example template and parameter files, see the `yamls` and `jsons` folders and the `[json|yaml]/replace_test.go` files.

Note that `value` can itself be a structured JSON/YAML object, not just a scalar like string or number.

For development, you may use `go install` and then `templates` to run the executable.
This project uses `cobra`, so running `templates` in the command line will present more specific usage instructions.
