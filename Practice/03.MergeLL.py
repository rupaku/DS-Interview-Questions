'''
https://leetcode.com/problems/merge-two-sorted-lists/submissions/
'''
import pdb

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

pdb.set_trace()
x = [1,2,4]
y = [1,3,4]
res = Solution.mergeTwoLists(x, y)
print(res)