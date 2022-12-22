'''
https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
'''
def leftViewUtil(result, node,level):
    global max_level
    
    #if root is null, we simply return.
    if (node == None): 
        return
    
    #if this is the first node of its level then it is in the left view. 
    if (max_level < level):
        #storing data of current node in list.
        result.append(node.data)
        max_level = level
       
    #calling function recursively for left and right subtrees of current node. 
    leftViewUtil(result,node.left, level+1);
    leftViewUtil(result,node.right, level+1);
    

#Function to return a list containing elements of left view of the binary tree.   
def LeftView(root):
    global max_level
    max_level = 0
    result = []
    leftViewUtil(result,root,1);
    #returning the list.
    return result