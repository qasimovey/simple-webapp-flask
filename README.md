### Why do we need to build an image ? 

- You coudn`t find particular image in docker registry
- You need to containerize your application in order easy shipping , deploying to other environment

### How to containerize Application using Dockerfile

An image has layered architecture , when you create an image you build an new layer on another image
Below example , we have used ubuntu OS image to build our new image .

### What is Dockerfile ? 
Dockerfile is a file contaning inctructions and arguments .
when you build an image , docker reads instructions in dockerfile and executes it , in order to build new layer .
### Dockerfile Example
```
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python 
RUN apt-get install -y python-pip
RUN pip install flask

COPY app.py /opt/app.py

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
```

```
docker build . -t <dockerID>/<appname>
docker run -d <dockerID>/<appname>
```

### The followings code snippet is used to startup application and monitor it 

```
docker ps 
docker inspect <container id>
```
```
curl http:// <IP ADRESS>:5000
curl http:// <IP ADRESS>:5000/info
```
```
docker build <dockerID>/<appname>
docker login
docker push  <dockerID>/<appname>
```
 

