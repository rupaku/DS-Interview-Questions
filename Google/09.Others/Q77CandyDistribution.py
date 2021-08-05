'''
https://leetcode.com/problems/candy/submissions/
https://www.youtube.com/watch?v=h6_lIwZYHQw

allocate all with 1 candy
from left to right compare 2nd value with first ,if current rating < prev, update rating with +1
from backward, compare both neighbours and update +1
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        
        #assign all 1 candy
        candies=[1]*n
        #Forward
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        #Backward compare neighbours
        for i in range(n-1,0,-1):
            if ratings[i] < ratings[i-1] and candies[i] >= candies[i-1]:
                candies[i-1]=candies[i]+1
                
        return sum(candies)
        
        