'''
algoexpert.io/questions/Cycle%20In%20Graph
'''
# O(V+E) | O(V) space
def cycleInGraph(edges):
    # Write your code here.
    num_of_nodes = len(edges)
	visited = [False for _ in range(num_of_nodes)]
	currently_in_stack = [False for _ in range(num_of_nodes)]
	for node in range(num_of_nodes):
		if visited[node]:
			continue
		containsCycle = isNodeInCycle(edges, node, visited,currently_in_stack)
		if containsCycle:
			return True
	return False

def isNodeInCycle(edges,node, visited,currently_in_stack):
	visited[node]= True
	currently_in_stack[node] = True
	
	neighbors = edges[node]
	for neighbor in neighbors:
		if not visited[neighbor]:
			containsCycle = isNodeInCycle(edges,neighbor,visited,currently_in_stack)
			if containsCycle:
				return True
		elif currently_in_stack[neighbor]:
			return True
	currently_in_stack[node] = False
	return False
