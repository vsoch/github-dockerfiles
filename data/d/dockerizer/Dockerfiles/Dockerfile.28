FROM alpine

    # install pip on Linux
 RUN  apk update && apk add py-pip git
 RUN  pip install bottle
 RUN  git clone https://github.com/namecoin/nmcontrol/ 
 RUN ls -lart
 RUN  python ./nmcontrol/nmcontrol.py

    # alternatively start in debug mode:
    # CMD  ["python","nmcontrol.py","--daemon=0","--debug=1"," start"]
