'''
https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1495/
'''
#using recursion
def fibonacci(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Using Memoization

def fibonacci(self,n):
    cache={}
    def fibo_recur(self,n):
        if n in cache:
            return cache[n]
        if n < 2:
            res=n
        else:
            res=fibo_recur(n-1)+fibo_recur(n-2)
        
        cache[n] =res
        return res
    return fibo_recur(n)