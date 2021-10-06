'''
https://www.algoexpert.io/questions/Spiral%20Traverse
'''
#Time O(n) | space O(n)
def spiralTraverse(array):
    # Write your code here.
    res=[]
	spiralFill(array,0,len(array)-1,0,len(array[0])-1,res)
	return res
	
def spiralFill(array,startRow,endRow,startCol,endCol,res):
	if startRow > endRow or startCol > endCol:
		return
	for col in range(startCol,endCol+1):
		res.append(array[startRow][col])
	for row in range(startRow+1,endRow+1):
		res.append(array[row][endCol])
	for col in reversed(range(startCol,endCol)):
		if startRow == endRow:
			break
		res.append(array[endRow][col])
	for row in reversed(range(startRow+1,endRow)):
		if startCol == endCol:
			break
		res.append(array[row][startCol])
	
	spiralFill(array,startRow+1,endRow-1,startCol+1,endCol-1,res)

