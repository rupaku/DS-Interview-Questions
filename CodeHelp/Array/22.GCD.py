'''
'''

def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    while (a!=b):
        if a > b:
            a=a-b 
        else:
            b=b-a
    return a

if '__name__' == "__main__":
    a=10
    b=20
    print(gcd(a,b))