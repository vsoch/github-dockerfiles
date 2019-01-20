FROM alpine:3.7

# Install dependencies and Download and install shiny server
RUN apk add --no-cache libstdc++ R libxml2 && \
        apk add --no-cache --virtual=tidyversedeps openssl-dev libxml2-dev && \
        apk add --no-cache --virtual=builddeps ca-certificates cmake gcc g++ git linux-headers R-dev python2 unzip wget bash
#this is the secret sauce that allows shiny to compile on alpine. thanks https://github.com/ifvox/ for this brilliance
RUN mkdir ~/.R && \
        echo "CFLAGS = -D__USE_MISC" > ~/.R/Makevars && \
        cd ~ && \
        R -e "install.packages('shiny', repos='https://cran.rstudio.com')"
#extras: freetype fontconfig ttf-dejavu bash

#straight out of the installation guide (https://github.com/rstudio/shiny-server/wiki/Building-Shiny-Server-from-Source)
RUN git clone https://github.com/rstudio/shiny-server.git && \
        cd shiny-server && mkdir tmp && cd tmp && \
        DIR=`pwd` && PATH=$DIR/../bin:$PATH && \
        PYTHON=`which python` && cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DPYTHON="$PYTHON" ../ && \
        make && \
        mkdir ../build && \
        (cd .. && ./bin/npm --python="$PYTHON" install) && \
        (cd .. && ./bin/node ./ext/node/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js --python="$PYTHON" rebuild) && \
        make install 

#install R packages
RUN R -e 'install.packages(c("devtools", "rmarkdown", "dplyr", "readr", "ggplot2", "tidyr", "tibble", "purrr", "stringr", "jsonlite", "data.table", "dbplyr", "RMySQL", "lubridate", "xml2", "readxl", "modelr", "broom", "caret", "tidyverse", "forcats", "curl", "leaflet", "ggthemes", "htmltools", "htmlwidgets", "shinythemes", "tidyverse"), repos="http://cran.us.r-project.org")'
#some user stuff to reduce permissions
RUN adduser -h /home/shiny -s /bin/false -D -H shiny && \
        mkdir /home/shiny && chown shiny.shiny /home/shiny && \
        mkdir -p /var/log/shiny-server /srv/shiny-server /var/lib/shiny-server /etc/shiny-server /var/lib/shiny-server/bookmarks/shiny && \
        chown shiny /var/log/shiny-server

#cleanup
RUN apk del builddeps

#add in config
COPY --chown=shiny ./shiny-server.conf /etc/shiny-server/shiny-server.conf
#add in the shiny apps
COPY --chown=shiny ./server-contents /srv/shiny-server

#go
CMD /bin/su -l shiny -s /bin/sh -c /usr/local/shiny-server/bin/shiny-server
EXPOSE 3838