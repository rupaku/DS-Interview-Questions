'''
https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
'''
class Height: 
    def __init__(self): 
        self.height = 0

#Function to check for balanced tree.
def isBalancedUtil(root, height): 
      
    lh = Height() 
    rh = Height() 
  
    #if root is null, we return true.
    if root is None: 
        return True
  
    #calling the function isBalancedUtil recursively for the heights of left 
    #and right subtrees and storing the returned values in l and r.
    l = isBalancedUtil(root.left, lh) 
    r = isBalancedUtil(root.right, rh) 
  
    #height of current node is (max of heights of left and right subtrees) +1.
    height.height = max(lh.height, rh.height) + 1
  
    #if difference between heights of left and right subtrees is 2 or more 
    #than 2 then this node is not balanced so we return false.
    if abs(lh.height - rh.height) >= 2: 
        return False  
  
    #if this node is balanced and left and right subtrees are balanced 
    #then we return true.
    else:
        return l and r

class Solution: 
    #Function to check whether a binary tree is balanced or not.   
    def isBalanced(self,root):
        height = Height() 
        return isBalancedUtil(root,height)
    
    