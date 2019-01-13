# ubuntu-atom/Dockerfile
This dockerfile is the atom text editor in a container.

## Usage example
build and run:

```
docker build -t ubuntu-atom .
docker run -it -e DISPLAY=192.168.99.1:0 --rm ubuntu-atom bash
```

start atom:

```
cd /path/to/workspace
atom .
```
