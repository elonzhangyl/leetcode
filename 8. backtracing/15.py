
class Solution():
    def __init__(self):
        self.path = []
        self.res = []
        self.record = []

    def permutation(self, nums):
        self.backtracking(nums)
        return self.res

    def backtracking(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return

        for i in range(len(nums)):
            self.record[i] = 1
            self.path.append(nums[i])
            self.backtracking(nums)
            self.path.pop()
            self.record[i] = 0

print(Solution().permutation([1,2,3]))