# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:20:12 2020

@author: ricardo.montoya
"""
from selenium import webdriver
import pywhatkit
driver = webdriver.Chrome()

pywhatkit.sendwhatmsg('[Area code + Phone Number]', 'Python Automated Message', 18, 49)