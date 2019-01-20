# Captain Teach

This repository contains the implementation of Captain Teach. Yes, the repo is
named admiral-edu.

You might be interested in running Captain Teach. If so, take a look at the
instructions in the file Run.md, which show how to set up a project, download
the images for MySQL and Captain Teach, and start the server.

## Building Captain Teach

If you're interested in building Captain Teach, rather than simply running it,
you'll need to do the following:

1) Install docker on your platform.
2) Add yourself to the docker group.
3) run

`make all`

Please note that step (2) has rather frightening security consequences; the
members of the docker group are essentially root-equivalent. One alternative
is to run the makefile as root, which doesn't sound better to me. As far as
I know, this is a baked-in limitation of Docker. I suppose you could run the
whole build process in a VM, which really seems like one VM too many.....

## Running after Building

Okay, so you built it, and now you want to run it.

1) Follow all of the steps in the Run.md script up until the step labeled
"Start Captain Teach".
2) Take a look at the Makefile, and tweak the path to your configuration
directory, if necessary.
3) Run `make run`, or `make bash`, or `make debug`, as you wish.

