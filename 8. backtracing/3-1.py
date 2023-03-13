class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    def backtracking(self, nums, n, k):
        if sum(self.path[:]) > n:
            return
        if len(self.path[:]) == k:
            if sum(self.path[:]) == n:
                self.res.append(self.path[:])
            return
        for i in range(len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums[i + 1: len(nums)], n, k)
            self.path.pop()
    def comb(self, n, k):
        self.backtracking(list(range(1, 10)), n, k)
        return self.res
print(Solution().comb(7,3))
