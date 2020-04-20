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

    
```bash
pip install opencv-python 
pip install numpy 
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