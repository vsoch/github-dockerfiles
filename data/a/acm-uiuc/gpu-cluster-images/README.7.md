# How to use this docker box

Build the nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04 docker image 

Build this image 
```
docker build -t acm-uiuc/mxnet .
```

Run with NVIDIA Docker 
```
NV_GPU=[device_id] nvidia-docker run --rm -ti --ipc=host -p 8888:8888 -p 6006:6006 -v /vault:/vault --name test acm-uiuc/mxnet
```
