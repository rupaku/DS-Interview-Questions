'''
'''

# def sum_of_array(arr,n):
#     if n <= 0:
#         return 0
#     return sum_of_array(arr,n-1)+arr[n-1]
def sum_of_array(*arr,n):
    if n==0:
        return 0
    if n==1:
        return arr[0]
    rem_part=sum_of_array(arr+1,n-1)
    sum=arr[0]+rem_part
    return sum


n=4
print(sum_of_array([1,2,3,4],n))