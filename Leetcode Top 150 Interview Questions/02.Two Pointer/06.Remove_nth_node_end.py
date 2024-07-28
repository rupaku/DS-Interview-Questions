# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150

# start with l and r with head, move r n step ahead, move both till r comes to end.Then l would be n step from end before.remove link of l
# time Com O(n) , space comp O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right=head
        left=head
        for i in range(n):
            right=right.next
        if not right:
            return head.next
        while right.next:
            left=left.next
            right=right.next
        left.next=left.next.next
        return head