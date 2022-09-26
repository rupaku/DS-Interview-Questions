'''
https://www.codingninjas.com/codestudio/problems/reverse-the-array_1262298?leftPanelTab=0
'''
from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    # Write your code here.
    s=m+1
    e=len(arr)-1
    while s < e:
        arr[s],arr[e] = arr[e],arr[s]
        s=s+1
        e=e-1
    return arr
