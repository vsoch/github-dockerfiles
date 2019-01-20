# linkeddata-trifid
Trifid-LD deployment for swisstopo SPARQL Endpoint

Build with:
     docker build -t geoadmin .


Run with:
     docker run -p 8080:8080 geoadmin

This is intended to be run behind a forward proxy that listens on the host an
port corresponing to the namespace used in the data.