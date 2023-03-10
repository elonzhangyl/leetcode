class Solution:
    def knapsack(self, nums):
        if sum(nums) % 2 != 0:
            return -1
        cap = sum(nums) // 2
        dp = [0 for _ in range(cap + 1)]
        for j in range(nums[0], cap + 1):
            dp[j] = nums[0]
        
        for i in range(1, len(nums)):
            for j in range(cap, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        return dp[-1] == cap

print(Solution().knapsack([1,5,11,5]))

        