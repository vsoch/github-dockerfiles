############################################################
# Dockerfile for SAR processing container images
# Based on Ubuntu
#
# Docker Build:
# docker build -t satsargroup/sar-docker:0.1 .
#
# Docker Run: 
# docker run -it satsargroup/sar-docker:0.1 /bin/bash
#
# Docker Run Jupyter:
# docker run -i -t -p 8888:8888 satsargroup/sar-docker:0.1 /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser"
# 
# Docker Run with X11-window
# docker run -it --rm \
#  --env DISPLAY=$DISPLAY --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
#  -v=$(pwd)/..:$(pwd)/.. -w=$(pwd) \
#  satsargroup/sar-docker:0.1 \
#  /script/to/run; 
# 
# Docker Misc:
# Show all images: docker images
# Remove all untagged images: docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
# ############################################################

FROM phusion/baseimage

MAINTAINER Colin Schwegmann <cschwegmann@csir.co.za> version: 0.1

# Environmental values
ENV PYTHON_VERSION 2.7
ENV OPENCV_VERSION 3.2.0
ENV NUM_CORES 4
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

############ Install Conda with Python 2.7 #################################################

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda2-4.3.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

# Install the necessary prerequisites for the next sections
RUN apt-get install -y libpng12-dev libgtk2.0-0 python-dev

# Set/Add path
ENV PATH /opt/conda/bin:/opt/conda/lib:/usr/local/lib/python2.7/site-packages:$PATH

############ Done installing Conda with Python 2.7 #################################################


############ Install OpenCV 3.2.0 #################################################

# Get necessary installs 
RUN apt-get -y update -qq && \
    apt-get -y install python$PYTHON_VERSION-dev wget unzip \
                       build-essential cmake git pkg-config libatlas-base-dev \
                       # gfortran \
                       libgtk2.0-dev \
                       libavcodec-dev libavformat-dev \
                       libswscale-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libv4l-dev \
                       qt4-default &&\
    apt-get autoclean autoremove

# Make sure pip is up-to-date
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir numpy matplotlib

# Get OpenCV 3.2.0
RUN git clone --progress https://github.com/opencv/opencv.git &&\
    cd opencv &&\
    git checkout $OPENCV_VERSION &&\
    cd / &&\

# Get OpenCV 3.2.0 contrib modules
    git clone --progress https://github.com/opencv/opencv_contrib &&\
    cd opencv_contrib &&\
    git checkout $OPENCV_VERSION &&\
    mkdir /opencv/build &&\
    cd /opencv/build &&\

# Build OpenCV
    cmake \
      -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_C_EXAMPLES=OFF \
      -D INSTALL_PYTHON_EXAMPLES=OFF \
      -D OPENCV_EXTRA_MODULES_PATH=/opencv_contrib/modules \
      -D BUILD_EXAMPLES=OFF \
      -D BUILD_NEW_PYTHON_SUPPORT=ON \
      -D BUILD_DOCS=OFF \
      -D BUILD_TESTS=OFF \
      -D BUILD_PERF_TESTS=OFF \
      -D BUILD_PYTHON_SUPPORT=ON \
      -D WITH_TBB=ON \
      -D WITH_OPENMP=ON \
      -D WITH_IPP=ON \
      -D WITH_CSTRIPES=ON \
      -D WITH_OPENCL=ON \
      -D WITH_V4L=ON \
      .. &&\
    make -j$NUM_CORES &&\
    make install &&\
    ldconfig &&\

# Clean the install from sources
    cd / &&\
    rm -r /opencv &&\
    rm -r /opencv_contrib 

RUN apt-get -y autoclean && apt-get -y autoremove

############ Done installing opencv 3.2.0 #########################################


############ Install conda required extras ########################################

RUN conda install -y libgcc basemap

############ Done installing conda required extras ################################


############ Install tensorflow ###################################################

RUN pip install tensorflow

############ Done installing tensorflow ###########################################



############ Install OTB 5.10.0 from run files off otb/packages url ################

ADD https://www.orfeo-toolbox.org/packages/OTB-5.10.0-Linux64.run /opt/otb/
ADD https://www.orfeo-toolbox.org/packages/OTB-contrib-5.10.0-Linux64.run /opt/otb/
RUN chmod +x /opt/otb/OTB-5.10.0-Linux64.run
RUN chmod +x /opt/otb/OTB-contrib-5.10.0-Linux64.run
RUN cd /opt/otb/ && ./OTB-5.10.0-Linux64.run && ./OTB-contrib-5.10.0-Linux64.run 
RUN rm /opt/otb/OTB-5.10.0-Linux64.run && rm /opt/otb/OTB-contrib-5.10.0-Linux64.run

############ Done installing OTB ################################################### 


############ Make sure everything is added to the correct paths ####################

RUN ldconfig && touch /etc/ld.so.conf.d/opencv.conf && echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf && ldconfig && \
    echo "PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig" >> /etc/bash.bashrc &&\
    echo "export PKG_CONFIG_PATH" >> /etc/bash.bashrc &&\
    echo "PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages:/opt/otb/OTB-5.10.0-Linux64/lib/python:/opt/otb/OTB-contrib-5.10.0-Linux64/lib/python" >> /etc/bash.bashrc &&\
    echo "export PYTHONPATH" >> /etc/bash.bashrc

############ Correct paths installed ###############################################


# Define default command.
CMD [ "/bin/bash" ]