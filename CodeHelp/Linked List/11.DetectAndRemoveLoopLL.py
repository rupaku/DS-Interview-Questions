'''
https://www.codingninjas.com/codestudio/problems/interview-shuriken-42-detect-and-remove-loop_241049?leftPanelTab=2
'''
"""
    Time Complexity: O(N)
    Space Complexity: O(1)

    where ‘N’ is the number of nodes in the list.   
"""

from typing import *


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeLoop(head: Node) -> Node:

    if head == None or head.next == None:
        return head

    #  Slow Pointer - This will be incremented by 1 Nodes
    slow = head

    #  Fast Pointer  - This will be incremented by 2 Nodes
    fast = head

    while True:

        #  We reached the end of the List and haven't found any Cycle
        if fast == None or fast.next == None:
            return head

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    # Cycle Found.
    fast = head

    # start will point the starting node of cycle.
    start = None

    while fast != slow:

        fast = fast.next
        slow = slow.next

    start = slow

    # Finding the previous node of 'start'.
    cur = head

    while True:

        if cur.next == start:

            cur.next = None
            return head

        cur = cur.next
