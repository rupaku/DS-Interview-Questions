'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/3051/
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return str(int(num1)*int(num2))
    
        l = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,"0":0}
        def co ( a: str):
            i=0
            for v,x in enumerate(a):
                i+= l[x] * (10**(len(a)-v-1))
            return i

        return str(co(num1)* co(num2))