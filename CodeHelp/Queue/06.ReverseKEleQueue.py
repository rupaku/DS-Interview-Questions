'''
https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1
'''
#Function to reverse first k elements of a queue.
def modifyQueue(q,k):
    
    #using a stack and another queue to reverse first k elements.
    stack= []
    ansqueue = []

    #we pop first k elements from queue and push it in the stack.
    for i in range(k):
        stack.append(q.pop(0))

    #while stack is not empty, we push the elements into the new queue.
    while len(stack):
        ansqueue.insert(0,stack.pop(0))

    #then we add rest of the elements of original queue to the new queue.
    while len(q):
        ansqueue.append(q.pop(0))

    #returning the new queue.
    return ansqueue