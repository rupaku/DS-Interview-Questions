'''
https://leetcode.com/problems/plus-one-linked-list/solution/
create sentinel node pointing to head
check rightmost not nine digit
increment it by 1
set all following 9 to 0
return sentinel or sentinet next val
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        #sentinel head
        x= ListNode(0)
        x.next =head
        not_nine = x
        
        #rightmost non-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head=head.next
        
        #increment not nine by 1
        not_nine.val +=1
        not_nine =not_nine.next
        
        #set all following 9 to 0
        while not_nine:
            not_nine.val=0
            not_nine=not_nine.next
        
        return x if x.val else x.next
                
                