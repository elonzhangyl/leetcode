

class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.record = []
        self.layer = -1
        self.record_column = []

    def subset(self, n):
        self.record = [[False] * n for _ in range(n)]
        self.record_column = [False] * n
        self.backtracking(n)
        return self.res

    def backtracking(self, n):
        if len(self.path) == n:
            self.res.append(self.path[:])
            return

        for i in range(1, 10):
            for j in range(1, 10):
                if self.board[i][j] != '.':
                    continue
                for k in range(1, 10):
                    if self.is_valid(i, j, k):
                        self.board[i][j] = str(k)
                        if self.backtracking():
                            return True
                        self.board[i][j] = '.'
                return False
        return True
                    
    
    def is_valid(self, i, j, k):
        cur = str(k)
        for x in range(1, 10):
            if cur == self.board[i][x]:
                return False
        for x in range(1, 10):
            if cur == self.board[x][j]:
                return False
        for x in (i // 3, i // 3 + 3):
            for y in (j // 3, j // 3 + 3):
                if cur == self.board[x][y]:
                    return False
        return True
        




board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(Solution().subset(board))
