'''
https://www.codingninjas.com/codestudio/problems/implement-a-phone-directory_1062666?leftPanelTab=1
'''
'''
    Time Complexity = O(N * (W ^ 2))
    Space Complexity = O(N * W)

    Where N is the number of elements in the given array/list and W is the maximum length of a string.
'''

class TrieNode:

	#    Constructor
	def __init__(self):
		
		#    'isEnd' is true if the node represents end of a contact.
		self.isEnd = False
		
		#    Each Trie Node contains a HashMap 'children' where each alphabet points to a Trie Node.
		self.children = {}

def insertContact(string, root):
	n = len(string)

	#    'itr' is used to iterate the Trie Nodes
	itr = root

	for i in range(n):
		
		#    Check if the string[i] is already present in our Trie.
		if string[i] not in itr.children:
			itr.children[string[i]] = TrieNode()

		next = itr.children[string[i]]

		#    Move the iterator('itr') to point to next Trie Node.
		itr = next

		#    If its the last character of the string 'str' then mark 'isEnd' as true
		if (i == n - 1):
			itr.isEnd = True
	
def viewSuggestionsHelper(curr, prefix, temp):
	
	#    Check if the string 'prefix' ends at this Node If yes then display the string found so far
	if (curr.isEnd == True):
		temp.append(prefix)

	#    Find all the adjacent Nodes to the current Node and then call the function recursively.
	c = ord('a')
	while c <= ord('z'):
		if chr(c) in curr.children:
			next = curr.children[chr(c)]
			viewSuggestionsHelper(next, prefix + chr(c), temp)
		c += 1


def viewSuggestions(string, root):
	
	prev = root

	prefix = ""

	n = len(string)

	result = []

	i = 0
	while i < n:
		
		#    'prefix' stores the string formed so far.
		prefix += string[i]

		#    Get the last character entered.
		lastCharacter = prefix[i]

		#    If nothing found, then break the loop as no more prefixes are going to be present.
		if lastCharacter not in prev.children:
			i += 1
			break
		
		#    Find the Node corresponding to the last character of 'prefix' which is pointed by prev of the Trie.			
		curr = prev.children[lastCharacter]
		
		#    If present in trie then insert all the contacts with given prefix in the result.
		temp = []

		viewSuggestionsHelper(curr, prefix, temp)
		
		result.append(temp)

		#    Change prev for next prefix
		prev = curr
		
		i += 1
	
	return result


def insertContactList(contactList, root):

	n = len(contactList)

	#    Insert each contact into the trie.
	for i in range(n):
		insertContact(contactList[i], root)

def phoneDirectory(contactList, queryStr):

	root = TrieNode()

	#    Insert all the Contacts into Trie.
	insertContactList(contactList, root)
	

	#    Return the corresponding suggestions.
	return viewSuggestions(queryStr, root)
	