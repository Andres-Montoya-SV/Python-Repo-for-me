# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:13:53 2020

@author: ricardo.montoya
"""

import cv2 as cv
import numpy as np
import os

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]

p = []
for i in os.listdir(r'C:\Users\*****\Desktop\Neural_Network\train'):
    p.append(i)
    
DIR = r'C:\Users\*****\Desktop\Neural_Network\train'

haar_cascade  = cv.CascadeClassifier("Haar_face.xml")

feature = []
labels = []

def create_train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)
        
        for img in os.listdir(path):
            img_path =os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=4)
            
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y + h, x:x + w]
                feature.append(faces_roi)
                labels.append(label)

create_train()
print("Training done -----------------------")
feature = np.array(feature)
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(feature, labels)

face_recognizer.save("face_trained.yml")

print(f"Length of features lis is = {len(feature)}")
print(f"Length of features lis is = {len(labels)}")

np.save("labels.npy", labels)
np.save("features.npy", feature)

cv.waitKey(0)