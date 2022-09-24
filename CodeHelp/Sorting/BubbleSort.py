'''
'''
def bubble(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

if __name__ == "__main__":
    print(bubble([4,3,5,1,8]))