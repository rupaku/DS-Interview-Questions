# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2

            # Case 1: find target
            if nums[mid] == target:
                return True #

            #extra condition
            if nums[mid] == nums[left]:
                left=left+1
                continue

            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            # Case 3: subarray on mid's right is sorted.
            else:
                if nums[right] >= target and nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False #
        