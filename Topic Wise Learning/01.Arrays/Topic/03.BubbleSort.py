'''
https://www.geeksforgeeks.org/recursive-bubble-sort/
'''

def bubble_recursive(arr,n):
    if n == 1:
        return
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1]= arr[i+1],arr[i]

    bubble_recursive(arr,n-1)

arr=[64, 34, 25, 12, 22, 11, 90]
n=len(arr)
bubble_recursive(arr,n)
print(arr)
