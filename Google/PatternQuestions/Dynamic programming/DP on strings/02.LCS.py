'''https://leetcode.com/problems/longest-common-subsequence/editorial/?envType=list&envId=55afh7m7'''
class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        if len(t2) < len(t1):
            t1,t2=t2,t1

        prev=[0]*(len(t1)+1)
        curr=[0]*(len(t1)+1)

        for i in reversed(range(len(t2))):
            for j in reversed(range(len(t1))):
                if t2[i] == t1[j]:
                    curr[j]=1+prev[j+1]
                else:
                    cur[j]=max(prev[j],curr[j+1])
            prev,curr=curr,prev
        return prev[0]