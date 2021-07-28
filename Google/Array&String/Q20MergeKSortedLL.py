'''
https://leetcode.com/problems/merge-k-sorted-lists/submissions/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #Divide and conquer
        n=len(lists)
        interval=1
        while interval < n :
            for i in range(0,n-interval,interval*2):
                lists[i] = self.mergeTwoLists(lists[i],lists[i+interval])
            interval = interval*2
        return lists[0] if n > 0 else None
            
    def mergeTwoLists(self,l1,l2):
        head=point=ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                point.next =l1
                l1=l1.next
            else:
                point.next =l2
                l2=l1
                l1=point.next.next
            point=point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
            
        return head.next