'''
https://leetcode.com/problems/longest-string-chain/submissions/
'''
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(reverse=True)
        word_cache=set(words)
        memo=dict() # to store longest possible word seq
        visited=set()
        def dfs(word):
            t_max=1
            if word in memo:
                return memo[word]
            visited.add(word)
            for i in range(len(word)):
                temp=word[:i]+word[i+1:]
                if temp in word_cache:
                    t_max=max(t_max,dfs(temp)+1)
            memo[word]=t_max
            return memo[word]
        res=0
        for word in words:
            if word not in visited:
                res=max(dfs(word),res)
        return res
        
        