
class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.record = []

    def subset(self, nums):
        nums.sort()
        self.record = [False] * len(nums)
        self.backtracking(0, nums)
        return self.res

    def backtracking(self, start, nums):
        self.res.append(self.path[:])
        if start >= len(nums):
            return

        for i in range(start, len(nums)):
            if nums[i] == nums[i - 1] and self.record[i - 1] == False:
                continue
            self.record[i] = True
            self.path.append(nums[i])
            self.backtracking(i+1, nums)
            self.path.pop()
            self.record[i] = False

print(Solution().subset([1,2,2]))