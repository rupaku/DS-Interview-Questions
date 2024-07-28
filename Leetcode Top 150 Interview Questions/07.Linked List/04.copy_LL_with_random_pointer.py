# https://leetcode.com/problems/copy-list-with-random-pointer/?envType=study-plan-v2&envId=top-interview-150
class Node:
    def __init__(self,val=0, next=None, random=None):
        self.val=val
        self.next=next
        self.random=random

class Solution:
    def __init__(self):
        self.visited_hash={}

    def copy_LL(self,head):
        if head is Node:
            return head
        
        if head in self.visited_hash:
            return self.visited_hash[head]
        
        node=Node(head.val, None, None)
        self.visited_hash[head]=node

        node.next= Solution.copy_LL(head.next)
        node.random=Solution.copy_LL(head.random)

        return node