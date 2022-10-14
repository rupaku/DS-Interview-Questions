'''
'''
class Solution:

    def linear_search_2d(self,arr,target):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == target:
                    return [i,j]
        return [-1,-1]

if __name__ == "__main__":
    arr = [[3, 12, 9], [5, 2, 89], [90, 45, 22]]
    target = 89
    obj=Solution()
    print(obj.linear_search_2d(arr,target))
