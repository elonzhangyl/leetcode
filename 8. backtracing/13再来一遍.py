
class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def subset(self, nums):
        self.record = [False] * len(nums)
        self.backtracking(0, nums)
        return self.res

    def backtracking(self, start, nums):
        if len(self.path) >= 2:
            self.res.append(self.path[:])

        record = set()
        for i in range(start, len(nums)):
            if self.path and nums[i] < self.path[-1]:
                continue
            if nums[i] in record:
                continue
            record.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(i+1, nums)
            self.path.pop()

print(Solution().subset([4,7,6,7]))