
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def subset(self, nums):
        self.backtracking(0, nums)
        return self.res

    def backtracking(self, start, nums):
        self.res.append(self.path[:])
        if start >= len(nums):
            return

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtracking(i+1, nums)
            self.path.pop()

print(Solution().subset([1,2,3]))