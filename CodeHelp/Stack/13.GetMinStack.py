'''
https://www.codingninjas.com/codestudio/problems/design-a-stack-that-supports-getmin-in-o-1-time-and-o-1-extra-space_842465?leftPanelTab=1
'''
'''
    Time complexity: O(1)
        For push(): O(1) - Constant extra space is required.
        For pop(): O(1) - Constant extra space is required.
        For top(): O(1) - Constant extra space is required.
        For getMin(): O(1) - Constant extra space is required.
        For isEmpty(): O(1) - Constant extra space is required.

    Space complexity: O(1)
'''

class SpecialStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, data):
        if (len(self.s2) == 0 or data <= self.s2[-1]):
            self.s2.append(data)
        self.s1.append(data)

    def pop(self):
        if (self.isEmpty()):
            return -1
        if (self.s1[-1] == (self.s2[-1])):
            self.s2.pop()
        x = self.s1[-1]
        self.s1.pop()
        return x

    def top(self):
        if (self.isEmpty()):
            return -1
        return self.s1[-1]

    def isEmpty(self):
        return len(self.s1) == 0

    def getMin(self):
        if (self.isEmpty()):
            return -1
        else:
            return self.s2[-1]
