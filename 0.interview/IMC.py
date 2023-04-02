class Solution:
    def findMaximumMoneyEarned(self, cost, x):
        # Write your code here
        dp = [0] * (x + 1)
        for i in range(1, len(cost)):
            for j in range(x, cost[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - cost[i]] + 2 ** i)
        return dp[-1] % (10**9 + 7)

print(Solution().findMaximumMoneyEarned([3,3,4,1,8], 70))
