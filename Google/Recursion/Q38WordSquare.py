'''
https://leetcode.com/explore/interview/card/google/62/recursion-4/370/
https://www.youtube.com/watch?v=YTQjsPiMtRk
'''
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words=words
        self.n=len(words[0])
        self.buildPrefixHashTable(self.words)
        res=[]
        word_sq=[]
        for word in words:
            word_sq=[word]
            self.backtracking(1,word_sq,res)
        return res
    
    def backtracking(self,step,word_sq,res):
        if step == self.n:
            res.append(word_sq[:])
            return
        
        prefix=''.join([word[step] for word in word_sq])
        for i in self.getWordsWithPrefix(prefix):
            word_sq.append(i)
            self.backtracking(step+1,word_sq,res)
            word_sq.pop()
            
    def buildPrefixHashTable(self,words):
        self.prefixHashTable ={}
        for word in words:
            for prefix in (word[:i] for i in range(1,len(word))):
                self.prefixHashTable.setdefault(prefix,set()).add(word)
    
    def getWordsWithPrefix(self,prefix):
        if prefix in self.prefixHashTable:
            return self.prefixHashTable[prefix]
        else:
            return set([])
    