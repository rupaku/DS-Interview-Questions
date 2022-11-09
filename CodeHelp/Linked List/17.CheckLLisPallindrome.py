'''
https://leetcode.com/problems/palindrome-linked-list/description/
'''
'''
    Time Complexity: O(N)
    Space complexity: O(N)
    
    Where N is the number of nodes in the linked list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        visitedNodes = []

        # push all nodes in the stack
        cur = head

        while (cur != None):
            visitedNodes.append(cur)
            cur = cur.next

        cur = head
        while (cur != None):

            # compare node values
            temp = visitedNodes.pop()
            if (cur.val != temp.val):
                return False

            cur = cur.next

        return True
