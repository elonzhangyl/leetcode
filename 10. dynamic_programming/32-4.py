# dynamic programming
# dp[i][0] means max profit when day i hold stock
# dp[i][1] means max profit when day i not hold stock
# dp[i][0] = max(dp[i - 1][0], -prices[i])
# dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
# dp[j] = max(dp[j - 1], dp[j - 1] + min(num[:j]) - nums[j])
# dp[0] = 0
# nums = [7,1,5,3,6,4], dp = [0, 0, 0, 4, ]
# 最优子结构没找对，所以写出的动态规划不对，后者说递推关系没找对
# 0 
# 0
prices = [7,1,5,3,6,4]
dp = [[0] * 2 for _ in range(len(prices))]
dp[0][0] = -prices[0]
dp[0][1] = 0
for i in range(1, len(prices)):
    print(f"i={i}")
    dp[i][0] = max(dp[i - 1][0], -prices[i])
    dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])    
    print(dp)
# print(dp[-1])


