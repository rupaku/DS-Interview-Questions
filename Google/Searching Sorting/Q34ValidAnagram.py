'''
https://leetcode.com/problems/valid-anagram/solution/
 we could increment the counter for each letter in s
 and decrement the counter for each letter in t, then check if the counter reaches back to zero.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp={}
        for i in s:
            if i not in mp:
                mp[i]=0
            mp[i] +=1
        for i in t:
            if i not in mp:
                mp[i]=0
            mp[i] -=1
            
        for key in mp.keys():
            if mp[key]!=0:
                return False
        return True
