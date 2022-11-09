'''
https://www.codingninjas.com/codestudio/problems/split-a-circular-linked-list_1071003
'''
"""
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where N is the number of Nodes in the circular linked list.
"""


def splitCircularList(head):
    slow = head
    fast = head

    while fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    fast = fast.next

    fast.next = slow.next

    slow.next = head
