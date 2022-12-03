'''
'''


class Stack(object):
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit
    def is_empty(self):
        return len(self.stack) <= 0
    def push(self,item):
        if len(self.stack) >= self.limit:
            print("stackoverflow")
        else:
            self.stack.append(item)
    def pop(self):
        if len(self.stack) <= 0:
            print("stack underflow")
            return 0
        else:
            return self.stack.pop()
    def peek(self):
        if len(self.stack) <= 0:
            print("stack underflow")
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
def is_pallindrome(str):
    strStack=Stack()
    pallin=False
    for char in str:
        strStack.push(char)
    for char in str:
        if char == strStack.pop():
            pallin = True
        else:
            pallin=False
    return pallin
print(is_pallindrome("smadams"))