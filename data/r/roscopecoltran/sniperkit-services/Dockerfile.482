FROM dpa/spark-client:0.1

ENV PROJECT_NAME dummy

## Copiamos los scripts
ADD . /${PROJECT_NAME}/
WORKDIR /${PROJECT_NAME}

## Instalamos el requirements.txt (si existe)
RUN [ -f /${PROJECT_NAME}/requirements.txt ] && pip install -r /${PROJECT_NAME}/requirements.txt

ENTRYPOINT [ "spark-submit", "/dummy/spark-script.py" ]


