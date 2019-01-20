FROM pytorch_cuda9

MAINTAINER Naren Dasan <sivagna2@illinois.edu>

RUN apt-get update && apt-get -y install \
        vim \
        emacs24 \
        nano \
       && \
       apt-get clean && \
       rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        scipy \
        sklearn \
        pandas \
        Pillow \
        torchvision \
        tensorflow \
        tensorboardX \
        bash_kernel \
        && \
python -m bash_kernel.install \
        && \
python -m ipykernel.kernelspec

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


