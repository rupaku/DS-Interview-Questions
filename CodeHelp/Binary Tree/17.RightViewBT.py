'''
https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1
'''
class Solution:
    
    #Function to get the right view of the binary tree.
    def rightViewUtil(self,result, root, level, max_level): 
          
        #if root is null, we simply return. 
        if root is None: 
            return
          
        #if this is the last node of its level then it is in the right view.
        if (max_level[0] < level):
            
            #storing data of current node in list.
            result.append(root.data) 
            max_level[0] = level 
      
        #calling function recursively for right and left 
        #subtrees of current node.
        self.rightViewUtil(result, root.right, level+1, max_level) 
        self.rightViewUtil(result, root.left, level+1, max_level) 
    
    #Function to return list containing elements of right view of binary tree. 
    def rightView(self,root): 
        max_level = [0] 
        result = []
        self.rightViewUtil(result,root, 1, max_level) 
        #returning the list.
        return result