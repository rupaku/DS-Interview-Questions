''' Input:
 
nums = [8, 7, 2, 5, 3, 1]
target = 10
 
Output:
 
Pair found (8, 2)
or
Pair found (7, 3)'''

def find_pair(nums,target):
    d={}
    for i,e in enumerate(nums):
        if target- e in d:
            print((nums[d.get(target-e)],nums[i]))
            return 
        d[e]=i
    print('Pair not found')

if __name__ == '__main__':
    print(find_pair([8, 7, 2, 5, 3, 1],10))