'''

 move current time by one minute and check whether all the digits are reused; repeat this process until we encounter one.
'''
class Solution:
    def nextClosestTime(self, time: str) -> str:
        hh = int(time[0:2])
        mm = int(time[3:5])
        # get current digits
        digits = set()
        for d in time:
            if d != ':':
                digits.add(ord(d) - ord('0'))
        # try possible closest time one by one
        for _ in range(1440):
            hh, mm = self.addOne(hh, mm)
            # whether all the digits are reused
            if self.areDigitsIn(digits, hh, mm):
                return '{0:0>2}:{1:0>2}'.format(hh, mm)
        return time
        
    def addOne(self, hh, mm):
        # add one minite to current time
        mm += 1
        if mm == 60:
            hh += 1
            mm = 0
        if hh == 24:
            hh = 0
        return hh, mm
    
    def areDigitsIn(self, digits, hh, mm):
        # whether the digits in time hh:mm are all in given digits
        h1, h2 = hh // 10, hh % 10
        m1, m2 = mm // 10, mm % 10
        return h1 in digits and h2 in digits and m1 in digits and m2 in digits
        