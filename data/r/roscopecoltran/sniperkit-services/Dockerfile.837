FROM dpa/r:0.2

ENV PROJECT_NAME magicloop


## Copiamos los scripts
ADD . /${PROJECT_NAME}/
WORKDIR /${PROJECT_NAME}

RUN mkdir /${PROJECT_NAME}/data

CMD [ "Rscript", "/magicloop/script.R" ]
