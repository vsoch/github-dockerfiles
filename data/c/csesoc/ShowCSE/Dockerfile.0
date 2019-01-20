FROM python:3.5-alpine

# RUN apt-get -y update && \
	# apt-get install -y build-essential python3.4 python3-dev python3-setuptools git
# RUN easy_install3 pip


RUN apk add --no-cache git gcc python3-dev musl-dev libffi-dev
WORKDIR /build/


ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD . /build/
VOLUME /build/Application/static/uploads/
CMD gunicorn -c gunicorn.py Application:app