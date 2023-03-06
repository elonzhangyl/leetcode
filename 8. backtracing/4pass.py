class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def com_sum(self, nums, n, k):
        self.backtracking(nums, n, k, 0)
        return self.res

    def backtracking(self, nums, n, k, start):
        if len(self.path) == k and sum(self.path) == n:
            self.res.append(self.path[:])
            return

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, n, k, i+1)
            self.path.pop()

print(Solution().com_sum(list(range(1,10)), 9, 3))