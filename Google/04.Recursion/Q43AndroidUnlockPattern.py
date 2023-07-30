'''
https://leetcode.com/explore/interview/card/google/62/recursion-4/484/
create skip dictionary
used as visited False
apply dfs-> index i mark used as True, find count -> over 1 to 10 num check if its False and not in skip or used[skip] -> sum of this
mark used index as False again and return count

out of DFS loop return sum of dfs(1,k) * 4 -> since starting with 1,3,7,9 symmetric.
dfs(2,k)*4 -> starting2,4,6,8 symmetric
dfs(5,k) -> center over loop m-1 to n

corner,mid ,center

'''
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:

        cross = collections.Counter({(1,3):2,(3,1):2,(1,7):4,(7,1):4,(3,9):6,(9,3):6,(7,9):8,(9,7):8,(1,9):5,(9,1):5,(2,8):5,(8,2):5,(3,7):5,(7,3):5,(4,6):5,(6,4):5})                                      
        used = [False]*10
        def dfs(i, k):
            print(i,k)
            # 1 0
            # 2 0
            # 5 0
            
            if not k: return 1
            used[i] = True
            cnt = sum(dfs(j, k-1) for j in range(1,10) if not used[j] and (not cross[i,j] or used[cross[i,j]]))
            used[i] = False
            return cnt
        return sum(dfs(1,k)*4 + dfs(2,k)*4 + dfs(5,k) for k in range(m-1, n))
        
        




        