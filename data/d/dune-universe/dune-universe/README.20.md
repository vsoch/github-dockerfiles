[![Build stats](https://travis-ci.org/mirage/ocaml-gnt.png?branch=master)](https://travis-ci.org/mirage/ocaml-gnt)

Xen grant table bindings for OCaml.
===================================

These are used to create Xen device driver "backends" (servers)
and "frontends" (clients).

This library can be used in both kernelspace (via Mirage) or in userspace
(on Linux). To see a concrete example, have a look at [mirage/ocaml-vchan]
