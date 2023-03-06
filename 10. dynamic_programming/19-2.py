

coins = [1,2,5]
amount = 5
dp = [0] * 10
dp[0] = 1

dp = [0]*(amount + 1)
dp[0] = 1
# 遍历物品
for i in range(len(coins)):
    # 遍历背包
    for j in range(coins[i], amount + 1):
        dp[j] += dp[j - coins[i]]
        print(f"j = {j}, i = {i}, dp = {dp}")
