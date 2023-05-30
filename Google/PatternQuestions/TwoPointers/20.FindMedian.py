'''https://leetcode.com/problems/find-median-from-data-stream/'''

import bisect
class MedianFinder:

    def __init__(self):
        self.arr=[]
        self.left=-1
        self.right=-1

    def addNum(self, num: int) -> None:
        if len(self.arr) == 0:
            self.arr.append(num)
            self.left=self.left+1
            self.right=self.right+1
            return
        i= bisect.bisect_left(self.arr,num)
        self.arr.insert(i,num)
        if len(self.arr)% 2 == 0:
            self.right=self.right+1
        else:
            self.left=self.left+1
        

    def findMedian(self) -> float:
        if len(self.arr) == 0:
            raise Exception('An array is empty, no median exists')
        if self.left == self.right:
            return self.arr[self.left]
        return (self.arr[self.left] +self.arr[self.right] )/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()