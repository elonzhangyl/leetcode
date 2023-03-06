class Solution:
    def findMaximumMoneyEarned(self, cost, x):
        # Write your code here
        dp = [[0] * x for _ in range(len(cost))]
        for i in range(len(cost)):
            dp[0][cost[i]] = 2 ** i
        for i in range(1, len(cost)):
            for j in range(x - cost[i]):
                dp[i][j] = max(dp[i - 1][j], dp[i][j + cost[i]] + 2 ** i)
        return max(max(dp)) % (10**9 + 7)



print(Solution().findMaximumMoneyEarned([3,3,4,1,8], 70))
