'''
https://leetcode.com/problems/longest-common-prefix/submissions/866304346/
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = {}
        
        # Add words to trie
        for word in strs:
            curNode = trie
            for char in word:
                if char not in curNode:
                    curNode[char] = {}
                curNode = curNode[char]    
            curNode['*'] = {}    
        
        curNode = trie
        curPre = ''
        while len(curNode) == 1 and '*' not in curNode: # only have one child and current node is not an endword
            for key in curNode:
                curNode = curNode[key]
                curPre += key
        return curPre        
                
            