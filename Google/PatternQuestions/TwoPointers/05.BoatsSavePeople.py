'''https://leetcode.com/problems/boats-to-save-people/description/'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low=0
        high=len(people)-1
        cnt=0
        while low <= high:
            num=people[low]+people[high]
            if num <= limit:
                low=low+1
                high=high-1
            else:
                high=high-1
            cnt=cnt+1
        return cnt