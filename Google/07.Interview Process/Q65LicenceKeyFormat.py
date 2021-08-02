'''
https://leetcode.com/explore/interview/card/google/67/sql-2/472/
https://www.youtube.com/watch?v=GaMTTfZDcdo

convert string without hyphen, read from reverse till k, then append hyphen, avoid i=0 hyphen, and append to result with reverse
'''
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count=0
        st=s.replace('-','')
        ans=[]
        #from reverse
        for i in range(len(st)-1,-1,-1):
            ans.append(st[i].upper())
            count=count+1
            
            if count == k and i != 0:
                ans.append('-')
                count=0
                
        return ''.join(ans[::-1])
            
            
        