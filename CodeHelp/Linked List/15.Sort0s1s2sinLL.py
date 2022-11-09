'''
https://www.codingninjas.com/codestudio/problems/sort-linked-list-of-0s-1s-2s_1071937?leftPanelTab=2
'''
'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where N is number of nodes in the linked list.
'''

def sortList(head):

    ptr = head
    cnt = [0] * 3

    # Iterate while ptr is not empty
    while(ptr != None):
        cnt[ptr.data] += 1
        ptr = ptr.next
    
    ptr = head
    i = 0
     
    # Updating data.
    while(ptr != None):
        
        while(cnt[i] == 0):
            i += 1
        
        ptr.data = i
        cnt[i] -= 1
        ptr = ptr.next

    # Return head    
    return head
