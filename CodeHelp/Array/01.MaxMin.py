'''
'''
def max(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max=arr[i]
    return max
def min(arr):
    min=arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min=arr[i]
    return min
if __name__ == '__main__':
    print(max([1,2,3,4]))
    print(min([1,2,3,4]))