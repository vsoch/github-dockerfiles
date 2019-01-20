# alpine-phantomjs-builder

This is meant to build a phantomjs package that can be used in alpine docker images.  It's **NOT** meant to be a usable docker image after the build is complete, and simply outputs the phantomjs tarball.

Please don't push the built image up to any docker image repos.  It's not suitable for running services, containers, etc.

This should be broken out into a repo of its own, but since it doesn't work yet... that step was skipped.

Current status as of May 22nd, 2017: Need to figure out why the phantomjs binary built by this image hangs in alpine.  A couple of patches were introduced to integrate this phantomjs more closely with alpine, (build-deps, and build-nonstatic) but neither one fixed the hanging problem.
