'''
'''


def reverse(arr):
    start=0
    end=len(arr)-1
    while start <= end:
       arr[start],arr[end] = arr[end], arr[start]
       start=start+1
       end=end-1
    return arr

if __name__ == '__main__':
    print(reverse([2,3,4]))