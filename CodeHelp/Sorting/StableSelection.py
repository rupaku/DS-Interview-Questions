'''
'''
def stableSelectionSort(a, n):
     
    # Traverse through all array elements
    for i in range(n):
 
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
 
        # Move minimum element at current i
        key = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
            
        a[i] = key