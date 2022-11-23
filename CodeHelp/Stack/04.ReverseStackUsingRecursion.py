'''
https://www.codingninjas.com/codestudio/problems/reverse-stack-using-recursion_631875?leftPanelTab=1

pop top element, reverse all element in stack, do insert at bottom for popped element.
'''
'''
	Time complexity : O(N^2)
	Space complexity : O(N)
	where N is the size of input stack
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def insertAtBottom(stack, val) :

	if(len(stack) == 0) :

		stack.append(val)
		
	else :

		top = stack.pop()
		insertAtBottom(stack, val) 
		stack.append(top)

	
def reverseStack(stack) :
	
	if(len(stack) > 0) :

		top = stack.pop()
		reverseStack(stack)
		insertAtBottom(stack, top)


# taking input
def takeInput() :

	n = int(input().strip())
	if(n == 0) :
		 return list(), n

	stack = list(map(int,stdin.readline().strip().split(" ")))
	return stack, n


def printStack(stack) :

	while(len(stack) > 0) :

		print(stack.pop(),end = " ")


# main
stack, n = takeInput()
reverseStack(stack)
printStack(stack)