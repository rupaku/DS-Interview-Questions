'''
https://leetcode.com/problems/intersection-of-three-sorted-arrays/submissions/

Algorithm

Initiate three pointers p1, p2, p3, and place them at the beginning of arr1, arr2, arr3 by initializing them to 0;
while they are within the boundaries:
if arr1[p1] == arr2[p2] && arr2[p2] == arr3[p3], we should store it because it appears three times in arr1, arr2, and arr3;
else
if arr1[p1] < arr2[p2], move the smaller one, i.e., p1;
else if arr2[p2] < arr3[p3], move the smaller one, i.e., p2;
if neither of the above conditions is met, it means arr1[p1] >= arr2[p2] && arr2[p2] >= arr3[p3], therefore move p3.
'''
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        '''Method 1
        res=[]
        counter=collections.COunter(arr1+arr2+arr3)
        
        for item in counter:
            if counter[item] == 3:
                res.append(item)
        return res
        '''
        res=[]
        p1=p2=p3=0
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                res.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1
        return res
        