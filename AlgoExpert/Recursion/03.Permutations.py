'''
https://www.algoexpert.io/questions/Permutations
'''
#O(n*n!) |O(n*n!)
def getPermutations(array):
    # Write your code here.
    permutations = []
	permutation_helper(0,array,permutations)
	return permutations

def permutation_helper(i,array,permutations):
	if i == len(array)-1:
		permutations.append(array[:])
	else:
		for j in range(i,len(array)):
			swap(array,i,j)
			permutation_helper(i+1,array,permutations)
			swap(array,i,j)
def swap(array,i,j):
	array[i],array[j]= array[j],array[i]
