#https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def add_two_LL(self, l1:ListNode, l2:ListNode) -> ListNode:
        carry=0
        res = ListNode(0)
        res_tail=res
        while l1 or l2 or carry:
            v1= (l1.val if l1 else 0)
            v2= (l2.val if l2 else 0)
            carry,out = divmod(v1+v2+carry,10)
            res_tail.next=ListNode(out)
            res_tail=res_tail.next
            l1=l1 if l1.next else None
            l2=l2 if l2.next else None
        return res.next