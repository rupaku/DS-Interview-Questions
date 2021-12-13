'''
https://www.algoexpert.io/questions/Same%20BSTs
'''
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    return areSameBST(arrayOne,arrayTwo,0,0,float("-inf"),float("inf"))

def areSameBST(arr1,arr2,rix1,rix2,minValue,maxValue):
	if rix1 == -1 or rix2 == -1:
		return rix1 == rix2
	if arr1[rix1] != arr2[rix2]:
		return False
	left_rix1 = get_index_of_first_smaller(arr1,rix1,minValue)
	left_rix2 = get_index_of_first_smaller(arr2, rix2, minValue)
	right_idx1 = get_index_of_first_bigger_equal(arr1,rix1,maxValue)
	right_idx2 = get_index_of_first_bigger_equal(arr2,rix2,maxValue)
	
	curr_value = arr1[rix1]
	left_are_same = areSameBST(arr1,arr2,left_rix1,left_rix2,minValue,curr_value)
	right_are_same = areSameBST(arr1,arr2,right_idx1,right_idx2,curr_value, maxValue)
	return left_are_same and right_are_same

def get_index_of_first_smaller(arr,start_idx,minValue):
	for i in range(start_idx + 1,len(arr)):
		if arr[i] < arr[start_idx] and arr[i] >= minValue:
			return i
	return -1

def get_index_of_first_bigger_equal(arr,start_idx,maxValue):
	for i in range(start_idx+1,len(arr)):
		if arr[i] >= arr[start_idx] and arr[i] < maxValue:
			return i
	return -1