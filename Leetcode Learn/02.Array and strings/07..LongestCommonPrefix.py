'''
https://leetcode.com/problems/longest-common-prefix/submissions/
find minimum length string ,iterate over it and find ith unique char, if its len(ch) == 1, increment prefix 
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_str = min([len(st) for st in strs])
        prefix=""
        
        for i in range(min_len_str):
            
            ch = list(set([st[i] for st in strs])) #take ith unique value
            
            if len(ch) == 1:
                prefix+=ch[0] #append common char
            else:
                break
        return prefix