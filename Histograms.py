# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:52:01 2020

@author: ricardo.montoya
"""
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread("Photos/cat2.jpg")
cv.imshow("Cat", img)

blank = np.zeros(img.shape[:2], dtype="uint8")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(img, img, mask = circle)
cv.imshow("Mask", mask)

gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
color = ("b", "g", "r")
for i, col in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)