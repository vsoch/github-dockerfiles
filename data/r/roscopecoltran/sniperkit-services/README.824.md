# docker-sonnet
[![](https://images.microbadger.com/badges/image/smizy/sonnet.svg)](https://microbadger.com/images/smizy/sonnet "Get your own image badge on microbadger.com") 
[![](https://images.microbadger.com/badges/version/smizy/sonnet.svg)](https://microbadger.com/images/smizy/sonnet "Get your own version badge on microbadger.com")
[![build status](https://gitlab.com/smizy/docker-sonnet/badges/master/build.svg)](https://gitlab.com/smizy/docker-sonnet/commits/master)

Python3 [Sonnet](https://github.com/deepmind/sonnet) with Jupyter docker image based on alpine

* numpy, scipy, pandas, scikit-learn, seaborn, tensorflow, sonnet installed via pip. See `pip list --format=columns` for detail.
* CPU only
* Note that this image is experimental.

## Usage
```
# verify
docker run -it --rm smizy/sonnet:1.0-cpu-alpine sh
> python
Python 3.5.2 (default, Dec 22 2016, 10:15:38) 
[GCC 6.2.1 20160822] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sonnet as snt
>>> import tensorflow as tf
>>> snt.resampler(tf.constant([0.]), tf.constant([0.]))
<tf.Tensor 'resampler/Resampler:0' shape=(1,) dtype=float32>

# run examples
> cd /code/examples
> python rnn_shakespeare_test.py 
2017-04-21 08:28:19.513494: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
 :
 :
..
----------------------------------------------------------------------
Ran 2 tests in 867.042s

OK

# jupyter
docker run -it --rm -v $(pwd):/data -w /data -p 8888:8888 smizy/sonnet:1.0-cpu-alpine

```