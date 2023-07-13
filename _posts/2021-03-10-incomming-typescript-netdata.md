---
layout: post
title: Notes on Typescript, Netdata on Raspi, send nginx log to sql database
categories: [Typescript]
tags: [ Typescript, Netdata, Raspi, nginx ]
--- 
- [Typescript](#typescript)
- [Netdata Docker on Raspi - Working](#netdata-docker-on-raspi---working)
- [send nginx log to sql database](#send-nginx-log-to-sql-database)

# Typescript 

- <https://www.heise.de/news/Programmiersprache-Neues-Handbuch-fuer-TypeScript-vorgestellt-5075830.html>


# Netdata Docker on Raspi - Working

- <https://github.com/netdata/netdata>

```bash 
    docker run -d --name=netdata \
    -p 19999:19999 \
    -v netdataconfig:/etc/netdata \
    -v netdatalib:/var/lib/netdata \
    -v netdatacache:/var/cache/netdata \
    -v /etc/passwd:/host/etc/passwd:ro \
    -v /etc/group:/host/etc/group:ro \
    -v /proc:/host/proc:ro \
    -v /sys:/host/sys:ro \
    -v /etc/os-release:/host/etc/os-release:ro \
    --restart unless-stopped \
    --cap-add SYS_PTRACE \
    --security-opt apparmor=unconfined \
    netdata/netdata
```
 # send nginx log to sql database 
 
 - <https://www.shubhamdipt.com/blog/send-nginx-logs-to-sql-database/>