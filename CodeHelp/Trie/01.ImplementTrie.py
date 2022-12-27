'''
https://www.codingninjas.com/codestudio/problems/implement-trie_631356?leftPanelTab=1
'''
'''
    Time Complexity : O(N*W) (insert - O(W), search - O(W), startsWith - O(W))
    Space Complexity : O(N*W)

    Where N is the number of queries and W is the average length of words.
'''
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

class TrieNode :
    
    def __init__(self) :

        self.child = {}
        self.isEnd = False

class Trie :

    def __init__(self) :

        self.node = TrieNode()
    
    def insert(self, string) :

        n = len(string)
        if(n == 0) :
            self.node.isEnd = True
            return 
        else :
            if string[0] in self.node.child :
                self.node.child[string[0]].insert(string[1:])
            
            else :
                self.node.child[string[0]] = Trie()
                self.node.child[string[0]].insert(string[1:])
        return 

    
    def search(self, word) :
        temp = self.node
        for i in range(len(word)) :
            if word[i] not in temp.child :
                return False
            
            else :
                temp = temp.child[word[i]].node

        if(temp.isEnd == True) :
            return True
        else :
            return False

        
    def startWith(self, prefix) :
        temp = self.node
        for i in range(len(prefix)) :
            if prefix[i] not in temp.child :
                return False

            temp = temp.child[prefix[i]].node
        
        return True



# main
t = int(input().strip())
root = Trie()
for i in range(t) :

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1) :
        root.insert(str1)
    
    elif (q == 2) :
        if(root.search(str1)) :
            print("true") 

        else :
            print("false")
        
    else :
        if(root.startWith(str1)) :
            print("true")

        else :
            print("false")

