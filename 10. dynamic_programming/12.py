class Solution:
    def backpack(self, c: int, w: list[int], v: list[int]) -> int:
        dp = [0 for _ in range(c + 1)]
        for j in range(c + 1):
            if j >= w[0]:
                dp[j] = v[0]
        for i in range(1, len(w)):
            for j in range(c, -1, -1):
                if j >= w[i]:
                    dp[j] = max(dp[j], dp[j - w[i]] + v[i])
        return dp[-1]

print(Solution().backpack(c = 4, w = [1,3,4], v = [15,20,30]))