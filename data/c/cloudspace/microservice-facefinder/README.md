# microservice-facefinder
Experiments in finding faces within video footage using OpenCV.

There are currently three parts to this:

#Server
Responsible for showing the mjpeg stream produced.
Runs in Sinatra.

#Capture Engine
Gets images and forwards them on to Geec.

#Docker image
Produces the docker image.
