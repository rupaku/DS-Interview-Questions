
def min_index(arr,i,j):
    if i == j:
        return i
    
    k=min_index(arr,i+1,j)

    return (i if arr[i] < arr[k] else k)

def selection_recursive(arr,n,index=0):
    if index == n:
        return -1

    k = min_index(arr,index,n-1)

    if k != index:
        arr[k],arr[index]=arr[index],arr[k]

    selection_recursive(arr, n, index+1)

arr = [3, 1, 5, 2, 7, 0]
n = len(arr)
 
# Calling function
selection_recursive(arr, n)
 
# printing sorted array
for i in arr:
    print(i, end = ' ')