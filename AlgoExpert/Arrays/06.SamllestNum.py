'''
https://www.algoexpert.io/questions/Smallest%20Difference
'''
# Time O(nlogn)+O(mlogm) | space O(1)
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
	arrayTwo.sort()
	idxOne=0
	idxTwo=0
	smallest = float("inf")
	current=float("inf")
	smallestpair=[]
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum=arrayOne[idxOne]
		secNum=arrayTwo[idxTwo]
		if firstNum < secNum:
			current=secNum-firstNum
			idxOne += 1
		elif secNum < firstNum:
			current=firstNum - secNum
			idxTwo += 1
		else:
			return [firstNum,secNum]
		if smallest > current:
			smallest = current
			smallestpair=[firstNum,secNum]
	return smallestpair
