# docker build ./ -t example
# docker build ./ -t linux_python
FROM centos:centos8
ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# RUN yum install -y python3 httpd
# RUN yum install -y python3 python3-devel python3-libs httpd-devel gcc make mariadb-devel wget
# RUN yum install -y python3 httpd

RUN yum install -y python3 httpd
# RUN yum install -y python3 httpd python36u python36u-libs python36u-devel python36u-pip
# RUN yum install -y python36u python36u-libs python36u-devel python36u-pip
# RUN pip3.6 install django

# CMD echo 'Hello docker world!'
# RUN mkdir /code
# WORKDIR /code
WORKDIR /home/app/src
# ADD requirements.txt /code/
# RUN pip install -r requirements.txt
# ADD . /code/
# CMD python3 data_structure/main.py