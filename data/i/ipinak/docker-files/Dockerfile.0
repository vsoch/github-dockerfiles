# DjangoPypi Server

FROM ubuntu:14.04
MAINTAINER Jim Yeh <lemonlatte@gmail.com>

RUN dpkg-divert --local --rename --add /sbin/initctl\
  && ln -sf /bin/true /sbin/initctl\
  && ln -sf /bin/false /usr/sbin/policy-rc.d\
  && apt-get update -y\
  && apt-get -y -q install python-dev python-pip git supervisor nginx\
  && pip install uwsgi virtualenv\
  && virtualenv pypi-site\
  && /bin/bash -c 'source pypi-site/bin/activate && pip install djangopypi2'\
  && /bin/bash -c 'source pypi-site/bin/activate && DJANGOPYPI2_ROOT=/pypi-site/djangopypi2 manage-pypi-site syncdb --noinput'\
  && /bin/bash -c 'source pypi-site/bin/activate && DJANGOPYPI2_ROOT=/pypi-site/djangopypi2 manage-pypi-site collectstatic --noinput'\
  && /bin/bash -c 'source pypi-site/bin/activate && DJANGOPYPI2_ROOT=/pypi-site/djangopypi2 manage-pypi-site loaddata initial'

ADD setup_script.py pypi-site/
RUN /bin/bash -c 'source pypi-site/bin/activate && python pypi-site/setup_script.py'\
  && rm pypi-site/setup_script.py\
  && echo 'daemon off;' >> /etc/nginx/nginx.conf\
  && rm /etc/nginx/sites-enabled/default

ADD uwsgi.ini pypi-site/
ADD wsgi.py pypi-site/
ADD settings.json pypi-site/djangopypi2/
ADD pypi-site /etc/nginx/sites-enabled/
ADD supervisor.conf/ /etc/supervisor/conf.d/
RUN chown www-data:www-data -R pypi-site/djangopypi2
VOLUME /var/data

EXPOSE 80
ADD run_server.sh run_server.sh
CMD ["sh", "run_server.sh"]
