# dummy for testing. Don't use this in production!
#c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'
c.Authenticator.allowed_users = {'test1','test2','phil','aloeppky','fjones','cjohnson','czhang','hari'}
c.Authenticator.admin_users = {'test1','test2','phil','aloeppky','fjones','cjohnson','czhang','hari'}
# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'newe211hub'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
# c.DockerSpawner.image = 'phaustin/basicbook:aug07'
c.DockerSpawner.allowed_images = {'e211' : 'phaustin/basicbook:aug07',
                                  'e350' : 'phaustin/basicbook:aug07'}
notebook_dir = "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'proxy_aug07'
c.DockerSpawner.volumes = {"e211hub-user-{username}": notebook_dir}
                        #     "/home/phil/repos/a448hub/data_readonly": 
                        #     {"bind": '/home/jovyan/work/data_readonly', "mode": "ro"},
                        #     "/home/phil/repos/a448hub/data_share": 
                        #     {"bind": '/home/jovyan/work/data_share', "mode": "rw"}
                        #    }


# delete containers when the stop
c.DockerSpawner.remove = True
