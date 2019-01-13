# alpine-python3-tensorflow
python 3.6.1 with

bleach==1.5.0
certifi==2017.7.27.1
chardet==3.0.4
cycler==0.10.0
Cython==0.26
decorator==4.1.2
FALCONN==2.0.0
html5lib==0.9999999
idna==2.6
Keras==2.0.6
Markdown==2.6.9
matplotlib==2.0.2
networkx==1.11
numpy==1.13.1
olefile==0.44
pandas==0.20.3
Pillow==4.2.1
protobuf==3.4.0
pyparsing==2.2.0
python-dateutil==2.6.1
pytz==2017.2
PyWavelets==0.5.2
PyYAML==3.12
requests==2.18.4
scikit-image==0.13.0
scikit-learn==0.19.0
scipy==0.19.1
six==1.10.0
tensorflow==1.3.0
tensorflow-tensorboard==0.1.4
tensorlayer==1.6.1
Theano==0.9.0
urllib3==1.22
Werkzeug==0.12.2


This is heavily inspired by https://github.com/tatsushid/docker-alpine-py3-tensorflow-jupyter/ Docker image.
Docker image with alpine + Python3 + TensolFlow + Jupyter
=========================================================

This provides a Docker image with

- Alpine
- Python3
- TensolFlow
- Juptyer

This is heavily inspired by https://hub.docker.com/r/enakai00/jupyter_tensorflow/
Docker image.

## Supported tags and respective `Dockerfile` links

- [`1.3.0`, `latest`](https://github.com/tatsushid/docker-alpine-py3-tensorflow-jupyter/blob/master/Dockerfile)

## How to use this image

Please run the following

```shellsession
docker run -itd -p 8888:8888 -e PASSWORD=foobar tatsushid/alpine-py3-tensorflow-jupyter
```

and access to `http://{docker host}:8888/`. It opens Jupyter's login panel so
please enter the password which you specified as `PASSWORD` environment value

This repository also provides Docker Compose example so you can boot a
container of this image by running

```shellsession
docker-compose up
```

in `docker_compose_example` directory.

## License
This alpine-py3-tensorflow-jupyter Docker image is under MIT License. See the
[LICENSE][license] file for details.

[license]: https://github.com/tatsushid/docker-alpine-py3-tensorflow-jupyter/blob/master/LICENSE
Docker Compose Example
======================

This is Docker Compose example. You can boot a container based on this
repository image with Jupyter port 8888, its password 'foobar' and sharing
files in `notebook` directory with the container by just running

```shellsession
docker-compose up
```

To stop it, please press 'Ctrl-C'.
Notebook Directory
==================

If you put files into this directory and boot a container by docker-compose
with an example `docker-compose.yml` in a parent directory, all files in this
directory are shared with the container and placed at `/root/notebook/my_notes`
in the container. It can be also used from Jupyter as `my_notes`.
