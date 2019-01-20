This repository holds supplemental Go packages for low-level interactions with the operating system.

To submit changes to this repository, see http://golang.org/doc/contribute.html.
# Building `sys/unix`

The sys/unix package provides access to the raw system call interface of the
underlying operating system. See: https://godoc.org/golang.org/x/sys/unix

Porting Go to a new architecture/OS combination or adding syscalls, types, or
constants to an existing architecture/OS pair requires some manual effort;
however, there are tools that automate much of the process.

## Build Systems

There are currently two ways we generate the necessary files. We are currently
migrating the build system to use containers so the builds are reproducible.
This is being done on an OS-by-OS basis. Please update this documentation as
components of the build system change.

### Old Build System (currently for `GOOS != "Linux" || GOARCH == "sparc64"`)

The old build system generates the Go files based on the C header files
present on your system. This means that files
for a given GOOS/GOARCH pair must be generated on a system with that OS and
architecture. This also means that the generated code can differ from system
to system, based on differences in the header files.

To avoid this, if you are using the old build system, only generate the Go
files on an installation with unmodified header files. It is also important to
keep track of which version of the OS the files were generated from (ex.
Darwin 14 vs Darwin 15). This makes it easier to track the progress of changes
and have each OS upgrade correspond to a single change.

To build the files for your current OS and architecture, make sure GOOS and
GOARCH are set correctly and run `mkall.sh`. This will generate the files for
your specific system. Running `mkall.sh -n` shows the commands that will be run.

Requirements: bash, perl, go

### New Build System (currently for `GOOS == "Linux" && GOARCH != "sparc64"`)

The new build system uses a Docker container to generate the go files directly
from source checkouts of the kernel and various system libraries. This means
that on any platform that supports Docker, all the files using the new build
system can be generated at once, and generated files will not change based on
what the person running the scripts has installed on their computer.

The OS specific files for the new build system are located in the `${GOOS}`
directory, and the build is coordinated by the `${GOOS}/mkall.go` program. When
the kernel or system library updates, modify the Dockerfile at
`${GOOS}/Dockerfile` to checkout the new release of the source.

To build all the files under the new build system, you must be on an amd64/Linux
system and have your GOOS and GOARCH set accordingly. Running `mkall.sh` will
then generate all of the files for all of the GOOS/GOARCH pairs in the new build
system. Running `mkall.sh -n` shows the commands that will be run.

Requirements: bash, perl, go, docker

## Component files

This section describes the various files used in the code generation process.
It also contains instructions on how to modify these files to add a new
architecture/OS or to add additional syscalls, types, or constants. Note that
if you are using the new build system, the scripts cannot be called normally.
They must be called from within the docker container.

### asm files

The hand-written assembly file at `asm_${GOOS}_${GOARCH}.s` implements system
call dispatch. There are three entry points:
```
  func Syscall(trap, a1, a2, a3 uintptr) (r1, r2, err uintptr)
  func Syscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2, err uintptr)
  func RawSyscall(trap, a1, a2, a3 uintptr) (r1, r2, err uintptr)
```
The first and second are the standard ones; they differ only in how many
arguments can be passed to the kernel. The third is for low-level use by the
ForkExec wrapper. Unlike the first two, it does not call into the scheduler to
let it know that a system call is running.

When porting Go to an new architecture/OS, this file must be implemented for
each GOOS/GOARCH pair.

### mksysnum

Mksysnum is a script located at `${GOOS}/mksysnum.pl` (or `mksysnum_${GOOS}.pl`
for the old system). This script takes in a list of header files containing the
syscall number declarations and parses them to produce the corresponding list of
Go numeric constants. See `zsysnum_${GOOS}_${GOARCH}.go` for the generated
constants.

Adding new syscall numbers is mostly done by running the build on a sufficiently
new installation of the target OS (or updating the source checkouts for the
new build system). However, depending on the OS, you make need to update the
parsing in mksysnum.

### mksyscall.pl

The `syscall.go`, `syscall_${GOOS}.go`, `syscall_${GOOS}_${GOARCH}.go` are
hand-written Go files which implement system calls (for unix, the specific OS,
or the specific OS/Architecture pair respectively) that need special handling
and list `//sys` comments giving prototypes for ones that can be generated.

The mksyscall.pl script takes the `//sys` and `//sysnb` comments and converts
them into syscalls. This requires the name of the prototype in the comment to
match a syscall number in the `zsysnum_${GOOS}_${GOARCH}.go` file. The function
prototype can be exported (capitalized) or not.

Adding a new syscall often just requires adding a new `//sys` function prototype
with the desired arguments and a capitalized name so it is exported. However, if
you want the interface to the syscall to be different, often one will make an
unexported `//sys` prototype, an then write a custom wrapper in
`syscall_${GOOS}.go`.

### types files

For each OS, there is a hand-written Go file at `${GOOS}/types.go` (or
`types_${GOOS}.go` on the old system). This file includes standard C headers and
creates Go type aliases to the corresponding C types. The file is then fed
through godef to get the Go compatible definitions. Finally, the generated code
is fed though mkpost.go to format the code correctly and remove any hidden or
private identifiers. This cleaned-up code is written to
`ztypes_${GOOS}_${GOARCH}.go`.

The hardest part about preparing this file is figuring out which headers to
include and which symbols need to be `#define`d to get the actual data
structures that pass through to the kernel system calls. Some C libraries
preset alternate versions for binary compatibility and translate them on the
way in and out of system calls, but there is almost always a `#define` that can
get the real ones.
See `types_darwin.go` and `linux/types.go` for examples.

To add a new type, add in the necessary include statement at the top of the
file (if it is not already there) and add in a type alias line. Note that if
your type is significantly different on different architectures, you may need
some `#if/#elif` macros in your include statements.

### mkerrors.sh

This script is used to generate the system's various constants. This doesn't
just include the error numbers and error strings, but also the signal numbers
an a wide variety of miscellaneous constants. The constants come from the list
of include files in the `includes_${uname}` variable. A regex then picks out
the desired `#define` statements, and generates the corresponding Go constants.
The error numbers and strings are generated from `#include <errno.h>`, and the
signal numbers and strings are generated from `#include <signal.h>`. All of
these constants are written to `zerrors_${GOOS}_${GOARCH}.go` via a C program,
`_errors.c`, which prints out all the constants.

To add a constant, add the header that includes it to the appropriate variable.
Then, edit the regex (if necessary) to match the desired constant. Avoid making
the regex too broad to avoid matching unintended constants.


## Generated files

### `zerror_${GOOS}_${GOARCH}.go`

A file containing all of the system's generated error numbers, error strings,
signal numbers, and constants. Generated by `mkerrors.sh` (see above).

### `zsyscall_${GOOS}_${GOARCH}.go`

A file containing all the generated syscalls for a specific GOOS and GOARCH.
Generated by `mksyscall.pl` (see above).

### `zsysnum_${GOOS}_${GOARCH}.go`

A list of numeric constants for all the syscall number of the specific GOOS
and GOARCH. Generated by mksysnum (see above).

### `ztypes_${GOOS}_${GOARCH}.go`

A file containing Go types for passing into (or returning from) syscalls.
Generated by godefs and the types file (see above).
# go-colorable

[![Godoc Reference](https://godoc.org/github.com/mattn/go-colorable?status.svg)](http://godoc.org/github.com/mattn/go-colorable)
[![Build Status](https://travis-ci.org/mattn/go-colorable.svg?branch=master)](https://travis-ci.org/mattn/go-colorable)
[![Coverage Status](https://coveralls.io/repos/github/mattn/go-colorable/badge.svg?branch=master)](https://coveralls.io/github/mattn/go-colorable?branch=master)
[![Go Report Card](https://goreportcard.com/badge/mattn/go-colorable)](https://goreportcard.com/report/mattn/go-colorable)

Colorable writer for windows.

For example, most of logger packages doesn't show colors on windows. (I know we can do it with ansicon. But I don't want.)
This package is possible to handle escape sequence for ansi color on windows.

## Too Bad!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/bad.png)


## So Good!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/good.png)

## Usage

```go
logrus.SetFormatter(&logrus.TextFormatter{ForceColors: true})
logrus.SetOutput(colorable.NewColorableStdout())

logrus.Info("succeeded")
logrus.Warn("not correct")
logrus.Error("something error")
logrus.Fatal("panic")
```

You can compile above code on non-windows OSs.

## Installation

```
$ go get github.com/mattn/go-colorable
```

# License

MIT

# Author

Yasuhiro Matsumoto (a.k.a mattn)
# go-isatty

[![Godoc Reference](https://godoc.org/github.com/mattn/go-isatty?status.svg)](http://godoc.org/github.com/mattn/go-isatty)
[![Build Status](https://travis-ci.org/mattn/go-isatty.svg?branch=master)](https://travis-ci.org/mattn/go-isatty)
[![Coverage Status](https://coveralls.io/repos/github/mattn/go-isatty/badge.svg?branch=master)](https://coveralls.io/github/mattn/go-isatty?branch=master)
[![Go Report Card](https://goreportcard.com/badge/mattn/go-isatty)](https://goreportcard.com/report/mattn/go-isatty)

isatty for golang

## Usage

```go
package main

import (
	"fmt"
	"github.com/mattn/go-isatty"
	"os"
)

func main() {
	if isatty.IsTerminal(os.Stdout.Fd()) {
		fmt.Println("Is Terminal")
	} else if isatty.IsCygwinTerminal(os.Stdout.Fd()) {
		fmt.Println("Is Cygwin/MSYS2 Terminal")
	} else {
		fmt.Println("Is Not Terminal")
	}
}
```

## Installation

```
$ go get github.com/mattn/go-isatty
```

## License

MIT

## Author

Yasuhiro Matsumoto (a.k.a mattn)

## Thanks

* k-takata: base idea for IsCygwinTerminal

    https://github.com/k-takata/go-iscygpty
# ansi

Package ansi is a small, fast library to create ANSI colored strings and codes.

## Install

Get it

```sh
go get -u github.com/mgutz/ansi
```

## Example

```go
import "github.com/mgutz/ansi"

// colorize a string, SLOW
msg := ansi.Color("foo", "red+b:white")

// create a FAST closure function to avoid computation of ANSI code
phosphorize := ansi.ColorFunc("green+h:black")
msg = phosphorize("Bring back the 80s!")
msg2 := phospohorize("Look, I'm a CRT!")

// cache escape codes and build strings manually
lime := ansi.ColorCode("green+h:black")
reset := ansi.ColorCode("reset")

fmt.Println(lime, "Bring back the 80s!", reset)
```

Other examples

```go
Color(s, "red")            // red
Color(s, "red+b")          // red bold
Color(s, "red+B")          // red blinking
Color(s, "red+u")          // red underline
Color(s, "red+bh")         // red bold bright
Color(s, "red:white")      // red on white
Color(s, "red+b:white+h")  // red bold on white bright
Color(s, "red+B:white+h")  // red blink on white bright
Color(s, "off")            // turn off ansi codes
```

To view color combinations, from project directory in terminal.

```sh
go test
```

## Style format

```go
"foregroundColor+attributes:backgroundColor+attributes"
```

Colors

* black
* red
* green
* yellow
* blue
* magenta
* cyan
* white
* 0...255 (256 colors)

Foreground Attributes

* B = Blink
* b = bold
* h = high intensity (bright)
* i = inverse
* s = strikethrough
* u = underline

Background Attributes

* h = high intensity (bright)

## Constants

* ansi.Reset
* ansi.DefaultBG
* ansi.DefaultFG
* ansi.Black
* ansi.Red
* ansi.Green
* ansi.Yellow
* ansi.Blue
* ansi.Magenta
* ansi.Cyan
* ansi.White
* ansi.LightBlack
* ansi.LightRed
* ansi.LightGreen
* ansi.LightYellow
* ansi.LightBlue
* ansi.LightMagenta
* ansi.LightCyan
* ansi.LightWhite

## References

Wikipedia ANSI escape codes [Colors](http://en.wikipedia.org/wiki/ANSI_escape_code#Colors)

General [tips and formatting](http://misc.flogisoft.com/bash/tip_colors_and_formatting)

What about support on Windows? Use [colorable by mattn](https://github.com/mattn/go-colorable).
Ansi and colorable are used by [logxi](https://github.com/mgutz/logxi) to support logging in
color on Windows.

## MIT License

Copyright (c) 2013 Mario Gutierrez mario@mgutz.com

See the file LICENSE for copying permission.

logstreamer [![Build Status][BuildStatusIMGURL]][BuildStatusURL]
===============
[![Flattr][FlattrIMGURL]][FlattrURL]

[BuildStatusIMGURL]:        https://secure.travis-ci.org/kvz/logstreamer.png?branch=master
[BuildStatusURL]:           //travis-ci.org/kvz/logstreamer  "Build Status"
[FlattrIMGURL]:             http://api.flattr.com/button/flattr-badge-large.png
[FlattrURL]:                https://flattr.com/submit/auto?user_id=kvz&url=github.com/kvz/logstreamer&title=logstreamer&language=&tags=github&category=software

Prefixes streams (e.g. stdout or stderr) in Go.

If you are executing a lot of (remote) commands, you may want to indent all of their
output, prefix the loglines with hostnames, or mark anything that was thrown to stderr
red, so you can spot errors more easily.

For this purpose, Logstreamer was written.

You pass 3 arguments to `NewLogstreamer()`:

 - Your `*log.Logger`
 - Your desired prefix (`"stdout"` and `"stderr"` prefixed have special meaning)
 - If the lines should be recorded `true` or `false`. This is useful if you want to retrieve any errors.

This returns an interface that you can point `exec.Command`'s `cmd.Stderr` and `cmd.Stdout` to.
All bytes that are written to it are split by newline and then prefixed to your specification.

**Don't forget to call `Flush()` or `Close()` if the last line of the log
might not end with a newline character!**

A typical usage pattern looks like this:

```go
// Create a logger (your app probably already has one)
logger := log.New(os.Stdout, "--> ", log.Ldate|log.Ltime)

// Setup a streamer that we'll pipe cmd.Stdout to
logStreamerOut := NewLogstreamer(logger, "stdout", false)
defer logStreamerOut.Close()
// Setup a streamer that we'll pipe cmd.Stderr to.
// We want to record/buffer anything that's written to this (3rd argument true)
logStreamerErr := NewLogstreamer(logger, "stderr", true)
defer logStreamerErr.Close()

// Execute something that succeeds
cmd := exec.Command(
	"ls",
	"-al",
)
cmd.Stderr = logStreamerErr
cmd.Stdout = logStreamerOut

// Reset any error we recorded
logStreamerErr.FlushRecord()

// Execute command
err := cmd.Start()
```

## Test

```bash
$ cd src/pkg/logstreamer/
$ go test
```

Here I issue two local commands, `ls -al` and `ls nonexisting`:

![screen shot 2013-07-02 at 2 48 33 pm](https://f.cloud.github.com/assets/26752/736371/16177cf0-e316-11e2-8dc6-320f52f71442.png)

Over at [Transloadit](http://transloadit.com) we use it for streaming remote commands.
Servers stream command output over SSH back to me, and every line is prefixed with a date, their hostname & marked red in case they
wrote to stderr.

## License

This project is licensed under the MIT license, see `LICENSE.txt`.
[![GoDoc](http://godoc.org/github.com/robfig/cron?status.png)](http://godoc.org/github.com/robfig/cron) 
[![Build Status](https://travis-ci.org/robfig/cron.svg?branch=master)](https://travis-ci.org/robfig/cron)
