'''
'''
def find_duplicate(arr):
    ans=0
     #XOR ing all array elements
    for i in range(len(arr)):
        ans=ans^ arr[i]
     #XOR ing [1,n-1] array elements
    for i in range(1,len(arr)-1):
        ans=ans^i
    return ans

if __name__ == '__main__':
    print(find_duplicate([1,3,3,6,4]))