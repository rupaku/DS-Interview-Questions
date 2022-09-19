'''
'''
def find_unique(arr):
    ans=0
    for i in range(len(arr)):
        ans=ans^ arr[i]
    return ans

if __name__ == '__main__':
    print(find_unique([1,1,3,4,4]))