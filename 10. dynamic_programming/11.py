class Solution:
    def backpack(self, c: int, w: list[int], v: list[int]) -> int:
        dp = [[-1 for _ in range(c+1)] for _ in range(len(w))]

        for i in range(c+1):
            if i < w[0]:
                dp[0][i] = 0
            else:
                dp[0][i] = v[0]
        for i in range(len(w)):
            dp[i][0] = 0

        for i in range(len(w)):
            for j in range(c+1):
                if j < w[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
        
        return dp[i][j]

print(Solution().backpack(c = 4, w = [1,3,4], v = [15,20,30]))