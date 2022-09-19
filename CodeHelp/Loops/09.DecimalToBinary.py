'''
'''
# def decimalToBinary(n):
 
#     if(n > 1):
#         # divide with integral result
#         # (discard remainder)
#         decimalToBinary(n//2)
 
     
#     print(n%2, end=' ')
     
def decimalToBinary(n): 
    i=0  
    ans=0
    while n !=0:
        bit=n & 1 # any num & 1== 1 , it means odd else even
        ans= (bit*pow(10,i) ) +ans
        n = n >> 1 #right shify by 1 to get next bit
        i = i + 1
 
# Driver code
if __name__ == '__main__':
    decimalToBinary(8)
    print("\n")
    decimalToBinary(18)
    print("\n")
    decimalToBinary(7)
    print("\n")
  
