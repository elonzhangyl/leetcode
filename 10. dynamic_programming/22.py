w = [1,2]
c = 2
# dp[i][j] means the number of methods to arrive the jth step using range(0, i+1) w
# dp[i][j] = dp[i - 1][j] + dp[i][j - w[i]]

dp  = [[0] * len(w)]*(c + 1)
dp[0][0] = 1
for j in range(c + 1):
    for i in range(len(w)):
        if j >= w[i]:
            dp[i][j] = dp[i-1][j] + dp[i][j - w[i]]

print(dp[-1])