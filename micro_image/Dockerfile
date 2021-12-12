FROM ubuntu

RUN echo "Creating jovyan user..." 
RUN groupadd -r jovyan -g 1004 \
    && useradd -u 1002 --no-log-init -s /bin/bash -r --create-home -g jovyan jovyan

ENV HOME=/home/jovyan
RUN echo "home is ${HOME}"
USER jovyan
RUN mkdir -p ${HOME}/testing 
VOLUME ${HOME}/testing
WORKDIR "${HOME}"
