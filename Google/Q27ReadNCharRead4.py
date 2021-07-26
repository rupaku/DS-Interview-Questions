'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/436/
'''
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4=['']*4
        self.start=0
        self.m =0
        
    def read(self, buf: List[str], n: int) -> int:
        count=0
        for i in range(n):
            if self.start == 0:
                self.m = read4(self.buf4)

            if self.m == 0:
                break
            buf[i] =self.buf4[self.start]
            count = count +1
            self.start = (self.start +1)%self.m
        return count.
    
    

        