class Solution:
    def target_sum(self, nums, target):
        # if sum(nums) < target or (sum(nums) + target) % 2 != 0:
        #     return 0
        cap = 11
        dp = [0] * (cap + 1)
        for i in range(nums[0] + 1):
            dp[i] = 1
        for i in range(1, len(nums)):
            for j in range(cap, -1, -1):
                dp[j] += dp[j - nums[i]]

        return dp
print(Solution().target_sum([1,5,11,5], 11))