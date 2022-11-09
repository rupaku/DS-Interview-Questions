'''
https://www.codingninjas.com/codestudio/problems/unique-sorted-list_2420283
'''
'''
    Time Complexity: O( L )
    Space Complexity: O( 1 )

    where L denotes the length of the linked list
'''


def uniqueSortedList(head):

    # Initialize 'cur' to store head
    cur = head

    # Run a while loop
    while head != None and cur.next != None:

        # Next element has same value as the current element
        if (cur.next.data == cur.data):

            # Adjust links to remove the next element
            cur.next = cur.next.next

        # Next element is different from the current element
        else:
            cur = cur.next

    return head
