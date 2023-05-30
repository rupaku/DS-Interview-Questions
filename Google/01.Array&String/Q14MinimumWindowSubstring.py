'''
https://leetcode.com/problems/minimum-window-substring/
-- formed -> num of unique alphabets
create filtered list with char which are part of t with index,
start with l and r as 0 index , check in filtered list with t, increment r till we get all string of t in one window, keeping l as 0.
now move l -> repeat until we get smallest window expand r and contract l to include all t in window with smallest frame.

'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Struggled with this problem for a long while.
        # Idea: Two pointers: moving end forward to find a valid window,
        #                     moving start forward to find a smaller window
        #                     counter and hash_map to determine if the window is valid or not

        # Count the frequencies for chars in t
        hash_map = dict()
        for c in t:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1

        start, end = 0, 0

        # If the minimal length doesn't change, it means there's no valid window
        min_window_length = len(s) + 1

        # Start point of the minimal window
        min_window_start = 0

        # Works as a counter of how many chars still need to be included in a window
        num_of_chars_to_be_included = len(t)

        while end < len(s):
            # If the current char is desired
            if s[end] in hash_map:
                # Then we decreased the counter, if this char is a "must-have" now, in a sense of critical value
                if hash_map[s[end]] > 0:
                    num_of_chars_to_be_included -= 1
                # And we decrease the hash_map value
                hash_map[s[end]] -= 1

            # If the current window has all the desired chars
            while num_of_chars_to_be_included == 0:
                # See if this window is smaller
                if end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    min_window_start = start

                # if s[start] is desired, we need to update the hash_map value and the counter
                if s[start] in hash_map:
                    hash_map[s[start]] += 1
                    # Still, update the counter only if the current char is "critical"
                    if hash_map[s[start]] > 0:
                        num_of_chars_to_be_included += 1

                # Move start forward to find a smaller window
                start += 1

            # Move end forward to find another valid window
            end += 1

        if min_window_length == len(s) + 1:
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_length]
                
                
            
        
# from collections import Counter
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         # S = "ABCDDDDDDEEAFFBC" T = "ABC"
#         #filtered_S = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
#         if not t or not s:
#             return ""
        
#         dict_t = Counter(t)
#         required= len(dict_t)
        
#         #filter s according to t with index
#         filtered_s =[]
#         for i ,char in enumerate(s):
#             if char in dict_t:
#                 filtered_s.append((i,char))
#         l=0
#         r=0
#         formed=0
#         # formed is used to keep track of how many unique characters in t are present in the  current window in its desired frequency.
#         # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        
#         window_counts={}
#         ans = float("inf"),None,None
#         #look in filtered list
#         while r < len(filtered_s):
#             character = filtered_s[r][1] #A
#             window_counts[character] = window_counts.get(character,0)+1
            
#             #dict_t ({'A': 1, 'B': 1, 'C': 1})
#             if window_counts[character] == dict_t[character]:
#                 formed+=1
                
#             # if t is in current window
#             while l <=r and formed == required:
#                 character = filtered_s[l][1] #A
                
#                 #save smallest window until now
#                 end= filtered_s[r][0]
#                 start =filtered_s[l][0]
#                 if end-start +1 < ans[0]:
#                     ans = (end-start+1,start,end)
                    
#                 window_counts[character] -= 1
#                 if window_counts[character] < dict_t[character]:
#                     formed -= 1
#                 l += 1
#             r += 1
#         return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]
                
                
            
        