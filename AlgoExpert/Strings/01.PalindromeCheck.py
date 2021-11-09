'''
https://www.algoexpert.io/questions/Palindrome%20Check
'''

# Method 1
# O(n^2) time | O(n) space
def isPalindrome(string):
    # Write your code here.
    reversedString=""
	for i in reversed(range(len(string))):
		reversedString += string[i]
	return string == reversedString

# Method 2
# O(n) time | O(n) space
def isPalindrome(string):
    # Write your code here.
    reversedChars=[]
	for i in reversed(range(len(string))):
		reversedChars.append(string[i])
	return string == "".join(reversedChars)

# Method 3
# O(n) time | O(1) space
def isPalindrome(string):
    # Write your code here.
    leftIdx=0
	rightIdx=len(string)-1
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return False
		leftIdx += 1
		rightIdx -= 1
	return True


