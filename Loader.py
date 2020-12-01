# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:17:22 2020

@author: ricardo.montoya
"""
import turtle

hr = turtle.Turtle()

hr.left(90)
hr.speed(200)

def tree(i):
    
    if i<10:
        return
    else:
        hr.forward(i)
        hr.left(30)
        tree(3*i/4)
        hr.right(60)
        tree(3 * i / 4)
        hr.left(30)
        hr.backward(i)

tree(100)
turtle.done()