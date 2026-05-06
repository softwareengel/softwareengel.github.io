---
layout: post
title: Yacy local network search setup
categories:
  - yacy
tags:
  - yacy
  - search
  - java
  - oss
  - docker
  - Synology
---
# setup yacy search engine in docker 

![](../pics/2023-11-03-yacy-search-local_image_1.webp)

## setup yacy 

- intranet indexing only 
![](../pics/2023-11-03-yacy-search-local_image_2.webp)

- Network config: robinson mode ... Private Peer 

![](../pics/2023-11-03-yacy-search-local_image_3.webp)


## Setup Search 

![](../pics/2023-11-03-yacy-search-local_image_4.webp)
- ftp - Search 
- depth `20` 
- regex filter `.*240.*` for ip adress only 
- add agent name for search `user240Regex-depth20`

## Max Ram usage

![](../pics/2023-11-03-yacy-search-local_image_5.webp)
  
- Max RAM usage 900 MB
  

## Local Indexing 

![](../pics/2023-11-03-yacy-search-local_image_6.webp)

## Local Search Result 

- web search result 
![](../pics/2023-11-03-yacy-search-local_image_7.webp)

- web search result images 
![](../pics/2023-11-03-yacy-search-local_image_8.webp)

- yacy file search result 
![](../pics/2023-11-03-yacy-search-local_image_9.webp)

- view web url content 

![](../pics/2023-11-03-yacy-search-local_image_10.webp)