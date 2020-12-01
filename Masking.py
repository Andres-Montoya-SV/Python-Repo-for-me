# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:37:37 2020

@author: ricardo.montoya
"""

import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat2.jpg")
cv.imshow("Cat", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank Image", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Imaged", masked)

rectangle = cv.rectangle(blank.copy(), (30,  30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Weird Shape", weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("Masked Imaged", masked)

cv.waitKey(0)