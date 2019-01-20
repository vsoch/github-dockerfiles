FROM bde2020/hadoop-base:1.1.0-hadoop2.7.1-java8
MAINTAINER Alexandre Abadie <alexandre.abadie@gmail.com>

RUN apt-get update -yqq  && apt-get install -yqq \
  wget \
  bzip2 \
  git \
  libglib2.0-0 \
  vim \
  make \
  && rm -rf /var/lib/apt/lists/*

# Configure environment
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /work

RUN wget -O miniconda.sh \
  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
  && bash miniconda.sh -b -p /work/miniconda \
&& rm miniconda.sh

ENV PATH="/work/bin:/work/miniconda/bin:$PATH"

# Create environment for python 3.5
COPY conda-environment.yml /work/conda-environment.yml
RUN conda env create -n py35 python=3.5 --file conda-environment.yml

# Required for libhdfs3
RUN conda install -y -n py35 -c clinicalgraphics libgcrypt11

# Use conda py35 environment by default
ENV PATH /work/miniconda/envs/py35/bin:$PATH

WORKDIR /shared

CMD ["bash"]
