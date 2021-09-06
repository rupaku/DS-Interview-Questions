'''
https://www.geeksforgeeks.org/counting-sort/
'''

def count_sort(arr):
    max_ele= int(max(arr))
    min_ele= int(min(arr))
    range_of_elements= max_ele-min_ele+1

    count_arr= [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    # Store count of each character
    for i in range(0,len(arr)):
        count_arr[arr[i]- min_ele] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array

    for i in range(1,len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # Build the output character array
    for i in range(len(arr)-1,-1,-1):
        output_arr[count_arr[arr[i] - min_ele]-1] = arr[i]

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
 
    return arr

arr = [-5, -10, 0, -3, 8, 5, -1, 10]
ans = count_sort(arr)
print("Sorted character array is " + str(ans))