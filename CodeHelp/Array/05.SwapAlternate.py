'''
'''
def swap_alternate(arr):
    size=len(arr) -1
    i=0
    while i < size:
        if i+1 < size:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        i=i+2
    return arr

if __name__ == '__main__':
    print(swap_alternate([1,2,3,4]))