class Solution:
    def __init__(self) -> None:
        self.blanks = []
        self.board = None

    def shudu(self, board):
        self.board = board
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    self.blanks.append([i, j])
        self.backtracking(0, len(self.blanks))
        return self.board

    def is_valid(self, row, col, val):
        if val in self.board[row]:
            return False
        for r in range(9):
            if val == self.board[r][col]:
                return False
        for i in range(row // 3 * 3, row // 3 * 3 + 3):
            for j in range(col // 3 * 3, col // 3 * 3 + 3):
                if self.board[i][j] == val:
                    return False
        return True

    def backtracking(self, idx, len_blank):
        if idx == len_blank:
            # self.board = deepcopy(self.board)
            return True
        
        for m in range(1, 10):
            if not self.is_valid(self.blanks[idx][0], self.blanks[idx][1], str(m)):
                continue
            self.board[self.blanks[idx][0]][self.blanks[idx][1]] = str(m)
            if self.backtracking(idx + 1, len_blank):
                return True
            self.board[self.blanks[idx][0]][self.blanks[idx][1]] = '.'

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(Solution().shudu(board))