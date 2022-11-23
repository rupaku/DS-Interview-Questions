'''
https://www.codingninjas.com/codestudio/problems/two-stacks_983634?leftPanelTab=1
'''
'''
    Time Complexity: O(1)
    Space Complexity: O(N)

    Where N is the size of the stack given by user.
'''


class TwoStack:
    def __init__(self, s):
        self.size = s
        self.arr = [0] * self.size
        self.top1 = -1
        self.top2 = self.size

    # Push function for the first stack
    def push1(self, val):
        # If overflow exists, return
        if self.top1 + 1 == self.top2:
            return
        self.top1 += 1
        self.arr[self.top1] = val

    # Push function for the second stack
    def push2(self, val):
        # If overflow exists, return
        if self.top2 - 1 == self.top1:
            return
        self.top2 -= 1
        self.arr[self.top2] = val

    # Pop function for the first stack
    def pop1(self):
        # If underflow exists, return -1
        if self.top1 == -1:
            return -1

        self.top1 -= 1
        return self.arr[self.top1 + 1]

    # Pop function for the second stack
    def pop2(self):
        # If underflow exists, return -1
        if self.top2 == self.size:
            return -1

        self.top2 += 1
        return self.arr[self.top2 - 1]
