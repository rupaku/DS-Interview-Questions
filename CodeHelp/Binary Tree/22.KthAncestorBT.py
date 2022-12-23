'''
https://practice.geeksforgeeks.org/problems/kth-ancestor-in-a-tree/1
'''
def generateArray(root, ancestors):
    # There will be no ancestor of root node
    ancestors[root.data] = -1

    # level order traversal to
    # generate 1st ancestor
    q = []
    q.append(root)

    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (temp.left):
            ancestors[temp.left.data] = temp.data
            q.append(temp.left)

        if (temp.right):
            ancestors[temp.right.data] = temp.data
            q.append(temp.right)

        # function to calculate Kth ancestor


def kthAncestor(root,k, node):
    # create array to store 1st ancestors
    ancestors = [0] * (10001)

    # generate first ancestor array
    generateArray(root, ancestors)

    # variable to track record of number
    # of ancestors visited
    count = 0

    while (node != -1):
        node = ancestors[node]
        count += 1
        if (count == k):
            break

    # prKth ancestor
    return node