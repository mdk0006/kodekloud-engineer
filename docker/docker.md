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
[Why to use docker](https://techiescamp.com/topic/why-to-use-docker/)
[Docker Core Architecture](https://techiescamp.com/topic/docker-core-architecture/)
[How Docker Works](https://techiescamp.com/topic/how-does-docker-work/)
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

# Running Custom Shell Scripts In Docker

[Shell Scripts](https://techiescamp.com/topic/running-custom-shell-scripts-in-docker/)
[Keep Docker Container Running](https://techiescamp.com/topic/keep-docker-container-running-for-debugging/)
[Docker in Docker Container](https://techiescamp.com/topic/run-docker-in-docker-container/)

_It is recommended to treat containers as immutable objects, and it is not recommended to make changes to a running container. Any changes made to a running container should only be for testing purposes._

# Lab 6

## Pulling and tagging the image

```
docker image pull <image_name>
docker image tag <name_of_old_image_with_tag> <name_of_image:with_new_tag>
```

# Lab 7

## Docker Permissions for the user

```
sudo usermod -aG docker <rose>
```

to check the user groups on the linux server

```
cat /etc/group
```
