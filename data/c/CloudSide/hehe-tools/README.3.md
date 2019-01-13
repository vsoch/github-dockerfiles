deis-builder加速

```
DEIS_RELEASE=v1.12.2
docker build -t hehe/builder:${DEIS_RELEASE} . && \
docker tag -f hehe/builder:${DEIS_RELEASE} localhost:5000/deis/builder:${DEIS_RELEASE} && \
docker push localhost:5000/deis/builder:${DEIS_RELEASE}
```

```
BACKEND_HOST=daocloud.io
DEIS_RELEASE=v1.12.2
docker build -t hehe/builder:${DEIS_RELEASE} . && \
docker tag -f hehe/builder:${DEIS_RELEASE} ${BACKEND_HOST}/cloudmario/builder:${DEIS_RELEASE} && \
docker push ${BACKEND_HOST}/cloudmario/builder:${DEIS_RELEASE}
```
