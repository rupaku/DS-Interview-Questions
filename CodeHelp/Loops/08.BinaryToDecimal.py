'''
'''


# def binaryToDecimal(binary):
#     decimal, i = 0, 0
#     while(binary != 0):
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary//10
#         i += 1
#     print(decimal)   
 def binaryToDecimal(n):
    ans, i = 0, 0
    while(n != 0):
        digit = n % 10
        if digit == 1:
            ans = ans + pow(2, i)
        n = n//10
        i += 1
    print(ans)     
 
# Driver code
if __name__ == '__main__':
    binaryToDecimal(100)
    binaryToDecimal(101)
    binaryToDecimal(1001)