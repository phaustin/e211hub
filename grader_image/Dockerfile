FROM phaustin/base_image:sep16

USER ${NB_USER}

RUN mkdir -p ${HOME}/work/datadir

WORKDIR ${HOME}/work

COPY jupyter_notebook_config.py /etc/jupyter/

RUN touch version_9_16_grader.txt

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc
COPY jupyter_notebook_config.py /etc/jupyter/

CMD ["jupyterhub-singleuser"]
