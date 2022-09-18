'''
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        sm=0
        while (n != 0):
            digit = n%10
            product =product*digit
            sm=sm+digit
            n=n//10
        res = product-sm
        return res