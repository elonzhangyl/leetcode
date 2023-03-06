n = 4
w = [i**2 for i in range(1, n + 1) if i**2 <= n]

# dp[j] means the min number of sq to make the sum n
# dp[j] = min(dp[j], dp[j - w[i]]+1)