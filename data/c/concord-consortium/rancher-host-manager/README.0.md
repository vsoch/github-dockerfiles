This small container is to fix a few issues we've had while using Rancher.
It should be run in the userlevel docker, and be configured with the following
environment variables:

    RANCHER_URL:
    RANCHER_ACCESS_KEY:
    RANCHER_SECRET_KEY:

When it is launched it will track down the host in rancher that the container is running on.
Then it will update that host definition with some data from the EC2 meta data.

Dockerhub should be building the image from this repository:
https://hub.docker.com/r/concordconsortium/rancher-host-manager/

### Possible Reaping Support

In the future this might also support running in system mode and automatically
removing a host from rancher when the EC2 host shutdown.

If it is run this way it should be treated specially because it will try to remove the host with a matching name from rancher. In theory the rancher introspection service won't be able available to this container because it is
running as a system service. But we should be able to find the host by name using the rancher api. That
assumes the userlevel container has been run and it correctly sets the EC2 info.

One thing that we need to test is what happens if the machine is stopped in AWS and then restarted.
With this container the host will be deleted from rancher, hopefully it will just be added again after the restart.

Updating the Gemfile.lock:
- Change Gemfile
- run docker-compose run app bundle install
- run docker-compose build
   (this is not strictly necessary but useful to make sure you didn't break anything)
