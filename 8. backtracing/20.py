from copy import deepcopy
import numpy as np
class Solution:
    def __init__(self):
        self.res = []
        self.col = []
        self.diag = []
        
    def queens(self, n):
        chess = [['.'] * n for _ in range(n)]
        self.backtracking(n, 0, chess)
        res_fit = [[0] * n for _ in range(len(self.res))]
        for i, res in enumerate(self.res):
            for j, row in enumerate(res):
                res_fit[i][j] = ''.join(row)
        return res_fit

    def backtracking(self, n, row, board):
        if row == n:
            self.res.append(deepcopy(board))
            return

        for col in range(n):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtracking(n, row + 1, board)
            board[row][col] = '.'

    def is_valid(self, board, row, col):
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        
        up = row
        left = col
        while up >= 0 and left >= 0:
            if board[up][left] == 'Q':
                return False
            up -= 1
            left -= 1

        up2 = row
        right = col
        while up2 >= 0 and right < len(board):
            if board[up2][right] == 'Q':
                return False
            up2 -= 1
            right += 1

        return True

print(Solution().queens(4))