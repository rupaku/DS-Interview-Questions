'''
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/submissions/
'''
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def num_ones(val):
            count=0
            while val > 0:
                val,digit = divmod(val,2)
                if digit == 1:
                    count=count+1
            return count
        
        # Create a list of tuples of (num_ones, val)
        ints = [(num_ones(val),val) for val in arr]
        
        # Sort the list of tuples first by num_ones, then by val
        ints.sort()
        
        # Create a list of the values in the sorted list
        results = [val for num_ones, val in ints]

        return results
