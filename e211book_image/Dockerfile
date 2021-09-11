FROM phaustin/base_image:sep11

USER ${NB_USER}

# RUN mkdir -p ${HOME}/work/problem_solving

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc

WORKDIR ${HOME}/work

COPY jupyter_notebook_config.py /etc/jupyter/

# COPY --chown=${NB_USER}:${NB_USER} problem_solving/ ./problem_solving/

RUN touch version_9_11

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc
COPY jupyter_notebook_config.py /etc/jupyter/

CMD ["jupyterhub-singleuser"]

