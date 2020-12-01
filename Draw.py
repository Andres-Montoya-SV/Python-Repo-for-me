# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 13:59:56 2020

@author: ricardo.montoya
"""

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = "uint8")
cv.imshow("Blank", blank)

img = cv.imread("Photos/cat.jpg")
cv.imshow('Cat', img)

blank[200:300, 300:400] = 0, 0, 255
cv.imshow("Red", blank)

cv.rectangle(blank, (0,0), (250,500), (0, 255, 0), thickness = cv.FILLED)
cv.imshow('Rectangle', blank)

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = cv.FILLED)
cv.imshow('Rectangle', blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv.imshow("Circle", blank)

cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=3)
cv.imshow("Line", blank)

cv.putText(blank, "Hello World", (10,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)

cv.waitKey(0)