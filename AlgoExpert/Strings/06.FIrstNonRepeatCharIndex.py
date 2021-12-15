'''
https://www.algoexpert.io/questions/First%20Non-Repeating%20Character
'''
#O(n)  | O(1) space
def firstNonRepeatingCharacter(string):
    # Write your code here.
    char_freq = {}
	for character in string:
		char_freq[character] = char_freq.get(character,0) + 1
	for idx in range(len(string)):
		character = string[idx]
		if char_freq[character] == 1:
			return idx
	return -1
