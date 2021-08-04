'''
https://leetcode.com/explore/interview/card/google/65/design-4/3095/
https://www.youtube.com/watch?v=xsnAlMknB9o
'''
class Trie:
    def __init__(self):
        self.root ={}
        
    def insert(self,sentence):
        curr = self.root
        for l in sentence:
            if l not in curr:
                curr[l]={}
            curr = curr[l]
        curr['#'] = sentence
        
        # {i:{' ':{l:{o:{}}}}}
        
    def search(self, prefix, curr=None):
        if not curr:
            curr=self.root
        for c in prefix:
            if c not in curr:
                return []
            curr =curr[c]
        ans =[]
        for k in curr:
            if k == "#":
                ans.append(curr[k])
            else:
                ans += self.search('',curr[k])
        return ans
            
        
            
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.lookUp={}
        for i,s in enumerate(sentences):
            self.lookUp[s] = times[i]
            
        self.trie = Trie()
        for s in sentences:
            self.trie.insert(s)
        self.keyword=""
        
        

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.lookUp[self.keyword] = self.lookUp.get(self.keyword,0) +1
            self.trie.insert(self.keyword)
            self.keyword=""
            return []
        else:
            self.keyword += c
            lst=self.trie.search(self.keyword)
            lst.sort(key= lambda x: (-self.lookUp[x],x))
            #toget 3 elements
            return lst[:3]
            

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)