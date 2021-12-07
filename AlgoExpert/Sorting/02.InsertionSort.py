
'''
https://www.algoexpert.io/questions/Insertion%20Sort
'''
#Time O(n^2) | space O(1)
def insertionSort(array):
    # Write your code here.
    for i in range(1,len(array)):
		j=i #compare current with prev
		while j > 0 and array[j] < array[j-1]:
			swap(j,j-1,array)
			j=j-1
	return array

def swap(i,j,array):
	array[i],array[j]=array[j],array[i]