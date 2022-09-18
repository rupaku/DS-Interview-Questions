'''
'''
def power(x, n):
 
    # If x^0 return 1
    if (n == 0):
        return 1
 
    # If we need to find of 0^y
    if (x == 0):
        return 0
 
    # For all other cases
    return x * power(x, n - 1)
 
 
# Driver Code
x = 2
n = 3
 
print(power(x, n))