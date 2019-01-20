FROM zazukoians/trifid-ld:0.6.2
ADD config.js /usr/src/app/config.js
ADD data /usr/src/app/data
RUN cd /usr/src/app/data && npm install git+https://github.com/rdf-ext/rdf-proxy-middleware.git#develop
