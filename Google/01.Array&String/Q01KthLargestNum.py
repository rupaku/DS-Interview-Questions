'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/361/
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Approach 1
        # nums.sort()
        # return nums[::-1][k-1]
        #Approach 2
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Approach 1
        # nums.sort()
        # return nums[::-1][k-1]
        #Approach 2
        def partition(l,r,p_index):
            p= nums[p_index]
            nums[p_index],nums[r] = nums[r],nums[p_index]
            store_index=l
            for i in range(l,r):
                if nums[i] < p:
                    nums[store_index],nums[i]=nums[i],nums[store_index]
                    store_index +=1
            nums[r],nums[store_index] = nums[store_index],nums[r]
            return store_index

        def select(l,r,k_smallest):
            if l == r:
                return nums[l]
            p_index= random.randint(l,r)
            p_index= partition(l,r,p_index)
            if k_smallest == p_index:
                return nums[k_smallest]
            elif k_smallest < p_index:
                return select(l,p_index-1,k_smallest)
            else:
                return select(p_index+1, r, k_smallest)
        return select(0,len(nums)-1,len(nums)-k)

obj = Solution()
obj.findKthLargest([3,2,3,1,2,4,5,5,6],4)