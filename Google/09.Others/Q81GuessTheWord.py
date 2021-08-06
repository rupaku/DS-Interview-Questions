'''
https://leetcode.com/explore/interview/card/google/66/others-4/3104/

if sum(1 if w[i]==candidate[i] else 0 for i in range(6)) == match
if sum() == match
'''
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
from random import random
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        while True:
            candidate = wordlist[int(random() * len(wordlist))]
            #candidate: any random string from wordlist
            match = master.guess(candidate)
            #print(match)  6
            if match == 6:
                break
            wordlist = [
				w for w in wordlist
				if sum(1 if w[i]==candidate[i] else 0 for i in range(6)) == match
			]