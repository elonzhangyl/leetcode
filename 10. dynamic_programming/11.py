class Solution:
    def backpack(self, c: int, w: list[int], v: list[int]) -> int:
        dp = [[0 for _ in range(c + 1)] for _ in range(len(w))]
        for j in range(c + 1):
            if j >= w[0]:
                dp[0][j] = v[0]
        for i in range(1, len(w)):
            for j in range(c + 1):
                if j >= w[i]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

print(Solution().backpack(c = 4, w = [1,3,4], v = [15,20,30]))