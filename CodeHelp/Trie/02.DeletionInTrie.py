'''
https://www.codingninjas.com/codestudio/problems/trie-delete-operation_1062663?leftPanelTab=1
'''
'''
    Time Complexity : O(N*W) (insert - O(W), search - O(W))
    Where N is the number of queries and W is the average length of input string.

    Space Complexity : O(N*W)
    Where N is the number of words inserted and W is the average length of words.
'''


class TrieNode:
    """A trie node"""

    def __init__(self):
        self.isEnd = False
        # children is the array which serves as index for the characters. There are 26 different characters
        # Therefore the size of the array is 26
        self.children = [None] * 26


# Utility function to check if root is empty
def isEmpty(root):
    for i in range(26):
        if root.children[i]:
            return False

    return True


def deleteWordHelper(root, word, depth):
    if root == None:
        return TrieNode()

    if depth == len(word):
        # Processing last character of word
        if root.isEnd:
            # To delete word
            root.isEnd = False
        if isEmpty(root):
            # To check if current node is prefix
            del root
            root = TrieNode()

        return root

    index = ord(word[depth]) - ord('a')
    root.children[index] = deleteWordHelper(root.children[index], word, depth + 1)  # Recursive call

    if isEmpty(root) and root.isEnd == False:
        # If current node does not  have child and also is not the end of any word
        del root
        root = TrieNode()

    return root


def deleteWord(root, word):
    # Maintaining depth variable
    depth = 0

    # Calling recursive function
    return deleteWordHelper(root, word, depth)
