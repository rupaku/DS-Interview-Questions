'''
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/submissions/
https://www.youtube.com/watch?v=TsA4vbtfCvo
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l=0
        r=len(cardPoints)-k
        total=sum(cardPoints[r:])
        res=total
        while r < len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            res=max(res,total)
            l=l+1
            r=r+1
        return res