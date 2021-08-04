'''
https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/331/
https://www.youtube.com/watch?v=paePJDgZaR4
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        n=len(equations)
        for i in range(n):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1/values[i]
            
        print(graph)
        # defaultdict(<class 'dict'>, {'a': {'b': 2.0}, 'b': {'a': 0.5, 'c': 3.0}, 'c': {'b':           0.3333333333333333}})
        
        def dfs(x,y,visited):
            if x not in graph or y not in graph:
                return -1
            if y in graph[x]:
                return graph[x][y]
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp=dfs(i,y,visited)   
                    if temp == -1:
                        continue
                    else:
                        return temp * graph[x][i]
            return -1
        
        output=[]
        for p,q in queries:
            output.append(dfs(p,q,set()))
        return output
