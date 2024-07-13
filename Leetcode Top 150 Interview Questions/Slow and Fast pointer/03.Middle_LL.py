#https://leetcode.com/problems/middle-of-the-linked-list/

# O(n) O(1)

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow=head
        fast=head
        while fast and fast.next:
            slow=head.next
            fast=fast.next.next

        return slow