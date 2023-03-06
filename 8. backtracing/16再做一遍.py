
class Solution():
    def __init__(self):
        self.path = []
        self.res = []
        self.record = []

    def permutation(self, nums):
        nums.sort()
        self.record = [0] * len(nums)
        self.backtracking(nums)
        return self.res

    def backtracking(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return

        for i in range(len(nums)):
            if self.record[i] == 1:
                continue
            if i > 0 and self.record[i-1] == 1 and nums[i-1] == nums[i]:
                continue
            self.record[i] = 1
            self.path.append(nums[i])
            self.backtracking(nums)
            self.path.pop()
            self.record[i] = 0

print(Solution().permutation([1,1,2]))