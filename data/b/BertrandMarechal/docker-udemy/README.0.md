# Take existing Node.js app and Dockerize it

Lecture 40

- [x] Make dockerfile
- [x] Build it
- [x] Test it
- [x] Push it
- [x] Remove from cache
- [x] Run it

Use the alpine version of the official node:6.x image
Expect result to be seen in localhost

[Answers](https://www.udemy.com/docker-mastery/learn/v4/t/lecture/6806640?start=0)

```bat
# build
docker image build -t dockerfile-assignment-1 .

# run it
docker container run -p 80:3000 --rm dockerfile-assignment-1

# tag it
docker image tag dockerfile-assignment-1:latest bertrandmarechal/dockerfile-assignment-1:latest

# push it
docker image push bertrandmarechal/dockerfile-assignment-1:latest

# remove from cache
docker image rm bertrandmarechal/dockerfile-assignment-1

# rerun it
docker container run -p 80:3000 --rm bertrandmarechal/dockerfile-assignment-1
```