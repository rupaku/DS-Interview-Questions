'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
digits="23"
if empty string return []
create dictionary with digit and alphabets
backtrack it with index -> 0 and path -> []
backtract func -> if len path aequals len digits -> append to res with path
find possible letters from letters corresponding to digits index, iterate over it and append to path
backtrack with index+1, path
pop up path


'''
# Using Backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index,path):
            #if path is same as digits - complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            #get letter that current digit maps to and loop them
            possible_letters = letters[digits[index]] # "abc"
            for letter in possible_letters:
                # add letter to current path
                path.append(letter)
                # move on to the next digit
                backtrack(index+1,path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

         # Initiate backtracking with an empty path and starting index of 0
        combinations=[]
        backtrack(0,[])
        return combinations


#using BFS
from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d={1: '', 2: 'abc',3: 'def',4: 'ghi',5: 'jkl',6: 'mno',7: 'pqrs',8: 'tuv',9: 'wxyz'}
        q=deque(d[int(digits[0])]) # 2 -> abc
        # starting with 1 since we want to ignore a
        for i in range(1,len(digits)):
            s=len(q)   #len(abc)  -> 3
            while s:
                res = q.popleft()
                for j in d[int(digits[i])]:
                    q.append(res+j)
                s = s-1
        return q
        