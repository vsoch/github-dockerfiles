# Voormedia Docker base images

There is only one rule, but it is important:

**These are public images. Do NOT add any keys, certificates, passwords.**

## Building a new image

Create a Dockerfile in a new directory, say 'base/Dockerfile'.

Then do something like this:

    ./create base

## Use the image in a project

In your project, use it as follows:

    FROM voormedia/ruby-build:3.7 AS build

    FROM voormedia/ruby:3.7


## Hooray! Have fun!
