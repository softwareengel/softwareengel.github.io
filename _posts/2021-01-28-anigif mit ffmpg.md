---
layout: post
title: Video mp4 2 gif animation convertion 
categories: [Video]
tags: [Video, mp4, gif, animation, convert ]
--- 
![](/pic/2021-01-28_14-55-24-output.gif)
# Video mp4 2 gif animation convert

create gif from mp4 

Command line 

    ffmpeg -ss 30 -t 3 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

    ffmpeg -t 3 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

![](/pic/2021-01-28-15-25-25.png)

Result 

![](/pic/2021-01-28_14-55-24-output.gif)

# Links 
Download windows  binaries 

<https://www.gyan.dev/ffmpeg/>

Command line 

<https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality>