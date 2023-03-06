# dynamic programming
# dp[i][0]还没有采取任何操作 （其实我们也可以不设置这个状态）
# dp[i][1]第一次持有股票最大利润
# dp[i][2]第一次不持有股票
# dp[i][3]第二次持有股票
# dp[i][4]第二次不持有股票
prices = [3,3,5,0,0,3,1,4]
dp = [[0] * 5 for _ in range(len(prices))]
dp[0][0] = 0
dp[0][1] = -prices[0]
dp[0][2] = 0
dp[0][3] = 0
dp[0][4] = 0
for i in range(1, len(prices)):
    for j in range(k):
        dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
        dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])
        print(dp)
# print(dp[-1])


