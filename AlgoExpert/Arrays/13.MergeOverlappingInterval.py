'''
https://www.algoexpert.io/questions/Merge%20Overlapping%20Intervals
'''
# time O(nlogn) | space O(n)
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sortedIntervals = sorted(intervals,key=lambda x:x[0])
	
	mergedIntervals =[]
	currentInterval = sortedIntervals[0]
	mergedIntervals.append(currentInterval)
	
	for nextInterval in sortedIntervals:
		_,currentIntervalEnd = currentInterval
		nextIntervalStart,nextIntervalEnd = nextInterval
		
		if currentIntervalEnd >= nextIntervalStart:
			currentInterval[1]=max(currentIntervalEnd,nextIntervalEnd)
		else:
			currentInterval = nextInterval
			mergedIntervals.append(currentInterval)
	return mergedIntervals