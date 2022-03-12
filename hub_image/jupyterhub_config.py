# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'
# c.Authenticator.allowed_users = {'test1','test2','phil','aloeppky','fjones','cjohnson','czhang','hari'}
c.Authenticator.admin_users = {'test1','test2','phil','aloeppky','fjones','cjohnson','czhang','hari'}
# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'e211hub'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
# c.DockerSpawner.image = 'phaustin/e211book:sep11'
c.DockerSpawner.allowed_images = {'a448' : 'phaustin/climbook:dec13',
                                  'a301' : 'phaustin/a301image:mar11',
                                  'e211' : 'phaustin/e211book:sep20',
                                  'test' : 'phaustin/test_image:dec11'}
notebook_dir = "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'proxy_aug07'
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir,
                        #     "/home/phil/repos/a448hub/data_readonly": 
                        #     {"bind": '/home/jovyan/work/data_readonly', "mode": "ro"},
                          "/home/jovyan/repos/e211hub/data_share": 
                           {"bind": '/home/jovyan/work/data_share', "mode": "rw"},
                          "/home/jovyan/repos/e211hub/sat_data": 
                           {"bind": '/home/jovyan/work/sat_data', "mode": "ro"},
                          "/home/jovyan/repos/e211hub/climate_data": 
                           {"bind": '/home/jovyan/work/climate_data', "mode": "ro"}
                           }
# c.DockerSpawner.volumes = {"e211hub-user-{username}": notebook_dir}
#                         #     "/home/phil/repos/a448hub/data_readonly": 
#                         #     {"bind": '/home/jovyan/work/data_readonly', "mode": "ro"},
#                         #     "/home/phil/repos/a448hub/data_share": 
#                         #     {"bind": '/home/jovyan/work/data_share', "mode": "rw"}
#                         #    }


# delete containers when the stop
c.DockerSpawner.remove = True

