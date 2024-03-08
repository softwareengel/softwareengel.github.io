---
layout: post
title: Video Mp4 2 Gif Animation Convert 
categories: [Video]
tags: [Video, mp4, gif, animation, convert ]
---
![](../pics/2021-01-28-anigif%20mit%20ffmpg_image_1.gif)

- [Video Mp4 2 Gif Animation Convert](#video-mp4-2-gif-animation-convert)
- [Links](#links)

# Video Mp4 2 Gif Animation Convert

Create gif from mp4 

Command line 
```bat
    ffmpeg -ss 30 -t 3 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

    ffmpeg -t 3 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```
![](../pics/2021-01-28-anigif%20mit%20ffmpg_image_2.png)

Result

![](../pics/2021-01-28-anigif%20mit%20ffmpg_image_1.gif)

# Links 
Download Windows Binaries 

<https://www.gyan.dev/ffmpeg/>

Command line 

<https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality>