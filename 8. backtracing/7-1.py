class Solution:
    def __init__(self):
        self.sum = 0
        self.path = []
        self.res = []

    def finder(self, candidates, target):
        self.backtracking(candidates, target, 0)
        return self.res


    def backtracking(self, candidates, target, idx):
        if idx > len(candidates)-1:
            return
        if self.sum == target:
            self.res.append(self.path[:])
            return


        for candidate in candidates[:]:
            self.path.append(candidate)
            self.sum += candidate
            self.backtracking(candidates, target, idx + 1)
            self.path.pop()
            self.sum -= candidate

print(Solution().finder(candidates = [7,3,6,2], target = 7))