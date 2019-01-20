# How to use this Dockerfile

To run a Payloader container you have two options: 

- You can build your own image using the Dockerfile we provide and then run the container from it or
- you can run the container directly from the image we provide in Docker Hub.

Both options require that you have [docker](https://docs.docker.com/installation/) installed on your machine.

## Build your own image and run the container from it

You have to download the [Payloader's code](https://github.com/ging/payloader) from GitHub and navigate to `docker` directory. There, to compile your own image just run:

	sudo docker build -t payloader-image .


> **Note**
> If you do not want to have to use `sudo` in this or in the next section follow [these instructions](https://docs.docker.com/installation/ubuntulinux/#create-a-docker-group).

This builds a new Docker image following the steps in `Dockerfile` and saves it in your local Docker repository with the name `payloader-image`. You can check the available images in your local repository using: 

	sudo docker images


> **Note**
> If you want to know more about images and the building process you can find it in [Docker's documentation](https://docs.docker.com/userguide/dockerimages/).

Now you can run a new container from the image you have just created with:

	sudo docker run --name my-container -v /path/to/your/videos/folder:/opt/payloader/media -e INPUT_FILE=<input_file> -e OUTPUT_FILE=<output_file> payloader-image 


Where the different params mean: 

* my-container is the name of the new container (you can use the name you want)
* /path/to/your/videos/folder: here you have to specify the folder where your input video is located. The output video will be created also there.
* input_file is the source of the media stream
* output_file is the destination of the media stream

Here is an example of this command:

	sudo docker run --name payloader-container payloader-image myvideo.avi outputvideo.avi


## Run the container from the last release in Docker Hub

You can also run the container from the [image we provide](https://hub.docker.com/r/ging/payloader/) in Docker Hub. In this case you have only to execute the run command. But now the image name is ging/payloader:*version* where `version` is the release you want to use:

	sudo docker run --name my-container -v /path/to/your/videos/folder:/opt/payloader/media -e INPUT_FILE=<input_file> -e OUTPUT_FILE=<output_file> ging/payloader

> **Note**
> If you do not specify a version you are pulling from `latest` by default.
