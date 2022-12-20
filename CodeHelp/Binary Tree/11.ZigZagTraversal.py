'''
https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1
'''
class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
 
        res = []
        #if root is null, we return the list.
        if root is None:
            return res
 
        #declaring two stacks to store the current and new level.
        currentLevel = []
        nextLevel = []

        ltr = True
 
        #pushing the root in currentlevel stack.
        currentLevel.append(root)
 
        while len(currentLevel) > 0:
            
            #storing the top element of currentlevel stack in temp and popping it.
            temp = currentLevel.pop(-1)
       
            #if temp is not null, we store the data at temp in list.
            res.append(temp.data)
 
            #if lefttoright is true then it stores nodes from left to right 
		    #else from right to left in nextlevel stack.
            if ltr:
                if temp.left:
                    nextLevel.append(temp.left)
                if temp.right:
                    nextLevel.append(temp.right)
            else:
                if temp.right:
                    nextLevel.append(temp.right)
                if temp.left:
                    nextLevel.append(temp.left)
 
            #if currentlevel stack is empty ltr is flipped to change 
		    #the order of storing the nodes and both stacks are swapped.
            if len(currentLevel) == 0:
            
                ltr = not ltr
                currentLevel, nextLevel = nextLevel, currentLevel
    
        #returning the list.    
        return res   