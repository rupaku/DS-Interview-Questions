'''
412
four one two
'''

class Solution:
    def say_digit(n,arr):
        if n ==0:
            return
        digit = n%10
        n=n/10
        Solution.say_digit(n,arr)
        print(arr[digit])


if '__name__' == "__main__":
    obj=Solution()
    n=412
    arr=["zero","one","two","three","four","five","six","seven","eight","nine"]
    print(obj.say_digit(n,arr))