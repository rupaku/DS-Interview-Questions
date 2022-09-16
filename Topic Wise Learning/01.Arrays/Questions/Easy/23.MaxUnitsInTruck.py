'''
https://leetcode.com/problems/maximum-units-on-a-truck/submissions/

time  : nlogn
space :O(1)
'''

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        '''
        boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
        sorted 2nd index [[5, 10], [3, 9], [4, 7], [2, 5]]

        '''
        
        boxTypes.sort(key=lambda x: -x[1]) # sort x[1] for 2nd time, - for descending
        print(boxTypes)
        cur_size = 0
        max_units = 0
        for num_box, unit in boxTypes:
            max_units += unit * min(truckSize- cur_size, num_box)
            cur_size += min(truckSize- cur_size, num_box)
        return max_units