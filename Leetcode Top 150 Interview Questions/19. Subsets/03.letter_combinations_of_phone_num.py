# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

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
            possible_letters = letters[digits[index]]
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