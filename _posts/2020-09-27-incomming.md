﻿---
layout: post
title: Notes on Kanban for Redmine, Locust, KodExplorer, Dell e7240 Cmos Battery, ..
categories: [Notes]
tags: [ Serenity ]
--- 
- [Scrum / Kanban for Redmine](#scrum--kanban-for-redmine)
  - [update docker readmine 3.3.10 + scrum plugin](#update-docker-readmine-3310--scrum-plugin)
- [Dell e7240 Cmos Battery](#dell-e7240-cmos-battery)
  - [dell Notebook Self Diag](#dell-notebook-self-diag)
- [Locust - An open source load testing tool.](#locust---an-open-source-load-testing-tool)
- [k8s - Ingress Controllers](#k8s---ingress-controllers)
- [k8s Dashboard Web UI](#k8s-dashboard-web-ui)
- [Python Fire  - Command Line Maker](#python-fire----command-line-maker)
- [Firefox Shortcuts](#firefox-shortcuts)
- [KodExplorer - Web](#kodexplorer---web)
- [Docker ELK on Raspi 4 2020-11-18](#docker-elk-on-raspi-4-2020-11-18)
  - [remote docker Extension in Raspi with  VS Code - Working](#remote-docker-extension-in-raspi-with--vs-code---working)
  - [ELK](#elk)
  - [Logstash Alternativen](#logstash-alternativen)
  - [USB Drive Raspi](#usb-drive-raspi)
  - [git install raspi](#git-install-raspi)
  - [Jenkins on  Raspi](#jenkins-on--raspi)
  - [Prometheus on Raspi](#prometheus-on-raspi)
  - [Prometheus node exporter](#prometheus-node-exporter)
  - [Nginx Basic Status](#nginx-basic-status)

## Clipboards

https://ditto-cp.sourceforge.io/ 

## Carto 
Unlock the power of spatial analysis
The world's leading Location Intelligence platform

<https://carto.com/ >

## Google Data Expolrer 

<https://www.google.com/publicdata/directory>

## OSS Kanban Borard

https://kanboard.org/ 


# Scrum / Kanban for Redmine 

<https://www.scrumexpert.com/tools/scrum-and-kanban-plugins-for-redmine/ >

<https://redmine.ociotec.com/attachments/536/scrum-v0.19.0.tar.gz>

## update docker readmine 3.3.10 + scrum plugin 

    sudo docker ps
    sudo docker exec -it f831edadec99 bash
    wget https://redmine.ociotec.com/attachments/536/scrum-v0.19.0.tar.gz 
    chmod -R redmine:redmine *

restart 

  
# Dell e7240 Cmos Battery 

<https://www.youtube.com/watch?v=6acrpAjQ6IU>

<https://www.parts-people.com/blog/2014/11/19/dell-latitude-e7240-cmos-battery-removal-and-installation/ >

<https://www.youtube.com/watch?v=zNGfT-b1Ejk>

## dell Notebook Self Diag 

Power + d (Display Check)

Poser + Fn 

# Locust - An open source load testing tool.

Define user behaviour with Python code, and swarm your system with millions of simultaneous users. 


<https://locust.io/>

![2020 10 23 Locust Screenfile](../pic/2020-10-23-locust-screenfile.png)

# k8s - Ingress Controllers 

    Kubernetes Documentation
    Concepts
    Services, Load Balancing, and Networking
    Ingress Controllers 


<https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/> 

# k8s Dashboard Web UI 
    Kubernetes Documentation
    Tasks
    Access Applications in a Cluster
    Web UI (Dashboard)


<https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/>
  
# Python Fire  - Command Line Maker 

Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.

<https://github.com/google/python-fire>


# Firefox Shortcuts 

<https://support.mozilla.org/en-US/kb/keyboard-shortcuts-perform-firefox-tasks-quickly>

<https://developer.mozilla.org/de/docs/Tools/Keyboard_shortcuts>

![2020 11 22 Data Vis List](../pic/2020-11-22-data-vis-list.png)# logistik summit 

<https://www.youtube.com/watch?v=q8W5KnmbWBg&feature=youtu.be&t=1388>


# KodExplorer - Web 

KodExplorer is a file manager for web. It is also a web code editor, which allows you to develop websites directly within the web browser.You can run KodExplorer either online or locally,on Linux, Windows or Mac based platforms. The only requirement is to have PHP 5 available.

<https://github.com/kalcaddle/KodExplorer>


# Docker ELK on Raspi 4 2020-11-18

<https://dev.to/rohansawant/installing-docker-and-docker-compose-on-the-raspberry-pi-in-5-simple-steps-3mgl>


1. Install Docker

    curl -sSL https://get.docker.com | sh
    
2. Add permission to Pi User to run Docker Commands

    sudo usermod -aG docker pi

Reboot here or run the next commands with a sudo

3. Test Docker installation

    newgrp docker 
    docker run hello-world

4. IMPORTANT! Install proper dependencies

    sudo apt-get install -y libffi-dev libssl-dev

    sudo apt-get install -y python3 python3-pip

    sudo apt-get remove python-configparser

5. Install Docker Compose

    sudo pip3 -v install docker-compose 

--- okay 2020-11-18 on raspi 4 raspberianos 

## remote docker Extension in Raspi with  VS Code - Working 

![2020 11 18 Vs Code Docker Addon Raspi](../pic/2020-11-18-vs-code-docker-addon-raspi.png)

## ELK  

<https://logz.io/learn/complete-guide-elk-stack/#installing-elk>

<https://logz.io/blog/elk-stack-raspberry-pi/>


## Logstash Alternativen 

https://sematext.com/blog/logstash-alternatives/

## USB Drive Raspi 
```bash 
    sudo apt-get install usbmount 
    sudo reboot now 
    sudo lsblk -o UUID,NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL,MODEL 
    sudo blkid
```
- <https://raspberrypi.stackexchange.com/questions/100312/raspberry-4-usbmount-not-working>

- <https://www.elektronik-kompendium.de/sites/raspberry-pi/1911271.htm> 

```
    lsblk
    sudo mount /dev/sda1 /media/usb 
```
    
## git install raspi 
```bash 
    sudo apt-get install git 
``` 

## Jenkins on  Raspi 

<https://khushil.io/2020/04/23/jenkins-on-raspberry-pi-4/>

<https://j-grote.de/?p=108>

<https://developer-blog.net/raspberry-pi-als-jenkins-server/>

<http://192.168.2.46:8080/> 


<https://www.vogella.com/tutorials/Jenkins/article.html>
```
    docker pull jenkins/jenkins:lts 

    docker run -p 8080:8080 -p 50000:50000 -v [yourjenkinshome]:/var/jenkins_home jenkins/jenkins:lts
```

Dockerfile 
```
    FROM jenkins/jenkins:lts
    # if we want to install via apt
    USER root
    RUN apt-get update && apt-get install -y maven
    # drop back to the regular jenkins user - good practice
    USER jenkins

    docker build -t jenkins-maven .
```

## Prometheus on Raspi 

<https://devconnected.com/the-definitive-guide-to-prometheus-in-2019/> 

![Pull Vs Push](../pic/pull-vs-push.png)

<http://192.168.2.46:9090/metrics> 


## Prometheus node exporter 

<https://github.com/prometheus/node_exporter>
```bash 
    docker run -d \
      --net="host" \
      --pid="host" \
      -v "/:/host:ro,rslave" \
      quay.io/prometheus/node-exporter \
      --path.rootfs=/host
```
<http://192.168.2.46:9100/metrics> 

## Nginx Basic Status 

<http://192.168.2.46/basic_status>