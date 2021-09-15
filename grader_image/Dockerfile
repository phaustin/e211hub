FROM phaustin/base_image:sep15

USER ${NB_USER}

RUN mkdir -p ${HOME}/work/datadir

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc

WORKDIR ${HOME}/work

COPY jupyter_notebook_config.py /etc/jupyter/

RUN touch version_9_14_grader

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc
COPY jupyter_notebook_config.py /etc/jupyter/

CMD ["jupyterhub-singleuser"]
