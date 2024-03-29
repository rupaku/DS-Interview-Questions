'''https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/submissions/964889635/'''
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i,j in stones:
            graph[i].append((i,j))
            graph[~j].append((i,j))
            
        visited=set()
        groups=0
        
        for i,j in stones:
            if (i,j) not in visited:
                groups=groups +1
                stack=[(i,j)]
                visited.add((i,j))
                
                while stack:
                    curr_i,curr_j =stack.pop()
                    
                    for new_i,new_j in graph[curr_i]:
                        if (new_i,new_j) not in visited:
                            stack.append((new_i,new_j))
                            visited.add((new_i,new_j))
                            
                    
                    for new_i,new_j in graph[~curr_j]:
                        if (new_i,new_j) not in visited:
                            stack.append((new_i,new_j))
                            visited.add((new_i,new_j))
                            
        return len(stones) - groups
