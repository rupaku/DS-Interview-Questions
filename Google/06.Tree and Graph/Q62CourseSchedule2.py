'''
https://leetcode.com/problems/course-schedule-ii/submissions/
'''
class Solution:
    WHITE =1
    GREY=2
    BLACK=3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list= defaultdict(list)
        
        for dest,src in prerequisites:
            adj_list[src].append(dest)

        print(adj_list)
        # defaultdict(<class 'list'>, {0: [1]})  
         
        topo_sorted_order =[]
        is_possible=True
        
        # by default: white
        color= {k: Solution.WHITE for k in range(numCourses)}
        
        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            
            color[node]=Solution.GREY
            
            if node in adj_list:
                for neighbour in adj_list[node]:
                    if color[neighbour] == Solution.WHITE:
                        dfs(neighbour)
                    elif color[neighbour] == Solution.GREY:
                        is_possible = False
                        
            color[node] = Solution.BLACK
            topo_sorted_order.append(node)
            print(topo_sorted_order)
            # [1]
            # [1, 0]
            
            
        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
                
        return topo_sorted_order[::-1] if is_possible else []
        
        