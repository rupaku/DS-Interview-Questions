# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items=[]
        self.min=[]
        

    def push(self, x: int) -> None:
        self.items.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)
            
        

    def pop(self) -> None:
        if len(self.items) == 0:
            return None
        else:
            if self.items[-1] == self.min[-1]:
                self.min.pop()
            return self.items.pop()
                   

    def top(self) -> int:
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]
        

    def getMin(self) -> int:
        if len(self.items) == 0:
            return None
        else:
            return self.min[-1]
        
       
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()