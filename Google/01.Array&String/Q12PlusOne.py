'''
https://leetcode.com/problems/plus-one/submissions/
from last, if 9 replace with zero, else +1
if all 9 , replace all 9 with 0 and append 1 at start of list
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n):
            index=n-1-i #last element
            #If 9 replace with 0
            if digits[index] == 9:
                digits[index] =0
            else:
                digits[index] +=1
                return digits
        return [1]+digits
        