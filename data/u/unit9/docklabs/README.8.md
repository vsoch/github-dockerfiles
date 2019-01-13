# Inspector

Inspector exposes a simple API to query running containers' images and
tags.

## Quickstart

Build it:

    docker build -t unit9/inspector .

Run it:

    docker run -ti --rm \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -p 8600:8600 --name inspector unit9/inspector

Probe it:

    $ docker run -ti --rm --link inspector \
          --name shell --hostname shell unit9/base bash
    root@shell:/# curl inspector:8600/whoami
    {
      "image": "unit9/base",
      "ip": "172.17.0.3",
      "name": "shell",
      "tags": [
        {
          "repository": "unit9/base",
          "tag": "latest"
        }
      ]
    }

Use with `jq`:

    root@shell:/# curl -s inspector:8600/whoami | jq -r .tags[].tag
    latest

## API reference

### GET /

Returns a greeting, and Docker server/client versions:

    {
      "message": "Hello",
      "version": {
        "client": "1.12.5",
        "server": "1.12.5"
      }
    }

### GET /whoami

Tries to match requester's IP address to any running containers, and
inspects the matching container:

    {
      "image": "unit9/base", 
      "ip": "172.17.0.3", 
      "name": "desperate_newton", 
      "tags": [
        {
          "repository": "unit9/base", 
          "tag": "latest"
        }
      ]
    }

### GET /containers

Lists running containers:

    {
      "containers": [
          {
          "id": "6e85cf044d7e", 
          "image": "unit9/base", 
          "names": [
            "shell"
          ]
        },
        {
          "id": "07c92bed3b3c", 
          "image": "unit9/inspector", 
          "names": [
            "inspector"
          ]
        }
      ]
    }

### GET /containers/<name>

Inspects the named container (format identical to `whoami`):

    {
      "image": "unit9/inspector", 
      "name": "inspector", 
      "tags": [
        {
          "repository": "unit9/inspector", 
          "tag": "latest"
        }
      ]
    }
