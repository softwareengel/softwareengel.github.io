---
layout: post
title: Send Logs to Server with Netcat  
categories: [netcat, log, data]
tags: [netcat, log, data]
--- 

Simple sending log data to Web-Server

# Send Logs to Server with Netcat  

Send data from log files to IP with port 5000

``` bash
    tail -f *.log | nc 192.168.2.44 5000
```
