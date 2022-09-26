'''
https://www.codingninjas.com/codestudio/problems/reverse-the-array_1230540?leftPanelTab=2
'''




def reverseArray(arr,start,end,length):
    
    while start < end:
        
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1     

length = int(input())
arr = [int(i) for i in input().split()]

reverseArray(arr,0,length - 1,length)
print(*arr)
