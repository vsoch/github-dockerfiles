# Docker-Volume-Sync
A docker volume container using [Unison](http://www.cis.upenn.edu/~bcpierce/unison/) for fast two-way folder sync. It is much faster than basic docker bind mounts on either Mac OS X or Windows.  The Docker folks are working on [speeding up the Mac OS X bind mounts](https://docs.docker.com/storage/bind-mounts/#configure-mount-consistency-for-macos) but they are still much slower than native speed.

When the development environment is configured correctly with docker-volume-sync, a developer doesn't need to remember any special commands. They just run `docker-compose up` as they normally would.

docker-volume-sync opens port 5001 after doing an initial sync. Any containers using the synced volume should wait for this port to be open before using the volume. Otherwise they will probably try to access files in the volume that are not there yet. There are several options to use for waiting: [wait-for-it](https://github.com/vishnubob/wait-for-it), [wait-for](https://github.com/eficode/wait-for), and [wait4ports](https://github.com/erikogan/wait4ports).

## Usage

### Compose file

docker-volume-sync is designed to work with compose. Let's say you have a compose file like the one below. It is mounting the host directory `.` to `/app` in the container. The container simply prints the contents of a file and then exits.

```yaml
version: '3'
services:
  app:
    build:
      context: .
    command: ["cat", "/app/test_files/zzz.txt"]
    volumes:
      - .:/app
```

To use docker-volume-sync you would change it to look like this:

```yaml
version: '3'
services:
  sync:
    image: concordconsortium/docker-volume-sync
    volumes:
      - sync-volume:/data
      - .:/host_data
  app:
    build:
      context: .
    entrypoint: ["/bin/bash", "/usr/local/bin/wait-for-it.sh", "sync:5001", "-s", "-t", "30", "--"]
    command: ["cat", "/app/test_files/zzz.txt"]
    depends_on: [ sync ]
    volumes:
      - sync-volume:/app
volumes:
  sync-volume:
```

You also need to change the app image to install the wait-for-it script. See the Waiting for Port section below.

These changes to the compose file can also be done using an overlay, so your original compose file can remain untouched. This overlay would look like this:

```yaml
version: '3'
services:
  sync:
    image: concordconsortium/docker-volume-sync
    volumes:
      - sync-volume:/data
      - .:/host_data
  app:
    entrypoint: ["/bin/bash", "/usr/local/bin/wait-for-it.sh", "sync:5001", "-s", "-t", "30", "--"]
    depends_on: [ sync ]
    volumes:
      - sync-volume:/app
volumes:
  sync-volume:
```

### Waiting for Port

In the example above wait-for-it is used to wait for the port. The Dockerfile for that app service is this:

```Dockerfile
FROM alpine:edge

RUN apk --no-cache add bash ca-certificates

WORKDIR /usr/local/bin
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/db049716e42767d39961e95dd9696103dca813f1/wait-for-it.sh && \
    chmod +x wait-for-it.sh

CMD ["cat", "/app/test_files/zzz.txt"]
```

wait-for-it requires bash, so bash is added, then the  wait-for-it script is downloaded, and made executable.

### Configuration

docker-volume-sync has a few environment variables that you can alter.

`UNISON_DIR` - This is the directory which receives data from unison inside docker-volume-sync. This is the directory you should use in other containers. The default is `/data`

`UNISON_HOST_DIR` - This should be the mounted host volume. docker-volume-sync will sync this directory with `UNISON_DIR`. The default is `/host_data`

`UNISON_GID` - Group ID for the user running unison inside container.

`UNISON_UID` - User ID for the user running unison inside container.

`UNISON_USER` - User name for the sync user ( UID matters more )

`UNISON_GROUP` - Group name for the sync user ( GID matters more )

### Without Waiting

If you can't modify the containers using the synced volume to wait for the port, then you shouldn't add the docker-volume-sync service to your app's docker compose file.  Instead you should run it separately. Then you should manually wait for the first sync to complete before starting any containers using the synced volume.

## Edge cases

docker-volume-sync tries to emulate a simple [docker bind mounted volume](https://docs.docker.com/storage/bind-mounts/). As such it treats the UNISON_HOST_DIR as the main source of the files. If there is a conflict it will use the file in the UNISON_HOST_DIR.  If the container is not running and a file is removed from UNISON_HOST_DIR but not UNISON_DIR, then docker-volume-sync will delete the file in UNISON_DIR when it starts up.

If docker-volume-sync has been removed and you make changes in UNISON_DIR, when docker-volume-sync starts up you will lose those changes. This is roughly what happens with a bind mount. If you unmount the bind mount, then add files to the unmounted directory, those changes will appear lost when the volume is mounted again. The difference is what the directory looks like when it is disconnected. With a bind mount the directory is empty, with docker-volume-sync the directory will continue to have the files in it. (assuming you just remove docker-volume-sync and don't remove the sync-volume). This has not been a problem in practice, if it causes problems for you, please file an issue, there might be a way to improve the behavior.

## Testing

There are no automated tests. But the files in `demo` can be used to run a manual test.

First cd into `demo`

Then run `generate_test_files.sh` this will generate 200 random files in a test_files directory.

Then run `docker-compose up`. Docker compose will build a image for a `sync` service and a image for a `app` service.  After these images are built you should see the `sync` service syncing all of the random files. And you should see the `app` image waiting for the files to be sync'd before printing the contents of the zzz.txt file.

## Credits
This is based off of https://github.com/onnimonni/docker-unison

The idea of bridging two volumes with unison running internally came from [docker-sync](https://github.com/EugenMayer/docker-sync)

## License
This docker image is licensed under GPLv3 because Unison is licensed under GPLv3 and is included in the image. See LICENSE.
