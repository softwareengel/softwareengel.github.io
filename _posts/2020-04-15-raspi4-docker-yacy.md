---
layout: post
title: Raspi 4 Docker Yacy local search engine 
categories: [Raspi, SEARCH, BOT]
tags: [raspi, yacy, docker]
--- 

- [Install Yacy in     Docker on Raspi 4 - 4GB Ram - 64 GB SD](#install-yacy-in-----docker-on-raspi-4---4gb-ram---64-gb-sd)
  - [1. Versuch](#1-versuch)
  - [2. Versuch (working)](#2-versuch-working)
  - [Netzwerk Traffic](#netzwerk-traffic)
  - [Settings](#settings)


# Install Yacy in     Docker on Raspi 4 - 4GB Ram - 64 GB SD

```bash 
    

    curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```
## 1. Versuch 

```bash 
    sudo docker pull luccioman/yacy:latest

    docker run --name yacy -p 8090:8090 -p 8443:8443 --log-opt max-size=200m --log-opt max-file=2 luccioman/yacy
```

Leider ERROR 

## 2. Versuch (working)

```bash
    docker pull syzygysystems/yacy-arm
    sudo docker run --name yacy -p 8090:8090 -p 8443:8443 --log-opt max-size=200m --log-opt max-file=2 syzygysystems/yacy-arm

```
Set 2000 MB Ram usage und local Crawl 
Restart 

```bash
    sudo docker container ls -a

    sudo docker start CONTAINER_ID
```


The only difference between this and the official build is the OpenJDK is for ARMv732.

Exposed ports are 8090 and 8443.

WebGUI Username/PW: admin/docker

## Netzwerk Traffic 

    sudo apt-get install ifstat 
    ifstat 

![Ifstat Raspi Docker Yacy](../pic/ifstat-raspi-docker-yacy.png)

## Settings 

Suche nach 
* ftp://username:Password@127.0.0.1/Path/  oder nach 
* smb://username:Password@192.168.0.1/Path/

* Crawl depth: 99 
* Load Filter on URLs Use filter: .*
* Load Filter on URLs Use filter: .*192.168.0.1.**
* Add Crawl result to collection(s) : userDataXXX
* Add Crawl result to collection(s) : user192.168.0.1XXX


