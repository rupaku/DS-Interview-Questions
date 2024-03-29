'''
https://leetcode.com/problems/moving-average-from-data-stream/submissions/
time  O(1)
space O(n)
'''
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue =deque()
        self.window_sum =0
        self.count= 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum - tail + val
        return self.window_sum/ min(self.size,self.count)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)