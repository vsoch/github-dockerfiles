# git-sync

git-sync is a command that pull a git repository to a local directory.

It can be used to source a container volume with the content of a git repo.

## Usage

```
# build the container
docker build -t git-sync .
# run the git-sync container
docker run -d GIT_SYNC_REPO=https://github.com/GoogleCloudPlatform/kubernetes GIT_SYNC_DEST=/git -e GIT_SYNC_BRANCH=gh-pages -r HEAD GIT_SYNC_DEST=/git -v /git-data:/git git-sync
# run a nginx container to serve sync'ed content
docker run -d -p 8080:80 -v /git-data:/usr/share/nginx/html nginx 
```
# git-blog-demo

This demo shows how to use the `git-sync` sidekick container along side `volumes` and `volumeMounts` to create a markdown powered blog.

## How it works

The pod is composed of 3 containers that share directories using 2 volumes:

- The `git-sync` container clones a git repo into the `markdown` volume
- The `hugo` container read from the `markdown` volume and render it into the `html` volume.
- The `nginx` container serve the content from the `html` volume.

## Usage

Build the demo containers, and push them to a registry

```
docker build -t <some-registry>/git-sync ..
docker build -t <some-registry>/hugo hugo/
docker push <some-registry>/hugo <some-registry>/git-sync
```

Create the pod and the service for the blog

```
kubectl pods create config/pod.html
kubectl services create config/pod.html
```

Open the service external ip in your browser
# hugo

`hugo` is a container that convert markdown into html using [hugo static site generator](http://gohugo.io/).

## Usage

```
# build the container
docker build -t hugo .
# run the hugo container
docker run -e HUGO_BASE_URL=example.com -v /path/to/md:/src -v /path/to/html:/dest hugo
``
