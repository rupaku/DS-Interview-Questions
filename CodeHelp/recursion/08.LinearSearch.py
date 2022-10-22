'''
'''
def linear_search_recursion(arr,l,r,key):
    if r < l:
        return -1
    if arr[l] == key:
        return l
    if arr[r] == key:
        return r    
    else:
        rem_part=linear_search_recursion(arr,l+1,r-1,key)
        return rem_part

arr=[1,2,3,4]
n=4
key=3
print(linear_search_recursion(arr,0,len(arr)-1,key))
