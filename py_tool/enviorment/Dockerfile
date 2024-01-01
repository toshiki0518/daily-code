# docker build ./ -t example
# docker build ./ -t linux_python
# FROM centos:centos8
FROM debian

ENV PYTHONUNBUFFERED 1
RUN apt update
# RUN apt-get install apache2
RUN apt-get install -y pip
RUN apt-get install -y python3-venv
RUN python3 -m venv /venv

# RUN source myenv/bin/activate
# RUN pip install matplotlib
RUN /venv/bin/pip install graphviz
RUN /venv/bin/pip install numpy
RUN /venv/bin/pip install requests
RUN /venv/bin/pip install requests-oauthlib


# 仮想環境内のPythonバイナリへのパスを通す
ENV PATH="/venv/bin:$PATH"

RUN pip --version
WORKDIR /home/app/src
RUN apt-get install -y vim
RUN PS1="\u\$ "
