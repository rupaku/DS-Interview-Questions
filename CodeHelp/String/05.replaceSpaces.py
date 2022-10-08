'''
https://www.codingninjas.com/codestudio/problems/replace-spaces_1172172?leftPanelTab=2
'''
"""
	Time Complexity : O(N)
	Space Complexity : O(N)

	Where 'N' is size of string of words.
"""

def replaceSpaces(str):
	# String to store result.
	res = ""
	
	# Variable to store length of string.
	leng = len(str)

	#  Iterate the length of the string.
	for i in range(leng):
		# Add "@40" in place of space.
		if(str[i] == ' '):
			res += "@40"
		# Add character to result.
		else:
			res += str[i]
		
	# Return result.
	return res