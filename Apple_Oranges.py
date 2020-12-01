# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:05:06 2020

@author: ricardo.montoya
"""

from sklearn import tree


###################################################################################
## features = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170,  "bumpy"]]##
## labels = ["Apple","Apple", "Orange", "Orange"]                                ##
###################################################################################

features = [[140, 1], [130, 1], [150, 0], [170,  0]]
labels = [0,0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150, 0]]))