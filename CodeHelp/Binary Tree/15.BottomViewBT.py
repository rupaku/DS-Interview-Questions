'''
https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
'''
class Solution:
    #Function to return a list containing the bottom view of the given tree.
    def bottomView(self, root):
        if (root == None):
            return
        
        # Initialize a variable 'hd' with 0
        # for the root element.
        hd = 0
        
        # TreeMap which stores key value pair
        # sorted on key value
        m = dict()
        mh = dict()
     
        # Queue to store tree nodes in level
        # order traversal
        q = []
     
        # Assign initialized horizontal distance
        # value to root node and add it to the queue.
        mh[root] = hd
        
        # In STL, append() is used enqueue an item
        q.append(root)  
     
        # Loop until the queue is empty (standard
        # level order loop)
        while (len(q) != 0):
            temp = q[0]
            
            # In STL, pop() is used dequeue an item
            q.pop(0)  
            
            # Extract the horizontal distance value
            # from the dequeued tree node.
            hd = mh[temp]
     
            # Put the dequeued tree node to TreeMap
            # having key as horizontal distance. Every
            # time we find a node having same horizontal
            # distance we need to replace the data in
            # the map.
            m[hd] = temp.data
     
            # If the dequeued node has a left child, add
            # it to the queue with a horizontal distance hd-1.
            if (temp.left != None):
                mh[temp.left] = hd - 1
                q.append(temp.left)
     
            # If the dequeued node has a right child, add
            # it to the queue with a horizontal distance
            # hd+1.
            if (temp.right != None):
                mh[temp.right] = hd + 1
                q.append(temp.right)
        ans = []
        for i in sorted(m.keys()):
            ans.append(m[i])
            
        return ans