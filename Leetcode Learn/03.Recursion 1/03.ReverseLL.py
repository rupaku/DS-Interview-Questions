'''
https://leetcode.com/problems/reverse-linked-list/submissions/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        second = head.next
        reverse = self.reverseList(second)
        second.next = head
        head.next = None
        
        return reverse
        
        