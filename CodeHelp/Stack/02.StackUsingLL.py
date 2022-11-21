'''
https://www.codingninjas.com/codestudio/problems/implement-stack-with-linked-list_630475?leftPanelTab=1
'''
from sys import stdin

#Following is the Node class already written for the Linked List

class Node :
    def __init__(self) :
        self.data = -1
        self.next = None

# Stack Class 
class Stack :
    def __init__(self) :
        self.newNode = Node()
        self.size = 0
        return 
    
    def getSize(self) :
        return self.size

    def isEmpty(self) :

        if(self.size == 0) :
            return True

        else :
            return False

    def push(self, data) :

        newHead = Stack()
        newHead.newNode.data = data
        newHead.newNode.next = self

        # To update the size of the stack
        newHead.size = self.size + 1
        return newHead

    def pop(self) :
        # if stack is already empty
        if(self.newNode.next == None) :
            return self
        
        else :
            return self.newNode.next

    def top(self) :
        return self.newNode.data

#main

t = int(input())
head = Stack()

while t > 0 : 

    query = list(map(int,stdin.readline().strip().split(" ")))
    if query[0] == 1 :
        print(head.getSize()) 
    
    elif query[0] == 2 :

        if(head.isEmpty()) :
            print("true")
        
        else :
            print("false")
    
    elif query[0] == 3 :
        head = head.push(query[1])

    elif query[0] == 4:
        head = head.pop()

    else :
        if(head == None) :
            print(-1)
        
        else :
            top = head.top()
            print(top)
    t -= 1
