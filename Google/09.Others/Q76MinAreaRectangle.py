'''
https://leetcode.com/explore/interview/card/google/66/others-4/3105/
https://www.youtube.com/watch?v=pFgBZFKJ2Co
find vertical lines which has same start and end in y axis and process in hash
x->key
y-> y list
look for y1,y2 pair from left to right in hashtable
if previous hashtable has same y1,y2 pair then its rectangle
'''
from collections import defaultdict
import sys

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        y_cord=defaultdict(list)
        seen_lines={}
        ans=sys.maxsize
        
        # points [[1,1],[1,3],[3,1],[3,3],[2,2]]
        for x,y in points:
            y_cord[x].append(y)
        print(y_cord) # defaultdict(<class 'list'>, {1: [1, 3], 3: [1, 3], 2: [2]})

        for x in sorted(y_cord):
            y_list=y_cord[x]
            y_list.sort()
            
            print(y_list) 
            #[1, 3]
            #[2]
            #[1, 3]

            for i,y1 in enumerate(y_list):
                for j in range(i):
                    y2=y_list[j]
                    
                    if (y1,y2) in seen_lines:
                        area=(x-seen_lines[(y1,y2)])*(y1-y2)
                        ans=min(ans,area)
                        
                    seen_lines[(y1,y2)] =x
        return ans if ans < sys.maxsize else 0
