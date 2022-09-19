'''
'''

def intersect_array(arr1,arr2):
    m =len(arr1)-1
    n=len(arr2)-1
    res=[]
    i=0
    j=0
    while (i< m and j < n):
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i=i+1
            j=j+1
        elif arr1[i] < arr2[j]:
            i =i +1
        else:
            j=j+1
    return res

if __name__ == '__main__':
    print(intersect_array([1,3,3,6,4],[1]))