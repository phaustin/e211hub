FROM phaustin/base_image:aug07

USER root

RUN mkdir -p /opt
RUN chown -R ${NB_USER} /opt

USER ${NB_USER}

#COPY e211_lib/ $HOME/
RUN mkdir -p $HOME/data

RUN mkdir -p ${HOME}/work

# RUN mkdir -p ${HOME}/work/data_readonly
# RUN mkdir -p ${HOME}/work/data_share


RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc
COPY jupyter_notebook_config.py /etc/jupyter/

WORKDIR ${HOME}/work

CMD ["jupyterhub-singleuser"]
