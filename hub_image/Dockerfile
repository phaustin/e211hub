# jupyterhub 1.4
# https://github.com/jupyterhub/jupyterhub/blob/main/Dockerfile
FROM jupyterhub/jupyterhub:1.4
COPY requirements.txt /tmp/requirements.txt
RUN python3.8 -m pip install --no-cache -r /tmp/requirements.txt
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
RUN touch /srv/jupyterhub/version_dec14.txt
