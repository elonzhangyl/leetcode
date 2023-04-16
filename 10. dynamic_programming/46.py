class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0
        res = 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])
        return res
    
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))