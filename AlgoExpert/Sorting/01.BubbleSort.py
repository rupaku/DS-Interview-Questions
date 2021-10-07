'''
https://www.algoexpert.io/questions/Bubble%20Sort
'''
# Time O(n^2) | space O(1)
def bubbleSort(array):
    # Write your code here.
    isSorted=False
	counter=0 # for loop will go one position less than current
	while not isSorted:
		isSorted=True
		for i in range(len(array)-1-counter):
            #compare current with next
			if array[i] > array[i+1]:
				swap(i,i+1,array)
				isSorted=False
		counter=counter+1
	return array

def swap(i,j,array):
	array[i],array[j]=array[j],array[i]