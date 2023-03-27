class Solution:
    def lastStoneWeightII(self, stones):
        target = sum(stones) - sum(stones) // 2
        dp = [0] * (target + 1)
        for j in range(target + 1):
            if j >= stones[0]:
                dp[j] = stones[0]
        for i in range(1, len(stones)):
            for j in range(target, -1, -1):
                if j >= stones[i]:
                    dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return dp[-1] - (sum(stones) - dp[-1])

print(Solution().lastStoneWeightII([2,7,4,1,8,1]))