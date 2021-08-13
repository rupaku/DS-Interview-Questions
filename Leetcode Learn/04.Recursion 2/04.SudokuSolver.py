'''
https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2796/
'''
# N is the size of the 2D matrix N*N
N = 9

# A utility function to print grid
def printing(arr):
	for i in range(N):
		for j in range(N):
			print(arr[i][j], end = " ")
		print()

# Checks whether it will be
# legal to assign num to the
# given row, col
def isSafe(grid, row, col, num):

	# Check if we find the same num
	# in the similar row , we
	# return false
	for x in range(9):
		if grid[row][x] == num:
			return False

	# Check if we find the same num in
	# the similar column , we
	# return false
	for x in range(9):
		if grid[x][col] == num:
			return False

	# Check if we find the same num in
	# the particular 3*3 matrix,
	# we return false
	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + startRow][j + startCol] == num:
				return False
	return True

# Takes a partially filled-in grid and attempts
# to assign values to all unassigned locations in
# such a way to meet the requirements for
# Sudoku solution (non-duplication across rows,
# columns, and boxes) */
def solveSuduko(grid, row, col):

	# Check if we have reached the 8th
	# row and 9th column (0
	# indexed matrix) , we are
	# returning true to avoid
	# further backtracking
	if (row == N - 1 and col == N):
		return True
	
	# Check if column value becomes 9 ,
	# we move to next row and
	# column start from 0
	if col == N:
		row += 1
		col = 0

	# Check if the current position of
	# the grid already contains
	# value >0, we iterate for next column
	if grid[row][col] > 0:
		return solveSuduko(grid, row, col + 1)
	for num in range(1, N + 1, 1):
	
		# Check if it is safe to place
		# the num (1-9) in the
		# given row ,col ->we
		# move to next column
		if isSafe(grid, row, col, num):
		
			# Assigning the num in
			# the current (row,col)
			# position of the grid
			# and assuming our assigned
			# num in the position
			# is correct
			grid[row][col] = num

			# Checking for next possibility with next
			# column
			if solveSuduko(grid, row, col + 1):
				return True

		# Removing the assigned num ,
		# since our assumption
		# was wrong , and we go for
		# next assumption with
		# diff num value
		grid[row][col] = 0
	return False

# Driver Code

# 0 means unassigned cells
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (solveSuduko(grid, 0, 0)):
	printing(grid)
else:
	print("no solution exists ")

	# This code is contributed by sudhanshgupta2019a

'''from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                    d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
            
        def remove_number(d, row, col):
            """
            Remove a number which didn't lead 
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'    
            
        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            #if not yet    
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)
                
                
        def backtrack(row = 0, col = 0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
                    
        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n ) * n + col // n
        
        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        sudoku_solved = False
        backtrack()'''