# https://leetcode.com/problems/graph-valid-tree/

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1: return False
        
        # Create an adjacency list.
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        
        # We still need a seen set to prevent our code from infinite
        # looping if there *is* cycles (and on the trivial cycles!)
        seen = set()

        def dfs(node):
            if node in seen: return
            seen.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour)

        dfs(0)
        return len(seen) == n

#BFS 2nd method

def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
    if len(edges) != n - 1: return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = {0}
    queue = collections.deque([0])
    
    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            queue.append(neighbour)
    
    return len(seen) == n