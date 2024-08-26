# https://leetcode.com/problems/sort-list/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def sortList(self, head):
        # If the head or the entire list is none, return the head
        if not head or not head.next:
            return head
        # Get the middle node
        mid = self.getMid(head)
        # Split the list to left and right and sort them
        left = self.sortList(head)
        right = self.sortList(mid)
        # Merge the sorted lists
        return self.merge(left, right)

    def merge(self, list1, list2):
        dummyHead = ListNode(0)
        tail = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummyHead.next

    def getMid(self, head):
        midPrev = None
        while head and head.next:
            midPrev = head if not midPrev else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid