'''

https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
o/p Triplet is 4, 8, 10
'''
def find3Numbers(arr, target):
    for i in range(len(arr)-1):
        s=set()
        curr_sum= target-arr[i]
        for j in range(i+1,len(arr)):
            if curr_sum - arr[j] in s:
                print(arr[i],arr[j],curr_sum-arr[j])
                return True
            s.add(arr[j])
            


if __name__ == '__main__':
    print(find3Numbers([1, 4, 45, 6, 10, 8],22))