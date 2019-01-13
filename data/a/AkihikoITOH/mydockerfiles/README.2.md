# Base image for Jupyter
# [The Jupyter Notebook](http://jdfreder-notebook.readthedocs.org/en/latest/index.html) with IPython, IRKernel, IJulia and some basic packages.

# RUN

```
docker run -it \
  -p 80:8888 \
  -e "PASSWORD=password" \
  -e "USE_HTTP=1" \
  -e "BASE_URL=/" \
  -e "WEBSOCKET_URL=''" \
  akihikoitoh/jupyter:latest
```

# OPTIONS

Currently, only four of [jupyter options](http://jdfreder-notebook.readthedocs.org/en/latest/config.html#options) are available.
