'''
https://www.algoexpert.io/questions/Array%20Of%20Products
'''
# time O(n) | space O(n)
def arrayOfProducts(array):
    # Write your code here.
    products = [1 for _ in range(len(array))]
	
	leftRunningProduct = 1
	for i in range(len(array)):
		products[i] = leftRunningProduct
		leftRunningProduct *= array[i]
		
	rightRunningProduct = 1
	for i in reversed(range(len(array))):
		products[i] *= rightRunningProduct
		rightRunningProduct *= array[i]
	
	return products
