FROM phaustin/base_image:sep20

USER ${NB_USER}

RUN mkdir -p ${HOME}/work

COPY jupyter_notebook_config.py /etc/jupyter/

# COPY --chown=${NB_USER}:${NB_USER} problem_solving/ ./problem_solving/

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc
COPY jupyter_notebook_config.py /etc/jupyter/

WORKDIR "${HOME}"

RUN touch version_9_20.txt

CMD ["jupyterhub-singleuser"]

