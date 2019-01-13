# docker-jupyter

Jupyter docker image based on alpine 

```
docker build -t local/jupyter .
docker build -f Dockerfile.nlp -t local/jupyter:nlp .

# run Jupyter Notebook container 
docker run  -p 8888:8888 -v $(pwd):/code  -d local/jupyter:nlp

# open browser
open http://$(docker-machine ip default):8888
```
