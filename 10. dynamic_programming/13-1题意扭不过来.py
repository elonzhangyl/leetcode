class Solution:
    def knapsack(self, nums):
        if sum(nums) % 2 != 0:
            return -1
        cap = sum(nums) // 2
        dp = [[0 for _ in range(cap + 1)] for _ in range(len(nums))]
        for j in range(cap + 1):
            if j >= nums[0]:
                dp[0][j] = nums[0]
        
        for i in range(1, len(nums)):
            for j in range(cap + 1):
                if j >= nums[i]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1] == cap

print(Solution().knapsack([1,5,11,5]))

        