'''
https://leetcode.com/explore/interview/card/google/67/sql-2/3046/
https://www.youtube.com/watch?v=hClCsJDcpSU

start=0,end=0
increment end ++ till we get two keys into dictionary, when we get 3rd key, remove oldest key.
start ++, get max_len
'''
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start=0
        end=0
        max_len=0
        d={}
        while end < len(fruits):
            d[fruits[end]] = end
            if len(d) >=3:
                min_val=min(d.values())
                del d[fruits[min_val]]
                start=min_val+1
            max_len=max(max_len,end-start+1)
            end=end+1
        return max_len
        