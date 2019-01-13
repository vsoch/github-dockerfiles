FROM jupyter/all-spark-notebook
MAINTAINER Timothy Hnat twhnat@memphis.edu

# Reference: https://github.com/jupyter/docker-stacks/wiki/Docker-Recipes

# Python3 installs
# RUN pip install 'ggplot==0.6.8'

# Add Live slideshows with RISE
RUN wget https://github.com/pdonorio/RISE/archive/master.tar.gz \
    && tar xvzf *.gz && cd RISE-master && python3 setup.py install \
    && cd .. && rm -rf RISE-master master.tar.gz

# Install Cerebral Cortex libraries for use in the notebook environment
RUN git clone https://github.com/MD2Korg/CerebralCortex \
    && cd CerebralCortex && python3 setup.py install \
    && cd .. && rm -rf CerebralCortex
