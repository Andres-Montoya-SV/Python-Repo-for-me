# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:20:35 2020

@author: ricardo.montoya
"""

import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow("Cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

cany = cv.Canny(img, 125, 175)
cv.imshow("Canny", cany)

dilated = cv.dilate(cany, (3, 3), iterations=3)
cv.imshow("Dilated", dilated)

eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Eroded", eroded)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

cropped  = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)