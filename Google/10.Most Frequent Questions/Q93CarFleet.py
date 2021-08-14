'''
https://leetcode.com/problems/car-fleet/submissions/
https://www.youtube.com/watch?v=m_x3VrhXdnk

sort and zip it ,from reverse find arrival time as (target-position)/speed , if its greater than stack top , append it to stack
'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed))
        n=len(cars)
        stack=[]
        for i in range(n-1,-1,-1):
            p,s=cars[i]
            arrival_time=(target-p)/s
            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
        return len(stack)
        