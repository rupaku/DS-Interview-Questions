'''
check if num is prime or not
'''

class Prime:
    def prime_num(self,n):
        isPrime=0
        for i in range(2,n):
            if n%i == 0:
                print("not prime")
                isPrime=1
                break
        if isPrime == 0:
            print("prime")
        else:
            print("Not prime")


obj=Prime()
n=4
obj.prime_num(n)