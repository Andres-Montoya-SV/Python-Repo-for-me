# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:25:20 2020

@author: ricardo.montoya
"""

import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,  30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise_Or", bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise_XOR", bitwise_xor)

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT", rectangle)

cv.waitKey(0)