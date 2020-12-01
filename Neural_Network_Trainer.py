# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:43:21 2020

@author: ricardo.montoya
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmod_deritive(x):
    return x * (1 - x)

training_inputs = np.array([[0, 0, 1],
                              [1, 1, 1],
                              [1, 0, 1],
                              [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T
Synaptics_weight = 2 * np.random.random((3, 1)) - 1

np.random.seed(1)

print("Random starting sypnatics weights: ")
print(Synaptics_weight)

for iteration in range(10000000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, Synaptics_weight))
    error = training_outputs - outputs
    
    adjustments = error * sigmod_deritive(outputs)
    
    Synaptics_weight += np.dot(input_layer.T, adjustments)
    
print("Synaptic weights after training")
print(Synaptics_weight)

print("Outputs after training: ")
print(outputs)

