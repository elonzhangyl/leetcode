# https://juejin.cn/post/7172913352820129829
class Solution:
    def question(self, nums, target):
        if min(nums) > target:
            return 0
        dp = [[0] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = 1
        for j in range(0, target + 1):
            for i in range(0, len(nums)):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[-1][j - nums[i - 1]] 
        return dp
    
print(Solution().question([1,2,3], 4))