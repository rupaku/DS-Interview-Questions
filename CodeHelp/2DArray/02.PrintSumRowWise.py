'''
'''
class Solution:

    def row_wise_sum(self,arr,target):
        rows = len(arr);  
        cols = len(arr[0]);  
        
        #Calculates sum of each row of given matrix  
        for i in range(0, rows):  
            sumRow = 0;  
            for j in range(0, cols):  
                sumRow = sumRow + arr[i][j];  
            print("Sum of " + str(i+1) +" row: " + str(sumRow));  
                

if __name__ == "__main__":
    arr = [[3, 12, 9], [5, 2, 89], [90, 45, 22]]
    target = 89
    obj=Solution()
    print(obj.row_wise_sum(arr,target))
