'''
https://www.codingninjas.com/codestudio/problems/remove-duplicates-from-unsorted-linked-list_1069331?leftPanelTab=1
'''
"""
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Linked list.
"""


def removeDuplicates(head):

    curr = head

    # Keep track of previous node.
    prev = None

    seen = {}
    while curr != None:
        seen[curr.data] = False
        curr = curr.next

    curr = head

    # Iterate over the given linked list.
    while curr != None:
        val = curr.data

        if seen[val]:
            # Node has been encountered before, so its a duplicate.
            # Firstly update the next pointer of the previous node.
            prev.next = curr.next

            # Delete the duplicate node.
            del curr

            # Move on to the next node.
            curr = prev.next
        else:
            # Node is seen for the first time, so add it to hash table.
            seen[val] = True

            # Move on to the next node.
            prev = curr
            curr = curr.next

    return head
