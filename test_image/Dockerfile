FROM phaustin/base_image:dec11

RUN mkdir -p ${HOME}/work
RUN mkdir -p ${HOME}/work/datadir

RUN chown -R jovyan ${HOME}
RUN chgrp -R jovyan ${HOME}     

USER ${NB_USER}

COPY jupyter_notebook_config.py /etc/jupyter/

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc

WORKDIR "${HOME}"

RUN touch version_12_11.txt

CMD ["jupyterhub-singleuser"]

