FROM python:3.5
MAINTAINER Centro Academico da Computação - CACo caco@ic.unicamp.br

WORKDIR /code
COPY ./requirements.txt /code

RUN python3 -m pip install -r requirements.txt

RUN echo "America/Sao_Paulo" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

CMD ["uwsgi", "--ini", "/code/uwsgi.ini"]
