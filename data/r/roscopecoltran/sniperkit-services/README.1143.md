# docker-gensim
[![](https://images.microbadger.com/badges/image/smizy/gensim.svg)](https://microbadger.com/images/smizy/gensim "Get your own image badge on microbadger.com") 
[![](https://images.microbadger.com/badges/version/smizy/gensim.svg)](https://microbadger.com/images/smizy/gensim "Get your own version badge on microbadger.com")
<!--[![CircleCI](https://circleci.com/gh/smizy/docker-gensim.svg?style=svg&circle-token=2b58baee340c55eef2cbece97ab66da62f5bef7e)](https://circleci.com/gh/smizy/docker-gensim)-->

Gensim docker image based on alpine

## run jupyter notebook
docker run -it --rm  -p 8888:8888 -v $(pwd)/data:/code  smizy/gensim:1.0-alpine