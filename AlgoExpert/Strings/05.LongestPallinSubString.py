'''
https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring
'''
#time O(n2) | space O(n)
def longestPalindromicSubstring(string):
    # Write your code here.
    currLongest=[0,1]
	for i in range(1,len(string)):
		odd = getLongestPallinFrom(string,i-1,i+1)
		even = getLongestPallinFrom(string,i-1,i)
		
		longest = max(odd,even,key=lambda x: x[1]-x[0])
		currLongest = max(longest,currLongest,key=lambda x: x[1]-x[0])
	return string[currLongest[0]:currLongest[1]]

def getLongestPallinFrom(string,left,right):
	while left >=0 and right < len(string):
		if string[left] != string[right]:
			break
		left -= 1
		right += 1
	return [left+1,right]