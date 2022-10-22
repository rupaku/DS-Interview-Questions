'''
https://leetcode.com/problems/count-primes/
'''

class Solution:
    def isPrime(self, n: int) -> int:
        if n <= 1:
            return False
        for i in range(2,n):
            if n%i ==0:
                return False
        return True
    def countPrimes(self, n: int) -> int:
        c=0
        for i in range(2,n):
            if Solution.isPrime(self,i):
                c=c+1
        return c
        