w = [1, 2, 3] 
c = 4

# dp[j] means the number of solution when target == j
# dp[j] = dp[j] + dp[j - w[i]]
# dp[0] = 1
# first traverse c

dp = [0] * (c + 1)
dp[0] = 1
for i in range(1, c+1):
    for j in range(len(w)):
        if i >= w[j]:
            dp[i] += dp[i - w[j]]
print(dp[4])

