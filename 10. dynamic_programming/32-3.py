# dynamic programming
# dp[j] means max profit for first j prices
# dp[j] = max(dp[j - 1], dp[j - 1] + min(num[:j]) - nums[j])
# dp[0] = 0
# nums = [7,1,5,3,6,4], dp = [0, 0, 0, 4, ]
# 最优子结构没找对，所以写出的动态规划不对，后者说递推关系没找对
nums = [7,1,5,3,6,4]
dp = [0] * (len(nums) + 1)
for j in range(1, len(nums)):
    dp[j] = max(dp[j - 1], dp[j - 1] + nums[j] - max(nums[:j]))
    print(dp)
print(dp[-1])


