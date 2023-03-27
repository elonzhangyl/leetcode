class Solution:
    def lastStoneWeightII(self, stones):
        target = sum(stones) - sum(stones) // 2
        dp = [[0] * (target + 1) for _ in range(len(stones))]
        for j in range(target + 1):
            if j >= stones[0]:
                dp[0][j] = stones[0]
        for i in range(1, len(stones)):
            for j in range(target + 1):
                if j >= stones[i]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i]] + stones[i])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1] - (sum(stones) - dp[-1][-1])

print(Solution().lastStoneWeightII([2,7,4,1,8,1]))