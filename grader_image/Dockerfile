FROM phaustin/base_image:sep16

USER ${NB_USER}

RUN mkdir -p ${HOME}/work/datadir

WORKDIR ${HOME}

COPY nbgrader_config.py jupyter_notebook_config.py /etc/jupyter/

RUN touch version_9_20b_grader.txt

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc

CMD ["jupyterhub-singleuser"]
