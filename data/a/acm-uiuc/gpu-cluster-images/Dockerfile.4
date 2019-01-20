FROM acmuiuc/cuda:9.0-cudnn7
MAINTAINER Naren Dasan <sivagna2@illinois.edu>

# caffe2 install with gpu support

RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel && \
    pip3 install --no-cache-dir \
    flask \
    future \
    graphviz \
    hypothesis \
    jupyter \
    matplotlib \
    numpy \
    protobuf \
    pydot \
    python-nvd3 \
    pyyaml \
    requests \
    scikit-image \
    scipy \
    setuptools \
    six \
    tornado

RUN apt-get -qq update && apt-get -qq -y install curl bzip2 \
    && curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
    && bash /tmp/miniconda.sh -bfp /usr/local \
    && rm -rf /tmp/miniconda.sh \
    && conda install -y python=3 \
    && conda update conda \
    && apt-get -qq -y remove curl bzip2 \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && conda clean --all --yes

ENV PYTHONPATH /usr/local
   
RUN python3 -m pip --no-cache-dir install \
        ipykernel \
        matplotlib \
        sklearn \
        pandas \
        Pillow \
        bash_kernel \
        flask \
    	pydot \
	ipython \
    	leveldb \
    	lmdb \
    	notebook \
	 && \
python3 -m bash_kernel.install \
        && \
python3 -m ipykernel.kernelspec

RUN conda install -c caffe2 caffe2-cuda9.0-cudnn7

EXPOSE 8888

RUN mkdir /opt/cluster-container
RUN cd /opt/cluster-container

COPY start-jupyter.sh /opt/cluster-container
COPY jupyter_get.py /opt/cluster-container
RUN mkdir /examples
COPY mnist.py /examples
COPY jupyter_notebook_config.py /root/.jupyter/
RUN chmod +x /opt/cluster-container/start-jupyter.sh

WORKDIR "/vault"

CMD ["/opt/cluster-container/start-jupyter.sh",  "--allow-root"]


