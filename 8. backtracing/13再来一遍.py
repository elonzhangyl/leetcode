
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def subset(self, nums):
        nums.sort()
        self.backtracking(nums)
        return self.res

    def backtracking(self, nums):
        self.res.append(self.path[:])
        if len(nums) == 0:
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.path.append(nums[i])
            self.backtracking(nums[i+1:])
            self.path.pop()

print(Solution().subset([1,2,2]))