'''
https://leetcode.com/problems/find-pivot-index/submissions/
'''

def pivot_index(self,nums):
    S=sum(nums)
    left_sm=0
    for i,x in enumerate(nums):
        if left_sm == (S-left_sm-x):
            return i

        left_sm =left_sm +x
    return -1