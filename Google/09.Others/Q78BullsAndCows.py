'''
https://leetcode.com/problems/bulls-and-cows/solution/
https://www.youtube.com/watch?v=Jip-D8TgsGM
Bulls-> current digit at corrct position
cows -> currect digits at wrong position
list secret and guess
check if char is same and at right position then pop that element
find count of each char with count in s
check this count with guess,decrement cows 
'''
from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        cow=0
        s=list(secret)
        g=list(guess)
        i=0
        j=0
        while i < len(secret):
            if s[j]== g[j]:
                bull= bull+1
                s.pop(j)
                g.pop(j)
            else:
                j=j+1
            i=i+1
        
        count=Counter(s)
        for l in g:
            if l in count and count[l] > 0:
                cow=cow+1
                count[l] =count[l]-1
                
        return "{}A{}B".format(bull,cow)