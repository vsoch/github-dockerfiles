# Flipstone Playgrounds

This repository contains a number of minimal Vagrant+Docker environments for playing around with various languages.
To get started with one of the languages, just clone this repo and then:

    ./play <language>
    
A vagrant host will be spun up (using the Docker provider). Once you're done playing, it will be automatically destroyed.

## Files

Any files you put in the `sandbox` directory will be available inside the playground in `/home/vagrant/sandbox`.
Once you're in, just `cd sandbox` to get there!

## Contributing

Please contribute new playgrounds! Just follow the examples, use playground-base (or one of the other playground images)
as your base, and make Dockerfile and VagrantFile. Submit a Pull Request and before merging we will build the image and
push it to hub.docker.com before merging it!
