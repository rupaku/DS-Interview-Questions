'''
'''
def linear(arr,key):
    for i in arr:
        if key in arr:
            return True
        else:
            return False

if __name__ == '__main__':
    print(linear([1,2,3,4],5))