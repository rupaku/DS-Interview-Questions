'''
https://www.algoexpert.io/questions/Three%20Number%20Sum
'''
# Time O(n^2) | space O(n)
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
	triplets = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentSum = array[i] +array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i],array[left],array[right]])
				left =left +1
				right=right-1
			elif currentSum < targetSum:
				left =left +1
			elif currentSum > targetSum:
				right=right-1
	return triplets
				
'''
Test cases
'''
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
