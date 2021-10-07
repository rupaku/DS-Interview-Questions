'''
https://www.algoexpert.io/questions/Selection%20Sort
'''
# Time O(n^2) | space O(1)
def selectionSort(array):
    # Write your code here.
    currIdx=0
	while currIdx < len(array)-1:
		smallestIdx=currIdx
        #start with 2nd element
		for i in range(currIdx+1,len(array)):
			if array[smallestIdx] > array[i]:
				smallestIdx =i
		swap(currIdx,smallestIdx,array)
		currIdx =currIdx+1
	return array

def swap(i,j,array):
	array[i],array[j]=array[j],array[i]