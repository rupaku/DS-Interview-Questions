'''
'''
def power(n):
    if n==0:
        return 1
    return 2 * power(n-1)

if '__name__' == "__main__":
    print(power(4))