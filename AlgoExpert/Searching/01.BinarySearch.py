'''
https://www.algoexpert.io/questions/Binary%20Search
'''
# Time O(nlogn) | space O(nlogn)
def binarySearch(array, target):
    # Write your code here.
	return binarySearchHelper(array,target,0,len(array)-1)

def binarySearchHelper(array,target,left,right):
	if left > right:
		return -1
	mid=(left+right)//2
	potentialMatch=array[mid]
	if target == potentialMatch:
		return mid
	elif target < potentialMatch:
		return binarySearchHelper(array,target,left,mid-1)
	else:
		return binarySearchHelper(array,target,mid+1,right)
