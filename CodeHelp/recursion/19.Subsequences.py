'''
https://www.codingninjas.com/codestudio/problems/subsequences-of-string_985087?leftPanelTab=1
'''
from os import *
from sys import *
from collections import *
from math import *

def helper(str,index,temp,res):
    if index == len(str):
        if len(temp) != 0:
            res.append(temp)
        return
    helper(str,index+1,temp,res)
    temp=temp+str[index]
    helper(str,index+1,temp,res)
 
def subsequences(str):

    # Write your code here
    res=[]
    helper(str,0,"",res)
    return res

