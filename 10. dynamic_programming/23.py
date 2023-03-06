coins = [1, 2, 5]
amount = 11

# dp[j] means the min number of coins to make amount j
# dp[j] = min(dp[j], dp[j - w[i]] + 1)

dp = [float('inf')] * 12
dp[0] = 0
dp[1] = 1
for i in range(len(coins)):
    for j in range(coins[i], amount+1):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        print(f"i = {i}, j = {j}, dp = {dp}")
print(dp[amount])