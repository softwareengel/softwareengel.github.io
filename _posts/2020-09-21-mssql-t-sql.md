---
layout: post
title: Ubuntu MS SQL Server 
categories: [MSSQL]
tags: [MS, SQL, Server, ubuntu, docker]
---
# MS SQL Server Setup in Ubuntu

Setup in Ubuntu bash History 

``` 
        2  docker 
        3  sudo apt install docker.io 
        4  ls -al
        5  ipconfig
        6  ifconfig
        7  history
        8  docker
        9  docker ps
       10  sudo docker ps
       11  sudo docker ps -al
       12  ifconfig
       13  ls -al 
       14  htop 
       15  wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
       16  sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/18.04/mssql-server-2019.list)"
       17  sudo apt-get update
       18  sudo apt-get install -y mssql-server
       19  sudo apt-get update
       20  version
       21  lsb_release -a
       22  sudo apt-get updat e
       23  sudo apt-get update
       24  sudo apt-get install -y mssql-server
       25  sudo /opt/mssql/bin/mssql-conf setup
       26  cat /var/log/syslog 
       27  ifconfig 
       28  htop
       29  exit
       30  exit
       31  history 

```