#https://www.educative.io/courses/grokking-coding-interview-patterns-python/solution-interval-list-intersections

# First list = [[2, 6], [7, 9], [10, 13], [14, 19], [20, 24]]

# Second list = [[1, 4], [6, 8], [15, 18]]



def interval_intersect(list1,list2):
    intersection=[]
    i=0
    j=0
    while i < len(list1) and j < len(list2):
        start=max(list1[i][0], list2[j][0])
        end=min(list1[i][1], list2[j][1])

        if start <= end:
            intersection.append([start,end])

        if list1[i][1] < list2[j][1]:
            i =i+1
        else:
            j=j+1
    return intersection
