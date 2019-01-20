FROM acmuiuc/cuda:9.0-cudnn7

LABEL maintainer "Naren Dasan <sivagna2@illinois.edu>" \
      com.microsoft.cntk.version="2.4"

ENV CNTK_VERSION="2.4"

RUN apt-get update && apt-get install -y --no-install-recommends \
        unzip \
        vim \
        emacs24 \
        nano \
        curl \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

RUN pip3 --no-cache-dir install \
	https://cntk.ai/PythonWheel/GPU/cntk-2.4-cp35-cp35m-linux_x86_64.whl

RUN pip3 --no-cache-dir install \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        scipy \
        sklearn \
        pandas \
        Pillow \
        bash_kernel \
        && \
python3 -m bash_kernel.install \
        && \
python3 -m ipykernel.kernelspec

#RUN ln -s /usr/bin/python3 /usr/bin/python

COPY jupyter_notebook_config.py /root/.jupyter/

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
