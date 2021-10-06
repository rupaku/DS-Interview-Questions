'''
https://www.algoexpert.io/questions/Monotonic%20Array
'''
# Time O(n) | space O(1)
def isMonotonic(array):
    # Write your code here.
	if len(array) <= 2:
		return True
	direction=array[1]-array[0]
	for i in range(2,len(array)):
		if direction == 0:
			direction =array[i] - array[i-1]
			continue
		if breaksDirection(direction,array[i-1],array[i]):
			return False
	return True

def breaksDirection(direction,prevInt,currInt):
	diff = currInt - prevInt
	if direction > 0:
		return diff < 0
	return diff > 0
    


# Time O(n) | space O(1)
def isMonotonic(array):
    # Write your code here.
    isNonDecreasing=True
	isNonIncreasing=True
	for i in range(1,len(array)):
		if array[i] < array[i-1]:
			isNonDecreasing = False
		if array[i] > array[i-1]:
			isNonIncreasing = False
	return isNonDecreasing or isNonIncreasing
