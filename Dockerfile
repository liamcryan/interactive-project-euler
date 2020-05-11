FROM ubuntu:20.04

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install python3.7 -y \
    && apt-get install python3-pip -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install build-essential cmake git libjson-c-dev libwebsockets-dev -y \
    && git clone https://github.com/tsl0922/ttyd.git \
    && cd ttyd && mkdir build && cd build \
    && cmake .. \
    && make && make install \
    && cd ../.. \
    && apt-get install docker.io -y \
    && apt-get install gunicorn -y

COPY . /usr/src/app/

WORKDIR /usr/src/app

RUN pip3 install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r requirements.txt

ARG FLASK_ENV=production

RUN export FLASK_ENV=${FLASK_ENV}