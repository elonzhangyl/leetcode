
class Solution():
    def __init__(self):
        self.path = []
        self.res = []
        self.record = []

    def comb_sum(self, nums, target):
        nums.sort()
        self.record = [0] * len(nums)
        self.backtracking(nums, target, 0)
        return self.res

    def backtracking(self, nums, target, start):
        if start >0 and start < len(nums) and \
            nums[start-1] == nums[start-2] and self.record[start-2] == 0:
            return
        if sum(self.path) == target:
            self.res.append(self.path[:])
            return

        for i in range(start, len(nums)):
            self.record[i] = 1
            self.path.append(nums[i])
            self.backtracking(nums, target, i+1)
            self.path.pop()
            self.record[i] = 0

print(Solution().comb_sum([1,1,2], 3))