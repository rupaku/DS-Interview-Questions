'''
https://www.algoexpert.io/questions/Non-Attacking%20Queens
'''
def nonAttackingQueens(n):
    # Write your code here.
    blockedCol = set()
	blockedUpDiagonals = set()
	blockedDownDiagonals = set()
	return get_num_of_non_attacking_queen_place(0,blockedCol,blockedUpDiagonals,blockedDownDiagonals,n)

def get_num_of_non_attacking_queen_place(row,blockedCol,blockedUpDiagonals,blockedDownDiagonals,board_size):
	if row == board_size:
		return 1
	valid_place = 0
	for col in range(board_size):
		if is_non_attack_place(row,col,blockedCol,blockedUpDiagonals,blockedDownDiagonals):
			place_queen(row,col,blockedCol,blockedUpDiagonals,blockedDownDiagonals)
			valid_place += get_num_of_non_attacking_queen_place(
			row+1,blockedCol,blockedUpDiagonals,blockedDownDiagonals,board_size)
			remove_queen(row,col,blockedCol,blockedUpDiagonals,blockedDownDiagonals)
			
	return valid_place
			
def is_non_attack_place(row,col,blockedCol,blockedUpDiagonals,blockedDownDiagonals):
	if col in blockedCol:
		return False
	if row+ col in blockedUpDiagonals:
		return False
	if row - col in blockedDownDiagonals:
		return False
	return True

def place_queen(row,col,blockedCol,blockedUpDiagonals,blockedDownDiagonals):
	blockedCol.add(col)
	blockedUpDiagonals.add(row+col)
	blockedDownDiagonals.add(row - col)
	
def remove_queen(row,col,blockedCol,blockedUpDiagonals,blockedDownDiagonals):
	blockedCol.remove(col)
	blockedUpDiagonals.remove(row+col)
	blockedDownDiagonals.remove(row - col)
			