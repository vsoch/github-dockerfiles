[![Build Status](https://jenkins.dockerproject.org/buildStatus/icon?job=runc Master)](https://jenkins.dockerproject.org/job/runc Master)

## runc

`runc` is a CLI tool for spawning and running containers according to the OCI specification.

## Releases

`runc` depends on and tracks the [runtime-spec](https://github.com/opencontainers/runtime-spec) repository.
We will try to make sure that `runc` and the OCI specification major versions stay in lockstep.
This means that `runc` 1.0.0 should implement the 1.0 version of the specification.

You can find official releases of `runc` on the [release](https://github.com/opencontainers/runc/releases) page.

## Building

`runc` currently supports the Linux platform with various architecture support. 
It must be built with Go version 1.6 or higher in order for some features to function properly.

```bash
# create a 'github.com/opencontainers' in your GOPATH/src
cd github.com/opencontainers
git clone https://github.com/opencontainers/runc
cd runc

make
sudo make install
```

`runc` will be installed to `/usr/local/sbin/runc` on your system.

In order to enable seccomp support you will need to install libseccomp on your platform.
If you do not want to build `runc` with seccomp support you can add `BUILDTAGS=""` when running make.

#### Build Tags

`runc` supports optional build tags for compiling support of various features.
To add build tags to the make option the `BUILDTAGS` variable must be set.

```bash
make BUILDTAGS='seccomp apparmor'
```

| Build Tag | Feature                            | Dependency  |
|-----------|------------------------------------|-------------|
| seccomp   | Syscall filtering                  | libseccomp  |
| selinux   | selinux process and mount labeling | <none>      |
| apparmor  | apparmor profile support           | libapparmor |


### Running the test suite

`runc` currently supports running its test suite via Docker.
To run the suite just type `make test`.

```bash
make test
```

There are additional make targets for running the tests outside of a container but this is not recommended as the tests are written with the expectation that they can write and remove anywhere.

You can run a specific test case by setting the `TESTFLAGS` variable.

```bash
# make test TESTFLAGS="-run=SomeTestFunction"
```

## Using runc

### Creating an OCI Bundle

In order to use runc you must have your container in the format of an OCI bundle.
If you have Docker installed you can use its `export` method to acquire a root filesystem from an existing Docker container.

```bash
# create the top most bundle directory
mkdir /mycontainer
cd /mycontainer

# create the rootfs directory
mkdir rootfs

# export busybox via Docker into the rootfs directory
docker export $(docker create busybox) | tar -C rootfs -xvf -
```

After a root filesystem is populated you just generate a spec in the format of a `config.json` file inside your bundle.
`runc` provides a `spec` command to generate a base template spec that you are then able to edit.
To find features and documentation for fields in the spec please refer to the [specs](https://github.com/opencontainers/runtime-spec) repository.

```bash
runc spec
```

### Running Containers

Assuming you have an OCI bundle from the previous step you can execute the container in two different ways.

The first way is to use the convenience command `run` that will handle creating, starting, and deleting the container after it exits.

```bash
cd /mycontainer

runc run mycontainerid
```

If you used the unmodified `runc spec` template this should give you a `sh` session inside the container.

The second way to start a container is using the specs lifecycle operations.
This gives you more power over how the container is created and managed while it is running.
This will also launch the container in the background so you will have to edit the `config.json` to remove the `terminal` setting for the simple examples here.
Your process field in the `config.json` should look like this below with `"terminal": false` and `"args": ["sleep", "5"]`.


```json
        "process": {
                "terminal": false,
                "user": {
                        "uid": 0,
                        "gid": 0
                },
                "args": [
                        "sleep", "5"
                ],
                "env": [
                        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                        "TERM=xterm"
                ],
                "cwd": "/",
                "capabilities": [
                        "CAP_AUDIT_WRITE",
                        "CAP_KILL",
                        "CAP_NET_BIND_SERVICE"
                ],
                "rlimits": [
                        {
                                "type": "RLIMIT_NOFILE",
                                "hard": 1024,
                                "soft": 1024
                        }
                ],
                "noNewPrivileges": true
        },
```

Now we can go though the lifecycle operations in your shell.


```bash
cd /mycontainer

runc create mycontainerid

# view the container is created and in the "created" state
runc list

# start the process inside the container
runc start mycontainerid

# after 5 seconds view that the container has exited and is now in the stopped state
runc list

# now delete the container
runc delete mycontainerid
```

This adds more complexity but allows higher level systems to manage runc and provides points in the containers creation to setup various settings after the container has created and/or before it is deleted.
This is commonly used to setup the container's network stack after `create` but before `start` where the user's defined process will be running.

#### Supervisors

`runc` can be used with process supervisors and init systems to ensure that containers are restarted when they exit.
An example systemd unit file looks something like this.

```systemd
[Unit]
Description=Start My Container

[Service]
Type=forking
ExecStart=/usr/local/sbin/runc run -d --pid-file /run/mycontainerid.pid mycontainerid
ExecStopPost=/usr/local/sbin/runc delete mycontainerid
WorkingDirectory=/mycontainer
PIDFile=/run/mycontainerid.pid

[Install]
WantedBy=multi-user.target
```
# runc Integration Tests

Integration tests provide end-to-end testing of runc.

Note that integration tests do **not** replace unit tests.

As a rule of thumb, code should be tested thoroughly with unit tests.
Integration tests on the other hand are meant to test a specific feature end
to end.

Integration tests are written in *bash* using the
[bats](https://github.com/sstephenson/bats) framework.

## Running integration tests

The easiest way to run integration tests is with Docker:
```
$ make integration
```
Alternatively, you can run integration tests directly on your host through make:
```
$ sudo make localintegration
```
Or you can just run them directly using bats
```
$ sudo bats tests/integration
```
To run a single test bucket:
```
$ make integration TESTFLAGS="/checkpoint.bats"
```


To run them on your host, you will need to setup a development environment plus
[bats](https://github.com/sstephenson/bats#installing-bats-from-source)
For example:
```
$ cd ~/go/src/github.com
$ git clone https://github.com/sstephenson/bats.git
$ cd bats
$ ./install.sh /usr/local
```

> **Note**: There are known issues running the integration tests using
> **devicemapper** as a storage driver, make sure that your docker daemon
> is using **aufs** if you want to successfully run the integration tests.

## Writing integration tests

[helper functions]
(https://github.com/opencontainers/runc/blob/master/test/integration/helpers.bash)
are provided in order to facilitate writing tests.

```sh
#!/usr/bin/env bats

# This will load the helpers.
load helpers

# setup is called at the beginning of every test.
function setup() {
  # see functions teardown_hello and setup_hello in helpers.bash, used to
  # create a pristine environment for running your tests
  teardown_hello
  setup_hello
}

# teardown is called at the end of every test.
function teardown() {
  teardown_hello
}

@test "this is a simple test" {
  runc run containerid
  # "The runc macro" automatically populates $status, $output and $lines.
  # Please refer to bats documentation to find out more.
  [ "$status" -eq 0 ]

  # check expected output
  [[ "${output}" == *"Hello"* ]]
}

```
runc man pages
====================

This directory contains man pages for runc in markdown format.

To generate man pages from it, use this command

    ./md2man-all.sh

You will see man pages generated under the man8 directory.

Libcontainer provides a native Go implementation for creating containers
with namespaces, cgroups, capabilities, and filesystem access controls.
It allows you to manage the lifecycle of the container performing additional operations
after the container is created.


#### Container
A container is a self contained execution environment that shares the kernel of the
host system and which is (optionally) isolated from other containers in the system.

#### Using libcontainer

Because containers are spawned in a two step process you will need a binary that
will be executed as the init process for the container. In libcontainer, we use
the current binary (/proc/self/exe) to be executed as the init process, and use
arg "init", we call the first step process "bootstrap", so you always need a "init"
function as the entry of "bootstrap".

```go
func init() {
	if len(os.Args) > 1 && os.Args[1] == "init" {
		runtime.GOMAXPROCS(1)
		runtime.LockOSThread()
		factory, _ := libcontainer.New("")
		if err := factory.StartInitialization(); err != nil {
			logrus.Fatal(err)
		}
		panic("--this line should have never been executed, congratulations--")
	}
}
```

Then to create a container you first have to initialize an instance of a factory
that will handle the creation and initialization for a container.

```go
factory, err := libcontainer.New("/var/lib/container", libcontainer.Cgroupfs, libcontainer.InitArgs(os.Args[0], "init"))
if err != nil {
	logrus.Fatal(err)
	return
}
```

Once you have an instance of the factory created we can create a configuration
struct describing how the container is to be created. A sample would look similar to this:

```go
defaultMountFlags := syscall.MS_NOEXEC | syscall.MS_NOSUID | syscall.MS_NODEV
config := &configs.Config{
	Rootfs: "/your/path/to/rootfs",
	Capabilities: []string{
		"CAP_CHOWN",
		"CAP_DAC_OVERRIDE",
		"CAP_FSETID",
		"CAP_FOWNER",
		"CAP_MKNOD",
		"CAP_NET_RAW",
		"CAP_SETGID",
		"CAP_SETUID",
		"CAP_SETFCAP",
		"CAP_SETPCAP",
		"CAP_NET_BIND_SERVICE",
		"CAP_SYS_CHROOT",
		"CAP_KILL",
		"CAP_AUDIT_WRITE",
	},
	Namespaces: configs.Namespaces([]configs.Namespace{
		{Type: configs.NEWNS},
		{Type: configs.NEWUTS},
		{Type: configs.NEWIPC},
		{Type: configs.NEWPID},
		{Type: configs.NEWUSER},
		{Type: configs.NEWNET},
	}),
	Cgroups: &configs.Cgroup{
		Name:   "test-container",
		Parent: "system",
		Resources: &configs.Resources{
			MemorySwappiness: nil,
			AllowAllDevices:  nil,
			AllowedDevices:   configs.DefaultAllowedDevices,
		},
	},
	MaskPaths: []string{
		"/proc/kcore",
		"/sys/firmware",
	},
	ReadonlyPaths: []string{
		"/proc/sys", "/proc/sysrq-trigger", "/proc/irq", "/proc/bus",
	},
	Devices:  configs.DefaultAutoCreatedDevices,
	Hostname: "testing",
	Mounts: []*configs.Mount{
		{
			Source:      "proc",
			Destination: "/proc",
			Device:      "proc",
			Flags:       defaultMountFlags,
		},
		{
			Source:      "tmpfs",
			Destination: "/dev",
			Device:      "tmpfs",
			Flags:       syscall.MS_NOSUID | syscall.MS_STRICTATIME,
			Data:        "mode=755",
		},
		{
			Source:      "devpts",
			Destination: "/dev/pts",
			Device:      "devpts",
			Flags:       syscall.MS_NOSUID | syscall.MS_NOEXEC,
			Data:        "newinstance,ptmxmode=0666,mode=0620,gid=5",
		},
		{
			Device:      "tmpfs",
			Source:      "shm",
			Destination: "/dev/shm",
			Data:        "mode=1777,size=65536k",
			Flags:       defaultMountFlags,
		},
		{
			Source:      "mqueue",
			Destination: "/dev/mqueue",
			Device:      "mqueue",
			Flags:       defaultMountFlags,
		},
		{
			Source:      "sysfs",
			Destination: "/sys",
			Device:      "sysfs",
			Flags:       defaultMountFlags | syscall.MS_RDONLY,
		},
	},
	UidMappings: []configs.IDMap{
		{
			ContainerID: 0,
			HostID: 1000,
			Size: 65536,
		},
	},
	GidMappings: []configs.IDMap{
		{
			ContainerID: 0,
			HostID: 1000,
			Size: 65536,
		},
	},
	Networks: []*configs.Network{
		{
			Type:    "loopback",
			Address: "127.0.0.1/0",
			Gateway: "localhost",
		},
	},
	Rlimits: []configs.Rlimit{
		{
			Type: syscall.RLIMIT_NOFILE,
			Hard: uint64(1025),
			Soft: uint64(1025),
		},
	},
}
```

Once you have the configuration populated you can create a container:

```go
container, err := factory.Create("container-id", config)
if err != nil {
	logrus.Fatal(err)
	return
}
```

To spawn bash as the initial process inside the container and have the
processes pid returned in order to wait, signal, or kill the process:

```go
process := &libcontainer.Process{
	Args:   []string{"/bin/bash"},
	Env:    []string{"PATH=/bin"},
	User:   "daemon",
	Stdin:  os.Stdin,
	Stdout: os.Stdout,
	Stderr: os.Stderr,
}

err := container.Run(process)
if err != nil {
	container.Destroy()
	logrus.Fatal(err)
	return
}

// wait for the process to finish.
_, err := process.Wait()
if err != nil {
	logrus.Fatal(err)
}

// destroy the container.
container.Destroy()
```

Additional ways to interact with a running container are:

```go
// return all the pids for all processes running inside the container.
processes, err := container.Processes()

// get detailed cpu, memory, io, and network statistics for the container and
// it's processes.
stats, err := container.Stats()

// pause all processes inside the container.
container.Pause()

// resume all paused processes.
container.Resume()

// send signal to container's init process.
container.Signal(signal)

// update container resource constraints.
container.Set(config)
```


#### Checkpoint & Restore

libcontainer now integrates [CRIU](http://criu.org/) for checkpointing and restoring containers.
This let's you save the state of a process running inside a container to disk, and then restore
that state into a new process, on the same machine or on another machine.

`criu` version 1.5.2 or higher is required to use checkpoint and restore.
If you don't already  have `criu` installed, you can build it from source, following the
[online instructions](http://criu.org/Installation). `criu` is also installed in the docker image
generated when building libcontainer with docker.


## Copyright and license

Code and documentation copyright 2014 Docker, inc. Code released under the Apache 2.0 license.
Docs released under Creative commons.

## nsenter

The `nsenter` package registers a special init constructor that is called before 
the Go runtime has a chance to boot.  This provides us the ability to `setns` on 
existing namespaces and avoid the issues that the Go runtime has with multiple 
threads.  This constructor will be called if this package is registered, 
imported, in your go application.

The `nsenter` package will `import "C"` and it uses [cgo](https://golang.org/cmd/cgo/)
package. In cgo, if the import of "C" is immediately preceded by a comment, that comment, 
called the preamble, is used as a header when compiling the C parts of the package.
So every time we  import package `nsenter`, the C code function `nsexec()` would be 
called. And package `nsenter` is now only imported in `main_unix.go`, so every time
before we call `cmd.Start` on linux, that C code would run.

Because `nsexec()` must be run before the Go runtime in order to use the
Linux kernel namespace, you must `import` this library into a package if
you plan to use `libcontainer` directly. Otherwise Go will not execute
the `nsexec()` constructor, which means that the re-exec will not cause
the namespaces to be joined. You can import it like this:

```go
import _ "github.com/opencontainers/runc/libcontainer/nsenter"
```

`nsexec()` will first get the file descriptor number for the init pipe
from the environment variable `_LIBCONTAINER_INITPIPE` (which was opened
by the parent and kept open across the fork-exec of the `nsexec()` init
process). The init pipe is used to read bootstrap data (namespace paths,
clone flags, uid and gid mappings, and the console path) from the parent
process. `nsexec()` will then call `setns(2)` to join the namespaces
provided in the bootstrap data (if available), `clone(2)` a child process
with the provided clone flags, update the user and group ID mappings, do
some further miscellaneous setup steps, and then send the PID of the
child process to the parent of the `nsexec()` "caller". Finally,
the parent `nsexec()` will exit and the child `nsexec()` process will
return to allow the Go runtime take over.

NOTE: We do both `setns(2)` and `clone(2)` even if we don't have any
CLONE_NEW* clone flags because we must fork a new process in order to
enter the PID namespace.



