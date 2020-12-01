# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:18:10 2020

@author: ricardo.montoya
"""

import time
import subprocess

while True:
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
