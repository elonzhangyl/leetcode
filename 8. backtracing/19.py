
class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.record = []

    def subset(self, nums):
        self.record = [False] * len(nums)
        self.backtracking(nums)
        return self.res

    def backtracking(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return

        for i in range(len(nums)):
            if self.path and nums[i][0] != self.path[-1][1]:
                continue
            if self.record[i] == True:
                continue
            self.path.append(nums[i])
            self.record[i] = True
            self.backtracking(nums)
            self.record[i] = False
            self.path.pop()

print(Solution().subset([["1", "2"], ["1", "3"], ["3", "1"]]))