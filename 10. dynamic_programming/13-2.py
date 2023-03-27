class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        if nums[0] < target:
            dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            for j in range(target + 1):
                a = dp[i - 1][j]
                b = False
                if nums[i] <= j:
                    b = dp[i - 1][j - nums[i]]
                dp[i][j] = a or b
        return dp[-1][-1]

print(Solution().canPartition([1,1]))

        