# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:51:59 2022

@author: kikig
"""
import matplotlib.pyplot as plt
import numpy as np


def std(arr, mean=2500):
    sum = 0
    for i in arr:
        sum += (i-mean)**2
    return np.sqrt(sum/len(arr))


def std_2(arr, mean=[10000, 0]):
    sum = 0
    mean = np.full(len(arr), mean)
    for a, b in zip(arr, mean):
        sum += (a-b)**2
    return np.sqrt(sum/len(arr))

res1 = [2311, 2104, 2918, 2667] # no error correction
res2 = [2619, 1940, 2801, 2640] # error correction, design 1
res3 = [2847, 2286, 2559, 2308] # error correction, design 2

print(std(res1))
print(std(res2))
print(std(res3))

def p_error(p):
    return 3*(p**2)*(1-p)+p**3

test_1 = [8382, 1618]
test_2 = [9913, 87]

print(std_2(test_1)) # error correction
print(std_2(test_2)) # no error correction

#print(p_error(0.05))


#x = np.linspace(0, 0.1, 100)
#y = p_error(x)

#plt.plot(x, y)
#plt.show()