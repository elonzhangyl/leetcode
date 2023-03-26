class Solution:   

    def coinChange(self, coins, amount):
        recorder = [-666] * (amount + 1)
        res = self.dp(coins, amount, recorder)
        if res == float('inf'):
            return -1
        else:
            return res

    def dp(self, coins, amount, recorder):
        if amount == 0:
            return 0
        elif amount < 0:
            return float('inf')
        if recorder[amount] != -666:
            return recorder[amount]
        res = float('inf')
        for i in range(len(coins)):
            temp_res = self.dp(coins, amount - coins[i], recorder)
            res = min(res, temp_res + 1)
        recorder[amount] = res
        return res

print(Solution().coinChange([2,5,1], 11))