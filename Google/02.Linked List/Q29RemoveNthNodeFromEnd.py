'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size=1
        curr = p =head
        while curr.next:
            size=size+1
            curr = curr.next
            if size > n+1:
                p=p.next
        if size == n:
            return head.next
        else:
            p.next=p.next.next
            return head
        