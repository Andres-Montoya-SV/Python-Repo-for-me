# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:57:04 2020

@author: ricardo.montoya
"""

import cv2 as cv

video_Capture = cv.VideoCapture(0, cv.CAP_DSHOW)
haar_cascade  = cv.CascadeClassifier("Haar_face.xml")

while True:
    Check, frame = video_Capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=5)
    
    for x, y, w, h in faces:
        img = cv.rectangle(frame, (x, y), (x + w, y +h), (0, 255, 0), 1)
        img[y:y+h, x:x+w] = cv.medianBlur(img[y:y+h, x:x + w], 35)
        
    cv.imshow("Image", frame)
    
    if cv.waitKey(1) & 0xFF == ord("d"):
        break
    
# destroys all Windows and release the camera #
video_Capture.release()
cv.destroyAllWindows()

cv.waitKey(0)