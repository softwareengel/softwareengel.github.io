---
layout: post
title: OpenCV und Python 
categories: []
tags: [opencv, python, ml, video, image, manipulatition]
--- 

# OpenCV und Python  

<https://de.wikipedia.org/wiki/OpenCV> 

Python openvc tutorial <https://opencv-python-tutroals.readthedocs.io/en/latest/>

<https://opencv.org/>

<https://github.com/opencv>

## Example

Python use opencv to save image from video capture 

https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/

    
```bash
# ? 
sudo pip3 install opencv-python 

sudo pip3 install numpy 
sudo apt install python3-opencv

# on linux/ Raspi 
sudo apt install libjasper1
sudo apt install libqtgui4 
```


```python 
# opencv 
import numpy as np
import cv2
print ("cv2 Version:", cv2.__version__)

cap = cv2.VideoCapture(0)
count = 10000
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('s'):
            count += 1
            filename = "frame"+ str(count) + ".png"
            print ("save" , filename)
            cv2.imwrite(filename, frame)
            filename = "frame"+ str(count) + "_sw.png"
            cv2.imwrite(filename, gray)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



```

![2020 05 04 Raspbery Opencv Video Frame](/pic/2020-05-04-raspbery-opencv-video-frame.png)

## VS Code on Raspi 


<https://www.hanselman.com/blog/HowToInstallVisualStudioCodeOnARaspberryPi4InMinutes.aspx>


![2020 05 04 Raspberry Pi VS Code Opencv Running in RDP](/pic/2020-05-04-raspberry-pi-vscode-opencv-running.png)

