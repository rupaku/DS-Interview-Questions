'''https://leetcode.com/problems/middle-of-the-linked-list/'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slowPtr=head
        fastPtr=head
        
        if(head):
            while fastPtr!=None and fastPtr.next!=None :
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next.next    

        return slowPtr        