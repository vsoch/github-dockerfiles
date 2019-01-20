FROM marcelocg/phoenix

RUN sudo apt-get update
RUN sudo apt-get install -y erlang

ENV MIX_ENV prod
ENV NODE_ENV production

COPY . /code

RUN yes | mix deps.get
RUN yes | mix deps.compile

RUN cd /code/apps/web_interface && npm install

RUN cd /code/apps/web_interface && npm run compile
RUN cd /code/apps/web_interface && mix phoenix.digest

CMD mix phoenix.server
