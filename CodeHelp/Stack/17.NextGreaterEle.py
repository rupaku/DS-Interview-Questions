'''
https://www.codingninjas.com/codestudio/problems/next-greater-element_799354?leftPanelTab=2
'''
''''
    Time Complexity : O(N)
    Space Complexity : O(N)
    
    Where N is the length of the array.
'''


from sys import stdin

def nextGreater(arr,n):
    
    ans = [0] * n
    
    s = []
    
    for i in range(n-1,-1,-1):
        
        # We will pop the elements from the stack till we get the greater element 
        # Or stack become empty
        while(len(s)>0 and s[len(s)-1] <= arr[i]):
            s.pop()
            
        if len(s) == 0:
            ans[i] = -1
            
        else:
            ans[i] = s[len(s)-1]
            
        s.append(arr[i])
        
        
    return ans 

#Main

t = int(stdin.readline().rstrip())

while t>0:
    
    n=int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    z = nextGreater(arr,n)
    print(*z)    
    t -= 1
