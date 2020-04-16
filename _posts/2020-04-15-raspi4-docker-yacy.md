---
layout: post
title: Raspi 4 Docker Yacy 
categories: [Raspi]
tags: [raspi, yacy, docker]
--- 

# Raspi 4 Docker Yacy 

    sudo apt-get update
    curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh

## 1. Versuch 

    sudo docker pull luccioman/yacy:latest

    docker run --name yacy -p 8090:8090 -p 8443:8443 --log-opt max-size=200m --log-opt max-file=2 luccioman/yacy

    ERROR 


## 2. Versuch (working)

    docker pull syzygysystems/yacy-arm
    docker run --name yacy -p 8090:8090 -p 8443:8443 --log-opt max-size=200m --log-opt max-file=2 syzygysystems/yacy-arm

The only difference between this and the official build is the OpenJDK is for ARMv732.

Exposed ports are 8090 and 8443.

WebGUI Username/PW: admin/docker

## Settings 

Suche nach 
* ftp://username:Password@127.0.0.1/Path/  oder nach 
* smb://username:Password@127.0.0.1/Path/

* Crawl depth: 99 
* Load Filter on URLs Use filter: .*
* Add Crawl result to collection(s) : userDataXXX


