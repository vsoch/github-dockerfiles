FROM python:3.6

RUN mkdir /project

ADD requirements.txt /project/requirements.txt
RUN pip install -r /project/requirements.txt

ADD . /project

CMD ["python", "/project/manage.py"]