go-novendor
===========
go-novendor verifies that there are no unused vendored imports in a Go project.

A vendored package is considered unused if the package is not imported by any of the non-vendored code in the project (including test code) either directly or transitively. It should be possible to remove any package that is reported by this tool from vendoring and still have the project build correctly. Standard Go build rules are used to determine if a package is vendored (basically, any package that is within a "vendor" directory is vendored).

Project Packages
----------------
`novendor` has a notion of "project packages". A "project package" is considered to be a top-level package for a single project that may contain many subpackages. Although this is not an official Go concept, it captures much of how code is organized in practice.

This concept is used because in many cases projects want to vendor "project packages" as a unit. For example, consider the packages `github.com/org/project`, `github.com/org/project/api` and `github.com/org/project/impl`. If the primary project code only imports `github.com/org/project/api`, then technically the other 2 packages are "unused". However, a project may still want to vendor `github.com/org/project` and all of its subdirectories because they may want to make use of the other code later or ensure that different subdirectories of a single project are not inadvertently vendored at different versions.

The default behavior of `novendor` works at the "project package" granularity. So, if `github.com/org/project/api` and `github.com/org/project/impl` are both vendored but only `github.com/org/project/api` is used, `github.com/org/project` is considered as "used" and is not reported as an unused project package. If both are unused, the default behavior will report that `github.com/org/project` is unused.

The project package for an import is determined using regular expressions. If an import matches a regular expression, then only the matching portion is used as the project package. By default, the following regular expressions are used:

```
`github\.com/[^/]+/[^/]+`
`golang\.org/[^/]+/[^/]+`
`gopkg\.in/[^/]+`
`github\.[^/]+/[^/]+/[^/]+`
```

Custom regular expression can be specified using a flag.
