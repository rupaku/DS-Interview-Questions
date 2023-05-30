'''https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/958850956/'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        point_a = headA
        point_b= headB
        while point_a != point_b:
            point_a = headB if point_a is None else point_a.next
            point_b = headA if point_b is None else point_b.next
        return point_a