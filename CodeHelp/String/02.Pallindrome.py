'''
https://www.codingninjas.com/codestudio/problems/check-if-the-string-is-a-palindrome_1062633
'''
'''
	Time complexity: O((length(S))
	Space Complexity: O(1)
	
	Where S is the given string. 
'''

def toLowerCase(s):

    str = ""

	# Traverse through the string s
    for i in range(len(s)):

        ch = s[i]

		# Check if ch is a uppercase letter
        if (ch <= 'Z' and ch >= 'A'):
            ch = ord(ch) - (ord('A') - ord('a'))
            ch = chr(ch)

        str = str + ch
	
    return str

def checkPalindrome(s):

	# Convert uppercase letter into lowercase letter
    s = toLowerCase(s)

    i = 0
    j = len(s) - 1

    while (i < j):

        if (s[i].isalnum() == False):

            # ith pointer points to invalid character.
            i += 1

        elif (s[j].isalnum() == False):

            # jth pointer points to invalid character.
            j -= 1

        elif (s[i] == s[j]):
            i += 1
            j -= 1

        else:
            return False

    return True
