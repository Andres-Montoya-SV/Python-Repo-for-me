# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:23:36 2020

@author: ricardo.montoya
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
driver.get("https://youtube.com/")

searchBox = driver.find_element_by_xpath('//*[@id="search"]')
searchBox.send_keys("Python Browser Automatization Test")
searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
