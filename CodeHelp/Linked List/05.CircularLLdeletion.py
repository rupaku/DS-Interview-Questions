'''
https://www.codingninjas.com/codestudio/problems/deletion-in-circular-linked-list_630409?leftPanelTab=2
'''
'''
    Time complexity: O(N)
    Space complexity: O(N)
    
    Where N is the size of the circular linked list
'''

def helper(root,key,head) :

    # Check if root is equal to head
    if (root == head) :
        return root

    # Check if the value of root node is equal to key
    if (root.data == key) :
        next = root.next
        return next

    root.next = helper(root.next, key, head)

    # Return the root node
    return root

def deleteNode(head,key):

    # Check if head is empty node
    if (head == None):
        return None

    # Check if the value of head node is equal to key
    if (head.data == key): 

        if (head == head.next):
            return None

        head = head.next

    # Make recursive call
    head.next = helper(head.next, key, head)

    return head
