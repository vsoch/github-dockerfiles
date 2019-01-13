FROM dpa/python:0.1

ENV PROJECT_NAME dummy

## Copiamos los scripts
ADD . /${PROJECT_NAME}/
WORKDIR /${PROJECT_NAME}

RUN mkdir /${PROJECT_NAME}/data

ENTRYPOINT [ "python", "/dummy/script.py" ]

