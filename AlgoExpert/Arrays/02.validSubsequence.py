'''
https://www.algoexpert.io/questions/Validate%20Subsequence
'''
# Time O(n) | Space O(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIndex=0
	for value in array:
		if seqIndex == len(sequence):
			break
		if sequence[seqIndex] == value:
			seqIndex =seqIndex +1
	return seqIndex == len(sequence)


'''
Test case
'''

# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(program.isValidSubsequence(array, sequence))
