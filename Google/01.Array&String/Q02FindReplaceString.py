'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3057/

zip function after reverse:[(2, 'cd', 'ffff'), (0, 'a', 'eee')]
'''

# class Solution:
#     def findReplaceString(self, S, indexes, sources, targets):
#         '''
#         to avoid conflict we should make reverse queries.
#         change characters in right part of string has no effect on index of characters of left part.
#         '''
#         for i,j,k in sorted(zip(indexes,sources,targets),reverse=True):
#             if S[i:i+len(j)]==j:
#                 S=S[:i]+k+S[i+len(j):]
#         return S


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Create a dictionary to store the index, source, and target for each replacement operation
        replacements = {}
        for i in range(len(indices)):
            if s[indices[i]:indices[i]+len(sources[i])] == sources[i]:
                replacements[indices[i]] = (sources[i], targets[i])
        
        # Apply the replacement operations to the original string
        result = ''
        i = 0
        while i < len(s):
            if i in replacements:
                result += replacements[i][1]
                i += len(replacements[i][0])
            else:
                result += s[i]
                i += 1
        
        return result
obj = Solution()
obj.findReplaceString("abcd",[0, 2],["a", "cd"],["eee", "ffff"])