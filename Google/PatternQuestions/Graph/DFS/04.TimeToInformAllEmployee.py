'''https://leetcode.com/problems/time-needed-to-inform-all-employees/submissions/964908933/'''
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node,curr_time):
            nonlocal ans
            if node not in graph:
                ans=max(ans,curr_time)
            for child in graph[node]:
                dfs(child,curr_time+informTime[node])
                
        graph=defaultdict(list)
        for c,m in enumerate(manager):
            graph[m].append(c)
            
        ans=0
        dfs(headID,0)
        return ans