'''
https://www.codingninjas.com/codestudio/problems/rat-in-a-maze_1215030?leftPanelTab=1
'''
'''
    Time complexity: O(3^(N^2))
    Space Complexity: O(N^2)

    where N is the size of array/list ARR.
'''

def isValidMove(y, x, arr, visited):
    
    if x == -1 or x == len(arr) or y == -1 or y == len(arr) or visited[y][x] or arr[y][x] == 0:
        return False
        
    return True

def printPathUtil(arr, y, x, path, pathList, visited):
    
    # This will check the initial point(i.e. (0, 0)) to start the paths.
    if x == -1 or x == len(arr) or y == -1 or y == len(arr) or visited[y][x] or arr[y][x] == 0:
        return
    
    # If reach the last cell (n-1, n-1) then store the path and return.
    if x == len(arr) - 1 and y == len(arr) - 1:
        pathList.append(path)
        return
    
    visited[y][x] = True
    
    # Try for all the 4 directions (down, left, right, up)
    # in the given order to get the paths in lexicographical order.
    
    if isValidMove(y + 1, x, arr, visited):
        path += 'D'
        printPathUtil(arr, y + 1, x, path, pathList, visited)
        path = path[:-1]
    
    if isValidMove(y, x - 1, arr, visited):
        path += 'L'
        printPathUtil(arr, y, x - 1 , path, pathList, visited)
        path = path[:-1]
    
    if isValidMove(y, x + 1, arr, visited):
        path += 'R'
        printPathUtil(arr, y, x + 1 , path, pathList, visited)
        path = path[:-1]
    
    if isValidMove(y - 1, x, arr, visited):
        path += 'U'
        printPathUtil(arr, y - 1, x, path, pathList, visited)
        path = path[:-1]
    
    # Mark the cell as unvisited for other possible paths.
    visited[y][x] = False


def searchMaze(arr, n):

    # List to store all the possible paths.
    possiblePaths = []
    path = ""
    visited = [[False for _ in range(n)]
                      for _ in range(n)]

    printPathUtil(arr, 0, 0, path, possiblePaths, visited)
    
    return possiblePaths
