#https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map={}
        for i,n in enumerate(nums):
            if n in map and abs(i-map[n]) <= k:
                return True
            else:
                map[n]=i
        return False
        