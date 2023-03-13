class Solution:
    def question(self, nums, target):
        dp = [[0] * (target + 1) for _ in range(len(nums))]
        for i in range(target + 1):
            dp[0][i] = 1
        for i in range(1, len(nums)):
            for j in range(target + 1):
                for k in range(i + 1):
                    if j >= nums[k]:
                        dp[i][j] = dp[i][j] + dp[i][j - nums[k]] 
                    else:
                        dp[i][j] = dp[i - 1][j]
        return dp

print(Solution().question([1,2,3], 4))