
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def subset(self, nums):
        self.backtracking(nums)
        return self.res

    def backtracking(self, nums):
        if len(nums) == 0:
            return

        for i in range(len(nums)):
            self.path.append(nums[i])
            self.res.append(self.path[:])
            self.backtracking(nums[i+1:])
            self.path.pop()

print(Solution().subset([1,2,3]))