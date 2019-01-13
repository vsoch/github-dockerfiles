FROM balpine

MAINTAINER Bolik WaterBolik@163.com

# nodejs 基础架构及模块学习

RUN set -ex \
    && cnpm install -g coffee-script \
    && cnpm install -g webpack \
    && cnpm install -g electron \
    && cnpm install -g express \
    # JavaScript Standard Style 
    && cnpm install -g standard \
    # && cnpm install -g phantomjs \
    # && npm install -g phantomjs --ignore-scripts \
    # GitBook 是一项致力于文档编制、数码写作和出版的新型、简单的解决方案。
    && cnpm install -g gitbook-cli \
    # && cnpm install -g phantomjs-prebuilt --ignore-scripts \
    # && cnpm install -g gitbook-pdf \
    && npm install -g gitbook-pdf --ignore-scripts \
    # 安装vue
    && cnpm install -g vue-cli \
    && echo "end"

WORKDIR /app

VOLUME /app

# ADD app.js /app/app.js
# ADD package.json /app/package.json

# ADD . /app

# 使用淘宝的npm镜像
# RUN npm install --production -d --registry=https://registry.npm.taobao.org

CMD ["bash"]

# CMD ["node", "/app/app.js"]

# $ docker build -t bnodejs /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/bnodejs/
# $ docker run -it --rm -v /Volumes/Work/OpenSource/WaterBolik/:/WaterBolik bnodejs
# docker build -t bnodejs B:\OpenSource\WaterBolik\prestudy\bdocker\bnodejs\
# docker run -it --rm -v /B/OpenSource/WaterBolik/:/WaterBolik/ bnodejs 