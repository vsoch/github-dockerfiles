FROM acmuiuc/cuda:9.0-cudnn7

MAINTAINER Naren Dasan <sivagna2@illinois.edu>

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

RUN pip3 --no-cache-dir install \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        scipy \
        sklearn \
        pandas \
        Pillow \
        && \
    python3 -m ipykernel.kernelspec

# Install TensorFlow GPU version.
RUN  pip3 --no-cache-dir install \
    tensorflow-gpu

RUN pip3 install keras
# For CUDA profiling, TensorFlow requires CUPTI.
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

# TensorBoard
EXPOSE 6006
# IPython
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
