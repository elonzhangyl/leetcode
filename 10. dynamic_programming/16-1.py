class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        if (target + sum(nums)) % 2 != 0:
            return 0
        cap = (target + sum(nums)) // 2
        dp = [[0] * (cap + 1) for _ in range(len(nums))]
        for j in range(cap + 1):
            if j <= nums[0]:
                dp[0][j] = 1
        for i in range(1, len(nums)):
            for j in range(cap + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1))