'''
https://www.algoexpert.io/questions/Powerset
'''
# O(n*2^n) | O(n*2^n)
def powerset(array):
    # Write your code here.
    subsets = [[]]
	for ele in array:
		for i in range(len(subsets)):
			currentSubsets = subsets[i]
			subsets.append(currentSubsets + [ele])
	return subsets
