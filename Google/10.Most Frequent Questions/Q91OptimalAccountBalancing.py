'''
https://leetcode.com/problems/optimal-account-balancing/
https://www.youtube.com/watch?v=B8pPWgLa2lQ
'''
from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debts=defaultdict(int)
        for f,t,amount in transactions:
            debts[f] -= amount
            debts[t] += amount
        
        debts_list = [debts[id] for id in debts if debts[id]]
        n=len(debts_list)
        
        def backtrack(index):
            while index < n and debts[index] == 0:
                index += 1
            if index == n:
                return 0
            
            ans=999999
            
            for i in range(index+1,n):
                if debts_list[index] * debts_list[i] < 0:
                    debts_list[i] += debts_list[index]
                    ans=min(ans,backtrack(index+1) +1)
                    debts_list[i] -= debts_list[index]
                    
            return ans
        
        return backtrack(0)
        