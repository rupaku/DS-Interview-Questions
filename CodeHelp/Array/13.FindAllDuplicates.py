'''
https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        uniques = set()
        
        for num in nums:
            if num in uniques:
                dups.append(num)
            else:
                uniques.add(num)
        return dups
        