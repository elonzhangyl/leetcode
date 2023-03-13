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
            self.backtracking(nums[0 : i] + nums[i + 1: len(nums)], k)
            self.path.pop()
    def comb(self, nums):
        self.backtracking(nums, len(nums))
        return self.res
print(Solution().comb([1,2,3]))
