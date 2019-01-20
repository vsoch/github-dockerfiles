# How to use this docker box

Build the pytorch-cudnnv6 docker image 

Build this image 
```
docker build -t acm-uiuc/pytorch .
```

Run with NVIDIA Docker 
```
NV_GPU=[device_id] nvidia-docker run --rm -ti --ipc=host -p 8888:8888  -v /vault:/vault --name test acm-uiuc/pytorch
```

Luda
