FROM deepcortex/scala-python3-ml:latest

RUN conda install --quiet --yes jupyter && \
    conda clean -tipsy

RUN pip install matplotlib

ENV HOME /home/projects/

EXPOSE 8888

WORKDIR $HOME

CMD ["/bin/bash", "-c", "/opt/conda/bin/jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root --no-browser"]

ARG BUILD_DATE
ARG VCS_REF
ARG IMAGE_VERSION

LABEL maintainer="nsemichev@gmail.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="DeepCortex" \
      org.label-schema.description="DeepCortex is the world’s first cloud based, automated platform for doing the entire end-to-end Data Science process" \
      org.label-schema.url="http://www.deepcortex.ai" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.version=$IMAGE_VERSION \
      org.label-schema.vcs-url="https://github.com/deepcortex/dockers" \
      org.label-schema.vendor="DeepCortex" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.docker.cmd="docker run -it -p 8888:8888 -v <local-projects-path>:/home/projects deepcortex/python3-ml-jupyter"
