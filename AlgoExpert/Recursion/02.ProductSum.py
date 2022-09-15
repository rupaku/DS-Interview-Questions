'''
https://www.algoexpert.io/questions/Product%20Sum
'''
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
#O(n) | O(d)
def productSum(array,multiplier=1):
    # Write your code here.
    sum=0
	for element in array:
		if type(element) is list:
			sum += productSum(element, multiplier+1)
		else:
			sum += element
	return sum * multiplier
