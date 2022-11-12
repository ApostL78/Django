# DjangoBlog
Django first repo
# Run with Docker
To start this app without cloning and installing all dependencies you can run it with `docker` ([install](https://www.docker.com/) before usage):
1. Pull the image from `docker hub`:
```shell
docker pull apostl/django-blog:latest
```
2. Run pulled image on port `8000`:
```shel
docker run -d -p 8000:8000 --name django_blog apostl/django-blog:latest
```
3. After the application starts, navigate to `http://localhost:8000` in your web browser.

# Clean Up
After all works done run following command to list all running containers:
```shell
docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED              STATUS              PORTS                    NAMES
9bebe43e03f3   apostl/django-blog:latest   "python3 DjangoProje…"   About a minute ago   Up About a minute   0.0.0.0:8000->8000/tcp   django_blog
```
Listing containers must show only one container running.
To stop a container run:
```shell
docker stop django_blog
```
Then delete this container:
```shell
docker rm django_blog
```
Additionaly, if u dont want to use this image anymore, run following command to delete it:
```shell
docker rmi apostl/django-blog:latest
```
