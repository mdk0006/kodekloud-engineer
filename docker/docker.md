# **_ Lab 1 _**

## Docker Installation

```
https://docs.docker.com/compose/install/linux/
```

# **_ Lab 2 _**

## Run Docker Container

```
docker run -d --name nginx_3  nginx:alpine
```

# **_ Lab 3 _**

## Delete Docker Container

```
 docker rm kke-container
```

```
docker ps -qa
```

# **_ Lab 4 _**

## Copy inside the container

```
docker cp /path/to/local/file.txt container_name:/path/inside/container/
```

```
docker exec -it mycontainer sh

```

[Docker Exec Command](https://docs.docker.com/engine/reference/commandline/exec/)
[Docker CP Command](https://docs.docker.com/engine/reference/commandline/cp/)

# **_ Lab 5 _**

## Troubleshooting Container

The container was in stopped condition

sudo usermod -aG docker $USER
changing the config of the current login user add to to
-a to append
-G for specifying the groups

DockerFile
each line of the dockerfile creates a new layer
All other layers other than top most layers are readable only
[DockerFile Explained](https://techiescamp.com/topic/dockerfile-explained/)
[EntryPoint vs CMD](https://devopscube.com/run-scripts-docker-arguments/)

