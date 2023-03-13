w = [1, 2, 3] 
c = 4

# dp[j] means the number of solution when target == j
# dp[j] = dp[j] + dp[j - w[i]]
# dp[0] = 1
# first traverse c

dp = [[0] * len(w) for _ in range(c + 1)]
dp[0][0] = 1
for i in range(1, c+1):
    for j in range(len(w)):
        if i >= w[j]:
            dp[i][j] = dp[i][j - 1] + dp[i - w[j]][j - 1]
print(dp)

