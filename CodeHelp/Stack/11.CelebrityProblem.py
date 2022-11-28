'''
https://www.codingninjas.com/codestudio/problems/the-celebrity-problem_982769?leftPanelTab=1
'''
"""
    Time complexity: O(N)
    Space complexity: O(N)
    
    Where ‘N’ is the number of people at the party.
"""

def findCelebrity(n, knows):
    # Create a stack and push all ids in it.
    ids = []
    for i in range(0, n):
        ids.append(i)
    #  Finding celebrity.
    while(len(ids) > 1):
        id1 = ids.pop()
        id2 = ids.pop()
        if knows(id1, id2) == True:
            # Because person with id1 can not be celebrity. 
            ids.append(id2)
        else:
            # Because person with id2 can not be celebrity.
            ids.append(id1)

    celebrity = ids[len(ids)-1]

    knowAny = False
    knownToAll = True
    # Verify whether the celebrity knows any other person.
    for i in range(0, n):
        if knows(celebrity, i) == True:
            knowAny = True
            break

    # Verify whether the celebrity is known to all the other person.
    for i in range(0, n):
        if i != celebrity and knows(i, celebrity) == False:
            knownToAll = False
            break

    if knowAny != False or knownToAll == False:
        # If verificatin failed, then it means there is no celebrity at the party.
        celebrity = -1
    
    return celebrity