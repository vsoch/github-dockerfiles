scripts
=======

This directory contains the following scripts.

- [check-ci][] - Checks that requirements for license headers, code formatting,
  and code linting have been met before changes should be merged
- [check-license][] - Prints a list of sources missing the license header
- [check-linters][] - Runs ShellCheck across scripts to lint them
- [deploy-docs][] - Deploys HTML documentation to GitHub pages
- [format-code][] - Formats Open Enclave C/C++ code using `clang-format`
- [install-open-enclave-stack][] - This is pending deprecation
- [install-prereqs][] - Installs packages needed to build Open Enclave
- [pre-commit][] - A [Git pre-commit hook](https://git-scm.com/docs/githooks)
  for developers
- [test-build-config][] - This will be deprecated by writing the configuration
  into the `Jenkinsfile`
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

Add Jenkins slave
=========

This role will install needed Jenkins students (slaves) for both linux and windows. That includes all the needed requirements for openenclave.

Requirements
------------

All the python requirements are in the requirements.txt and can be installed with:

```
pip3 install -r requierements.txt
```

Ansible >=2.7

Ubuntu 16.04 targets (should work with 18.04 also, but not tested)

Create the node on Jenkins master

Add the external role:

```
ansible-galaxy install kobanyan.jenkins-jnlp-slave

```

Add the IPADDRESS in the hosts file from the repository.

Role Variables
--------------

The bellow variables need to be changed in var/variables.var for the playbook to execute succesfully

jenkins_master: "JENKINS_MASTER_URL"
jenkins_slave_secret: "SECRET" #The secret must be taken from when the node is created


Dependencies
------------

https://galaxy.ansible.com/kobanyan/jenkins-jnlp-slave 

Example running
----------------
```
ansible-playbook -i hosts deploy_jenkins.yml -u **USER**
```
debugger
====

This directory contains the sources for the sgx_ptrace library and Python 
extension. The oe_ptrace library implements the customized ptrace function 
to debug sgx enclave. The Python extension is a GDB extension to enable 
enclave debugging and stack stitching etc.
pythonExtension
====

This directory contains the sources for the GDB python extension. That 
extension is used to load enclave symbol, enable enclave debugging, and 
stitch stacks etc. 

It will be loaded into gdb as a plugin. Please refer to 
https://sourceware.org/gdb/onlinedocs/gdb/Extending-GDB.html for GDB 
python extension model.
ptraceLib
====

This directory contains the sources for the oe_ptrace library. The oe_ptrace 
library implements the customized ptrace and waitpid function to get and set 
enclave registers, and fix the enclave breakpoint.

It will be preloaded into the GDB by oe-gdb script. 
3rdparty
========

This directory contains third-party software used in Open Enclave. It contains
the following directories:

- [dlmalloc](dlmalloc) - Dynamic memory allocator (used in oelibc)

- [musl](musl) - Standard C library implementation (used in oelibc)

- [libcxx](libcxx) - Standard C++ library (used in oelibcxx)

- [libcxxrt](libcxxrt) - C++ runtime support library (used in oelibcxx)

- [libunwind](libunwind) - C++ exception unwinding library (used in oelibcxx)

- [mbedtls](mbedtls) - Crypto library

- [openssl](openssl) - Crypto library
This README lists the set of changes made to the libcxxrt library.
When upgrading the library, make sure to preserve the following changes.

1. exception.cc: Use oe_thread_data_t's __cxx_thread_info instead of
    calloc-ing it on demand. This prevents crashes when an std::bad_alloc
	is thrown.
libcxxabi
=========

This library implements the Code Sourcery C++ ABI, as documented here:

http://www.codesourcery.com/public/cxx-abi/abi.html

It is intended to sit below an STL implementation, and provide features required by the compiler for implementation of the C++ language.

Current Status
--------------

At present, the library implements the following parts of the ABI specification:

- RTTI classes and support for the dynamic_cast<> operator.
- Exception handling.
- Thread-safe initializers.

Exception handling requires the assistance of a stack-unwinding library
implementing the low-level parts of the ABI.  Either libgcc_s or libunwind
should work for this purpose.

The library depends on various libc features, but does not depend on any C++
features not implemented purely in the compiler or in the library itself.

Supported Platforms
-------------------

This code was initially developed on FreeBSD/x86, and has also been tested on FreeBSD/x86-64.  It should work on other platforms that use the Code Sourcery ABI, for example Itanium, however this is untested.

This library also supports the ARM EH ABI.

Installation
------------

The default build system does not perform any installation.  It is expected that this will be done by at a higher level.  The exact installation steps depend on how you plan on deploying libcxxrt.

There are three files that you may consider installing:

- cxxabi.h (and unwind.h and either unwind-arm.h or unwind-itanium.h)
- libcxxrt.a
- libcxxrt.so

The first describes the contract between this library and the compiler / STL implementation (lib[std]{cxx,c++}).  Its contents should be considered semi-private, as it is probably not a good idea to encourage any code above the STL implementation to depend on it.  Doing so will introduce portability issues.  You may install this file but I recommend simply copying or linking it into your STL implementation's build directory.

In general, I recommend against installing both the .a and the .so file.  For static linking, the .a file should be linked against the static and dynamic versions of your STL implementation.  Statically linking libcxxrt into your STL implementation means that users who dynamically link against the STL implementation can have libcxxrt upgraded automatically when you ship a new version of your STL implementation.

The other option, installing the .so, is recommended for situations where you have two or more STL implementations and wish to be able to link against both (e.g. where an application links one library using libstdc++ and another using libc++).  To support this case, you should link both STL implementations against libcxxrt.so.  

Supporting all of these options in the CMake build system is not practical - the amount of effort required to select the one that you want would be more than the effort required to perform the installation from an external script or build system.
libunwind
=========

This directory contains a port of **libunwind** for enclaves. No **libunwind**
sources were changed. The **./libunwind** directory was copied intact from the 
following location.

```
https://github.com/pathscale/libunwind
```

The general porting approach is described as follows.

- Stub out functions unsupported for enclaves (see [stubs.h](stubs.h))

- Wrap **unw_step()** to verify that the cursor falls within enclave memory
  (see [libunwind-common.h](libunwind-common.h) and [Gstep.c](Gstep.c)).

- Provide a definition of **_Ux86_64_setcontext** that does not perform a
  system call (see [setcontext.S](setcontext.S))

This port also works with the newer libunwind version 1.3.

```
https://github.com/libunwind/libunwind
```
-*- mode: Outline -*-

This is version 1.0 of the unwind library.  This library supports
several architecture/operating-system combinations:

 Linux/x86-64:	Works well.
 Linux/x86:	Works well.
 Linux/ARM:	Works well.
 Linux/IA-64:	Fully tested and supported.
 Linux/PARISC:	Works well, but C library missing unwind-info.
 HP-UX/IA-64:	Mostly works but known to have some serious limitations.
 Linux/AArch64:	Newly added.
 Linux/PPC64:	Newly added.
 Linux/SuperH:	Newly added.
 FreeBSD/i386:	Newly added.
 FreeBSD/x86-64: Newly added (FreeBSD architecture is known as amd64).
 Linux/Tilegx:  Newly added (64-bit mode only).

* General Build Instructions

In general, this library can be built and installed with the following
commands:

	$ ./autogen.sh # Needed only for building from git. Depends on libtool.
	$ ./configure
	$ make
	$ make install prefix=PREFIX

where PREFIX is the installation prefix.  By default, a prefix of
/usr/local is used, such that libunwind.a is installed in
/usr/local/lib and unwind.h is installed in /usr/local/include.  For
testing, you may want to use a prefix of /usr/local instead.


* Building with Intel compiler

** Version 8 and later

Starting with version 8, the preferred name for the IA-64 Intel
compiler is "icc" (same name as on x86).  Thus, the configure-line
should look like this:

    $ ./configure CC=icc CFLAGS="-g -O3 -ip" CXX=icc CCAS=gcc CCASFLAGS=-g \
		LDFLAGS="-L$PWD/src/.libs"


* Building on HP-UX

For the time being, libunwind must be built with GCC on HP-UX.

libunwind should be configured and installed on HP-UX like this:

    $ ./configure CFLAGS="-g -O2 -mlp64" CXXFLAGS="-g -O2 -mlp64"

Caveat: Unwinding of 32-bit (ILP32) binaries is not supported
	at the moment.

** Workaround for older versions of GCC

GCC v3.0 and GCC v3.2 ship with a bad version of sys/types.h.  The
workaround is to issue the following commands before running
"configure":

    $ mkdir $top_dir/include/sys
    $ cp /usr/include/sys/types.h $top_dir/include/sys

GCC v3.3.2 or later have been fixed and do not require this
workaround.

* Building for PowerPC64 / Linux

For building for power64 you should use:

  $ ./configure CFLAGS="-g -O2 -m64" CXXFLAGS="-g -O2 -m64"

If your power support altivec registers:
  $ ./configure CFLAGS="-g -O2 -m64 -maltivec" CXXFLAGS="-g -O2 -m64 -maltivec"

To check if your processor has support for vector registers (altivec):
    cat /proc/cpuinfo | grep altivec
and should have something like this:
    cpu             : PPC970, altivec supported

If libunwind seems to not work (backtracing failing), try to compile
it with -O0, without optimizations. There are some compiler problems
depending on the version of your gcc.

* Building on FreeBSD

General building instructions apply. To build and execute several tests,
you need libexecinfo library available in ports as devel/libexecinfo.

Development of the port was done of FreeBSD 8.0-STABLE. The library
was build with the system compiler that is modified version of gcc 4.2.1,
as well as the gcc 4.4.3.

* Regression Testing

After building the library, you can run a set of regression tests with:

	$ make check

** Expected results on IA-64 Linux

Unless you have a very recent C library and compiler installed, it is
currently expected to have the following tests fail on IA-64 Linux:

	Gtest-init		(should pass starting with glibc-2.3.x/gcc-3.4)
	Ltest-init		(should pass starting with glibc-2.3.x/gcc-3.4)
	test-ptrace		(should pass starting with glibc-2.3.x/gcc-3.4)
	run-ia64-test-dyn1	(should pass starting with glibc-2.3.x)

This does not mean that libunwind cannot be used with older compilers
or C libraries, it just means that for certain corner cases, unwinding
will fail.  Since they're corner cases, it is not likely for
applications to trigger them.

Note: If you get lots of errors in Gia64-test-nat and Lia64-test-nat, it's
      almost certainly a sign of an old assembler.  The GNU assembler used
      to encode previous-stack-pointer-relative offsets incorrectly.
      This bug was fixed on 21-Sep-2004 so any later assembler will be
      fine.

** Expected results on x86 Linux

The following tests are expected to fail on x86 Linux:

	Gtest-resume-sig	(fails to get SIGUSR2)
	Ltest-resume-sig	(likewise)
	Gtest-dyn1		(no dynamic unwind info support yet)
	Ltest-dyn1		(no dynamic unwind info support yet)
	test-setjmp		(longjmp() not implemented yet)
	run-check-namespace	(no _Ux86_getcontext yet)
	test-ptrace

** Expected results on x86-64 Linux

The following tests are expected to fail on x86-64 Linux:

	Gtest-dyn1		(no dynamic unwind info support yet)
	Ltest-dyn1		(no dynamic unwind info support yet)
	Gtest-init (see http://gcc.gnu.org/bugzilla/show_bug.cgi?id=18743)
	Ltest-init		(likewise)
	test-async-sig		(crashes due to bad unwind-info?)
	test-setjmp		(longjmp() not implemented yet)
	run-check-namespace	(no _Ux86_64_getcontext yet)
	run-ptrace-mapper	(??? investigate)
	run-ptrace-misc	(see http://gcc.gnu.org/bugzilla/show_bug.cgi?id=18748
			 and http://gcc.gnu.org/bugzilla/show_bug.cgi?id=18749)

** Expected results on PARISC Linux

Caveat: GCC v3.4 or newer is needed on PA-RISC Linux.  Earlier
versions of the compiler failed to generate the exception-handling
program header (GNU_EH_FRAME) needed for unwinding.

The following tests are expected to fail on x86-64 Linux:

	Gtest-bt   (backtrace truncated at kill() due to lack of unwind-info)
	Ltest-bt   (likewise)
	Gtest-resume-sig  (Gresume.c:my_rt_sigreturn() is wrong somehow)
	Ltest-resume-sig  (likewise)
	Gtest-init (likewise)
	Ltest-init (likewise)
	Gtest-dyn1 (no dynamic unwind info support yet)
	Ltest-dyn1 (no dynamic unwind info support yet)
	test-setjmp		(longjmp() not implemented yet)
	run-check-namespace	(toolchain doesn't support HIDDEN yet)

** Expected results on HP-UX

"make check" is currently unsupported for HP-UX.  You can try to run
it, but most tests will fail (and some may fail to terminate).  The
only test programs that are known to work at this time are:

     tests/bt
     tests/Gperf-simple
     tests/test-proc-info
     tests/test-static-link
     tests/Gtest-init
     tests/Ltest-init
     tests/Gtest-resume-sig
     tests/Ltest-resume-sig

** Expected results on PPC64 Linux

"make check" should run with no more than 10 out of 24 tests failed.


* Performance Testing

This distribution includes a few simple performance tests which give
some idea of the basic cost of various libunwind operations.  After
building the library, you can run these tests with the following
commands:

 $ cd tests
 $ make perf

* Contacting the Developers

Please direct all questions regarding this library to:

	libunwind-devel@nongnu.org

You can do this by sending a mail to libunwind-request@nongnu.org with
a body of:

	subscribe libunwind-devel

or you can subscribe and manage your subscription via the
web-interface at:

	https://savannah.nongnu.org/mail/?group=libunwind
This code is based on "unwinding via ptrace" code from ptrace/
directory.

Files with names starting with _UCD_ are substantially changed
from their ptrace/_UPT_... progenitors.

Files which still have _UPT_... names are either verbiatim copies
from ptrace/, or unimplemented stubs.
README for Mbed TLS
===================

Configuration
-------------

Mbed TLS should build out of the box on most systems. Some platform specific options are available in the fully documented configuration file `include/mbedtls/config.h`, which is also the place where features can be selected. This file can be edited manually, or in a more programmatic way using the Perl script `scripts/config.pl` (use `--help` for usage instructions).

Compiler options can be set using conventional environment variables such as `CC` and `CFLAGS` when using the Make and CMake build system (see below).

Compiling
---------

There are currently four active build systems used within Mbed TLS releases:

-   yotta
-   GNU Make
-   CMake
-   Microsoft Visual Studio (Microsoft Visual Studio 2010 or later)

The main systems used for development are CMake and GNU Make. Those systems are always complete and up-to-date. The others should reflect all changes present in the CMake and Make build system, although features may not be ported there automatically.

Yotta, as a build system, is slightly different from the other build systems:

-   it provides a minimalistic configuration file by default
-   depending on the yotta target, features of Mbed OS may be used in examples and tests

The Make and CMake build systems create three libraries: libmbedcrypto, libmbedx509, and libmbedtls. Note that libmbedtls depends on libmbedx509 and libmbedcrypto, and libmbedx509 depends on libmbedcrypto. As a result, some linkers will expect flags to be in a specific order, for example the GNU linker wants `-lmbedtls -lmbedx509 -lmbedcrypto`. Also, when loading shared libraries using dlopen(), you'll need to load libmbedcrypto first, then libmbedx509, before you can load libmbedtls.

### Yotta

[yotta](http://yottabuild.org) is a package manager and build system developed by Mbed, and is the build system of Mbed OS 16.03. To install it on your platform, please follow the yotta [installation instructions](http://docs.yottabuild.org/#installing).

Once yotta is installed, you can use it to download the latest version of Mbed TLS from the yotta registry with:

    yotta install mbedtls

and build it with:

    yotta build

If, on the other hand, you already have a copy of Mbed TLS from a source other than the yotta registry, for example from cloning our GitHub repository, or from downloading a tarball of the standalone edition, then you'll first need to generate the yotta module by running:

    yotta/create-module.sh

This should be executed from the root Mbed TLS project directory. This will create the yotta module in the `yotta/module` directory within it. You can then change to that directory and build as usual:

    cd yotta/module
    yotta build

In any case, you'll probably want to set the yotta target before building unless it has already been set globally. For more information on using yotta, please consult the [yotta documentation](http://docs.yottabuild.org/).

For more details on the yotta/Mbed OS edition of Mbed TLS, including example programs, please consult the [Readme at the root of the yotta module](https://github.com/ARMmbed/mbedtls/blob/development/yotta/data/README.md).

### Make

We require GNU Make. To build the library and the sample programs, GNU Make and a C compiler are sufficient. Some of the more advanced build targets require some Unix/Linux tools.

We intentionally only use a minimum of functionality in the makefiles in order to keep them as simple and independent of different toolchains as possible, to allow users to more easily move between different platforms. Users who need more features are recommended to use CMake.

In order to build from the source code using GNU Make, just enter at the command line:

    make

In order to run the tests, enter:

    make check

The tests need Perl to be built and run. If you don't have Perl installed, you can skip building the tests with:

    make no_test

You'll still be able to run a much smaller set of tests with:

    programs/test/selftest

In order to build for a Windows platform, you should use `WINDOWS_BUILD=1` if the target is Windows but the build environment is Unix-like (for instance when cross-compiling, or compiling from an MSYS shell), and `WINDOWS=1` if the build environment is a Windows shell (for instance using mingw32-make) (in that case some targets will not be available).

Setting the variable `SHARED` in your environment will build shared libraries in addition to the static libraries. Setting `DEBUG` gives you a debug build. You can override `CFLAGS` and `LDFLAGS` by setting them in your environment or on the make command line; compiler warning options may be overridden separately using `WARNING_CFLAGS`. Some directory-specific options (for example, `-I` directives) are still preserved.

Please note that setting `CFLAGS` overrides its default value of `-O2` and setting `WARNING_CFLAGS` overrides its default value (starting with `-Wall -W`), so it you just want to add some warning options to the default ones, you can do so by setting `CFLAGS=-O2 -Werror` for example. Setting `WARNING_CFLAGS` is useful when you want to get rid of its default content (for example because your compiler doesn't accept `-Wall` as an option). Directory-specific options cannot be overriden from the command line.

Depending on your platform, you might run into some issues. Please check the Makefiles in `library/`, `programs/` and `tests/` for options to manually add or remove for specific platforms. You can also check [the Mbed TLS Knowledge Base](https://tls.mbed.org/kb) for articles on your platform or issue.

In case you find that you need to do something else as well, please let us know what, so we can add it to the [Mbed TLS knowledge base](https://tls.mbed.org/kb).

### CMake

In order to build the source using CMake in a separate directory (recommended), just enter at the command line:

    mkdir /path/to/build_dir && cd /path/to/build_dir
    cmake /path/to/mbedtls_source
    make

In order to run the tests, enter:

    make test

The test suites need Perl to be built. If you don't have Perl installed, you'll want to disable the test suites with:

    cmake -DENABLE_TESTING=Off /path/to/mbedtls_source

If you disabled the test suites, but kept the programs enabled, you can still run a much smaller set of tests with:

    programs/test/selftest

To configure CMake for building shared libraries, use:

    cmake -DUSE_SHARED_MBEDTLS_LIBRARY=On /path/to/mbedtls_source

There are many different build modes available within the CMake buildsystem. Most of them are available for gcc and clang, though some are compiler-specific:

-   `Release`. This generates the default code without any unnecessary information in the binary files.
-   `Debug`. This generates debug information and disables optimization of the code.
-   `Coverage`. This generates code coverage information in addition to debug information.
-   `ASan`. This instruments the code with AddressSanitizer to check for memory errors. (This includes LeakSanitizer, with recent version of gcc and clang.) (With recent version of clang, this mode also instruments the code with UndefinedSanitizer to check for undefined behaviour.)
-   `ASanDbg`. Same as ASan but slower, with debug information and better stack traces.
-   `MemSan`. This instruments the code with MemorySanitizer to check for uninitialised memory reads. Experimental, needs recent clang on Linux/x86\_64.
-   `MemSanDbg`. Same as MemSan but slower, with debug information, better stack traces and origin tracking.
-   `Check`. This activates the compiler warnings that depend on optimization and treats all warnings as errors.

Switching build modes in CMake is simple. For debug mode, enter at the command line:

    cmake -D CMAKE_BUILD_TYPE=Debug /path/to/mbedtls_source

To list other available CMake options, use:

    cmake -LH

Note that, with CMake, you can't adjust the compiler or its flags after the
initial invocation of cmake. This means that `CC=your_cc make` and `make
CC=your_cc` will *not* work (similarly with `CFLAGS` and other variables).
These variables need to be adjusted when invoking cmake for the first time,
for example:

    CC=your_cc cmake /path/to/mbedtls_source

If you already invoked cmake and want to change those settings, you need to
remove the build directory and create it again.

Note that it is possible to build in-place; this will however overwrite the
provided Makefiles (see `scripts/tmp_ignore_makefiles.sh` if you want to
prevent `git status` from showing them as modified). In order to do so, from
the Mbed TLS source directory, use:

    cmake .
    make

If you want to change `CC` or `CFLAGS` afterwards, you will need to remove the
CMake cache. This can be done with the following command using GNU find:

    find . -iname '*cmake*' -not -name CMakeLists.txt -exec rm -rf {} +

You can now make the desired change:

    CC=your_cc cmake .
    make

Regarding variables, also note that if you set CFLAGS when invoking cmake,
your value of CFLAGS doesn't override the content provided by cmake (depending
on the build mode as seen above), it's merely prepended to it.

### Microsoft Visual Studio

The build files for Microsoft Visual Studio are generated for Visual Studio 2010.

The solution file `mbedTLS.sln` contains all the basic projects needed to build the library and all the programs. The files in tests are not generated and compiled, as these need a perl environment as well. However, the selftest program in `programs/test/` is still available.

Example programs
----------------

We've included example programs for a lot of different features and uses in `programs/`. Most programs only focus on a single feature or usage scenario, so keep that in mind when copying parts of the code.

Tests
-----

Mbed TLS includes an elaborate test suite in `tests/` that initially requires Perl to generate the tests files (e.g. `test\_suite\_mpi.c`). These files are generated from a `function file` (e.g. `suites/test\_suite\_mpi.function`) and a `data file` (e.g. `suites/test\_suite\_mpi.data`). The `function file` contains the test functions. The `data file` contains the test cases, specified as parameters that will be passed to the test function.

For machines with a Unix shell and OpenSSL (and optionally GnuTLS) installed, additional test scripts are available:

-   `tests/ssl-opt.sh` runs integration tests for various TLS options (renegotiation, resumption, etc.) and tests interoperability of these options with other implementations.
-   `tests/compat.sh` tests interoperability of every ciphersuite with other implementations.
-   `tests/scripts/test-ref-configs.pl` test builds in various reduced configurations.
-   `tests/scripts/key-exchanges.pl` test builds in configurations with a single key exchange enabled
-   `tests/scripts/all.sh` runs a combination of the above tests, plus some more, with various build options (such as ASan, full `config.h`, etc).

Configurations
--------------

We provide some non-standard configurations focused on specific use cases in the `configs/` directory. You can read more about those in `configs/README.txt`

Porting Mbed TLS
----------------

Mbed TLS can be ported to many different architectures, OS's and platforms. Before starting a port, you may find the following knowledge base articles useful:

-   [Porting Mbed TLS to a new environment or OS](https://tls.mbed.org/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS)
-   [What external dependencies does Mbed TLS rely on?](https://tls.mbed.org/kb/development/what-external-dependencies-does-mbedtls-rely-on)
-   [How do I configure Mbed TLS](https://tls.mbed.org/kb/compiling-and-building/how-do-i-configure-mbedtls)

Contributing
------------

We gratefully accept bug reports and contributions from the community. There are some requirements we need to fulfill in order to be able to integrate contributions:

-   All contributions, whether large or small require a Contributor's License Agreement (CLA) to be accepted. This is because source code can possibly fall under copyright law and we need your consent to share in the ownership of the copyright.
-   We would ask that contributions conform to [our coding standards](https://tls.mbed.org/kb/development/mbedtls-coding-standards), and that contributions should be fully tested before submission.
-   As with any open source project, contributions will be reviewed by the project team and community and may need some modifications to be accepted.

To accept the Contributor’s Licence Agreement (CLA), individual contributors can do this by creating an Mbed account and [accepting the online agreement here with a click through](https://os.mbed.com/contributor_agreement/). Alternatively, for contributions from corporations, or those that do not wish to create an Mbed account, a slightly different agreement can be found [here](https://www.mbed.com/en/about-mbed/contributor-license-agreements/). This agreement should be signed and returned to Arm as described in the instructions given.

### Making a Contribution

1.  [Check for open issues](https://github.com/ARMmbed/mbedtls/issues) or [start a discussion](https://forums.mbed.com/c/mbed-tls) around a feature idea or a bug.
2.  Fork the [Mbed TLS repository on GitHub](https://github.com/ARMmbed/mbedtls) to start making your changes. As a general rule, you should use the "development" branch as a basis.
3.  Write a test which shows that the bug was fixed or that the feature works as expected.
4.  Send a pull request and bug us until it gets merged and published. Contributions may need some modifications, so work with us to get your change accepted. We will include your name in the ChangeLog :)

This directory contains example configuration files.

The examples are generally focused on a particular usage case (eg, support for
a restricted number of ciphersuites) and aim at minimizing resource usage for
this target. They can be used as a basis for custom configurations.

These files are complete replacements for the default config.h. To use one of
them, you can pick one of the following methods:

1. Replace the default file include/mbedtls/config.h with the chosen one.
   (Depending on your compiler, you may need to adjust the line with
   #include "mbedtls/check_config.h" then.)

2. Define MBEDTLS_CONFIG_FILE and adjust the include path accordingly.
   For example, using make:

    CFLAGS="-I$PWD/configs -DMBEDTLS_CONFIG_FILE='<foo.h>'" make

   Or, using cmake:

    find . -iname '*cmake*' -not -name CMakeLists.txt -exec rm -rf {} +
    CFLAGS="-I$PWD/configs -DMBEDTLS_CONFIG_FILE='<foo.h>'" cmake .
    make

Note that the second method also works if you want to keep your custom
configuration file outside the mbed TLS tree.
README for git hooks script
===========================
git has a way to run scripts, which are invoked by specific git commands.
The git hooks are located in `<mbed TLS root>/.git/hooks`, and as such are not under version control
for more information, see the [git documentation](https://git-scm.com/docs/githooks).

The mbed TLS git hooks are located in `<mbed TLS root>/tests/git-scripts` directory, and one must create a soft link from `<mbed TLS root>/.git/hooks` to `<mbed TLS root>/tesst/git-scripts`, in order to make the hook scripts successfully work.

Example:

Execute the following command to create a link on linux from the mbed TLS `.git/hooks` directory:  
`ln -s ../../tests/git-scripts/pre-push.sh pre-push`

**Note: Currently the mbed TLS git hooks work only on a GNU platform. If using a non-GNU platform, don't enable these hooks!**

These scripts can also be used independently.
# mbed TLS

mbed TLS makes it trivially easy for developers to include cryptographic and SSL/TLS capabilities in their embedded products, with a minimal code footprint. It offers an SSL library with an intuitive API and readable source code.

**Note:** The current release is beta, and implements no secure source of random numbers, weakening its security.

Currently the only supported yotta targets are:
- `frdm-k64f-gcc`
- `frdm-k64f-armcc`
- `x86-linux-native`
- `x86-osx-native`

## Sample programs

This release includes the following examples:

1. [**Self test:**](https://github.com/ARMmbed/mbedtls/blob/development/yotta/data/example-selftest) Tests different basic functions in the mbed TLS library.

2. [**Benchmark:**](https://github.com/ARMmbed/mbedtls/blob/development/yotta/data/example-benchmark) Measures the time taken to perform basic cryptographic functions used in the library.

3. [**Hashing:**](https://github.com/ARMmbed/mbedtls/blob/development/yotta/data/example-hashing) Demonstrates the various APIs for computing hashes of data (also known as message digests) with SHA-256.

4. [**Authenticated encryption:**](https://github.com/ARMmbed/mbedtls/blob/development/yotta/data/example-authcrypt) Demonstrates usage of the Cipher API for encrypting and authenticating data with AES-CCM.

These examples are integrated as yotta tests, so that they are built automatically when you build mbed TLS. Each of them comes with complete usage instructions as a Readme file in the repository.

## Performing TLS and DTLS connections

A high-level API for performing TLS and DTLS connections with mbed TLS in mbed OS is provided in a separate yotta module: [mbed-tls-sockets](https://github.com/ARMmbed/mbed-tls-sockets). We recommend this API for TLS and DTLS connections. It is very similar to the API provided by the [sockets](https://github.com/ARMmbed/sockets) module for unencrypted TCP and UDP connections.

The `mbed-tls-sockets` module includes a complete [example TLS client](https://github.com/ARMmbed/mbed-tls-sockets/blob/master/test/tls-client/main.cpp) with [usage instructions](https://github.com/ARMmbed/mbed-tls-sockets/blob/master/test/tls-client/README.md).

## Configuring mbed TLS features

mbed TLS makes it easy to disable any feature during compilation, if that feature isn't required for a particular project. The default configuration enables all modern and widely-used features, which should meet the needs of new projects, and disables all features that are older or less common, to minimize the code footprint.

The list of available compilation flags is available in the fully documented [config.h file](https://github.com/ARMmbed/mbedtls/blob/development/include/mbedtls/config.h).

If you need to adjust those flags, you can provide your own configuration-adjustment file with suitable `#define` and `#undef` statements. These will be included between the default definitions and the sanity checks. Your configuration file should be in your application's include directory, and can be named freely; you just need to let mbed TLS know the file's name. To do that, use yotta's [configuration system](http://docs.yottabuild.org/reference/config.html). The file's name should be in your `config.json` file, under mbedtls, as the key `user-config-file`.

For example, in an application called `myapp`, if you want to enable the EC J-PAKE key exchange and disable the CBC cipher mode, you can create a file named  `mbedtls-config-changes.h` in the `myapp` directory containing the following lines:

    #define MBEDTLS_ECJPAKE_C
    #define MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED

    #undef MBEDTLS_CIPHER_MODE_CBC

And then create a file named `config.json` at the root of your application with the following contents:

    {
       "mbedtls": {
          "user-config-file": "\"myapp/mbedtls-config-changes.h\""
       }
    }

Please note: you need to provide the exact name that will be used in the `#include` directive, including the `<>` or quotes around the name.

## Getting mbed TLS from GitHub

Like most components of mbed OS, mbed TLS is developed in the open and its source can be found on GitHub: [ARMmbed/mbedtls](https://github.com/ARMmbed/mbedtls). Unlike most other mbed OS components, however, you cannot just clone the repository and run `yotta build` from its root. This is because mbed TLS also exists as an independent component, so its repository includes things that are not relevant for mbed OS, as well as other build systems.

The way to use mbed TLS from a clone of the GitHub repository is to run the following commands from the root of a checkout:

    yotta/create-module.sh
    cd yotta/module

You can then run any yotta command you would normally run, such as `yotta build` or `yotta link`.

## Differences between the standalone and mbed OS editions

While the two editions share the same code base, there are still a number of differences, mainly in configuration and integration. You should keep in mind those differences when reading some articles in our [knowledge base](https://tls.mbed.org/kb), as currently all the articles are about the standalone edition.

* The mbed OS edition has a smaller set of features enabled by default in `config.h`, in order to reduce footprint. While the default configuration of the standalone edition puts more emphasize on maintaining interoperability with old peers, the mbed OS edition only enables the most modern ciphers and the latest version of (D)TLS.

* The following components of mbed TLS are disabled in the mbed OS edition: `net_sockets.c` and `timing.c`. This is because mbed OS include their equivalents.

* The mbed OS edition comes with a fully integrated API for (D)TLS connections in a companion module: [mbed-tls-sockets](https://github.com/ARMmbed/mbed-tls-sockets). See "Performing TLS and DTLS connections" above.

## Other resources

The [mbed TLS website](https://tls.mbed.org) contains many other useful
resources for the developer, such as [developer
documentation](https://tls.mbed.org/dev-corner), [knowledgebase
articles](https://tls.mbed.org/kb), and a [support forum](https://tls.mbed.org/discussions).

## Contributing

We gratefully accept bug reports and contributions from the community. There are some requirements we need to fulfill in order to be able to integrate contributions:

* Simple bug fixes to existing code do not contain copyright themselves and we can integrate without issue. The same is true of trivial contributions.

* For larger contributions, such as a new feature, the code can possibly fall under copyright law. We then need your consent to share in the ownership of the copyright. We have a form for this, which we will send to you in case you submit a contribution or pull request that we deem this necessary for.

To contribute, please:

* [Check for open issues](https://github.com/ARMmbed/mbedtls/issues) or [start a discussion](https://tls.mbed.org/discussions) around a feature idea or a bug.

* Fork the [mbed TLS repository on GitHub](https://github.com/ARMmbed/mbedtls) to start making your changes. As a general rule, you should use the "development" branch as a basis.

* Write a test that shows that the bug was fixed or that the feature works as expected.

* Send a pull request and bug us until it gets merged and published. We will include your name in the ChangeLog.

# Authenticated Encryption Example

This application performs authenticated encryption and authenticated decryption of a buffer. It serves as a tutorial for the basic authenticated encryption functions of mbed TLS.

## Pre-requisites

To build and run this example you must have:

* A computer with the following software installed:
  * [CMake](http://www.cmake.org/download/).
  * [yotta](https://github.com/ARMmbed/yotta). Please note that **yotta has its own set of dependencies**, listed in the [installation instructions](http://armmbed.github.io/yotta/#installing-on-windows).
  * [Python](https://www.python.org/downloads/).
  * [The ARM GCC toolchain](https://launchpad.net/gcc-arm-embedded).
  * A serial terminal emulator (Like screen, pySerial and cu).
* An [FRDM-K64F](http://developer.mbed.org/platforms/FRDM-K64F/) development board, or another board supported by mbed OS (in which case you'll have to substitute frdm-k64f-gcc with the appropriate target in the instructions below).
* A micro-USB cable.
* If your OS is Windows, please follow the installation instructions [for the serial port driver](https://developer.mbed.org/handbook/Windows-serial-configuration).

## Getting started

1. Connect the FRDM-K64F to the computer with the micro-USB cable, being careful to use the "OpenSDA" connector on the target board.

2. Navigate to the mbedtls directory supplied with your release and open a terminal.

3. Set the yotta target:

    ```
    yotta target frdm-k64f-gcc
    ```

4. Build mbedtls and the examples. This may take a long time if this is your first compilation:

    ```
    $ yotta build
    ```

5. Copy `build/frdm-k64f-gcc/test/mbedtls-test-example-authcrypt.bin` to your mbed board and wait until the LED next to the USB port stops blinking.

6. Start the serial terminal emulator and connect to the virtual serial port presented by FRDM-K64F.

    Use the following settings:

    * 115200 baud (not 9600).
    * 8N1.
    * No flow control.

7. Press the Reset button on the board.

8. The output in the terminal window should look like:

    ```
    {{timeout;10}}
    {{host_test_name;default}}
    {{description;mbed TLS example authcrypt}}
    {{test_id;MBEDTLS_EX_AUTHCRYPT}}
    {{start}}


    plaintext message: 536f6d65207468696e67732061726520626574746572206c65667420756e7265616400
    ciphertext: c57f7afb94f14c7977d785d08682a2596bd62ee9dcf216b8cccd997afee9b402f5de1739e8e6467aa363749ef39392e5c66622b01c7203ec0a3d14
    decrypted: 536f6d65207468696e67732061726520626574746572206c65667420756e7265616400

    DONE
    {{success}}
    {{end}}
    ```

The actual output for the ciphertext line will vary on each run because of the use of a random nonce in the encryption process.
# mbed TLS Selftest Example

This application runs the various selftest functions of individual mbed TLS components. It serves as a basic sanity check to verify operation of mbed TLS on your platform. In the future, a wider portion of the mbed TLS test suite will become part of this example application.

## Pre-requisites

To build and run this example you must have:

* A computer with the following software installed:
  * [CMake](http://www.cmake.org/download/).
  * [yotta](https://github.com/ARMmbed/yotta). Please note that **yotta has its own set of dependencies**, listed in the [installation instructions](http://armmbed.github.io/yotta/#installing-on-windows).
  * [Python](https://www.python.org/downloads/).
  * [The ARM GCC toolchain](https://launchpad.net/gcc-arm-embedded).
  * A serial terminal emulator (Like screen, pySerial and cu).
* An [FRDM-K64F](http://developer.mbed.org/platforms/FRDM-K64F/) development board, or another board supported by mbed OS (in which case you'll have to substitute frdm-k64f-gcc with the appropriate target in the instructions below).
* A micro-USB cable.
* If your OS is Windows, please follow the installation instructions [for the serial port driver](https://developer.mbed.org/handbook/Windows-serial-configuration).

## Getting started

1. Connect the FRDM-K64F to the computer with the micro-USB cable, being careful to use the "OpenSDA" connector on the target board.

2. Navigate to the mbedtls directory supplied with your release and open a terminal.

3. Set the yotta target:

    ```
    yotta target frdm-k64f-gcc
    ```

4. Build mbedtls and the examples. This may take a long time if this is your first compilation:

    ```
    $ yotta build
    ```

5. Copy `build/frdm-k64f-gcc/test/mbedtls-test-example-selftest.bin` to your mbed board and wait until the LED next to the USB port stops blinking.

6. Start the serial terminal emulator and connect to the virtual serial port presented by FRDM-K64F.

    Use the following settings:

    * 115200 baud (not 9600).
    * 8N1.
    * No flow control.

7. Press the Reset button on the board.

8. The output in the terminal window should look like:

    ```
    {{timeout;40}}
    {{host_test_name;default}}
    {{description;mbed TLS selftest program}}
    {{test_id;MBEDTLS_SELFTEST}}
    {{start}}

      SHA-224 test #1: passed
      SHA-224 test #2: passed
      SHA-224 test #3: passed
      SHA-256 test #1: passed
      SHA-256 test #2: passed
      SHA-256 test #3: passed

        [ ... several lines omitted ... ]

      CTR_DRBG (PR = TRUE) : passed
      CTR_DRBG (PR = FALSE): passed

      HMAC_DRBG (PR = True) : passed
      HMAC_DRBG (PR = False) : passed

      ECP test #1 (constant op_count, base point G): passed
      ECP test #2 (constant op_count, other point): passed

      ENTROPY test: passed

      [ All tests passed ]

    {{success}}
    {{end}}
    ```
# SHA-256 Hash Example

This application performs hashing of a buffer with SHA-256 using various APIs. It serves as a tutorial for the basic hashing APIs of mbed TLS.

## Pre-requisites

To build and run this example you must have:

* A computer with the following software installed:
  * [CMake](http://www.cmake.org/download/).
  * [yotta](https://github.com/ARMmbed/yotta). Please note that **yotta has its own set of dependencies**, listed in the [installation instructions](http://armmbed.github.io/yotta/#installing-on-windows).
  * [Python](https://www.python.org/downloads/).
  * [The ARM GCC toolchain](https://launchpad.net/gcc-arm-embedded).
  * A serial terminal emulator (Like screen, pySerial and cu).
* An [FRDM-K64F](http://developer.mbed.org/platforms/FRDM-K64F/) development board, or another board supported by mbed OS (in which case you'll have to substitute frdm-k64f-gcc with the appropriate target in the instructions below).
* A micro-USB cable.
* If your OS is Windows, please follow the installation instructions [for the serial port driver](https://developer.mbed.org/handbook/Windows-serial-configuration).

## Getting started

1. Connect the FRDM-K64F to the computer with the micro-USB cable, being careful to use the "OpenSDA" connector on the target board.

2. Navigate to the mbedtls directory supplied with your release and open a terminal.

3. Set the yotta target:

    ```
    yotta target frdm-k64f-gcc
    ```

4. Build mbedtls and the examples. This may take a long time if this is your first compilation:

    ```
    $ yotta build
    ```

5. Copy `build/frdm-k64f-gcc/test/mbedtls-test-example-hashing.bin` to your mbed board and wait until the LED next to the USB port stops blinking.

6. Start the serial terminal emulator and connect to the virtual serial port presented by FRDM-K64F.

    Use the following settings:

    * 115200 baud (not 9600).
    * 8N1.
    * No flow control.

7. Press the Reset button on the board.

8. The output in the terminal window should look like:

    ```
    {{timeout;10}}
    {{host_test_name;default}}
    {{description;mbed TLS example on hashing}}
    {{test_id;MBEDTLS_EX_HASHING}}
    {{start}}


    Method 1: 315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3
    Method 2: 315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3
    Method 3: 315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3
    Method 4: 315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3

    DONE
    {{success}}
    {{end}}
    ```
# mbed TLS Benchmark Example

This application benchmarks the various cryptographic primitives offered by mbed TLS.

## Pre-requisites

To build and run this example you must have:

* A computer with the following software installed:
  * [CMake](http://www.cmake.org/download/).
  * [yotta](https://github.com/ARMmbed/yotta). Please note that **yotta has its own set of dependencies**, listed in the [installation instructions](http://armmbed.github.io/yotta/#installing-on-windows).
  * [Python](https://www.python.org/downloads/).
  * [The ARM GCC toolchain](https://launchpad.net/gcc-arm-embedded).
  * A serial terminal emulator (Like screen, pySerial and cu).
* An [FRDM-K64F](http://developer.mbed.org/platforms/FRDM-K64F/) development board, or another board supported by mbed OS (in which case you'll have to substitute frdm-k64f-gcc with the appropriate target in the instructions below).
* A micro-USB cable.
* If your OS is Windows, please follow the installation instructions [for the serial port driver](https://developer.mbed.org/handbook/Windows-serial-configuration).

## Getting started

1. Connect the FRDM-K64F to the computer with the micro-USB cable, being careful to use the "OpenSDA" connector on the target board.

2. Navigate to the mbedtls directory supplied with your release and open a terminal.

3. Set the yotta target:

    ```
    yotta target frdm-k64f-gcc
    ```

4. Build mbedtls and the examples. This may take a long time if this is your first compilation:

    ```
    $ yotta build
    ```

5. Copy `build/frdm-k64f-gcc/test/mbedtls-test-example-benchmark.bin` to your mbed board and wait until the LED next to the USB port stops blinking.

6. Start the serial terminal emulator and connect to the virtual serial port presented by FRDM-K64F.

    Use the following settings:

    * 115200 baud (not 9600).
    * 8N1.
    * No flow control.

7. Press the Reset button on the board.

8. The output in the terminal window should look like:

    ```
    {{timeout;150}}
    {{host_test_name;default}}
    {{description;mbed TLS benchmark program}}
    {{test_id;MBEDTLS_BENCHMARK}}
    {{start}}


      SHA-1                    :       3644 KiB/s,         32 cycles/byte
      SHA-256                  :       1957 KiB/s,         59 cycles/byte
      SHA-512                  :        587 KiB/s,        200 cycles/byte
      AES-CBC-128              :       1359 KiB/s,         86 cycles/byte
      AES-CBC-192              :       1183 KiB/s,         99 cycles/byte
      AES-CBC-256              :       1048 KiB/s,        111 cycles/byte
      AES-GCM-128              :        421 KiB/s,        279 cycles/byte
      AES-GCM-192              :        403 KiB/s,        292 cycles/byte
      AES-GCM-256              :        385 KiB/s,        305 cycles/byte
      AES-CCM-128              :        542 KiB/s,        216 cycles/byte
      AES-CCM-192              :        484 KiB/s,        242 cycles/byte
      AES-CCM-256              :        437 KiB/s,        268 cycles/byte
      CTR_DRBG (NOPR)          :       1002 KiB/s,        117 cycles/byte
      CTR_DRBG (PR)            :        705 KiB/s,        166 cycles/byte
      HMAC_DRBG SHA-1 (NOPR)   :        228 KiB/s,        517 cycles/byte
      HMAC_DRBG SHA-1 (PR)     :        210 KiB/s,        561 cycles/byte
      HMAC_DRBG SHA-256 (NOPR) :        212 KiB/s,        557 cycles/byte
      HMAC_DRBG SHA-256 (PR)   :        185 KiB/s,        637 cycles/byte
      RSA-2048                 :      41 ms/ public
      RSA-2048                 :    1349 ms/private
      RSA-4096                 :     134 ms/ public
      RSA-4096                 :    7149 ms/private
      ECDSA-secp384r1          :     640 ms/sign
      ECDSA-secp256r1          :     387 ms/sign
      ECDSA-secp384r1          :    1233 ms/verify
      ECDSA-secp256r1          :     751 ms/verify
      ECDHE-secp384r1          :    1191 ms/handshake
      ECDHE-secp256r1          :     730 ms/handshake
      ECDHE-Curve25519         :     611 ms/handshake
      ECDH-secp384r1           :     584 ms/handshake
      ECDH-secp256r1           :     365 ms/handshake
      ECDH-Curve25519          :     303 ms/handshake

    {{success}}
    {{end}}
    ```

Any performance data generated by this example application are indicative only of the performance of the mbed TLS module on the platform it's executed on.

Differences in the integration of mbed TLS into the platform, such as whether all available hardware accelerators have been used or not, can lead to significant differences in performance, and so results from the program are not intended to be used to meaningfully compare platforms.

The figures may also slightly change from execution to execution due to variations in the timing functions.
musl libc:
==========

This directory contains **musl libc**, obtained from this URL.

```
https://www.musl-libc.org/releases/musl-1.1.19.tar.gz
```

Typing **make** installs the source tree under the build directory and
applies patches to it. Nothing is built though, as building is performed
from the **libc** directory.
libc-test is developed as part of the musl project
http://www.musl-libc.org/

configuring:
	cp config.mak.def config.mak
	edit config.mak
build and run tests:
	make
clean up:
	make clean

make builds all test binaries and runs them to create
a REPORT file that contains all build and runtime errors
(this means that make does not stop at build failures)

contributing tests:

design goals:

- tests should be easy to run and build even a single test in isolation
(so test should be self contained if possible)
- failure of one test should not interfere with others
(build failure, crash or unexpected results are all failures)
- test output should point to the cause of the failure
- test results should be robust
- the test system should have minimal dependency
(libc, posix sh, gnu make)
- the test system should run on all archs and libcs
- tests should leave the system in a clean state

conventions:

each test is in a separate file at a path like src/directory/file.c with
its own main

the test should return 0 on success and non-0 on failure, on failure it
should print error messages to standard out if possible, on success no
message should be printed

to help with the above test protocol use t_error function for printing
errors and return t_status from main, see src/common/test.h
(t_error allows standard printf formatting, outputs at most 512bytes
in a single write call to fd 1, so there is no buffering, long outputs
are truncated, it sets the global t_status to 1)

it is common to do many similar checks in a test, in such cases macros
may be used to simplify the code like
#define T1(a,b) (check(a,b) || (t_error("check(%s,%s) failed\n", a, b),0))
#define T2(f,w) (result=(f), result==(w) || (t_error("%s failed: got %s, want %s\n", #f, result, w),0))

binaries should be possible to run from arbitrary directory.
the build system runs the tests using the src/common/runtest tool which
kills the test process after a timeout and reports the exit status
in case of failure

directories:

src/api: interface tests, build time include header tests
src/common: common utilities compiled into libtest.a
src/functional: functional tests aiming for large coverage of libc
src/math: tests for each math function with input-output test vectors
src/regression: regression tests aiming for testing particular bugs

initial set of functional tests are derived from the libc-testsuit of
Rich Felker, regression tests should contain reference of the bug
(musl commit hash, glibc bug tracker url, etc)

build system:

the main non-file make targets are all, run, clean and cleanall.
(cleanall removes the reports unlike clean, run reruns the dynamically
linked executables)

make variable can be overridden from config.mak or the make command line,
the variable B sets the build directory which is src by default

for each directory under src there are targets like $(B)/directory/all,
$(B)/directory/run and $(B)/directory/clean to make only the contents
of that directory, each directory has its own Makefile set up so it
invokes the top level make with B=src src/directory/foo for the foo
target, so it is possible to work only under a specific test directory

the build and runtime errors of each target are accumulated into a
target.err file and in the end they are concatenated into a REPORT

each .c file in src/functional and src/regression are built into a
dynamic linked and a static linked executable test binary by default,
this behaviour can be changed by a similarly named .mk file changing
make variables and specifying additional rules:

$(B)/$(N) is the name of the binary target (the file name without the .c)
$(B)/$(N)-static is the name of the static binary target
$(B)/$(D) is the build directory
$(N).CFLAGS are added to the CFLAGS at compilation
$(N).LDFLAGS are added to the LDFLAGS at linking
$(N).LDLIBS are added to the LDLIBS at linking
$(N).BINS are the targets (if empty no binaries are built)
$(N).LIBS are the non-executable targets (shared objects may use it)

if a binary is linked together from several .o files then they
have to be specified as prerequisits for the binary targets and
added to the $(N).LDLIBS as well

if a binary depends on a file at runtime (eg. a .so opened by dlopen)
then the $(N).err target should depend on that file
libm tests

tools from gen/ were used to generate the tests

test vectors are generated like

echo 3.14 |./gen sin

using crlibm, ucb and a various other test inputs
tools for generating testcases and checking ulp error of math functions
(needs cleanup)

gen: math functions implemented with mpfr
mgen: math functions from libm
check: compare input to libm and report errors

check asinh in the [0.125,0.5] domain over 100k points and report >1.5ulp errors:

./rnd -a 0x1p-3 -b 0x1p-1 -n 100000 |./gen asinh |./check asinh 1.5
test vectors from ucbtest/ucblib
http://www.netlib.org/fp/ucbtest.tgz

format is changed, but original comments are kept

some of the test outputs are changed to be
correctly rounded and follow c99 annex F.
test vectors from crlibm
http://lipforge.ens-lyon.fr/www/crlibm/

format is changed, but original comments are kept

    musl libc

musl, pronounced like the word "mussel", is an MIT-licensed
implementation of the standard C library targetting the Linux syscall
API, suitable for use in a wide range of deployment environments. musl
offers efficient static and dynamic linking support, lightweight code
and low runtime overhead, strong fail-safe guarantees under correct
usage, and correctness in the sense of standards conformance and
safety. musl is built on the principle that these goals are best
achieved through simple code that is easy to understand and maintain.

The 1.1 release series for musl features coverage for all interfaces
defined in ISO C99 and POSIX 2008 base, along with a number of
non-standardized interfaces for compatibility with Linux, BSD, and
glibc functionality.

For basic installation instructions, see the included INSTALL file.
Information on full musl-targeted compiler toolchains, system
bootstrapping, and Linux distributions built on musl can be found on
the project website:

    http://www.musl-libc.org/
**musl libc** patches
=====================

This directory contains patches for **musl libc**. These patches are applied
by the cmake file after the source distribution is copied to the build
directory.
Test Naming and Directory Structure
===================================

The directory structure for the unique_ptr class templates differs from the
normal test directory naming conventions (e.g. matching the stable name in the standard).

Instead of having a [unique.ptr.single] and [unique.ptr.runtime] directory,
each containing their own tests, a single directory, "unique.ptr.class",
contains both sets of tests.

This allows the common behavior of the two unique_ptr specializations to be
tested in the same place without duplication.

Tests specific to [unique.ptr.single] have the suffix ".single.pass.cpp"
and those specific to [unique.ptr.runtime] are named "*.runtime.pass.cpp".
Tests for both specializations are named normally.
This directory contains abi lists representing the symbols exported
by the libc++ library. The lists are generated using sym_extract.py.

Every time a symbol is added or removed from the libc++ library each of the
lists *MUST* be updated to reflect the changes.

TODO Add more documentation about generating and using the lists.
TODO Add more documentation about the build configuration the lists are generated against.
This directory contains a partial implementation of the xlocale APIs for
Solaris.  Some portions are lifted from FreeBSD libc, and so are covered by a
2-clause BSD license instead of the MIT/UUIC license that the rest of libc++ is
distributed under.
libc++ Documentation
====================

The libc++ documentation is written using the Sphinx documentation generator. It is
currently tested with Sphinx 1.1.3.

To build the documents into html configure libc++ with the following cmake options:

  * -DLLVM_ENABLE_SPHINX=ON
  * -DLIBCXX_INCLUDE_DOCS=ON

After configuring libc++ with these options the make rule `docs-libcxx-html`
should be available.
LLVM notes
----------

This directory contains the Google Benchmark source code with some unnecessary
files removed. Note that this directory is under a different license than
libc++.
# benchmark
[![Build Status](https://travis-ci.org/google/benchmark.svg?branch=master)](https://travis-ci.org/google/benchmark)
[![Build status](https://ci.appveyor.com/api/projects/status/u0qsyp7t1tk7cpxs/branch/master?svg=true)](https://ci.appveyor.com/project/google/benchmark/branch/master)
[![Coverage Status](https://coveralls.io/repos/google/benchmark/badge.svg)](https://coveralls.io/r/google/benchmark)
[![slackin](https://slackin-iqtfqnpzxd.now.sh/badge.svg)](https://slackin-iqtfqnpzxd.now.sh/)

A library to support the benchmarking of functions, similar to unit-tests.

Discussion group: https://groups.google.com/d/forum/benchmark-discuss

IRC channel: https://freenode.net #googlebenchmark

[Known issues and common problems](#known-issues)

[Additional Tooling Documentation](docs/tools.md)

[Assembly Testing Documentation](docs/AssemblyTests.md)


## Building

The basic steps for configuring and building the library look like this:

```bash
$ git clone https://github.com/google/benchmark.git
# Benchmark requires Google Test as a dependency. Add the source tree as a subdirectory.
$ git clone https://github.com/google/googletest.git benchmark/googletest
$ mkdir build && cd build
$ cmake -G <generator> [options] ../benchmark
# Assuming a makefile generator was used
$ make
```

Note that Google Benchmark requires Google Test to build and run the tests. This
dependency can be provided two ways:

* Checkout the Google Test sources into `benchmark/googletest` as above.
* Otherwise, if `-DBENCHMARK_DOWNLOAD_DEPENDENCIES=ON` is specified during
  configuration, the library will automatically download and build any required
  dependencies.

If you do not wish to build and run the tests, add `-DBENCHMARK_ENABLE_GTEST_TESTS=OFF`
to `CMAKE_ARGS`.


## Installation Guide

For Ubuntu and Debian Based System

First make sure you have git and cmake installed (If not please install it)

```
sudo apt-get install git
sudo apt-get install cmake
```

Now, let's clone the repository and build it

```
git clone https://github.com/google/benchmark.git
cd benchmark
git clone https://github.com/google/googletest.git
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=RELEASE
make
```

We need to install the library globally now

```
sudo make install
```

Now you have google/benchmark installed in your machine
Note: Don't forget to link to pthread library while building

## Stable and Experimental Library Versions

The main branch contains the latest stable version of the benchmarking library;
the API of which can be considered largely stable, with source breaking changes
being made only upon the release of a new major version.

Newer, experimental, features are implemented and tested on the
[`v2` branch](https://github.com/google/benchmark/tree/v2). Users who wish
to use, test, and provide feedback on the new features are encouraged to try
this branch. However, this branch provides no stability guarantees and reserves
the right to change and break the API at any time.

## Prerequisite knowledge

Before attempting to understand this framework one should ideally have some familiarity with the structure and format of the Google Test framework, upon which it is based. Documentation for Google Test, including a "Getting Started" (primer) guide, is available here:
https://github.com/google/googletest/blob/master/googletest/docs/primer.md


## Example usage
### Basic usage
Define a function that executes the code to be measured.

```c++
#include <benchmark/benchmark.h>

static void BM_StringCreation(benchmark::State& state) {
  for (auto _ : state)
    std::string empty_string;
}
// Register the function as a benchmark
BENCHMARK(BM_StringCreation);

// Define another benchmark
static void BM_StringCopy(benchmark::State& state) {
  std::string x = "hello";
  for (auto _ : state)
    std::string copy(x);
}
BENCHMARK(BM_StringCopy);

BENCHMARK_MAIN();
```

Don't forget to inform your linker to add benchmark library e.g. through 
`-lbenchmark` compilation flag. Alternatively, you may leave out the 
`BENCHMARK_MAIN();` at the end of the source file and link against 
`-lbenchmark_main` to get the same default behavior.

The benchmark library will reporting the timing for the code within the `for(...)` loop.

### Passing arguments
Sometimes a family of benchmarks can be implemented with just one routine that
takes an extra argument to specify which one of the family of benchmarks to
run. For example, the following code defines a family of benchmarks for
measuring the speed of `memcpy()` calls of different lengths:

```c++
static void BM_memcpy(benchmark::State& state) {
  char* src = new char[state.range(0)];
  char* dst = new char[state.range(0)];
  memset(src, 'x', state.range(0));
  for (auto _ : state)
    memcpy(dst, src, state.range(0));
  state.SetBytesProcessed(int64_t(state.iterations()) *
                          int64_t(state.range(0)));
  delete[] src;
  delete[] dst;
}
BENCHMARK(BM_memcpy)->Arg(8)->Arg(64)->Arg(512)->Arg(1<<10)->Arg(8<<10);
```

The preceding code is quite repetitive, and can be replaced with the following
short-hand. The following invocation will pick a few appropriate arguments in
the specified range and will generate a benchmark for each such argument.

```c++
BENCHMARK(BM_memcpy)->Range(8, 8<<10);
```

By default the arguments in the range are generated in multiples of eight and
the command above selects [ 8, 64, 512, 4k, 8k ]. In the following code the
range multiplier is changed to multiples of two.

```c++
BENCHMARK(BM_memcpy)->RangeMultiplier(2)->Range(8, 8<<10);
```
Now arguments generated are [ 8, 16, 32, 64, 128, 256, 512, 1024, 2k, 4k, 8k ].

You might have a benchmark that depends on two or more inputs. For example, the
following code defines a family of benchmarks for measuring the speed of set
insertion.

```c++
static void BM_SetInsert(benchmark::State& state) {
  std::set<int> data;
  for (auto _ : state) {
    state.PauseTiming();
    data = ConstructRandomSet(state.range(0));
    state.ResumeTiming();
    for (int j = 0; j < state.range(1); ++j)
      data.insert(RandomNumber());
  }
}
BENCHMARK(BM_SetInsert)
    ->Args({1<<10, 128})
    ->Args({2<<10, 128})
    ->Args({4<<10, 128})
    ->Args({8<<10, 128})
    ->Args({1<<10, 512})
    ->Args({2<<10, 512})
    ->Args({4<<10, 512})
    ->Args({8<<10, 512});
```

The preceding code is quite repetitive, and can be replaced with the following
short-hand. The following macro will pick a few appropriate arguments in the
product of the two specified ranges and will generate a benchmark for each such
pair.

```c++
BENCHMARK(BM_SetInsert)->Ranges({{1<<10, 8<<10}, {128, 512}});
```

For more complex patterns of inputs, passing a custom function to `Apply` allows
programmatic specification of an arbitrary set of arguments on which to run the
benchmark. The following example enumerates a dense range on one parameter,
and a sparse range on the second.

```c++
static void CustomArguments(benchmark::internal::Benchmark* b) {
  for (int i = 0; i <= 10; ++i)
    for (int j = 32; j <= 1024*1024; j *= 8)
      b->Args({i, j});
}
BENCHMARK(BM_SetInsert)->Apply(CustomArguments);
```

### Calculate asymptotic complexity (Big O)
Asymptotic complexity might be calculated for a family of benchmarks. The
following code will calculate the coefficient for the high-order term in the
running time and the normalized root-mean square error of string comparison.

```c++
static void BM_StringCompare(benchmark::State& state) {
  std::string s1(state.range(0), '-');
  std::string s2(state.range(0), '-');
  for (auto _ : state) {
    benchmark::DoNotOptimize(s1.compare(s2));
  }
  state.SetComplexityN(state.range(0));
}
BENCHMARK(BM_StringCompare)
    ->RangeMultiplier(2)->Range(1<<10, 1<<18)->Complexity(benchmark::oN);
```

As shown in the following invocation, asymptotic complexity might also be
calculated automatically.

```c++
BENCHMARK(BM_StringCompare)
    ->RangeMultiplier(2)->Range(1<<10, 1<<18)->Complexity();
```

The following code will specify asymptotic complexity with a lambda function,
that might be used to customize high-order term calculation.

```c++
BENCHMARK(BM_StringCompare)->RangeMultiplier(2)
    ->Range(1<<10, 1<<18)->Complexity([](int n)->double{return n; });
```

### Templated benchmarks
Templated benchmarks work the same way: This example produces and consumes
messages of size `sizeof(v)` `range_x` times. It also outputs throughput in the
absence of multiprogramming.

```c++
template <class Q> int BM_Sequential(benchmark::State& state) {
  Q q;
  typename Q::value_type v;
  for (auto _ : state) {
    for (int i = state.range(0); i--; )
      q.push(v);
    for (int e = state.range(0); e--; )
      q.Wait(&v);
  }
  // actually messages, not bytes:
  state.SetBytesProcessed(
      static_cast<int64_t>(state.iterations())*state.range(0));
}
BENCHMARK_TEMPLATE(BM_Sequential, WaitQueue<int>)->Range(1<<0, 1<<10);
```

Three macros are provided for adding benchmark templates.

```c++
#ifdef BENCHMARK_HAS_CXX11
#define BENCHMARK_TEMPLATE(func, ...) // Takes any number of parameters.
#else // C++ < C++11
#define BENCHMARK_TEMPLATE(func, arg1)
#endif
#define BENCHMARK_TEMPLATE1(func, arg1)
#define BENCHMARK_TEMPLATE2(func, arg1, arg2)
```

### A Faster KeepRunning loop

In C++11 mode, a ranged-based for loop should be used in preference to
the `KeepRunning` loop for running the benchmarks. For example:

```c++
static void BM_Fast(benchmark::State &state) {
  for (auto _ : state) {
    FastOperation();
  }
}
BENCHMARK(BM_Fast);
```

The reason the ranged-for loop is faster than using `KeepRunning`, is
because `KeepRunning` requires a memory load and store of the iteration count
ever iteration, whereas the ranged-for variant is able to keep the iteration count
in a register.

For example, an empty inner loop of using the ranged-based for method looks like:

```asm
# Loop Init
  mov rbx, qword ptr [r14 + 104]
  call benchmark::State::StartKeepRunning()
  test rbx, rbx
  je .LoopEnd
.LoopHeader: # =>This Inner Loop Header: Depth=1
  add rbx, -1
  jne .LoopHeader
.LoopEnd:
```

Compared to an empty `KeepRunning` loop, which looks like:

```asm
.LoopHeader: # in Loop: Header=BB0_3 Depth=1
  cmp byte ptr [rbx], 1
  jne .LoopInit
.LoopBody: # =>This Inner Loop Header: Depth=1
  mov rax, qword ptr [rbx + 8]
  lea rcx, [rax + 1]
  mov qword ptr [rbx + 8], rcx
  cmp rax, qword ptr [rbx + 104]
  jb .LoopHeader
  jmp .LoopEnd
.LoopInit:
  mov rdi, rbx
  call benchmark::State::StartKeepRunning()
  jmp .LoopBody
.LoopEnd:
```

Unless C++03 compatibility is required, the ranged-for variant of writing
the benchmark loop should be preferred.  

## Passing arbitrary arguments to a benchmark
In C++11 it is possible to define a benchmark that takes an arbitrary number
of extra arguments. The `BENCHMARK_CAPTURE(func, test_case_name, ...args)`
macro creates a benchmark that invokes `func`  with the `benchmark::State` as
the first argument followed by the specified `args...`.
The `test_case_name` is appended to the name of the benchmark and
should describe the values passed.

```c++
template <class ...ExtraArgs>
void BM_takes_args(benchmark::State& state, ExtraArgs&&... extra_args) {
  [...]
}
// Registers a benchmark named "BM_takes_args/int_string_test" that passes
// the specified values to `extra_args`.
BENCHMARK_CAPTURE(BM_takes_args, int_string_test, 42, std::string("abc"));
```
Note that elements of `...args` may refer to global variables. Users should
avoid modifying global state inside of a benchmark.

## Using RegisterBenchmark(name, fn, args...)

The `RegisterBenchmark(name, func, args...)` function provides an alternative
way to create and register benchmarks.
`RegisterBenchmark(name, func, args...)` creates, registers, and returns a
pointer to a new benchmark with the specified `name` that invokes
`func(st, args...)` where `st` is a `benchmark::State` object.

Unlike the `BENCHMARK` registration macros, which can only be used at the global
scope, the `RegisterBenchmark` can be called anywhere. This allows for
benchmark tests to be registered programmatically.

Additionally `RegisterBenchmark` allows any callable object to be registered
as a benchmark. Including capturing lambdas and function objects.

For Example:
```c++
auto BM_test = [](benchmark::State& st, auto Inputs) { /* ... */ };

int main(int argc, char** argv) {
  for (auto& test_input : { /* ... */ })
      benchmark::RegisterBenchmark(test_input.name(), BM_test, test_input);
  benchmark::Initialize(&argc, argv);
  benchmark::RunSpecifiedBenchmarks();
}
```

### Multithreaded benchmarks
In a multithreaded test (benchmark invoked by multiple threads simultaneously),
it is guaranteed that none of the threads will start until all have reached
the start of the benchmark loop, and all will have finished before any thread
exits the benchmark loop. (This behavior is also provided by the `KeepRunning()`
API) As such, any global setup or teardown can be wrapped in a check against the thread
index:

```c++
static void BM_MultiThreaded(benchmark::State& state) {
  if (state.thread_index == 0) {
    // Setup code here.
  }
  for (auto _ : state) {
    // Run the test as normal.
  }
  if (state.thread_index == 0) {
    // Teardown code here.
  }
}
BENCHMARK(BM_MultiThreaded)->Threads(2);
```

If the benchmarked code itself uses threads and you want to compare it to
single-threaded code, you may want to use real-time ("wallclock") measurements
for latency comparisons:

```c++
BENCHMARK(BM_test)->Range(8, 8<<10)->UseRealTime();
```

Without `UseRealTime`, CPU time is used by default.


## Manual timing
For benchmarking something for which neither CPU time nor real-time are
correct or accurate enough, completely manual timing is supported using
the `UseManualTime` function.

When `UseManualTime` is used, the benchmarked code must call
`SetIterationTime` once per iteration of the benchmark loop to
report the manually measured time.

An example use case for this is benchmarking GPU execution (e.g. OpenCL
or CUDA kernels, OpenGL or Vulkan or Direct3D draw calls), which cannot
be accurately measured using CPU time or real-time. Instead, they can be
measured accurately using a dedicated API, and these measurement results
can be reported back with `SetIterationTime`.

```c++
static void BM_ManualTiming(benchmark::State& state) {
  int microseconds = state.range(0);
  std::chrono::duration<double, std::micro> sleep_duration {
    static_cast<double>(microseconds)
  };

  for (auto _ : state) {
    auto start = std::chrono::high_resolution_clock::now();
    // Simulate some useful workload with a sleep
    std::this_thread::sleep_for(sleep_duration);
    auto end   = std::chrono::high_resolution_clock::now();

    auto elapsed_seconds =
      std::chrono::duration_cast<std::chrono::duration<double>>(
        end - start);

    state.SetIterationTime(elapsed_seconds.count());
  }
}
BENCHMARK(BM_ManualTiming)->Range(1, 1<<17)->UseManualTime();
```

### Preventing optimisation
To prevent a value or expression from being optimized away by the compiler
the `benchmark::DoNotOptimize(...)` and `benchmark::ClobberMemory()`
functions can be used.

```c++
static void BM_test(benchmark::State& state) {
  for (auto _ : state) {
      int x = 0;
      for (int i=0; i < 64; ++i) {
        benchmark::DoNotOptimize(x += i);
      }
  }
}
```

`DoNotOptimize(<expr>)` forces the  *result* of `<expr>` to be stored in either
memory or a register. For GNU based compilers it acts as read/write barrier
for global memory. More specifically it forces the compiler to flush pending
writes to memory and reload any other values as necessary.

Note that `DoNotOptimize(<expr>)` does not prevent optimizations on `<expr>`
in any way. `<expr>` may even be removed entirely when the result is already
known. For example:

```c++
  /* Example 1: `<expr>` is removed entirely. */
  int foo(int x) { return x + 42; }
  while (...) DoNotOptimize(foo(0)); // Optimized to DoNotOptimize(42);

  /*  Example 2: Result of '<expr>' is only reused */
  int bar(int) __attribute__((const));
  while (...) DoNotOptimize(bar(0)); // Optimized to:
  // int __result__ = bar(0);
  // while (...) DoNotOptimize(__result__);
```

The second tool for preventing optimizations is `ClobberMemory()`. In essence
`ClobberMemory()` forces the compiler to perform all pending writes to global
memory. Memory managed by block scope objects must be "escaped" using
`DoNotOptimize(...)` before it can be clobbered. In the below example
`ClobberMemory()` prevents the call to `v.push_back(42)` from being optimized
away.

```c++
static void BM_vector_push_back(benchmark::State& state) {
  for (auto _ : state) {
    std::vector<int> v;
    v.reserve(1);
    benchmark::DoNotOptimize(v.data()); // Allow v.data() to be clobbered.
    v.push_back(42);
    benchmark::ClobberMemory(); // Force 42 to be written to memory.
  }
}
```

Note that `ClobberMemory()` is only available for GNU or MSVC based compilers.

### Set time unit manually
If a benchmark runs a few milliseconds it may be hard to visually compare the
measured times, since the output data is given in nanoseconds per default. In
order to manually set the time unit, you can specify it manually:

```c++
BENCHMARK(BM_test)->Unit(benchmark::kMillisecond);
```

## Controlling number of iterations
In all cases, the number of iterations for which the benchmark is run is
governed by the amount of time the benchmark takes. Concretely, the number of
iterations is at least one, not more than 1e9, until CPU time is greater than
the minimum time, or the wallclock time is 5x minimum time. The minimum time is
set as a flag `--benchmark_min_time` or per benchmark by calling `MinTime` on
the registered benchmark object.

## Reporting the mean, median and standard deviation by repeated benchmarks
By default each benchmark is run once and that single result is reported.
However benchmarks are often noisy and a single result may not be representative
of the overall behavior. For this reason it's possible to repeatedly rerun the
benchmark.

The number of runs of each benchmark is specified globally by the
`--benchmark_repetitions` flag or on a per benchmark basis by calling
`Repetitions` on the registered benchmark object. When a benchmark is run more
than once the mean, median and standard deviation of the runs will be reported.

Additionally the `--benchmark_report_aggregates_only={true|false}` flag or
`ReportAggregatesOnly(bool)` function can be used to change how repeated tests
are reported. By default the result of each repeated run is reported. When this
option is `true` only the mean, median and standard deviation of the runs is reported.
Calling `ReportAggregatesOnly(bool)` on a registered benchmark object overrides
the value of the flag for that benchmark.

## User-defined statistics for repeated benchmarks
While having mean, median and standard deviation is nice, this may not be
enough for everyone. For example you may want to know what is the largest
observation, e.g. because you have some real-time constraints. This is easy.
The following code will specify a custom statistic to be calculated, defined
by a lambda function.

```c++
void BM_spin_empty(benchmark::State& state) {
  for (auto _ : state) {
    for (int x = 0; x < state.range(0); ++x) {
      benchmark::DoNotOptimize(x);
    }
  }
}

BENCHMARK(BM_spin_empty)
  ->ComputeStatistics("max", [](const std::vector<double>& v) -> double {
    return *(std::max_element(std::begin(v), std::end(v)));
  })
  ->Arg(512);
```

## Fixtures
Fixture tests are created by
first defining a type that derives from `::benchmark::Fixture` and then
creating/registering the tests using the following macros:

* `BENCHMARK_F(ClassName, Method)`
* `BENCHMARK_DEFINE_F(ClassName, Method)`
* `BENCHMARK_REGISTER_F(ClassName, Method)`

For Example:

```c++
class MyFixture : public benchmark::Fixture {};

BENCHMARK_F(MyFixture, FooTest)(benchmark::State& st) {
   for (auto _ : st) {
     ...
  }
}

BENCHMARK_DEFINE_F(MyFixture, BarTest)(benchmark::State& st) {
   for (auto _ : st) {
     ...
  }
}
/* BarTest is NOT registered */
BENCHMARK_REGISTER_F(MyFixture, BarTest)->Threads(2);
/* BarTest is now registered */
```

### Templated fixtures
Also you can create templated fixture by using the following macros:

* `BENCHMARK_TEMPLATE_F(ClassName, Method, ...)`
* `BENCHMARK_TEMPLATE_DEFINE_F(ClassName, Method, ...)`

For example:
```c++
template<typename T>
class MyFixture : public benchmark::Fixture {};

BENCHMARK_TEMPLATE_F(MyFixture, IntTest, int)(benchmark::State& st) {
   for (auto _ : st) {
     ...
  }
}

BENCHMARK_TEMPLATE_DEFINE_F(MyFixture, DoubleTest, double)(benchmark::State& st) {
   for (auto _ : st) {
     ...
  }
}

BENCHMARK_REGISTER_F(MyFixture, DoubleTest)->Threads(2);
```

## User-defined counters

You can add your own counters with user-defined names. The example below
will add columns "Foo", "Bar" and "Baz" in its output:

```c++
static void UserCountersExample1(benchmark::State& state) {
  double numFoos = 0, numBars = 0, numBazs = 0;
  for (auto _ : state) {
    // ... count Foo,Bar,Baz events
  }
  state.counters["Foo"] = numFoos;
  state.counters["Bar"] = numBars;
  state.counters["Baz"] = numBazs;
}
```

The `state.counters` object is a `std::map` with `std::string` keys
and `Counter` values. The latter is a `double`-like class, via an implicit
conversion to `double&`. Thus you can use all of the standard arithmetic
assignment operators (`=,+=,-=,*=,/=`) to change the value of each counter.

In multithreaded benchmarks, each counter is set on the calling thread only.
When the benchmark finishes, the counters from each thread will be summed;
the resulting sum is the value which will be shown for the benchmark.

The `Counter` constructor accepts two parameters: the value as a `double`
and a bit flag which allows you to show counters as rates and/or as
per-thread averages:

```c++
  // sets a simple counter
  state.counters["Foo"] = numFoos;

  // Set the counter as a rate. It will be presented divided
  // by the duration of the benchmark.
  state.counters["FooRate"] = Counter(numFoos, benchmark::Counter::kIsRate);

  // Set the counter as a thread-average quantity. It will
  // be presented divided by the number of threads.
  state.counters["FooAvg"] = Counter(numFoos, benchmark::Counter::kAvgThreads);

  // There's also a combined flag:
  state.counters["FooAvgRate"] = Counter(numFoos,benchmark::Counter::kAvgThreadsRate);
```

When you're compiling in C++11 mode or later you can use `insert()` with
`std::initializer_list`:

```c++
  // With C++11, this can be done:
  state.counters.insert({{"Foo", numFoos}, {"Bar", numBars}, {"Baz", numBazs}});
  // ... instead of:
  state.counters["Foo"] = numFoos;
  state.counters["Bar"] = numBars;
  state.counters["Baz"] = numBazs;
```

### Counter reporting

When using the console reporter, by default, user counters are are printed at
the end after the table, the same way as ``bytes_processed`` and
``items_processed``. This is best for cases in which there are few counters,
or where there are only a couple of lines per benchmark. Here's an example of
the default output:

```
------------------------------------------------------------------------------
Benchmark                        Time           CPU Iterations UserCounters...
------------------------------------------------------------------------------
BM_UserCounter/threads:8      2248 ns      10277 ns      68808 Bar=16 Bat=40 Baz=24 Foo=8
BM_UserCounter/threads:1      9797 ns       9788 ns      71523 Bar=2 Bat=5 Baz=3 Foo=1024m
BM_UserCounter/threads:2      4924 ns       9842 ns      71036 Bar=4 Bat=10 Baz=6 Foo=2
BM_UserCounter/threads:4      2589 ns      10284 ns      68012 Bar=8 Bat=20 Baz=12 Foo=4
BM_UserCounter/threads:8      2212 ns      10287 ns      68040 Bar=16 Bat=40 Baz=24 Foo=8
BM_UserCounter/threads:16     1782 ns      10278 ns      68144 Bar=32 Bat=80 Baz=48 Foo=16
BM_UserCounter/threads:32     1291 ns      10296 ns      68256 Bar=64 Bat=160 Baz=96 Foo=32
BM_UserCounter/threads:4      2615 ns      10307 ns      68040 Bar=8 Bat=20 Baz=12 Foo=4
BM_Factorial                    26 ns         26 ns   26608979 40320
BM_Factorial/real_time          26 ns         26 ns   26587936 40320
BM_CalculatePiRange/1           16 ns         16 ns   45704255 0
BM_CalculatePiRange/8           73 ns         73 ns    9520927 3.28374
BM_CalculatePiRange/64         609 ns        609 ns    1140647 3.15746
BM_CalculatePiRange/512       4900 ns       4901 ns     142696 3.14355
```

If this doesn't suit you, you can print each counter as a table column by
passing the flag `--benchmark_counters_tabular=true` to the benchmark
application. This is best for cases in which there are a lot of counters, or
a lot of lines per individual benchmark. Note that this will trigger a
reprinting of the table header any time the counter set changes between
individual benchmarks. Here's an example of corresponding output when
`--benchmark_counters_tabular=true` is passed:

```
---------------------------------------------------------------------------------------
Benchmark                        Time           CPU Iterations    Bar   Bat   Baz   Foo
---------------------------------------------------------------------------------------
BM_UserCounter/threads:8      2198 ns       9953 ns      70688     16    40    24     8
BM_UserCounter/threads:1      9504 ns       9504 ns      73787      2     5     3     1
BM_UserCounter/threads:2      4775 ns       9550 ns      72606      4    10     6     2
BM_UserCounter/threads:4      2508 ns       9951 ns      70332      8    20    12     4
BM_UserCounter/threads:8      2055 ns       9933 ns      70344     16    40    24     8
BM_UserCounter/threads:16     1610 ns       9946 ns      70720     32    80    48    16
BM_UserCounter/threads:32     1192 ns       9948 ns      70496     64   160    96    32
BM_UserCounter/threads:4      2506 ns       9949 ns      70332      8    20    12     4
--------------------------------------------------------------
Benchmark                        Time           CPU Iterations
--------------------------------------------------------------
BM_Factorial                    26 ns         26 ns   26392245 40320
BM_Factorial/real_time          26 ns         26 ns   26494107 40320
BM_CalculatePiRange/1           15 ns         15 ns   45571597 0
BM_CalculatePiRange/8           74 ns         74 ns    9450212 3.28374
BM_CalculatePiRange/64         595 ns        595 ns    1173901 3.15746
BM_CalculatePiRange/512       4752 ns       4752 ns     147380 3.14355
BM_CalculatePiRange/4k       37970 ns      37972 ns      18453 3.14184
BM_CalculatePiRange/32k     303733 ns     303744 ns       2305 3.14162
BM_CalculatePiRange/256k   2434095 ns    2434186 ns        288 3.1416
BM_CalculatePiRange/1024k  9721140 ns    9721413 ns         71 3.14159
BM_CalculatePi/threads:8      2255 ns       9943 ns      70936
```
Note above the additional header printed when the benchmark changes from
``BM_UserCounter`` to ``BM_Factorial``. This is because ``BM_Factorial`` does
not have the same counter set as ``BM_UserCounter``.

## Exiting Benchmarks in Error

When errors caused by external influences, such as file I/O and network
communication, occur within a benchmark the
`State::SkipWithError(const char* msg)` function can be used to skip that run
of benchmark and report the error. Note that only future iterations of the
`KeepRunning()` are skipped. For the ranged-for version of the benchmark loop
Users must explicitly exit the loop, otherwise all iterations will be performed.
Users may explicitly return to exit the benchmark immediately.

The `SkipWithError(...)` function may be used at any point within the benchmark,
including before and after the benchmark loop.

For example:

```c++
static void BM_test(benchmark::State& state) {
  auto resource = GetResource();
  if (!resource.good()) {
      state.SkipWithError("Resource is not good!");
      // KeepRunning() loop will not be entered.
  }
  for (state.KeepRunning()) {
      auto data = resource.read_data();
      if (!resource.good()) {
        state.SkipWithError("Failed to read data!");
        break; // Needed to skip the rest of the iteration.
     }
     do_stuff(data);
  }
}

static void BM_test_ranged_fo(benchmark::State & state) {
  state.SkipWithError("test will not be entered");
  for (auto _ : state) {
    state.SkipWithError("Failed!");
    break; // REQUIRED to prevent all further iterations.
  }
}
```

## Running a subset of the benchmarks

The `--benchmark_filter=<regex>` option can be used to only run the benchmarks
which match the specified `<regex>`. For example:

```bash
$ ./run_benchmarks.x --benchmark_filter=BM_memcpy/32
Run on (1 X 2300 MHz CPU )
2016-06-25 19:34:24
Benchmark              Time           CPU Iterations
----------------------------------------------------
BM_memcpy/32          11 ns         11 ns   79545455
BM_memcpy/32k       2181 ns       2185 ns     324074
BM_memcpy/32          12 ns         12 ns   54687500
BM_memcpy/32k       1834 ns       1837 ns     357143
```


## Output Formats
The library supports multiple output formats. Use the
`--benchmark_format=<console|json|csv>` flag to set the format type. `console`
is the default format.

The Console format is intended to be a human readable format. By default
the format generates color output. Context is output on stderr and the
tabular data on stdout. Example tabular output looks like:
```
Benchmark                               Time(ns)    CPU(ns) Iterations
----------------------------------------------------------------------
BM_SetInsert/1024/1                        28928      29349      23853  133.097kB/s   33.2742k items/s
BM_SetInsert/1024/8                        32065      32913      21375  949.487kB/s   237.372k items/s
BM_SetInsert/1024/10                       33157      33648      21431  1.13369MB/s   290.225k items/s
```

The JSON format outputs human readable json split into two top level attributes.
The `context` attribute contains information about the run in general, including
information about the CPU and the date.
The `benchmarks` attribute contains a list of every benchmark run. Example json
output looks like:
```json
{
  "context": {
    "date": "2015/03/17-18:40:25",
    "num_cpus": 40,
    "mhz_per_cpu": 2801,
    "cpu_scaling_enabled": false,
    "build_type": "debug"
  },
  "benchmarks": [
    {
      "name": "BM_SetInsert/1024/1",
      "iterations": 94877,
      "real_time": 29275,
      "cpu_time": 29836,
      "bytes_per_second": 134066,
      "items_per_second": 33516
    },
    {
      "name": "BM_SetInsert/1024/8",
      "iterations": 21609,
      "real_time": 32317,
      "cpu_time": 32429,
      "bytes_per_second": 986770,
      "items_per_second": 246693
    },
    {
      "name": "BM_SetInsert/1024/10",
      "iterations": 21393,
      "real_time": 32724,
      "cpu_time": 33355,
      "bytes_per_second": 1199226,
      "items_per_second": 299807
    }
  ]
}
```

The CSV format outputs comma-separated values. The `context` is output on stderr
and the CSV itself on stdout. Example CSV output looks like:
```
name,iterations,real_time,cpu_time,bytes_per_second,items_per_second,label
"BM_SetInsert/1024/1",65465,17890.7,8407.45,475768,118942,
"BM_SetInsert/1024/8",116606,18810.1,9766.64,3.27646e+06,819115,
"BM_SetInsert/1024/10",106365,17238.4,8421.53,4.74973e+06,1.18743e+06,
```

## Output Files
The library supports writing the output of the benchmark to a file specified
by `--benchmark_out=<filename>`. The format of the output can be specified
using `--benchmark_out_format={json|console|csv}`. Specifying
`--benchmark_out` does not suppress the console output.

## Debug vs Release
By default, benchmark builds as a debug library. You will see a warning in the output when this is the case. To build it as a release library instead, use:

```
cmake -DCMAKE_BUILD_TYPE=Release
```

To enable link-time optimisation, use

```
cmake -DCMAKE_BUILD_TYPE=Release -DBENCHMARK_ENABLE_LTO=true
```

If you are using gcc, you might need to set `GCC_AR` and `GCC_RANLIB` cmake cache variables, if autodetection fails.
If you are using clang, you may need to set `LLVMAR_EXECUTABLE`, `LLVMNM_EXECUTABLE` and `LLVMRANLIB_EXECUTABLE` cmake cache variables.

## Linking against the library

When the library is built using GCC it is necessary to link with `-pthread`,
due to how GCC implements `std::thread`.

For GCC 4.x failing to link to pthreads will lead to runtime exceptions, not linker errors.
See [issue #67](https://github.com/google/benchmark/issues/67) for more details.

## Compiler Support

Google Benchmark uses C++11 when building the library. As such we require
a modern C++ toolchain, both compiler and standard library.

The following minimum versions are strongly recommended build the library:

* GCC 4.8
* Clang 3.4
* Visual Studio 2013
* Intel 2015 Update 1

Anything older *may* work.

Note: Using the library and its headers in C++03 is supported. C++11 is only
required to build the library.

## Disable CPU frequency scaling
If you see this error:
```
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
```
you might want to disable the CPU frequency scaling while running the benchmark:
```bash
sudo cpupower frequency-set --governor performance
./mybench
sudo cpupower frequency-set --governor powersave
```

# Known Issues

### Windows with CMake

* Users must manually link `shlwapi.lib`. Failure to do so may result
in unresolved symbols.

### Solaris

* Users must explicitly link with kstat library (-lkstat compilation flag).
Open Enclave pkg-config files:
==============================

This directory defines the following **pkg-config** files.

```
oeenclave-gcc.pc
oeenclave-g++.pc
oeenclave-clang.pc
oeenclave-clang++.pc
oehost-gcc.pc
oehost-g++.pc
oehost-clang.pc
oehost-clang++.pc
```

These files are installed into the following directory.

```
$ /usr/local/share/pkgconfig
```

Once installed, **pkg-config** may be used to obtain compiler and linker flags 
sufficient for building enclave applications with the GCC or Clang compiler.

Setting **PKG_CONFIG_PATH**
---------------------------

If **Open Enclave** is not installed with the default prefix (**/usr/local**),
the **PKG_CONFIG_PATH** variable must be set relative to that custom prefix.

Building enclave applications:
------------------------------

To build an enclave application with the Clang C compiler, use the following 
commands.

```
cflags=`pkg-config oeenclave-clang --cflags`
libs=`pkg-config oeenclave-clang --libs`
$ clang-7 ${cflags} -o enc enc.c ${libs}
```

To build an enclave application with the Clang C++ compiler, use these commands.

```
cxxflags=`pkg-config oeenclave-clang++ --cflags`
libs=`pkg-config oeenclave-clang++ --libs`
$ clang++-7 ${cxxflags} -o enc enc.cpp ${libs}
```

Building host applications:
---------------------------

To build a host application with the Clang C compiler, use the following 
commands.

```
cflags=`pkg-config oehost-clang --cflags`
libs=`pkg-config oehost-clang --libs`
$ clang-7 ${cflags} -o host host.c ${libs}
```

To build a host application with the Clang C++ compiler, use these commands.

```
cflags=`pkg-config oehost-clang++ --cflags`
libs=`pkg-config oehost-clang++ --libs`
$ clang++-7 ${cflags} -o host host.c ${libs}
```
tests
=====

# Overview:

This directory contains dedicated unit tests for Open Enclave. To run all
tests Open Enclave tests, type the following commands to build and run the
tests from the corresponding CMake output folder.

```
build$ make
build$ ctest
```

To run only specific tests, go to the corresponding subtree in the build
directory and run ctest from there. For example,

```
build/tests/echo$ make
```


This builds and runs all the tests. For libcxx a small subset is the default,
the complete one is very slow to build and run. To enable the full set,
set the ENABLE_FULL_LIBCXX_TESTS cmake variable as follows:

```
build$ cmake .. -DENABLE_FULL_LIBCXX_TESTS=1
build$ make
build$ ctest

```

# Test mechanics

OE_TEST() is used as a simple check, and is the general paradigm in all tests.

Some tests can only be run in certain environments and fail in others. It is
recommended for such tests to check the environment, and abort the test
signalling a "did not run" state to ctest (rather than failing). To signal
"did not run", such tests should return with an exit code of 2. ctest
evaluates this specifically.

# Testing on Windows [Work in progress]

Refer to [Getting Started on Windows](/docs/GettingStartedDocs/GettingStarted.Windows.md) for
instructions on testing Linux-built enclaves with Windows-built host apps.


oe-gdb tests
=====================

Test suite locking down supported debugging capabilities in both
Debug and RelWithDbgInfo builds.

1. Set pending breakpoing in an yet to be loaded enclave.
2. Multiple breakpoints.
3. Adjacent breakpoints in successive lines.
4. Read variable values.
5. Set variable values.
6. Call functions with the enclave.
Libcxxrt tests
=============

This directory run libcxxrt tests in an enclave enviornment. It does
this by repeatedly building and running the enclave located under the 'enc'
directory for each unit test found in tests.supported.

The unit tests are partitioned into three files:

* tests.supported -- unit tests that work
* tests.unsupported -- unit tests that are not supported

To run all the tests, type the following command:

```
# make tests
```

As tests are fixed, they should be moved from tests.broken to tests.supported.

As tests are determined to be unsupportable, they should be moved from
tests.broken to tests.unsupported.

Note
====

libcxxrt basically contains two tests:

  1. test_foreign_exceptions.cc

In case of test_foreign_exception, it is tested using the return value from
the main() function and hence conclude whether test is success or failure.

  2. test.cc (contains test_guard.cc, test_typeinfo.cc and test_exception.cc)

In case of test.cpp, the main(), which is of void type, will generate a
sequence of test logs regarding test_guard, test_typeinfo and test_exception.

Test is compiled in two different ways, one using **libcxxrt** and the other
using standard system depended libraries (i.e., it will use **libsupcxx** ABI
library instead of libcxxrt). It then generates a log file for each version of
the test and compares them with each other. The test is marked as passing only
if both log files are identical.

Since these tests are dependent comparing test-generated logs, test files such
as enc.cpp and host.cpp must not print any messages to stdout, as these messages
will not match the comparison log that does not include these additional messages.

For the enclave versions of these tests, the following additional modifications
were needed:

* Separated test_guard.cpp, test_typeinfo.cpp and test_exception.cpp from
test.cpp so that each test can be executed individually using the test
configuration files tests.supported/unsupported.

* Each test (test_guard.cc, test_typeinfo.cc and test_exception.cc) is compiled
against **libcxxrt** in both cases. Instead of the test comparison being
between the use of **libcxxrt** and **libsupcxx** as in the normal version,
the enclave version compares the log of the test built against **libcxxrt
using OE dependencies** (e.g. OE version of libunwind) with the log of the
one built against **libcxxrt and standard library dependencies**.


To test, test.cc on Windows, perform following steps in given order...
==========================================================================

Select Linux-Debug configuration and build libcxxrt logs.

Select x64-Debug-tests configuration and build and run libcxxrt tests...

2.1. Libcxxrt Signed .so files will be copied to windows project binary folder .

2.2 After 2.1 is successful, Linux Libcxxrt log files will be copied to windows
project binary folder.

2.3 Libcxxrt log files will be generated using run.bat file in windows project binary folder.

2.4 Linux and Windows Logs will be compared to pass the test.

Note that test_exception.cc requires std::uncaught_exceptions(), which requires
cpp standard **stdc++17** (or above) with compiler version **GCC version 6 or
Clang 3.8** (or above). But Open Enclave currently support only **GCC version
5 with cpp standard stdc++14** (at the most). Hence, test_exception.cc is not
currently supported in Open Enclave.

oe_get_report API tests
=====================

Test behavior of oe_get_report, oe_parse_report, oe_verify_report APIs:

- **Host Side**
  1. *TestLocalReport* : Tests optParams scenarios (null, valid target info), small report buffer scenarios, and succeeding invocations.
  2. *TestRemoteReport* : Tests null optParams, small report buffer scenarios, and succeeding invocations.
  3. *TestLocalVerifyReport*: Tests oe_verify_report on locally attested reports. Negative test.
  4. *TestRemoteVerifyReport*: Tests oe_verify_report on remote attested reports. 


- **Enclave side**
  1. *TestLocalReport* : Tests reportData scenarios (null, partial, full), optParams scenarios (null, valid target info), small report buffer scenarios, and succeeding invocations.
  2. *TestRemoteReport* : Tests reportData scenarios (null, partial, full), null optParams, small report buffer scenarios, and succeeding invocations.
  3. *TestLocalVerifyReport*: Tests oe_verify_report on locally attested reports. No, partial and full report data scenarios. Negative test.
  4. *TestRemoteVerifyReport*: Tests oe_verify_report on remote attested reports. Tests reportData scenarios (null, partial, full).

**Other tests**
  1. *TestVerifyTCBInfo*: Tests tcbInfo JSON processing. Positive and negative tests. Schema validation.
  2. *TestIso861Time*, *TestIso861TimeNegative*: Positive and negative tests oe_datetime_t.
  3. test_minimum_issue_date: Tests that setting the minimum crl, tcb issue date has the desired effect on attestation.
  
  
Libmbed tests
=============

This directory run ARM Mbedtls tests in an enclave enviornment. It does
this by repeatedly building and running the enclave located under the 'enc' 
directory for each unit test found in tests.supported.

The unit tests are partitioned into three files:

* tests.supported -- unit tests that work
* tests.broken -- unit tests that are broken
* tests.unsupported -- unit tests that are not supported

To run all the tests, type the following command:

```
# make tests
```

As tests are fixed, they should be moved from tests.broken to tests.supported.

As tests are determined to be unsupportable, they should be moved from
tests.broken to tests.unsupported.

## LIBCIO 
    A Wrapper library implementation for the FILE I/O operations. Its a supportive library for the enclave
    applications such that any file operation comes, it can perform the same on host side and return to enclave.
    This library is a developed completly beased on OCALL implementation  

This directory tests the usage of enclave properties, which may be defined
in one of two ways:

- Using the OE_SET_ENCLAVE_SGX macro (for unsigned debug enclaves)
- Using the OESIGN tool (for signed enclaves)

In both cases, the enclave properties are written to a special enclave
properties section (.oeinfo) within the enclave image.

The enclave loader is able to load unsigned debug images, by use of the
OE_SET_ENCLAVE_SGX macro.

The propshost program tests both of these scenarios. It is run once for 
the unsigned case and once for the signed case as follows.

```
# ./host/propshost ./enc/propsenc unsigned
# ./host/propshost ./enc/propsenc.signed signed
```

These tests check that the enclave properties contain the expected values.
cppException tests
============

This directory runs cpp exception tests within enclave.
All test functions are included in enc/cppException.cpp.

# Following scenarios are tested

* Basic types (char, int, string, class, derived class from std::exception) can
be thrown and caught correctly.
* Ellipsis catch can catch all kinds of cpp exception.
* Handlers for a given try block are examined in order of their appearance.
* Find the matching handler through nested try blocks.
* Find the matching catch handler through call stack
* Re-throw the same exception in the catch clause.
* New exception can be thrown in catch clause.
* Stack local unwind.
* Stack global unwind.
* The exception happens in function-try-block is handled.
* Unhandled exception.
This directory runs tests relating to enclave creation via OCALL.

Following scenarios are tested:

* The created enclave can be used by the host for ECALLs, OCALLs, and enclave termination.
* Same as case #1, but testing if the enclave can use the OCALL-created enclave.

This directory tests enclave memory management with the following tests:
  - Checking that basic uses of malloc and free work.
  - Checking that malloc returns pointers within the enclave boundary.
  - Stress test the malloc family set of functions by rapid allocation
    and freeing.
  - Stress test the malloc family functions by rapid allocation and freeing
    in a multi-threaded context.
This directory runs tests relating to debug-mode and signed enclaves.

There are 8 different cases for debug/signed enclaves which depend on the following settings:
  - If the enclave is signed or unsigned.
  - If the enclave is debug mode or not.
  - If the flags parameter in `oe_create_enclave` has the debug bit set or not.
  
The table demonstrates the expected value of the 8 cases:

| Enclave Signed? | Enclave Debug? | Flags Debug Bit Set? | Result                |
| --------------- |----------------| ---------------------|-----------------------|
| Yes             | Yes            | Yes                  | Success               |
| Yes             | Yes            | No                   | Sucesss*              |
| Yes             | No             | Yes                  | Fail (OE_DOWNGRADE)   |
| Yes             | No             | No                   | Success*              |
| No              | Yes            | Yes                  | Success**             |
| No              | Yes            | No                   | Fail**                |
| No              | No             | Yes                  | Fail (OE_DOWNGRADE)** |
| No              | No             | No                   | Fail**                |

\* Requires Coffeelake (SGX-1 with Flexible Launch Control)  
\*\* Requires Linux

Note that these tests are skipped when run in simulation mode.
Libunwind tests
=============

This directory runs the libunwind tests in an enclave enviornment. It does
this by repeatedly building and running the enclave located under the 'enc' 
directory for each unit test found in tests.supported.

The unit tests are partitioned into three files:

* tests.all
* tests.supported -- unit tests that work
* tests.unsupported -- unit tests that are not supported

To run all the tests, type the following command:

```
# make tests
```

Note
====
libunwind basically contains 33 tests which are listed in the tests.all file.
Out of these 33 tests, 11 tests can be compiled and run properly and are listed
in the test.supported file. The remaining 22 tests were moved to the
test.unsupported file.

All the tests in test.supported can be compiled and run proprely in debug 
mode("-O2"). In release mode("-O3"), a couple of tests (Gtest-exc and Ltest-exc)
were failing. Those tests were also failing in system dependent side when
compiled with -O3. By adding GCC flag "fno-inline-function" with -O3 flag
("-O3 -fno-inline-function") both system dependent tests as well as enclave 
tests were able to run sucessfully in release mode.

The tests listed in tests.unsupported file uses the features that enclave 
don't support like signals, pthreads, timers, dynamic loading etc.

Out of the 22 unsupproted tests, 4 of them are bash scripts. They are

* run-coredump-unwind
* run-check-namespace
* run-ptrace-mapper
* run-ptrace-misc

The detailed list of the unsupported tests with their features that are not
supported are given below :

SL.No | Tests_Name  | Compile? | Run? | Comments |
:---:|:---:|:---:|:---:|:---:|
1  | Gtest-bt | No | No | undefined reference to 'kill', 'sigaltstack', 'sigaction', 'signal' |
2  | Gtest-concurrent   | No |  No | undefined reference to 'signal', 'pthread_kill', 'pthread_attr_init', 'pthread_attr_setstacksize' |
3  | Gtest-dyn1 | No | No | undefined reference to 'mprotect', `signal' |
4  | Gtest-resume-sig | No | No | undefined reference to 'sigemptyset', 'sigaddset', 'sigprocmask', 'signal', 'kill', 'sigaction' |
5  | Gtest-resume-sig-rt| No | No | undefined reference to 'sigemptyset', 'sigaddset', 'sigprocmask', 'signal', 'kill', 'sigaction' | 
6  | Gtest-trace | No | No | undefined reference to 'kill', 'sigaltstack', 'sigaction', 'signal' |
7  | Ltest-bt | No |  No | undefined reference to 'kill', 'sigaltstack', 'sigaction', 'signal' |
8  | Ltest-concurrent | No | No |undefined reference to 'signal', 'pthread_kill', 'pthread_attr_init', 'pthread_attr_setstacksize' |
9  | Ltest-dyn1 | No | No | undefined reference to 'mprotect', 'signal' |
10 | Ltest-nocalloc | No | No | undefined reference to `dlsym' |
11 | Ltest-nomalloc | No | No | undefined reference to `dlsym' |
12 | Lrs-race | Yes | No | test calls pthread_create() and gets aborted |
13 | Ltest-resume-sig | No | No | undefined reference to 'sigemptyset', 'sigaddset', 'sigprocmask', 'signal', 'kill', 'sigaction' |
14 | Ltest-resume-sig-rt | No | No |undefined reference to 'sigemptyset', 'sigaddset', 'sigprocmask', 'signal', 'kill', 'sigaction' |
15 | Ltest-trace | No | No | undefined reference to 'kill', 'sigaltstack', 'sigaction', 'signal' |
16 | run-coredump-unwind | No | No | execinfo.h is not supported |
17 | run-check-namespace | No | No | this test will check whether some specific symbols are there in the generated libraries or not |
18 | run-ptrace-mapper | No | No | depends on test-ptrace |
19 | run-ptrace-misc | No | No | depends on test-ptrace |
20 | test-async-sig | No | No | undefined reference to 'setitimer', 'sigaction' |
21 | test-ptrace | No | No | undefined reference to 'kill', 'fork', 'open', 'dup2', 'ptrace', 'execve', 'wait4' |
22 | test-setjmp | No | No | undefined reference to 'sigsetjmp', 'sigaddset', 'sigprocmask', 'siglongjmp' 'sigemptyset', 'kill', 'sigaction' |

run-coredump-unwind does not have support for execinfo.h which declares the functions backtrace, backtrace_symbols, backtrace_symbols_fd.
Currently enc/CMakeLists.txt have  support  for the tests in tests.supported.
To compile any of the test from test.unsupported you have to add the corresponding support libraries in the enc/CMakeLists.txt.

oeedger8r tests
=====================

Test constructs supported by oeedger8r .

- **edltestutils.h**
  1. *Purpose*: Contains utilities to lock down types of the marshalling struct and to track memory allocation during parameter marshaling.

- **mytypes.h**
  1. *Purpose*: Contains types used for testing "foreign" types in EDL.

- **array.edl**
  1. *Purpose*: Test ecalls and ocalls for in, in-out, out compinations for single, double, triple dimensional arrays
      for all basic types.
  2. *enc/teststring.cpp* : Defines ecall implementations. Also test_array_edl_ocalls function to test ocalls.
  3. *host/teststring.cpp*: Defines ocall implementations. Also test_array_edl_ecalls function to test ecalls.  

- **basic.edl**
  1. *Purpose* : Test ecalls and ocalls using basic types as parameters and return types.
  2. *enc/testbasic.cpp* : Defines ecall implementations. Also test_basic_edl_ocalls function to test ocalls.
  3. *host/testbasic.cpp*: Defines ocall implementations. Also test_basic_edl_ecalls function to test ecalls.

- **enum.edl**
  1. *Purpose* : Test ecalls and ocalls for enum type defined in edl. Test pass-by value, return, and all pointer semantics.
  2. *enc/testbasic.cpp* : Defines ecall implementations. Also test_enum_edl_ocalls function to test ocalls.
  3. *host/testbasic.cpp*: Defines ocall implementations. Also test_enum_edl_ecalls function to test ecalls.

- **foreign.edl**
  1. *Purpose* : Test ecalls and ocalls for foreign types. Foreign type is a type that is defined outside of EDL and is not a primitive type. Test pass by value and isary attributes. Also when an explicit * is used, test all pointer semantics.
     Also if \* is not used but isptr attribute is specified (say for typedef int \* my_type), then pointer semantics are allowed.
  2. *enc/testbasic.cpp* : Defines ecall implementations. Also test_foreign_edl_ocalls function to test ocalls.
  3. *host/testbasic.cpp*: Defines ocall implementations. Also test_foreign_edl_ecalls function to test ecalls.

- **pointer.edl**
  1. *Purpose* : Test ecalls and ocalls for pointer parameters types. Test in, in-out, out attributes for all primitive types.
      By default the parameter is expected to point to one element. If 'count' attribute is specified, then the
      parameter is expected to point to count number of elements. If 'size' attribute is specified then the parameter is
      expected to point to 'size' bytes whether size is a multiple of element-size or not.
      Also test 'user_check' attribute.
  2. *enc/testbasic.cpp* : Defines ecall implementations. Also test_foreign_edl_ocalls function to test ocalls.
  3. *host/testbasic.cpp*: Defines ocall implementations. Also test_foreign_edl_ecalls function to test ecalls.

- **string.edl**
  1. *Purpose*: Test ecalls and ocalls for [string, in], [string, in, out] attribute combinations.
  2. *enc/teststring.cpp* : Defines ecall implementations. Also test_string_edl_ocalls function to test ocalls.
  3. *host/teststring.cpp*: Defines ocall implementations. Also test_string_edl_ecalls function to test ecalls.

- **struct.edl**
  1. *Purpose* : Test ecalls and ocalls for struct type defined in edl. Test pass-by value, return, and all pointer semantics.
     Also test nesting of structs.
  2. *enc/testbasic.cpp* : Defines ecall implementations. Also test_struct_edl_ocalls function to test ocalls.
  3. *host/testbasic.cpp*: Defines ocall implementations. Also test_struct_edl_ecalls function to test ecalls.
This directory tests rapid enclave creation and termination. It has the following tests:
* Creating many enclaves and terminating them in a sequential order.
* Creating many enclaves simultaneously and then terminating all of them at once.
* Creating many enclaves and terminating them in a multithreaded program.

This directory tests if global initializers work in the enclave.
abortStatus tests
============

This directory runs enclave abort status tests.

# Following scenarios are tested

* Host gets the abort status when enclave call oe_abort to abort itself.
* Host gets the abort status when un-handled hardware exception happens inside 
enclave.
* Enclave is aborted in one thread, other active enclave threads can return to 
host with correct abort status, and both enclave thread and host thread can exit
gracefully.
* Same case as scenario 3, but the enclave is aborted due to an un-handled
hardware exception.
C++11 std::thread tests
=======================

Test various C++11 synchronization primitives provided for std::thread.
- **std::mutex**  and **std::recursive_mutex**
  1. *TestMutex* : Tests basic locking, unlocking, recursive locking.
  1. *TestThreadLockingPatterns* : Tests various locking patterns A/B, A/B/C, A/A/B/C etc in a tight-loop across multiple threads.


- **std::condition_variable**, **std::unique_lock**, **std::lock_guard**
  1. *TestCond* : Tests basic condition variable use.
  1. *TestThreadWakeWait* : Tests internal _ThreadWakeWait function.
  1. *TestCondBroadcast* : Tests notify_all function in a tight-loop to verify that all waiting threads are woken.

Uses and tests the **std::atomic types** as well.
ECall/Ocall tests
=================

Testing various functionality around ecalls/ocalls:
- verify OCall can be executed in global initializers
- verify non-exported enclave functions cannot be called
- verify threads are actually executed in parallel (not round-robin nested on ocall)
  + multi-thread in enclave
  + multi-enclave / multi-thread

libcxx tests
============

This directory runs each LLVM libcxx unit test from within an enclave. It does
this by repeatedly building and runing the enclave located under the 'enc' 
directory for each unit test found in tests.supported.

The unit tests are partitioned into three files:

* tests.supported -- unit tests that work
* tests.broken -- unit tests that are broken
* tests.unsupported -- unit tests that are not supported

To run all the tests, type the following command:

```
# make tests
```

As tests are fixed, they should be moved from tests.broken to tests.supported.

As tests are determined to be unsupportable, they should be moved from
tests.broken to tests.unsupported.



Additional Crypto API tests
===========================

==Preparing Test Data==

All the certificates and certificate revocation lists needed by this test are dynamically generated by the custom commands embedded inside 
crypto_crls_cert_chains/host CMakeLists.txt 
  
==List of Tests==

  1. test_cert_chain_positive
       Asserts the following condition: "In a valid cert chain, each certificate's issuer is also present in the chain".
       Tests various ordering, duplicates, two and three level chains.
  2. test_cert_chain_negative: Negative tests involving missing certs etc.
  3. test_crls.
      1. Assert that verify succeeds when no crls are passed.
      2. Assert that when crls are passed, but don't revoke certs, verify succeeds.
      3. Assert that when crl revoking leaf is passed, verify fails.
      4. Assert that when crl revoking intermediate is passed in, verify fails. (This behavior is currently broken.)
      5. Assert that when only one crl is passed in (either root or intermediate), verify fails. (This behavior is currently broken.)

gethostenclave:
===============

This function tests the new optional **enclave** OCALL parameter.

The host creates three instances of the same enclave and then initiates
the following sequence of calls.

    - enclave-1:test_enclave_param()
    - host:callback_1
    - enclave-2:test_enclave_param()
    - host:callback_2
    - enclave-3:test_enclave_param()
    - host:callback_3

bigmalloc
=========

This test verifies creation of an enclave with 16 gigabytes of heap. The
enclave then attempts to allocate 99% of its heap with **oe_malloc()**.

This test requires approximately 64 gigabytes of system memory (RAM plus swap
space), else the test exits (with success) with a warning.

On Linux systems, use the following command to determine total system memory.

```
free -m
```

If the sum of RAM and swap space is less than 64 gigabytes, then add additional
swap space with the following commands.

```
# Create a 64 GB file that is filled with zeros.
dd if=/dev/zero of=/swapfile bs=1024 count=64M

# Initialize with a swap file system.
mkswap /swapfile

# Make the swap file readable by root.
chmod 0600 /swapfile

# Add the swap space.
swapon /swapfile
```
Thread library tests
=====================

Test various OE synchronization primitives:
- **oe_mutex_t**
  1. *TestMutex* : Tests basic locking, unlocking, recursive locking.
  1. *TestThreadLockingPatterns* : Tests various locking patterns A/B, A/B/C, A/A/B/C etc in a tight-loop across multiple threads.


- **oe_cond_t**
  1. *TestCond* : Tests basic condition variable use.
  1. *TestThreadWakeWait* : Tests internal _ThreadWakeWait function.
  1. *TestCondBroadcast* : Tests oe_cond_broadcast function in a tight-loop to assert that all waiting threads are woken.


  **oe_rwlock_t**
  1. *TestReadersWriterLock* : Tests readers-writer lock invariants by launching multiple reader and writer threads racing against each other. Asserts that multiple/all readers can be simultaneously active, only one writer is active,  readers and writers are never simultaneously active.

This directory builds test enclaves for both OE threads and pthreads.
Thread Local Storage Tests
=====================

The following constructs are tested:

1. GNU __thread keyword
2. C++11 thread_local keyword
3. Simple types 
4. Types with constructors
5. Types with destructors
6. extern thread_local variables with complex initializers.
7. Reinitialization of tls via thread recreation.
8. Test exported and non-exported thread-locals. These have different implementations.

Disabled in simulation mode since simulation mode needs
completely different implementation of tls variables.
libc tests
==========

This directory runs the MUSL libc unit tests. It reads **tests.cmake** and 
generates a wrapper (in the build directory) for each of the tests in this file.

All unit tests are all listed in **tests.cmake** in the following sections:

* Supported -- unit tests that work.
* Broken -- unit tests that are broken.
* Unsupported -- unit tests that are unsupported.

Tests determined to be unsupportable should be moved to the broken section.
Test for Quoting Enclave Identity tests
=====================

This QE Identity test oe_parse_qe_identity_info_json() internal routine with different json inputs.
host
====

This directory contains the sources for the oehost library. This library
supports creating, invoking, and terminating enclaves.

# Enclave Layout

The host creates an enclave image with the following layout (for details, see
see [create.c](create.c)).

        +----------------------------------------+
        | Text pages:                            |
        |     _start() - enclave entry point     |
        |     oe_exit() - enclave entry routine  |
        +----------------------------------------+
        | Relocation pages:                      |
        |     (contains data relocations)        |
        +----------------------------------------+
        | ECALL address pages:                   |
        {     (ECALL virtual adddresses)         |
        +----------------------------------------+
        | Data pages:                            |
        |     __oe_numPages                      |
        |     __oe_virtualBaseAddr               |
        |     __oe_BaseRelocPage                 |
        |     __oe_numRelocPages                 |
        |     __oe_BaseECallPage                 |
        |     __oe_numECallPages                 |
        |     __oe_BaseHeapPage                  |
        |     __oe_numHeapPages                  |
        +----------------------------------------+ <--+
        | Guard page                             |    |
        +----------------------------------------+    |
        | Stack pages                            |    |
        +----------------------------------------+    |
        | Guard page                             |    |
        +----------------------------------------+    |
        | Thread Control Structure (TCS) Page    |    |
        |     state: 0 = available               |    |
        |     oentry - vaddress of _start()      |    |- Thread context
        |     fsbase - vaddress of FS segment    |    |  (one per TCS)
        |     gsbase - vaddress of GS segment    |    |
        +----------------------------------------+    |
        | Set Asside Area (SSA Slot 1) Page      |    |
        +----------------------------------------+    |
        | Set Asside Area (SSA Slot 2) Page      |    |
        +----------------------------------------+    |
        | Guard page                             |    |
        +----------------------------------------+    |
        | Segment Page: (FS or GS)               |    |
        |     (contains thread data structure)   |    |
        +----------------------------------------+    |
        | Thread specific data (TSD) Page        |    |
        +----------------------------------------+ <--+
        | Padding Pages (must be a power of two) |
        +----------------------------------------+

# clangw : Clang Compiler Wrapper for building enclaves

clangw takes a mix of msvc and gcc/clang command-line agruments generated
by cmake on windows, transforms them to their clang equivalents and
then passes them along to clang.

It is similar to clang-cl. However clang-cl cannot be used for 
cross-compiling since it also does not understand options like -fPIC,
-fvisibility=hidden etc.

# llvm-arw: Wrapper for llvm-ar
Ninja generator uses response files when the command line is long.
However it uses \ directory separator within the response files, which
llvm-ar does not handle. llvm-arw transforms all \ to / in both command line
as well as in response files specified in the command line.enclave
=======

This directory contains the sources for the oeenclave library, which implements
the enclave extras, which depend on mbedtls and oelibc. The main parts include:

- Certificate management ([cert.c](cert.c))

- EC key management ([ec.c](ec.c))

- RSA key management ([rsa.c](rsa.c))

- Entropy ([random.c](random.c))

- SHA hash management ([sha.c](sha.c))

core
====

This directory contains the sources for the oecore library, which implements
the enclave intrinsics. The main parts include:

- Enclave entry ([main.S](main.S)) and exit ([exit.S](exit.S)) functions

- Enclave initialization ([init.c](init.c))

- ECALL and OCALL dispatching logic ([calls.c](calls.c))

- The thread data (TD) structure ([td.c](td.c))

- Spinlock implementation ([spinlock.c](spinlock.c))

- Enclave threads implementation ([thread.c](thread.c))

- Functions for testing enclave memory boundaries ([memory.c](memory.c))

- Globals set during enclave signing and loading ([globals.c](globals.c))

- Host calls ([hostcalls.c](hostcalls.c))

- Standard-like string functions ([string.c](string.c))

- Assertion implementation ([assert.c](assert.c))

- Enclave setjmp and longjmp functions ([jump.c](jump.c))

- Functions for report creation (ENCLU.EREPORT) ([report.c](report.c))

- Enclave sbrk() implementation ([sbrk.c](sbrk.c))

enclave/core/dlmalloc
=====================

This directory contains dummy standard C headers needed to compile dlmalloc.c
(included by enclave/core/malloc.c).
# Open Enclave SDK Samples

All the samples that come with the Open Enclave SDK installation share similar directory structure and build instructions. The section contains general information on how to setup/build/sign/run all samples. It's important that you read information on this page before jumping into any individual sample.

## Common Sample information

### Prepare samples

Building samples involves writing files into the working directory, which is not allowed in `/opt` unless it's running in the context of superuser (`sudo`).

To avoid this `sudo` requirement, you may want to first copy them to a user directory of your choice then build and run on those local copy.

For example, assuming Open Enclave SDK is installed to the default location `/opt/openenclave`:

```bash
cp -r /opt/openenclave/share/openenclave/samples ~/mysamples
```

### How Sample source code directories were structured

Open Enclave SDK helps developers build enclave applications. An enclave application is partitioned into an untrusted component (called a host) and a trusted component (called an enclave). An enclave is a secure container whose memory (text and data) is protected from access by outside entities, including the host, privileged users, and even the hardware. All functionality that needs to be run in a Trusted Execution Environment (TEE) should be compiled into the enclave binary. The enclave may run in an untrusted environment with the expectation that secrets will not be compromised. A host is a normal user mode application that loads an enclave into its address space before starting interacting with an enclave. 

![Sample components diagram](sampledirstructure.png)

All the samples that come with the Open Enclave SDK installation are all structured into two subdirectories (one for enclave and one for host) accordingly.

| Files/dir    |  contents                                   |
|:-------------|---------------------------------------------|
| Makefile     | Makefile for the whole samples              |
| ./enc        | Files needed for building the sample enclave|
| ./host       | Files needed for building the host          |

For example:

```bash
/home/yourusername:~/openenclave/share/openenclave/samples/helloworld$ ls -l
total 12
drwxr-xr-x 2 yourusername yourusername 4096 Aug 16 13:59 enc
drwxr-xr-x 2 yourusername yourusername 4096 Aug 16 13:59 host
-rw-r--r-- 1 yourusername yourusername  245 Aug 16 13:57 Makefile
```

### How to build and run samples

Each sample comes with a set of simple Makefiles to simplify the sample building process, which involves building and signing
binaries.

#### Source the openenclaverc file (Required)

Before building any samples, you need to source the `openenclaverc` file to setup environment variables for sample building. `openenclaverc` file can be found in  the `share/openenclave` subdirectory of the package installation destination.

You can use `.` in Bash to `source`:

```bash
. <package_installation_destination>/share/openenclave/openenclaverc
```

For example, if your package_installation_destination is /opt/openenclave:

```bash
. /opt/openenclave/share/openenclave/openenclaverc
```

Note: You will get error messages like the following if this sourcing step was skipped.

```sh
make[2]: Entering directory '.../openenclave/samples/helloworld/enc`
Package oeenclave-clang was not found in the pkg-config search path.
Perhaps you should add the directory containing `oeenclave-clang.pc`
```

#### Build samples

To build a sample, change directory to your target sample directory and run `make build` to build the sample
and run `make run` to run it.

For example:

```bash
username@yourVMname:~/openenclave/share/openenclave/samples$ cd helloworld/
username@yourVMname:~/openenclave/share/openenclave/samples/helloworld$ ls enc  host  Makefile

username@yourVMname:~/openenclave/share/openenclave/samples/helloworld$ make build
 ...
username@yourVMname:~/openenclave/share/openenclave/samples/helloworld$ make run host/helloworldhost ./enc/helloworldenc.signed
Enclave called into host to print: Hello World!
```

For details on how to configure build and sign options, refer to [Enclave Building and Signing](https://github.com/Microsoft/openenclave/blob/master/docs/GettingStartedDocs/buildandsign.md).

## Samples

The following samples demonstrate how to develop enclave applications using OE APIs. It's recommended to go through the following samples in the order listed.

#### [HelloWorld](helloworld/README.md)

- Minimum code needed for an OE app
- Help understand the basic components an OE application
- Demonstrate how to build, sign, and run an OE image

#### [File-Encryptor](file-encryptor/README.md)

- Shows how to encrypt and decrypt data inside an enclave
- Uses AES mbedTLS API to perform encryption and decryption

#### [Data-Sealing](data-sealing/README.md)

- Introduce OE sealing and unsealing features 
- Demonstrate how to use OE sealing APIs
- Explore two supported seal polices
  - OE_SEAL_POLICY_UNIQUE
  - OE_SEAL_POLICY_PRODUCT

#### [Remote Attestation](remote_attestation/README.md)

- Explain how OE attestation works
- Demonstrate an implementation of remote attestation between two enclaves running on different machines

#### [Local Attestation](local_attestation/README.md)

- Explain the concept of OE local attestation
- Demonstrate an implementation of local attestation between two enclaves on the same VM


# The Remote Attestation Sample

This sample demonstrates how to do remote attestation between two enclaves and establish a secure communication channel for exchanging messages between them.

It has the following properties:

- Written in C++
- Demonstrates an implementation of remote attestation
- Use of mbedTLS within the enclave
- Use Asymmetric / Public-Key Encryption to establish secure communications between two attesting enclaves
- Enclave APIs used:
  - oe_get_report
  - oe_verify_report,
  - oe_is_within_enclave

**Note: Currently this sample only works on SGX-FLC systems.** The underlying SGX library support for end-to-end remote attestation is available only on SGX-FLC system. There is no plan to back port those libraries to either SGX1 system or software emulator.

## Attestation primer

### What is Attestation

Attestation is the process of demonstrating that a software component (such as an enclave image) has been properly instantiated on an Trusted Execution Environment (TEE, such as the SGX enabled platform).

A successfully attested enclave proves:

- The enclave is running in a valid Trusted Execution Environment (TEE), which is Intel SGX in this case (trustworthiness).

- The enclave has the correct identity and runtime properties that has not been tampered with (identity).

  In the context of Open Enclave, when an enclave requests confidential information from a remote entity, the remote entity will issue a challenge to the requesting enclave to prove its identity and trustworthiness before provisioning any confidential information to the enclave. This process of proving its identity and trustworthiness to a challenger is known as attestation.

### Attestation types

There are two types of attestation:

- **Local Attestation** refers to two enclaves on the same TEE platform authenticating each other before exchanging information. In Open Enclave, this is done through the creation and validation of an enclave's `local report`.

  ![Local Attestation](images/localattestation.png)

- **Remote Attestation** is the process of a [trusted computing base (TCB)](https://en.wikipedia.org/wiki/Trusted_computing_base), a combination of HW and SW, gaining the trust of a remote enclave/provider. In Open Enclave, this is done through the creation and validation of an enclave's `remote report`.

  ![Remote Attestation Sample](images/remoteattestation_service.png)

### Secure Communication Channel

Remote Attestation alone is not enough for the remote party to be able to securely deliver their secrets to the requesting enclave. Securely delivering services requires a secure communication channel. Using Asymmetric/Public-Key encryption is a mechanism for establishing such a channel.

In this remote attestation sample, it demonstrates a way to embed public keys in the remote attestation process to help establish a secure communication channel right after the attestation is done.

Here is a good article about [Intel SGX attestation](
https://software.intel.com/sites/default/files/managed/57/0e/ww10-2016-sgx-provisioning-and-attestation-final.pdf), which describes how Intel's SGX attestation works. The current Open Enclave's implementation was based on it for the SGX platform.

Note: `local report` is the same as an `Intel SGX report`, while the `remote report` is the same as an `Intel SGX quote`.

## Remote Attestation sample

In a typical Open Enclave application, it's common to see multiple enclaves working together to achieve common goals. Once an enclave verifies the counterpart is trustworthy, they can exchange information on a protected channel, which typically provides confidentiality, integrity and replay protection.

This is why instead of attesting an enclave to a remote (mostly cloud) service, this sample demonstrates how to attest two enclaves to each other by using Open Enclave APIs `oe_get_report` and `oe_verify_report` which takes care of all remote attestation operations.

To simplify this sample without losing the focus in explaining how the remote attestation works, host1 and host2 are combined into one single host to eliminate the need for additional socket code logic to deal with communication between two hosts.

![Remote Attestation](images/remoteattestation_sample.png)

### Authoring the Host

The host process is what drives the enclave app. It is responsible for managing the lifetime of the enclave and invoking enclave ECALLs but should be considered an untrusted component that is never allowed to handle plaintext secrets intended for the enclave.

![Remote Attestation](images/remoteattestation_sample_details.png)

The host does the following in this sample:

   1. Create two enclaves for attesting each other, let's say they are enclave1 and enclave2

      ```c
      oe_create_remoteattestation_enclave( enclaveImagePath, OE_ENCLAVE_TYPE_SGX, OE_ENCLAVE_FLAG_DEBUG, NULL, 0, &enclave);
      ```

   2. Ask enclave1 for a remote report and a public key, which is returned in a `RemoteReportWithPKey` structure.

      This is done through a call into the enclave1 `GetRemoteReportWithPKey` `OE_ECALL`

      ```c
      oe_call_enclave(enclave, "GetRemoteReportWithPKey", &args);

      struct RemoteReportWithPKey
      {
          uint8_t pem_key[512]; // public key information
          uint8_t* remote_report;
          size_t remote_report_size;
      };
      ```

      Where:

        - `pem_key` holds the public key that identifying enclave1 and will be used for establishing a secure communication channel between the enclave1 and the enclave2 once the attestation was done.

        - `remote_report` contains a remote report signed by the enclave platform for use in remote attestation

   3. Ask enclave2 to attest (validate) enclave1's remote report (remote_report from above)

      This is done through the following call:
      ```c
      oe_call_enclave(enclave, "VerifyReportAndSetPKey", &args);
      ```

      In the enclave2's implmentation of `VerifyReportAndSetPKey`, it calls `oe_verify_report`, which will be described in the enclave section to handle all the platform specfic report validation operations (including PCK certificate chain checking). If successful the public key in `RemoteReportWithPKey.pem_key` will be stored inside the enclave for future use

   4. Repeat step 2 and 3 for asking enclave1 to validate enclave2
  
   5. After both enclaves successfully attest each other, use Asymmetric/Public-Key Encryption to establish secure communications between the two attesting enclaves.
  
      The fact that each enclave has the other enclave's public key makes it possible to establish a secure communication channel.
  
   6. Send encrypted messages securely between enclaves

      ```c
      // Ask enclave1 to encrypt an internal data with its private key and output encrypted message in encrypted_msg
      generate_encrypted_message(enclave1, &encrypted_msg, &encrypted_msg_size);

      // Send encrypted_msg to the enclave2, which will decrypt it and comparing with its internal data,
      // In this sample, it starts both enclaves with the exact same data contents for the purpose of
      // demonstrating that the encryption works as expected
      process_encrypted_msg(enclave2, encrypted_msg, encrypted_msg_size);
      ```

   7. Free the resource used, including the host memory allocated by the enclaves and the enclaves themselves
  
      For example:

      ```c
      oe_terminate_enclave(enclave1);
      oe_terminate_enclave(enclave2);
      ```

### Authoring the Enclave

#### Attesting an Enclave

Attesting an enclave consists of three steps:

##### 1) Generating an Enclave Report

The enclave being attested first needs to generate a cryptographically strong proof of its identity that the challenger can verify. In the sample this is done by asking the SGX platform to generate a `remote report` signed by Intel via the `oe_get_report` method with `OE_REPORT_FLAGS_REMOTE_ATTESTATION` flag. The `remote report` can be verified by the `oe_verify_report` method on a different machine.

An important feature of `oe_get_report` is that you can pass in application specific data as the `reportData` parameter to be signed into the report.

- This is limited to 64 bytes in SGX. As illustrated in the sample, you sign arbitrarily large data into the report by first hashing it and then passing it to the `oe_get_report` method.

- This is useful to bootstrap a secure communication channel between the enclave and the challenger.

  - In this sample, the enclave signs the hash of an ephemeral public key into its report, which the challenger can then use to encrypt a response to it.

  - Other usage examples for `reportData` might be to include a nonce, or to initiate Diffie-Helman key exchange.

##### 2) Verifying the integrity of the Enclave Report

Once the report is generated and passed to the challenger, the challenger can call `oe_verify_report` to validate the report originated from an Trust Execution Environment (TEE, in the case it's a valid SGX platform).

In the context of Open Enclave on Intel SGX platform, a remote report is verified using the certificate chain issued by Intel which is only valid for SGX platforms.

At this point, the challenger knows that the report originated from an enclave running in a TEE, and that the information in the report can be trusted.

Note that for the Public Preview, remote attestation verification is only supported in the Azure ACC VMs, but Intel will be expanding support for this with Open Enclave SDK more broadly moving forwards.

##### 3) Verifying the enclave identity

Finally, it is up to the enclave app to check that identity and properties of the enclave reflected in the report matches its expectation.
Open Enclave exposes a generalized identity model to support this process across TEE types. In the sample, the app-specific `AttestQuote` method calls `oe_parse_report` to obtain an `oe_report_t`. This data structure surfaces:

- The `reportData` signed into the report
- The generalized identity structure as defined by `oe_identity_t`:

  ```c
  typedef struct _oe_identity
  {
      /** Version of the oe_identity_t structure */
      uint32_t idVersion;

      /** Security version of the enclave. For SGX enclaves, this is the
        *  ISVN value */
      uint32_t securityVersion;

      /** Values of the attributes flags for the enclave -
        *  OE_REPORT_ATTRIBUTES_DEBUG: The report is for a debug enclave.
        *  OE_REPORT_ATTRIBUTES_REMOTE: The report can be used for remote
        *  attestation */
      uint64_t attributes;

      /** The unique ID for the enclave.
        * For SGX enclaves, this is the MRENCLAVE value */
      uint8_t uniqueID[OE_UNIQUE_ID_SIZE];

      /** The author ID for the enclave.
        * For SGX enclaves, this is the MRSIGNER value */
      uint8_t authorID[OE_AUTHOR_ID_SIZE];

      /** The Product ID for the enclave.
        * For SGX enclaves, this is the ISVPRODID value. */
      uint8_t productID[OE_PRODUCT_ID_SIZE];
  } oe_identity_t;
  ```

As shown in the sample, the set of validations performed on these properties is up to the app. In general, we would strongly recommend:

- Ensure that the identity of the enclave matches the expected value:
  - Verify the `uniqueID` value if you want to match the exact bitwise identity of the enclave. Bear in mind that any patches to the enclave will change the uniqueID in the future.
  - Verify the `authorID` and `productID` values if you want to match the identity of an enclave that might span multiple binary versions. This is what the attestation sample does.  
- Ensure that the `securityVersion` of the enclave matches your minimum required security version.
- Ensure that the `reportData` matches the hash of the data provided with the report, as illustrated by the sample.

## Using Cryptography in an Enclave

The attestation remote_attestation/common/crypto.cpp file from the sample illustrates how to use mbedTLS inside the enclave for cryptographic operations such as:

- RSA key generation, encryption and decryption
- SHA256 hashing

In general, the Open Enclave SDK provides default support for mbedTLS layered on top of the Open Enclave core runtime with a small integration surface so that it can be switched out by open source developers in the future for your choice of crypto libraries.

See [here](https://github.com/Microsoft/openenclave/tree/master/docs/MbedtlsSupport.md) for supported mbedTLS functions

## Build and run

To build the sample, change into the remote_attestation directory and run `make build` to build the sample and run `make run` to run it.

For example:

```c
yourusername@yourVMname:~/openenclave/share/openenclave/samples$ cd remote_attestation
yourusername@yourVMname:~/openenclave/share/openenclave/samples/remote_attestation$ make build
yourusername@yourVMname:~/openenclave/share/openenclave/samples/remote_attestation$ make run
```
# Data-sealing Sample

This sample demonstrates how to perform data sealing and unsealing.

It has the following properties:

- Explain the concept of sealing and unsealing in the OE
- Demonstrate how to use OE sealing APIs
- Use OE APIs
  - `oe_get_seal_key_by_policy`
  - `oe_get_seal_key`

## Data Sealing Primer

The *states of an enclave* are not persisted by a system, that is, when an enclave is destroyed, all of its states are lost. This could happen when an enclave application exits, when a system reboots, or simply when a system goes into deep sleep states. To preserve an enclave's states, those states information must explicitly be sent outside the enclave to some persistent storage. When the same enclave is brought back, its states could be restored from the persistent storage. Some data-sealing is more for caching purpose.

The exact definition of an enclave's states is up to a host app and those enclaves involved. It could be some information about the current processing stage in a data pipeline or as simple as some internal secret.

Before those states information leaves an enclave, they are encrypted to protect it from an untrusted host. **Data Sealing** is the process of *encrypting* enclave's states for persistent storage outside of an enclave. This encrypted states are called *sealed data*. This encryption is performed using a private *seal key*, which is derived from the TEE system an enclave is running on. On the other hand, **Data Unsealing** is the reverse process that decrypts an enclave's sealed data using the same seal key. This allows an enclave's states to be restored when the same enclave was subsequently brought back up.

## How OE supports Data Sealing

Instead of publishing convenient APIs, such as Intel SGX SDK's  [sgx_seal_data](https://software.intel.com/en-us/sgx-sdk-dev-reference-sgx-seal-data) and [sgx_unseal_data](https://software.intel.com/en-us/sgx-sdk-dev-reference-sgx-unseal-data), which uses a pre-determined fixed encryption algorithm(AES-GCM) for encryption, OE decides to only provide generic routine for getting seal key and leaves the encryption algorithm up to the enclave developers to choose whatever algorithm they see fit.

### Seal Key Types

Two type of seal keys are supported by OE: In the OE terminology, each seal key type is called a seal policy.

- `OE_SEAL_POLICY_UNIQUE`

  This type of seal key is derived from a measurement of the enclave. Under this policy, the sealed secret can only be unsealed by an instance of the exact enclave code that sealed it. This policy corresponds to using the SGX MRENCLAVE identity for deriving the sealing key.

- `OE_SEAL_POLICY_PRODUCT`

  This type of seal key is derived from the signer of the enclave. Under this policy,  the sealed secret can be unsealed by any enclave signed by the same signer as that of the sealing enclave. The "PRODUCT" in the policy name assumes all enclaves signed by the same signer belong to the same product. This policy corresponds to using the SGX MRSIGNER and ISVPRODID values for deriving the sealing key.

### OE APIs for getting Seal Key

For sealing data to the enclave for caching, OE SDK exposes two methods for an application to take advantage of sealing keys provided by underlying platform:

- Call `oe_get_seal_key_by_policy` to obtain a symmetric key based on the current enclave properties (such as its SecurityVersion and debug state) and your choice of identity properties as specified by the seal policy.

- Call `oe_get_seal_key` to obtain a seal key with the same properties as returned in the keyInfo from a previous call to 
`oe_get_seal_key_by_policy`. This method is used to get the sealing key to unseal previously sealed data.
This is recommended because events such as patching of the server can change the properties used to derive the sealing key
(e.g. CPUSVN) in `oe_get_seal_key_by_policy`. As a best practice, you should persist the `keyInfo` along with your encrypted data for such scenarios.

Once an enclave gets a seal key, it can use it to seal/unseal data.

## Host application

This sample emphasizes on demonstrating how an OE host application initiates seal and unseal operations with simple input data with different policies on enclave environments.

Note: While it's not shown in this sample, seal/unseal operations could be triggered from inside an enclave on the data invisible to host.

### Create three enclaves

- `enclave_a_v1` and `enclave_a_v2` were created and signed by the same private.pem file, which means they share the same signer.

  Notice that in `enc2/Makefile`, instead of generating enc2's own private.pem, it copies the one from enc1, this is how enclave1 and enclave2 shares the same signer.

- `enclave_b` was signed by a newly created private.pem and has a different signer/product identity.

### Seal and unseal data with OE_SEAL_POLICY_UNIQUE in different enclaves

- The host seals a test data string into enclave_a_v1 with `OE_SEAL_POLICY_UNIQUE`, which was done through an `unseal_data()` ecall into enclave1. Upon finishing sealing, a `sealed_data_t` structure is returned back to the host.

- The host unseals the `sealed_data_t` in `enclave_a_v1` and expects to see it's unsealed **successfully** because this sealed data was sealed in the same `enclave_a_v1 enclave`.

- The host unseals the `sealed_data_t` in `enclave_a_v2` and expects to see it **fail** to unseal because this sealed data was not sealed by the same enclave.

- The host unseals the `sealed_data_t` in `enclave_b` and expects to see it **fail** to unseal because this sealed data was not sealed by the same enclave.

### Seal and unseal data with OE_SEAL_POLICY_PRODUCT in different enclaves

- The host seals a test data string into `enclave_a_v1` with `OE_SEAL_POLICY_PRODUCT`, which was done through an `unseal_data()` ecall into enclave1. Upon finishing sealing, a `sealed_data_t` structure is returned back to the host.

- The host unseals the `sealed_data_t` in `enclave_a_v1` and expects to see it's unsealed **successfully** because this sealed data was sealed in the same `enclave_a_v1 enclave`.

- The host unseals the `sealed_data_t` in `enclave_a_v2` and expects to see it **successfully** unseal because this sealed data was signed by the same signature for the same product.

- The host unseals the `sealed_data_t` in `enclave_b` and expects to see it **fail** to unseal because this sealed data was not sealed by the same enclave.

## Enclave library

All three enclaves are almost identical except signed by two different private.pem files.

### ECALLs

There are two ECALLs implemented inside each enclave library.

#### seal_data

```c
int seal_data(int sealPolicy, 
              unsigned char* opt_mgs, size_t opt_msg_len, 
              unsigned char* data, size_t data_size, 
              sealed_data_t** sealed_data, size_t* sealed_data_size)
```

 The enclave allocates the following sealed data structure and fills with iv,encrypted data, and other fields before adding the generated signature to it.
 
```c
typedef struct _sealed_data_t
{
    size_t total_size;
    unsigned char signature[SIGNATURE_LEN];
    unsigned char opt_msg[MAX_OPT_MESSAGE_LEN];
    unsigned char iv[IV_SIZE];
    size_t key_info_size;
    size_t encrypted_data_len; 
    unsigned char encrypted_data[];
} sealed_data_t;
```

- `seal_data` calls `oe_get_seal_key_by_policy` with either `OE_SEAL_POLICY_UNIQUE` or
  `OE_SEAL_POLICY_PRODUCT` to get a unique seal key and its seal key info.
- Generate an initialization vector.
- Encrypt the input data.
- Allocate the `sealed_data_t` structure
- Generate a signature from the `sealed_data_t` structure with the seal key.
- Fill the `sealed_data_t` with above information before returning to the host.

#### unseal_data

```c
int unseal_data(sealed_data_t* sealed_data, size_t sealed_data_size,
                unsigned char** data, size_t* data_size)
```

- `seal_data` calls `oe_get_seal_key` with key info from `sealed_data_t`.
- Retrieve initialization vector from `sealed_data_t.iv`.
- Regenerate a new signature from `sealed_data_t` and validate it against `sealed_data_t.signature`.
- Decrypt `sealed_data_t.encrypted_data`.
- Return the decrypted data before returning to the host.

### Notes

- Security implications with sealing/unsealing: a host is a untrusted entity. And it can load and invoke an enclave in any order they chose. It's important that an enclave implementation does NOT allow the sealing and unsealing capability to leak secrets, or grant unauthorized access to them.

- In a cloud environment, you must not expect that any information sealed by an enclave can be unsealed by it at a future point. This is because the sealing keys generated by platform are machine specific, and your VM may be migrated off a node at any time. For example, if a server is misbehaving and the service healing moves the VM to a different server to maintain a minimum level of service. As such, these APIs should only be used for caching enclave information across restarts of the application or reboots of the VM. It should always be able to fall back to obtaining the sealed data in some other way, such as requesting the secret again from a trusted source via remote attestation.

## Build and run

To build a sample, change directory to your target sample directory and run `make build` to build the sample and run `make run` to run it.

For example:

```bash
yourusername@yourVMname:~/openenclave/share/openenclave/samples$ cd data-sealing
yourusername@yourVMname:~/openenclave/share/openenclave/samples/data-sealing$ make build
yourusername@yourVMname:~/openenclave/share/openenclave/samples/data-sealing$ make run
```
# The Local Attestation Sample

In a typical Open Enclave application, it's common to see multiple enclaves working together to achieve common goals. They would need to attest each other before a trust could be established.
Once an enclave verifies the counterpart is trustworthy, they can exchange information on a protected channel, which typically provides confidentiality, integrity and replay protection.
This sample demonstrates how to conduct local attestation between two enclaves on the same system and establish a secure communication channel for exchanging messages between them.

It has the following properties:

- Written in C++
- Demonstrates an implementation of local attestation
- Use of mbedTLS within the enclave
- Use Asymmetric / Public-Key Encryption to establish secure communications between two attesting enclaves
- Enclave APIs used:
  - oe_get_report
  - oe_verify_report,
  - oe_get_target_info
  
## Attestation primer

See [Remote Attestation's README](../remote_attestation/README.md#attestation-primer) for information

## Local Attestation sample

This sample demonstrates how to attest two enclaves to each other locally by using Open Enclave APIs: `oe_get_report`, `oe_get_target_info`, and `oe_verify_report`. They work together to complete a local attestation process.

To simplify this sample without losing the focus in explaining how the local attestation works, host1 and host2 are combined into one single host to eliminate the need for additional  code for inter-process communication between two hosts.
Diagram 2 is the configuration used in this sample.

![Local Attestation sample](images/localattestation_sample_datails.png)

### Local Attestation steps

For two enclaves on the same system to locally attest each other, the enclaves need to know each other’s identities. OE SDK provides `oe_get_report`, `oe_get_target_info`, and `oe_verify_report` APIs to help broker the identity retrieval, exchange and validation between two enclaves. 

Here are the basic steps of a typical local attestation between two enclaves.

Let's say two enclaves involved are enclave1 and enclave2.

1. Inside enclave1, call `oe_get_report` to get enclave1's report, then call `oe_get_target_info` on enclave1's report
   to get enclave1's target info, enclave1's identity.

2. Send enclave1's identity to enclave2.

3. Inside enclave2, create an **enclave2 report targeted at enclave1**, that is, a report with enclave2's identity
   signed so that enclave1 can verify it.

4. Send the enclave2 report above to enclave1.

5. Inside enclave1, call `oe_verify_report` to verify enclave2 report, on success, it means enclave2 was successfully attested to enclave1.

Step 1-5 completes the process of local attesting enclave2 to enclave1

Repeating step 1-4 with reverse roles of enclave1 and enclave2 can achieve attesting enclave1 to enclave2.

### Authoring the Host

The host application coordinates the local attestation steps described above for helping local attestation process.

The host does the following in this sample:

1. Create two enclaves for attesting each other, let's say they are enclave1 and enclave2

    ```c
    oe_create_localattestation_enclave( enclaveImagePath, OE_ENCLAVE_TYPE_SGX, OE_ENCLAVE_FLAG_DEBUG, NULL, 0, &enclave);
    ```

2.  Attest enclave 1 to enclave 2

    ```c
    attest_one_enclave_to_the_other("enclave1", enclave1, "enclave2", enclave2);
    ```

3. Attest enclave 2 to enclave 1

    ```c
    attest_one_enclave_to_the_other("enclave2", enclave2, "enclave1", enclave1);
    ```

    With successfully attestation on each other, we are ready to securely exchange data between enclaves via asymmetric encryption.

4. Get encrypted message from 1st enclave

    ```c
    generate_encrypted_message(enclave1, &ret, &encrypted_msg, &encrypted_msg_size);
    ```

5. Sending the encrypted message to 2nd enclave to decrypt and validate if the decrypted 
   message is correct.

   Note: both enclaves hardcode their sample messages for this validation.

    ```c
    process_encrypted_msg(enclave2, &ret, encrypted_msg, encrypted_msg_size);
    ```

#### attest_one_enclave_to_the_other() routine

This routine handles the process of attesting enclave2 to enclave1 with the following three steps.

```c
get_target_info(enclave1, &ret, &target_info_buf, &target_info_size);

get_targeted_report_with_pubkey(enclave2, &ret,
                                target_info_buf, target_info_size,
                                &pem_key, &pem_key_size,
                                &report, &report_size);

verify_report_and_set_pubkey(enclave1, &ret, 
                             pem_key,pem_key_size,
                             report, report_size);
```

### Authoring the Enclave

#### Attesting an Enclave

Let's say, we want to attest enclave 2 to enclave 1.

Attesting an enclave consists of three steps:

##### 1) Get an enclave's identity (target info)

To conduct a local attestation, both enclaves need to know each other’s identities.
This is done by calling oe_get_target_info on the enclave 1's own report.

```c
oe_result_t oe_get_target_info(
    const uint8_t* report,
    size_t report_size,
    void* target_info_buffer,
    size_t* target_info_size);
```

On a successful return, target_info_buffer will be deposited with platform specific identity information needed for local attestation.

##### 2) Generate a targeted report with the other enclave's target info (identity)

Inside enclave 2, call oe_get_report with the target info as opt_params. This creates a enclave2 report that' targeted at enclave 1, 
that is, for enclave 1 to validate.

```c
oe_result_t oe_get_report(
    uint32_t flags,
    const uint8_t* report_data,
    size_t report_data_size,
    const void* opt_params,
    size_t opt_params_size,
    uint8_t* report_buffer,
    size_t* report_buffer_size);
```

##### 3) Verify targeted report

This validation consists two parts:

1. Integrity of the Enclave Report

    Enclave 1 can call `oe_verify_report` to validate the report originated from an Trust Execution Environment (TEE),
    which in this case would be a valid SGX platform.

    ```c
    oe_result_t oe_verify_report(const uint8_t* report, size_t report_size, oe_report_t* parsed_report);
    ```

    At this point, Enclave 1 knows that the report originated from an enclave running in a TEE, and that the information in the report can be trusted.

1. Validation of an enclave identity

    Finally, **it is up to the enclave app to check that identity and properties of the enclave reflected in the report matches its expectation**.
    Open Enclave exposes a generalized identity model to support this process across TEE types. `oe_identity_t` is the data structure that defined for this 
    identity model.

    ```c
    typedef struct _oe_identity
    {
        /** Version of the oe_identity_t structure */
        uint32_t idVersion;

        /** Security version of the enclave. For SGX enclaves, this is the
         *  ISVN value */
        uint32_t securityVersion;

        /** Values of the attributes flags for the enclave -
         *  OE_REPORT_ATTRIBUTES_DEBUG: The report is for a debug enclave.
         *  OE_REPORT_ATTRIBUTES_REMOTE: The report can be used for remote
         *  attestation */
        uint64_t attributes;

        /** The unique ID for the enclave.
         * For SGX enclaves, this is the MRENCLAVE value */
        uint8_t uniqueID[OE_UNIQUE_ID_SIZE];

        /** The author ID for the enclave.
         * For SGX enclaves, this is the MRSIGNER value */
        uint8_t authorID[OE_AUTHOR_ID_SIZE];

        /** The Product ID for the enclave.
         * For SGX enclaves, this is the ISVPRODID value. */
        uint8_t productID[OE_PRODUCT_ID_SIZE];
    } oe_identity_t;
    ```

    As shown in the sample, the set of validations performed on these properties is up to the app.

    In general, we would strongly recommend:

    - Ensure that the identity of the enclave matches the expected value:
    - Verify the `uniqueID` value if you want to match the exact bitwise identity of the enclave. Bear in mind that any patches to the enclave will change the uniqueID in the future.
    - Verify the `authorID` and `productID` values if you want to match the identity of an enclave that might span multiple binary versions. This is what the attestation sample does.
    - Ensure that the `securityVersion` of the enclave matches your minimum required security version.
    - Ensure that the `reportData` matches the hash of the data provided with the report, as illustrated by the sample.

    In the sample, the app-specific `Attestation::attest_local_report` method calls `oe_parse_report` to obtain an `oe_report_t`
    for report integrity checking before conducting enclave identity validation based on the information inside `parsed_report`.

## Using Cryptography in an Enclave

The attestation `local_attestation/common/crypto.cpp` file from the sample illustrates how to use mbedTLS inside the enclave for cryptographic operations such as:

- RSA key generation, encryption and decryption
- SHA256 hashing

In general, the Open Enclave SDK provides default support for mbedTLS layered on top of the Open Enclave core runtime with a small integration surface so that it can be switched out by open source developers in the future for your choice of crypto libraries.

See [here](https://github.com/Microsoft/openenclave/tree/master/docs/MbedtlsSupport.md) for supported mbedTLS functions

## Build and run

To build the sample, change into the local_attestation directory and run `make build` to build the sample and run `make run` to run it.

For example:

```bash
yourusername@yourVMname:~/openenclave/share/openenclave/samples$ cd local_attestation
yourusername@yourVMname:~/openenclave/share/openenclave/samples/local_attestation$ make build
yourusername@yourVMname:~/openenclave/share/openenclave/samples/local_attestation$ make run
```

# The helloworld sample

- Written in C
- Minimum code needed for an Open Enclave app
- Help understand the basic components an OE(Open Enclave) application
- Demonstrate how to build, sign, and run an OE image
- Also runs in OE simulation mode

Prerequisite: you may want to read [Common Sample Information](../README.md#common-sample-information) before going further

## About the helloworld sample

This sample is about as simple as you can get regarding creating and calling into an enclave. In this sample you will see:

- The host creates an enclave
- The host calls a simple function in the enclave
- The enclave function prints a message and then calls a simple function back in the host
- The host function prints a message before returning to the enclave
- The enclave function returns back to the host
- The enclave is terminated

This sample uses the Open Enclave SDK `oeedger8r` tool to generate marshaling code necessary to call functions between the enclave
and the host. For more information on using the Open Enclave oeedger8r tool refer to
[Getting started with the Open Enclave edger8r](https://github.com/Microsoft/openenclave/tree/master/docs/GettingStartedDocs/Edger8rGettingStarted.md).

First we need to define the functions we want to call between the enclave and host. To do this we create a `helloworld.edl` file:

```edl
enclave {
    trusted {
        public void enclave_helloworld();

    };

    untrusted {
        void host_helloworld();
    };
};
```

In this `helloworld.edl` file we define two different functions.

```c
public void enclave_helloworld();
```

This method will be implemented inside the trusted enclave itself and the untrusted host will call it. For the host to be able to call this function the host needs to call through the Open Enclave SDK to transition from the untrusted host into the trusted enclave. To help with this the `oeedger8r` tool generates some marshaling code in the host directory with the same signature as the function in the enclave, with the addition of an enclave handle so the SDK knows which enclave will execute the code.

```c
void host_helloworld();
```

The reverse is also true for functions defined in the untrusted host that the trusted enclave needs to call into. The untrusted host will implement this function and the `oeedger8r` tool generates some marshaling code in the enc directory with the same signature as the function in the host.

To generate the functions with the marshaling code the `oeedger8r` is called in both the host and enc directories from their Makefiles:

To generate the marshaling code the untrusted host uses to call into the trusted enclave the following command is run:

```bash
oeedger8r ../helloworld.edl --untrusted
```

This command compiles the `helloworld.edl` file and generates the following files within the host directory:

| file | description |
|---|---|
| host/helloworld_args.h | Defines the parameters that are passed to all functions defined in the edl file |
| host/helloworld_u.c | Contains the `enclave_helloworld()` function with the marshaling code to call into the enclave version of the `enclave_helloworld()` function |
| host/helloworld_u.h | Function prototype for `enclave_helloworld()` function |

To generate the marshaling code the trusted enclave uses to call into the untrusted host the following command is run:

```bash
oeedger8r ../helloworld.edl --trusted
```

| file | description |
|---|---|
| enc/helloworld_args.h | Defines the parameters that are passed to all functions defined in the edl file |
| enc/helloworld_t.c | Contains the `host_helloworld()` function with the marshaling code to call into the host version of the `host_helloworld()` function |
| enc/helloworld_t.h | function prototype for `host_helloworld()` function |

The Makefile in the root of this sample directory has three rules

- build: Calls into the Makefiles in the host and enc directories to build
- clean: Calls in to the Makefiles in the host and enc directories to clean all generated files
- run: Runs the generated host executable, passing the signed enclave executable as a parameter

```make
build:
        $(MAKE) -C enc
        $(MAKE) -C host

clean:
        $(MAKE) -C enc clean
        $(MAKE) -C host clean

run:
        host/helloworldhost ./enc/helloworldenc.signed
```

Build the project with the following command:

```bash
make build
```

Clean the project with the following command:

```bash
make clean
```

Run the built sample with the following command:

```bash
make run
```

## Enclave component
  
This section shows how to develop and build a simple enclave called helloworld.
  
### Develop an enclave
  
An enclave exposes its functionality to the host application in the form of a set of trusted methods that are defined in the `helloworld.edl` file and implemented within the enclave project.

The helloworld sample implements a single function named `enclave_helloworld` which is called by the host. All it does is print out a message and then call back to the host. No parameters are passed in this sample for simplicity.

The full source for the enclave implementation is here: [helloworld/enc/enc.c](enc/enc.c)

```c
#include <stdio.h>

// Include the trusted helloworld header that is generated
// during the build. This file is generated by calling the
// sdk tool oeedger8r against the helloworld.edl file.
#include "helloworld_t.h"

// This is the function that the host calls. It prints
// a message in the enclave before calling back out to
// the host to print a message from there too.
void enclave_helloworld()
{
    // Print a message from the enclave. Note that this
    // does not directly call fprintf, but calls into the
    // host and calls fprintf from there. This is because
    // the fprintf function is not part of the enclave
    // as it requires support from the kernel.
    fprintf(stdout, "Hello world from the enclave\n");

    // Call back into the host
    oe_result_t result = host_helloworld();
    if (result != OE_OK)
    {
        fprintf(stderr, "Call to host_helloworld failed: result=%u (%s)\n", result, 
         oe_result_str(result));
    }
}
```

Each line will now be described in turn.

```c
#include <stdio.h>
```

An enclave library will be loaded into and run inside a host application which is a user-mode process. To keep the [trusted computing base](https://en.wikipedia.org/wiki/Trusted_computing_base) small, the decision was made to make only a specific set of APIs available to an enclave library. A complete list of APIs available to an enclave library can be found [here](https://github.com/Microsoft/openenclave/tree/master/docs/GettingStartedDocs/using_oe_sdk.md#api-references)

The `stdio.h` header file is included in this sample because we are calling the CRT function `fprintf` to print a message on the screen. However this function has a dependency on the kernel to print a message on the screen so this code cannot execute within the enclave itself. Instead this function marshals the call through to the host to carry out the call on the enclaves behalf. Only a subset of the CRT is made available through this open enclave library.

 ```c
void enclave_helloworld()
```

An enclave exposes its functionality via a set of methods defined in the `helloworld.edl` file and implemented here. The only implemented function in the enclave in this sample is `enclave_helloworld`.

```c
fprintf(stdout, "Hello world from the enclave\n");
```

As described above, this call to print a message on the screen marshals the call out of the enclave and back to the untrusted host to print the message.

```c
oe_result_t result = host_helloworld();
if (result != OE_OK)
{
    fprintf(stderr, "Call to host_helloworld failed: result=%u (%s)\n", result, oe_result_str(result));
}
```

This calls the marshaling function that is generated from the `helloworld.edl` file which in turn calls into the function within the host. Even though the `host_helloworld()` function is a `void` this call can still fail within the marshaling code itself and so we should always validate it. If `host_helloworld()` were to return a value, it would actually be passed back as an out parameter of the function.

### Build and sign an enclave

As mentioned in [how-to-build-and-run-samples](../README.md#how-to-build-and-run-samples), make files are provided for each sample. You can build the whole sample by running `make build` from the sample root, or you can build the enclave and host separately by running `make build` in each directory.

The following enclave files come with the sample:

| File | Description |
| --- | --- |
| enc.c | Source code for the enclave `enclave_helloworld` function |
| Makefile | Makefile used to build the enclave |
| helloworld.conf | Configuration parameters for the enclave |

The following files are generated during the build.

| File | Description |
| --- | --- |
| enc.o | Compiled source file for enc.c |
| helloworldenc | built and linked enclave executable |
| helloworldenc.signed | signed version of the enclave executable |
| helloworld_args.h | Defines the parameters that are passed to all functions defined in the edl file |
| helloworld_t.c | Contains the `host_helloworld()` function with the marshaling code to call into the host version of the `host_helloworld()` function |
| helloworld_t.h | function prototype for `host_helloworld()` function |
| helloworld_t.o | compiled marshaling code for helloworld_t.c |
| private.pem | generated signature used for signing the executable |
| public.pem | generated signature used for signing the executable |

Only the signed version of the enclave `helloworldenc.signed` is loadable on Linux as enclaves are required to be digitally signed.

#### Under the hood for the `make build` operation

Here is a listing of key components in the helloworld/enc/Makefile. Also see the [complete listing](enc/Makefile).

```make
# Detect C and C++ compiler options
# if not gcc, default to clang-7

COMPILER=$(notdir $(CC))
ifeq ($(COMPILER), gcc)
        USE_GCC = true
endif

ifeq ($(USE_GCC),)
        CC = clang-7
        COMPILER=clang
endif

CFLAGS=$(shell pkg-config oeenclave-$(COMPILER) --cflags)
LDFLAGS=$(shell pkg-config oeenclave-$(COMPILER) --libs)

all:
	$(MAKE) build
	$(MAKE) keys
	$(MAKE) sign

build:
	@ echo "Compilers used: $(CC), $(CXX)"
	oeedger8r ../helloworld.edl --trusted
	$(CC) -c $(CFLAGS) enc.c -o enc.o
	$(CC) -c $(CFLAGS) helloworld_t.c -o helloworld_t.o
	$(CC) -o helloworldenc helloworld_t.o enc.o $(LDFLAGS)

sign:
	oesign helloworldenc helloworld.conf private.pem

clean:
	rm -f enc.o helloworldenc helloworldenc.signed private.pem ...

keys:
	openssl genrsa -out private.pem -3 3072
	openssl rsa -in private.pem -pubout -out public.pem
```

All OE samples use the `pkg-config` tool for building.

If you are interested in its details, you can find OE pkg-config pc files in package_installtation_destination/share/pkgconfig.

For example: /opt/openenclave/share/pkgconfig

##### Build

The Makefile's `build` target is for compiling enclave source code and linking its library with its dependent libraries (in the following order):

- oeenclave
- mbedx509
- mbedcrypto
- oelibc
- oecore

`helloworldenc is the resulting enclave executable (unsigned)

##### Sign

The OE SDK comes with a signing tool called `oesign` for digitally signing an enclave library. Run `oesign --help` for the usage. For this sample we use the `openssl` command in the `keys` rule to generate the signature, then we sign with the `oesign` tool using the generated signatures.

The signing process also reads the `helloworld.conf` file which describes important parameters associated with with enclave.

```conf
Debug=1
NumHeapPages=1024
NumStackPages=1024
NumTCS=1
ProductID=1
SecurityVersion=1
```

These parameters are described in the [Enclave Building and Signing](https://github.com/Microsoft/openenclave/tree/master/docs/GettingStartedDocs/buildandsign.md#signing-the-enclave) document.

## Host Application

The host process is what drives the enclave app. It is responsible for managing the lifetime of the enclave and invoking enclave methods, but should be considered an untrusted component that is never allowed to handle plaintext secrets intended for the enclave.

In this section we will cover how to develop a host to load and run the helloworld enclave we built above.

### Develop a host

There are relatively fewer restrictions on developing a host application compared to authoring an enclave.
In general, you are free to link your choice of additional libraries into the host application. A part of
a typical host application job is to manage the life cycle of an enclave. Open Enclave SDK provides
an enclave host runtime, with enclave management functions exposed through [openenclave/host.h](https://microsoft.github.io/openenclave/api/host_8h.html).

The full source for the host implementation is here: [helloworld/host/host.c](host/host.c)

```c
#include <openenclave/host.h>
#include <stdio.h>

// Include the untrusted helloworld header that is generated
// during the build. This file is generated by calling the 
// sdk tool oeedger8r against the helloworld.edl file.
#include "helloworld_u.h"

// This is the function that the enclave will call back into to
// print a message.
void host_helloworld()
{
    fprintf(stdout, "Enclave called into host to print: Hello World!\n");
}

int main(int argc, const char* argv[])
{
    oe_result_t result;
    int ret = 1;
    oe_enclave_t* enclave = NULL;

    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s enclave_image_path\n", argv[0]);
        goto exit;
    }

    // Create the enclave by calling oeedger8r generated function.
    result = oe_create_helloworld_enclave(
        argv[1], OE_ENCLAVE_TYPE_SGX, OE_ENCLAVE_FLAG_DEBUG, NULL, 0, &enclave);
    if (result != OE_OK)
    {
        fprintf(stderr, "oe_create_helloworld_enclave(): result=%u (%s)\n", result, oe_result_str(result));
        goto exit;
    }

    // Call into the enclave
    result = enclave_helloworld(enclave);
    if (result != OE_OK)
    {
        fprintf(stderr, "calling into enclave_helloworld failed: result=%u (%s)\n", result, oe_result_str(result));
        goto exit;
    }

    ret = 0;

exit:
    //Clean up the enclave if we created one
    if (enclave)
        oe_terminate_enclave(enclave);

    return ret;
}
```

Each line will now be described in turn.

```c
#include <openenclave/host.h>
```

Includes the header for the Open Enclave functions used in this file, (e.g `oe_terminate_enclave`).

```c
#include <stdio.h>
```

Includes the standard CRT libraries. Unlike the enclave implementation, which includes a special enclave version of the stdio library that marshals APIs to the host, the host is not protected, so uses all the normal C libraries and functions.

```c
void host_helloworld()
{
    fprintf(stdout, "Enclave called into host to print: Hello World!\n");
}
```

This is the actual host function that the enclave calls into. The function is defined in the `helloworld.edl` file and implemented here.

```c
int main(int argc, const char* argv[])
```

The host is the application that creates and calls into the enclave, so this host is a normal C executable with a standard `main` function.

```c
result = oe_create_helloworld_enclave(
    argv[1], OE_ENCLAVE_TYPE_SGX, OE_ENCLAVE_FLAG_DEBUG, NULL, 0, &enclave);
```

This `oe_create_helloworld_enclave` function is generated by oeedger8r.
This function creates an enclave for use in the host process. This includes:
- Allocating the enclave address space.
- Loading the enclave code and data from its library file into that address space.
- Setting up the enclave environment, including the enclave heap and data structures for each enclave thread.
- Measuring the resulting enclave identity and ensuring it matches the enclave signature.
- Initializing the enclave so that it is ready to be called from the host.

The helloworld sample creates an enclave by calling `oe_create_helloworld_enclave` with the path to the signed enclave library file, which happens to be passed as the first parameter to the launching application. 

The `OE_ENCLAVE_FLAG_DEBUG` flag allows the enclave to be created without the enclave binary being signed. It also gives a developer permission to debug the process and get access to enclave memory. What this means is ** DO NOT SHIP CODE WITH THE `OE_ENCLAVE_FLAG_DEBUG` ** because it is insecure. What it gives is the ability to develop your enclave more easily. Before you ship the code, you need to have a proper code signing story for the enclave executable. Some newer Intel SGX platforms allow self-signed certificates to be used, but some of the older Intel SGX platforms require Intel to sign your enclave executable.

On a successful creation, the function returns an opaque enclave handle for any future operation on the enclave.

> You can create multiple enclave instances this way if there are remaining enclave resources available, such as the Enclave Page Cache (EPC).

```c
result = enclave_helloworld(enclave);
if (result != OE_OK)
{
    fprintf(stderr, "calling into enclave_helloworld failed: result=%u (%s)\n", result, oe_result_str(result));
    goto exit;
}
```

This function calls into the host marshaling function that is generated from the `helloworld.edl` file. It handles the code that marshals any parameters, and calls the function within the enclave itself. In this sample, we do not have any actual function parameters. Even though the function `enclave_helloworld()` is a `void` return type, the marshaling code itself can fail, so we need to validate the return code associated with it. If `enclave_helloworld()` were to return a value, this would be passed back as an out parameter.

The Open Enclave handles all the context switching between the host mode and the enclave mode.

```c
oe_terminate_enclave
```

Terminates the enclave and frees up all resources associated with it.

### Build a host

The helloworld sample comes with a Makefile with a `build` target. You can run `make build` to generate the marshaling files and build the host app.

Listing of [helloworld/host/Makefile](host/Makefile)

```make
# Detect C and C++ compiler options
# if not gcc, default to clang-7

COMPILER=$(notdir $(CC))
ifeq ($(COMPILER), gcc)
        USE_GCC = true
endif

ifeq ($(USE_GCC),)
        CC = clang-7
        COMPILER=clang
endif

CFLAGS=$(shell pkg-config oehost-$(COMPILER) --cflags)
LDFLAGS=$(shell pkg-config oehost-$(COMPILER) --libs)

build:
	@ echo "Compilers used: $(CC), $(CXX)"
	oeedger8r ../helloworld.edl --untrusted
	$(CC) -c $(CFLAGS) host.c
	$(CC) -c $(CFLAGS) helloworld_u.c
	$(CC) -o helloworldhost helloworld_u.o host.o $(LDFLAGS)

clean:
	rm -f helloworldhost host.o helloworld_u.o helloworld_u.c helloworld_u.h helloworld_args.h

```

The following host files come with the sample:

| File | Description |
| --- | --- |
| host.c | Source code for the host `host_helloworld` function, as well as the executable `main` function. |
| Makefile | Makefile used to build the host |

The following files are generated during the build.

| File | Description |
| --- | --- |
| host.o | Compiled host.c source file |
| helloworldhost | built and linked host executable |
| helloworld_args.h | Defines the parameters that are passed to all functions defined in the edl file |
| helloworld_u.c | Contains the `enclave_helloworld()` function with the marshaling code to call into the enclave version of the `enclave_helloworld()` function |
| helloworld_u.h | Function prototype for `enclave_helloworld()` function |
| helloworld_u.o | compiled helloworld_u.c source file |

# How to Run

You can run the helloworld sample directly on the command line as follows:

```bash
./host/helloworldhost ./enc/helloworldenc.signed
```

Or execute `make run` from the root of the sample:

```bash
$ make run
host/helloworldhost ./enc/helloworldenc.signed
Hello world from the enclave
Enclave called into host to print: Hello World!
```

helloworld sample can run under OE simulation mode.

To run the helloworld sample in simulation mode from the command like, use the following:

```bash
./host/helloworldhost ./enc/helloworldenc.signed --simulate
```
# The File-Encryptor Sample

OE SDK comes with a default crypto support library that supports a [subset of the open sources mbedTLS](https://github.com/Microsoft/openenclave/blob/master/docs/MbedtlsSupport.md) library.
This sample demonstrates how to perform simple file cryptographic operations inside an enclave using mbedTLS library.

It has the following properties:

- Written in C++
- Show how to encrypt and decrypt data inside an enclave
- Show how to derive a key from a password string using [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2)
- Use AES mbedTLS API to perform encryption and decryption
- Use the following OE APIs
  - mbedtls_aes_setkey_*
  - mbedtls_aes_crypt_cbc
  - mbedtls_pkcs5_pbkdf2_hmac
  - mbedtls_ctr_drbg_random
  - mbedtls_entropy_*
  - mbedtls_ctr_drbg_*
  - mbedtls_sha256_*
  - oe_is_outside_enclave
- Also runs in OE simulation mode

## Host application

This sample is relatively straightforward, It's all about the use of the mbedTLS library.

![Sample components diagram](diagram.png)

The host application drives an enclave to perform the following operations:

1. Create an enclave from the host.

2. Encrypt a `testfile` into `out.encrypted`. It breaks an input file into 16-byte blocks.
   It then sends each block to the enclave for encryption one block after the other until the
   very last block is encountered. It makes sure the last block is padded to make it a 16-byte block,
   which was required AES-CBC encryption algorithm used by the enclave.

3. Decrypt the `out.encrypted` file to the `out.decrypted` file.

   The decryption process is a reverse of the encryption except that it provides a encryption header
   to the encryptor in the enclave in its `initialize_encryptor` call, which contains a
   `encryption_header_t` (defined below), that has encryption metadata for the encryptor
   to validate its password and retrieve the encryption key from it.

   In the end, the host makes sure the contents of `testfile` and `out.decrypted` are identical
   i.e. that the encryption and the decryption produce the expected result.

4. Terminate the enclave.

## Enclave library

### ECALLs

There are three ECALLs implemented inside the enclave library:

### 1. initialize_encryptor

```c
int initialize_encryptor(
    bool encrypt,
    const char* password,
    size_t password_len,
    encryption_header_t* header)
```

The bulk of the operations done in this enclave call involve allocating resources and setting up mbedTLS for encryption and decryption operations.

#### For encryption operation

It does the following operations to generate `encryption_header_t` information for passing back the host to write into the encrypted file.

```c
typedef struct _encryption_header
{
    size_t fileDataSize;
    unsigned char digest[HASH_VALUE_SIZE_IN_BYTES];
    unsigned char encrypted_key[ENCRYPTION_KEY_SIZE_IN_BYTES];
} encryption_header_t;
```

- Generate a SHA256 digest for the input password, stored in digest field.
- Derive a password key from the input password.
- Produce an encryption key.
- Encrypt the encryption key with the password key, stored in `encrypted_key` field.

See the following routine for implementation details:

```c
int ecall_dispatcher::prepare_encryption_header(
    encryption_header_t* header,
    string password)
```

#### For decryption operation 

In decryption, instead of generating `encryption_header_t` information, initialize_encryptor uses the host provided `encryption_header_t`
information to validate the input password and extract encryption key for later decryption operations.

Here what it does:

- Check password by comparing `encryption_header_t.digest` with the calculated hash of the input password.
- Derive a password key from the input password.
- Decrypt `encryption_header_t.encrypted_key` with the password key produced above, in preparing for upcoming decryption operations.

See the following routine for details:

```c
int ecall_dispatcher::parse_encryption_header(
    encryption_header_t* header,
    string password)
```

#### 2. encrypt_block

```c
int encrypt_block(
    bool encrypt,
    unsigned char* input_buf,
    unsigned char* output_buf,
    size_t size)
```

Send a block of data to the enclave for encryption using the configuration setup up by the `initialize_encryptor()` call.

#### 3. close_encryptor()

```c
void close_encryptor()
```

Free all the resources allocated for this encryptor instance.

## Build and run

To build a sample, change directory to your target sample directory and run `make build` to build the sample and run `make run` to run it.

For example:

```bash
yourusername@yourVMname:~/openenclave/share/openenclave/samples$ cd file-encryptor
yourusername@yourVMname:~/openenclave/share/openenclave/samples/file-encryptor$ make build
yourusername@yourVMname:~/openenclave/share/openenclave/samples/file-encryptor$ make run
```
prereqs
=======

This directory contains a makefile to build and install Open Enclave
prerequisites, including:

- Package dependencies

- Intel(R) SGX driver

- Intel(R) SGX AESM service
az-dcap-client
==============

This directory contains an optional Makefile to install the Azure DCAP client
package. The DCAP client is necessary for performing remote attestation in
Open Enclave apps running in the Azure environment.

You can download and install the package with:

```bash
sudo make
sudo make install
```

If you have a local copy of the package, you can also install from it directly:

```bash
sudo make USE_PKGS_IN=~/my_packages
sudo make install
```

To uninstall the package, you can run:

```bash
sudo make uninstall
sudo make distclean
```
refman
======

This directory builds all Doxygen output formats. To learn how Doxygen is used
in Open Enclave, please refer to
[Using Doxygen in Open Enclave](doxygen-howto.md).

libcxx
======

This directory contains a makefile that combines the following third-party
libraries into a single library.

- libcxxrt.a - C++ runtime support library
- libunwind.a - C++ exception unwinding library
- libcxx.a - Standard C++ library

The resuling library is named liboelibcxx.a.
cmake
=====

This folder contains various CMake scripts and includes used for building Open Enclave.
# Open Enclave Edger8r POC

This folder contains Proof Of Concept of adapting Intel Edger8r to generate Open Enclave edge routines.

---
## Building and Running

### Build

`$ make`

This creates **dist/oe_edger8r**.

### Run

`$ cd test`

`$ ../dist/oe_edger8r array.edl`

This should generate _t.h, _t.c, _u.h, _u.c and _args.h files.

### Clean
`$ make clean`

---
## Documentation

### Changes to Intel's Edger8r code
Intel's Edger8r code exists in the intel folder. The following minimal changes have been made:

1. New Plugin.ml file that contains two dependency injection points **available** and **gen_edge_routines**.
   They indicate whether a plugin is available or not, and the edge routines generation function installed by the plugin.
   Currently, to avoid distribution challenges, the plugin is compiled together with the main edger8r program.
2. Changes to CodeGen.ml's gen_enclave_code to check and use a plugin if it exists:
    ```ocaml
        if Plugin.available() then
        Plugin.gen_edge_routines ec ep
        else (      
        (if ep.gen_untrusted then (gen_untrusted_header ec; if not ep.header_only then gen_untrusted_source ec));
        (if ep.gen_trusted then (gen_trusted_header ec; if not ep.header_only then gen_trusted_source ec))    
    ```
3. Definition of enclave_content record type in Ast.ml to avoid cyclic dependency. The plugin uses enclave_content and 
   edger8r_params record types in addition to the abstract syntax tree types defined in Ast.ml.
   If enclave_content is defined only in CodeGen.ml, then it would lead to a cyclic dependency between CodeGen.ml and Plugin.ml.
   This is solved by defining the enclave_content record in Ast.ml and redefining it as an equivalent type in CodeGen.ml.

### Open Enclave Emitter

Edge routine emitter for Open Enclave is implemented in Emitter.ml. It generates code for all the test .edl files.
It is work in progress. There is also a new main.ml which acts are the program entry point. I would like to somehow get rid of that.




oesgx
=====

This directory contains the oesgx tool, which determines the level of 
SGX support for the given CPU. It printfs one of these:

    0 -- no support
    1 -- SGX-1
    2 -- SGX-2

For example:

    $ ./oesgx
    1

libc
====

This directory contains the oelibc library, formed from the following parts:

- Sources included from MUSL libc ([located here](../3rdparty/musl))
- The heap allocator ([located here](../enclave/core))
- Customization of standard functions for enclave usage
- Stubs to work around missing definitions needed by other components

Sources shared by both the Enclave and Host libraries.

