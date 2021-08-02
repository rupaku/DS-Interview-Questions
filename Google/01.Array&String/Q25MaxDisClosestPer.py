'''
https://leetcode.com/problems/maximize-distance-to-closest-person/submissions/
https://www.youtube.com/watch?v=93LkD_YwU8M
start wth 0 index , if seat == 1, prev_seat=None , dist ->i else find max(dist, (currentindex-prev_seatIndex)//2)
assign prev_seat to current
handle rightmost person as 1 to length of seats -prev seat
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_seat=None
        dist=float('-inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                if prev_seat==None:
                    dist=i
                else:
                    # currentIndex-prevPersonIndex//2
                    dist=max(dist,(i-prev_seat)//2)
                prev_seat=i
        # Righmost person
        dist = max(dist,len(seats)-1-prev_seat)
        return dist
                
                