# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=ListNode(0, head)
        # predecessor = the last node before the sublist of duplicates
        pred=curr
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head=head.next

                # Skip all duplicates
                pred.next=head.next
            else:
                pred=pred.next
            head=head.next
        return curr.next