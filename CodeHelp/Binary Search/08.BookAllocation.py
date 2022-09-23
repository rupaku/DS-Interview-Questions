'''
https://www.codingninjas.com/codestudio/problems/allocate-books_1090540
'''

from os import *
from sys import *
from collections import *
from math import *

def is_possible(arr,n,m,mid):
    student_cnt=1
    pagesm=0
    for i in range(len(arr)):
        if (pagesm+arr[i] <= mid):
            pagesm += arr[i]
        else:
            student_cnt = student_cnt + 1
            if student_cnt < m or arr[i] > mid:
                return False
            pagesm=arr[i]
    return True
            
def allocateBooks(arr, n, m):

    # Write your code here
    # Return the minimum number of pages
    s=0
    sm=0
    for i in range(len(arr)):
        sm=sm+arr[i]
    e=sm
    ans=-1
    while s <= e:
        mid= (s+e)//2
        if is_possible(arr,n,m,mid):
            ans=mid
            e=mid-1 #left part
        else:
            s=mid+1
    return ans
