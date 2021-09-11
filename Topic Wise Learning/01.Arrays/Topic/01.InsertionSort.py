'''
https://www.geeksforgeeks.org/recursive-insertion-sort/
'''
def insertion_recursive(arr,n):
    if n<=1:
        return

    #sort first n-1 element
    insertion_recursive(arr,n-1)
    last=arr[n-1]
    j=n-2

    while j >= 0 and arr[j] > last:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1] =last

def print_array(arr,n):
    for i in range(n):
        print(arr[i])

arr=[12,11,13,5,6]
n=len(arr)

insertion_recursive(arr,n)
print_array(arr,n)
