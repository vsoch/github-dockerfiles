FROM bnodejs

MAINTAINER Bolik WaterBolik@163.com

RUN set -ex \
    && apk add --update --no-cache \   
        # Netwide Assembler
        nasm \
        imagemagick \

    # Gatsby 使用 React 生态系统来生成静态 html 文件。
    && cnpm install -g gatsby \
    && echo "end"

VOLUME /blog
WORKDIR /blog

EXPOSE 8000

ENTRYPOINT [ "gatsby", "develop" ]

# CMD ["bash"]

# $ docker build -t bnodejs /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/bnodejs/
# $ docker run -it --rm bnodejs
# docker build -t bnodejs B:\OpenSource\WaterBolik\prestudy\bdocker\bnodejs\
# docker run -it --rm bnodejs 