
coins = [1,2,5]
amount = 5
dp = [0] * 10
dp[0] = 1
for j in range(amount+1):
    for i in range(len(coins)):
        if j >= coins[i]:
            dp[j] += dp[j - coins[i]]
            print(f"j = {j}, i = {i}, dp = {dp}")