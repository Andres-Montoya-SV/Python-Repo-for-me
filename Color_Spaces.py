# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:32:29 2020

@author: ricardo.montoya
"""

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/cat.jpg")
cv.imshow("Cat", img)


plt.imshow(img)
plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("Lab", lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

plt.imshow(rgb)
plt.show()

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV --> BGR", hsv_bgr)

cv.waitKey(0)