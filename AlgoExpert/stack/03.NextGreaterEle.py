'''
https://www.algoexpert.io/questions/Next%20Greater%20Element
'''
# O(n) time | O(n) space
def nextGreaterElement(array):
    # Write your code here.
    res= [-1]*len(array)
	stack=[]
	for i in range(2*len(array)-1,-1,-1):
		cirIdx = i % len(array)
		while len(stack) > 0:
			if stack[len(stack) - 1] <= array[cirIdx]:
				stack.pop()
			else:
				res[cirIdx]=stack[len(stack)-1]
				break
		stack.append(array[cirIdx])
	return res
