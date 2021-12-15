FROM phaustin/base_image:dec11

RUN mkdir -p ${HOME}/work
RUN mkdir -p ${HOME}/work/data_share
RUN mkdir -p ${HOME}/work/sat_data
RUN mkdir -p ${HOME}/work/climate_data

RUN chown -R jovyan ${HOME}
RUN chgrp -R jovyan ${HOME}     

VOLUME ${HOME}/work/data_share
VOLUME ${HOME}/work/sat_data
VOLUME ${HOME}/work/climate_data

USER ${NB_USER}

COPY jupyter_notebook_config.py /etc/jupyter/

RUN echo "conda activate ${CONDA_ENV}" >> ${HOME}/.bashrc

WORKDIR "${HOME}"

RUN touch version_12_14.txt

CMD ["jupyterhub-singleuser"]

