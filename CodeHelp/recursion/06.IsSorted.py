'''
'''

def is_sorted(arr,n):
    if n == 0 or n ==1:
        return True
    if arr[0] > arr[1]:
        return False
    else:
        rem_part=is_sorted(arr+1,n-1)
        return rem_part

if '__name__' == "__main__":
    arr=[2,4,6,8,9]
    n=5
    ans=is_sorted(arr,n)
    if(ans):
        print("array is sorted")
    else:
        print("array is not sorted")