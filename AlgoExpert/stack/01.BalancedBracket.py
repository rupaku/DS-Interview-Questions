'''
https://www.algoexpert.io/questions/Balanced%20Brackets
'''
# O(n) time | O(n) space
def balancedBrackets(string):
    # Write your code here.
    openB ="([{"
	closeB = ")]}"
	matchingB = {")":"(","]":"[","}":"{"}
	stack=[]
	for char in string:
		if char in openB:
			stack.append(char)
		elif char in closeB:
			if len(stack) == 0:
				return False
			if stack[-1] == matchingB[char]:
				stack.pop()
			else:
				return False
	return len(stack) == 0
