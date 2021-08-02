'''
https://leetcode.com/problems/split-array-largest-sum/submissions/
#Binary search
 you can basically make a guess for the largest number. For each guess you can check if its possible. 
 If it is possible, meaning that you are able to split with less than m num, then you should decrease your right pointer. 
 If it's not possible then that means your guess is too small and you need to increase your right pointer.
'''

class Solution(object):
    def splitArray(self, nums, m):
        def is_possible(arr, guess, count):
            cnt = 1
            running_sum = 0
            for num in arr:
                if running_sum + num > guess:
                    cnt += 1
                    if cnt > count:
                        return False
                    running_sum = num
                else:
                    running_sum += num
            return True

        l = 0
        r = 0
        for num in nums:
            r += num
            l = max(l, num)
        while l < r:
            guess = l + (r-l)//2
            if is_possible(nums, guess, m):
                r = guess
            else:
                l = guess+1
        return l
# class Solution(object):
#     def splitArray(self, nums, m):
#         if not nums or not m or len(nums) < m:
#             return
        
#         n = len(nums)
#         presum = [0] * (n + 1)
#         for i in range(n):
#             presum[i + 1] = presum[i] + nums[i]
        
#         f = [float("inf")] * (n + 1)
#         f[0] = 0
        
#         for j in range(m):
#             for i in range(n, 0, -1): # must be from n to 1, otherwise results will be wrong
#                 for k in range(j - 1, i):
#                     f[i] = min(f[i], max(f[k], presum[i] - presum[k]))
        
#         return f[n]