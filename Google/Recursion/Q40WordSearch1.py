'''
https://leetcode.com/problems/word-search/
https://www.youtube.com/watch?v=X0kX7PMOYi0
'''
class Solution:
    def search(self, i, j, idx):
        if idx == len(self.word) - 1: return True
        #visited True
        self.board[i][j] = chr(ord(self.board[i][j]) - 65)
        # i-1
        if i > 0 and self.board[i-1][j] == self.word[idx+1] and self.search(i-1, j, idx+1): return True
        #j-1
        if j > 0 and self.board[i][j-1] == self.word[idx+1] and self.search(i, j-1, idx+1): return True
        #i+1
        if i < len(self.board)-1 and self.board[i+1][j] == self.word[idx+1] and self.search(i+1, j, idx+1): return True
        # j+1
        if j < len(self.board[0])-1 and self.board[i][j+1] == self.word[idx+1] and self.search(i, j+1, idx+1): return True
        #visited False
        self.board[i][j] = chr(ord(self.board[i][j]) + 65)
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        if r == 0: return False
        c = len(board[0])
        self.board = board
        self.word = word
        for i in range(r):
            for j in range(c):
                # check if first char of word matches
                if board[i][j] == word[0] and self.search(i, j, 0): return True
        return False