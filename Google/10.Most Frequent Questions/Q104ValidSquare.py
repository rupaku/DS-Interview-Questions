'''
https://leetcode.com/problems/valid-square/submissions/
'''
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        distances = sorted([self.distance(p1, p2), self.distance(p1, p3), self.distance(p1, p4), self.distance(p2, p3), self.distance(p2, p4), self.distance(p3, p4)])
        return distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5] and distances[-1] > distances[0]
    
    def distance(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5