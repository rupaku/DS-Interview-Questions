''''''

def sort_array(arr,n):
    if n == 0 or n == 1:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1]= arr[i+1],arr[i]

    sort_array(arr,n-1)

arr=[1,4,2,6]
print(sort_array(arr,len(arr)-1))