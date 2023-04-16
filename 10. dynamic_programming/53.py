class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        res = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if i == j:
                        dp[i][j] = 1
                    elif j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                res = max(res, dp[i][j])
        return res
print(Solution().longestPalindromeSubseq('bbbab'))