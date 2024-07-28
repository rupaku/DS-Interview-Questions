# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150

import re
class Solution:
    def str_rev(ele, s, e):
        while s < e:
           ele[s],ele[e] =ele[e],ele[s]
           s += 1
           e -= 1
    def reverseWords(self, sentence: str) -> str:
        sentence = re.sub(' +', ' ', sentence.strip())

        sentence = list(sentence)
        str_len = len(sentence) - 1

        Solution.str_rev(sentence, 0, str_len)
        start = 0

        for end in range(0, str_len + 1):
            if end == str_len or sentence[end] == ' ':
                end_idx = end if end == str_len else end - 1
                Solution.str_rev(sentence, start, end_idx)
                start = end + 1

        return ''.join(sentence)





