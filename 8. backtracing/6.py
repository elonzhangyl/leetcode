class Solution:
    def __init__(self) -> None:
        self.sum = 0
        self.path = []
        self.res = []
        
    def combine_sum(self, nums, target):
        if self.sum == target:
            self.res.append(self.path[:])
            return
        if self.sum > target:
            return

        for num in nums:
            self.path.append(num)
            self.sum += num
            self.combine_sum(nums, target)
            self.path.pop()
            self.sum -= num

s = Solution()
s.combine_sum([2,3,5],8)