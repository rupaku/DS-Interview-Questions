'''
'''
class Solution:

    def largest_col_wise_sum(self,arr,target):
        rows = len(arr);  
        cols = len(arr[0]);  
        
        #Calculates sum of each row of given matrix  
        maxSum =-99999
        row_index=-1
        for i in range(0, rows):  
            sumRow = 0;  
            for j in range(0, cols):  
                sumRow = sumRow + arr[j][i];  
            if sumRow > maxSum:
                maxSum=sumRow
                row_index=i

        print(maxSum, row_index)
                

if __name__ == "__main__":
    arr = [[3, 12, 9], [5, 2, 89], [90, 45, 22]]
    target = 89
    obj=Solution()
    print(obj.largest_col_wise_sum(arr,target))
