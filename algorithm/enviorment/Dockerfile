# docker build ./ -t example
# docker build ./ -t linux_python
# FROM centos:centos8
FROM debian

ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt-get install -y python3
# RUN apt-get install apache2
RUN apt-get install -y pip
RUN pip install matplotlib
WORKDIR /home/app/src
