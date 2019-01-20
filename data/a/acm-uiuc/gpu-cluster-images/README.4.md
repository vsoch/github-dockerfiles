# How to use this docker box

Build the caffe2ai/caffe2:gpu-fulloptions-ubuntu16.04 docker image 

Build this image 
```
docker build -t acm-uiuc/caffe2 .
```

Run with NVIDIA Docker 
```
NV_GPU=[device_id] nvidia-docker run --rm -ti --ipc=host -p 8888:8888  -v /vault:/vault --name test acm-uiuc/caffe2
```
