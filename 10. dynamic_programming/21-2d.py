class Solution:
    def question(self, nums, target):
        if min(nums) > target:
            return 0
        dp = [[0] * (target + 1) for _ in range(len(nums))]
        for i in range(target + 1):
            if i % nums[0] == 0:
                dp[0][i] = 1
        for j in range(len(nums)):
            dp[j][0] = 1
        for i in range(1, len(nums)):
            for j in range(target + 1):
                for k in range(i + 1):
                    if j >= nums[k]:
                        dp[i][j] = dp[i][j] + dp[i][j - nums[k]]
        return dp

print(Solution().question([3,1,2,4], 4))