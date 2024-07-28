# https://leetcode.com/problems/random-pick-with-weight/description/

import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sm_list=[]
        prefix_sm =0
        for weight in w:
            prefix_sm= prefix_sm+weight
            self.prefix_sm_list.append(prefix_sm)
        self.total_sm= prefix_sm
        

    def pickIndex(self) -> int:
        target = self.total_sm * random.random()
        l=0
        r=len(self.prefix_sm_list)
        while l < r:
            mid= l+(r-l)//2
            if target > self.prefix_sm_list[mid]:
                l=mid+1
            else:
                r=mid
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()