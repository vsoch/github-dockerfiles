# This builds a docker image to reproducibly build our IPython
# notebook.
FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade --yes
RUN apt-get install --yes texlive-fonts-recommended texlive-latex-extra \
    texlive-latex-base python-progressbar \
    python-matplotlib python-numpy \
    python-scipy python-sympy supervisor inkscape \
    pandoc jq python-h5py build-essential libzmq3-dev \
    python-pip

RUN apt-get install --yes pkg-config

RUN apt-get remove --yes ipython
RUN pip install ipython==2.3.0
RUN pip install runipy==0.1.1

ADD . /asymmetric-motion
WORKDIR /asymmetric-motion/tutorial-src

CMD ["/usr/bin/make","website-tarball"]
