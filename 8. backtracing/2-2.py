class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    def backtracking(self, nums, k):
        if len(self.path) == k:
            self.res.append(self.path[:])
            return
        for i in range(len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums[i + 1: len(nums)], k)
            self.path.pop()
    def comb(self, n, k):
        self.backtracking(list(range(1, n + 1)), k)
        return self.res
print(Solution().comb(3,2))
