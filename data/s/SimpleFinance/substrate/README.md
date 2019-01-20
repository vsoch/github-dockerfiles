# Substrate

This is an opinionated tool for managing Kubernetes clusters. It is no longer under active development at Simple, but we're sharing it as-is. It should probably not be used directly. See [@asynchio's giant spreadsheet](https://docs.google.com/spreadsheets/d/1LxSqBzjOxfGx3cmtZ4EbB_BGCxT_wlxW_xgHVVa23es/edit#gid=0) for some alternatives.

For more information, see the `./docs` directory:

 - [`docs/developing.md`](docs/developing.md) describes the basics of hacking on Substrate.

 - [`docs/design.md`](docs/design.md) documents the overall design and terminology.

 - [`docs/mechanics.md`](docs/mechanics.md) describes how the bootstrap process works to create a zone.

## Versioning

 - Substrate uses [SemVer](http://semver.org/).
 - Major versions live in long-lived branches named like `v1.x`, `v2.x`, etc...
 - We may maintain more than one major version of Substrate. This allows us to
   make major backwards-incompatible changes while still shipping bug fixes to
   older versions. For example, versions `v1.0.1` and `v2.0.1` might be
   released at the same time to fix the same bug across multiple major
   versions.
