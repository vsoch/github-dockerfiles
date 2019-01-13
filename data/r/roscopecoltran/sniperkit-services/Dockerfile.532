FROM dpa/python:0.1

ENV PROJECT_NAME rita

## Copiamos los scripts
ADD . /${PROJECT_NAME}/
WORKDIR /${PROJECT_NAME}

RUN curl -LOk https://github.com/nanounanue/get-rita/archive/master.zip

RUN unzip master.zip

WORKDIR /${PROJECT_NAME}/get-rita-master

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "get_rita.py" ]

