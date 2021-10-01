'''
https://www.algoexpert.io/questions/Sorted%20Squared%20Array
'''
# Time O(nlogn) | space O(n)
def sortedSquaredArray(array):
    # Write your code here.
	ls=[]
	for value in array:
		ls.append(value*value)
		ls.sort()
    return ls


# Using two pointer
# Time O(n) | space O(n)
def sortedSquaredArray(array):
    # Write your code here.
	sortedSq=[0 for _ in array]
	smallervalueInx=0
	largervalueIdx=len(array)-1
	
	for idx in reversed(range(len(array))):
		smallervalue=array[smallervalueInx]
		largervalue=array[largervalueIdx]
		if abs(smallervalue) > abs(largervalue):
			sortedSq[idx]= smallervalue * smallervalue
			smallervalueInx = smallervalueInx + 1
		else:
			sortedSq[idx]= largervalue * largervalue
			largervalueIdx = largervalueIdx - 1
    return sortedSq


'''
Test case
'''
import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = program.sortedSquaredArray(input)
        self.assertEqual(actual, expected)