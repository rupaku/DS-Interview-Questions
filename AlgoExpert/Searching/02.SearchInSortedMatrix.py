'''
https://www.algoexpert.io/questions/Search%20In%20Sorted%20Matrix
'''
#Time O(n+m) | space O(1)
def searchInSortedMatrix(matrix, target):
    # Write your code here.
    row=0
	col=len(matrix[0])-1
	while row < len(matrix) and col >= 0:
		if matrix[row][col] > target:
			col = col -1 #move left
		elif matrix[row][col] < target:
			row = row +1 # move down
		else:
			return [row,col]
	return [-1,-1]
