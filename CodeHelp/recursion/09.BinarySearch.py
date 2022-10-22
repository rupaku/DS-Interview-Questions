'''
'''
def binary_search_recursion(arr,l,r,key):
    if r < l:
        return False
    mid = l+(r-l)//2
    if arr[mid] == key:
        return True  
    if arr[mid] > key:
        return binary_search_recursion(arr,l,mid-1,key)
    else:
        return binary_search_recursion(arr,mid+1,r,key)

arr=[1,2,3,4,5]
n=4
key=4
print(binary_search_recursion(arr,0,len(arr)-1,key))