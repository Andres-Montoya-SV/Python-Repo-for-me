# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:57:02 2020

@author: ricardo.montoya
"""

import cv2 as cv

# This variable captures the camera of the users #
capture = cv.VideoCapture(0)

# This While function initiates the camera #
while True:
    isTrue, frame = capture.read()
    
    # this section turs the image to gray #
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray camera", gray) # Shows gray image
    cv.imshow("Video", frame) # Shows video
    
    # Face recognizition files #
    haar_cascade1  = cv.CascadeClassifier("Haar_eye.xml")
    haar_cascade  = cv.CascadeClassifier("Haar_face.xml")
    
    # Recognizes faces / Eyes #
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    eyes_rect = haar_cascade1.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    
    # Prints the faces found in the camera #
    print(f"Number of faces found = {len(faces_rect)}")
    print(f"Numbers of eyes found = {len(eyes_rect)}")
    
    # Marks the eyes / faces with a green rectangle #
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)
        
    for (x, y, w, h) in eyes_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)
    
    # Shows the faces #    
    cv.imshow("Detected Faces", frame)
    
    # Close the windows pressing "d" #
    if cv.waitKey(20) & 0xFF == ord("d"):
        break
    
# destrys all Windows and release the camera #
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
