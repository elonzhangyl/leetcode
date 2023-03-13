class Solution:
    def count_(self, str_):
        c = 0
        for s in str_:
            if s == '0':
                c += 1
        return [c, len(str_) - c]
    
    def zero_one(self, strs, m, n):
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs))]
        c = self.count_(strs[0])
        for j in range(c[0], m + 1):
            for k in range(c[1], n + 1):
                dp[0][j][k] = 1
        
        for i in range(1, len(strs)):
            c = self.count_(strs[i])
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= c[0] and k >= c[1]:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - c[0]][k - c[1]] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[-1][-1][-1]


print(Solution().zero_one(["10", "0001", "111001", "1", "0"], m = 5, n = 3))