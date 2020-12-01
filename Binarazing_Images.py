# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:29:06 2020

@author: ricardo.montoya
"""

import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold Inverse", thresh_inv)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 3)
cv.imshow("Adaptive Threshold", adaptive_thresh)

cv.waitKey(0)