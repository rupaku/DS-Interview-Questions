'''
https://leetcode.com/problems/isomorphic-strings/submissions/
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(word):
            output=[]
            lookup={}
            i=1
            for w in word:
                if w not in lookup:
                    lookup[w]=i
                    i=i+1
                output.append(lookup[w])
            return output
        return helper(s) == helper(t)
        