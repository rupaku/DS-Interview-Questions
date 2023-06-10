'''https://leetcode.com/problems/sliding-window-maximum/submissions/964163595/'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[0]*(n-k+1)
        dq=deque()
        ri=0
        for i in range(n):
            # remove indexes of elements not from sliding window
            if dq and dq[0] == i-k:
                dq.popleft()
            # remove from deq indexes of all elements 
            # which are smaller than current element nums[i]
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                res[ri]=nums[dq[0]]
                ri=ri+1
        return res