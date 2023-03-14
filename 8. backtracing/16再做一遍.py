
class Solution():
    def __init__(self):
        self.path = []
        self.res = []
        self.len = 0

    def permutation(self, nums):
        nums.sort()
        self.record = [0] * len(nums)
        self.backtracking(nums, len(nums))
        return self.res

    def backtracking(self, nums, k):
        if self.len == k:
            self.res.append(self.path[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.len += 1
            self.path.append(nums[i])
            self.backtracking(nums[0:i]+nums[i+1:], k)
            self.path.pop()
            self.len -= 1

print(Solution().permutation([1,1,2]))