'''
https://www.codingninjas.com/codestudio/problems/merge-sort-linked-list_920473?leftPanelTab=1
'''
from os import *
from sys import *
from collections import *
from math import *

# Node class 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next


def find_mid(head):
    slow=head
    fast=head.next
    while(fast != None or fast.next != None):
        slow=slow.next
        fast=fast.next.next
    return slow

def merge(left,right):
    if left == None:
        return right
    if right == None:
        return left
    
    ans=Node(-1)
    temp=ans
    
    while left != None and right != None:
        if left.data < right.data:
            temp.next=left
            temp=left
            left=left.next
        else:
            temp.next=right
            temp=right
            right=right.next
    while left != None:
        temp.next=left
        temp=left
        left=left.next
    while right != None:
        temp.next=right
        temp=right
        right=right.next  
    ans=ans.next
    return ans
        
def sortLL(head):
    # Write your code here.
    if (head == None or head.next == None):
        return head
    
    mid= find_mid(head)
    left=head
    right=mid.next
    mid.next=None
    left=sortLL(left)
    right=sortLL(right)
    result= merge(left,right)
    return result


    
    