'''
Fibonacci Series using For loop
'''

class Fibonacci:
    def fibo(self,a,b):
        print(a)
        print(b)
        n=6
        for i in range(1,n):
            c=a+b
            print(c)
            a=b
            b=c



obj=Fibonacci()
a=0
b=1
print(obj.fibo(a,b))