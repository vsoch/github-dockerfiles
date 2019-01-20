FROM acmuiuc/cuda:9.0-cudnn7

MAINTAINER Naren Dasan <sivagna2@illinois.edu>

RUN pip3 --no-cache-dir install \
        mxnet-cu90==1.0.0 \
	ipykernel \
        jupyter \
        matplotlib \
        numpy \
        scipy \
	graphviz \
        sklearn \
        pandas \
        Pillow \
        tensorflow \
        tensorboardX \
        bash_kernel \
        && \
python3 -m bash_kernel.install \
        && \
python3 -m ipykernel.kernelspec

# TensorBoard
EXPOSE 6006
# Jupyter
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


