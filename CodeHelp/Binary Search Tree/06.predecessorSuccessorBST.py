'''
https://www.codingninjas.com/codestudio/problems/predecessor-and-successor_920476?leftPanelTab=1
'''
'''
    Time Complexity : O(N)
	Space Complexity : O(N)

	Where 'N' is the number of nodes in the tree.
'''

pre = None
suc = None

def findPreSucHelp(root, pre, suc, key):
    # Base case.
    if root == None:
        return (pre, suc)

    # If key is present at root.
    if root.data == key:

        # The maximum value in left subtree is predecessor.
        if root.left != None:
            tmp = root.left
            while tmp.right != None:
                tmp = tmp.right

            pre = tmp

        # The minimum value in right subtree is successor.
        if root.right != None:
            tmp = root.right
            while tmp.left != None:
                tmp = tmp.left

            suc = tmp

        return(pre, suc)

    # If key is smaller than root's key, go to left subtree.
    if root.data > key:
        suc = root
        return findPreSucHelp(root.left, pre, suc, key)

    # Else go to right subtree.
    else:
        pre = root
        return findPreSucHelp(root.right, pre, suc, key)

def findPreSuc(root, key):
    
    global suc
    global pre

    pre, suc = findPreSucHelp(root, pre, suc, key)
    
    res = []
    
    if pre != None:
        res.append(pre.data)
    else:
        res.append(-1)


    if suc != None:
        res.append(suc.data)
    else:
        res.append(-1)

    pre = None
    suc = None

    return res