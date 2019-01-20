# Docker Images

A collection of Dockerfiles and related code for building Docker Images.

## Important Notes

* it should be used only for public images
* images created here should be pushed to the [lonelyplanet](https://hub.docker.com/r/lonelyplanet/) organization on Docker Hub and made public

## Images
Each image has it's own directory

## Tips

* If you need to share the same Docker image between multiple services, consider adding it to this repository
* Same rules apply in case you have some common parts between multiple images
* Extracting common stuff into separate image will optimize build and deployment speed because we avoid repeating the same steps every time when we build image for the specific service
* Try to keep the images slim
* Avoid copying community Dockerfiles, build on top of them (use `FROM`)
