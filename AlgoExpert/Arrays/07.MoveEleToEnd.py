'''
https://www.algoexpert.io/questions/Move%20Element%20To%20End
'''
def moveElementToEnd(array, toMove):
    # Write your code here.
	ls=[]
	ls2=[]
    for i in range(len(array)):
		if array[i] == toMove:
			ls.append(toMove)
		else:
			ls2.append(array[i])
	print(ls2.extend(ls))
	return ls2
			

# Time O(n) | space O(1)
def moveElementToEnd(array,toMove):
	i=0
	j=len(array)-1
	while i < j:
		while i < j and array[j] == toMove:
			j=j-1
		if array[i] == toMove:
			array[i],array[j]=array[j],array[i]
		i=i+1
	return array