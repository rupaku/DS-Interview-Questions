'''
https://www.codingninjas.com/codestudio/problems/insertion-in-circular-linked-list_4609562?leftPanelTab=0
'''
'''
    Time Complexity : O(K)
    Space Complexity : O(1)

    Where, K is the position of the node to be inserted in the list.
'''

'''
    Following is the linkedList class structure:
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert(k, val, head):
    
    length = 1
    cur = head
    
    while cur.next != head:
        length += 1
        cur = cur.next
    
    start = False
    
    # If the node is inserted at beginning.
    
    if k == 0:
        start = True
        k = length

    itr = head

    # Iterating to get the node at k-1th position.
    for i in range(1, k):
        itr = itr.next

    # Node with value 'val'.
    temp = Node(val)

    # Inserting the temp between node pointed by
    # itr and itr->next.
    temp.next = itr.next
    itr.next = temp
    
    if start == True:
        return temp
    return head
