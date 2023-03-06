
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

        for i in range(n):
            if self.record_column[i] == True:
                continue
            if i >= 1 and self.record[self.layer][i-1] == True:
                continue
            if i <= n - 2 and self.record[self.layer][i+1] == True:
                continue
            self.path.append(i)
            self.layer += 1
            self.record_column[i] = True
            self.record[self.layer][i] = True
            self.backtracking(n)
            self.record[self.layer][i] = False
            self.record_column[i] = False
            self.layer -= 1
            self.path.pop()

print(Solution().subset(1))