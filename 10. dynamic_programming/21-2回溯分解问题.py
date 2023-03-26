class Solution:

    def coinChange(self, coins, amount):
        res = self.dp(coins, amount)
        if res == float('inf'):
            return -1
        else:
            return res

    def dp(self, coins, amount):
        if amount == 0:
            return 0
        elif amount < 0:
            return float('inf')
        res = float('inf')
        for i in range(len(coins)):
            temp_res = self.dp(coins, amount - coins[i])
            res = min(res, temp_res + 1)
        return res

print(Solution().coinChange([2,5,1], 11))