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
[Docker Multistage Docker](https://techiescamp.com/topic/docker-multistage-build/)
When we use multistage the size of the image can be reduced
[Methods to optimize the size of Docker Image](https://techiescamp.com/topic/optimize-docker-image/)
1: Use the minimal base image
2: Use multistage builds
3: Minimize the number of layers
4: Keep application data else where
5: Use Docker caching by planning the Docker File commands
6: Use DockerIgnore and avoid nested file structures
[Using HereDoc Within Dockerfile](https://techiescamp.com/topic/using-heredoc-with-dockerfile/)
[ENTRYPOINT VS CMD](https://techiescamp.com/topic/entrypoint-vs-cmd/)
[Docker File Best Practices](https://techiescamp.com/topic/dockerfile-best-practices/)

## Done till Docker Projects
