'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3057/

zip function after reverse:[(2, 'cd', 'ffff'), (0, 'a', 'eee')]
'''

class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        '''
        to avoid conflict we should make reverse queries.
        change characters in right part of string has no effect on index of characters of left part.
        '''
        for i,j,k in sorted(zip(indexes,sources,targets),reverse=True):
            if S[i:i+len(j)]==j:
                S=S[:i]+k+S[i+len(j):]
        return S

obj = Solution()
obj.findReplaceString("abcd",[0, 2],["a", "cd"],["eee", "ffff"])