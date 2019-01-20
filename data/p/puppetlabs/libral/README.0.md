- mount_fstab.aug
- tests/test_mount_fstab.aug

Forks of augeas/lenses/fstab.aug, augeas/lenses/tests/test_fstab.aug from
commit c887c7cc630eb359dc900a32ffa8517bc80ea356.
Files to help with running builds inside Docker containers. They can all be
built with `make NAME`.

Make targets that end in `-build` create containers that will build libral
automatically when they are run. They have the necessary tooling to do that
in them, but libral sources will be downloaded every time they are run.

Make targets that are just a distro nmae like `f25` will create a container
image that has a prebuilt libral in them and can be used for trying it out.
# Libral

This directory contains the CRuby bindings for using libral, and builds the
libral CRuby gem. This gem is needed for provider development, especially
to run tests, but is not needed to actually run libral; unless, of course,
running libral entails talking to it from CRuby code.

The gem should be built with the larger CMake setup of libral. The native
code for the extension will be built by a simple 'make', which eventually
invokes the `ruby_compile` target for this directory. To produce a
packaged gem, you need to explicitly run `make ruby_gem`.

The easiest way to try this gem out when you are building from source is to
run `./bin/dev irb -rlibral` in your build directory.
MRuby extensions that are very specific to libral
