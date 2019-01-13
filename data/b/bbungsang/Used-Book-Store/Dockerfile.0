##
# Dockerfile.ubuntu 를 활용한 custom docker file
#   Dockerfile.ubuntu : 변하지 않을 과정으로 확정된 부분을 미리 생성한 것
#   Dockerfile.custom : 반복적으로 추가/변경/삭제 할 부분
##

FROM            bbungsang/used-book-store
MAINTAINER      bbungsang@gmail.com

##
# uWSGI 가 정상적으로 서버를 열어줄 수 있는지 커맨드 생성
# 커맨드에 따라서 설정 파일 수정
# 수정한 설정 파일이 자동으로 삽입되도록 다시 Dockerfile.custom 변경
##

# 현재 경로의 모든 파일을 컨테이너의 /srv/used-book-store 폴더에 복사
COPY            . /srv/used-book-store

# cd /srv/used-book-store 과 같은 효과
WORKDIR         /srv/used-book-store

# requirements 설치
RUN             /root/.pyenv/versions/used-book-store/bin/pip install -r .requirements/deploy.txt

# supervisor 파일 복사
COPY            .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY            .config/supervisor/nginx.conf /etc/supervisor/conf.d/

# nginx 파일 복사
COPY            .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY            .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
    # 기존 80 포트 요청을 받는 default 제거
RUN             rm -rf /etc/nginx/sites-enabled/default
    # symbolic link 생성
RUN             ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.ini

RUN             /root/.pyenv/versions/used-book-store/bin/python /srv/used-book-store/django_app/manage.py collectstatic --settings=config.settings.deploy --noinput

CMD             supervisord -n

# 컨테이너 내부 어느 포트와 연결시킬 것인지에 대한 커맨드 : nginx 가 80 포트 요청을 받기 때문에 80 으로 지정
EXPOSE          80

##
# Note :
#   - 이미지 생성 명령어 : docker build -t eb . -f .dockerfiles/Dockerfile.custom
#   - 이미지 실행 명령어 : docker run --rm -it -p 8080:80 eb /bin/zsh
#       기본적으로 컨테이너는 외부와 포트가 닫혀있다. 즉 컨테이너가 실행되고 있을 떄, 외부에서 해당 컨테이너에 접속할 방법이 없다.
#       이 때문에 '-p 외부포트:내부포트' 옵션을 줘야한다. 위 명령어의 경우, 로컬에서 8080 포트로 접속하면 컨테이너의 80 포트로 연결이 된다는 의미이다.
##