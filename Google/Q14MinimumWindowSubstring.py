'''
https://leetcode.com/problems/minimum-window-substring/
-- formed -> num of unique alphabets
create filtered list with char which are part of t with index,
start with l and r as 0 index , check in filtered list with t, increment r till we get all string of t in one window, keeping l as 0.
now move l -> repeat until we get smallest window expand r and contract l to include all t in window with smallest frame.

'''

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # S = "ABCDDDDDDEEAFFBC" T = "ABC"
        #filtered_S = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        required= len(dict_t)
        
        #filter s according to t with index
        filtered_s =[]
        for i ,char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i,char))
        l=0
        r=0
        formed=0
        # formed is used to keep track of how many unique characters in t are present in the  current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        
        window_counts={}
        ans = float("inf"),None,None
        #look in filtered list
        while r < len(filtered_s):
            character = filtered_s[r][1] #A
            window_counts[character] = window_counts.get(character,0)+1
            
            #dict_t ({'A': 1, 'B': 1, 'C': 1})
            if window_counts[character] == dict_t[character]:
                formed+=1
                
            # if t is in current window
            while l <=r and formed == required:
                character = filtered_s[l][1] #A
                
                #save smallest window until now
                end= filtered_s[r][0]
                start =filtered_s[l][0]
                if end-start +1 < ans[0]:
                    ans = (end-start+1,start,end)
                    
                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]
                
                
            
        