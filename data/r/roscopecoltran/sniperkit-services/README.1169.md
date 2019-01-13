# docker-keras-theano
[![](https://images.microbadger.com/badges/image/smizy/keras-theano.svg)](https://microbadger.com/images/smizy/keras-theano "Get your own image badge on microbadger.com") 
[![](https://images.microbadger.com/badges/version/smizy/keras-theano.svg)](https://microbadger.com/images/smizy/keras-theano "Get your own version badge on microbadger.com")
[![CircleCI](https://circleci.com/gh/smizy/docker-keras-theano.svg?style=svg&circle-token=3d06a409dacb17ef9c99bb4597492887ec9b2050)](https://circleci.com/gh/smizy/docker-keras-theano)

Python3 Keras(Theano backended) with Jupyter docker image based on alpine.

See (https://hub.docker.com/r/smizy/keras/) for Thensorflow backend version

* numpy, scipy, pandas, scikit-learn, seaborn, theano, keras installed via pip. See ` pip list --format=columns` for detail.
* CPU only

## Usage
```
docker run -it --rm -v $(pwd):/data -w /data -p 8888:8888 smizy/keras-theano:1.2.2-cpu-alpine
```