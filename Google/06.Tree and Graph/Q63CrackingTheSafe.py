'''
https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/3075/
'''

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(curr,counted,total):
            print(curr,counted,total) #0 {'0'} 2  #01 {'0', '1'} 2

            if len(counted) == total:
                return curr
            for i in range(k):
                temp = curr[-(n-1):]+str(i) if n != 1 else str(i)
                print('temp',temp) # 0 #1

                if temp not in counted:
                    counted.add(temp)
                    res=dfs(curr+str(i),counted,total)
                    print('res',res) #01
                    
                    if res:
                        return res
                    counted.remove(temp)
        return dfs("0"*n,set(["0"*n]),k**n)