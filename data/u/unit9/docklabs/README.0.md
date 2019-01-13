# Docker-in-Docker (out of Docker)

Base image for tools / experiments with containers talking to their
host's Docker daemon.

When running, you'd want to mount a volume with the host's
`/var/run/docker.sock` (or equivalent):

    docker run -ti --rm \
        -v /var/run/docker.sock:/var/run/docker.sock \
        unit9/dind

When overriding `rc.local` in your own image, remember to modify the
container's `docker` group's GID to match host's:

    gid=$(ls -ldn /var/run/docker.sock | cut -d' ' -f 4)
    groupmod -g $gid docker

When running the container with the shell as the entry point, you may
want to run `/etc/rc.local` by hand.

When running some service, remember to grant it group membership:

    chpst -u nobody:docker some-app...
