'''
selection sorting : at each index, find minimum element and keep it to correct place aand swap it with i
'''

def selection(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
    return arr

if __name__ == "__main__":
    print(selection([4,3,5,1,8]))