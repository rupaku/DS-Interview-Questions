'''
https://www.algoexpert.io/questions/Two%20Number%20Sum
'''

# Using two for loop
# time O(n^2) | space O(1)
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)-1):
		first_num=array[i]
		for j in range(i+1,len(array)):
			sec_num=array[j]
			if first_num + sec_num == targetSum:
				return [first_num,sec_num]
	return []


# Using Hash Map
# Time O(n) | space O(n)
# x+y=sum => y= sum -x
def twoNumberSum(array, targetSum):
    # Write your code here.
    nums={}
	for num in array:
		y=targetSum - num
		if y in nums:
			return [y, num]
		else:
			nums[num] = True
	return []


#Using Two pointers
# Time O(nlogn) | space O(1)
def twoNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	left=0
	right=len(array)-1
	while left < right:
		currSum = array[left] + array[right]
		if currSum == targetSum:
			return [array[left], array[right]]
		elif currSum < targetSum:
			left = left+1
		elif currSum > targetSum:
			right = right-1
	return []


'''
Test cases
'''

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)