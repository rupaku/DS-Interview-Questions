'''
https://www.codingninjas.com/codestudio/problems/h_920474?leftPanelTab=1
'''
"""

    Time Complexity : O(N + M)
    Space Complexity : O(N + M)

    Where,‘N’ and ‘M’ are the number of nodes in the
    first BST and the second BST respectively.

"""

class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

# Function to store the inorder traversal of tree in a list.
def storeInOrder(root, arr):
    if (root != None):
        storeInOrder(root.left, arr)
        arr.append(root.data)
        storeInOrder(root.right, arr)

# Function to merge two sorted array/lists.
def mergeSortedArrays(arr1, arr2):
    i = 0
    j = 0
    arr = []
    
    while (i < len(arr1) and j < len(arr2)):
        if (arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
          
    while (i < len(arr1)):
        arr.append(arr1[i])
        i += 1
    
    while (j < len(arr2)):
        arr.append(arr2[j])
        j += 1
    
    return arr


# Function to convert sorted array-list to balanced BST.
def constructBSTFromSortedArray(arr, start, end):
    # Base case.
    if (start > end):
        return None
    
    mid = (start + end) // 2
    
    root = TreeNode(arr[mid])
    root.left = constructBSTFromSortedArray(arr, start, mid - 1)
    root.right = constructBSTFromSortedArray(arr, mid + 1, end)
    return root


def mergeBST(root1, root2):
    # Store the in-order traversal of tree1 in an array.
    temp1 = []
    storeInOrder(root1, temp1)
    
    # Store the in-order traversal of tree2 in an array.
    temp2 = []
    storeInOrder(root2, temp2)
    
    # Merge the two sorted arrays.
    final = mergeSortedArrays(temp1, temp2)
    
    # Construct the balanced BST from this sorted array.
    return constructBSTFromSortedArray(final, 0, len(final) - 1)
