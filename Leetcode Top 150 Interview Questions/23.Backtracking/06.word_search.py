# https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows, self.cols = len(board), len(board[0])
        self.board = board
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtracking(row, col, word):
                    return True
                
        return False
    
    
    
    def backtracking(self, row, col, suffix):
        if len(suffix) == 0: return True
        
        if row < 0 or row == self.rows or col < 0 or col == self.cols or self.board[row][col] != suffix[0]:
            return False
        
        
        ret = False
        self.board[row][col] = '#'
        for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ret = self.backtracking(row + row_offset, col + col_offset, suffix[1:])
            if ret: break
                
        self.board[row][col] = suffix[0]
        
        return ret