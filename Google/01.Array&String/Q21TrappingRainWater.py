'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/341/
https://www.youtube.com/watch?v=C8UjlJZsHBw
At one block -> min(max-left,max-right)- current height , repeat and get sum of all block result
min(leftmax,rightmax) -current block
'''

class Solution:
    #Two pointer
    def trap(self, height: List[int]) -> int:
        #Two pointer
        areas = 0
        max_l = max_r = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]:
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    areas += max_l - height[l]
                l +=1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    areas += max_r - height[r] 
                r -=1
        return areas