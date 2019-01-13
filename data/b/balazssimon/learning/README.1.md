# Assignment: Build Your Own Image

* Dockerfiles are part process workflow and part art
* Take existing Node.js app and Dockerize it
* Make `Dockerfile`. Build it. Test it. Push it. (rm it). Run it.
* Expect this to be iterative. Rarely do I get it right the first time.
* Details in `dockerfile-assignment-1/Dockerfile`
* Use the Alpine version of the official ' node ' 6.x image
* Expected result is web site at `http://localhost:8000`
* Tag and push to your Docker Hub account (free)
* Remove your image from local cache, run again from Hub

# Solution

```
docker image build -t a04-node .
docker image ls

docker container run --rm -p 8000:3000 a04-node

docker image tag a04-node sbalazs03/a04-node
docker push sbalazs03/a04-node

docker image rm a04-node
docker image ls

docker container run --rm -p 8000:3000 sbalazs03/a04-node
```
