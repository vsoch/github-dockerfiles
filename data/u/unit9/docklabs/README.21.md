# Locust dockerized

See <http://locust.io/> for docs on Locust itself.

## Build

Builds are automated via DockerHub, but in case you need to build
manually:

    docker build -t unit9/locust .

## Specifying the target

Use the `TARGET` environment variable, and set it to the root URL of
the tested website, e.g. `http://example.org`.

## Providing the Locustfile

The Locustfile (`locustfile.py`) can come either from a URL (by
setting `LOCUSTFILE_URL`), or from a local directory (by using a
volume mounted at `/app/tests`).

1. Using volumes:

        docker run -it --rm -p 8089:8089 \
            -v /some/path:/app/tests \
            -e TARGET=http://example.org \
            unit9/locust

    Useful in local development.

2. Using URLs:

        docker run -it --rm -p 8089:8089 \
            -e LOCUSTFILE_URL=http://example.com/locustfile.py \
            -e TARGET=http://example.org \
            unit9/locust

    You can pull a Locustfile directly from a private Bitbucket git
    repo, by embedding the API key in the URL (`<commit>` can be short
    id, long id, branch name, `HEAD`, etc):

        https://<user>:<api_key>@bitbucket.org/<user>/<repo>/raw/<commit>/locustfile.py

## Running in master/slave mode

For the controlling node, set `MASTER_MODE` to 1, expose the web UI,
and C&C (command & control) ports:

    docker run -it --rm \
        -p 8089:8089 \
        -p 5557:5557 \
        -p 5558:5558 \
        -e LOCUSTFILE_URL=http://example.com/locustfile.py \
        -e TARGET=http://example.org \
        -e MASTER_MODE=1 \
        unit9/locust

(For C&C, you might want to filter the master's incoming connections
on your firewall to only allow the slave pool's IP address range!)

For slave nodes, provide the same Locustfile and `TARGET`, but don't
expose any ports, and specify the master's hostname / IP (NOT url):

    docker run -it --rm \
        -e LOCUSTFILE_URL=http://example.com/locustfile.py \
        -e TARGET=http://example.org \
        -e MASTER_HOST=locust.example.com \
        unit9/locust

## Tips for running on Kubernetes

Assuming everything runs in the "default" namespace.

- Create a replication controller for the master as usual, exposing a
  service on the ports for HTTP (you can map 80:8089) and C&C (5557,
  5558); you can name the service `locust`.

- Create another RC for the slave pool; you can scale it manually to
  the desired capacity. Set `MASTER_HOST` to
  `locust.default.svc.cluster.local`. There's no need for exposing a
  service (slaves connect to the master for C&C). Name it something
  like `locust-slave`.

- If you need to re-fetch the Locustfile after an update, all you need
  is to kill all existing pods (master and slaves). The replication
  controller will spawn new pods, and the startup script will pull the
  changed file. It's quite easy from the CLI:

        kubectl delete pods -l app=locust
        kubectl delete pods -l app=locust-slave

- If you need to roll out an updated image on an existing replication
  controller:

        kubectl rolling-update locust \
            --image unit9/locust:latest \
            --image-pull-policy Always \
            --update-period 1s
