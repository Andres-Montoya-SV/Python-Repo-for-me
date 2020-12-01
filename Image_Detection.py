# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:17:20 2020

@author: ricardo.montoya
"""

import numpy as np
import cv2 as cv

haar_cascade  = cv.CascadeClassifier("Haar_face.xml")

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]
feature = np.load("features.npy")
labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img = cv.imread(r"C:\Users\ricardo.montoya\Desktop\Neural_Network\val\elton_john\5.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y +h, x:x + h]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {label} with a confidence of {confidence}")
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=1)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255,0), thickness=2)
    
cv.imshow("Detected", img)

cv.waitKey(0)