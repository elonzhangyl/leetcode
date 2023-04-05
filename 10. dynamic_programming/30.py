class Solution:
    def rob(self, nums):
        dp_1 = self.rob_basic(nums[:-1])
        dp_2 = self.rob_basic(nums[1:])
        return max(dp_1, dp_2)


    def rob_basic(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]



print(Solution().rob([1]))