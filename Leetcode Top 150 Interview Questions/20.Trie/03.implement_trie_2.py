#https://leetcode.com/problems/implement-trie-ii-prefix-tree/


class Trie(object):

    def __init__(self):
        self.trie={}
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr=self.trie
        for letter in word:
            if letter not in curr:
                curr[letter]= {"count":1}
            else:
                curr[letter]["count"] += 1
            curr=curr[letter]
        curr['$']=None
        
        

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        curr=self.trie
        for letter in word:
            if letter not in curr:
                return 0
            else:
                curr=curr[letter]
        word_count= curr["count"]
        for letter in curr:
            if letter !='$' and letter != "count":
                word_count-=curr[letter]["count"]
        return word_count

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr=self.trie
        for letter in prefix:
            if letter not in curr:
                return 0
            else:
                curr=curr[letter]
        return curr["count"]
        

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr=self.trie
        for letter in word:
            curr[letter]["count"]-=1
            curr=curr[letter]
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)