'''
https://www.codingninjas.com/codestudio/problems/print-like-a-wave_893268
'''

'''

    Time Complexity : O(N*M)
    Space Complexity : O(N*M)

    Where N denotes the total number of rows and M denote the total number of columns.


'''

def wavePrint(arr, nRows, mCols):
    
    ans = []

    
    #Loop to iterate through the columns given to us.
    for j in range(mCols):
        
        # If the current column is even then we will add the elements from top to bottom.
        if j % 2 == 0:
            
            for i in range(nRows):
                ans.append(arr[i][j])
                
        
        # Else the elements will be add from bottom to top.
        else:
            for i in range(nRows - 1, -1, -1):
                ans.append(arr[i][j])
                
    return ans