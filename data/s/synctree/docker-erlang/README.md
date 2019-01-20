# synctree/erlang

The `synctree/erlang` image is intended for use as a base image for Erlang/OTP applications. This Debian-based image uses the packages from [Erlang Solutions Limited](https://www.erlang-solutions.com/).

## Available Variants
There are versions of this image for Erlang/OTP R15, R16, and R17. Additionally, the R16 and R17 versions have a `slim` variant that installs only `erlang-base` and `erlang-crypto` as opposed to installing the `erlang` package and all its dependencies.

| Tag        | Base             | Packages                         |
|------------|------------------|----------------------------------|
| R15        | `debian:squeeze` | `esl-erlang`                     |
| R16        | `debian:wheezy`  | `erlang`                         |
| R16-slim   | `debian:wheezy`  | `erlang-base`<br>`erlang-crypto` |
| R17        | `debian:jessie`  | `erlang`                         |
| R17-slim   | `debian:jessie`  | `erlang-base`<br>`erlang-crypto` |
| R17-trusty | `ubuntu:trusty`  | `erlang`                         |
| R17-utopic | `ubuntu:utopic`  | `erlang`                         |
