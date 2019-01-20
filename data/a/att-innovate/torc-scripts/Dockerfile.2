FROM phusion/baseimage:0.9.17

RUN apt-get update
RUN apt-get install -y nodejs npm git && \
	ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install -g bower
RUN sudo npm install http-server -g

RUN git clone https://github.com/att-innovate/charmander-vector.git && \
	cd charmander-vector && \
	git checkout fc9fd9cb94f7afb75ada6cbece99e1b8cb39ea4e

ENV METADATAURL wedge

RUN cd charmander-vector && \
	sed -i -- 's/false/true/' src/app/containerResolver.js &&\
	sed -i -- "s/wedge-fb-1/$METADATAURL/" src/app/containerResolver.js &&\
	bower --allow-root install --config.interactive=false && \
	npm install && \
	npm install --global gulp && \
	gulp
WORKDIR charmander-vector/dist
ENTRYPOINT ["http-server", "--cors"]
CMD ["-p 33100"]
