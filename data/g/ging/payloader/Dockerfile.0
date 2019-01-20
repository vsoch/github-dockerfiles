FROM ubuntu:14.04

MAINTAINER aalonsog@dit.upm.es

WORKDIR /opt

# Install Ubuntu dependencies
RUN sudo apt-get update && \
	sudo apt-get install yasm gcc g++ pkg-config make cmake git libgomp1 libglib2.0-dev libboost-regex-dev libboost-thread-dev libboost-system-dev libboost-test-dev libssl-dev liblzma-dev libbz2-dev liblog4cxx10-dev libva-dev libvdpau-dev libxcb-fixes0-dev libxcb-shape0-dev libxcb-shm0-dev -y

# Install ffmpeg
RUN git clone https://github.com/magonzalezc/LHE.git && \
	cd LHE && \
	git checkout -b lhe_develop origin/lhe_develop && \
	./configure --extra-cflags=-fopenmp --extra-ldflags=-fopenmp --enable-shared && \ 
	make && \
	sudo make install
	
#Install OpenCV

#TODO

# Install the project
RUN git clone https://github.com/ging/payloader.git && \
	cd payloader && \
	cmake . && \
	make

WORKDIR /opt/payloader
CMD ./prototype1 media/${INPUT_FILE} media/${OUTPUT_FILE}
