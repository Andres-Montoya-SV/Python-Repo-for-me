# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:58:33 2020

@author: ricardo.montoya
"""

import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow("Cats", img)

average = cv.blur(img, (7, 7))
cv.imshow("Average", average)

gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussin Blur", gauss)

median_blur = cv.medianBlur(img, 7)
cv.imshow("Media", median_blur)

bilateral = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)