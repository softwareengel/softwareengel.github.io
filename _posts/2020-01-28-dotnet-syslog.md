---
layout: post
title: Dotnet und Syslog  
categories: [Logging]
tags: [dotnet, rsyslog, ubuntu, dotnet core, greylog, elk]
---

# Dotnet und Syslog 

## Syslogserver 

<https://maxbelkov.github.io/visualsyslog/> 

<https://www.draytek.com/products/utility/> 

<https://www.winsyslog.com/> 


## Ubuntu Rsyslog 

<https://raymii.org/s/tutorials/Syslog_config_for_remote_logservers_for_syslog-ng_and_rsyslog_client_server.html> 

<https://www.rsyslog.com/>

Ecryption rsyslog
<https://help.papertrailapp.com/kb/configuration/encrypting-remote-syslog-with-tls-ssl/>


### imfile: Text File Input Module 

<https://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html>


## Dotnet 

    dotnet new --list  

## Dotnet Logging 

<https://docs.microsoft.com/de-de/aspnet/core/fundamentals/logging/?view=aspnetcore-3.1>

<https://michaelscodingspot.com/logging-in-dotnet/> 

## Greylog

<https://www.proudcommerce.com/blog/graylog-logserver-einrichten> 

- OVA

<http://docs.graylog.org/en/3.1/pages/installation/virtual_machine_appliances.html>

<https://packages.graylog2.org/appliances/ova> 


- Docker Image 

<https://hub.docker.com/r/graylog/graylog/>

- Docker installation 

<http://docs.graylog.org/en/3.1/pages/installation/docker.html#here>


- Datensammler 

<https://www.elastic.co/de/downloads/beats/filebeat>

<https://nxlog.co/whitepapers> 

<https://www.fluentd.org/faqs> 



## ELK Stack 

    sudo apt install openjdk-8-jre-headless

<https://jaxenter.de/elastic-stack-containern-docker-86374> 

![2020 01 28 Elk Stack Jax](../pic/2020-01-28-elk-stack-jax.png)

<https://logz.io/blog/elk-stack-on-docker/>

![2020 01 28 Elk Stack Logx](../pic/2020-01-28-elk-stack-logx.png)

<https://dev.to/dendihandian/elk-stack-local-development-using-docker-elk-6k7>

sudo docker exec -ti engels_filebeat_1 /bin/bash
 
<http://192.168.2.25:9200/_cat/indices?v> 

<http://192.168.2.25:9200/_search?q=*>

<http://192.168.2.25:5601/app/kibana#/home>
