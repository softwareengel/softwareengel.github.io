---
layout: post
title: Netcat send data 
categories: [netcat, log, data]
tags: [netcat, log, data]
--- 
Simple sending log data to Web-Server 

# netcat send log 

Send data from log files to IP with port 5000 

	tail -f *.log | nc 192.168.2.44 5000


