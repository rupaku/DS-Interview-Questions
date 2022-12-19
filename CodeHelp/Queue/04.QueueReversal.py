'''
https://practice.geeksforgeeks.org/problems/queue-reversal/1?page=1&category[]=Queue&sortBy=submissions
'''
#Function to reverse the queue.
def rev(q):
    #using a stack to reverse the queue.
    stack=[]
    
    #pushing elements from queue into stack and removing them from queue.
    while(q.qsize()!=0):
        x=q.get()
        stack.append(x)
        
        
    #now pushing elements back into the queue from stack and removing them 
    #from stack. queue gets reversed as stack follows last in first out.
    while(len(stack)!=0):
        x=stack.pop()
        q.put(x)
        
    #returning reversed queue.
    return q