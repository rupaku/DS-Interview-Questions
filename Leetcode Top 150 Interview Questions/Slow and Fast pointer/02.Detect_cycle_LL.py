# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150

# O(n) O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow=head
        fast=head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow=slow.next
            fast=fast.next.next

        return slow