#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        first=dummy
        sec=dummy
        #move first pointer one ahead
        for i in range(n+1):
            first=first.next
        #move first till end
        while first is not None:
            first=first.next
            sec=sec.next
        sec.next=sec.next.next
        return dummy.next